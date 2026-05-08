BEGIN;

DO $$
BEGIN
  IF EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'product'
      AND table_name = 'schema_migrations'
  ) THEN
    DROP TRIGGER IF EXISTS sync_schema_migrations_to_infra
      ON product.schema_migrations;
  END IF;

  IF EXISTS (
    SELECT 1
    FROM information_schema.tables
    WHERE table_schema = 'infra'
      AND table_name = 'schema_migrations'
  ) THEN
    DROP TRIGGER IF EXISTS sync_schema_migrations_to_product
      ON infra.schema_migrations;
  END IF;
END $$;

DO $$
BEGIN
  IF EXISTS (
    SELECT 1 FROM pg_proc p
    JOIN pg_namespace n ON n.oid = p.pronamespace
    WHERE n.nspname = 'infra'
      AND p.proname = 'sync_schema_migrations_to_infra'
  ) THEN
    DROP FUNCTION infra.sync_schema_migrations_to_infra();
  END IF;
  IF EXISTS (
    SELECT 1 FROM pg_proc p
    JOIN pg_namespace n ON n.oid = p.pronamespace
    WHERE n.nspname = 'infra'
      AND p.proname = 'sync_schema_migrations_to_product'
  ) THEN
    DROP FUNCTION infra.sync_schema_migrations_to_product();
  END IF;
END $$;

DROP TABLE IF EXISTS product.schema_migrations;
DROP TABLE IF EXISTS product.job_runs;
DROP SCHEMA IF EXISTS product;

COMMIT;

INSERT INTO infra.schema_migrations (version)
VALUES ('0008_product_schema_migrations_compat')
ON CONFLICT (version) DO NOTHING;
