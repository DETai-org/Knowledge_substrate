# storage/publications/blogs

Это временное хранилище входящих блог-постов для двух сайтов.

## Назначение

- сюда попадают новые и обновлённые markdown-файлы постов;
- отсюда workflow синхронизирует их в репозиторий `DETai-org/sites`;
- рядом хранится `list_publication_blogs.json` как реестр уже обработанных публикаций.

## Папки

- `detai_site_blog/`
- `personal_site_blog/`

## Синхронизация

Workflow: [Sync Blog Posts to Site](https://github.com/DETai-org/Knowledge_substrate/blob/main/.github/workflows/sync-blog-posts.yml)

Целевой путь в репозитории `sites`:
[storage/publications/blogs](https://github.com/DETai-org/sites/tree/main/storage/publications/blogs)
