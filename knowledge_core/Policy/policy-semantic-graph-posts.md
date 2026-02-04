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

## Связанные документы
- [Guide: Semantic Graph Posts](../guides/guide-semantic-graph-posts.md)
- [ADR-0001: Semantic Similarity Graph for Posts](../ADR/adr-0001-semantic-similarity-graph-posts.md)
