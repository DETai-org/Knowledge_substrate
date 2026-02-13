# INGEST PIPELINE / ПАЙПЛАЙН ЗАГРУЗКИ

## Что это такое (по-человечески)
Ingest pipeline — это конвейер, который **берёт канонические документы из source_of_truth**, проверяет их метаданные, 
и **синхронизирует** всё в Postgres так, чтобы дальше работали: фильтры, поиск, граф, агенты и векторизация.

## Конфигурация и секреты

### Что хранится в env

Секреты **никогда** не коммитятся в репозиторий и приходят только через env:

* `OPENAI_API_KEY`
* `DATABASE_URL`

Локальный запуск использует `.env` на сервере, запуск через GitHub Actions — `Secrets`.

### Что хранится в config.json

Параметры вычислений, которые **не являются секретами** и могут меняться от запуска к запуску,
живут в `knowledge_core/ingest_pipeline/config.json`:

* `embeddings.*` (model, batch_size, normalize_text, max_chars)
* `graph.*` (top_k, min_similarity, method)
* `execution.*` (mode, limit_posts)

Приоритет источников: **CLI → config.json → env → defaults**.

## Что важно не забыть (чек-лист мыслей)

### 1) Что pipeline обязан делать
- Читать контент из source_of_truth (Markdown + frontmatter).
- Парсить документы в структурированные поля (type, status, taxonomy, links).
- Валидировать ссылки на controlled vocabularies (rubric_id/category_id/keyword_id).
- Делать upsert в БД (идемпотентно: повторный запуск не ломает данные).
- Запускать подпроцесс embeddings:
  - **document embeddings** (1 вектор на документ)
  - **chunk embeddings** (векторы на чанки)

### 2) Политики, которые сильно облегчают жизнь (и относятся именно сюда)
- **Политика “что считается изменением” (hash/mtime)**  
  Нужно определить, как pipeline понимает, что документ изменился и требует обновления в БД/векторов.
- **Политика чанкинга** (по заголовкам / по длине / по абзацам)  
  Нужно определить, как резать документ на chunks для chunk-embeddings и RAG.
  См. политику размеров постов: [source_of_truth/schemas/publications/post_documents/size_policies.md](../source_of_truth/schemas/publications/post_documents/size_policies.md).

### 3) Практический смысл этих политик
- Экономия денег и времени: пересчитывать embeddings только когда надо.
- Предсказуемость: одинаковые правила → стабильный индекс и поиск.
- Безопасность: меньше неожиданных “перезаписей” и случайных обновлений.

---

## Stage-оркестратор (`run_ingest.py`)

Единая точка входа:

```bash
python -m knowledge_core.ingest_pipeline.run_ingest --stage all
```

Поддерживаемые этапы:

- `--stage metadata` — materialization `knowledge.doc_metadata`
- `--stage embeddings` — расчёт/upsert `knowledge.embeddings`
- `--stage edges` — построение/upsert `knowledge.similarity_edges`
- `--stage all` — последовательность `metadata -> embeddings -> edges`

Обязательные env:

- `DATABASE_URL` (или PGHOST/PGPORT/PGUSER/PGPASSWORD/PGDATABASE)
- `OPENAI_API_KEY` (для non-dry-run в embeddings stage)

Примеры запуска:

```bash
python -m knowledge_core.ingest_pipeline.run_ingest --stage metadata
python -m knowledge_core.ingest_pipeline.run_ingest --stage embeddings --limit-posts 20
python -m knowledge_core.ingest_pipeline.run_ingest --stage edges --k 8 --min-similarity 0.75
python -m knowledge_core.ingest_pipeline.run_ingest --stage all
```

## Smoke-проверки

После выполнения этапов проверьте минимально:

```sql
SELECT count(*) FROM knowledge.doc_metadata;
SELECT count(*) FROM knowledge.embeddings;
SELECT count(*) FROM knowledge.similarity_edges;
```

Ожидаемое поведение:
- после `metadata` число строк в `knowledge.doc_metadata` растёт/обновляется;
- после `embeddings` появляются/обновляются строки в `knowledge.embeddings`;
- после `edges` появляются/обновляются строки в `knowledge.similarity_edges`.
