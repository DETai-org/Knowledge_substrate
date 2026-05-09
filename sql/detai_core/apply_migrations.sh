#!/usr/bin/env bash
set -euo pipefail

DB_NAME="${DB_NAME:-detai_core}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

mapfile -t MIGRATION_FILES < <(
  find "$SCRIPT_DIR/infra/migrations" "$SCRIPT_DIR/ecosystem/migrations" "$SCRIPT_DIR/publications/migrations" \
    -maxdepth 1 -type f -name '*.sql' | sort
)

[ "${#MIGRATION_FILES[@]}" -gt 0 ] || { echo "no migrations found"; exit 0; }

for f in "${MIGRATION_FILES[@]}"; do
  echo "==> applying $f"
  sudo -u postgres psql -d "$DB_NAME" -v ON_ERROR_STOP=1 -f "$f"
done
