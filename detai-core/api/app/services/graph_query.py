from __future__ import annotations

import logging
from dataclasses import dataclass

import psycopg

from app.core.config import get_settings
from app.schemas.graph import (
    GraphEdge,
    GraphFiltersApplied,
    GraphMeta,
    GraphNode,
    GraphResponse,
    GraphYearsFilter,
)

logger = logging.getLogger(__name__)


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

    def _build_doc_filter_sql(self, filters: GraphFilters) -> tuple[str, list[object]]:
        clauses: list[str] = []
        params: list[object] = []

        if filters.channels:
            clauses.append('dm.channels && %s::text[]')
            params.append(filters.channels)
        if filters.authors:
            clauses.append('dm.authors && %s::text[]')
            params.append(filters.authors)
        if filters.rubric_ids:
            clauses.append('dm.rubric_ids && %s::text[]')
            params.append(filters.rubric_ids)
        if filters.category_ids:
            clauses.append('dm.category_ids && %s::text[]')
            params.append(filters.category_ids)
        if filters.year_from is not None:
            clauses.append('dm.year >= %s')
            params.append(filters.year_from)
        if filters.year_to is not None:
            clauses.append('dm.year <= %s')
            params.append(filters.year_to)

        where_sql = ''
        if clauses:
            where_sql = 'WHERE ' + ' AND '.join(clauses)

        return where_sql, params

    def fetch_graph(self, filters: GraphFilters) -> GraphResponse:
        where_sql, where_params = self._build_doc_filter_sql(filters)

        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    f'''
                    SELECT dm.doc_id
                    FROM knowledge.doc_metadata dm
                    {where_sql}
                    ORDER BY dm.updated_at DESC, dm.doc_id
                    LIMIT %s;
                    ''',
                    [*where_params, filters.limit_nodes + 1],
                )
                filtered_doc_ids_raw = [str(row[0]) for row in cur.fetchall()]
                truncated = len(filtered_doc_ids_raw) > filters.limit_nodes
                filtered_doc_ids = filtered_doc_ids_raw[: filters.limit_nodes]

                if not filtered_doc_ids:
                    return GraphResponse(
                        nodes=[],
                        edges=[],
                        meta=GraphMeta(
                            filters_applied=GraphFiltersApplied(
                                channels=list(filters.channels or []),
                                years=GraphYearsFilter(from_=filters.year_from, to=filters.year_to),
                                authors=list(filters.authors or []),
                                rubric_ids=list(filters.rubric_ids or []),
                                category_ids=list(filters.category_ids or []),
                                limit_nodes=filters.limit_nodes,
                            ),
                            total_nodes=0,
                            total_edges=0,
                            truncated=truncated,
                        ),
                    )

                cur.execute(
                    '''
                    SELECT dm.doc_id, dm.doc_type, dm.meta->>'title' AS title, dm.year, dm.channels, dm.rubric_ids, dm.category_ids, dm.authors, dm.meta
                    FROM knowledge.doc_metadata dm
                    WHERE dm.doc_id = ANY(%s)
                    ORDER BY dm.doc_id;
                    ''',
                    (filtered_doc_ids,),
                )
                node_rows = cur.fetchall()

                cur.execute(
                    '''
                    SELECT e.source_id::text, e.target_id::text, MAX(e.weight)::float8 AS weight
                    FROM knowledge.similarity_edges e
                    INNER JOIN knowledge.doc_metadata s ON s.doc_id = e.source_id
                    INNER JOIN knowledge.doc_metadata t ON t.doc_id = e.target_id
                    WHERE e.source_id = ANY(%s) AND e.target_id = ANY(%s)
                    GROUP BY e.source_id, e.target_id
                    ORDER BY e.source_id, e.target_id, weight DESC;
                    ''',
                    (filtered_doc_ids, filtered_doc_ids),
                )
                edge_rows = cur.fetchall()

                cur.execute(
                    '''
                    SELECT count(*)
                    FROM knowledge.similarity_edges e
                    LEFT JOIN knowledge.doc_metadata s ON s.doc_id = e.source_id
                    LEFT JOIN knowledge.doc_metadata t ON t.doc_id = e.target_id
                    WHERE (e.source_id = ANY(%s) OR e.target_id = ANY(%s))
                      AND (s.doc_id IS NULL OR t.doc_id IS NULL);
                    ''',
                    (filtered_doc_ids, filtered_doc_ids),
                )
                data_gap_count = int(cur.fetchone()[0])
                if data_gap_count > 0:
                    logger.warning('data_gap detected in /v1/graph: edges_without_metadata=%s', data_gap_count)

        nodes = [
            GraphNode(
                id=str(doc_id),
                type=str(doc_type or 'publish-post'),
                label=(title or str(doc_id)),
                year=year,
                channels=list(channels or []),
                rubric_ids=list(rubric_ids or []),
                category_ids=list(category_ids or []),
                authors=list(authors or []),
                meta=dict(meta or {}),
            )
            for doc_id, doc_type, title, year, channels, rubric_ids, category_ids, authors, meta in node_rows
        ]
        edges = [
            GraphEdge(
                source=str(source_id),
                target=str(target_id),
                type='SIMILAR_UNDIRECTED',
                weight=float(weight),
                meta={},
            )
            for source_id, target_id, weight in edge_rows
        ]

        return GraphResponse(
            nodes=nodes,
            edges=edges,
            meta=GraphMeta(
                filters_applied=GraphFiltersApplied(
                    channels=list(filters.channels or []),
                    years=GraphYearsFilter(from_=filters.year_from, to=filters.year_to),
                    authors=list(filters.authors or []),
                    rubric_ids=list(filters.rubric_ids or []),
                    category_ids=list(filters.category_ids or []),
                    limit_nodes=filters.limit_nodes,
                ),
                total_nodes=len(nodes),
                total_edges=len(edges),
                truncated=truncated,
            ),
        )
