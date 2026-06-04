# Blogs

Это publication-family для блоговых post documents.

По сути здесь лежат пасты и снимки страниц блога с обоих сайтов: материалы уже являются публикациями или подготовлены как публикационные материалы для синхронизации с сайтом.

## Назначение

- сюда попадают новые и обновлённые Markdown-файлы постов;
- здесь сохраняется канонический слой блоговых публикаций внутри `source_of_truth/docs/publications/`;
- отсюда workflow синхронизирует посты в operational-слой репозитория `DETai-org/sites`;
- рядом хранится `list_publication_blogs.json` как реестр уже обработанных публикаций.

## Папки

- `detai_site_blog/`
- `personal_site_blog/`

## Синхронизация

Workflow: [Sync Blog Posts to Site](https://github.com/DETai-org/Knowledge_substrate/blob/main/.github/workflows/sync-blog-posts.yml)

Целевой путь в репозитории `sites`:
[storage/publications/blogs](https://github.com/DETai-org/sites/tree/main/storage/publications/blogs)
