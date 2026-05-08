-- Канонические диагностические KPI для полноты embeddings и устойчивости graph API.

-- 1) Корректный расчёт количества уникальных документов в рёбрах (doc_type='post').
WITH edge_docs AS (
  SELECT e.source_id AS doc_id
  FROM knowledge.similarity_edges e
  WHERE e.doc_type = 'post'
  UNION
  SELECT e.target_id AS doc_id
  FROM knowledge.similarity_edges e
  WHERE e.doc_type = 'post'
)
SELECT COUNT(*) AS distinct_edge_docs
FROM edge_docs;

-- 2) Полнота embeddings для постов.
WITH canonical_posts AS (
  SELECT dm.doc_id
  FROM knowledge.doc_metadata dm
  WHERE dm.doc_type = 'post'
),
posts_with_embedding AS (
  SELECT DISTINCT emb.doc_id
  FROM knowledge.embeddings emb
  WHERE emb.doc_type = 'post'
),
embedding_duplicates AS (
  SELECT emb.doc_id
  FROM knowledge.embeddings emb
  WHERE emb.doc_type = 'post'
  GROUP BY emb.doc_id
  HAVING COUNT(*) > 1
)
SELECT
  (SELECT COUNT(*) FROM canonical_posts) AS posts_total,
  (SELECT COUNT(*) FROM posts_with_embedding) AS posts_with_embedding,
  (
    SELECT COUNT(*)
    FROM canonical_posts cp
    LEFT JOIN posts_with_embedding pwe ON pwe.doc_id = cp.doc_id
    WHERE pwe.doc_id IS NULL
  ) AS posts_missing_embedding,
  (SELECT COUNT(*) FROM embedding_duplicates) AS embedding_duplicates;

-- 3) Полнота metadata для endpoint-ов графа (doc_type='post').
WITH edge_docs AS (
  SELECT e.source_id AS doc_id
  FROM knowledge.similarity_edges e
  WHERE e.doc_type = 'post'
  UNION
  SELECT e.target_id AS doc_id
  FROM knowledge.similarity_edges e
  WHERE e.doc_type = 'post'
)
SELECT COUNT(*) AS edge_docs_missing_metadata
FROM edge_docs ed
LEFT JOIN knowledge.doc_metadata dm ON dm.doc_id = ed.doc_id
WHERE dm.doc_id IS NULL;

-- 4) Доля endpoint-ов без metadata (для критерия стабильности global графа).
WITH edge_docs AS (
  SELECT e.source_id AS doc_id
  FROM knowledge.similarity_edges e
  WHERE e.doc_type = 'post'
  UNION
  SELECT e.target_id AS doc_id
  FROM knowledge.similarity_edges e
  WHERE e.doc_type = 'post'
),
edge_docs_quality AS (
  SELECT
    COUNT(*) AS edge_docs_total,
    COUNT(*) FILTER (WHERE dm.doc_id IS NULL) AS edge_docs_missing_metadata
  FROM edge_docs ed
  LEFT JOIN knowledge.doc_metadata dm ON dm.doc_id = ed.doc_id
)
SELECT
  edge_docs_total,
  edge_docs_missing_metadata,
  CASE
    WHEN edge_docs_total = 0 THEN 0
    ELSE ROUND(edge_docs_missing_metadata::numeric / edge_docs_total, 6)
  END AS edge_docs_missing_metadata_ratio
FROM edge_docs_quality;
