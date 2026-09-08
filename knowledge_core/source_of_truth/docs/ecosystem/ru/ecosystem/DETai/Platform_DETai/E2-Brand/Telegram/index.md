---
type: ecosystem
classification:
  scope: DETai_cluster
  context: platform
  layer: null
  function: index
descriptive:
  id: detai-platform-detai-e2-brand-telegram-index
  version: v2
  status: active
  date_ymd: 2026-09-08
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/DETai/Platform_DETai/E2-Brand/Telegram/
  document_links:
    - schema: ecosystem
      link_type: explains
      linked_document_id: detai-platform-telegram-account-manager-explanation
    - schema: ecosystem
      link_type: explains
      linked_document_id: detai-platform-telegram-account-manager-philosophy
title: Telegram
---

# Telegram

**Telegram** — внутренний технологический контур DETai для управляемой работы с авторизованными Telegram-аккаунтами и Telegram-workflow. Репозиторий исторически объединял отдельные инструменты — сессии, реакции, комментарии, личные сообщения и другие операции; текущая архитектура доводит этот замысел до связного операционного слоя для команды.

Ключевая идея проста: **авторизованный аккаунт и его сессия — это ресурс**. Реакция, публикация, комментарий, модерация, ручная настройка профиля или другой workflow — это действия, которые используют этот ресурс, а не определяют его архитектуру.

```text
Authorized Telegram accounts
          ↓
     Account Registry
          ↓
     Session Runtime
          ↓
 ┌────────┼─────────┬───────────┐
 ↓        ↓         ↓           ↓
Publish  Reaction  Comment   Moderation / DM / other workflows
```

## Два действующих контура

### Account Manager

**Account Manager** отвечает за жизненный цикл managed accounts: добавление существующего Telegram-аккаунта, регистрацию нового аккаунта, каноническую automation session, закреплённый Network Profile, Visual Profile и понятный интерфейс управления через внутреннего Telegram-бота.

Это слой, который отвечает на вопросы: **какие аккаунты есть у команды, кому они принадлежат, где и через какое сетевое подключение работают, какие сессии созданы и готовы ли они к использованию**.

Подробнее:

- [Account Manager — как устроена система](account-manager.md) 🔍
- [Account Manager — зачем мы строим её именно так](account-manager-philosophy.md) 🌿

### UserControl

**UserControl** — контур прикладных Telegram-workflow, которые используют уже авторизованные аккаунты и сессии как ресурс. В нём исторически возникли comment chains, like/repost flows, personal messages, channel operations и другие инструменты. Часть этих возможностей постепенно переносится из набора отдельных скриптов в управляемые действия Account Manager и связанных сервисов.

- [UserControl](UserControl/index.md)

## Граница проекта

Telegram-контур владеет Telegram-специфичной логикой аккаунтов, сессий и действий. Сетевую инфраструктуру и фактические egress endpoint предоставляет Infrastructure через Network Provider contract; Telegram выбирает capacity, priority и sticky assignment для своих managed accounts. Другие продукты DETai могут использовать Telegram как исполнительную capability, не становясь владельцами Telegram-сессий или сетевой инфраструктуры.

**Проект Telegram** функционирует как **проект второго эшелона** в рамках экосистемы DET/DETai.