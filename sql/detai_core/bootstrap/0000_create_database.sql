SELECT 'CREATE DATABASE detai_core'
WHERE NOT EXISTS (
  SELECT
  FROM pg_database
  WHERE datname = 'detai_core'
)\gexec
