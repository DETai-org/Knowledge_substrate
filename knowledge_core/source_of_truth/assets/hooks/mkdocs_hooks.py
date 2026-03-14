"""Хуки MkDocs для предобработки Markdown."""

from __future__ import annotations

import re
from typing import Match

from markdown.extensions.toc import slugify_unicode

WIKILINK_PATTERN = re.compile(r"\[\[([^\[\]]+?)\]\]")


def _split_wikilink_payload(payload: str) -> tuple[str, str | None]:
    """Разделяет содержимое wikilink на target и label."""
    normalized = payload.replace("\\|", "|")
    if "|" not in normalized:
        return normalized.strip(), None

    target, label = normalized.split("|", 1)
    return target.strip(), label.strip()


def _convert_target(target: str) -> str:
    """Конвертирует target Obsidian-ссылки в Markdown href."""
    if target.startswith("#"):
        anchor = target[1:].strip()
        return f"#{slugify_unicode(anchor, '-')}"
    return target


def convert_obsidian_wikilinks(
    markdown: str,
    /,
    *,
    page,
    config,
    files,
) -> str:
    """Преобразует Obsidian wikilinks [[...]] в обычные Markdown-ссылки."""

    def _replace(match: Match[str]) -> str:
        payload = match.group(1)
        target, label = _split_wikilink_payload(payload)
        href = _convert_target(target)
        text = label or target
        return f"[{text}]({href})"

    return WIKILINK_PATTERN.sub(_replace, markdown)
