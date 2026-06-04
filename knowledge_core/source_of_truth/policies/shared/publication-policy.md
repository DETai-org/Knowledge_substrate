# Publication Policy

Связанные технические файлы:

- `../../schemas/publications/post_documents/rubrics.json`
- `../../schemas/publications/post_documents/categories.json`
- `post-creation-prompt.md`

## Основные правила

- Пост может публиковаться на одном сайте или сразу на двух.
- Если `administrative.channels` содержит оба сайта, пост не должен использовать `detai-only` или `personal-only` рубрики и категории.
- Если такая ситуация возникает, нужно либо:
  - сменить рубрику или категорию на `shared`,
  - либо пересмотреть набор каналов публикации.

## Таксономия

- `rubric_ids` — ровно одна рубрика.
- `category_ids` — одна или несколько категорий.
- `keywords_raw` — текущий рабочий слой ключевых слов.
