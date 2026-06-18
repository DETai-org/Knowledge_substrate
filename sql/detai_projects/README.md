# detai_projects

`sql/detai_projects/` больше не является source of truth для общих платформенных runtime-миграций.

Рабочие миграции DETai runtime-платформы перенесены в [`DETai-org/ecosystem-runtime/db/schemas`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas):

- [`identity`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas/identity)
- [`access`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas/access)
- [`ecosystem_events`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas/ecosystem_events)
- [`intake`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas/intake)
- [`notifications`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas/notifications)

`Knowledge_substrate` оставляет за собой:

- `detai_core` knowledge/query database;
- knowledge/document/publication ingest pipeline;
- навигационную карту SQL-контуров;
- переходные SQL-контуры проектов, пока они не перенесены в собственные product repositories.

## Что Осталось Здесь

- [`bootstrap`](bootstrap) — создание database `detai_projects`.
- [`psychology_in_quotes`](psychology_in_quotes) — временный project-specific SQL-контур первого продукта.

Product-specific схемы в дальнейшем должны жить в репозиториях конкретных продуктов.
