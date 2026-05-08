# detai_projects

`detai_projects` — private project runtime database.

Она предназначена для project-scoped operational state, который не является публичным каноном экосистемы.

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
