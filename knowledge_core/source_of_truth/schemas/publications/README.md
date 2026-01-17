# Publications Schema — Source of Truth

Этот раздел описывает **типы документов внутри схемы публикаций** и их базовые правила.
Подробные документы, словари и политики разнесены по папкам ниже.

## Типы документов

В `publications_schema` существуют основные типы:

- **post** — основной тип публикаций (посты, эссе, заметки);
- **research_publication** — научные публикации (статьи, диссертации, тезисы);
- **quote** — цитаты.

Контракт схемы хранится в `research_publication/publications_schema.md`
(в канонической формулировке, описывающей все типы документов).

## Структура раздела

- `post_documents/` — правила и словари для документов типа **post**:
  - `README.md` — краткая политика и сущности типа;
  - `categories.json`, `rubrics.json`, `keywords.json`, `cycle.json`;
  - `_indexes_min.md` — быстрый обзор сущностей;
  - подробные политики (`category_policies.md`, `keywords_policy.md`,
    `rubrics_and_subrubrics_policy.md`, `preview_policies.md`).
- `research_publication/` — заглушка под документы и правила научных публикаций.

## Связанные разделы

- Общие правила схем и словарей: `knowledge_core/source_of_truth/schemas/README.md`.
- Тематические циклы (канонический словарь для постов): `knowledge_core/source_of_truth/schemas/publications/post_documents/cycle.json`.
- Ingest & RAG hybrid model: `knowledge_core/ingest_pipeline/policies/ingest_and_rag_hybrid_model.md`.
