from __future__ import annotations

import argparse
import logging
import os
import sys
import traceback
import uuid
from pathlib import Path

from knowledge_core.ingest_pipeline.graph_builder.pipeline import (
    DbConfig,
    apply_cli_embeddings,
    apply_cli_execution,
    apply_cli_graph,
    build_dsn,
    load_config,
    run_pipeline,
)
from knowledge_core.ingest_pipeline.logging import log_error, log_event, setup_logging
from knowledge_core.ingest_pipeline.metadata.metadata_ingest import run_metadata_stage
from knowledge_core.ingest_pipeline.stages.edges_stage import run_edges_stage

logger = logging.getLogger(__name__)


STAGES = ('metadata', 'embeddings', 'edges', 'all')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Единый оркестратор ingest-пайплайна')
    parser.add_argument('--stage', choices=STAGES, default='all')
    parser.add_argument('--source-root', type=Path, required=False)
    parser.add_argument('--config', type=Path, required=False)
    parser.add_argument('--limit-posts', type=int, default=None)
    parser.add_argument('--model', type=str, required=False)
    parser.add_argument('--provider', type=str, default=None)
    parser.add_argument('--batch-size', type=int, default=None)
    parser.add_argument('--max-chars', type=int, default=None)
    parser.add_argument('--k', type=int, default=None)
    parser.add_argument('--min-similarity', type=float, default=None)
    parser.add_argument('--mode', type=str, choices=('incremental', 'full'), default=None)
    parser.add_argument('--min-posts', type=int, default=None)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--fail-fast', action='store_true')
    parser.add_argument('--full-rebuild', action='store_true')
    parser.add_argument('--debug', action='store_true')
    return parser.parse_args()


def run_stage(stage: str, args: argparse.Namespace, run_id: str) -> None:
    source_root = args.source_root or (
        Path(__file__).resolve().parents[1] / 'source_of_truth' / 'docs' / 'publications' / 'blogs'
    )
    config_path = args.config or Path(os.getenv('CONFIG_PATH', Path(__file__).resolve().parent / 'config.json'))
    config = load_config(config_path)
    embedding_config = apply_cli_embeddings(config.embeddings, args)
    graph_config = apply_cli_graph(config.graph, args)
    execution_config = apply_cli_execution(config.execution, args)

    if stage == 'metadata':
        run_metadata_stage(source_root=source_root, dsn=build_dsn(), limit_posts=args.limit_posts, run_id=run_id)
        return

    if stage == 'embeddings':
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
        return

    if stage == 'edges':
        run_edges_stage(
            db_config=DbConfig(dsn=build_dsn()),
            graph_config=graph_config,
            embedding_config=embedding_config,
            full_rebuild=execution_config.mode == 'full',
            run_id=run_id,
        )
        return

    for staged in ('metadata', 'embeddings', 'edges'):
        log_event(logger, run_id, 'start', 'запуск этапа', stage=staged)
        run_stage(staged, args, run_id)


def main() -> None:
    args = parse_args()
    setup_logging(logging.DEBUG if args.debug else logging.INFO)
    run_id = uuid.uuid4().hex[:8]
    log_event(logger, run_id, 'start', 'запуск ingest orchestrator', stage=args.stage)

    try:
        run_stage(args.stage, args, run_id)
        log_event(logger, run_id, 'done', 'ingest orchestrator завершён', stage=args.stage)
    except Exception as exc:
        log_error(logger, run_id, args.stage, f'этап упал: {exc}')
        log_error(
            logger,
            run_id,
            args.stage,
            'что делать дальше: проверьте DATABASE_URL/OPENAI_API_KEY/config.json и перезапустите нужный --stage',
        )
        if args.debug:
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
