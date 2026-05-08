from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Literal

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
    edge_scope: Literal['local', 'global'] = 'local'


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
        is_global_scope = filters.edge_scope == 'global'

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
                                edge_scope=filters.edge_scope,
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

                edge_condition_sql = (
                    '(e.source_id = ANY(%s) OR e.target_id = ANY(%s))'
                    if is_global_scope
                    else 'e.source_id = ANY(%s) AND e.target_id = ANY(%s)'
                )
                edge_join_sql = (
                    'LEFT JOIN knowledge.doc_metadata s ON s.doc_id = e.source_id\n'
                    '                    LEFT JOIN knowledge.doc_metadata t ON t.doc_id = e.target_id'
                    if is_global_scope
                    else 'INNER JOIN knowledge.doc_metadata s ON s.doc_id = e.source_id\n'
                    '                    INNER JOIN knowledge.doc_metadata t ON t.doc_id = e.target_id'
                )
                cur.execute(
                    f'''
                    SELECT
                      LEAST(e.source_id::text, e.target_id::text) AS source_id,
                      GREATEST(e.source_id::text, e.target_id::text) AS target_id,
                      MAX(e.weight)::float8 AS weight
                    FROM knowledge.similarity_edges e
                    {edge_join_sql}
                    WHERE {edge_condition_sql}
                      AND e.source_id <> e.target_id
                    GROUP BY LEAST(e.source_id::text, e.target_id::text), GREATEST(e.source_id::text, e.target_id::text)
                    ORDER BY source_id, target_id, weight DESC;
                    ''',
                    (filtered_doc_ids, filtered_doc_ids),
                )
                edge_rows = cur.fetchall()

                logger.info(
                    '🔗 graph_filter_stats raw_count=%s filtered_count=%s truncated=%s raw_head=%s filtered_head=%s edge_rows=%s edge_scope=%s',
                    len(filtered_doc_ids_raw),
                    len(filtered_doc_ids),
                    truncated,
                    filtered_doc_ids_raw[:5],
                    filtered_doc_ids[:5],
                    len(edge_rows),
                    filters.edge_scope,
                )

                node_ids_set = {str(row[0]) for row in node_rows}
                if is_global_scope:
                    edge_node_ids = {
                        edge_node_id
                        for source_id, target_id, _ in edge_rows
                        for edge_node_id in (str(source_id), str(target_id))
                    }
                    missing_node_ids = sorted(edge_node_ids - node_ids_set)
                    if missing_node_ids:
                        cur.execute(
                            '''
                            SELECT dm.doc_id, dm.doc_type, dm.meta->>'title' AS title, dm.year, dm.channels, dm.rubric_ids, dm.category_ids, dm.authors, dm.meta
                            FROM knowledge.doc_metadata dm
                            WHERE dm.doc_id = ANY(%s)
                            ORDER BY dm.doc_id;
                            ''',
                            (missing_node_ids,),
                        )
                        supplemental_node_rows = cur.fetchall()
                        node_rows.extend(supplemental_node_rows)
                        node_ids_set.update(str(row[0]) for row in supplemental_node_rows)
                        logger.info(
                            '🧩 graph_global_missing_nodes missing_count=%s missing_head=%s loaded=%s',
                            len(missing_node_ids),
                            missing_node_ids[:5],
                            len(supplemental_node_rows),
                        )

                    fallback_node_ids = sorted(edge_node_ids - node_ids_set)
                    if fallback_node_ids:
                        node_rows.extend(
                            (
                                doc_id,
                                'unknown',
                                doc_id,
                                None,
                                [],
                                [],
                                [],
                                [],
                                {},
                            )
                            for doc_id in fallback_node_ids
                        )
                        logger.warning(
                            '🛟 graph_global_fallback_nodes created=%s ids_head=%s',
                            len(fallback_node_ids),
                            fallback_node_ids[:5],
                        )

                cur.execute(
                    '''
                    SELECT count(*)
                    FROM knowledge.similarity_edges e
                    LEFT JOIN knowledge.doc_metadata s ON s.doc_id = e.source_id
                    LEFT JOIN knowledge.doc_metadata t ON t.doc_id = e.target_id
                    WHERE (e.source_id = ANY(%s) OR e.target_id = ANY(%s))
                      AND e.source_id <> e.target_id
                      AND (s.doc_id IS NULL OR t.doc_id IS NULL);
                    ''',
                    (filtered_doc_ids, filtered_doc_ids),
                )
                data_gap_count = int(cur.fetchone()[0])
                if data_gap_count > 0:
                    ratio = (data_gap_count / len(edge_rows)) if edge_rows else 0.0
                    logger.warning(
                        'data_gap detected in /v1/graph: edges_without_metadata=%s returned_edges=%s ratio=%.4f edge_scope=%s',
                        data_gap_count,
                        len(edge_rows),
                        ratio,
                        filters.edge_scope,
                    )

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
                    edge_scope=filters.edge_scope,
                ),
                total_nodes=len(nodes),
                total_edges=len(edges),
                truncated=truncated,
            ),
        )
