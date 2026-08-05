---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: product-market-system
  layer: operating-model
  function: decision-record
  system: product-market
  domain: portfolio-decisions
  audiences: [team, founders, product, agents]
descriptive:
  id: detai-lead-product-decision
  version: v1
  status: draft
  date_ymd: 2026-08-05
governance:
  canonicality: working
  visibility: public
  owner_role: product-market-owner
  approver_role: founder
  review_date: 2026-08-20
object_state:
  architecture_status: hypothesis
  implementation_status: in-design
  evidence_status: untested
  visibility_status: public
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: depends-on
      linked_document_id: detai-business-thesis
    - schema: ecosystem
      link_type: constrains
      linked_document_id: detai-product-catalog
title: Выбор lead product
---

# Выбор lead product

## Состояние решения

Lead product DETai пока **не утверждён**. Для customer discovery приоритет получает гипотеза `DETai Insight Workspace`. Это разрешает сфокусированное исследование, но не создаёт General Availability, clinical claim или обязательство строить весь портфель вокруг неё.

## Кандидаты и их текущая роль

| Кандидат | Текущая роль | Что уже можно утверждать |
|---|---|---|
| Psychology in Quotes | существующий публичный продукт | продукт доступен и может давать фактические данные использования |
| DETai Insight Workspace | priority discovery hypothesis | разрешены problem interviews, concept testing и безопасное прототипирование |
| Professional Knowledge capabilities | capability / возможная соседняя линия | может проверяться как часть professional mode или отдельная будущая гипотеза |

## Рабочий intended use гипотезы P1

`DETai Insight Workspace` предназначается для добровольной психологической саморефлексии, psychoeducation и non-clinical professional workflow support. Он может помогать структурировать self-report results, наблюдения и подготовку обсуждения со специалистом.

Первая версия не должна устанавливать медицинский или психиатрический диагноз, назначать лечение, заменять профессиональное клиническое решение или выдавать непроверенную интерпретацию как валидированный результат.

## Gate решения

До утверждения lead product необходимы:

- подтверждённая проблема и первый сегмент;
- разделение user, buyer, payer и beneficiary;
- сравнение с существующими альтернативами;
- проверяемое ценностное предложение;
- willingness-to-pay или иное evidence устойчивости;
- intended и excluded use;
- instrument, IP, data и Trust feasibility;
- прототип и план controlled pilot;
- предварительная экономика и связь с Platform DETai;
- явные pivot и kill criteria.

## Право решения

Product–Market owner собирает evidence и рекомендацию. Technology, Trust, Method/Professional, Evidence и Legal дают обязательные reviews в своих границах. Финальное портфельное решение принимается в действующей Governance-модели и получает срок следующего пересмотра.

До прохождения gate сайт и внешние материалы называют P1 гипотезой или направлением разработки, а не доказанным основным продуктом DETai.
