from __future__ import annotations

import argparse
import logging
import os
import time
import uuid
from pathlib import Path

import psycopg2
import psycopg2.extras

from knowledge_core.ingest_pipeline.logging import log_error, log_event, setup_logging
from knowledge_core.ingest_pipeline.posts import PostExtracted, extract_publish_posts

logger = logging.getLogger(__name__)


def build_dsn() -> str:
    if os.getenv('DATABASE_URL'):
        return os.environ['DATABASE_URL']
    host = os.getenv('PGHOST', 'localhost')
    port = os.getenv('PGPORT', '5432')
    user = os.getenv('PGUSER', 'postgres')
    password = os.getenv('PGPASSWORD', '')
    database = os.getenv('PGDATABASE', 'postgres')
    return f'dbname={database} user={user} password={password} host={host} port={port}'


def validate_post_metadata(post: PostExtracted, run_id: str) -> None:
    if not post.channels:
        log_event(logger, run_id, 'warn', 'пост без channels', doc_id=post.id, source_path=post.source_path)
    if not post.authors:
        log_event(logger, run_id, 'warn', 'пост без authors', doc_id=post.id, source_path=post.source_path)


def upsert_doc_metadata(posts: list[PostExtracted], dsn: str, run_id: str) -> int:
    values = [
        (
            post.id,
            post.date_ymd,
            post.channels,
            post.authors,
            post.rubric_ids,
            post.category_ids,
            'post',
            psycopg2.extras.Json(
                {
                    'source_path': post.source_path,
                    'title': post.title,
                    'source_hash': post.source_hash,
                }
            ),
        )
        for post in posts
    ]

    query = """
    INSERT INTO knowledge.doc_metadata
      (doc_id, date_ymd, channels, authors, rubric_ids, category_ids, doc_type, meta)
    VALUES %s
    ON CONFLICT (doc_id)
    DO UPDATE SET
      date_ymd = EXCLUDED.date_ymd,
      channels = EXCLUDED.channels,
      authors = EXCLUDED.authors,
      rubric_ids = EXCLUDED.rubric_ids,
      category_ids = EXCLUDED.category_ids,
      doc_type = EXCLUDED.doc_type,
      meta = EXCLUDED.meta,
      updated_at = now()
    """

    with psycopg2.connect(dsn) as conn:
        with conn.cursor() as cur:
            psycopg2.extras.execute_values(cur, query, values)
    return len(values)


def run_metadata_stage(source_root: Path, dsn: str, limit_posts: int | None = None, run_id: str | None = None) -> int:
    local_run_id = run_id or uuid.uuid4().hex[:8]
    started = time.time()
    log_event(logger, local_run_id, 'start', 'старт metadata stage', stage='metadata')
    posts = extract_publish_posts(source_root)
    if limit_posts is not None:
        posts = posts[:limit_posts]
    log_event(logger, local_run_id, 'read', 'прочитаны publish-посты', stage='metadata', posts=len(posts))

    for post in posts:
        validate_post_metadata(post, local_run_id)

    if not posts:
        log_event(logger, local_run_id, 'warn', 'нет данных для materialization', stage='metadata')
        return 0

    rows = upsert_doc_metadata(posts, dsn=dsn, run_id=local_run_id)
    duration_ms = int((time.time() - started) * 1000)
    log_event(logger, local_run_id, 'upsert', 'materialization metadata завершен', stage='metadata', table='knowledge.doc_metadata', rows=rows)
    log_event(logger, local_run_id, 'done', 'metadata stage done', stage='metadata', duration_ms=duration_ms)
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Materialize metadata: SoT -> knowledge.doc_metadata')
    parser.add_argument('--source-root', type=Path, required=False)
    parser.add_argument('--limit-posts', type=int, default=None)
    parser.add_argument('--debug', action='store_true')
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    setup_logging(logging.DEBUG if args.debug else logging.INFO)
    source_root = args.source_root or (
        Path(__file__).resolve().parents[2] / 'source_of_truth' / 'docs' / 'publications' / 'blogs'
    )

    try:
        run_metadata_stage(source_root=source_root, dsn=build_dsn(), limit_posts=args.limit_posts)
    except Exception as exc:
        run_id = uuid.uuid4().hex[:8]
        log_error(logger, run_id, 'metadata', f'metadata stage failed: {exc}')
        if args.debug:
            raise
        raise SystemExit(1) from exc


if __name__ == '__main__':
    main()
