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

HOME_LOCALES = ("ru", "en", "fi", "de", "zh")
HOME_LANGUAGE_NAMES = {
    "ru": "Русский",
    "en": "English",
    "fi": "Suomi",
    "de": "Deutsch",
    "zh": "中文",
}
DETAI_ORGANIZATION_ID = "https://detai-x.com/#organization"
DETAI_ORGANIZATION_SAME_AS = [
    "https://t.me/detai_ru",
    "https://t.me/detai_en",
    "https://t.me/detai_fi",
    "https://t.me/detai_de",
    "https://www.youtube.com/@Ecosystem-DET",
    "https://github.com/DETai-org",
]
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
search:
  exclude: true
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

    <a class="md-button detai-telegram-button translation-placeholder-page__telegram" href="{copy["telegram_url"]}"><img class="translation-placeholder-page__telegram-flag" src="/assets/images/flags/{copy["flag"]}.svg" alt="" aria-hidden="true"><span>{copy["telegram_button"]}</span><img class="translation-placeholder-page__telegram-mark" src="/assets/images/telegram-mark.svg" alt="" aria-hidden="true"></a>

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


def _home_locale(page_url: str) -> str | None:
    normalized = page_url.strip("/")
    return normalized if normalized in HOME_LOCALES else None


def _home_structured_data(page, config, locale: str | None) -> dict:
    """Строит минимальный связный граф документации и основной DETai Organization."""
    page_url = urljoin(config.site_url, page.url)
    docs_website_id = urljoin(config.site_url, "#website")
    page_id = f"{page_url}#webpage"
    title = page.meta.get("title", page.title)
    description = page.meta.get("description", config.site_description or "")

    organization = {
        "@type": "Organization",
        "@id": DETAI_ORGANIZATION_ID,
        "name": "DETai",
        "url": "https://detai-x.com/",
        "logo": "https://detai-x.com/logo/logo.png",
        "sameAs": DETAI_ORGANIZATION_SAME_AS,
    }
    website = {
        "@type": "WebSite",
        "@id": docs_website_id,
        "name": "DETai Documentation",
        "alternateName": "DETai Knowledge Substrate",
        "url": config.site_url,
        "publisher": {"@id": DETAI_ORGANIZATION_ID},
        "about": {"@id": DETAI_ORGANIZATION_ID},
        "inLanguage": list(HOME_LOCALES),
    }
    webpage = {
        "@type": "CollectionPage" if locale else "WebPage",
        "@id": page_id,
        "url": page_url,
        "name": title,
        "description": description,
        "isPartOf": {"@id": docs_website_id},
        "publisher": {"@id": DETAI_ORGANIZATION_ID},
        "about": [
            {"@id": DETAI_ORGANIZATION_ID},
            {"@id": "https://detai-x.com/#det"},
            {"@id": "https://detai-x.com/#ai-augmented-psychotherapy"},
        ],
    }

    graph = [organization, website, webpage]
    if locale:
        webpage["inLanguage"] = locale
        if locale != "ru":
            webpage["translationOfWork"] = {
                "@id": f"{urljoin(config.site_url, 'ru/')}#webpage"
            }
    else:
        language_list_id = f"{page_url}#language-options"
        webpage["inLanguage"] = list(HOME_LOCALES)
        webpage["mainEntity"] = {"@id": language_list_id}
        graph.append(
            {
                "@type": "ItemList",
                "@id": language_list_id,
                "name": "Available DETai documentation languages",
                "numberOfItems": len(HOME_LOCALES),
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": position,
                        "name": HOME_LANGUAGE_NAMES[language],
                        "url": urljoin(config.site_url, f"{language}/"),
                    }
                    for position, language in enumerate(HOME_LOCALES, start=1)
                ],
            }
        )

    return {"@context": "https://schema.org", "@graph": graph}


def set_page_semantics(context: dict, /, *, page, config, nav) -> dict:
    """Устанавливает canonical заглушек и семантику индексируемых home pages."""
    original = page.meta.get("canonical_original") if page.meta else None
    if page.meta and page.meta.get("translation_placeholder") and original:
        page.canonical_url = urljoin(config.site_url, original.lstrip("/"))

    locale = _home_locale(page.url)
    if page.url == "" or locale:
        structured_data = _home_structured_data(page, config, locale)
        context["detai_structured_data"] = json.dumps(
            structured_data, ensure_ascii=False, separators=(",", ":")
        ).replace("</", "<\\/")
        context["detai_hreflang"] = [
            {"lang": language, "url": urljoin(config.site_url, f"{language}/")}
            for language in HOME_LOCALES
        ] + [{"lang": "x-default", "url": config.site_url}]
    return context


def remove_translation_placeholders_from_sitemap(*, config) -> None:
    """Фильтрует noindex routes и создаёт locale sitemaps для instant navigation."""
    sitemap_path = Path(config.site_dir) / "sitemap.xml"
    if not sitemap_path.exists():
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
    _gzip_file(sitemap_path)

    site_url = config.site_url.rstrip("/")
    serialized_root = ElementTree.tostring(root, encoding="utf-8")
    for locale in HOME_LOCALES:
        locale_root = ElementTree.fromstring(serialized_root)
        locale_prefix = f"{site_url}/{locale}/"
        for url_element in list(locale_root):
            location = url_element.find(location_tag)
            if location is None or not (location.text or "").startswith(locale_prefix):
                locale_root.remove(url_element)

        locale_sitemap = Path(config.site_dir) / locale / "sitemap.xml"
        locale_sitemap.parent.mkdir(parents=True, exist_ok=True)
        ElementTree.ElementTree(locale_root).write(
            locale_sitemap, encoding="utf-8", xml_declaration=True
        )
        _gzip_file(locale_sitemap)


def _gzip_file(path: Path) -> None:
    with path.open("rb") as source, gzip.open(path.with_suffix(".xml.gz"), "wb") as destination:
        destination.write(source.read())
