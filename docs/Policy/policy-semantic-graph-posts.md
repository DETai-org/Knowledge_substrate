# Policy: Semantic Graph for Posts
Данная политика относится **только** к построению семантического графа для документов типа `post` со статусом `publish`.

---
## Rules

1. В граф включаются документы:

   * `type = post`
   * `status = publish`.

2. Для построения графа используются **только document-level embeddings**
   (chunk embeddings в этом контексте не применяются).

---

## Политика построения семантического графа
Графовые связи — производные данные, которые строятся ingestion‑пайплайном и
управляются параметрами в [config.json](../ingest_pipeline/config.json).

Базовая стратегия:
- **Top‑K per document** (берём K ближайших соседей для каждого документа);
- **порог min_similarity** отбрасывает шумовые связи;
- граф undirected: рёбра нормализуются как `(min(idA, idB), max(idA, idB))`.

Поведение при обновлениях:
- embeddings пересчитываются только при изменении `source_hash`;
- edges пересобираются для затронутых документов;
- допускается полный пересчёт графа как fallback (например, параметром запуска).

Начальные значения по умолчанию:
- `graph.top_k = 8`
- `graph.min_similarity = 0.75`

---

## Связанные документы
- Guide: [Semantic Similarity Graph for Posts](../guides/guide-semantic-graph-posts.md)
- ADR: [ADR-0001: Semantic Similarity Graph for Posts](../ADR/adr-0001-semantic-similarity-graph-posts.md)
