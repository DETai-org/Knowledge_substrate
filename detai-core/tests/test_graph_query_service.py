import os
import sys
import unittest
from pathlib import Path


class FakeCursor:
    def __init__(self, scripted_results):
        self.scripted_results = list(scripted_results)
        self.executed_sql = []
        self._current = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def execute(self, sql, params=None):
        self.executed_sql.append((sql, params))
        if not self.scripted_results:
            raise AssertionError('No scripted result for execute call')
        self._current = self.scripted_results.pop(0)

    def fetchall(self):
        if self._current is None:
            raise AssertionError('fetchall without execute')
        return self._current

    def fetchone(self):
        if self._current is None:
            raise AssertionError('fetchone without execute')
        if not self._current:
            return None
        return self._current[0]


class FakeConnection:
    def __init__(self, cursor):
        self._cursor = cursor

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def cursor(self):
        return self._cursor


class GraphQueryServiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.environ.setdefault('DATABASE_URL', 'postgresql://test:test@localhost:5432/test')
        api_dir = Path(__file__).resolve().parents[1] / 'api'
        if str(api_dir) not in sys.path:
            sys.path.insert(0, str(api_dir))

        from app.services.graph_query import GraphFilters, GraphQueryService  # pylint: disable=import-outside-toplevel

        cls.GraphFilters = GraphFilters
        cls.GraphQueryService = GraphQueryService

    def test_fetch_graph_global_returns_edge_and_fallback_node_when_metadata_missing(self):
        # 1) filtered ids, 2) nodes by filter, 3) edges, 4) supplemental nodes, 5) data_gap
        scripted_results = [
            [('post-1',)],
            [('post-1', 'publish-post', 'Post 1', 2024, ['site'], [], [], [], {'title': 'Post 1'})],
            [('post-1', 'post-2', 0.91)],
            [],
            [(1,)],
        ]
        fake_cursor = FakeCursor(scripted_results)
        service = self.GraphQueryService()
        service._connect = lambda: FakeConnection(fake_cursor)  # type: ignore[method-assign]

        result = service.fetch_graph(self.GraphFilters(edge_scope='global', limit_nodes=5))

        node_by_id = {node.id: node for node in result.nodes}
        self.assertIn('post-1', node_by_id)
        self.assertIn('post-2', node_by_id)
        self.assertEqual(node_by_id['post-2'].type, 'unknown')
        self.assertEqual(node_by_id['post-2'].label, 'post-2')
        self.assertEqual(len(result.edges), 1)
        self.assertEqual(result.edges[0].source, 'post-1')
        self.assertEqual(result.edges[0].target, 'post-2')

        edge_query_sql = fake_cursor.executed_sql[2][0]
        self.assertIn('LEFT JOIN knowledge.doc_metadata s ON s.doc_id = e.source_id', edge_query_sql)
        self.assertIn('LEFT JOIN knowledge.doc_metadata t ON t.doc_id = e.target_id', edge_query_sql)


if __name__ == '__main__':
    unittest.main()
