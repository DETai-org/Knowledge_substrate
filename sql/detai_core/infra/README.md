# infra schema

`sql/detai_core/infra/` хранит SQL-артефакты нейтральной технической schema `infra`
внутри database `detai_core`.

## Что сюда относится

- `infra.schema_migrations`
- compat/migration ledger transitions
- другие database-служебные объекты, которые не являются частью доменной модели
  `ecosystem` или `publications`

## Что сюда не относится

- knowledge/query tables
- metadata
- graph
- embeddings
- project runtime data

## Состав каталога

- `migrations/` — миграции, которые создают или изменяют только техслой `infra`
