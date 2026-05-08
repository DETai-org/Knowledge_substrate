# detai_projects DB Runbook

Этот runbook описывает **первую infra-итерацию** private runtime database для проекта `psychology-in-quotes`.

## Цель итерации

Собрать и применить SQL-контур, который:

- создаёт database `detai_projects`;
- создаёт schema `psychology_in_quotes`;
- создаёт первый рабочий набор runtime tables;
- загружает initial data snapshot из текущих JSON seed-файлов проекта `psychology-in-quotes`.

Эта итерация **не** переписывает Telegram-бота на SQL. Бот пока может продолжать жить на текущем runtime JSON, пока в проекте `psychology-in-quotes` не будет добавлен отдельный database access layer.

## Граница ответственности

### Что делает `Knowledge_substrate`

- хранит SQL bootstrap, migrations и seed для `detai_projects`;
- фиксирует структуру runtime schema `psychology_in_quotes`;
- задаёт runbook применения и initial import.

### Что делает `psychology-in-quotes`

- хранит bot application code;
- временно остаётся владельцем текущих JSON runtime seed-файлов;
- в следующей итерации должен перейти на прямое чтение и запись в PostgreSQL.

## Источник initial seed

Initial import берётся из текущего operational snapshot в соседнем репозитории:

```text
D:\dev\DETai-org\psychology-in-quotes\apps\telegram-bot\runtime-db-seed\
```

С точки зрения сервера это означает: перед применением initial seed нужно либо подготовить эквивалентный SQL snapshot, либо запустить импорт из актуального checked-out состояния проекта `psychology-in-quotes`.

В этом репозитории зафиксирован SQL seed snapshot, собранный из текущих файлов:

- `config/user-access.json`
- `config/channel-bindings.json`
- `config/moderation.json`

`access-control.json` в эту итерацию не переносится в SQL и не считается primary source.

## Состав файлов

- `bootstrap/0000_create_database.sql` — создаёт database `detai_projects`, если её ещё нет.
- `bootstrap/create_database.sh` — shell-wrapper для применения bootstrap.
- `migrations/0001_psychology_in_quotes_runtime.sql` — создаёт schema, функции, таблицы и индексы.
- `seeds/0001_psychology_in_quotes_initial_seed.sql` — initial import текущего snapshot.
- `apply_migrations.sh` — накатывает migrations на database `detai_projects`.

## Порядок применения на сервере

### 1. Создать database

```bash
cd /srv/Knowledge_substrate/sql/detai_projects
bash workspace/db/bootstrap/create_database.sh
```

### 2. Накатить migrations

```bash
cd /srv/Knowledge_substrate/sql/detai_projects
bash workspace/db/apply_migrations.sh
```

### 3. Загрузить initial seed

```bash
sudo -u postgres psql -d detai_projects -v ON_ERROR_STOP=1 -f /srv/Knowledge_substrate/sql/detai_projects/workspace/db/seeds/0001_psychology_in_quotes_initial_seed.sql
```

## Проверка результата

### Проверка database и schema

```bash
sudo -u postgres psql -Atqc "SELECT datname FROM pg_database WHERE datname = 'detai_projects';"
sudo -u postgres psql -d detai_projects -Atqc "SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'psychology_in_quotes';"
```

### Проверка таблиц

```bash
sudo -u postgres psql -d detai_projects -Atqc "SELECT table_name FROM information_schema.tables WHERE table_schema = 'psychology_in_quotes' ORDER BY table_name;"
```

### Проверка initial rows

```bash
sudo -u postgres psql -d detai_projects -Atqc "SELECT count(*) FROM psychology_in_quotes.users;"
sudo -u postgres psql -d detai_projects -Atqc "SELECT count(*) FROM psychology_in_quotes.user_plans;"
sudo -u postgres psql -d detai_projects -Atqc "SELECT count(*) FROM psychology_in_quotes.channel_bindings;"
sudo -u postgres psql -d detai_projects -Atqc "SELECT count(*) FROM psychology_in_quotes.moderation_entries;"
```

## Важные ограничения этой итерации

- `detai_core` не трогаем и не используем для новых project runtime данных.
- `product` schema внутри `detai_core` рассматривается как legacy текущего core-контура, а не как место для новых runtime tables проекта.
- system brand kit `det-ecosystem` не переносится в SQL.
- system templates и caption defaults не переносятся в SQL.
- product outputs и publication artifacts не являются частью этого SQL runbook.

## Следующая итерация

После применения этого контура следующий этап делается в репозитории `psychology-in-quotes`:

- заменить чтение `user-access.json`, `channel-bindings.json`, `moderation.json` на SQL;
- заменить runtime updates этих данных на прямую запись в SQL;
- зафиксировать database access layer и runtime ownership модели.
