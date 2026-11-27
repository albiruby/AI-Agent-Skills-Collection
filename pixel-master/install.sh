#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/skills"
OVERWRITE=false
DESTINATION=""

for arg in "$@"; do
  case "$arg" in
    --overwrite) OVERWRITE=true ;;
    -h|--help)
      echo "Usage: bash ./install.sh <destination> [--overwrite]"
      exit 0
      ;;
    *)
      if [[ -z "$DESTINATION" ]]; then DESTINATION="$arg"; else
        echo "Unexpected argument: $arg" >&2; exit 2
      fi
      ;;
  esac
done

if [[ -z "$DESTINATION" ]]; then
  echo "Usage: bash ./install.sh <destination> [--overwrite]" >&2
  exit 2
fi
if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Skills source directory not found: $SOURCE_DIR" >&2
  exit 1
fi
mkdir -p "$DESTINATION"
DESTINATION="$(cd "$DESTINATION" && pwd)"
installed=0
skipped=0

for source in "$SOURCE_DIR"/*; do
  [[ -d "$source" ]] || continue
  skill="$(basename "$source")"
  target="$DESTINATION/$skill"
  if [[ -e "$target" ]]; then
    if [[ "$OVERWRITE" == true ]]; then
      rm -rf -- "$target"
    else
      echo "SKIP  $skill (already exists)"
      skipped=$((skipped+1))
      continue
    fi
  fi
  cp -R "$source" "$target"
  if [[ ! -s "$target/SKILL.md" ]]; then
    echo "ERROR $skill (SKILL.md missing after copy)" >&2
    exit 1
  fi
  echo "OK    $skill"
  installed=$((installed+1))
done

echo "Installed: $installed | Skipped: $skipped | Destination: $DESTINATION"
