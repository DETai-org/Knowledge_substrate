BEGIN;

ALTER TABLE knowledge.embeddings
  DROP CONSTRAINT IF EXISTS embeddings_doc_id_fkey,
  DROP CONSTRAINT IF EXISTS embeddings_pkey;

ALTER TABLE knowledge.embeddings
  ALTER COLUMN doc_id TYPE TEXT USING doc_id::text;

DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1
    FROM pg_constraint
    WHERE conrelid = 'knowledge.embeddings'::regclass
      AND conname = 'embeddings_doc_id_type_model_unique'
  ) THEN
    ALTER TABLE knowledge.embeddings
      ADD CONSTRAINT embeddings_doc_id_type_model_unique UNIQUE (doc_id, doc_type, model);
  END IF;
END $$;

COMMIT;

INSERT INTO infra.schema_migrations (version)
VALUES ('0004_embeddings_text_id')
ON CONFLICT (version) DO NOTHING;
