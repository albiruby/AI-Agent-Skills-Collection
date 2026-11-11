#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/skills"
DEST="${1:-}"
MODE="${2:-}"

if [[ -z "$DEST" ]]; then
  echo "Usage: bash install.sh <destination-skill-root> [--overwrite]" >&2
  echo "Example: bash install.sh .agents/skills" >&2
  exit 2
fi
if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Could not find package skills directory: $SOURCE_DIR" >&2
  exit 1
fi
if [[ "$MODE" != "" && "$MODE" != "--overwrite" ]]; then
  echo "Unknown option: $MODE" >&2
  exit 2
fi

mkdir -p "$DEST"
DEST="$(cd "$DEST" && pwd)"
count=0
skipped=0
for skill_dir in "$SOURCE_DIR"/*; do
  [[ -d "$skill_dir" && -f "$skill_dir/SKILL.md" ]] || continue
  name="$(basename "$skill_dir")"
  target="$DEST/$name"
  if [[ -e "$target" ]]; then
    if [[ "$MODE" == "--overwrite" ]]; then
      rm -rf "$target"
    else
      echo "SKIP existing: $target (use --overwrite to replace)"
      skipped=$((skipped + 1))
      continue
    fi
  fi
  cp -R "$skill_dir" "$target"
  echo "INSTALLED: $target"
  count=$((count + 1))
done
printf '\nInstalled: %s\nSkipped: %s\nDestination: %s\n' "$count" "$skipped" "$DEST"
