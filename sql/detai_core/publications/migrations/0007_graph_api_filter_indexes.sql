BEGIN;

CREATE INDEX IF NOT EXISTS doc_metadata_year_idx
  ON publications.doc_metadata (year);

CREATE INDEX IF NOT EXISTS doc_metadata_date_ymd_idx
  ON publications.doc_metadata (date_ymd);

CREATE INDEX IF NOT EXISTS doc_metadata_channels_gin_idx
  ON publications.doc_metadata USING GIN (channels);

CREATE INDEX IF NOT EXISTS doc_metadata_authors_gin_idx
  ON publications.doc_metadata USING GIN (authors);

CREATE INDEX IF NOT EXISTS doc_metadata_rubric_ids_gin_idx
  ON publications.doc_metadata USING GIN (rubric_ids);

CREATE INDEX IF NOT EXISTS doc_metadata_category_ids_gin_idx
  ON publications.doc_metadata USING GIN (category_ids);

COMMIT;

INSERT INTO infra.schema_migrations (version)
VALUES ('0006_graph_api_filter_indexes')
ON CONFLICT (version) DO NOTHING;
