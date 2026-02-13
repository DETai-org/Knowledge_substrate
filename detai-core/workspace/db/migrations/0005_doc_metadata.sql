BEGIN;

CREATE TABLE IF NOT EXISTS knowledge.doc_metadata (
  doc_id         TEXT PRIMARY KEY,
  date_ymd       DATE,
  year           INTEGER GENERATED ALWAYS AS (
    CASE
      WHEN date_ymd IS NULL THEN NULL
      ELSE EXTRACT(YEAR FROM date_ymd)::INTEGER
    END
  ) STORED,
  channels       TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
  authors        TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
  rubric_ids     TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
  category_ids   TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
  doc_type       TEXT NOT NULL DEFAULT 'post',
  updated_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  meta           JSONB NOT NULL DEFAULT '{}'::JSONB
);

COMMENT ON TABLE knowledge.doc_metadata IS
'Canonical metadata для semantic graph API v1. PK doc_id = administrative.id (SoT).';

COMMENT ON COLUMN knowledge.doc_metadata.doc_id IS
'Canonical SoT id (administrative.id). Не использовать knowledge.documents.id как canonical id.';

COMMIT;

INSERT INTO product.schema_migrations (version)
VALUES ('0005_doc_metadata')
ON CONFLICT (version) DO NOTHING;
