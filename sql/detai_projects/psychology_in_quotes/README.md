# psychology_in_quotes schema

`sql/detai_projects/psychology_in_quotes/` хранит SQL-контур project schema
`psychology_in_quotes` внутри database `detai_projects`.

## Цель текущей итерации

Первая итерация этого контура — **infra-only migration layer**.

Она покрывает:

- создание schema `psychology_in_quotes`;
- создание runtime tables, индексов и ограничений;
- initial SQL seed на базе текущего snapshot из
  `DETai-org/psychology-in-quotes/apps/telegram-bot/runtime-db-seed/`.

Она пока не покрывает:

- переписывание Telegram-бота на прямую работу с PostgreSQL;
- runtime repository/service layer внутри проекта `psychology-in-quotes`;
- product output layout внутри `docs/publications/quotes/`.

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

В этом репозитории зафиксирован SQL seed snapshot, собранный из текущих файлов:

- `config/user-access.json`
- `config/channel-bindings.json`
- `config/moderation.json`

`access-control.json` в эту итерацию не переносится в SQL и не считается primary source.

## Состав каталога

- `migrations/0001_psychology_in_quotes_runtime.sql` — создаёт schema, функции, таблицы и индексы.
- `seeds/0001_psychology_in_quotes_initial_seed.sql` — initial import текущего snapshot.
- `apply_migrations.sh` — накатывает migrations на database `detai_projects`.

Database bootstrap находится уровнем выше, потому что относится ко всей database:

- `sql/detai_projects/bootstrap/0000_create_database.sql`
- `sql/detai_projects/bootstrap/create_database.sh`
- `sql/detai_projects/apply_all_migrations.sh`

## Порядок применения на сервере

### 1. Создать database

```bash
cd /srv/Knowledge_substrate/sql/detai_projects
bash bootstrap/create_database.sh
```

### 2. Накатить migrations schema

```bash
cd /srv/Knowledge_substrate/sql/detai_projects/psychology_in_quotes
bash apply_migrations.sh
```

Если нужно накатить все project schemas database целиком, используется root-level
entrypoint:

```bash
cd /srv/Knowledge_substrate/sql/detai_projects
bash apply_all_migrations.sh
```

### 3. Загрузить initial seed

```bash
sudo -u postgres psql -d detai_projects -v ON_ERROR_STOP=1 -f /srv/Knowledge_substrate/sql/detai_projects/psychology_in_quotes/seeds/0001_psychology_in_quotes_initial_seed.sql
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

## Важные ограничения

- `detai_core` не трогаем и не используем для новых project runtime данных.
- system brand kit `det-ecosystem` не переносится в SQL.
- system templates и caption defaults не переносятся в SQL.
- product outputs и publication artifacts не являются частью этого SQL runbook.
