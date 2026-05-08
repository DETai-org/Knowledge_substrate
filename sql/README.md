# SQL Layers

`sql/` — навигационный слой по SQL-контурам экосистемы DET / DETai.

Он разделяет две разные database-роли на одном PostgreSQL server:
- `detai_core` — canonical/query database экосистемы;
- `detai_projects` — private project runtime database.

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

Источник истины для этого слоя находится в `knowledge_core/source_of_truth/`.

### `detai_projects`

Хранит private mutable project runtime data:
- users;
- plans;
- moderation;
- channel bindings;
- user-owned brand kits;
- user-owned templates;
- runtime audit и другие project-scoped operational данные.

Внутри `detai_projects` каждая схема должна называться по проекту:
- `psychology_in_quotes`
- будущие project schemas по тому же правилу.

## Текущее состояние репозитория

Действующая codebase query/API слоя теперь физически лежит в каталоге:
- `sql/detai_core/`

Это означает, что SQL-навигация и реальное расположение core-реализации теперь совпадают.
