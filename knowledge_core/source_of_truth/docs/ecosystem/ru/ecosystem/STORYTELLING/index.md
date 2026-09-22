---
type: ecosystem
classification:
  scope: DETai_ecosystem
  context: brand-and-communications
  layer: operating-model
  function: project
  system: governance-operating-model
  domain: storytelling
  audiences: [team, brand, authors, developers, agents]
descriptive:
  id: storytelling-index
  version: v5
  status: active
  date_ymd: 2026-03-25
  date_update: 2026-09-23
governance:
  canonicality: canonical
  visibility: public
  owner_role: brand-communications-owner
  approver_role: founder
  review_date: 2026-10-23
object_state:
  architecture_status: canonical
  implementation_status: operational
  evidence_status: not-applicable
  visibility_status: public
links:
  external_links:
    - type: MkDocs_ru
      url: https://docs.detai-x.com/ru/ecosystem/STORYTELLING/
    - type: GitHub
      url: https://github.com/DETai-org/Storytelling
  document_links:
    - schema: ecosystem
      link_type: part-of
      linked_document_id: brand-and-communications-domain
    - schema: ecosystem
      link_type: published-through
      linked_document_id: detai-platform-detai-e2-brand-sites-index
    - schema: ecosystem
      link_type: interfaces-with
      linked_document_id: team-os-contribution-ledger
title: Storytelling — Publication Core
---

# Storytelling — Publication Core

**Storytelling — самостоятельный редакционно-технологический проект и Publication Core DETai с [собственным репозиторием](https://github.com/DETai-org/Storytelling). Он владеет процессом создания, review, версионирования и доставки публикаций, но не является архивом опубликованного корпуса.**

Storytelling относится к направлению [«Бренд и внешние коммуникации»](../DETai/Platform_DETai/brand-and-external-communications/index.md) и является его внутренней производственной системой. Пользователь получает результат через сайт, Telegram или другую публичную площадку, а не через сам Publication Core.

## Место в публикационном процессе

| Уровень | Роль |
|---|---|
| **Редакционная рабочая среда** | Идея, черновик, обсуждение, автор и подготовка исходного материала |
| **Storytelling / Publication Core** | Оркестрация, enrichment, локализация, review, версионирование и approval |
| **Representation** | Независимое представление канонического материала для конкретной площадки |
| **Публичная площадка** | Сайт, Telegram и будущие B17, Instagram, YouTube или другие каналы |
| **Архив / knowledge projection** | Downstream-системы, которые сохраняют опубликованный результат после завершения lifecycle Storytelling |

Текущей операционной точкой передачи исходного материала остаётся папка ClickUp [STORYTELLING (TimeOS) для текстов](https://app.clickup.com/90152202658/v/f/901515038276/901510140866). Это действующий вход в процесс, а не постоянная техническая зависимость.

## Мозаичная архитектура

Storytelling следует [мозаичному подходу DETai](../DETai/U.L.I/3_Technical_Standards/mosaic-approach.md): части системы имеют явные границы и развиваются независимо.

```text
Content kind
→ canonical content
→ Representation
→ Strategy
→ Format
→ Features
→ immutable artifact
→ execution requirements
→ transport / execution identity
```

Эти сущности не являются синонимами. Telegram Representation может использовать Strategy `Basic` или `Custom`, Format `Standard` или `Rich`, а Typography является отдельной Feature. Transport выбирается позже и не становится частью самого Representation.

Такое разделение позволяет развивать B17, Instagram или другой Representation без риска затронуть Telegram, а изменение Telegram Format не должно менять Site Representation.

## Full Publication и канонический материал

Для Full Publication основной канонический результат — публикация на Site. Site и Telegram при этом являются независимыми Representation одной логической публикации.

```text
логическая публикация
├── Site Representation
└── Telegram Representation
    ├── Strategy
    ├── Format
    └── Features
```

Одна логическая публикация имеет устойчивый `publicationId` и `contentVersion`. Destination-specific идентификаторы принадлежат своим Representation: Site использует `sitePostId` и URL, Telegram — chat/message receipts.

В дальнейшем Storytelling может работать не только со статьями. Например, Event является отдельным content kind со своими типами событий — обновление проекта, месячный отчёт, новый участник команды и другие. Event может иметь Site и Telegram Representation, переиспользуя общие мозаики доставки, но не превращаясь в разновидность Article.

## Publication Workspace: процесс, а не архив

Storytelling хранит durable рабочее состояние только на время активного lifecycle публикации. Publication Workspace содержит текущий `contentVersion`, drafts Representation, approvals, delivery attempts и working media.

Это состояние нужно для restart/recovery, idempotency и reconciliation, но после безопасной финализации становится purgeable. Опубликованный корпус и долгосрочные knowledge projections принадлежат downstream-системам.

## Кодовые границы Publication Core

- `telegram_bot/` — operator interface и Telegram UI;
- `publication_core/domain/` — publication identity, state и transport-neutral contracts;
- `publication_core/application/`, `publication_core/workflows/` — use cases и orchestration;
- `publication_core/representations/` — Site, Telegram и будущие Representation projections;
- `publication_core/ports/` — стабильные границы внешних возможностей;
- `publication_core/adapters/` — реализации внешних execution systems;
- `publication_core/infrastructure/` — persistence и runtime infrastructure.

Направление зависимостей остаётся односторонним: interface вызывает application/workflows, доменная модель не зависит от operator UI, а Representation не знает устройство конкретного transport. `publication_core.channels` является переходным compatibility seam и не считается целевым местом для новой Representation-логики.

## Telegram Representation и execution

| Telegram Representation | Execution |
|---|---|
| Standard | Bot API |
| Rich без Typography | Bot API |
| Rich + Typography | user execution |
| Artifact, который текущий user transport не может воспроизвести exactly | capability conflict |

Fragment / collectible-username сценарий Bot API custom emoji не используется как поддерживаемая ветка Storytelling. Для channel Typography действует инвариант: **Typography требует user execution**.

Storytelling владеет publication intent: точной целью, immutable artifact, human approval и delivery intent. Проект [Telegram](../DETai/Platform_DETai/E2-Brand/Telegram/index.md) владеет managed accounts, authorization, sessions, Premium state, network profiles и Telegram API clients.

Storytelling может показывать оператору logical execution identity, например `Anton-Psy-01`, и позволять выбрать другую доступную identity. Путь к Telethon session, authorization key, телефон, 2FA и network credentials остаются внутренними деталями проекта Telegram.

Текущий Premium MTProto owner является compatibility bridge. Целевая граница — private Telegram Service API: Storytelling передаёт exact target, immutable artifact и execution requirements, а Telegram Service возвращает identity/transport либо capability conflict.

## Operator / Process Settings

Настройки самого процесса образуют отдельную мозаику и не являются частью Publication или конкретного Representation. Например, выбор Telegram execution identity относится к operator/runtime settings: он влияет на техническое исполнение, но не меняет утверждённый контент.

## Связь с сайтом

[Сайт DETai](../DETai/Platform_DETai/E2-Brand/sites/index.md) — основная публичная web-поверхность и потребитель Site Representation. Storytelling готовит утверждённый материал и destination intent; репозиторий `sites` самостоятельно отвечает за route, HTML, SEO, Open Graph, structured data и deployment.

## Технологическая основа

Storytelling сохраняет собственную предметную публикационную логику, даже когда использует общие технические системы. Intelligence Runtime исполняет LLM-сценарии, Telegram — Telegram execution, Sites — web runtime. Подробная карта этих границ находится на странице [«Как Storytelling использует технологическую основу»](technology-foundation.md).

## Рабочее состояние и управление

Текущие задачи, сроки и Work Packages живут в ClickUp и management runtime. Эта страница фиксирует устойчивую модель Storytelling и его системные границы, а не текущий план разработки.
