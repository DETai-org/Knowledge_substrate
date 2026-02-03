# База данных DETai core

## Расширения

* Включено расширение `pgvector` через `CREATE EXTENSION IF NOT EXISTS vector;`.

## Семантический граф

* Граф семантической похожести хранится в таблице `knowledge.similarity_edges`.
* Рёбра считаются **ненаправленными**: направление нормализуется ограничением
  `CHECK (source_id < target_id)`, а уникальность обеспечивается
  `UNIQUE (source_id, target_id, doc_type, method)`.
* Индексы: `source_id`, `target_id`, `weight DESC`.

## Embeddings

* Таблица `knowledge.embeddings` расширена полями `doc_type`, `source_hash`, `updated_at`.
* `doc_id` хранится как `TEXT`, чтобы использовать канонический `administrative.id` из SoT.
* Текущее хранение использует `vector(1536)` как стартовый стандарт. Если модель
  изменится, потребуется отдельная миграция для обновления размерности.
* В `similarity_edges` внешние ключи на `knowledge.documents(id)` не добавлены,
  потому что `documents.id` имеет тип `BIGINT`, а поля `source_id/target_id`
  определены как `TEXT`.
