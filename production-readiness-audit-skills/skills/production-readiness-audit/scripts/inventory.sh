#!/usr/bin/env bash
# Read-only project inventory for production-readiness audits.
# Usage: bash inventory.sh [project-root]
# Prints structure, versions, routes, env var NAMES (never values), CI, docs, git hygiene.
set -u
ROOT="${1:-.}"
cd "$ROOT" 2>/dev/null || { echo "Cannot cd to $ROOT"; exit 1; }
# find wrapper that skips heavy/generated folders (no eval)
ff() { find . -type f -not -path '*/node_modules/*' -not -path '*/.next/*' -not -path '*/.git/*' -not -path '*/dist/*' "$@" 2>/dev/null; }
h() { printf '\n## %s\n' "$1"; }

h "Runtime / package manager"
for c in node npm pnpm yarn bun; do command -v $c >/dev/null 2>&1 && printf '%s %s\n' "$c" "$($c -v 2>/dev/null | head -1)"; done
ls -1 package-lock.json pnpm-lock.yaml yarn.lock bun.lockb bun.lock 2>/dev/null | sed 's/^/lockfile: /'
[ -f .nvmrc ] && echo ".nvmrc: $(cat .nvmrc)"; [ -f .node-version ] && echo ".node-version: $(cat .node-version)"
node -e 'try{const p=require("./package.json");console.log("packageManager: "+(p.packageManager||"(not set)"));console.log("engines: "+JSON.stringify(p.engines||"(not set)"))}catch(e){}' 2>/dev/null

h "Key dependency versions (declared)"
if command -v node >/dev/null 2>&1 && [ -f package.json ]; then
  node -e 'try{const p=require("./package.json");const w=["next","react","react-dom","typescript","tailwindcss","sanity","next-sanity","@sanity/client","@sanity/image-url","eslint","zod"];const all={...p.devDependencies,...p.dependencies};for(const k of w)if(all[k])console.log(k+": "+all[k])}catch(e){console.log("package.json unreadable")}'
else
  grep -E '"(next|react|react-dom|typescript|tailwindcss|sanity|next-sanity)"' package.json 2>/dev/null
fi

h "Scripts"
node -e 'try{const s=require("./package.json").scripts||{};for(const k in s)console.log(k+": "+s[k])}catch(e){}' 2>/dev/null

h "Router & special files"
ls -d app src/app pages src/pages middleware.* src/middleware.* proxy.* src/proxy.* 2>/dev/null
ff \( -name 'page.*' -o -name 'route.*' -o -name 'layout.*' -o -name 'loading.*' -o -name 'error.*' -o -name 'global-error.*' -o -name 'not-found.*' -o -name 'template.*' -o -name '_app.*' -o -name '_document.*' \) | grep -E '/(app|pages)/' | sort | head -200

h "Client / server component markers"
echo "files with 'use client': $(grep -rlE "^['\"]use client['\"]" --include='*.ts' --include='*.tsx' --include='*.js' --include='*.jsx' . 2>/dev/null | grep -v node_modules | wc -l)"
echo "files with 'use server': $(grep -rlE "^['\"]use server['\"]" --include='*.ts' --include='*.tsx' . 2>/dev/null | grep -v node_modules | wc -l)"

h "Environment variable NAMES referenced in code (values never printed)"
grep -rhoE 'process\.env\.[A-Za-z0-9_]+' --include='*.ts' --include='*.tsx' --include='*.js' --include='*.jsx' --include='*.mjs' . 2>/dev/null | grep -v node_modules | sort -u
echo "-- NEXT_PUBLIC_* (exposed to browser):"
grep -rhoE 'NEXT_PUBLIC_[A-Za-z0-9_]+' . --include='*.ts' --include='*.tsx' --include='*.js' --include='*.mjs' --include='*.json' 2>/dev/null | sort -u
echo "-- env files present (names only):"; ls -1a .env* 2>/dev/null

h "Config files"
ls -1 next.config.* tsconfig*.json tailwind.config.* postcss.config.* eslint.config.* .eslintrc* .prettierrc* vercel.json sanity.config.* sanity.cli.* sanity.json playwright.config.* vitest.config.* jest.config.* 2>/dev/null

h "CI/CD"
ls -1 .github/workflows 2>/dev/null; ls -1 .github 2>/dev/null | grep -Ei 'dependabot|codeowners|renovate'; ls -1 renovate.json 2>/dev/null

h "Documentation"
ls -1 *.md docs 2>/dev/null | head -50

h "Tests"
find . \( -path ./node_modules -o -path ./.next -o -path ./.git \) -prune -o \( -name '*.test.*' -o -name '*.spec.*' -o -name '__tests__' -o -name 'e2e' \) -print 2>/dev/null | head -30

h "Code-health markers (counts)"
for p in TODO FIXME HACK XXX "console\\.log" "debugger" "@ts-ignore" "@ts-expect-error" ": any" "dangerouslySetInnerHTML"; do
  printf '%s: %s\n' "$p" "$(grep -rE "$p" --include='*.ts' --include='*.tsx' --include='*.js' --include='*.jsx' . 2>/dev/null | grep -v node_modules | wc -l)"
done

h "Git hygiene"
if git rev-parse --git-dir >/dev/null 2>&1; then
  echo "branch: $(git branch --show-current)"
  echo "remotes (credentials masked):"; git remote -v | sed -E 's#//[^@/]+@#//***@#'
  echo "uncommitted/untracked entries: $(git status --porcelain | wc -l)"
  echo "recent commits:"; git log -5 --oneline 2>/dev/null
  echo "tracked env files:"; git ls-files | grep -E '(^|/)\.env' || echo "none"
  echo "tracked files >1MB:"; git ls-files -z | xargs -0 -I{} sh -c 'f="{}"; [ -f "$f" ] && s=$(wc -c <"$f") && [ "$s" -gt 1000000 ] && echo "$s $f"' 2>/dev/null | sort -rn | head -15
  echo "tags: $(git tag | wc -l)"
  echo "merge-conflict markers:"; git grep -nE '^(<<<<<<<|>>>>>>>) ' -- . ':!*.md' 2>/dev/null | head -5
else
  echo "not a git repository"
fi
echo; echo "Done. Output contains no env values or secrets."
