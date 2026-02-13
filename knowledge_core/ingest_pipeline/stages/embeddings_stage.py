from __future__ import annotations

import argparse
import logging
import os
import uuid
from pathlib import Path

from knowledge_core.ingest_pipeline.graph_builder.pipeline import (
    DbConfig,
    apply_cli_embeddings,
    apply_cli_execution,
    apply_cli_graph,
    load_config,
    run_pipeline,
    build_dsn,
)
from knowledge_core.ingest_pipeline.logging import log_error, log_event, setup_logging

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Embeddings stage (без metadata и без edges)')
    parser.add_argument('--source-root', type=Path, required=False)
    parser.add_argument('--config', type=Path, required=False)
    parser.add_argument('--model', type=str, required=False)
    parser.add_argument('--provider', type=str, default=None)
    parser.add_argument('--batch-size', type=int, default=None)
    parser.add_argument('--max-chars', type=int, default=None)
    parser.add_argument('--limit-posts', type=int, default=None)
    parser.add_argument('--mode', type=str, choices=('incremental', 'full'), default=None)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--fail-fast', action='store_true')
    parser.add_argument('--debug', action='store_true')
    return parser.parse_args()



def main() -> None:
    args = parse_args()
    setup_logging(logging.DEBUG if args.debug else logging.INFO)
    run_id = uuid.uuid4().hex[:8]

    source_root = args.source_root or (
        Path(__file__).resolve().parents[2] / 'source_of_truth' / 'docs' / 'publications' / 'blogs'
    )
    config_path = args.config or Path(os.getenv('CONFIG_PATH', Path(__file__).resolve().parents[1] / 'config.json'))

    try:
        config = load_config(config_path)
        embedding_config = apply_cli_embeddings(config.embeddings, args)
        graph_config = apply_cli_graph(config.graph, args)
        execution_config = apply_cli_execution(config.execution, args)
        log_event(logger, run_id, 'start', 'старт embeddings stage', stage='embeddings')
        run_pipeline(
            source_root=source_root,
            db_config=DbConfig(dsn=build_dsn()),
            embedding_config=embedding_config,
            graph_config=graph_config,
            execution_config=execution_config,
            extract_config=config.extract,
            full_rebuild=False,
            run_id=run_id,
            run_embeddings=True,
            run_edges=False,
        )
    except Exception as exc:
        log_error(logger, run_id, 'embeddings', f'embeddings stage failed: {exc}')
        if args.debug:
            raise
        raise SystemExit(1) from exc


if __name__ == '__main__':
    main()
