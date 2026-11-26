#!/usr/bin/env bash
set -euo pipefail

usage() { echo "Usage: $0 <destination> [--overwrite]"; }
if [[ $# -lt 1 || $# -gt 2 ]]; then usage; exit 2; fi
DEST="$1"
OVERWRITE="${2:-}"
if [[ -n "$OVERWRITE" && "$OVERWRITE" != "--overwrite" ]]; then usage; exit 2; fi
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p "$DEST"
installed=0; skipped=0
for src in "$SCRIPT_DIR"/*/SKILL.md; do
  [[ -f "$src" ]] || continue
  skill_dir="$(basename "$(dirname "$src")")"
  target="$DEST/$skill_dir"
  if [[ -e "$target" && "$OVERWRITE" != "--overwrite" ]]; then
    echo "SKIP existing: $skill_dir"; ((skipped+=1)); continue
  fi
  if [[ -e "$target" ]]; then rm -rf -- "$target"; fi
  mkdir -p "$target"
  cp -R "$(dirname "$src")"/. "$target"/
  echo "INSTALLED: $skill_dir"; ((installed+=1))
done
echo "Done. Installed: $installed | Skipped: $skipped | Destination: $DEST"
