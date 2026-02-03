# Guide: Semantic Similarity Graph for Posts (Publish Only)

## Purpose
Собрать и визуализировать граф смысловой близости опубликованных постов DET / DETai:
- nodes = post documents
- edges = semantic similarity links (взвешенные)
- weight = cosine similarity (0..1)

Цель графа: обнаружение смысловых кластеров и опорных узлов для формулирования постулатов DET.

---

## Scope
- Document type: `post`
- Status: `publish` only
- Channels: допускается фильтрация по channels (например detai_site_blog/personal_site_blog), но базовый граф может быть общий.

---

## Data Inputs (SoT)
Источник истины: Markdown + frontmatter постов в SoT.

Минимально используемые поля:
- administrative.id (string) — ключ документа
- administrative.status (publish)
- administrative.channels (list)
- administrative.date_ymd (date)
- administrative.authors (list)
- descriptive.title (string)
- descriptive.preview (string, optional for embedding)
- body markdown (основной текст)

---

## Embeddings Strategy
### What we compute now
- **Document embedding**: 1 embedding per post document.
- Text payload for embedding (рекомендуемо):
  - `title + "\n\n" + body_markdown_stripped`
  - preview можно добавить, но лучше не дублировать смысл, если preview повторяет текст.

### What we explicitly do NOT compute in this phase
- **Chunk embeddings** (N vectors per doc) — откладываем для RAG/агентов.

Почему:
- граф "пост ↔ пост" не требует точного поиска по фрагментам,
- чанкинг и re-embedding усложняют pipeline и качество.

---

## Graph Construction
### Similarity metric
- cosine similarity между document embeddings.

### Edge selection strategy (chosen)
- **Top-K** per node:
  - для каждого поста выбираем K наиболее близких постов (исключая самого себя)
- Дополнительный фильтр:
  - применяем `min_similarity` (например 0.72–0.80) чтобы отрезать шумовые связи.

### Parameters (initial defaults)
- K = 8 (можно 5–12)
- min_similarity = 0.75 (подбирается по факту плотности графа)
- Graph is undirected:
  - если A выбрал B, а B выбрал A — одна связь, weight = max(weightAB, weightBA) или среднее.

---

## Storage (Operational Store)
Храним два слоя:

1) **Embeddings table**
- `knowledge.embeddings`
- Поля минимум:
  - doc_id
  - doc_type (=post)
  - embedding_vector
  - model
  - embedding_hash / source_hash
  - updated_at

2) **Similarity edges table** (рекомендуется отдельная)
- `knowledge.similarity_edges`
- Поля минимум:
  - source_id
  - target_id
  - doc_type (=post)
  - weight (float)
  - method (topk)
  - k (int)
  - min_similarity (float)
  - updated_at

Идемпотентность:
- уникальный ключ: (source_id, target_id, doc_type, method)
- при пересборке графа: upsert + удаление устаревших рёбер для source_id (если нужно)

---

## Update Trigger (Pipeline)
Граф должен обновляться при изменении SoT:
- вариант 1: вручную (CLI команда)
- вариант 2: по расписанию (cron / GitHub Actions)
- вариант 3: по push в SoT paths (лучше позже, когда pipeline стабилен)

Рекомендуемый порядок обновления:
1) собрать список publish-постов из SoT
2) для каждого поста вычислить source_hash (контроль изменений)
3) если hash изменился или embedding отсутствует:
   - пересчитать embedding и upsert в `knowledge.embeddings`
4) построить edges:
   - для каждого поста найти top-K ближайших (через vector index или batch similarity)
   - upsert в `knowledge.similarity_edges`
5) API начинает отдавать актуальный граф

---

## API Contract (Graph Endpoint)
Endpoint: `GET /graph`

Query params:
- channel (optional)
- year_from/year_to (optional)
- rubric/category (optional, если хотим фильтровать graph slices)
- limit_nodes (optional)

Response:
- `nodes`: [{ id, title, year, authors, channels, rubric_ids, category_ids }]
- `edges`: [{ source, target, weight }]

Важно:
- возвращаем только publish-документы
- weight используется в UI для толщины/прозрачности/силы притяжения в layout

---

## Next.js Visualization
UI задача:
- отрисовать граф на отдельной странице (например `/graph`)
- поддержать hover, click:
  - клик по node → открыть пост
  - клик по edge → показать similarity weight

Рекомендуемые библиотеки:
- Cytoscape.js (быстрый старт, много готовых layout)
- Sigma.js (хорош для больших графов)
- D3 force (гибко, но требует больше времени)

---

## Notes / Future (v0.2+)
- Chunk embeddings + RAG: поиск по фрагментам, ответы на вопросы.
- Добавление типов документов: quote, research_publication и т.д. — по мере готовности контрактов.
- Автоматическое построение тематических кластеров (community detection) и генерация "постулатов-кандидатов".
