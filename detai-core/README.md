# DETai Core API

## Локальный запуск

### Требования
- Python 3.10+
- `DATABASE_URL` (обязательно)
- `API_CORS_ORIGINS` (опционально, список origin через запятую, без `*`)

### Через Makefile

```bash
cd detai-core
export DATABASE_URL=postgresql://detai:detai@localhost:5432/detai
export API_CORS_ORIGINS=http://localhost:3000,http://localhost:5173
make api
```

Проверка:

```bash
curl http://localhost:8000/health
curl "http://localhost:8000/v1/graph?limit_nodes=5"
```

## Локальный запуск через Docker Compose

```bash
cd detai-core
docker compose up --build
```

API будет доступен на `http://localhost:8000`.

## Полезные цели Makefile

```bash
make lint
make format
```
