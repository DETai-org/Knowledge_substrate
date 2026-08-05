---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: product-market-system
  layer: cross-cutting-system
  function: standard
  system: product-market
  domain: product-documentation
  audiences: [team, product, developers, support, agents]
descriptive:
  id: product-documentation-model
  version: v1
  status: draft
  date_ymd: 2026-08-05
governance:
  canonicality: working
  visibility: public
  owner_role: product-market-owner
  approver_role: knowledge-architect
  review_date: 2026-08-20
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: implements
      linked_document_id: product-object-model
    - schema: ecosystem
      link_type: constrains
      linked_document_id: detai-product-catalog
title: Модель документации продукта
---

# Модель документации продукта

У каждого зрелого продукта или услуги DETai есть собственный документационный узел. Он отвечает и человеку, и агенту на четыре разных вопроса: **что это, как этим пользоваться, почему это допустимо и как это устроено**.

## Обязательные представления

| Представление | Главный вопрос | Типичное содержание |
|---|---|---|
| Product overview / Charter | Что это за продукт и для кого он существует? | назначение, аудитория, owner, lifecycle, value proposition, status |
| Пользовательская документация | Как получить результат? | начало работы, сценарии, инструкции, FAQ, ограничения, поддержка |
| Trust и ответственное использование | Когда и как продукт допустимо применять? | intended/excluded use, данные, privacy, oversight, risks, claims, release status |
| Техническая документация | Как продукт устроен и интегрируется? | архитектура, API, конфигурация, deployment, observability, runbooks |
| Offer и Evidence | Что именно предлагается и чем подтверждено? | доступ, price/terms, пилоты, metrics, evidence, ограничения обещаний |

Не каждому раннему эксперименту нужны пять отдельных страниц. Представления можно временно объединять, но их вопросы и владельцы не должны смешиваться.

## Правило размещения

Каноническая документация живёт **рядом с owning system**:

- цифровой продукт Platform DETai — в его продуктовой ветке;
- образовательная программа — в образовательном контуре институционального слоя;
- психотерапевтическая услуга — в контуре практики и супервизии;
- общая capability — рядом с технологической или knowledge-инфраструктурой.

[Каталог продуктов](product-catalog.md) не копирует эти страницы, а собирает связи и сравнимые статусы. Product–Market System владеет общими требованиями к Product Object, ценностному предложению, offer и lifecycle, но не присваивает себе локальную документацию продукта.

## Минимальный маршрут пользователя

Запрос вида «как пользоваться Психологией в цитатах?» должен приводить прямо к пользовательскому руководству продукта, а не к бизнес-модели DETai. На обзорной странице продукта должны быть видны:

1. короткое обещание результата;
2. кнопка или ссылка «Начать»;
3. пошаговые сценарии;
4. ограничения и ответственное использование;
5. поддержка и обратная связь;
6. статус версии и дата актуальности.

## Маршрут агента

Агент должен уметь пройти от каталога к Product Object, затем к пользовательскому сценарию, Trust-гейту, evidence и технической реализации. Связи фиксируются стабильными document IDs и relation types, а не только положением страницы в меню.

## Граница публичности

Публичные инструкции, ограничения и claims находятся в Knowledge Substrate или на сайте продукта. Секреты, персональные данные, уязвимости, договорные оригиналы и эксплуатационные ключи остаются в соответствующих закрытых источниках истины.
