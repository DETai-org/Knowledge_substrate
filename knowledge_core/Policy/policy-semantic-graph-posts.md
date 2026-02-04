# Policy: Semantic Graph for Posts
Данная политика относится **только** к построению семантического графа для документов типа `post` со статусом `publish`.

---
## Rules

1. В граф включаются документы:

   * `type = post`
   * `status = publish`.

2. Для построения графа используются **только document-level embeddings**
   (chunk embeddings в этом контексте не применяются).
