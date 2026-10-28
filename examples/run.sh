#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python -m gbt_art_brief info
PYTHONPATH=src python -m gbt_art_brief check --payload '{}'
PYTHONPATH=src python -m gbt_art_brief run   --payload '{}'
