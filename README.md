[GitHub Repo: Markdown + Frontmatter]
(Источник истины контента / Content Source of Truth)
                |
                v
[Sync Trigger]
(Триггер синхронизации / Scheduler, Cron, Webhook)
                |
                v
[INGEST PIPELINE / ПАЙПЛАЙН ЗАГРУЗКИ]
  ├─ Parse / Парсинг (Markdown -> structured data)
  ├─ Validate / Валидация (IDs vs Controlled Vocabularies)
  ├─ Upsert / Идемпотентная запись (Postgres)
  ├─ Link building / Построение связей (document_links, external_links)
  └─ EMBEDDING SUBPIPELINE / ПОДПРОЦЕСС ВЕКТОРИЗАЦИИ
       ├─ Document Embeddings / Векторы документа (1 vector per doc)
       └─ Chunk Embeddings / Векторы чанков (N vectors per doc)
                |
                v
[Postgres / Cloud SQL: publications_schema]
(Операционное хранилище / Operational Store)
  ├─ documents
  ├─ taxons (rubrics/categories/keywords/subrubrics)
  ├─ document_taxons (join table)
  ├─ document_links / external_links
  ├─ embeddings_documents
  └─ embeddings_chunks
                |
                v
[API DOOR / API-ДВЕРЬ (FastAPI)]
(Сервис доступа / Query & Write Service)
  ├─ Filter search / Фильтры (rubric/category/status/date)
  ├─ Semantic search / Семантический поиск (vectors)
  ├─ Graph queries / Графовые запросы (links)
  └─ Agent endpoints / Эндпоинты для агентов
                |
                v
[Clients / Потребители]
  ├─ Website UI / Сайт (поиск, фильтры, граф)
  ├─ Admin UI / Админка (ревью keywords candidates)
  └─ Agents / Агенты (RAG, рекомендации, кластеризация)

