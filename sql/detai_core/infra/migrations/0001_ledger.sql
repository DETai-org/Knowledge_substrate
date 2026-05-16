BEGIN;

CREATE SCHEMA IF NOT EXISTS infra;
CREATE SCHEMA IF NOT EXISTS ecosystem;

CREATE TABLE IF NOT EXISTS infra.schema_migrations (
  id         BIGSERIAL PRIMARY KEY,
  version    TEXT NOT NULL UNIQUE,
  applied_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  applied_by TEXT NOT NULL DEFAULT current_user
);

COMMIT;

INSERT INTO infra.schema_migrations (version)
VALUES ('0001_ledger')
ON CONFLICT (version) DO NOTHING;
