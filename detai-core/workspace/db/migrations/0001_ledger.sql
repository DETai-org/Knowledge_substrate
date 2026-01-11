BEGIN;

CREATE SCHEMA IF NOT EXISTS knowledge;
CREATE SCHEMA IF NOT EXISTS product;

CREATE TABLE IF NOT EXISTS product.schema_migrations (
  id         BIGSERIAL PRIMARY KEY,
  version    TEXT NOT NULL UNIQUE,
  applied_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  applied_by TEXT NOT NULL DEFAULT current_user
);

CREATE TABLE IF NOT EXISTS product.job_runs (
  id           BIGSERIAL PRIMARY KEY,
  job_name     TEXT NOT NULL,
  run_id       TEXT,
  status       TEXT NOT NULL CHECK (status IN ('started','success','failed')),
  started_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
  finished_at  TIMESTAMPTZ,
  input_count  INT,
  output_count INT,
  error_text   TEXT,
  meta         JSONB NOT NULL DEFAULT '{}'::jsonb
);

COMMIT;

INSERT INTO product.schema_migrations (version)
VALUES ('0001_ledger')
ON CONFLICT (version) DO NOTHING;
