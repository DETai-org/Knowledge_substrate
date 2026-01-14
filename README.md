# Knowledge Substrate

```mermaid
flowchart TD
    A[GitHub Repo: Markdown + Frontmatter<br/>(Источник истины контента / Content Source of Truth)] --> B[Sync Trigger<br/>(Триггер синхронизации / Scheduler, Cron, Webhook)]
    B --> C[INGEST PIPELINE / ПАЙПЛАЙН ЗАГРУЗКИ]

    C --> C1[Parse / Парсинг<br/>(Markdown → structured data)]
    C --> C2[Validate / Валидация<br/>(IDs vs Controlled Vocabularies)]
    C --> C3[Upsert / Идемпотентная запись<br/>(Postgres)]
    C --> C4[Link building / Построение связей<br/>(document_links, external_links)]
    C --> C5[EMBEDDING SUBPIPELINE / ПОДПРОЦЕСС ВЕКТОРИЗАЦИИ]

    C5 --> C51[Document Embeddings / Векторы документа<br/>(1 vector per doc)]
    C5 --> C52[Chunk Embeddings / Векторы чанков<br/>(N vectors per doc)]

    C --> D[Postgres / Cloud SQL: publications_schema<br/>(Операционное хранилище / Operational Store)]
    D --> D1[documents]
    D --> D2[taxons<br/>(rubrics/categories/keywords/subrubrics)]
    D --> D3[document_taxons<br/>(join table)]
    D --> D4[document_links / external_links]
    D --> D5[embeddings_documents]
    D --> D6[embeddings_chunks]

    D --> E[API DOOR / API-ДВЕРЬ (FastAPI)<br/>(Сервис доступа / Query & Write Service)]
    E --> E1[Filter search / Фильтры<br/>(rubric/category/status/date)]
    E --> E2[Semantic search / Семантический поиск<br/>(vectors)]
    E --> E3[Graph queries / Графовые запросы<br/>(links)]
    E --> E4[Agent endpoints / Эндпоинты для агентов]

    E --> F[Clients / Потребители]
    F --> F1[Website UI / Сайт<br/>(поиск, фильтры, граф)]
    F --> F2[Admin UI / Админка<br/>(ревью keywords candidates)]
    F --> F3[Agents / Агенты<br/>(RAG, рекомендации, кластеризация)]
```
