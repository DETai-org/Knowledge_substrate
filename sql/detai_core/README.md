# detai_core

`sql/detai_core/` хранит реализацию canonical/query SQL-контура экосистемы DET / DETai.

## Как читать структуру

`detai_core` — это одна database с фиксированным набором schema-ролей:

- `infra`
- `ecosystem`
- `publications`

Поэтому layout этого каталога делится на два типа:

- root-level database assets;
- schema-specific folders.

### Root-level database assets

Здесь живут вещи, которые относятся ко всей database, а не к одной schema:

- `bootstrap/`
- `api/`
- `tests/`
- `apply_migrations.sh`
- `docker-compose.yml`
- `Makefile`
- `requirements.txt`
- `analysis_exports/`

### Schema-specific folders

- `infra/` — нейтральный технический schema-layer.
- `ecosystem/` — schema-layer для будущих ecosystem SQL-представлений.
- `publications/` — schema-layer для текущих canonical/query SQL-представлений публикационного домена.

Служебный журнал миграций относится к техслою `infra`, а не к доменной модели
`ecosystem` или `publications`.

## Кто что накатывает

### Database-level entrypoints

- `bootstrap/` — создаёт саму database `detai_core` на PostgreSQL server.
- `apply_migrations.sh` — накатывает весь schema-contour database `detai_core`
  в правильном порядке: `infra -> ecosystem -> publications`.
- `Makefile bootstrap` — это только developer bootstrap Python-зависимостей, а не
  database bootstrap.

### Schema-level folders

- `infra/` — хранит только technical schema migrations.
- `ecosystem/` — хранит только ecosystem schema migrations.
- `publications/` — хранит только publications schema migrations и diagnostics.

Иными словами:

- root-level entrypoints управляют всей database;
- schema folders описывают только свой собственный SQL layer.

## Принцип layout

Папка внутри `sql/detai_core/` должна означать либо:

- конкретную PostgreSQL schema;
- либо database-wide asset, который не принадлежит одной schema.

Абстрактные технические контейнеры вроде `workspace/db/` здесь больше не используются
для schema-specific SQL.

## Канонический runbook (PROD): systemd + 127.0.0.1:9000

### 0. Bootstrap и schema migrations

```bash
cd /srv/Knowledge_substrate/sql/detai_core
bash bootstrap/create_database.sh
bash apply_migrations.sh
```

### 1. Проверка, что API жив

```bash
systemctl status detai-core-api.service --no-pager
curl -sS -i http://127.0.0.1:9000/health
```

### 2. Проверка доступных эндпоинтов (OpenAPI)

```bash
curl -sS http://127.0.0.1:9000/openapi.json
```

### 3. Проверка Graph API

```bash
curl -sS -i "http://127.0.0.1:9000/v1/graph?channels=detai_site_blog&limit_nodes=50"
curl -sS -i "http://127.0.0.1:9000/v1/graph?channels=detai_site_blog&limit_nodes=50&edge_scope=global"
```

### 4. Перезапуск и диагностика

```bash
systemctl restart detai-core-api.service
journalctl -u detai-core-api.service -n 200 --no-pager
```

### 5. Как ingest влияет на API

- `knowledge_core/ingest_pipeline/metadata/metadata_ingest.py` обновляет метаданные в БД.
- `knowledge_core/ingest_pipeline/graph_builder/pipeline.py` пересобирает графовые связи в БД.
- API (`sql/detai_core/api`) читает граф и метаданные из БД и отдает их через `/v1/graph`.

### 6. KPI-валидация пайплайна перед PROD

Канонический набор диагностик находится в:

- `publications/diagnostics/graph_embedding_kpi.sql`

```bash
cd sql/detai_core
psql "$DATABASE_URL" -f publications/diagnostics/graph_embedding_kpi.sql
```

## Локальный запуск

```bash
cd sql/detai_core
python -m pip install -r requirements.txt
```

```bash
cd sql/detai_core
export DATABASE_URL=postgresql://detai:detai@localhost:5432/detai
export API_CORS_ORIGINS=http://localhost:3000,http://localhost:5173
make api
```
