BEGIN;

WITH upserted_user AS (
  INSERT INTO psychology_in_quotes.users (
    telegram_user_id,
    username,
    display_name
  )
  VALUES (
    997865187,
    'Anton_Kolhonen',
    'Anton'
  )
  ON CONFLICT (telegram_user_id) DO UPDATE
  SET
    username = EXCLUDED.username,
    display_name = EXCLUDED.display_name,
    updated_at = now()
  RETURNING id
),
resolved_user AS (
  SELECT id FROM upserted_user
  UNION ALL
  SELECT id
  FROM psychology_in_quotes.users
  WHERE telegram_user_id = 997865187
  LIMIT 1
)
INSERT INTO psychology_in_quotes.user_plans (
  user_id,
  plan_code,
  status,
  starts_at,
  ends_at,
  source,
  notes
)
SELECT
  id,
  'pro',
  'active',
  DATE '2026-05-06',
  DATE '2026-06-06',
  'runtime-db-seed:user-access.json',
  ''
FROM resolved_user
WHERE NOT EXISTS (
  SELECT 1
  FROM psychology_in_quotes.user_plans up
  WHERE up.user_id = resolved_user.id
    AND up.plan_code = 'pro'
    AND up.starts_at = DATE '2026-05-06'
    AND up.ends_at = DATE '2026-06-06'
);

WITH resolved_user AS (
  SELECT id
  FROM psychology_in_quotes.users
  WHERE telegram_user_id = 997865187
)
INSERT INTO psychology_in_quotes.channel_bindings (
  user_id,
  channel_title,
  channel_username,
  channel_id,
  status
)
SELECT
  id,
  'Психология |🌓| Колхонен Антон',
  '@psychology_evil',
  '-1002249561075',
  'active'
FROM resolved_user
ON CONFLICT (user_id, channel_username) DO UPDATE
SET
  channel_title = EXCLUDED.channel_title,
  channel_id = EXCLUDED.channel_id,
  status = EXCLUDED.status,
  updated_at = now();

COMMIT;
