# detai_projects

`detai_projects` — private project runtime database.

Она предназначена для project-scoped operational state, который не является публичным каноном экосистемы.

## Текущая итерация

Первая итерация этого контура — **infra-only migration layer**.

Она покрывает:

- создание database `detai_projects`;
- создание project schema `psychology_in_quotes`;
- создание runtime tables, индексов и ограничений;
- initial SQL seed на базе текущего snapshot из `DETai-org/psychology-in-quotes/apps/telegram-bot/runtime-db-seed/`.

Она пока не покрывает:

- переписывание Telegram-бота на прямую работу с PostgreSQL;
- runtime repository/service layer внутри проекта `psychology-in-quotes`;
- product output layout внутри `docs/publications/quotes/`.

## Что сюда относится

- users
- user_plans
- moderation_entries
- channel_bindings
- user_brand_kits
- user_brand_kit_templates
- user_caption_templates
- admin_audit_events

## Как раскладывать данные

Одна database:
- `detai_projects`

Много project schemas:
- `psychology_in_quotes`
- другие проекты по мере появления

## Что сюда не относится

- канонические ecosystem documents
- канонические publications documents
- system-owned defaults, которые должны жить рядом с кодом
- product output files как primary layer

## Переходный принцип seed

JSON-файлы из `psychology-in-quotes/apps/telegram-bot/runtime-db-seed/` рассматриваются здесь только как переходный источник initial import.

После перевода runtime-слоя проекта на PostgreSQL:

- JSON seed перестаёт быть primary runtime source;
- bot runtime должен читать и писать напрямую в `detai_projects.psychology_in_quotes`;
- code-owned system defaults остаются в репозитории `psychology-in-quotes`.

## Runbook

Операционный runbook первой итерации находится в:

- `sql/detai_projects/workspace/db/README.md`
