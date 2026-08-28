"""Хуки MkDocs для предобработки Markdown."""

from __future__ import annotations

import gzip
import html
import json
import re
from pathlib import Path
from typing import Match
from urllib.parse import urljoin
from xml.etree import ElementTree

from markdown.extensions.toc import slugify_unicode
from mkdocs.structure.files import File, Files, InclusionLevel

WIKILINK_PATTERN = re.compile(r"\[\[([^\[\]]+?)\]\]")
TITLE_PATTERN = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)
HEADING_PATTERN = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)

PLACEHOLDER_LOCALES = {
    "en": {
        "language": "English",
        "eyebrow": "Translation preview · English",
        "lead": "The English edition of this document is being prepared.",
        "warning_title": "This page is currently available in Russian",
        "warning_body": "We’re preparing the English version. You can open the Russian original now.",
        "original_button": "Open the Russian original",
        "info_title": "Get the English release update",
        "info_body": "Be the first to know when DETai documentation is available in English. Follow our Telegram channel for release updates.",
        "telegram_button": "Subscribe on Telegram",
        "telegram_url": "https://t.me/detai_en",
        "flag": "gb",
    },
    "fi": {
        "language": "Suomi",
        "eyebrow": "Käännöksen esikatselu · Suomi",
        "lead": "Tämän asiakirjan suomenkielistä versiota valmistellaan.",
        "warning_title": "Tämä sivu on tällä hetkellä saatavilla venäjäksi",
        "warning_body": "Valmistelemme suomenkielistä versiota. Voit avata venäjänkielisen alkuperäisversion nyt.",
        "original_button": "Avaa venäjänkielinen alkuperäisversio",
        "info_title": "Saa tieto suomenkielisestä julkaisusta",
        "info_body": "Saat ensimmäisten joukossa tiedon, kun DETai-dokumentaatio julkaistaan suomeksi. Seuraa Telegram-kanavaamme.",
        "telegram_button": "Seuraa Telegramissa",
        "telegram_url": "https://t.me/detai_fi",
        "flag": "fi",
    },
    "de": {
        "language": "Deutsch",
        "eyebrow": "Übersetzungsvorschau · Deutsch",
        "lead": "Die deutsche Fassung dieses Dokuments wird vorbereitet.",
        "warning_title": "Diese Seite ist derzeit auf Russisch verfügbar",
        "warning_body": "Wir arbeiten an der deutschen Version. Sie können jetzt das russische Original öffnen.",
        "original_button": "Russisches Original öffnen",
        "info_title": "Über die deutsche Veröffentlichung informiert werden",
        "info_body": "Erfahren Sie als Erste, wann die DETai-Dokumentation auf Deutsch verfügbar ist. Folgen Sie unserem Telegram-Kanal.",
        "telegram_button": "Auf Telegram folgen",
        "telegram_url": "https://t.me/detai_de",
        "flag": "de",
    },
    "zh": {
        "language": "中文",
        "eyebrow": "翻译预览 · 中文",
        "lead": "本文档的中文版本正在准备中。",
        "warning_title": "此页面目前仅提供俄语版本",
        "warning_body": "我们正在准备中文版本。您现在可以查看俄语原文。",
        "original_button": "打开俄语原文",
        "info_title": "获取中文版发布通知",
        "info_body": "想第一时间获知 DETai 文档中文版上线，请关注我们的英文 Telegram 频道。",
        "telegram_button": "在 Telegram 上关注",
        "telegram_url": "https://t.me/detai_en",
        "flag": "gb",
    },
}

GENERATED_PLACEHOLDER_URLS: set[str] = set()
SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"


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


def _document_title(markdown: str, fallback: str) -> str:
    """Возвращает title русского источника без YAML-обвязки."""
    match = TITLE_PATTERN.search(markdown) or HEADING_PATTERN.search(markdown)
    if not match:
        return fallback.replace("-", " ").replace("_", " ").strip().title()

    title = match.group(1).strip().strip('"\'')
    return re.sub(r"[*_`]", "", title)


def _route_from_relative(relative_path: str) -> str:
    """Преобразует относительный Markdown path в directory URL."""
    if relative_path == "index.md":
        return ""
    if relative_path.endswith("/index.md"):
        return relative_path[: -len("index.md")]
    return relative_path[: -len(".md")] + "/"


def _placeholder_markdown(title: str, locale: str, original_url: str) -> str:
    """Строит честную локализованную заглушку для отсутствующего перевода."""
    copy = PLACEHOLDER_LOCALES[locale]
    yaml_title = json.dumps(title, ensure_ascii=False)
    return f'''---
title: {yaml_title}
description: {json.dumps(copy["lead"], ensure_ascii=False)}
robots: noindex, follow
translation_placeholder: true
canonical_original: {original_url}
descriptive:
  status: draft
hide:
  - navigation
  - toc
---

<section class="translation-placeholder-page" markdown>

<p class="translation-placeholder-page__eyebrow">{copy["eyebrow"]}</p>

# {title}

<p class="translation-placeholder-page__lead">
{copy["lead"]}
</p>

!!! warning "{copy["warning_title"]}"

    {copy["warning_body"]}

    [{copy["original_button"]}]({original_url}){{ .md-button .md-button--primary }}

!!! info "{copy["info_title"]}"

    {copy["info_body"]}

    <a class="md-button translation-placeholder-page__telegram" href="{copy["telegram_url"]}"><img class="translation-placeholder-page__telegram-flag" src="/assets/images/flags/{copy["flag"]}.svg" alt="" aria-hidden="true"><span>{copy["telegram_button"]}</span><img class="translation-placeholder-page__telegram-mark" src="/assets/images/telegram-mark.svg" alt="" aria-hidden="true"></a>

</section>
'''


def _legacy_cn_redirect(target_url: str) -> str:
    """Создаёт статический compatibility redirect /cn/* → /zh/*."""
    escaped_url = html.escape(target_url, quote=True)
    js_url = json.dumps(target_url, ensure_ascii=False)
    return f'''<!doctype html>
<html lang="zh">
  <head>
    <meta charset="utf-8">
    <meta name="robots" content="noindex, follow">
    <link rel="canonical" href="{escaped_url}">
    <meta http-equiv="refresh" content="0; url={escaped_url}">
    <title>Redirecting…</title>
  </head>
  <body>
    <p><a href="{escaped_url}">继续前往中文文档</a></p>
    <script>window.location.replace({js_url} + window.location.search + window.location.hash);</script>
  </body>
</html>
'''


def generate_translation_placeholders(files: Files, /, *, config) -> Files:
    """Добавляет виртуальные placeholders и legacy redirects на этапе сборки."""
    GENERATED_PLACEHOLDER_URLS.clear()
    existing = {file.src_uri for file in files}
    generated: list[File] = []

    for source in list(files):
        if not source.src_uri.startswith("ru/") or not source.is_documentation_page():
            continue
        if source.inclusion == InclusionLevel.EXCLUDED:
            continue

        relative_path = source.src_uri[len("ru/") :]
        route = _route_from_relative(relative_path)
        original_url = f"/ru/{route}"
        title = _document_title(source.content_string, source.name)

        for locale in PLACEHOLDER_LOCALES:
            target_uri = f"{locale}/{relative_path}"
            if target_uri in existing:
                continue
            generated.append(
                File.generated(
                    config,
                    target_uri,
                    content=_placeholder_markdown(title, locale, original_url),
                    inclusion=InclusionLevel.NOT_IN_NAV,
                )
            )
            GENERATED_PLACEHOLDER_URLS.add(urljoin(config.site_url, f"{locale}/{route}"))
            existing.add(target_uri)

        legacy_uri = f"cn/{route}index.html"
        if legacy_uri not in existing:
            generated.append(
                File.generated(
                    config,
                    legacy_uri,
                    content=_legacy_cn_redirect(f"/zh/{route}"),
                    inclusion=InclusionLevel.INCLUDED,
                )
            )
            existing.add(legacy_uri)

    for generated_file in generated:
        files.append(generated_file)
    return files


def set_translation_placeholder_canonical(context: dict, /, *, page, config, nav) -> dict:
    """Canonical заглушки указывает на русский оригинал, а не на noindex route."""
    original = page.meta.get("canonical_original") if page.meta else None
    if page.meta and page.meta.get("translation_placeholder") and original:
        page.canonical_url = urljoin(config.site_url, original.lstrip("/"))
    return context


def remove_translation_placeholders_from_sitemap(*, config) -> None:
    """Не публикует noindex placeholders в sitemap до появления перевода."""
    sitemap_path = Path(config.site_dir) / "sitemap.xml"
    if not sitemap_path.exists() or not GENERATED_PLACEHOLDER_URLS:
        return

    ElementTree.register_namespace("", SITEMAP_NAMESPACE)
    tree = ElementTree.parse(sitemap_path)
    root = tree.getroot()
    location_tag = f"{{{SITEMAP_NAMESPACE}}}loc"

    for url_element in list(root):
        location = url_element.find(location_tag)
        if location is not None and location.text in GENERATED_PLACEHOLDER_URLS:
            root.remove(url_element)

    tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)
    with sitemap_path.open("rb") as source, gzip.open(
        sitemap_path.with_suffix(".xml.gz"), "wb"
    ) as destination:
        destination.write(source.read())
