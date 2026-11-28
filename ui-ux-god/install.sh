#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: bash install.sh <destination-skills-dir> [--overwrite]"
  exit 2
fi

DEST="$1"
OVERWRITE="${2:-}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_NAME="$(basename "$SCRIPT_DIR")"
TARGET="$DEST/$PACK_NAME"

mkdir -p "$DEST"

if [ "$SCRIPT_DIR" = "$TARGET" ]; then
  echo "Source and destination are the same: $TARGET"
  exit 0
fi

if [ -e "$TARGET" ]; then
  if [ "$OVERWRITE" != "--overwrite" ]; then
    echo "SKIP    $PACK_NAME (already exists at $TARGET; use --overwrite to replace)"
    exit 0
  fi
  rm -rf "$TARGET"
fi

echo "INSTALL $PACK_NAME -> $TARGET"
cp -R "$SCRIPT_DIR" "$TARGET"

find "$TARGET" -type d \( -name '__pycache__' -o -name 'node_modules' -o -name 'audit-out' -o -name '.git' \) -prune -exec rm -rf {} + 2>/dev/null || true

SKILL_COUNT="$(find "$TARGET/skills" -name SKILL.md -type f | wc -l | tr -d ' ')"
echo "Done. Installed $SKILL_COUNT skills."
echo "Validate with: python \"$TARGET/scripts/validate_package.py\""
