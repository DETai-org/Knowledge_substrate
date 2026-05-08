# detai_projects

`sql/detai_projects/` — SQL-контур private project runtime database `detai_projects`.

## Основная идея layout

Здесь одна папка верхнего уровня должна означать одно из двух:

- либо database-wide asset;
- либо конкретную project schema.

То есть git-структура здесь должна отражать реальную модель PostgreSQL:

- одна database `detai_projects`;
- внутри неё несколько project schemas;
- у каждой project schema свой собственный SQL-контур.

## Как читать структуру

### Database-wide assets

Root-level каталоги и файлы относятся ко всей database, а не к одному проекту.

Сейчас сюда относятся:

- `bootstrap/` — создание database `detai_projects`
- `apply_all_migrations.sh` — накатить migrations всех project schemas в этой database
- `README.md` — правила и навигация по database-контуру

### Project schema folders

Каждая project schema получает собственную папку прямо в root:

- `psychology_in_quotes/`
- будущие project folders по тому же правилу

Внутри такой папки должны жить:

- `migrations/`
- `seeds/`
- `apply_migrations.sh`
- schema-specific runbook/README

## Кто что накатывает

### Database-level entrypoints

- `bootstrap/` — создаёт саму database `detai_projects`.
- `apply_all_migrations.sh` — проходит по всем project schema folders и запускает
  их локальные `apply_migrations.sh`.

### Project schema entrypoints

Каждая project schema отвечает только за свой собственный SQL layer:

- `<project>/apply_migrations.sh` — накатывает migrations только этой schema;
- `<project>/seeds/*.sql` — загружает initial seed или schema-specific data import;
- `<project>/README.md` — описывает runbook и границы ответственности проекта.

Иными словами:

- root-level entrypoints управляют database `detai_projects` целиком;
- project folders управляют только своим schema-level контуром.

## Базовый порядок запуска

```bash
cd /srv/Knowledge_substrate/sql/detai_projects
bash bootstrap/create_database.sh
bash apply_all_migrations.sh
```

После этого initial seed накатывается уже на уровне конкретного проекта, потому что
seed и его источник зависят от schema, а не от database целиком.

## Что хранит database `detai_projects`

- users
- user_plans
- moderation
- channel bindings
- user-owned brand kits
- user-owned templates
- runtime audit
- другие project-scoped private operational данные

## Что она не хранит

- канонические ecosystem documents
- канонические publications documents
- system-owned defaults, которые должны жить рядом с кодом
- product output files как primary layer

## Переходный принцип seed

JSON-файлы из `psychology-in-quotes/apps/telegram-bot/runtime-db-seed/` рассматриваются
здесь только как переходный источник initial import.

После перевода runtime-слоя проекта на PostgreSQL:

- JSON seed перестаёт быть primary runtime source;
- bot runtime должен читать и писать напрямую в `detai_projects.psychology_in_quotes`;
- code-owned system defaults остаются в репозитории `psychology-in-quotes`.

## Текущая первая project schema

Первая итерация сейчас реализована для:

- `psychology_in_quotes`

Её runbook находится в:

- `sql/detai_projects/psychology_in_quotes/README.md`
