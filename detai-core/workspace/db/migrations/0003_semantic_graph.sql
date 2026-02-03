BEGIN;

CREATE TABLE IF NOT EXISTS knowledge.similarity_edges (
  source_id       TEXT NOT NULL,
  target_id       TEXT NOT NULL,
  doc_type        TEXT NOT NULL,
  weight          DOUBLE PRECISION NOT NULL,
  method          TEXT NOT NULL,
  k               INTEGER NOT NULL,
  min_similarity  DOUBLE PRECISION NOT NULL,
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT similarity_edges_direction_chk CHECK (source_id < target_id),
  CONSTRAINT similarity_edges_weight_chk CHECK (weight >= 0 AND weight <= 1),
  CONSTRAINT similarity_edges_unique UNIQUE (source_id, target_id, doc_type, method)
);

CREATE INDEX IF NOT EXISTS similarity_edges_source_idx ON knowledge.similarity_edges (source_id);
CREATE INDEX IF NOT EXISTS similarity_edges_target_idx ON knowledge.similarity_edges (target_id);
CREATE INDEX IF NOT EXISTS similarity_edges_weight_idx ON knowledge.similarity_edges (weight DESC);

ALTER TABLE knowledge.embeddings
  ADD COLUMN IF NOT EXISTS doc_type TEXT NOT NULL DEFAULT 'post',
  ADD COLUMN IF NOT EXISTS source_hash TEXT NOT NULL DEFAULT '',
  ADD COLUMN IF NOT EXISTS updated_at TIMESTAMPTZ NOT NULL DEFAULT now();

COMMIT;

INSERT INTO product.schema_migrations (version)
VALUES ('0003_semantic_graph')
ON CONFLICT (version) DO NOTHING;
