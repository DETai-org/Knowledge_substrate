---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: knowledge-system
  layer: technical-standards
  function: standard
  system: knowledge
  domain: object-status
  audiences: [team, editors, product, agents]
descriptive:
  id: detai-object-status-model
  version: v1
  status: active
  date_ymd: 2026-08-05
governance:
  canonicality: canonical
  visibility: public
  owner_role: knowledge-architect
  approver_role: ecosystem-architect
  review_date: 2026-09-05
object_state:
  architecture_status: canonical
  implementation_status: operational
  evidence_status: not-applicable
  visibility_status: public
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: governs
      linked_document_id: knowledge-document-model
    - schema: ecosystem
      link_type: governs
      linked_document_id: management-layer-docs-ecosystem-document-metadata-policy
title: Многомерная модель статуса объекта
---

# Многомерная модель статуса объекта

Одного поля `status` недостаточно: документ может быть действующим, а описываемый продукт — только гипотезой; архитектура может быть утверждена, а реализация ещё не начата.

## Четыре измерения

| Измерение | Допустимые значения | Главный вопрос |
|---|---|---|
| `architecture_status` | `canonical`, `approved-target`, `experiment`, `hypothesis`, `deprecated`, `retired` | Какое место объект занимает в принятой архитектуре? |
| `implementation_status` | `not-started`, `in-design`, `prototype`, `controlled-pilot`, `commercial-beta`, `operational`, `paused`, `closed` | В каком состоянии исполнение? |
| `evidence_status` | `untested`, `preliminary-support`, `supported`, `validated-within-scope`, `contested`, `contradicted`, `not-applicable` | Насколько подтверждены связанные claims? |
| `visibility_status` | `public`, `team`, `restricted`, `legal-privileged`, `personal-data` | Кому допустимо видеть объект или его представление? |

## Связь со статусом документа

`descriptive.status` описывает жизненный цикл Markdown-документа: `draft`, `active`, `superseded` и так далее. `object_state` описывает сущность, о которой говорит документ. Эти поля не выводятся друг из друга автоматически.

```yaml
descriptive:
  status: active
object_state:
  architecture_status: hypothesis
  implementation_status: prototype
  evidence_status: untested
  visibility_status: team
```

Такой пример означает: действующая страница честно и канонически описывает командный прототип, который остаётся непроверенной гипотезой.

## Правила применения

1. `object_state` добавляется только после содержательного review.
2. Неизвестное состояние не угадывается; отсутствие поля честнее ложной точности.
3. Evidence status относится к явно определённым claims и scope.
4. Visibility metadata не заменяет технический access control.
5. Смена статуса требует даты, основания, owner и при необходимости decision record.
6. Публичное представление не может показывать более зрелое состояние, чем канонический объект.
