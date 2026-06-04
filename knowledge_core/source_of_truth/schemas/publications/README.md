# Publications Schema — Source of Truth

Этот раздел описывает **типы документов внутри схемы публикаций** и их базовые правила.
Подробные документы, словари и политики разнесены по папкам ниже.

## Типы документов

В `publications_schema` существуют основные типы:

- **post** — блоговые публикации сайта: посты, эссе, заметки;
- **research_publication** — научные публикации: статьи, диссертации, тезисы;
- **quote** — цитаты как отдельные publication records.

`post_documents` не равен всему домену publications. Это блоговый подслой, который сейчас синхронизирован с репозиторием сайта. `research_publication` и `quote` остаются отдельными типами документов и развиваются по своим контрактам.

Контракт схемы хранится в `publications_schema.md`
(в канонической формулировке, описывающей все типы документов).

## Структура раздела

- `post_documents/` — правила и словари для документов типа **post**:
  - `categories.json`, `rubrics.json`, `keywords.json`, `cycle.json`, `sizes.json`;
  - это зеркало [sites/docs/schemas/post_documents](https://github.com/DETai-org/sites/tree/main/docs/schemas/post_documents).
- `quotes/` — контракт Quote Record и связанные правила для документов типа **quote**.
- `research_publication/` — заглушка под документы и правила научных публикаций.
- `publications_schema.md` — канонический контракт схемы публикаций.

## Разделение ответственности

- `publications_schema.md` — верхнеуровневый общий контракт по типам документов.
- `post_documents/` — детальный контракт и controlled vocabularies для `post`.
- `quotes/` — детальный контракт Quote Record для `quote`.
- `research_publication/` — место для детального контракта `research_publication`.

## Связанные разделы

- Общие правила схем и словарей: `knowledge_core/source_of_truth/schemas/README.md`.
- Тематические циклы (зеркальный словарь для постов): `knowledge_core/source_of_truth/docs/schemas/post_documents/cycle.json`.
- Operational source for website blog taxonomy: [DETai-org/sites docs/schemas/post_documents](https://github.com/DETai-org/sites/tree/main/docs/schemas/post_documents).
- Ingest & RAG hybrid model: `knowledge_core/ingest_pipeline/policies/ingest_and_rag_hybrid_model.md`.
