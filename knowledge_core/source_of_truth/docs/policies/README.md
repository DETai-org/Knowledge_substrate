# Policies

В этой папке хранятся описательные Markdown-политики для публикационных документов базы знаний.

- JSON-словари post-document слоя лежат в [docs/schemas/post_documents](../schemas/post_documents).
- Общий справочник авторов лежит в [docs/schemas/authors.json](../schemas/authors.json).
- Человекочитаемые правила и таблицы лежат в [shared](shared).
- Подробный индекс post-document слоя: [shared/post-documents-index.md](shared/post-documents-index.md).

## Роль в Knowledge Substrate

`post_documents` описывает блоговые посты как один тип публикационного документа. Это не весь слой publications: рядом остаются `research_publication` для научных публикаций и `quote` для цитат.

Post-document policies являются зеркальной копией документов из репозитория сайта:

- [sites/docs/policies/shared](https://github.com/DETai-org/sites/tree/main/docs/policies/shared)
- [sites/docs/schemas/post_documents](https://github.com/DETai-org/sites/tree/main/docs/schemas/post_documents)

Дублирующие policy bundle-папки удалены: единая рабочая зона политик — [docs/policies/shared](shared).
