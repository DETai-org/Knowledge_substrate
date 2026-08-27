# detai_projects

`sql/detai_projects/` — SQL-контур private project runtime database `detai_projects`.

## Основная идея layout

Здесь одна папка верхнего уровня должна означать одно из двух:

- либо database-wide asset;
- либо shared runtime schema.

То есть git-структура здесь должна отражать реальную модель PostgreSQL:

- одна database `detai_projects`;
- в этом репозитории — shared runtime schemas для общих operational-доменов;
- исполняемый SQL конкретного продукта хранится в owning repository этого продукта.

## Как читать структуру

### Database-wide assets

Root-level каталоги и файлы относятся ко всей database, а не к одному проекту.

Сейчас сюда относятся:

- `bootstrap/` — создание database `detai_projects`
- `apply_all_migrations.sh` — накатить migrations всех project schemas в этой database
- `README.md` — правила и навигация по database-контуру

### Shared runtime schema folders

Shared runtime schemas не принадлежат одному продукту. Они обслуживают
экосистемные operational-домены, на которые могут ссылаться разные project
schemas.

Сейчас как draft-contours зафиксированы:

- `identity/` — общий слой пользовательской идентичности;
- `access/` — общий слой прав, ролей, подписок и доступов.
- `ecosystem_events/` — календарный и событийный слой экосистемы;
- `intake/` — входящие формы, заявки, регистрации, предложения и жалобы;
- `notifications/` — подписки, dispatch jobs и delivery logs.

Эти каталоги пока являются черновыми контурами. Production migrations должны
появиться только после отдельного согласования schema contract.

### Project-owned schemas

Project schema может физически находиться в database `detai_projects`, но её
исполняемые migrations, seeds, проверки и runbook принадлежат продукту и не
дублируются в `Knowledge_substrate`.

Для `psychology_in_quotes` канонический контур находится в owning repository
[`DETai-org/psychology-in-quotes`](https://github.com/DETai-org/psychology-in-quotes),
в каталоге `db/psychology_in_quotes/`.

## Кто что накатывает

### Database-level entrypoints

- `bootstrap/` — создаёт саму database `detai_projects`.
- `apply_all_migrations.sh` — запускает локальные migration entrypoints только
  для schema-контуров, которыми владеет этот репозиторий.

### Project schema entrypoints

Project-specific migrations запускаются по runbook owning repository. Root-level
entrypoints этого каталога не являются источником migrations продуктов.

## Базовый порядок запуска

```bash
cd /srv/Knowledge_substrate/sql/detai_projects
bash bootstrap/create_database.sh
bash apply_all_migrations.sh
```

После этого project-specific migrations и seed накатываются из owning repository
проекта по его собственному runbook.

## Что хранит database `detai_projects`

- users
- user_plans
- moderation
- channel bindings
- user-owned brand kits
- user-owned templates
- runtime audit
- другие project-scoped private operational данные

Общие пользовательские и access-данные должны постепенно выделяться из
project-local таблиц в shared runtime schemas:

- `identity`
- `access`
- `ecosystem_events`
- `intake`
- `notifications`

## Что она не хранит

- канонические ecosystem documents
- канонические publications documents
- system-owned defaults, которые должны жить рядом с кодом
- product output files как primary layer

## Boundary policy

Общая карта ответственности между `Knowledge_substrate`, `detai_core`,
`detai_projects`, `ecosystem-runtime` и `sites` зафиксирована в:

- [Policy: Runtime Boundary Map](../../docs/Policy/runtime-boundaries.policy.md)

## Ownership проекта Psychology in Quotes

Старая исполняемая копия migrations и seed для `psychology_in_quotes`, основанная
на Telegram ID, удалена из этого репозитория. Актуальная модель идентичности,
migrations, роли, проверки и runbook поддерживаются в owning repository
[`DETai-org/psychology-in-quotes`](https://github.com/DETai-org/psychology-in-quotes),
в каталоге `db/psychology_in_quotes/`.
