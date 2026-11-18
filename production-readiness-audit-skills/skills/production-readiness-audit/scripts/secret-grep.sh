#!/usr/bin/env bash
# Read-only secret pattern scan. Prints file:line and the PATTERN NAME only — never the matched value.
# Usage: bash secret-grep.sh [project-root] [--history]
set -u
ROOT="${1:-.}"; HIST="${2:-}"
cd "$ROOT" 2>/dev/null || { echo "Cannot cd to $ROOT"; exit 1; }
INC=(--include='*.ts' --include='*.tsx' --include='*.js' --include='*.jsx' --include='*.mjs' --include='*.json' --include='*.yml' --include='*.yaml' --include='*.env*' --include='*.md' --include='*.sh' --include='*.toml')
EXD=(--exclude-dir=node_modules --exclude-dir=.next --exclude-dir=.git --exclude-dir=dist --exclude=package-lock.json --exclude=pnpm-lock.yaml --exclude=yarn.lock)
declare -A P=(
 [aws-access-key]='AKIA[0-9A-Z]{16}'
 [github-token]='gh[pousr]_[A-Za-z0-9]{36,}'
 [slack-token]='xox[baprs]-[A-Za-z0-9-]{10,}'
 [stripe-live-key]='sk_live_[A-Za-z0-9]{16,}'
 [openai-style-key]='sk-[A-Za-z0-9_-]{32,}'
 [google-api-key]='AIza[0-9A-Za-z_-]{35}'
 [private-key-block]='-----BEGIN [A-Z ]*PRIVATE KEY-----'
 [sanity-token-like]='\bsk[A-Za-z0-9]{50,}\b'
 [jwt-like]='eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}'
 [generic-assignment]='(api[_-]?key|secret|token|passwd|password|private[_-]?key)["'"'"']?[[:space:]]*[:=][[:space:]]*["'"'"'][^"'"'"' ]{12,}["'"'"']'
 [credentials-in-url]='[a-z]+://[^/[:space:]:@]+:[^/[:space:]@]{4,}@'
)
found=0
for name in "${!P[@]}"; do
  out=$(grep -rnE "${INC[@]}" "${EXD[@]}" -e "${P[$name]}" . 2>/dev/null | cut -d: -f1,2)
  if [ -n "$out" ]; then found=1; echo "[$name]"; echo "$out" | sed 's/^/  /' | head -25; fi
done
echo "-- NEXT_PUBLIC_ variables whose NAME suggests a secret:"
grep -rnoE "${EXD[@]}" 'NEXT_PUBLIC_[A-Z0-9_]*(SECRET|TOKEN|PRIVATE|PASSWORD|WRITE|SERVICE_ROLE)[A-Z0-9_]*' . 2>/dev/null | sed 's/^/  /' | head -20
if git rev-parse --git-dir >/dev/null 2>&1; then
  echo "-- tracked .env files:"; git ls-files | grep -E '(^|/)\.env(\.|$)' | grep -vE '\.example$|\.sample$|\.template$' | sed 's/^/  /'
  if [ "$HIST" = "--history" ]; then
    echo "-- .env files ever added in history:"; git log --all --diff-filter=A --name-only --pretty=format: -- '*.env' '.env*' 2>/dev/null | sort -u | sed '/^$/d' | sed 's/^/  /'
  fi
fi
[ $found -eq 0 ] && echo "No pattern matches in working tree (this is not proof of absence)."
echo "Review each hit manually; mask values in the report. Rotate any confirmed live secret (needs owner approval)."
