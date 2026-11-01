---
type: ecosystem
classification:
  scope: Infrastructure
  context: ecosystem-runtime
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: infrastructure-ecosystem-runtime
  version: v2
  status: active
  date_ymd: 2026-08-20
  date_update: 2026-11-02
governance:
  canonicality: canonical
  visibility: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/infrastructure/ecosystem-runtime/
  document_links:
    - schema: ecosystem
      link_type: coordinates-with
      linked_document_id: company-economy-index
title: ecosystem-runtime
---

# ecosystem-runtime

**ecosystem-runtime** — общий backend-контур DETai. Этот контур содержит приложения, общую доменную логику и структуру runtime-данных, которые
нужны сайту, Telegram-интерфейсам и фоновым процессам.

Если публичный сайт или Telegram-интерфейс показывает событие, принимает
заявку или отправляет уведомление, интерфейс остаётся поверхностью
взаимодействия. Долгоживущая runtime-логика и данные такого процесса принадлежат
ecosystem-runtime.

## Что находится внутри

Репозиторий разделён на три понятных уровня.

### Приложения

- **API** принимает запросы от сайтов и ботов, применяет правила доступа и
  записывает данные в правильную область;
- **admin-bot** даёт команде приватный Telegram-интерфейс для работы с
  событиями и поступившими заявками;
- **public-bot** принимает пользовательские действия, регистрации и подписки,
  а также доставляет сообщения;
- **workers** выполняют фоновые задачи: доставку, повторы, напоминания и
  синхронизации.

### Общая логика

Packages описывают повторно используемые части backend: identity, access,
commerce, events, intake, notifications и platform contracts. Благодаря этому сайт и
разные боты не создают собственные несовместимые правила для одних данных.

### Runtime-данные

Миграции PostgreSQL поддерживают отдельные области для общей идентичности
пользователя, прав доступа, событий, заявок и уведомлений. Боты и сайт не
становятся источниками истины: они читают и изменяют эти данные через API и
общую application-логику.

### Commerce Core — общая техническая возможность

**Commerce Core** обслуживает коммерческие операции разных продуктов DETai: каталог предложений, заказы, проверенные платёжные события, платные периоды и возвраты. Первые сценарии реализованы для Psychology in Quotes и Telegram Stars; развитие Core как общего сервиса позволяет добавлять другие продукты и способы оплаты без независимых платёжных реестров.

Технический код, платёжные адаптеры, SQL-данные, API и их эксплуатация принадлежат **ecosystem-runtime** внутри Infrastructure. Целевая PostgreSQL-схема `commerce` отделяет коммерческие факты от `access`, который отвечает за основания доступа, и от `identity`, который владеет учётными записями. Это целевая граница: существующая реализация Commerce пока использует объекты `access`, а не самостоятельную схему `commerce`. Продукты продолжают самостоятельно определять возможности и ограничения полученного доступа.

Экономические условия, результаты и устойчивость рассматриваются через [Company & Economy](https://docs.detai-x.com/ru/company-and-economy/). Это **предметная перспектива**, не перенос Commerce Core из Infrastructure и не подмена его технического владельца.

## Как проходит действие

```text
сайт или Telegram-интерфейс
→ ecosystem-runtime API
→ проверка правил и запись runtime-данных
→ worker или интерфейс показывает результат
```

Репозиторий отделён от конкретного сервера. Infrastructure может развернуть
его компоненты на подходящем вычислительном узле, но машина не становится
источником версии или владельцем логики.

ecosystem-runtime также не владеет каноническими знаниями и не исполняет
LLM-сценарии: эти задачи принадлежат соответственно
[Knowledge Substrate](../knowledge-substrate/index.md) и
[intelligence-runtime](../intelligence-runtime/index.md).
