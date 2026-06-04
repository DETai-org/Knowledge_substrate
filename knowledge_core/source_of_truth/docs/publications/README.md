# Publications

Домен публикаций хранит сами publication-документы.

Внутри него постепенно раскладываются отдельные document families:
- `blogs/`
- `Research_Publication/`
- `quotes/`

`blogs/` — это post documents: пасты/снимки страниц блога с обоих сайтов, сохранённые как публикационные материалы.
`Research_Publication/` и `quotes/` остаются отдельными семьями документов внутри того же publication-домена.

Если файл является публикационным материалом, он должен жить здесь.
Если файл описывает контракт этого материала, он должен жить в `schemas/publications/`.

`docs/publications/` не участвует в MkDocs-сборке и не относится к GitHub Pages-витрине экосистемных знаний.
Публикационные материалы живут на основном сайте и связаны с репозиторием:
[DETai-org/sites](https://github.com/DETai-org/sites/)
