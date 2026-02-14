# RUNBOOK: DETai Core API (Single Source of Truth)

## PROD truth

- API запускается через systemd unit: `detai-core-api.service`.
- `host`: `127.0.0.1`
- `port`: `9000`
- `ExecStart`: `uvicorn app.main:app --host 127.0.0.1 --port 9000`
- Переменные окружения берутся из `/srv/Knowledge_substrate/detai-core/.env` (или эквивалентного env-файла systemd).

## 1) Как проверить, что API жив

```bash
systemctl status detai-core-api.service --no-pager
curl -sS -i http://127.0.0.1:9000/health
```

## 2) Как посмотреть доступные эндпоинты

```bash
curl -sS http://127.0.0.1:9000/openapi.json
```

## 3) Как проверить Graph API

```bash
curl -sS -i "http://127.0.0.1:9000/v1/graph?channels=detai_site_blog&limit_nodes=50"
curl -sS -i "http://127.0.0.1:9000/v1/graph?channels=detai_site_blog&limit_nodes=50&edge_scope=global"
```

Ожидаемый контракт ответа: `nodes`, `edges`, `meta`; при `edge_scope=global` возвращаются рёбра, где хотя бы один конец в отфильтрованных узлах, и API догружает недостающие узлы для целостности графа.

## 4) Как перезапустить и диагностировать

```bash
systemctl restart detai-core-api.service
journalctl -u detai-core-api.service -n 200 --no-pager
```

## 5) Как ingest влияет на API

- `metadata_ingest` обновляет метаданные публикаций в БД.
- `graph_builder` пересчитывает графовые связи и сохраняет их в БД.
- API читает подготовленные данные из БД и отдает результат через `/v1/graph`.

## 6) Быстрая проверка фильтров в журнале

```bash
journalctl -u detai-core-api.service -n 300 --no-pager | grep -E "graph_filters_normalized|graph_filter_stats"
```

В логах проверяйте, что пришли ожидаемые `limit_nodes`, `channels_count/channels_head` и факт применения фильтров на стороне сервера.
