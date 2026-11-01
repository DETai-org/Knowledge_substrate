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
  version: v4
  status: active
  date_ymd: 2026-10-23
  date_update: 2026-11-01
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
| Product–Market | ценностная значимость оформленных продуктов, offers, показатели, portfolio evidence и выборочные discovery-процессы | техническая реализация и обязательная проверка каждой ранней идеи |
| Brand & Communications | бренд публичного продукта, коммуникация с аудиторией, сбор обратной связи и обсуждение направлений развития | техническая реализация следующих версий вместо U.L.I. |
| Management Layer | междоменная координация, назначение владельцев и синхронизация зависимых представлений | содержание ценностного предложения, техническая реализация и редакционная формулировка вместо owning domains |
| Trust | intended use, controls, risk and release gates | продуктовая ценность и roadmap целиком |
| Evidence | claims, evidence quality, limitations and snapshots | принятие продуктового решения вместо owner role |

## Производственный цикл U.L.I.

1. Мысль развивается в «🧠 Ещё мысль» существующего проекта или в R&D Idea Lab.
2. Если возникает отдельный проект, он получает собственный репозиторий и рабочий контур: один репозиторий — один проект.
3. U.L.I. проводит Work Model Planning, Implementation и Release Fixation.
4. Версии `v0.x` могут оставаться внутренними; стабильное состояние фиксируется как `v1.0` или следующая версия.
5. Platform DETai развёртывает и доставляет утверждённое публичное состояние, если проект предназначен пользователям.

Раннее развитие начинается с инициативы участника, согласованности с миссией, ценностями и принципами DETai и понимания того, какой ресурс экосистемы может быть создан.

Когда работающая версия готовится к публичному выпуску, проект проходит пилот с ограниченным кругом участников. После публичного `v1.0` Brand & Communications сопровождает бренд продукта, коммуникацию с аудиторией и обратную связь пользователей; вместе с командой проекта и Product–Market этот домен помогает определять направления дальнейшего развития. Этот процесс описан в [продуктовом цикле Product–Market](../governance/product-market-cycle.md). Технические улучшения проходят следующий [производственный цикл U.L.I.](../ecosystem/DETai/U.L.I/2_Architecture_and_Logic/production-cycle.md).

## Эстафета публичного релиза

| Сигнал | Кто передаёт | Кто принимает | Проверяемый результат |
|---|---|---|---|
| Проект готов к публичному `v1.0` или смысловому major-релизу | Владелец проекта и U.L.I. | Management Layer | Определены затронутые домены, владельцы и действия синхронизации |
| Требуется подтвердить продуктовую ценность | Management Layer | Команда пилота и Product–Market | Утверждены аудитория, ценностная формулировка, два вопроса, доступ и показатели |
| Требуется публичная проекция | Management Layer | Brand & Communications и владелец сайта / канала | Обновлены видимый текст, GEO/SEO, structured data, CTA и статус |
| Выпуск допущен | U.L.I., Trust и применимые owning domains | Platform DETai | Стабильная версия доставлена пользователям |
| Появились данные использования или новая гипотеза | Brand & Communications, Product–Market и команда продукта | Команда разработки U.L.I. при координации Management Layer | Аналитика и обратная связь обсуждены, идеи улучшений отобраны для следующего dev-цикла |

Management Layer здесь является диспетчером эстафеты, а не автором всех результатов. Подробные правила содержательной формулировки задаёт [стандарт ценностного предложения](../product-market/value-proposition-standard.md). Междоменную синхронизацию координирует Management Layer.

## Точка соединения

| Событие | Ответственность U.L.I. | Ответственность Product–Market |
|---|---|---|
| Идея или `v0.x` | Создать и проверить проектное решение | Не обязан подключаться |
| Подготовка публичного `v1.0` | Подтвердить техническую готовность | Зафиксировать ценность, аудиторию, доступ и метрики |
| Публичный релиз | Доставить стабильную версию | Начать наблюдение продукта |
| Следующий major-релиз | Обновить production-состояние | Пересмотреть ценность, показатели и публичное представление |

Полная карта находится в [производственном цикле проектов](../ecosystem/DETai/U.L.I/2_Architecture_and_Logic/production-cycle.md), [модели продуктового объекта](../product-market/product-object-model.md) и [стандарте ценностного предложения](../product-market/value-proposition-standard.md).

## Интерфейс с Team OS

U.L.I. может выпускать contribution evidence: merged change, утверждённый документ, evaluation result или release. Team OS связывает эти события с ролями и результатами по всей экосистеме. Ни одна система не превращает событие в долю или экономическое право автоматически.

## Интерфейс с книгой

Глава «Методоориентированная AI-инфраструктура» описывает, почему психотерапевтическому методу нужна связная технологическая среда. U.L.I. и Platform DETai являются конкретными ответами DETai на этот вопрос. Их текущая реализация может меняться, не меняя универсального тезиса главы.
