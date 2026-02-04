# DET / DETai — Knowledge Core

Knowledge Core — это центральный контур экосистемы **DET / DETai**, в котором зафиксированы:
- канон знаний (Source of Truth),
- правила их структурирования ,
- пайплайны преобразования,
- операционное хранение и сервисы доступа.

Ниже — общий обзор уровней и взаимосвязей, а также схема, показывающая поток данных от канона к производным системам.

## Общая схема

```mermaid
flowchart TD
    A["GitHub Repo: Markdown + Frontmatter\n(Источник истины контента / Content Source of Truth)"] --> B["Sync Trigger\n(Триггер синхронизации / Scheduler, Cron, Webhook)"]
    B --> C["INGEST PIPELINE / ПАЙПЛАЙН ЗАГРУЗКИ"]

    C --> C1["Parse / Парсинг\n(Markdown → structured data)"]
    C --> C2["Validate / Валидация\n(IDs vs Controlled Vocabularies)"]
    C --> C3["Upsert / Идемпотентная запись\n(Postgres)"]
    C --> C4["Link building / Построение связей\n(document_links, external_links)"]
    C --> C5["EMBEDDING SUBPIPELINE / ПОДПРОЦЕСС ВЕКТОРИЗАЦИИ"]

    C5 --> C51["Document Embeddings / Векторы документа\n(1 vector per doc)"]
    C5 --> C52["Chunk Embeddings / Векторы чанков\n(N vectors per doc)"]

    C --> D["Postgres / Cloud SQL: publications_schema\n(Операционное хранилище / Operational Store)"]
    D --> D1[documents]
    D --> D2["taxons\n(rubrics/categories/keywords/subrubrics)"]
    D --> D3["document_taxons\n(join table)"]
    D --> D4[document_links / external_links]
    D --> D5[embeddings_documents]
    D --> D6[embeddings_chunks]

    D --> E["API DOOR / API-ДВЕРЬ (FastAPI)\n(Сервис доступа / Query & Write Service)"]
    E --> E1["Filter search / Фильтры\n(rubric/category/status/date)"]
    E --> E2["Semantic search / Семантический поиск\n(vectors)"]
    E --> E3["Graph queries / Графовые запросы\n(links)"]
    E --> E4["Agent endpoints / Эндпоинты для агентов"]

    E --> F[Clients / Потребители]
    F --> F1["Website UI / Сайт\n(поиск, фильтры, граф)"]
    F --> F2["Admin UI / Админка\n(ревью keywords candidates)"]
    F --> F3["Agents / Агенты\n(RAG, рекомендации, кластеризация)"]
```

## Основные уровни и разделы

### 1. Source of Truth — канон знаний
- Каталог `source_of_truth/` содержит **первичные канонические документы**, метаданные и словари.
- Здесь же определены **схемы как контракты** — правила фиксации, идентификации и связи информации.
- Папка `source_of_truth/docs/` одновременно служит **базой знаний** и **витриной MkDocs**.

Подробнее: `knowledge_core/source_of_truth/README.md`.

### 2. Ingest Pipeline — преобразование канона
- Каталог `ingest_pipeline/` описывает процесс парсинга, валидации и загрузки данных.
- Здесь задаются правила трансформации Markdown в структурированные записи,
  а также вспомогательные политики для последующей индексации и RAG.

#### Навигация: Semantic Graph for Posts
- ADR: [ADR-0001: Semantic Similarity Graph for Posts](ADR/adr-0001-semantic-similarity-graph-posts.md)
- Guide: [Guide: Semantic Similarity Graph for Posts](guides/guide-semantic-graph-posts.md)
- Policy: [Policy: Semantic Graph for Posts](Policy/policy-semantic-graph-posts.md)
- Sub-Issue (Work Package): [1-sub-issue-semantic-graph-posts.md](../issue/1-sub-issue-semantic-graph-posts.md)
- **Концептуальная задумка** размещена в базе знаний на MkDocs: [Semantic Similarity Graph — Explanation](https://detai-org.github.io/Knowledge_substrate/ru/ecosystem/Infrastructure/Knowledge_Substrate/knowledge_core/Explanation/)

### 3. Operational Store — рабочие представления
- Каталог `operational_store/` хранит модели и структуры данных,
  которые используются в **операционных БД** и сервисах доступа.
- Это производный слой: он полностью воспроизводим из Source of Truth.

---

Если требуется менять структуру уровней, сначала согласуйте общую схему и роли разделов,
затем обновляйте детали на уровне конкретных подпапок.
