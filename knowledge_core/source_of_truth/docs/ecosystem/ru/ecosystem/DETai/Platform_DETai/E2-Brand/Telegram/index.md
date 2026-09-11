---
type: ecosystem
classification:
  scope: DETai_cluster
  context: platform
  layer: null
  function: index
descriptive:
  id: detai-platform-detai-e2-brand-telegram-index
  version: v4
  status: active
  date_ymd: 2026-09-09
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/DETai/Platform_DETai/E2-Brand/Telegram/
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/governance/brand-and-communications/
  document_links:
    - schema: ecosystem
      link_type: explains
      linked_document_id: detai-platform-telegram-account-manager-explanation
    - schema: ecosystem
      link_type: explains
      linked_document_id: detai-platform-telegram-account-manager-philosophy
    - schema: ecosystem
      link_type: relates-to
      linked_document_id: brand-and-communications-domain
title: Telegram
---

# Telegram

**Telegram** — внутренний технологический контур DETai для работы с Telegram-аккаунтами и Telegram-workflow. Репозиторий исторически объединяет инструменты авторизации и управления аккаунтами с прикладными сценариями: реакциями, комментариями, личными сообщениями, каналами и другими операциями.

Сегодня внутри контура особенно важно различать две части.

| Контур | За что отвечает |
|---|---|
| **Account Manager** | жизненный цикл managed accounts: добавление, регистрация, automation session, Network Profile, Visual Profile, readiness и командный интерфейс |
| **UserControl** | прикладные workflow над уже подготовленными аккаунтами: comments, reactions, personal messages, channel operations и другие сценарии |

## Account Manager

Account Manager отвечает на практические вопросы: какие managed accounts существуют, к какому командному профилю относятся, какая automation session является канонической, какой Network Profile закреплён и доступен ли Visual Profile.

Связанные документы:

- [Как устроен Account Manager](account-manager.md) — объектная модель, жизненный цикл и архитектурные границы.
- [Зачем нужны управляемые аккаунты](account-manager-philosophy.md) — философия разрешённого ресурса, управления вниманием и роли такого механизма на ранней стадии.

## UserControl

**UserControl** — контур конкретных Telegram-workflow, использующих уже подготовленные аккаунты и сессии. Здесь исторически развивались comment chains, like/repost flows, personal messages, channel operations и другие инструменты.

- [UserControl](UserControl/index.md)

## DETai Media Library { #detai-media-library }

**DETai Media Library** — закрытая Telegram-native медиатека экосистемы: единый источник переиспользуемых изображений, GIF/анимаций, стикеров и других media assets для managed accounts и Telegram-workflow DETai.

Для управляемого аккаунта доступ к медиатеке может входить в базовый Telegram-контур вместе с публичными каналами DETai. Это не ещё один канал, за лентой которого нужно следить: медиатека нужна, чтобы один и тот же материал можно было сохранить один раз и затем использовать повторно в комментариях, ботах и других Telegram-сценариях.

Для интеграций действует явная модель доступа: Account Manager управляет доступом к закрытой медиатеке, а конкретный DETai-бот или сервис подключается к ней отдельно и получает только необходимые права. Telegram `file_id` привязан к конкретному боту и не считается универсальным идентификатором media; устойчивой сущностью остаётся сам asset и его семантическая идентичность, а нужную Telegram-ссылку или идентификатор consumer получает в собственном контексте.

## Связь с E2-Brand и Brand & Communications

Telegram находится внутри E2-Brand как **техническая коммуникационная поверхность и исполнительный контур**, но сам по себе не создаёт бренд и не является владельцем репутации DETai.

Бренд возникает из смысла, качества, повторяемого опыта, доверия и согласованной публичной коммуникации. Ответственность за эту более широкую рамку описана в домене [Brand & Communications](https://docs.detai-x.com/ru/governance/brand-and-communications/). Telegram предоставляет ему одну из площадок и набор технических возможностей, но не подменяет бренд-стратегию.

## Граница проекта

Telegram владеет Telegram-specific логикой managed accounts, sessions и действий. Сетевую инфраструктуру и фактические egress endpoint предоставляет Infrastructure через Network Provider contract; Telegram хранит только свою capacity/priority policy и sticky assignment.

Другие продукты DETai могут использовать Telegram как исполнительную capability, не становясь владельцами Telegram-сессий, Desktop profiles или сетевой инфраструктуры.

**Проект Telegram** функционирует как **проект второго эшелона** в рамках экосистемы DET/DETai.
