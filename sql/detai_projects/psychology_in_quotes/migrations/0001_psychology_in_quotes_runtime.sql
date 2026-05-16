BEGIN;

CREATE SCHEMA IF NOT EXISTS psychology_in_quotes;

CREATE TABLE IF NOT EXISTS public.schema_migrations (
  id BIGSERIAL PRIMARY KEY,
  version TEXT NOT NULL UNIQUE,
  applied_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  applied_by TEXT NOT NULL DEFAULT current_user
);

CREATE OR REPLACE FUNCTION psychology_in_quotes.set_updated_at()
RETURNS trigger
LANGUAGE plpgsql
AS $$
BEGIN
  NEW.updated_at := now();
  RETURN NEW;
END;
$$;

CREATE TABLE IF NOT EXISTS psychology_in_quotes.users (
  id BIGSERIAL PRIMARY KEY,
  telegram_user_id BIGINT NOT NULL UNIQUE,
  username TEXT,
  display_name TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS psychology_in_quotes.user_plans (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT NOT NULL REFERENCES psychology_in_quotes.users (id) ON DELETE CASCADE,
  plan_code TEXT NOT NULL CHECK (plan_code IN ('public', 'free', 'plus', 'pro', 'admin')),
  status TEXT NOT NULL CHECK (status IN ('scheduled', 'active', 'expired', 'paused', 'cancelled')),
  starts_at DATE,
  ends_at DATE,
  source TEXT NOT NULL,
  notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS psychology_in_quotes.moderation_entries (
  id BIGSERIAL PRIMARY KEY,
  telegram_user_id BIGINT,
  username TEXT,
  reason TEXT,
  is_active BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT moderation_entries_target_required CHECK (telegram_user_id IS NOT NULL OR username IS NOT NULL)
);

CREATE TABLE IF NOT EXISTS psychology_in_quotes.channel_bindings (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT NOT NULL REFERENCES psychology_in_quotes.users (id) ON DELETE CASCADE,
  channel_title TEXT NOT NULL,
  channel_username TEXT NOT NULL,
  channel_id TEXT,
  status TEXT NOT NULL CHECK (status IN ('pending', 'active', 'disabled', 'revoked')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT channel_bindings_user_channel_username_key UNIQUE (user_id, channel_username)
);

CREATE TABLE IF NOT EXISTS psychology_in_quotes.user_brand_kits (
  id BIGSERIAL PRIMARY KEY,
  owner_user_id BIGINT NOT NULL REFERENCES psychology_in_quotes.users (id) ON DELETE CASCADE,
  slug TEXT NOT NULL UNIQUE,
  display_name TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('active', 'disabled', 'archived')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS psychology_in_quotes.user_brand_kit_templates (
  id BIGSERIAL PRIMARY KEY,
  brand_kit_id BIGINT NOT NULL REFERENCES psychology_in_quotes.user_brand_kits (id) ON DELETE CASCADE,
  template_code TEXT NOT NULL,
  label TEXT NOT NULL,
  template_kind TEXT NOT NULL CHECK (template_kind IN ('quote', 'story')),
  mime_type TEXT NOT NULL,
  filename TEXT NOT NULL,
  content_bytes BYTEA NOT NULL,
  checksum TEXT NOT NULL,
  width INTEGER,
  height INTEGER,
  is_default BOOLEAN NOT NULL DEFAULT FALSE,
  status TEXT NOT NULL CHECK (status IN ('active', 'disabled', 'archived')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT user_brand_kit_templates_brand_kit_template_code_key UNIQUE (brand_kit_id, template_code)
);

CREATE TABLE IF NOT EXISTS psychology_in_quotes.user_caption_templates (
  id BIGSERIAL PRIMARY KEY,
  brand_kit_id BIGINT NOT NULL REFERENCES psychology_in_quotes.user_brand_kits (id) ON DELETE CASCADE,
  owner_user_id BIGINT NOT NULL REFERENCES psychology_in_quotes.users (id) ON DELETE CASCADE,
  template_kind TEXT NOT NULL,
  content_text TEXT NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('active', 'disabled', 'archived')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS psychology_in_quotes.admin_audit_events (
  id BIGSERIAL PRIMARY KEY,
  actor_user_id BIGINT REFERENCES psychology_in_quotes.users (id) ON DELETE SET NULL,
  event_type TEXT NOT NULL,
  target_type TEXT NOT NULL,
  target_id TEXT NOT NULL,
  payload_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS user_plans_user_id_idx
  ON psychology_in_quotes.user_plans (user_id);

CREATE INDEX IF NOT EXISTS user_plans_plan_code_status_idx
  ON psychology_in_quotes.user_plans (plan_code, status);

CREATE INDEX IF NOT EXISTS moderation_entries_telegram_user_id_idx
  ON psychology_in_quotes.moderation_entries (telegram_user_id);

CREATE INDEX IF NOT EXISTS moderation_entries_username_idx
  ON psychology_in_quotes.moderation_entries (username);

CREATE INDEX IF NOT EXISTS moderation_entries_is_active_idx
  ON psychology_in_quotes.moderation_entries (is_active);

CREATE INDEX IF NOT EXISTS channel_bindings_user_id_idx
  ON psychology_in_quotes.channel_bindings (user_id);

CREATE INDEX IF NOT EXISTS channel_bindings_channel_username_idx
  ON psychology_in_quotes.channel_bindings (channel_username);

CREATE INDEX IF NOT EXISTS user_brand_kits_owner_user_id_idx
  ON psychology_in_quotes.user_brand_kits (owner_user_id);

CREATE INDEX IF NOT EXISTS user_brand_kit_templates_brand_kit_id_idx
  ON psychology_in_quotes.user_brand_kit_templates (brand_kit_id);

CREATE INDEX IF NOT EXISTS user_caption_templates_brand_kit_id_idx
  ON psychology_in_quotes.user_caption_templates (brand_kit_id);

CREATE INDEX IF NOT EXISTS user_caption_templates_owner_user_id_idx
  ON psychology_in_quotes.user_caption_templates (owner_user_id);

CREATE INDEX IF NOT EXISTS admin_audit_events_actor_user_id_idx
  ON psychology_in_quotes.admin_audit_events (actor_user_id);

CREATE INDEX IF NOT EXISTS admin_audit_events_target_idx
  ON psychology_in_quotes.admin_audit_events (target_type, target_id);

DROP TRIGGER IF EXISTS users_set_updated_at ON psychology_in_quotes.users;
CREATE TRIGGER users_set_updated_at
BEFORE UPDATE ON psychology_in_quotes.users
FOR EACH ROW
EXECUTE FUNCTION psychology_in_quotes.set_updated_at();

DROP TRIGGER IF EXISTS user_plans_set_updated_at ON psychology_in_quotes.user_plans;
CREATE TRIGGER user_plans_set_updated_at
BEFORE UPDATE ON psychology_in_quotes.user_plans
FOR EACH ROW
EXECUTE FUNCTION psychology_in_quotes.set_updated_at();

DROP TRIGGER IF EXISTS moderation_entries_set_updated_at ON psychology_in_quotes.moderation_entries;
CREATE TRIGGER moderation_entries_set_updated_at
BEFORE UPDATE ON psychology_in_quotes.moderation_entries
FOR EACH ROW
EXECUTE FUNCTION psychology_in_quotes.set_updated_at();

DROP TRIGGER IF EXISTS channel_bindings_set_updated_at ON psychology_in_quotes.channel_bindings;
CREATE TRIGGER channel_bindings_set_updated_at
BEFORE UPDATE ON psychology_in_quotes.channel_bindings
FOR EACH ROW
EXECUTE FUNCTION psychology_in_quotes.set_updated_at();

DROP TRIGGER IF EXISTS user_brand_kits_set_updated_at ON psychology_in_quotes.user_brand_kits;
CREATE TRIGGER user_brand_kits_set_updated_at
BEFORE UPDATE ON psychology_in_quotes.user_brand_kits
FOR EACH ROW
EXECUTE FUNCTION psychology_in_quotes.set_updated_at();

DROP TRIGGER IF EXISTS user_brand_kit_templates_set_updated_at ON psychology_in_quotes.user_brand_kit_templates;
CREATE TRIGGER user_brand_kit_templates_set_updated_at
BEFORE UPDATE ON psychology_in_quotes.user_brand_kit_templates
FOR EACH ROW
EXECUTE FUNCTION psychology_in_quotes.set_updated_at();

DROP TRIGGER IF EXISTS user_caption_templates_set_updated_at ON psychology_in_quotes.user_caption_templates;
CREATE TRIGGER user_caption_templates_set_updated_at
BEFORE UPDATE ON psychology_in_quotes.user_caption_templates
FOR EACH ROW
EXECUTE FUNCTION psychology_in_quotes.set_updated_at();

COMMIT;

INSERT INTO public.schema_migrations (version)
VALUES ('0001_psychology_in_quotes_runtime')
ON CONFLICT (version) DO NOTHING;
