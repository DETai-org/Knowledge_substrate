# `docs/` — слой документов

`docs/` в `Knowledge_substrate` хранит только документы и их человекочитаемые описания.

## Что важно после реструктуризации

- Документы и policies остаются в `docs/`.
- Машинно-читаемые реестры для blog post documents лежат в `docs/schemas/post_documents/` как зеркало operational-слоя сайта.
- Временное хранилище входящих блог-постов вынесено из `docs/` в `../storage/publications/blogs/`.
- `post_documents` — только один тип публикационного документа внутри домена publications. Рядом с ним в базе знаний остаются `research_publication` и `quote`.

## Зеркало сайта

Словари и policies для blog post documents синхронизируются с репозиторием сайта:

- [sites/docs/schemas/post_documents](https://github.com/DETai-org/sites/tree/main/docs/schemas/post_documents)
- [sites/docs/schemas/authors.json](https://github.com/DETai-org/sites/blob/main/docs/schemas/authors.json)
- [sites/docs/policies/shared](https://github.com/DETai-org/sites/tree/main/docs/policies/shared)

В `Knowledge_substrate` эти файлы нужны для согласования базы знаний, ingest/RAG и будущих связей между постами, research publications и quotes. Изменения taxonomy/policy сначала фиксируются в `sites`, затем зеркалируются сюда.

## Домены

- `docs/ecosystem/...` — документация экосистемы
- `docs/publications/quotes/...` — экземпляры quote-документов
- `docs/policies/...` — человекочитаемые политики
- `docs/schemas/post_documents/...` — JSON-реестры и технические схемы для `post`

## Отдельно про blog storage

Временные папки `detai_site_blog` и `personal_site_blog` больше не считаются частью document-layer.
Они лежат в:

- `knowledge_core/source_of_truth/storage/publications/blogs/detai_site_blog/`
- `knowledge_core/source_of_truth/storage/publications/blogs/personal_site_blog/`
