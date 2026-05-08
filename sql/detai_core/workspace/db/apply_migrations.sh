#!/usr/bin/env bash
set -euo pipefail

DB_NAME="${DB_NAME:-detai_core}"

for f in "$(dirname "$0")/migrations/"*.sql; do
  [ -e "$f" ] || { echo "no migrations found"; exit 0; }
  echo "==> applying $f"
  sudo -u postgres psql -d "$DB_NAME" -v ON_ERROR_STOP=1 -f "$f"
done
