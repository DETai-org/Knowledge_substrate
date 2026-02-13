# Guide: Semantic Graph API v1

## Исходный sub-issue
- [Sub-Issue 2: Semantic Graph API (v1) & API Service Hardening](../../issue/2-sub-issue-semantic-graph-api.md)

## Что делает endpoint
`GET /v1/graph` возвращает semantic graph в формате:
- `nodes`
- `edges`
- `meta`

Целевой сценарий: выдача publish-графа для клиентов/фронта с детерминированным контрактом.


## Каноничный ingest → API mapping для metadata

Источник metadata: `knowledge.doc_metadata`.

- `doc_metadata.doc_id` → `nodes[].id`
- `doc_metadata.doc_type` → `nodes[].type`
- `doc_metadata.year` (или `date_ymd`) → `nodes[].year`
- `doc_metadata.channels` → `nodes[].channels`
- `doc_metadata.authors` → `nodes[].authors`
- `doc_metadata.rubric_ids` → `nodes[].rubric_ids`
- `doc_metadata.category_ids` → `nodes[].category_ids`
- `doc_metadata.meta` → `nodes[].meta`

Важно: `knowledge.documents.id` не участвует в этом mapping и не используется как canonical id semantic graph.

## Query-параметры
- `channels` — повторяемый query-параметр
- `year_from`, `year_to`
- `rubric_ids`, `category_ids`
- `authors`
- `limit_nodes` — ограничение размера выдачи (в v1: `default=200`, `max=1000`)

## Структура ответа
- `nodes`: `[{ id, type, label, year, channels, rubric_ids, category_ids, authors, meta }]`
- `edges`: `[{ source, target, type, weight, meta }]`
- `meta`: `{"filters_applied": ..., "total_nodes": ..., "total_edges": ..., "truncated": bool}`

### JSON-структура `meta.filters_applied`
```json
{
  "channels": ["string"],
  "years": {"from": 2023, "to": 2024},
  "authors": ["string"],
  "rubric_ids": ["string"],
  "category_ids": ["string"],
  "limit_nodes": 200
}
```

## Как интерпретировать `truncated`
- `truncated=false`: данные уместились в лимит.
- `truncated=true`: граф урезан до `limit_nodes`; рёбра возвращаются только между отданными узлами.

## Коды ответов
- `200 OK` — валидный ответ, включая пустой результат.
- `400 Bad Request` — синтаксически некорректный query.
- `422 Unprocessable Entity` — семантически невалидные параметры (например, `year_from > year_to`).
- `500 Internal Server Error` — непредвиденная ошибка исполнения.

## Практические примеры

### Пример A (частичные фильтры, без truncation)

```http
GET /v1/graph?channels=telegram&year_from=2023&year_to=2024&limit_nodes=3
```

```json
{
  "nodes": [
    {
      "id": "post-2024-001",
      "type": "publish-post",
      "label": "DET weekly update",
      "year": 2024,
      "channels": ["telegram"],
      "rubric_ids": ["det-updates"],
      "category_ids": ["ecosystem"],
      "authors": ["team-det"],
      "meta": {"doc_type": "post"}
    }
  ],
  "edges": [],
  "meta": {
    "filters_applied": {
      "channels": ["telegram"],
      "years": {"from": 2023, "to": 2024},
      "authors": [],
      "rubric_ids": [],
      "category_ids": [],
      "limit_nodes": 3
    },
    "total_nodes": 1,
    "total_edges": 0,
    "truncated": false
  }
}
```

### Пример B (`truncated=true` и дедупликация неориентированного ребра)

```http
GET /v1/graph?channels=site&limit_nodes=2
```

```json
{
  "nodes": [
    {"id": "post-a", "type": "publish-post", "label": "post-a", "year": null, "channels": ["site"], "rubric_ids": [], "category_ids": [], "authors": [], "meta": {}},
    {"id": "post-b", "type": "publish-post", "label": "post-b", "year": 2024, "channels": ["site"], "rubric_ids": ["core"], "category_ids": [], "authors": ["editor"], "meta": {}}
  ],
  "edges": [
    {"source": "post-a", "target": "post-b", "type": "SIMILAR_UNDIRECTED", "weight": 0.93, "meta": {"deduplicated": true}}
  ],
  "meta": {
    "filters_applied": {
      "channels": ["site"],
      "years": {"from": null, "to": null},
      "authors": [],
      "rubric_ids": [],
      "category_ids": [],
      "limit_nodes": 2
    },
    "total_nodes": 2,
    "total_edges": 1,
    "truncated": true
  }
}
```

## Локальный запуск
- Команды запуска и окружение берите из актуального README/Makefile API-сервиса (в рамках реализации sub-issue).
- Не вводите новые Make targets вне согласованного списка.
- Для debug-диагностики используйте debug-режим (`--debug`), а строгие правила по раскрытию ошибок см. в policy:
  - [Semantic Graph API v1 — Policy](../Policy/semantic-graph-api-v1.policy.md)
