BEGIN;

CREATE SCHEMA IF NOT EXISTS intake;

CREATE TABLE IF NOT EXISTS public.schema_migrations (
  id BIGSERIAL PRIMARY KEY,
  version TEXT NOT NULL UNIQUE,
  applied_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  applied_by TEXT NOT NULL DEFAULT current_user
);

CREATE OR REPLACE FUNCTION intake.set_updated_at()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
  NEW.updated_at := now();
  RETURN NEW;
END;
$$;

CREATE TABLE IF NOT EXISTS intake.submissions (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT,
  kind TEXT NOT NULL CHECK (
    kind IN (
      'therapy_request',
      'education_interest',
      'event_registration',
      'section_participation',
      'team_application',
      'partner_request',
      'feedback'
    )
  ),
  source_channel TEXT NOT NULL CHECK (source_channel IN ('website', 'telegram', 'account', 'admin', 'import')),
  source_app TEXT NOT NULL,
  source_surface TEXT NOT NULL,
  target_key TEXT,
  locale TEXT NOT NULL DEFAULT 'ru' CHECK (locale IN ('ru', 'en', 'es', 'fr', 'de')),
  status TEXT NOT NULL DEFAULT 'new' CHECK (
    status IN ('new', 'in_review', 'contacted', 'closed', 'spam', 'archived')
  ),
  payload_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  contact_snapshot JSONB NOT NULL DEFAULT '{}'::jsonb,
  consent JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT submissions_contact_snapshot_object CHECK (jsonb_typeof(contact_snapshot) = 'object'),
  CONSTRAINT submissions_payload_json_object CHECK (jsonb_typeof(payload_json) = 'object'),
  CONSTRAINT submissions_consent_object CHECK (jsonb_typeof(consent) = 'object')
);

CREATE TABLE IF NOT EXISTS intake.therapy_requests (
  id BIGSERIAL PRIMARY KEY,
  submission_id BIGINT NOT NULL UNIQUE REFERENCES intake.submissions (id) ON DELETE CASCADE,
  therapy_direction TEXT NOT NULL CHECK (therapy_direction IN ('individual', 'group', 'not_sure')),
  request_context TEXT NOT NULL,
  previous_therapy_experience TEXT CHECK (
    previous_therapy_experience IN ('yes', 'no', 'prefer_not_to_answer')
  ),
  preferred_contact TEXT CHECK (preferred_contact IN ('email', 'telegram', 'either')),
  contact_comment TEXT,
  request_status TEXT NOT NULL DEFAULT 'new' CHECK (
    request_status IN ('new', 'in_review', 'contacted', 'closed', 'spam', 'archived')
  ),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS intake.processing_notes (
  id BIGSERIAL PRIMARY KEY,
  submission_id BIGINT NOT NULL REFERENCES intake.submissions (id) ON DELETE CASCADE,
  actor_user_id BIGINT,
  actor_source TEXT NOT NULL DEFAULT 'admin-bot',
  note_text TEXT NOT NULL,
  visibility TEXT NOT NULL DEFAULT 'internal' CHECK (visibility IN ('internal', 'submitter_visible')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS submissions_kind_status_created_at_idx
  ON intake.submissions (kind, status, created_at DESC);

CREATE INDEX IF NOT EXISTS submissions_source_idx
  ON intake.submissions (source_channel, source_app, source_surface);

CREATE INDEX IF NOT EXISTS submissions_target_key_idx
  ON intake.submissions (target_key);

CREATE INDEX IF NOT EXISTS submissions_contact_snapshot_gin_idx
  ON intake.submissions USING GIN (contact_snapshot);

CREATE INDEX IF NOT EXISTS therapy_requests_request_status_created_at_idx
  ON intake.therapy_requests (request_status, created_at DESC);

CREATE INDEX IF NOT EXISTS processing_notes_submission_id_created_at_idx
  ON intake.processing_notes (submission_id, created_at DESC);

DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'ecosystem_runtime_api') THEN
    GRANT USAGE ON SCHEMA intake TO ecosystem_runtime_api;
    GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA intake TO ecosystem_runtime_api;
    GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA intake TO ecosystem_runtime_api;
    ALTER DEFAULT PRIVILEGES IN SCHEMA intake
      GRANT SELECT, INSERT, UPDATE ON TABLES TO ecosystem_runtime_api;
    ALTER DEFAULT PRIVILEGES IN SCHEMA intake
      GRANT USAGE, SELECT ON SEQUENCES TO ecosystem_runtime_api;
  END IF;
END;
$$;

DROP TRIGGER IF EXISTS submissions_set_updated_at ON intake.submissions;
CREATE TRIGGER submissions_set_updated_at
BEFORE UPDATE ON intake.submissions
FOR EACH ROW
EXECUTE FUNCTION intake.set_updated_at();

DROP TRIGGER IF EXISTS therapy_requests_set_updated_at ON intake.therapy_requests;
CREATE TRIGGER therapy_requests_set_updated_at
BEFORE UPDATE ON intake.therapy_requests
FOR EACH ROW
EXECUTE FUNCTION intake.set_updated_at();

COMMIT;

INSERT INTO public.schema_migrations (version)
VALUES ('0001_intake_runtime')
ON CONFLICT (version) DO NOTHING;
