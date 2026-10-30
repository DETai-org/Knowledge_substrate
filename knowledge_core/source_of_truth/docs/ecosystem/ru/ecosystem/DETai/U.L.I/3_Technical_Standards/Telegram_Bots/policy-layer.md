---
type: ecosystem
classification:
  scope: DETai_cluster
  context: uli
  layer: technical-standards
  function: policy
descriptive:
  id: detai-u-l-i-3-technical-standards-telegram-bots-policy-layer
  version: v2
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-10-30
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/DETai/U.L.I/3_Technical_Standards/Telegram_Bots/policy-layer/
title: Policy Layer — полномочия и контекст Telegram-ботов
---

# Policy Layer — полномочия и контекст Telegram-ботов

**Функция:** `policy`. Обязательная граница между Telegram-интерфейсом и фактической авторизацией действий. Нормативна **семантика** проверок, а не конкретная Python-папка `core/policy_layer.py`.

## Что проверяется

- **Вход в экземпляр (rollout admission):** development/pilot/public, а также проверенный Telegram sender и список разрешённой аудитории. Доступ к боту **не** означает административную роль в продукте.
- **Identity и роли:** подтверждённая связь с DETai Account и полномочия, которые принадлежат соответствующему provider/backend. Telegram username или callback-данные не заменяют Identity.
- **Тарифы, grants, квоты и владение контентом:** продуктовая исполняемая policy/API/SQL, а не локальная кнопка, JSON допуска или наличие дорогого подписочного экрана.
- **Безопасность операции:** нужная стадия сценария, revision, environment, idempotency, лимит и отсутствие подтверждённого запрета. Продолжение после `uncertain` требует выяснения фактического исхода, не нового слепого запроса.

## Архитектурные правила

1. Telegram handler получает событие и вызывает **одну** серверную проверку нужных полномочий. Дублировать расходование квоты и проверку прав по нескольким UI-веткам запрещено.
2. Policy не должна доверять только клиентскому состоянию, видимости кнопки, языку, callback payload или неподписанному deep link. Оплата признаётся только после проверки фактического provider evidence.
3. Входные списки и режимы берутся из [канонической декларативной конфигурации](configuration-standard.md), а бизнес-права — из исполняемой продуктовой политики. Эти данные **разного назначения** и не сводятся к одному `is_admin`.
4. Серверные ошибки доступа не должны раскрывать данные других пользователей или секреты. Запрет/лимит — обычный продуктовый исход, а не автоматический критический alert.
5. Бот, сайт, API и worker должны разрешать одно и то же право одним backend-контрактом. Если отдельный процесс не может подтвердить право, он не должен выдавать его по старой UI-копии.

## Организация кода

Реализация может называться `policy-layer.ts`, `access.ts`, `policy_layer.py` или иначе. В небольшом приложении достаточно одного модуля; при росте разделяйте Identity/admission, product entitlement, safety и context без циклических импортов. Нормативный принцип — **единая проверяемая семантика**, а не предписанные 300 строк или превосходство одной файловой структуры.

```text
Telegram update
  → verified sender / authentication
  → rollout admission
  → policy + product authorization
  → application service + durable outcome
  → presentation
```

[Стандарт создания Telegram-бота](telegram-bot-creation-standard.md) · [Стандарт конфигурации](configuration-standard.md) · [Стандарт передачи языка](language-handover.md).
