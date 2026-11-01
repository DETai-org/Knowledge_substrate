---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: company-and-economy
  layer: architecture-and-logic
  function: index
  system: legal-economic
  domain: company-and-economy
  audiences: [public, team, managers, agents]
descriptive:
  id: company-economy-index
  version: v3
  status: draft
  date_ymd: 2026-11-02
  date_update: 2026-11-02
governance:
  canonicality: working
  visibility: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/company-and-economy/
  document_links:
    - schema: ecosystem
      link_type: contains
      linked_document_id: detai-company-operator
    - schema: ecosystem
      link_type: contains
      linked_document_id: company-economy-slicing-pie
    - schema: ecosystem
      link_type: coordinates-with
      linked_document_id: brand-and-communications-domain
    - schema: ecosystem
      link_type: coordinates-with
      linked_document_id: infrastructure-ecosystem-runtime
title: Company & Economy
---

# Company & Economy

**Company & Economy** — направление экосистемы DETai, отвечающее за её экономическое и корпоративное развитие: финансы, коммерческую деятельность, юридические вопросы, собственность, инвестиции и распределение экономических ресурсов. Обеспечивает условия для устойчивого развития экосистемы и реализации её предпринимательских инициатив.

## Состав раздела

- [Планируемый оператор DETai Oy](company-operator.md) — будущая юридическая и экономическая роль компании, финская предпринимательская среда и возможные направления её развития.
- [Slicing Pie](slicing-pie.md) — идея динамического распределения долей участия, пока не являющаяся принятой политикой DETai.

## Коммерческая система DETai

**Company & Economy** рассматривает коммерческую деятельность продуктов и услуг через экономические условия, финансовые результаты, обязательства и устойчивость экосистемы. Предложения и их ценность формируются совместно с соответствующими продуктами и [Brand & Communications](https://docs.detai-x.com/ru/brand-and-communications/); эта перспектива не означает владения технической реализацией платежей.

**Commerce Core** — общий технический контур коммерческих операций DETai: предложений, заказов, подтверждённых платежей, платных периодов, отмен и возвратов. Он предоставляется разным продуктам через согласованные интерфейсы и технически принадлежит [ecosystem-runtime](https://docs.detai-x.com/ru/infrastructure/ecosystem-runtime/) в [Infrastructure](https://docs.detai-x.com/ru/infrastructure/). Экономическая ответственность Company & Economy не превращает Commerce Core в отдельную компанию или подчинённое ей техническое подразделение.

В целевой модели данных `identity` отвечает за единую идентичность, `commerce` — за коммерческие факты, `access` — за общие основания доступа, а конкретный продукт — за свои возможности и ограничения. Выделение PostgreSQL-схемы `commerce` из существующего контура `access` является направлением технического развития, а не утверждением о завершённом переносе.

Финансовый вклад продуктов рассматривается как одна из проекций общей [модели ресурсов экосистемы](https://docs.detai-x.com/ru/management-layer/ecosystem-resources/), которая остаётся в Management Layer. Платёжный реестр при этом не заменяет бухгалтерский учёт и юридическое оформление обязательств.

## Связь с другими направлениями

[Brand & Communications](../brand-and-communications/index.md) формирует ценностные
предложения, развивает бренд и связь с аудиторией. Company & Economy обеспечивает
экономические и корпоративные условия реализации этих предложений.
[Management Layer](../management-layer/index.md) согласует работу направлений,
ресурсы и междоменные зависимости в рамках [Governance](../governance/index.md).
