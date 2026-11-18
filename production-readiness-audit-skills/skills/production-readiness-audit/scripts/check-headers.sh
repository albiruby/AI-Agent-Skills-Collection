#!/usr/bin/env bash
# Read-only HTTP checks against an AUTHORIZED url (HEAD/GET only).
# Usage: bash check-headers.sh https://example.com [path ...]
set -u
BASE="${1:?usage: check-headers.sh https://host [path ...]}"; shift
BASE="${BASE%/}"; PATHS=("${@:-/}")
command -v curl >/dev/null || { echo "curl required"; exit 1; }
echo "== Redirect check (http -> https) =="
HOST="${BASE#*://}"; curl -sI -m 15 -o /dev/null -w "http://$HOST -> %{http_code} %{redirect_url}\n" "http://$HOST" || echo "request failed"
echo "== www / apex canonical check =="
case "$HOST" in www.*) ALT="${HOST#www.}";; *) ALT="www.$HOST";; esac
curl -sI -m 15 -o /dev/null -w "https://$ALT -> %{http_code} %{redirect_url}\n" "https://$ALT" || echo "request failed"
for p in "${PATHS[@]}"; do
  echo; echo "== $BASE$p =="
  H=$(curl -sI -m 20 -H 'Accept-Encoding: gzip, br' "$BASE$p") || { echo "request failed"; continue; }
  echo "$H" | head -1
  for k in strict-transport-security content-security-policy x-content-type-options referrer-policy permissions-policy x-frame-options cache-control content-encoding server x-powered-by x-vercel-cache x-robots-tag; do
    v=$(echo "$H" | grep -i "^$k:" | head -1 | tr -d '\r'); [ -n "$v" ] && echo "  present  $v" || echo "  MISSING  $k"
  done
done
echo; echo "== robots / sitemap / 404 =="
for u in /robots.txt /sitemap.xml /this-route-should-not-exist-404-check; do curl -s -m 15 -o /dev/null -w "$u -> %{http_code}\n" "$BASE$u"; done
echo; echo "Interpretation: x-powered-by/server disclosure and missing headers are findings only if relevant to this project; CSP/frame-ancestors need context. x-robots-tag: noindex on production is a launch blocker."
