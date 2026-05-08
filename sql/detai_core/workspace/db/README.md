# База данных DETai core

## Расширения

* Включено расширение `pgvector` через `CREATE EXTENSION IF NOT EXISTS vector;`.

## Семантический граф

* Граф семантической похожести хранится в таблице `knowledge.similarity_edges`.
* Рёбра считаются **ненаправленными**: направление нормализуется ограничением
  `CHECK (source_id < target_id)`, а уникальность обеспечивается
  `UNIQUE (source_id, target_id, doc_type, method)`.
* Индексы: `source_id`, `target_id`, `weight DESC`.


## Metadata-узлы для graph API v1

* Таблица `knowledge.doc_metadata` — канонический источник metadata для graph API.
* Канонический идентификатор: `doc_id TEXT PRIMARY KEY`, где `doc_id = administrative.id` из SoT.
* `knowledge.documents.id (BIGSERIAL)` **не является** canonical id для semantic graph.
* Минимальные поля и типы для v1:
  * `date_ymd DATE`, вычисляемый `year INTEGER` (generated column),
  * `channels TEXT[]`, `authors TEXT[]`, `rubric_ids TEXT[]`, `category_ids TEXT[]`,
  * `doc_type TEXT`, `updated_at TIMESTAMPTZ`, `meta JSONB`.
* Контракт сериализации для API v1:
  * массивные поля всегда сериализуются как JSON-массивы строк (включая пустые `[]`),
  * отсутствующий год сериализуется как `null`,
  * произвольные расширения metadata сериализуются через `meta`.

## Embeddings

* Таблица `knowledge.embeddings` расширена полями `doc_type`, `source_hash`, `updated_at`.
* `doc_id` хранится как `TEXT`, чтобы использовать канонический `administrative.id` из SoT.
* Текущее хранение использует `vector(1536)` как стартовый стандарт. Если модель
  изменится, потребуется отдельная миграция для обновления размерности.
* В `similarity_edges` внешние ключи на `knowledge.documents(id)` не добавлены,
  потому что `documents.id` имеет тип `BIGINT`, а поля `source_id/target_id`
  определены как `TEXT`.


## Индексы для фильтров graph API v1

* Для `knowledge.doc_metadata` добавлены индексы:
  * BTREE: `year`, `date_ymd`;
  * GIN: `channels`, `authors`, `rubric_ids`, `category_ids`.
* Для `knowledge.similarity_edges` используются индексы `source_id`, `target_id`, `weight DESC`.
  В стратегии `/v1/graph` выборка рёбер идёт по `source_id/target_id` внутри отфильтрованного множества `doc_id`.

## Канонические KPI мониторинга (embeddings + graph)

* SQL-проверки вынесены в `workspace/db/diagnostics/graph_embedding_kpi.sql`.
* Ключевая правка по unique edge docs: использовать `UNION source_id/target_id`,
  а не сумму двух `count(distinct ...)`.
* Канонические KPI:
  * `posts_total` — общее число постов в каноническом источнике (`knowledge.doc_metadata`, `doc_type='post'`);
  * `posts_with_embedding` — число постов с embeddings (`knowledge.embeddings`, `doc_type='post'`);
  * `posts_missing_embedding` — сколько постов ещё без embeddings;
  * `embedding_duplicates` — сколько `doc_id` имеют дубликаты embeddings (`HAVING count(*) > 1`);
  * `edge_docs_missing_metadata` и `edge_docs_missing_metadata_ratio` — качество metadata покрытия endpoint-ов графа.
* Критерий готовности к прод:
  * **Embeddings готовы**: `posts_missing_embedding = 0` и `embedding_duplicates = 0`.
  * **Global graph стабилен**: `edge_docs_missing_metadata_ratio` ниже согласованного порога.
