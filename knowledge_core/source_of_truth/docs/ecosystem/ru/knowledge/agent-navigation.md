---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: knowledge-system
  layer: architecture-and-logic
  function: guide
  system: knowledge
  domain: agent-navigation
  audiences: [team, developers, agents]
descriptive:
  id: agent-navigation
  version: v1
  status: draft
  date_ymd: 2026-08-05
governance:
  canonicality: working
  visibility: public
  owner_role: knowledge-architect
  approver_role: ecosystem-architect
  review_date: 2026-08-20
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: knowledge-system-index
title: Навигация для людей и агентов
---

# Навигация для людей и агентов

Меню MkDocs помогает человеку двигаться от целого к системе и документу. Агенту дополнительно нужен машинно-читаемый граф, который не зависит от порядка пунктов меню.

## Стартовый маршрут агента

1. Определить намерение запроса и затронутые systems.
2. Открыть [архитектурный канон](../architecture/ecosystem-canon.md).
3. Прочитать index каждой затронутой системы.
4. Отфильтровать документы по canonicality, status, visibility и audience.
5. Пройти `document_links` и связанные реестры.
6. Различить факт, правило, working model, hypothesis и historical context.
7. Назвать использованные источники и противоречия.

## Сквозной запрос

Запрос «можно ли выпустить AI-функцию для терапии?» не принадлежит одному разделу. Агент должен поднять как минимум Method, Institutional, Product–Market, Technology, Trust, Legal, Evidence и Governance. [Реестр сквозных систем](../architecture/cross-cutting-systems.md) задаёт такую маршрутизацию.

## Минимальные отношения графа

- `defines`, `implements`, `governs`, `constrains`;
- `depends-on`, `produces-evidence-for`, `reviewed-by`;
- `supersedes`, `contradicts`, `projects-to`;
- `part-of`, `owned-by`, `applies-to`.

## Защита от ложной полноты

Отсутствие ссылки не означает отсутствие зависимости. Агент должен сообщать, когда граф неполон, и не превращать working documents в канон. Выявленное устойчивое отношение возвращается владельцу Knowledge System для фиксации.
