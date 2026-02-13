import os
import sys
import unittest
from pathlib import Path

from fastapi.testclient import TestClient


class GraphApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.environ.setdefault('DATABASE_URL', 'postgresql://test:test@localhost:5432/test')
        api_dir = Path(__file__).resolve().parents[1] / 'api'
        if str(api_dir) not in sys.path:
            sys.path.insert(0, str(api_dir))

        from app.main import app  # pylint: disable=import-outside-toplevel
        from app.schemas.graph import (
            GraphEdge,
            GraphFiltersApplied,
            GraphMeta,
            GraphNode,
            GraphResponse,
            GraphYearsFilter,
        )
        from app.routers import graph as graph_router  # pylint: disable=import-outside-toplevel

        cls.app = app
        cls.client = TestClient(app)
        cls.graph_router = graph_router
        cls.GraphResponse = GraphResponse
        cls.GraphNode = GraphNode
        cls.GraphEdge = GraphEdge
        cls.GraphMeta = GraphMeta
        cls.GraphFiltersApplied = GraphFiltersApplied
        cls.GraphYearsFilter = GraphYearsFilter

    def test_health_check(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')

    def test_graph_happy_path(self):
        def fake_fetch_graph(filters):
            return self.GraphResponse(
                nodes=[
                    self.GraphNode(
                        id='post-1',
                        type='publish-post',
                        label='post-1',
                        year=2024,
                        channels=['site'],
                        rubric_ids=['core'],
                        category_ids=['ecosystem'],
                        authors=['detai'],
                        meta={},
                    )
                ],
                edges=[
                    self.GraphEdge(
                        source='post-1',
                        target='post-2',
                        type='SIMILAR_UNDIRECTED',
                        weight=0.9,
                        meta={},
                    )
                ],
                meta=self.GraphMeta(
                    filters_applied=self.GraphFiltersApplied(
                        channels=list(filters.channels or []),
                        years=self.GraphYearsFilter(from_=filters.year_from, to=filters.year_to),
                        authors=list(filters.authors or []),
                        rubric_ids=list(filters.rubric_ids or []),
                        category_ids=list(filters.category_ids or []),
                        limit_nodes=filters.limit_nodes,
                    ),
                    total_nodes=1,
                    total_edges=1,
                    truncated=False,
                ),
            )

        original = self.graph_router.service.fetch_graph
        self.graph_router.service.fetch_graph = fake_fetch_graph
        try:
            response = self.client.get('/v1/graph?channels=site&limit_nodes=5')
            self.assertEqual(response.status_code, 200)
            body = response.json()
            self.assertEqual(body['nodes'][0]['id'], 'post-1')
            self.assertEqual(body['meta']['total_nodes'], 1)
        finally:
            self.graph_router.service.fetch_graph = original

    def test_graph_filter_channels(self):
        captured = {}

        def fake_fetch_graph(filters):
            captured['channels'] = filters.channels
            return self.GraphResponse(nodes=[], edges=[], meta=self.GraphMeta(
                filters_applied=self.GraphFiltersApplied(
                    channels=list(filters.channels or []),
                    years=self.GraphYearsFilter(from_=filters.year_from, to=filters.year_to),
                    authors=[], rubric_ids=[], category_ids=[], limit_nodes=filters.limit_nodes,
                ),
                total_nodes=0,
                total_edges=0,
                truncated=False,
            ))

        original = self.graph_router.service.fetch_graph
        self.graph_router.service.fetch_graph = fake_fetch_graph
        try:
            response = self.client.get('/v1/graph?channels=site&channels=telegram')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(captured['channels'], ['site', 'telegram'])
        finally:
            self.graph_router.service.fetch_graph = original

    def test_graph_limit_nodes_truncation(self):
        def fake_fetch_graph(filters):
            return self.GraphResponse(nodes=[], edges=[], meta=self.GraphMeta(
                filters_applied=self.GraphFiltersApplied(
                    channels=[],
                    years=self.GraphYearsFilter(from_=None, to=None),
                    authors=[], rubric_ids=[], category_ids=[], limit_nodes=filters.limit_nodes,
                ),
                total_nodes=filters.limit_nodes,
                total_edges=0,
                truncated=True,
            ))

        original = self.graph_router.service.fetch_graph
        self.graph_router.service.fetch_graph = fake_fetch_graph
        try:
            response = self.client.get('/v1/graph?limit_nodes=2')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.json()['meta']['truncated'])
        finally:
            self.graph_router.service.fetch_graph = original

    def test_graph_invalid_query_params(self):
        response = self.client.get('/v1/graph?year_from=2025&year_to=2024')
        self.assertEqual(response.status_code, 422)

        response = self.client.get('/v1/graph?channels=')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
