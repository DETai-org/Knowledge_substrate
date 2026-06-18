# Policy: Runtime Boundary Map

## Назначение

Эта политика фиксирует границы ответственности между Knowledge Core,
`detai_core`, `detai_projects`, сайтом и runtime-приложениями экосистемы.

Документ нужен, чтобы не смешивать:
- каноническое знание;
- производные query-представления;
- mutable runtime-данные;
- код процессов;
- пользовательские web/bot surfaces.

## Главный принцип

```txt
Knowledge_substrate owns data contracts and knowledge pipelines.
ecosystem-runtime owns live process code.
sites owns public web surfaces.
```

## Слои Knowledge_substrate

### `knowledge_core/source_of_truth`

Канонический слой знания.

Хранит первичные документы, frontmatter, controlled vocabularies и политики
канонического контента.

Не хранит заявки, пользователей, события, подписки или runtime-состояния.

### `knowledge_core/ingest_pipeline`

Пайплайн преобразования канона в машинные представления.

Отвечает за:
- чтение canonical Markdown;
- парсинг;
- валидацию;
- materialization metadata;
- embeddings;
- graph edges;
- idempotent upsert в operational/query store.

Не отвечает за пользовательские формы, события, регистрации или Telegram-bot
runtime.

### `knowledge_core/operational_store`

Концептуальное описание operational/query store для knowledge data.

Это производный слой, воспроизводимый из source of truth и ingest pipeline.

### `sql/detai_core`

SQL-контур canonical/query database `detai_core`.

Отвечает за:
- structured knowledge documents;
- metadata;
- embeddings;
- semantic graph;
- query-facing tables.

Не хранит private mutable runtime-данные вроде пользователей, заявок, событий,
подписок и delivery logs.

### `sql/detai_core/api`

API доступа к `detai_core`.

Отвечает за чтение подготовленных knowledge/query data, например graph API.

Не является API для ecosystem events, intake, auth/account или notifications.

### `sql/detai_projects`

SQL-контур private mutable runtime database `detai_projects`.

Здесь живут shared runtime schemas и project schemas.

Shared runtime schemas:
- `identity`
- `access`
- `ecosystem_events`
- `intake`
- `notifications`

Project schemas:
- `psychology_in_quotes`
- future product/project schemas.

## Слои ecosystem-runtime

`ecosystem-runtime` является code runtime project. Он не владеет SQL-политиками,
но реализует процессы поверх schema contracts из `Knowledge_substrate`.

### `apps/api`

Write/read boundary для runtime-процессов.

Отвечает за:
- auth/authz для runtime operations;
- public event reads для сайта;
- write operations в `ecosystem_events`;
- intake submissions;
- notification triggers;
- интеграцию ботов и workers с database layer.

### `apps/admin-bot`

Private staff Telegram interface.

Может создавать и редактировать события, просматривать заявки и запускать
операционные действия, но не хранит собственный event source of truth.

### `apps/public-bot`

Public user Telegram interface.

Может управлять подписками, доставлять уведомления и принимать заявки, но не
владеет `notifications` или `intake` как закрытым bot-local store.

### `apps/workers`

Фоновые процессы.

Отвечают за:
- notification dispatch;
- retries;
- reminders;
- future scheduled jobs.

### `packages/db`

Shared database access code for runtime schemas.

### `packages/events`

Domain logic for `ecosystem_events`.

### `packages/intake`

Domain logic for `intake`.

### `packages/notifications`

Domain logic for `notifications`.

### `deploy`

Runbooks, systemd units, env examples and server deployment notes for runtime
services.

## Связь с sites

`sites` владеет public web surfaces:
- `/events`;
- `/det/therapy`;
- future account/auth/legal/cookie pages;
- future forms.

Сайт не должен быть source of truth для событий или заявок. Он должен читать и
писать через runtime API.

## Example: `/det/therapy` request flow

```txt
User opens /det/therapy on sites
→ user submits individual/group therapy request
→ sites calls ecosystem-runtime apps/api
→ api creates or resolves identity.users
→ api stores request in intake
→ optional notifications/admin flow alerts staff
→ staff reviews request through admin-bot or future admin UI
```

Data ownership:
- user/contact identity: `identity`
- access/subscription state: `access`
- therapy request payload and processing status: `intake`
- staff notification/subscriber delivery: `notifications`
- public page rendering: `sites`
- process code: `ecosystem-runtime`

## Инварианты

1. `detai_core` MUST NOT be used for private mutable runtime data.
2. `detai_projects` is the database for mutable runtime schemas and project
   schemas.
3. Runtime APIs and bots MUST write through domain services, not directly invent
   separate local stores.
4. Website pages MAY display and submit runtime data, but MUST NOT become
   independent sources of truth.
5. Schema policies live in `Knowledge_substrate`; application code lives in
   runtime/application repositories.
