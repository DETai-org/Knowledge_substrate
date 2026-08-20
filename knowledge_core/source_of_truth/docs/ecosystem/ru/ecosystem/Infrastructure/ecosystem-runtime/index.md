---
type: ecosystem
classification:
  scope: Infrastructure
  context: ecosystem-runtime
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: infrastructure-ecosystem-runtime
  version: v1
  status: active
  date_ymd: 2026-08-20
governance:
  canonicality: canonical
  visibility: public
title: ecosystem-runtime
---

# ecosystem-runtime

**ecosystem-runtime** — общий backend-контур DETai. Его
[самостоятельный репозиторий](https://github.com/DETai-org/ecosystem-runtime)
содержит приложения, общую доменную логику и структуру runtime-данных, которые
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
events, intake, notifications и platform contracts. Благодаря этому сайт и
разные боты не создают собственные несовместимые правила для одних данных.

### Runtime-данные

Миграции PostgreSQL поддерживают отдельные области для общей идентичности
пользователя, прав доступа, событий, заявок и уведомлений. Боты и сайт не
становятся источниками истины: они читают и изменяют эти данные через API и
общую application-логику.

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
[Knowledge Substrate](../Knowledge_Substrate/index.md) и
[intelligence-runtime](../intelligence-runtime/index.md).
