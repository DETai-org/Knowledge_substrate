from __future__ import annotations

from dataclasses import dataclass

import psycopg

from app.core.config import get_settings
from app.schemas.graph import GraphEdge, GraphMeta, GraphNode, GraphResponse


@dataclass
class GraphFilters:
    channels: list[str] | None = None
    year_from: int | None = None
    year_to: int | None = None
    rubric_ids: list[str] | None = None
    category_ids: list[str] | None = None
    authors: list[str] | None = None
    limit_nodes: int = 100


class GraphQueryService:
    def __init__(self) -> None:
        self._settings = get_settings()

    def _connect(self):
        return psycopg.connect(self._settings.database_url)

    def fetch_graph(self, filters: GraphFilters) -> GraphResponse:
        # Базовый v1-запрос: выбираем ограниченный набор рёбер и связанных узлов.
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT source_id::text, target_id::text, weight
                    FROM knowledge.similarity_edges
                    ORDER BY weight DESC, source_id, target_id
                    LIMIT %s;
                    """,
                    (filters.limit_nodes,),
                )
                edge_rows = cur.fetchall()

        nodes_map: dict[str, GraphNode] = {}
        edges: list[GraphEdge] = []

        for source_id, target_id, weight in edge_rows:
            source_key = str(source_id)
            target_key = str(target_id)
            nodes_map.setdefault(source_key, GraphNode(id=source_key))
            nodes_map.setdefault(target_key, GraphNode(id=target_key))
            edges.append(GraphEdge(source=source_key, target=target_key, weight=float(weight)))

        nodes = sorted(nodes_map.values(), key=lambda item: item.id)
        edges = sorted(edges, key=lambda item: (item.source, item.target, -item.weight))

        return GraphResponse(
            nodes=nodes,
            edges=edges,
            meta=GraphMeta(
                limit_nodes=filters.limit_nodes,
                nodes_count=len(nodes),
                edges_count=len(edges),
                truncated=len(edges) >= filters.limit_nodes,
            ),
        )
