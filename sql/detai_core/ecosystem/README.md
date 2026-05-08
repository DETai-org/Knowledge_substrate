# ecosystem schema

`sql/detai_core/ecosystem/` резервирует и описывает SQL-контур schema `ecosystem`
внутри database `detai_core`.

Эта schema должна зеркалить ecosystem-домен из:

- `knowledge_core/source_of_truth/docs/ecosystem/`
- `knowledge_core/source_of_truth/schemas/ecosystem/`

## Текущее состояние

На текущем этапе schema `ecosystem` зафиксирована как часть целевой архитектуры
database `detai_core`, но ещё не наполнена отдельными SQL-таблицами и query-слоем.

## Состав каталога

- `migrations/` — будущие ecosystem-specific SQL migrations

## Граница

Сюда не относятся:

- publication graph/query tables
- publication embeddings
- publication metadata materialization
- database technical ledger
