# Post Taxonomy Overview

Этот документ объясняет общую логику таксономии блоговых `post`-документов.

## Технический аналог

- `../../schemas/post_documents/rubrics.json`
- `../../schemas/post_documents/categories.json`
- `../../schemas/post_documents/cycle.json`
- `../../schemas/post_documents/sizes.json`
- `../../schemas/post_documents/keywords.json`

## Основная модель

- Рубрика у поста ровно одна.
- Категорий у поста может быть несколько.
- `keywords_raw` пока является рабочим слоем.
- `keyword_ids` пока не считаются утверждённым повторно используемым словарём.

## Shared vs unique

Для рубрик и категорий используется поле `scope`.

- `shared` — сущность доступна обоим сайтам.
- `detai-only` — сущность доступна только профессиональному сайту.
- `personal-only` — сущность доступна только персональному сайту.

На страницах блогов это отображается как:

- `Общие рубрики`
- `Уникальные рубрики`
- `Общие категории`
- `Уникальные категории`

## Frontmatter

Во frontmatter поста нет отдельного поля для shared/unique. Пост хранит только ID:

- `rubric_ids`
- `category_ids`
- `keyword_ids`
- `keywords_raw`

Принадлежность к сайту и тип сущности вычисляются через JSON-реестры.
