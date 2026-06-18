BEGIN;

ALTER TABLE intake.therapy_requests
  DROP CONSTRAINT IF EXISTS therapy_requests_therapy_direction_check;

ALTER TABLE intake.therapy_requests
  ADD CONSTRAINT therapy_requests_therapy_direction_check
  CHECK (therapy_direction IN ('individual', 'group', 'ai_assisted', 'not_sure'));

CREATE TABLE IF NOT EXISTS intake.section_participations (
  id BIGSERIAL PRIMARY KEY,
  submission_id BIGINT NOT NULL UNIQUE REFERENCES intake.submissions (id) ON DELETE CASCADE,
  participation_role TEXT NOT NULL CHECK (participation_role IN ('listener', 'speaker')),
  attendance_mode TEXT CHECK (attendance_mode IN ('offline', 'online', 'either')),
  professional_role TEXT,
  professional_role_other TEXT,
  listener_affiliation TEXT,
  listener_department TEXT,
  bachelor_course TEXT,
  specialist_course TEXT,
  master_course TEXT,
  postgraduate_course TEXT,
  listener_research_area TEXT,
  listener_psychotherapy_format TEXT,
  listener_psychotherapy_organization TEXT,
  listener_technical_area TEXT,
  field_of_study TEXT,
  listener_expectations TEXT,
  referral_source TEXT,
  speaker_current_status TEXT,
  speaker_status_other TEXT,
  speaker_bachelor_course TEXT,
  speaker_specialist_course TEXT,
  speaker_master_course TEXT,
  speaker_postgraduate_course TEXT,
  speaker_research_area TEXT,
  speaker_psychotherapy_format TEXT,
  speaker_psychotherapy_organization TEXT,
  speaker_technical_area TEXT,
  speaker_affiliation TEXT,
  speaker_specialization TEXT,
  talk_topic TEXT,
  talk_summary TEXT,
  speaker_background TEXT,
  section_status TEXT NOT NULL DEFAULT 'new' CHECK (
    section_status IN ('new', 'in_review', 'contacted', 'closed', 'spam', 'archived')
  ),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS section_participations_role_status_created_at_idx
  ON intake.section_participations (participation_role, section_status, created_at DESC);

CREATE INDEX IF NOT EXISTS section_participations_attendance_mode_idx
  ON intake.section_participations (attendance_mode);

CREATE INDEX IF NOT EXISTS section_participations_professional_role_idx
  ON intake.section_participations (professional_role);

DROP TRIGGER IF EXISTS section_participations_set_updated_at ON intake.section_participations;
CREATE TRIGGER section_participations_set_updated_at
BEFORE UPDATE ON intake.section_participations
FOR EACH ROW
EXECUTE FUNCTION intake.set_updated_at();

DO $$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'ecosystem_runtime_api') THEN
    GRANT SELECT, INSERT, UPDATE ON intake.section_participations TO ecosystem_runtime_api;
    GRANT USAGE, SELECT ON SEQUENCE intake.section_participations_id_seq TO ecosystem_runtime_api;
  END IF;
END;
$$;

INSERT INTO intake.section_participations (
  submission_id,
  participation_role,
  attendance_mode,
  professional_role,
  professional_role_other,
  listener_affiliation,
  listener_department,
  bachelor_course,
  specialist_course,
  master_course,
  postgraduate_course,
  listener_research_area,
  listener_psychotherapy_format,
  listener_psychotherapy_organization,
  listener_technical_area,
  field_of_study,
  listener_expectations,
  referral_source,
  speaker_current_status,
  speaker_status_other,
  speaker_bachelor_course,
  speaker_specialist_course,
  speaker_master_course,
  speaker_postgraduate_course,
  speaker_research_area,
  speaker_psychotherapy_format,
  speaker_psychotherapy_organization,
  speaker_technical_area,
  speaker_affiliation,
  speaker_specialization,
  talk_topic,
  talk_summary,
  speaker_background,
  section_status
)
SELECT
  s.id,
  COALESCE(NULLIF(s.payload_json->>'participation_role', ''), 'listener'),
  NULLIF(s.payload_json->>'attendance_mode', ''),
  NULLIF(s.payload_json->>'professional_role', ''),
  NULLIF(s.payload_json->>'professional_role_other', ''),
  NULLIF(s.payload_json->>'listener_affiliation', ''),
  NULLIF(s.payload_json->>'listener_department', ''),
  NULLIF(s.payload_json->>'bachelor_course', ''),
  NULLIF(s.payload_json->>'specialist_course', ''),
  NULLIF(s.payload_json->>'master_course', ''),
  NULLIF(s.payload_json->>'postgraduate_course', ''),
  NULLIF(s.payload_json->>'listener_research_area', ''),
  NULLIF(s.payload_json->>'listener_psychotherapy_format', ''),
  NULLIF(s.payload_json->>'listener_psychotherapy_organization', ''),
  NULLIF(s.payload_json->>'listener_technical_area', ''),
  NULLIF(s.payload_json->>'field_of_study', ''),
  NULLIF(s.payload_json->>'listener_expectations', ''),
  NULLIF(s.payload_json->>'referral_source', ''),
  NULLIF(s.payload_json->>'speaker_current_status', ''),
  NULLIF(s.payload_json->>'speaker_status_other', ''),
  NULLIF(s.payload_json->>'speaker_bachelor_course', ''),
  NULLIF(s.payload_json->>'speaker_specialist_course', ''),
  NULLIF(s.payload_json->>'speaker_master_course', ''),
  NULLIF(s.payload_json->>'speaker_postgraduate_course', ''),
  NULLIF(s.payload_json->>'speaker_research_area', ''),
  NULLIF(s.payload_json->>'speaker_psychotherapy_format', ''),
  NULLIF(s.payload_json->>'speaker_psychotherapy_organization', ''),
  NULLIF(s.payload_json->>'speaker_technical_area', ''),
  NULLIF(s.payload_json->>'speaker_affiliation', ''),
  NULLIF(s.payload_json->>'speaker_specialization', ''),
  NULLIF(s.payload_json->>'talk_topic', ''),
  NULLIF(s.payload_json->>'talk_summary', ''),
  NULLIF(s.payload_json->>'speaker_background', ''),
  s.status
FROM intake.submissions s
WHERE s.kind = 'section_participation'
ON CONFLICT (submission_id) DO NOTHING;

COMMIT;

INSERT INTO public.schema_migrations (version)
VALUES ('0002_section_participations')
ON CONFLICT (version) DO NOTHING;
