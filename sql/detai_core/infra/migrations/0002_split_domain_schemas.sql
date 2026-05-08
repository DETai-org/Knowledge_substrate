BEGIN;

CREATE SCHEMA IF NOT EXISTS ecosystem;

DO $$
BEGIN
  IF EXISTS (
    SELECT 1
    FROM information_schema.schemata
    WHERE schema_name = 'knowledge'
  ) THEN
    IF EXISTS (
      SELECT 1
      FROM information_schema.schemata
      WHERE schema_name = 'publications'
    ) THEN
      RAISE EXCEPTION
        'Both schemas "knowledge" and "publications" exist. Manual reconciliation is required before continuing.';
    END IF;

    EXECUTE 'ALTER SCHEMA knowledge RENAME TO publications';
  ELSIF NOT EXISTS (
    SELECT 1
    FROM information_schema.schemata
    WHERE schema_name = 'publications'
  ) THEN
    EXECUTE 'CREATE SCHEMA publications';
  END IF;
END $$;

COMMIT;

INSERT INTO infra.schema_migrations (version)
VALUES ('0002_split_domain_schemas')
ON CONFLICT (version) DO NOTHING;
