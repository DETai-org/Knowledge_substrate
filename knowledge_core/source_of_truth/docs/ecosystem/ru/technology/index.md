---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: technology-layer
  layer: system-interface
  function: index
  system: technology
  domain: technology-layer
  audiences: [public, team, developers, product, agents]
descriptive:
  id: technology-index
  version: v1
  status: active
  date_ymd: 2026-08-05
governance:
  canonicality: canonical
  visibility: public
  owner_role: technical-lead
  approver_role: founder
  review_date: 2026-09-05
links:
  external_links:
    - type: MkDocs_ru
      url: https://detai-org.github.io/Knowledge_substrate/ru/technology/
  document_links:
    - schema: ecosystem
      link_type: contains
      linked_document_id: detai-u-l-i-index
    - schema: ecosystem
      link_type: contains
      linked_document_id: detai-platform-detai-index
title: Технологический слой DETai
---

# Технологический слой DETai

Технологический слой — собственная цифровая среда экосистемы, которая усиливает институциональную жизнь метода, создаёт общие capabilities и доставляет конкретные продукты людям.

Он является практической реализацией универсальной идеи **методоориентированной AI-инфраструктуры**, описанной в главе `book.part-1.chapter-2` книги. Книга раскрывает принцип; настоящий раздел показывает, как он получает конкретную форму в DETai.

## U.L.I. — контур создания

[U.L.I.](../ecosystem/DETai/U.L.I/index.md) — Human–AI Development Environment технологической команды. Он объединяет людей, AI-агентов, знания, репозитории, стандарты, evaluation и production cycles.

U.L.I. не является Telegram-ботом, Team OS или системой управления всей экосистемой. Бот, уведомления и resource tracker являются компонентами текущей реализации.

## Platform DETai — контур доставки

[Platform DETai](../ecosystem/DETai/Platform_DETai/index.md) связывает общие capabilities, product lines, продукты и пользовательские сервисы. Она обеспечивает переиспользование инфраструктуры и доставку ценности, но не является всей экосистемой.

## Интерфейс двух контуров

Подробно: [создание, доставка и обратная связь](system-interface.md).

```text
требование → U.L.I. → проверенный результат → Platform DETai
→ использование → допустимый feedback → новая версия
```

## Универсальное и методоспецифическое

- универсальная психологическая AI-инфраструктура может быть полезна разным методам и контекстам;
- Method-Specific AI Infrastructure удерживает язык, границы и профессиональные требования DET.

Обе формы могут использовать общие технические capabilities, но не обязаны иметь одинаковые claims, данные или release gates.

## Технология не управляет методом

Техническая возможность не создаёт профессионального права. Intended use, data classes, human oversight и evidence определяются до выпуска чувствительных функций.
