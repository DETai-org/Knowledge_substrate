from __future__ import annotations

import argparse
import logging
import os
import time
import uuid
from pathlib import Path

import psycopg2

from knowledge_core.ingest_pipeline.graph_builder.pipeline import (
    DbConfig,
    apply_cli_embeddings,
    apply_cli_execution,
    apply_cli_graph,
    build_similarity_edges,
    build_dsn,
    clear_edges,
    fetch_embeddings_for_edges,
    load_config,
    persist_edges,
)
from knowledge_core.ingest_pipeline.logging import log_error, log_event, setup_logging

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Edges stage (только построение и запись рёбер)')
    parser.add_argument('--config', type=Path, required=False)
    parser.add_argument('--k', type=int, default=None)
    parser.add_argument('--min-similarity', type=float, default=None)
    parser.add_argument('--mode', type=str, choices=('incremental', 'full'), default=None)
    parser.add_argument('--full-rebuild', action='store_true')
    parser.add_argument('--debug', action='store_true')
    return parser.parse_args()


def run_edges_stage(db_config: DbConfig, graph_config, embedding_config, full_rebuild: bool, run_id: str) -> int:
    started = time.time()
    log_event(logger, run_id, 'start', 'старт edges stage', stage='edges')
    with psycopg2.connect(db_config.dsn) as conn:
        conn.autocommit = False
        embeddings = fetch_embeddings_for_edges(
            conn,
            doc_type=graph_config.doc_type,
            model=embedding_config.model,
        )
        log_event(logger, run_id, 'embeddings', 'подготовлены embeddings для построения рёбер', stage='edges', docs_count=len(embeddings), model=embedding_config.model)
        if full_rebuild:
            clear_edges(conn, graph_config)

        edges = build_similarity_edges(embeddings, graph_config)
        log_event(logger, run_id, 'edges', 'рёбра рассчитаны', stage='edges', edges_count=len(edges), top_k=graph_config.k, min_similarity=graph_config.min_similarity)
        written = persist_edges(
            conn,
            edges,
            graph_config=graph_config,
            affected_doc_ids={record.doc_id for record in embeddings},
            full_rebuild=full_rebuild,
        )
        conn.commit()

    duration_ms = int((time.time() - started) * 1000)
    log_event(logger, run_id, 'done', 'edges stage done', stage='edges', rows=written, duration_ms=duration_ms)
    return written


def main() -> None:
    args = parse_args()
    setup_logging(logging.DEBUG if args.debug else logging.INFO)
    run_id = uuid.uuid4().hex[:8]
    config_path = args.config or Path(os.getenv('CONFIG_PATH', Path(__file__).resolve().parents[1] / 'config.json'))

    try:
        config = load_config(config_path)
        embedding_config = apply_cli_embeddings(config.embeddings, args)
        graph_config = apply_cli_graph(config.graph, args)
        execution_config = apply_cli_execution(config.execution, args)
        run_edges_stage(
            db_config=DbConfig(dsn=build_dsn()),
            graph_config=graph_config,
            embedding_config=embedding_config,
            full_rebuild=args.full_rebuild or execution_config.mode == 'full',
            run_id=run_id,
        )
    except Exception as exc:
        log_error(logger, run_id, 'edges', f'edges stage failed: {exc}')
        if args.debug:
            raise
        raise SystemExit(1) from exc


if __name__ == '__main__':
    main()
