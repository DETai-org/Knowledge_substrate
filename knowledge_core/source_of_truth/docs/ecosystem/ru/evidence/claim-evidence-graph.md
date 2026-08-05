---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: evidence-system
  layer: architecture-and-logic
  function: standard
  system: evidence
  domain: claim-evidence-graph
  audiences: [team, researchers, product, agents]
descriptive:
  id: claim-evidence-graph
  version: v1
  status: draft
  date_ymd: 2026-08-05
governance:
  canonicality: working
  visibility: public
  owner_role: evidence-owner
  approver_role: research-methodology-owner
  review_date: 2026-08-20
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: evidence-system-index
title: Граф claim → evidence → decision
---

# Граф claim → evidence → decision

## Минимальная модель

```text
Claim
  ├─ supported_by → Evidence Item
  ├─ contradicted_by → Evidence Item
  ├─ limited_by → Limitation
  ├─ applies_to → Product / Method / Organization / Market
  └─ used_in → Decision / Publication / Page / Application
```

Каждый объект получает стабильный ID, owner, status, дату, область применимости и provenance. Evidence Item дополнительно содержит метод получения, quality assessment и допустимость публичного раскрытия.

## Статусы claim

- `vision` — желаемое направление;
- `hypothesis` — проверяемое предположение;
- `descriptive` — описание существующего объекта;
- `supported` — имеет достаточное evidence для указанного контекста;
- `contested` — существенные свидетельства расходятся;
- `deprecated` — больше не должно использоваться;
- `superseded` — заменено более точным claim.

## Правило повторного использования

Сайт, книга, научная статья, grant application и pitch могут по-разному объяснять один claim, но должны ссылаться на один и тот же объект и snapshot. Перефразирование не позволяет убрать limitation или повысить статус доказанности.

## Агентный интерфейс

Агент должен уметь ответить: «какие claims есть у этого продукта?», «какой snapshot поддерживает страницу?», «что изменилось с прошлого review?» и «какие публичные формулировки сильнее evidence?». Поэтому граф является отдельной системой, а не набором ссылок в тексте.
