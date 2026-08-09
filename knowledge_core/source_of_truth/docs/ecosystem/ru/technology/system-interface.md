---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: technology-layer
  layer: architecture-and-logic
  function: explanation
  system: technology
  domain: uli-platform-interface
  audiences: [team, developers, product, agents]
descriptive:
  id: technology-system-interface
  version: v2
  status: active
  date_ymd: 2026-08-05
  date_update: 2026-08-09
governance:
  canonicality: canonical
  visibility: public
  owner_role: technical-lead
  approver_role: ecosystem-architect
  review_date: 2026-09-05
links:
  external_links: []
  document_links:
    - schema: ecosystem
      link_type: connects
      linked_document_id: detai-u-l-i-index
    - schema: ecosystem
      link_type: connects
      linked_document_id: detai-platform-detai-index
title: U.L.I., Platform DETai, производственный и продуктовый циклы
---

# U.L.I., Platform DETai, производственный и продуктовый циклы

## Разделение ответственности

| Контур | Владеет | Не владеет |
|---|---|---|
| U.L.I. | architecture, development process, standards, evaluation, release evidence | customer relationships, corporate authority, whole-ecosystem strategy |
| Platform DETai | shared capabilities, product runtime, delivery, user experience, analytics | методологическая истина, Governance, Team OS |
| Product–Market | ценностная значимость публичных продуктов, offers, показатели, portfolio evidence и выборочные discovery-процессы | техническая реализация и обязательная проверка каждой ранней идеи |
| Trust | intended use, controls, risk and release gates | продуктовая ценность и roadmap целиком |
| Evidence | claims, evidence quality, limitations and snapshots | принятие продуктового решения вместо owner role |

## Два связанных цикла

### Производственный цикл U.L.I.

1. Мысль развивается в «🧠 Ещё мысль» существующего проекта или в R&D Idea Lab.
2. Если возникает отдельный проект, он получает собственный репозиторий и рабочий контур: один репозиторий — один проект.
3. U.L.I. проводит Work Model Planning, Implementation и Release Fixation.
4. Версии `v0.x` могут оставаться внутренними; стабильное состояние фиксируется как `v1.0` или следующая версия.
5. Platform DETai развёртывает и доставляет утверждённое публичное состояние, если проект предназначен пользователям.

Раннее движение не требует обязательного customer discovery. Достаточно инициативы участника, согласованности с миссией, ценностями и принципами DETai и понимания того, какой ресурс экосистемы может быть создан.

### Продуктовый цикл Product–Market

1. Когда проект готовится к публичному `v1.0`, он обозначается как Product Candidate.
2. Владелец проекта и Product–Market формулируют ценностную значимость, аудиторию, доступ и показатели наблюдения.
3. Trust, Legal, Evidence и профессиональные роли подключаются соразмерно реальному intended use и риску.
4. После публичного релиза Product–Market наблюдает использование, пользовательский результат, ресурсный вклад, доход и устойчивость.
5. Наблюдения возвращаются владельцу проекта и могут стать материалом следующего dev-цикла.
6. Следующий релиз обновляет продукт и запускает проверку его документации, ценностной формулировки и публичной страницы.

Customer discovery остаётся отдельным доступным инструментом для специально выбранных портфельных гипотез, но не является обязательным началом каждого проекта.

## Точка соединения

| Событие | Ответственность U.L.I. | Ответственность Product–Market |
|---|---|---|
| Идея или `v0.x` | Создать и проверить проектное решение | Не обязан подключаться |
| Подготовка публичного `v1.0` | Подтвердить техническую готовность | Зафиксировать ценность, аудиторию, доступ и метрики |
| Публичный релиз | Доставить стабильную версию | Начать наблюдение продукта |
| Следующий major-релиз | Обновить production-состояние | Пересмотреть ценность, показатели и публичное представление |

Полная карта находится в [производственном цикле проектов](../ecosystem/DETai/U.L.I/2_Architecture_and_Logic/production-cycle.md) и [модели продуктового объекта](../product-market/product-object-model.md).

## Интерфейс с Team OS

U.L.I. может выпускать contribution evidence: merged change, утверждённый документ, evaluation result или release. Team OS связывает эти события с ролями и результатами по всей экосистеме. Ни одна система не превращает событие в долю или экономическое право автоматически.

## Интерфейс с книгой

Глава «Методоориентированная AI-инфраструктура» описывает, почему психотерапевтическому методу нужна связная технологическая среда. U.L.I. и Platform DETai являются конкретными ответами DETai на этот вопрос. Их текущая реализация может меняться, не меняя универсального тезиса главы.
