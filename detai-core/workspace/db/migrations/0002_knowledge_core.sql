BEGIN;

-- documents
CREATE TABLE IF NOT EXISTS knowledge.documents (
  id          BIGSERIAL PRIMARY KEY,
  zone        TEXT NOT NULL CHECK (zone IN ('public','team','private')),
  source      TEXT,
  title       TEXT,
  content     TEXT NOT NULL,
  meta        JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- full-text search
ALTER TABLE knowledge.documents
  ADD COLUMN IF NOT EXISTS fts tsvector
  GENERATED ALWAYS AS (
    to_tsvector('simple', coalesce(title,'') || ' ' || coalesce(content,''))
  ) STORED;

CREATE INDEX IF NOT EXISTS documents_fts_idx ON knowledge.documents USING GIN (fts);
CREATE INDEX IF NOT EXISTS documents_zone_idx ON knowledge.documents (zone);

-- links (graph edges)
CREATE TABLE IF NOT EXISTS knowledge.links (
  id            BIGSERIAL PRIMARY KEY,
  from_id       BIGINT NOT NULL REFERENCES knowledge.documents(id) ON DELETE CASCADE,
  to_id         BIGINT NOT NULL REFERENCES knowledge.documents(id) ON DELETE CASCADE,
  relation      TEXT NOT NULL CHECK (relation IN (
                 'part_of','explains','implements','supports','contradicts','relates_to'
               )),
  weight        REAL NOT NULL DEFAULT 1.0,
  evidence      TEXT,
  meta          JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS links_from_idx ON knowledge.links (from_id);
CREATE INDEX IF NOT EXISTS links_to_idx   ON knowledge.links (to_id);
CREATE INDEX IF NOT EXISTS links_rel_idx  ON knowledge.links (relation);

-- embeddings
-- dims фиксируем 1536 как стартовый стандарт (потом миграцией поменяем, если нужно)
CREATE TABLE IF NOT EXISTS knowledge.embeddings (
  doc_id     BIGINT PRIMARY KEY REFERENCES knowledge.documents(id) ON DELETE CASCADE,
  model      TEXT NOT NULL,
  dims       INT  NOT NULL DEFAULT 1536,
  embedding  vector(1536) NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

COMMIT;

INSERT INTO product.schema_migrations (version)
VALUES ('0002_knowledge_core')
ON CONFLICT (version) DO NOTHING;
