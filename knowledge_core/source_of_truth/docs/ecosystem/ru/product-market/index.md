---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: product-market-system
  layer: cross-cutting-system
  function: explanation
  system: product-market
  domain: system-overview
  audiences: [public, team, product, agents]
descriptive:
  id: product-market-index
  version: v4
  status: active
  date_ymd: 2026-08-05
  date_update: 2026-08-09
governance:
  canonicality: canonical
  visibility: public
  owner_role: product-market-owner
  approver_role: founder
  review_date: 2026-09-05
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: implements
      linked_document_id: cross-cutting-systems
    - schema: ecosystem
      link_type: contains
      linked_document_id: detai-product-catalog
    - schema: ecosystem
      link_type: contains
      linked_document_id: product-documentation-model
    - schema: ecosystem
      link_type: contains
      linked_document_id: detai-business-thesis
    - schema: ecosystem
      link_type: contains
      linked_document_id: detai-lead-product-decision
title: Продукты, рынок и бизнес-модель
---

# Продукты, рынок и бизнес-модель

Product–Market System оформляет публичную ценность проектов и услуг DETai, наблюдает их использование и устойчивость и связывает продуктовые результаты с портфелем экосистемы. Она проходит через институциональный и технологический слои, но не подменяет ни метод, ни профессиональную ответственность, ни разработку.

## Что система удерживает

- сегменты, роли пользователя, покупателя, плательщика и бенефициара;
- пользовательские ситуации и задачи, для которых выпускаются продукты;
- собственное ценностное предложение каждого продукта или услуги и границы обещаний;
- минимальный паспорт каждого публичного продукта или услуги;
- портфель: create, continue, change, pause, stop или scale;
- каналы, отношения, revenue logic и cost logic;
- evidence того, что ценность создаётся, доставляется и может поддерживаться.

## Базовая единица

Экосистема DETai как целое не является одним продаваемым продуктом. Базовой единицей является конкретное публичное предложение: психотерапевтическая услуга, образовательная программа, цифровой сервис или иной оформленный продукт.

В технологическом контуре один репозиторий соответствует одному проекту. Не каждый проект становится продуктом: внутренняя инфраструктура и capabilities могут создавать значимый ресурс экосистемы без отдельного внешнего предложения. Переход проекта к публичному `v1.0` и [Product Object](product-object-model.md) описывается отдельно от производственного цикла U.L.I.

Umbrella Brand DETai объединяет происхождение и доверие, но не создаёт общего ценностного предложения вместо конкретных продуктов. Принцип описан в [стандарте ценностного предложения продукта](../ecosystem/Management_layer/1_Philosophy/product-and-service-value-proposition.md).

[Business Thesis DETai](business-thesis.md) удерживает гипотезу предпринимательского целого. Она не заменяет ценностные предложения продуктов: `Psychology in Quotes`, психотерапевтическая услуга, образовательная программа и возможный будущий цифровой workspace отвечают на разные пользовательские ситуации.

## Связь разработки и продукта

- U.L.I. владеет производственным циклом проекта: от мысли и реализации до Release Fixation и следующей версии.
- Product–Market подключается к обязательной работе при подготовке публичного `v1.0`, формулирует ценностную значимость и показатели, а после выпуска наблюдает фактический результат.
- Customer discovery используется только для специально выбранных исследовательских гипотез и не является обязательным началом каждого проекта.
- Следующая версия продукта возникает через новый производственный цикл того же проекта; при релизе Product–Market проверяет ценность, показатели и публичное представление.

## Где находится документация продуктов

- [Каталог продуктов и предложений](product-catalog.md) даёт единый обзор портфеля и ссылки на канонические узлы.
- [Модель документации продукта](product-documentation-model.md) разделяет обзор, пользовательские инструкции, Trust, техническую документацию, offer и evidence.
- Документы конкретного продукта остаются рядом с его owning system. Например, цифровые продукты находятся в ветке Platform DETai, а будущие профессиональные и образовательные предложения — в соответствующих контурах институционального слоя.

Так запрос пользователя «как пользоваться продуктом?» ведёт к руководству продукта, а не к общему описанию рынка или бизнес-модели.

`DETai Insight Workspace` не добавляется в каталог как действующий продукт или проект. Что означал его исследовательский приоритет и почему он не управляет текущей разработкой, объясняет [портфельное решение](portfolio-decisions/insight-workspace-customer-discovery.md).

## Интерфейсы

| Система | Вопрос на границе |
|---|---|
| [Метод и институт](../method/index.md) | Допустима ли ценность с профессиональной и методологической точки зрения? |
| [U.L.I. и Platform DETai](../technology/index.md) | Как решение создать, проверить и доставить? |
| [Governance](../governance/index.md) | Кто вправе определить приоритет и принять риск? |
| [Право и экономика](../legal-economic/index.md) | На каком основании предложение существует и монетизируется? |
| [Trust](../trust/index.md) | Как ограничить вред и подтвердить готовность выпуска? |
| [Evidence](../evidence/index.md) | Какие утверждения уже подтверждены и где их предел? |

## Где продолжить

- [Business Thesis DETai](business-thesis.md)
- [Портфельное решение: приоритет customer discovery](portfolio-decisions/insight-workspace-customer-discovery.md)
- [Каталог продуктов и предложений](product-catalog.md)
- [Модель документации продукта](product-documentation-model.md)
- [Стандарт ценностного предложения продукта](../ecosystem/Management_layer/1_Philosophy/product-and-service-value-proposition.md)
- [Модель продуктового объекта](product-object-model.md)
- [Рыночный и портфельный цикл](market-operations.md)
- [Бизнес-модель и портфель](business-model-and-portfolio.md)
