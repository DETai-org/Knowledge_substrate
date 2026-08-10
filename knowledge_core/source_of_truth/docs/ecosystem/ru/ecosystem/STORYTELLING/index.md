---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: brand-and-communications
  layer: operating-model
  function: project
  system: governance-operating-model
  domain: storytelling
  audiences: [team, brand, authors, developers, agents]
descriptive:
  id: storytelling-index
  version: v2
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-08-09
governance:
  canonicality: canonical
  visibility: public
  owner_role: brand-communications-owner
  approver_role: founder
  review_date: 2026-09-09
object_state:
  architecture_status: canonical
  implementation_status: operational
  evidence_status: not-applicable
  visibility_status: public
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/STORYTELLING/"
    - type: "GitHub"
      url: "https://github.com/DETai-org/Storytelling"
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: brand-and-communications-domain
    - schema: ecosystem
      link_type: published-through
      linked_document_id: detai-platform-detai-e2-brand-sites-index
title: Storytelling
---

# Storytelling

**Storytelling — самостоятельный редакционно-технологический проект DETai с [собственным репозиторием](https://github.com/DETai-org/Storytelling). Он превращает идеи и исходные материалы в подготовленные публикации и доставляет их в публичные каналы.**

Проект относится к операционному домену [Brand & Communications](../../governance/brand-and-communications.md), но не сводится к общему разговору о бренде. В репозитории живут процессы, интеграции, автоматизация и кодовая бизнес-логика публикационного контура.

## Проект, результат и канал

| Уровень | Роль |
|---|---|
| **Storytelling как проект** | Репозиторий, редакционные процессы, интеграции и автоматизация |
| **Продуктовый результат проекта** | Пост, серия постов, публикационный пакет, Markdown, metadata и media assets |
| **Канал доставки** | Блог основного или персонального сайта, Telegram, VK, а в будущем YouTube или другой канал |

Публикация является продуктовым результатом Storytelling. При этом отдельный пост не становится самостоятельным Product Object DETai автоматически: отдельный Product Object нужен только для поддерживаемого публичного предложения с собственной аудиторией, ценностью, владельцем и показателями.

## Что создаёт Storytelling

- идеи, сюжеты и смысловые линии;
- черновики постов и серий публикаций;
- истории о проектах, людях, исследованиях и развитии DETai;
- локализованные Markdown-материалы и metadata;
- обложки и другие media assets;
- публикационные пакеты для сайта и социальных каналов;
- заготовки, которые после отдельного научного review могут стать Research Papers.

Переход текста в научную публикацию не происходит автоматически: research claim, evidence и формат публикации проверяются соответствующими научными и Evidence-ролями.

## Редакционная и техническая эстафета

```text
идея или наблюдение
→ разработка материала в Storytelling
→ редакционное и предметное review
→ сборка публикационного пакета
→ выбор одного или нескольких каналов
→ публикация
→ обратная связь и следующая версия материала
```

Текущая реализация репозитория включает контур навигации и публикации для Telegram и VK, циклы постов и интеграции с Google Docs. Целевой блоговый pipeline должен готовить Markdown, frontmatter и media, совместимые с контрактами репозитория `sites`.

## Связь с сайтом

[Сайт DETai](../DETai/Platform_DETai/E2-Brand/sites/index.md) принимает подготовленный post object, Markdown и media-файлы. Затем `sites` самостоятельно собирает страницу, SEO, Open Graph, structured data и deployment.

Граница ответственности:

- изменение кода подготовки публикационного пакета маршрутизируется владельцу Storytelling;
- изменение редакционного процесса маршрутизируется Brand & Communications;
- изменение runtime-кода блога маршрутизируется владельцу проекта `sites`;
- изменение смысла конкретного материала возвращается его автору и предметному owner;
- публикация одного материала в нескольких каналах проверяется на согласованность формулировок, ссылок и CTA.

## Рабочее состояние

Автор, редактор, срок, статус и набор каналов фиксируются в ClickUp или утверждённой management runtime. Эта страница хранит устойчивое определение проекта и его связей, а не текущий редакционный календарь.
