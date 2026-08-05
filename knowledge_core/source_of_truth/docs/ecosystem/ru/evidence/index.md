---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: evidence-system
  layer: cross-cutting-system
  function: explanation
  system: evidence
  domain: system-overview
  audiences: [public, team, researchers, product, agents]
descriptive:
  id: evidence-system-index
  version: v2
  status: active
  date_ymd: 2026-08-05
governance:
  canonicality: canonical
  visibility: public
  owner_role: evidence-owner
  approver_role: research-methodology-owner
  review_date: 2026-09-05
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: implements
      linked_document_id: cross-cutting-systems
    - schema: ecosystem
      link_type: contains
      linked_document_id: venture-execution-view
title: Evidence, Learning и External Readiness
---

# Evidence, Learning и External Readiness

Evidence System делает утверждения DETai проверяемыми, ограниченными по контексту и связанными с источниками. Она объединяет научное, продуктово-рыночное, техническое, операционное и организационное evidence, не смешивая их стандарты качества.

## Объекты

- **Claim** — что именно утверждается.
- **Evidence Item** — наблюдение, документ, данные, исследование или проверка.
- **Evidence Link** — поддерживает, опровергает, ограничивает или лишь контекстуализирует claim.
- **Limitation** — где вывод перестаёт быть применимым.
- **Snapshot** — состояние evidence на дату и для конкретной версии.
- **Decision** — что было решено на основании доступного evidence.

## Разные виды evidence

Технический test подтверждает поведение реализации, но не клинический outcome. Интервью подтверждает существование опыта или проблемы, но не размер рынка. Метрика использования показывает действие, но не обязательно ценность. Научная публикация может поддерживать общий механизм, но не автоматически конкретный продукт.

## Зачем это нужно публичности

Амбициозная подача DETai становится сильнее, когда читатель видит, что vision, current reality и evidence-backed claims не маскируются друг под друга. Для каждого внешнего контекста создаётся [readiness snapshot](external-readiness.md), а не новая несвязанная версия правды.

[Venture Execution View](venture-execution-view.md) собирает предпринимательскую готовность из канонических источников и датированных evidence. Он позволяет показать компанию, продукт, рынок, активы и план без сведения всей экосистемы к заявке или одному приложению.

## Где продолжить

- [Граф claim → evidence → decision](claim-evidence-graph.md)
- [External Readiness](external-readiness.md)
- [Venture Execution View](venture-execution-view.md)
