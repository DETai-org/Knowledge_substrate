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
  version: v4
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-08-20
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
    - schema: ecosystem
      link_type: interfaces-with
      linked_document_id: team-os-contribution-ledger
    - schema: ecosystem
      link_type: delivered-by
      linked_document_id: detai-platform-detai-index
title: Storytelling — Publication Core
---

# Storytelling — Publication Core

**Storytelling — самостоятельный редакционно-технологический проект и Publication Core DETai с [собственным репозиторием](https://github.com/DETai-org/Storytelling). Он принимает подготовленные материалы, проводит их через обогащение и review, собирает версионированные публикационные пакеты и доставляет утверждённый результат в выбранные публичные каналы.**

Storytelling относится к направлению [«Бренд и внешние коммуникации»](../DETai/Platform_DETai/brand-and-external-communications/index.md) и является его внутренней производственной системой. Он не является публичной поверхностью или самостоятельным пользовательским продуктом: система может участвовать в создании продукта, публикации или другого результата, но пользователь получает этот результат через сайт, Telegram или другую площадку.

Организационно Storytelling остаётся самостоятельным E2-проектом с собственным репозиторием, версиями и циклом развития. Проект относится к операционному домену [Brand & Communications](../../governance/brand-and-communications.md): домен определяет аудитории, редакционные рамки и согласованность, а Storytelling воплощает публикационный процесс в повторяемой рабочей и технической системе.

## Редакционная среда, Publication Core и каналы

| Уровень | Роль |
|---|---|
| **Редакционная рабочая среда** | Идея, черновик, обсуждение, автор, назначение и подготовка материала; сейчас Storytelling принимает материалы из папки ClickUp [STORYTELLING (TimeOS) для текстов](https://app.clickup.com/90152202658/v/f/901515038276/901510140866), а в дальнейшем этот контур может стать частью TimeOS / [Team OS](../../governance/team-os.md) |
| **Storytelling как Publication Core** | Репозиторий, оркестрация, интеграции, обогащение, локализация, review, версионирование и сборка публикационного пакета |
| **Продуктовый результат проекта** | Пост, серия постов, публикационный пакет, Markdown, metadata и media assets |
| **Площадка публикации** | Блог основного или персонального сайта, Telegram, VK, а в будущем YouTube, Habr или другой внешний канал |

Публикация является продуктовым результатом Storytelling. При этом отдельный пост не становится самостоятельным Product Object DETai автоматически: отдельный Product Object нужен только для поддерживаемого публичного предложения с собственной аудиторией, ценностью, владельцем и показателями.

```text
идея и черновик в редакционной рабочей среде
→ подготовленный исходный материал
→ Storytelling / Publication Core
→ enrichment, локализация, review и публикационный пакет
→ адаптеры площадок
→ сайт, Telegram, VK, YouTube, Habr и другие каналы
→ обратная связь в редакционную среду
```

[Рабочая среда участника](../../start/working-environment.md) связывает знания, задачи, код и runtime как маршрут, но не переносит их в один общий контейнер. Аналогично TimeOS может стать местом совместной редакционной работы, не забирая у Storytelling публикационную бизнес-логику и код.

На текущем этапе операционной точкой передачи исходного материала является папка ClickUp [STORYTELLING (TimeOS) для текстов](https://app.clickup.com/90152202658/v/f/901515038276/901510140866). Эта ссылка фиксирует действующий вход в процесс, а не постоянную техническую зависимость Publication Core от ClickUp.

## Что поставляет Storytelling

- локализованные Markdown-материалы и metadata;
- обложки и другие media assets;
- публикационные пакеты для сайта и социальных каналов;
- версии, результаты review и машинно-проверяемые контракты доставки;
- заготовки, которые после отдельного научного review могут стать Research Papers.

Переход текста в научную публикацию не происходит автоматически: research claim, evidence и формат публикации проверяются соответствующими научными и Evidence-ролями.

## Редакционная и техническая эстафета

```text
идея или наблюдение в редакционной рабочей среде
→ подготовка исходного материала
→ передача в Storytelling
→ редакционное и предметное review
→ сборка публикационного пакета
→ выбор одного или нескольких каналов
→ публикация
→ обратная связь и следующая версия материала
```

Текущая реализация репозитория включает контур навигации и публикации для Telegram и VK, циклы постов и интеграции с Google Docs. Целевой блоговый pipeline должен готовить Markdown, frontmatter и media, совместимые с контрактами репозитория `sites`.

Техническое выполнение LLM-шагов не делает Storytelling частью LLM-инфраструктуры. Предметные правила и публикационный процесс остаются в Storytelling, а общая техническая оркестрация моделей принадлежит intelligence-runtime. Эта граница подробно показана на странице [«Как Storytelling использует технологическую основу»](technology-foundation.md).

## Связь с сайтом

[Сайт DETai](../DETai/Platform_DETai/E2-Brand/sites/index.md) — одна из площадок публикации и один из потребителей Storytelling. Он принимает подготовленный post object, Markdown и media-файлы, после чего репозиторий `sites` самостоятельно собирает страницу, маршруты, SEO, Open Graph, structured data и deployment. Сайт не выполняет enrichment, переводы, редакционное review и сборку исходного публикационного пакета.

Та же публикационная версия может передаваться в Telegram, VK, YouTube, Habr и будущие площадки через их адаптеры. Storytelling остаётся единым Publication Core, а техническая доставка и отображение на каждой площадке принадлежат владельцу соответствующего канала.

Граница ответственности:

- изменение кода подготовки публикационного пакета маршрутизируется владельцу Storytelling;
- изменение редакционного процесса маршрутизируется Brand & Communications;
- изменение runtime-кода блога маршрутизируется владельцу проекта `sites`;
- изменение смысла конкретного материала возвращается его автору и предметному owner;
- публикация одного материала в нескольких каналах проверяется на согласованность формулировок, ссылок и CTA.

## Рабочее состояние

Автор, редактор, срок, статус и набор каналов фиксируются в ClickUp или утверждённой management runtime. Эта страница хранит устойчивое определение проекта и его связей, а не текущий редакционный календарь.
