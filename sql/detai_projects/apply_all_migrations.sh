#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

mapfile -t APPLY_SCRIPTS < <(
  find "$SCRIPT_DIR" -mindepth 2 -maxdepth 2 -type f -name 'apply_migrations.sh' \
    ! -path "$SCRIPT_DIR/bootstrap/*" | sort
)

[ "${#APPLY_SCRIPTS[@]}" -gt 0 ] || { echo "no project schema migration scripts found"; exit 0; }

for f in "${APPLY_SCRIPTS[@]}"; do
  echo "==> applying project schema via $f"
  bash "$f"
done
