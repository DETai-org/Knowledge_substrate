from __future__ import annotations

import dataclasses
import hashlib
import logging
import re
from pathlib import Path
from typing import Any, Iterable

import yaml


logger = logging.getLogger(__name__)


@dataclasses.dataclass(frozen=True)
class PostExtracted:
    id: str
    title: str
    authors: list[str]
    date_ymd: str
    year: int
    channels: list[str]
    rubric_ids: list[str]
    category_ids: list[str]
    text_for_embedding: str
    source_path: str
    source_hash: str


def extract_publish_posts(
    source_root: Path,
    prefer_channel: str | None = None,
) -> list[PostExtracted]:
    posts: list[PostExtracted] = []
    for path in iter_markdown_files(source_root):
        try:
            raw_text = path.read_text(encoding="utf-8")
        except OSError as exc:
            logger.error("❌ Не удалось прочитать файл %s: %s", path, exc)
            continue

        try:
            frontmatter, body = split_frontmatter(raw_text, path)
            meta = yaml.safe_load(frontmatter) or {}
        except ValueError as exc:
            logger.error("❌ %s", exc)
            continue
        except yaml.YAMLError as exc:
            logger.error("❌ Ошибка YAML в %s: %s", path, exc)
            continue

        if not is_publish_post(meta):
            continue

        post = build_post(meta, body, raw_text, path)
        if post is None:
            continue
        posts.append(post)

    return deduplicate_posts(posts, prefer_channel)


def iter_markdown_files(source_root: Path) -> Iterable[Path]:
    return (
        path
        for path in source_root.rglob("*.md")
        if path.is_file() and path.name.lower() != "readme.md"
    )


def split_frontmatter(raw_text: str, path: Path) -> tuple[str, str]:
    lines = raw_text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"Отсутствует frontmatter в {path}")

    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            frontmatter = "\n".join(lines[1:idx])
            body = "\n".join(lines[idx + 1 :])
            return frontmatter, body

    raise ValueError(f"Не найден конец frontmatter в {path}")


def is_publish_post(meta: dict[str, Any]) -> bool:
    if meta.get("type") != "post":
        return False

    administrative = meta.get("administrative") or {}
    if administrative.get("status") != "publish":
        return False

    return True


def build_post(
    meta: dict[str, Any],
    body: str,
    raw_text: str,
    path: Path,
) -> PostExtracted | None:
    administrative = meta.get("administrative") or {}
    descriptive = meta.get("descriptive") or {}
    taxonomy = (descriptive.get("taxonomy") or {}) if isinstance(descriptive, dict) else {}

    missing = []

    if meta.get("type") != "post":
        missing.append("type=post")
    if administrative.get("status") != "publish":
        missing.append("administrative.status=publish")
    if not administrative.get("id"):
        missing.append("administrative.id")
    if not administrative.get("date_ymd"):
        missing.append("administrative.date_ymd")
    if not descriptive.get("title"):
        missing.append("descriptive.title")

    if missing:
        logger.error(
            "❌ Пропущен файл %s: отсутствуют обязательные поля: %s",
            path,
            ", ".join(missing),
        )
        return None

    doc_id = str(administrative["id"]).strip()
    if not doc_id:
        logger.error("❌ Пропущен файл %s: пустой administrative.id", path)
        return None

    date_ymd = str(administrative["date_ymd"]).strip()
    try:
        year = int(date_ymd.split("-", 1)[0])
    except (ValueError, IndexError):
        logger.error("❌ Пропущен файл %s: некорректный date_ymd=%s", path, date_ymd)
        return None

    title = str(descriptive["title"]).strip()
    cleaned_body = clean_markdown(body)
    text_for_embedding = build_text_for_embedding(title, cleaned_body)

    source_hash = hashlib.sha256(raw_text.encode("utf-8")).hexdigest()

    return PostExtracted(
        id=doc_id,
        title=title,
        authors=list(administrative.get("authors") or []),
        date_ymd=date_ymd,
        year=year,
        channels=list(administrative.get("channels") or []),
        rubric_ids=list(taxonomy.get("rubric_ids") or []),
        category_ids=list(taxonomy.get("category_ids") or []),
        text_for_embedding=text_for_embedding,
        source_path=str(path),
        source_hash=source_hash,
    )


def build_text_for_embedding(title: str, cleaned_body: str) -> str:
    parts = [title.strip(), cleaned_body.strip()]
    return "\n\n".join(part for part in parts if part)


def clean_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*([-*+]|\d+\.)\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\|?[-:| ]+\|?\s*$", " ", text, flags=re.MULTILINE)
    text = text.replace("|", " ")
    text = re.sub(r"[*_~]+", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def deduplicate_posts(
    posts: list[PostExtracted],
    prefer_channel: str | None,
) -> list[PostExtracted]:
    by_id: dict[str, PostExtracted] = {}
    duplicates: dict[str, list[PostExtracted]] = {}

    for post in posts:
        existing = by_id.get(post.id)
        if existing is None:
            by_id[post.id] = post
            continue

        duplicates.setdefault(post.id, [existing]).append(post)
        chosen = choose_canonical_post(
            [existing, post],
            prefer_channel=prefer_channel,
        )
        by_id[post.id] = chosen

    for doc_id, items in duplicates.items():
        paths = sorted({item.source_path for item in items})
        chosen_path = by_id[doc_id].source_path
        logger.info(
            "📃х2☝️ Дубликат post id=%s, выбран путь=%s, кандидаты=%s",
            doc_id,
            chosen_path,
            paths,
        )

    return list(by_id.values())


def choose_canonical_post(
    candidates: list[PostExtracted],
    prefer_channel: str | None,
) -> PostExtracted:
    if prefer_channel:
        preferred = [
            post for post in candidates if prefer_channel in post.channels
        ]
        if preferred:
            return sorted(preferred, key=lambda post: post.source_path)[0]
    return sorted(candidates, key=lambda post: post.source_path)[0]


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    default_root = (
        Path(__file__).resolve().parents[2]
        / "source_of_truth"
        / "docs"
        / "publications"
        / "blogs"
    )
    posts = extract_publish_posts(default_root)
    logger.info("Найдено publish-постов: %s", len(posts))


if __name__ == "__main__":
    main()
