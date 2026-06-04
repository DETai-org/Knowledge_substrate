# Post Creation Prompt

Короткая техническая памятка для создания новых блоговых постов.

## Куда сохранять blog post document

Блоговые post documents находятся в публикационном слое:

- `docs/publications/blogs/detai_site_blog/`
- `docs/publications/blogs/personal_site_blog/`

Если пост публикуется на оба сайта, один и тот же файл должен существовать в обеих site-папках.

## Где лежат правила

- рубрики: `../../schemas/publications/post_documents/rubrics.json` + `rubrics-policy.md`
- категории: `../../schemas/publications/post_documents/categories.json` + `categories-policy.md`
- публикация на один или два сайта: `publication-policy.md`

## Таксономия

- `rubric_ids` — ровно одна рубрика
- `category_ids` — одна или несколько категорий
- `keywords_raw` — рабочий слой ключевых слов
- `keyword_ids` — пока не использовать как обязательный словарь

## Важное ограничение

Если `administrative.channels` содержит и `detai_site_blog`, и `personal_site_blog`, нельзя назначать `detai-only` или `personal-only` рубрики и категории.


## Расположение

Этот prompt хранится в Markdown-политиках, а не в папке JSON-схем. JSON-источники остаются в [schemas/publications/post_documents](../../schemas/publications/post_documents).
