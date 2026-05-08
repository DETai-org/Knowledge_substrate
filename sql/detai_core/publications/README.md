# publications schema

`sql/detai_core/publications/` хранит SQL-артефакты schema `publications`
внутри database `detai_core`.

Эта schema обслуживает текущий canonical/query SQL-слой публикационного домена:

- publication metadata
- publication graph
- publication embeddings
- publication query-facing tables

## Что сюда относится

- `publications.documents`
- `publications.links`
- `publications.embeddings`
- `publications.similarity_edges`
- `publications.doc_metadata`
- диагностические SQL-проверки publication graph/query слоя

## Состав каталога

- `migrations/` — schema-specific миграции publications-layer
- `diagnostics/` — SQL-диагностики и KPI-проверки

## Каноническая диагностика

```bash
cd sql/detai_core
psql "$DATABASE_URL" -f publications/diagnostics/graph_embedding_kpi.sql
```

## Важная граница

- `infra.schema_migrations` не относится к этой schema.
- ecosystem SQL-представления сюда не относятся.
- project runtime data сюда не относятся.
