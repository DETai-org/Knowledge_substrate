#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

sudo -u postgres psql -d postgres -v ON_ERROR_STOP=1 -f "$SCRIPT_DIR/0000_create_database.sql"
