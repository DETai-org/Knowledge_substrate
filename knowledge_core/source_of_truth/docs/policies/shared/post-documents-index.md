# Post Documents Index

Этот файл — описательный индекс для post-document словарей и политик. В Knowledge Substrate `post_documents` означает блоговые посты как один тип публикационного документа внутри более широкого домена `publications`. Рядом с ним остаются `research_publication` и `quote`.

JSON-источники лежат отдельно в [docs/schemas/post_documents](../../schemas/post_documents). Markdown-политики и человекочитаемые описания лежат здесь, в [docs/policies/shared](.).

Эти файлы являются зеркалом сайта:

- [sites/docs/schemas/post_documents](https://github.com/DETai-org/sites/tree/main/docs/schemas/post_documents)
- [sites/docs/schemas/authors.json](https://github.com/DETai-org/sites/blob/main/docs/schemas/authors.json)
- [sites/docs/policies/shared](https://github.com/DETai-org/sites/tree/main/docs/policies/shared)

Если меняются JSON-словари или policies для блога, сначала обновляется репозиторий `sites`, затем копия синхронизируется сюда.

## JSON-источники

| JSON | Назначение |
| --- | --- |
| [categories.json](../../schemas/post_documents/categories.json) | Канонический словарь категорий, emoji, scope и landing-page флагов. |
| [rubrics.json](../../schemas/post_documents/rubrics.json) | Канонический словарь рубрик, локализованных route slugs, описаний и site availability. |
| [cycle.json](../../schemas/post_documents/cycle.json) | Канонический словарь тематических циклов. |
| [sizes.json](../../schemas/post_documents/sizes.json) | Канонический словарь размеров постов. Сейчас используются только M и L. |
| [keywords.json](../../schemas/post_documents/keywords.json) | Канонический словарь ключевых слов. |

Общий справочник авторов не является post-document словарём, но используется блоговой публикацией: [authors.json](../../schemas/authors.json).

## Markdown-политики

| Policy | Назначение |
| --- | --- |
| [categories-policy.md](categories-policy.md) | Правила категорий, таблица и описания категорий из JSON. |
| [rubrics-policy.md](rubrics-policy.md) | Правила рубрик, таблица, пояснение route slugs и описания рубрик из JSON. |
| [cycles-policy.md](cycles-policy.md) | Правила тематических циклов и список циклов из JSON. |
| [sizes-policy.md](sizes-policy.md) | Правила размеров постов и список размеров из JSON. |
| [post-creation-prompt.md](post-creation-prompt.md) | Рабочий prompt для создания/нормализации post documents. |
| [post-taxonomy-overview.md](post-taxonomy-overview.md) | Общее описание слоя таксономии. |
| [authors-policy.md](authors-policy.md) | Правила общего справочника авторов и использования author-фильтра. |

## Синхронизация

Канонические operational-копии этих документов и JSON-словарей для сайта:

- JSON schemas: [sites/docs/schemas/post_documents](https://github.com/DETai-org/sites/tree/main/docs/schemas/post_documents)
- Markdown policies: [sites/docs/policies/shared](https://github.com/DETai-org/sites/tree/main/docs/policies/shared)

Копии в Knowledge Substrate:

- JSON schemas mirror: `knowledge_core/source_of_truth/docs/schemas/post_documents`
- Publications schema mirror: `knowledge_core/source_of_truth/schemas/publications/post_documents`
- Markdown policies mirror: `knowledge_core/source_of_truth/docs/policies/shared`
