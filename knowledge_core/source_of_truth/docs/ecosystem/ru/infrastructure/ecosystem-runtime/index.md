---
type: ecosystem
classification:
  scope: Infrastructure
  context: ecosystem-runtime
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: infrastructure-ecosystem-runtime
  version: v3
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

Модель PostgreSQL разделяет данные идентичности, доступа, коммерческих операций,
событий, заявок и уведомлений. Боты и сайт работают с этими данными через API
и общую прикладную логику, не создавая собственные источники истины.

### Commerce Core — коммерческие операции

**Commerce Core** — общая техническая система коммерческих операций DETai. Через неё продукты работают с коммерческими предложениями, заказами, подтверждёнными платежами, подписками и возвратами, используя единые контракты для разных способов оплаты.

Техническая реализация Commerce Core — часть **ecosystem-runtime**: здесь находятся серверная логика, платёжные интеграции и работа с данными. В архитектуре данных `commerce` отвечает за коммерческие факты, `identity` — за идентичность пользователей, а `access` — за основания доступа. Каждый продукт самостоятельно определяет, какие функции предоставляет пользователю на основании этих прав.

[Company & Economy](https://docs.detai-x.com/ru/company-and-economy/) рассматривает ту же коммерческую деятельность с точки зрения экономических условий, обязательств и устойчивости. Это самостоятельная область ответственности, а не ещё одна техническая реализация Commerce Core.

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
