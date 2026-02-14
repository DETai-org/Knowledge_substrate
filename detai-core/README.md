# DETai Core API

## Канонический runbook (PROD): systemd + 127.0.0.1:9000

### 1) Проверка, что API жив

```bash
systemctl status detai-core-api.service --no-pager
curl -sS -i http://127.0.0.1:9000/health
```

### 2) Проверка доступных эндпоинтов (OpenAPI)

```bash
curl -sS http://127.0.0.1:9000/openapi.json
```

### 3) Проверка Graph API

```bash
curl -sS -i "http://127.0.0.1:9000/v1/graph?channels=detai_site_blog&limit_nodes=50"
curl -sS -i "http://127.0.0.1:9000/v1/graph?channels=detai_site_blog&limit_nodes=50&edge_scope=global"
```

Ожидается HTTP 200 и контракт с полями `nodes`, `edges`, `meta`; при `edge_scope=global` возвращаются рёбра, где хотя бы один конец в отфильтрованных узлах, и API догружает недостающие узлы для целостности графа.

### 4) Перезапуск и диагностика

```bash
systemctl restart detai-core-api.service
journalctl -u detai-core-api.service -n 200 --no-pager
```

### 5) Как ingest влияет на API

- `knowledge_core/ingest_pipeline/metadata/metadata_ingest.py` обновляет метаданные в БД.
- `knowledge_core/ingest_pipeline/graph_builder/pipeline.py` пересобирает графовые связи в БД.
- API (`detai-core/api`) читает граф и метаданные из БД и отдает их через `/v1/graph`.

## Локальный запуск (опционально, не канонический)

### Требования

- Python 3.10+
- `DATABASE_URL` (обязательно)
- `API_CORS_ORIGINS` (опционально, список origin через запятую, без `*`)

### Bootstrap зависимостей (API + тесты)

```bash
cd detai-core
python -m pip install -r requirements.txt
```

### Через Makefile

```bash
cd detai-core
export DATABASE_URL=postgresql://detai:detai@localhost:5432/detai
export API_CORS_ORIGINS=http://localhost:3000,http://localhost:5173
make api
```

Проверка:

```bash
curl -sS -i http://127.0.0.1:9000/health
curl -sS -i "http://127.0.0.1:9000/v1/graph?limit_nodes=5"
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
