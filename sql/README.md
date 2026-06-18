# SQL Layers

`sql/` — навигационный слой по SQL-контурам экосистемы DET / DETai.

Он разделяет две разные database-роли на одном PostgreSQL server:
- `detai_core` — canonical/query database экосистемы;
- `detai_projects` — private runtime database для платформенных и проектных operational schemas.

Git-структура внутри каждого database-контура должна по возможности отражать
структуру самих PostgreSQL schemas, а не прятать schema-specific SQL в абстрактные
технические папки.

## Зачем это разделение

`detai_core` и `detai_projects` решают разные задачи и не должны смешиваться.

### `detai_core`

Хранит производные SQL-представления канонического слоя:
- ecosystem documents;
- publications documents;
- metadata;
- graph;
- embeddings;
- query-facing tables и сервисы доступа.

Внутри `detai_core` допустим только нейтральный технический служебный слой для самой БД
например `infra.schema_migrations`, если он нужен для bootstrap и обслуживания схемы.
Он не является частью доменной модели.

Источник истины для этого слоя находится в `knowledge_core/source_of_truth/`.

Ожидаемая раскладка внутри `sql/detai_core/`:
- root-level файлы и каталоги — database-wide assets (`bootstrap/`, `api/`, `tests/`, `apply_migrations.sh`, `Makefile`, `docker-compose.yml`, `analysis_exports/`);
- `infra/` — нейтральный технический schema-layer;
- `ecosystem/` — ecosystem schema-layer;
- `publications/` — publications schema-layer.

### `detai_projects`

Хранит private mutable runtime data.

Рабочий source of truth для общих платформенных runtime-схем перенесен в [`DETai-org/ecosystem-runtime`](https://github.com/DETai-org/ecosystem-runtime):

- [`identity`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas/identity)
- [`access`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas/access)
- [`ecosystem_events`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas/ecosystem_events)
- [`intake`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas/intake)
- [`notifications`](https://github.com/DETai-org/ecosystem-runtime/tree/main/db/schemas/notifications)

Product-specific schemas должны жить в репозиториях своих продуктов. В этом репозитории может временно оставаться только переходный SQL-контур проекта, пока у него нет собственного runtime ownership.

Ожидаемая раскладка внутри `sql/detai_projects/`:
- root-level файлы и каталоги — database-wide assets (`bootstrap/`, `README.md`);
- `psychology_in_quotes/` — временный SQL-контур конкретной project schema;
- будущие project folders по тому же правилу.

## Текущее состояние репозитория

Действующая codebase query/API слоя теперь физически лежит в каталоге:
- `sql/detai_core/`

Это означает, что SQL-навигация и реальное расположение core-реализации теперь совпадают.
