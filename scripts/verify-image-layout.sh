#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
required=(
  "image/stage-azmiga/00-run.sh"
  "image/stage-azmiga/files/az-miga-launch.sh"
  "image/stage-azmiga/files/az-miga.desktop"
  "scripts/build-image.sh"
  "docs/WORKBENCH-FIRST.md"
  "docs/FICHIERS-EMULATION.md"
  "data/kickstart-manifest.json"
)
for f in "${required[@]}"; do
  [[ -s "$f" ]] || { echo "MISSING $f" >&2; exit 1; }
done
bash -n image/stage-azmiga/00-run.sh scripts/build-image.sh
sh -n image/stage-azmiga/files/az-miga-launch.sh
python3 -m json.tool data/kickstart-manifest.json >/dev/null
echo "AZ-miga layout/syntax checks OK (no disk image built)"
