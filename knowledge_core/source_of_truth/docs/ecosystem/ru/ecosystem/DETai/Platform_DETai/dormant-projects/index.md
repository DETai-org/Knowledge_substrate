---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: platform
  layer: technology
  function: index
  system: platform-detai
  domain: dormant-projects
  audiences: [team, product, developers, agents]
descriptive:
  id: detai-platform-detai-dormant-projects-index
  version: v1
  status: active
  date_ymd: 2026-08-09
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
      url: "https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/DETai/Platform_DETai/dormant-projects/"
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: detai-platform-detai-index
title: Приостановленные проекты
---

# Приостановленные проекты / Dormant Projects

**Dormant Project — самостоятельный проект с owning repository, для которого сейчас не идёт активный производственный цикл, но решение о закрытии или архивировании не принято.**

Это состояние отличается от соседних категорий:

| Категория | Граница |
|---|---|
| R&D Idea Lab | Идея или ранний эксперимент ещё не получил собственного репозитория и проектного контура |
| Active Project | Есть владелец, текущая работа и активный производственный цикл |
| Dormant Project | Репозиторий и проектная идентичность сохранены, но работа приостановлена |
| Archived / Closed | Принято явное решение не продолжать проект; активное состояние закрыто |

Размещение здесь не означает отказ от проекта и не возвращает его в стадию идеи. Оно честно показывает, что проект «заморожен», и защищает каталог продуктов, R&D и активный портфель от ложного статуса.

## Минимальное описание dormant-проекта

Страница проекта должна указывать:

- owning repository;
- последний известный смысл и создаваемый ресурс;
- состояние `implementation_status: paused`;
- известного владельца либо `owner_role: not-assigned`;
- условие, при котором проект может быть возобновлён;
- является ли он внутренним проектом, Product Candidate или бывшим публичным продуктом.

## Возобновление

Для «разморозки» назначается владелец, подтверждается Project Intent, проверяется состояние репозитория и запускается новый производственный цикл U.L.I. Если проект должен стать публичным продуктом, Product–Market подключается к точке Product Candidate до публичного релиза.
