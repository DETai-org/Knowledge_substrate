---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: product-market-system
  layer: architecture-and-logic
  function: standard
  system: product-market
  domain: product-object
  audiences: [team, product, managers, agents]
descriptive:
  id: product-object-model
  version: v1
  status: draft
  date_ymd: 2026-08-05
governance:
  canonicality: working
  visibility: public
  owner_role: product-market-owner
  approver_role: operating-model-owner
  review_date: 2026-08-20
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: product-market-index
title: Модель продуктового объекта
---

# Модель продуктового объекта

Product Object — минимальная управляемая единица продукта или услуги. Эта модель нужна, чтобы идея, проект, приложение и действующее предложение не назывались одним словом «продукт».

## Обязательные поля Product Charter

1. **Identity** — имя, тип и место в портфеле.
2. **Owner** — одна роль, отвечающая за целостность решения.
3. **Audience** — пользователь, покупатель, плательщик, бенефициар и затронутые стороны.
4. **Problem** — подтверждаемая проблема или потребность.
5. **Value proposition** — результат и причина выбрать предложение.
6. **Intended use / non-intended use** — допустимые и недопустимые сценарии.
7. **Delivery model** — канал, сервисный процесс и необходимые capabilities.
8. **Method and institutional dependencies** — профессиональные роли, образование, супервизия, исследование.
9. **Technology dependencies** — U.L.I., Platform DETai, данные и runtime.
10. **Trust gates** — риск, human oversight, privacy, safety и release conditions.
11. **Business logic** — payer, revenue, costs и допущения устойчивости.
12. **Evidence and metrics** — claims, baselines, outcomes и ограничения.
13. **Lifecycle state** — hypothesis, discovery, pilot, active, scaling, paused или retired.

## Различение состояний

- **Idea** ещё не имеет согласованного charter.
- **Initiative** имеет owner и ограниченную цель изменения.
- **Project** организует временную работу.
- **Product Object** сохраняет идентичность на протяжении жизненного цикла.
- **Release** является конкретной версией доставляемого результата.

Репозиторий, Telegram-бот или страница могут быть компонентами продукта, но не определяют продукт автоматически.

## Связь с другими реестрами

Product Object ссылается на decision records, claims, evidence, risks, releases, владельцев и действующие legal objects. Он не дублирует эти объекты, а связывает их вокруг конкретного предложения.
