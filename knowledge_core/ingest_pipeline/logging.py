from __future__ import annotations

import logging
from typing import Any

STAGE_EMOJI = {
    'start': '🚀',
    'read': '📥',
    'upsert': '🧱',
    'embeddings': '🧠',
    'edges': '🕸️',
    'done': '✅',
    'warn': '⚠️',
    'error': '❌',
    'preflight': '✅',
    'extract': '📥',
    'embed': '🧠',
    'knn': '🕸️',
    'persist': '🧱',
    'dry_run': '🧪',
}


def setup_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s')


def _fmt_fields(fields: dict[str, Any]) -> str:
    if not fields:
        return ''
    ordered = sorted((key, value) for key, value in fields.items() if value is not None)
    return ' | ' + ' '.join(f'{key}={value}' for key, value in ordered)


def log_event(logger: logging.Logger, run_id: str, event: str, message: str, **fields: Any) -> None:
    emoji = STAGE_EMOJI.get(event, 'ℹ️')
    logger.info('%s %s run_id=%s%s', emoji, message, run_id, _fmt_fields(fields))


def log_error(logger: logging.Logger, run_id: str, stage: str, message: str, **fields: Any) -> None:
    emoji = STAGE_EMOJI.get('error', '❌')
    logger.error('%s %s run_id=%s stage=%s%s', emoji, message, run_id, stage, _fmt_fields(fields))
