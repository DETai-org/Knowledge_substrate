SELECT 'CREATE DATABASE detai_projects'
WHERE NOT EXISTS (
  SELECT 1
  FROM pg_database
  WHERE datname = 'detai_projects'
)
\gexec
