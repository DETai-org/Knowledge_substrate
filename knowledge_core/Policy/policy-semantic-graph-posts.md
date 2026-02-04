Policy: Semantic Graph for Posts
Scope

Данная политика относится только к построению семантического графа для документов типа post со статусом publish.

Rules

В граф включаются только документы:

type = post

status = publish.

Для построения графа используются только document-level embeddings
(chunk embeddings в этом контексте не применяются).
