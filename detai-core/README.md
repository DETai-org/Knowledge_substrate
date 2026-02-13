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



## OpenAPI и пример контракта

- OpenAPI JSON: `GET /openapi.json`
- Swagger UI: `GET /docs`

Минимальный пример ответа `/v1/graph`:

```json
{
  "nodes": [
    {
      "id": "post-1",
      "type": "publish-post",
      "label": "post-1",
      "year": 2024,
      "channels": ["site"],
      "rubric_ids": ["core"],
      "category_ids": ["ecosystem"],
      "authors": ["detai"],
      "meta": {}
    }
  ],
  "edges": [
    {
      "source": "post-1",
      "target": "post-2",
      "type": "SIMILAR_UNDIRECTED",
      "weight": 0.92,
      "meta": {}
    }
  ],
  "meta": {
    "filters_applied": {
      "channels": ["site"],
      "years": {"from": 2024, "to": 2024},
      "authors": [],
      "rubric_ids": ["core"],
      "category_ids": ["ecosystem"],
      "limit_nodes": 200
    },
    "total_nodes": 1,
    "total_edges": 1,
    "truncated": false
  }
}
```

## Mock-клиент контракта

Для проверки, что контракт потребляется клиентом, добавлен mock-клиент:

```bash
python tests/mock_graph_client.py
```

Скрипт валидирует payload через `GraphResponse` и имитирует базовую проверку фронта.
