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

**ecosystem-runtime** — инфраструктурная система для живых операционных
потоков DETai. Её [самостоятельный репозиторий](https://github.com/DETai-org/ecosystem-runtime)
содержит application-код, API, ботов, workers, общие runtime-контракты и
миграции данных.

Если публичный сайт или Telegram-интерфейс показывает событие, принимает
заявку или отправляет уведомление, интерфейс остаётся поверхностью
взаимодействия. Долгоживущая runtime-логика и данные такого процесса принадлежат
ecosystem-runtime.

## Что система соединяет

```text
интерфейс пользователя
→ API и правила доступа
→ runtime-данные
→ фоновые процессы и доставка
```

Репозиторий отделён от конкретного сервера. Infrastructure может развернуть
его компоненты на подходящем вычислительном узле, но машина не становится
источником версии или владельцем логики.

ecosystem-runtime также не владеет каноническими знаниями и не исполняет
LLM-сценарии: эти задачи принадлежат соответственно
[Knowledge Substrate](../Knowledge_Substrate/index.md) и
[intelligence-runtime](../intelligence-runtime/index.md).
