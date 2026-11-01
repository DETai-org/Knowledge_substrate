---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: platform
  layer: technology
  function: index
  system: platform-detai
  domain: archive
  audiences: [team, product, developers, agents]
descriptive:
  id: detai-platform-detai-dormant-projects-index
  version: v2
  status: active
  date_ymd: 2026-11-01
  date_update: 2026-11-01
governance:
  canonicality: canonical
  visibility: public
  owner_role: technical-lead
  approver_role: ecosystem-architect
  review_date: 2026-09-09
object_state:
  architecture_status: canonical
  implementation_status: operational
  evidence_status: not-applicable
  visibility_status: public
links:
  external_links:
    - type: "MkDocs_ru"
      url: "https://docs.detai-x.com/ru/technology/platform/archive/"
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: detai-platform-detai-index
title: Archive
---

# Archive

**Archive — проекты, у которых сохранены репозиторий и проектная идентичность, а сам репозиторий в организации DETai на GitHub имеет статус archived.** Здесь остаются исходный замысел, история и полезные материалы проекта.

## Три состояния инициативы

| Категория | Что означает |
|---|---|
| R&D Idea Lab | Идея или ранний эксперимент, который ещё не получил собственного репозитория и самостоятельного проектного контура |
| Active Project | Самостоятельный проект с репозиторием, который ведётся в рабочем контуре разработки или поддержки |
| Archive | Самостоятельный проект, чей репозиторий архивирован в GitHub; его идентичность и история сохранены |

Архивирование сохраняет историю проекта. Возобновление возможно по отдельному решению: репозиторий выводится из архива, уточняется назначение и запускается новый цикл разработки.

## Проекты архива

- [GPT Prompt Engine](gpt-prompt-engine/index.md) — генерация и сборка промтов для других систем.
- [News Agent](news-agent/index.md) — исходная идея отбора новостей и подготовки кратких смысловых карточек.

## Что сохраняется

Страница архивного проекта удерживает его назначение, создаваемый ресурс, последнее известное состояние и условия возможного возобновления. Репозиторий сохраняет исходный код и историю; сведения о владении и рабочие ссылки ведутся в соответствующем командном контуре.

## Возобновление

Нужно принять решение о продолжении, вывести репозиторий из архива GitHub, назначить ответственного, проверить состояние кода и потребителей, обновить Project Intent и начать новый [производственный цикл U.L.I.](../../production-cycle/index.md). Готовность к пилоту и публичному выпуску определяется по результатам этого цикла.
