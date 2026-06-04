# `docs/` — слой документов

`docs/` в `Knowledge_substrate` хранит только экземпляры документов.

## Что важно после реструктуризации

- Policies вынесены из `docs/` в `../policies/`.
- Машинно-читаемые реестры для blog post documents лежат в `../schemas/publications/post_documents/`.
- Блоговые публикации из бывшего storage-слоя живут в `publications/blogs/`.
- `post_documents` — только один тип публикационного документа внутри домена publications. Рядом с ним в базе знаний остаются `research_publication` и `quote`.

## Зеркало сайта

Словари и policies для blog post documents синхронизируются с репозиторием сайта:

- [sites/docs/schemas/post_documents](https://github.com/DETai-org/sites/tree/main/docs/schemas/post_documents)
- [sites/docs/schemas/authors.json](https://github.com/DETai-org/sites/blob/main/docs/schemas/authors.json)
- [sites/docs/policies/shared](https://github.com/DETai-org/sites/tree/main/docs/policies/shared)

В `Knowledge_substrate` эти файлы нужны для согласования базы знаний, ingest/RAG и будущих связей между постами, research publications и quotes. Изменения taxonomy/policy сначала фиксируются в `sites`, затем зеркалируются сюда.

## Домены

- `docs/ecosystem/...` — документация экосистемы
- `docs/publications/blogs/...` — блоговые post documents с двух сайтов
- `docs/publications/quotes/...` — экземпляры quote-документов
- `docs/publications/Research_Publication/...` — научные публикации

## Связанные слои

- `../schemas/publications/post_documents/...` — JSON-реестры и технические схемы для `post`
- `../policies/shared/...` — человекочитаемые политики для публикационных документов
