---
type: ecosystem
classification:
  scope: Infrastructure
  context: ecosystem-runtime
  layer: architecture-and-logic
  function: explanation
descriptive:
  id: infrastructure-ecosystem-runtime
  version: v4
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

## Приложения

- **API** принимает запросы от сайтов и ботов, применяет правила доступа и
  записывает данные в правильную область;
- **admin-bot** даёт команде приватный Telegram-интерфейс для работы с
  событиями и поступившими заявками;
- **public-bot** принимает пользовательские действия, регистрации и подписки,
  а также доставляет сообщения;
- **workers** выполняют фоновые задачи: доставку, повторы, напоминания и
  синхронизации.

## Общая логика

Packages описывают повторно используемые части backend: identity, access,
commerce, events, intake, notifications и platform contracts. Благодаря этому сайт и
разные боты не создают собственные несовместимые правила для одних данных.

## Runtime-данные

В модели проекта выделены семь предметных схем PostgreSQL, интеграционная
схема `integrations` и служебная `public`. Их назначение описано ниже.

### identity — учётные записи

Общая идентичность пользователя DETai: учётная запись, профиль и связи
с внешними аккаунтами и интерфейсами.

### access — доступ

Роли, разрешения и основания доступа к ресурсам и возможностям экосистемы.

### commerce — данные Commerce Core

Коммерческие факты [Commerce Core](../../company-and-economy/commerce-core.md):
предложения, заказы, подтверждённые платежи, подписки и возвраты.
Технически этот контур входит в ecosystem-runtime; экономический взгляд на него
задаёт [Company & Economy](../../company-and-economy/index.md).

### ecosystem_events — события

Предусмотренный архитектурой календарный и событийный слой экосистемы:
события, с которыми работают административные интерфейсы, сайт и уведомления.

### intake — заявки и формы

Первичные обращения, заявки, регистрации, предложения и жалобы,
а также сведения, необходимые для их обработки.

### notifications — уведомления

Подписки на уведомления, настройки каналов, задания доставки и результаты
отправки сообщений.

### support — поддержка

Обращения в поддержку, переписка и состояние обработки обращений.

### integrations — интеграционные контракты

Ограниченные интерфейсы обмена между продуктами и общими runtime-данными.
Они предоставляют согласованные операции без прямого доступа ко всей внутренней
структуре данных.

### public — служебный журнал

Общий журнал применённых миграций базы данных, используемый проектом.

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
