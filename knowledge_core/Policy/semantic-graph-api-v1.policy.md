# Policy: Semantic Graph API v1

## Исходный sub-issue
- [Sub-Issue 2: Semantic Graph API (v1) & API Service Hardening](../../issue/2-sub-issue-semantic-graph-api.md)

## Назначение и область действия (только v1)
Этот документ фиксирует **обязательные инварианты (MUST / MUST NOT)** для API-контракта `GET /v1/graph` и стыка ingest ↔ API в версии `v1`.

## Инварианты (MUST / MUST NOT)

1. **Источник фильтров (MUST)**
   - Фильтры `channels / years / authors / rubrics / categories` MUST вычисляться только из `knowledge.doc_metadata`.

2. **Запрет альтернативного SoT для фильтров (MUST NOT)**
   - `knowledge.documents.meta` MUST NOT использоваться как источник истины для фильтрации в `v1`.

3. **Каноничное join-правило (MUST)**
   - `knowledge.similarity_edges.source_id` и `knowledge.similarity_edges.target_id` MUST join'иться с `knowledge.doc_metadata.doc_id`.

4. **Правило metadata-gap (MUST)**
   - Если у ребра отсутствует одна или обе metadata-ноды, это ребро MUST NOT попадать в ответ API.
   - Такой случай MUST логироваться как `data_gap`.

5. **Fallback при неполной metadata (MUST)**
   - Если `label` отсутствует, API MUST вернуть `label = id`.
   - Если массивные поля отсутствуют (`channels`, `authors`, `rubric_ids`, `category_ids`), API MUST вернуть пустые массивы.
   - Если `year` отсутствует, API MUST вернуть `year = null`.

6. **Политика edge-дедупликации (MUST)**
   - Для `SIMILAR_UNDIRECTED` пара MUST нормализоваться как `min(source,target)|max(source,target)`.
   - Для одной нормализованной пары MUST возвращаться одно ребро с максимальным `weight`.
   - Для направленных рёбер (`type != SIMILAR_UNDIRECTED`) схлопывание MUST NOT применяться.

7. **Политика раскрытия ошибок (MUST / MUST NOT)**
   - Stacktrace MUST NOT возвращаться пользователю по умолчанию.
   - Stacktrace MAY быть доступен только в debug-режиме (например, при `--debug`) для локальной диагностики.

## Правила наблюдаемости
Для запроса `/v1/graph` в structured logs MUST присутствовать как минимум:
- `request_id`
- `path`
- `status_code`
- `duration_ms`
- `total_nodes`
- `total_edges`
- `truncated`
- при data-gap: событие/признак `data_gap`.

## Связанный guide
- [Semantic Graph API v1 — Guide](../guides/semantic-graph-api-v1.guide.md)
