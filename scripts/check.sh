#!/usr/bin/env bash
set -euo pipefail

mkdocs build --clean
python -m compileall detai-core
