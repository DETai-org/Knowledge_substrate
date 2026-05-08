BEGIN;

CREATE SCHEMA IF NOT EXISTS infra;

CREATE TABLE IF NOT EXISTS infra.schema_migrations (
  id         BIGSERIAL PRIMARY KEY,
  version    TEXT NOT NULL UNIQUE,
  applied_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  applied_by TEXT NOT NULL DEFAULT current_user
);

DO $$
BEGIN
  IF EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'product'
      AND table_name = 'schema_migrations'
  ) THEN
    INSERT INTO infra.schema_migrations (version, applied_at, applied_by)
    SELECT version, applied_at, applied_by
    FROM product.schema_migrations
    ON CONFLICT (version) DO NOTHING;
  END IF;
END $$;

DROP TABLE IF EXISTS product.job_runs;

COMMENT ON SCHEMA infra IS
'Neutral technical schema for detai_core database infrastructure.';

COMMENT ON TABLE infra.schema_migrations IS
'Applied schema migration ledger for detai_core.';

COMMIT;

INSERT INTO infra.schema_migrations (version)
VALUES ('0007_infra_migration_ledger')
ON CONFLICT (version) DO NOTHING;
