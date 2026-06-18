#!/usr/bin/env bash
set -euo pipefail

DB_NAME="${DB_NAME:-detai_projects}"
MIGRATIONS_DIR="$(cd "$(dirname "$0")" && pwd)/migrations"

for f in "$MIGRATIONS_DIR"/*.sql; do
  [ -e "$f" ] || { echo "no migrations found"; exit 0; }
  echo "==> applying $f"
  sudo -u postgres psql -d "$DB_NAME" -v ON_ERROR_STOP=1 -f "$f"
done
