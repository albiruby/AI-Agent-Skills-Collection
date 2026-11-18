#!/usr/bin/env python3
"""Lint the skills pack: frontmatter, size, relative links, domain coverage."""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
SK = ROOT / "skills"
RANGES = {"pra-discovery":(1,4),"pra-codebase-architecture":(5,11),"pra-dependencies-build-cicd":(12,14),
"pra-security":(15,22),"pra-privacy-legal":(23,24),"pra-cms-sanity":(25,32),"pra-functionality-ux":(33,37),
"pra-accessibility-responsive":(38,39),"pra-performance-caching":(40,45),"pra-seo-i18n":(46,49),
"pra-infrastructure-deployment":(50,56),"pra-monitoring-observability":(57,64),"pra-backup-recovery-incident":(65,69),
"pra-cost-scalability":(70,73),"pra-maintenance-governance":(74,80),"pra-testing-acceptance":(81,89),
"pra-reporting-risk":(90,95),"pra-remediation-verification":(96,99)}
errors, warns = [], []
def fm(path):
    t = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not m: return None, t
    d = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1); d[k.strip()] = v.strip()
    return d, t
for d in sorted(p for p in SK.iterdir() if p.is_dir()):
    f = d / "SKILL.md"
    if not f.exists(): errors.append(f"{d.name}: missing SKILL.md"); continue
    meta, text = fm(f)
    if not meta: errors.append(f"{d.name}: no frontmatter"); continue
    if meta.get("name") != d.name: errors.append(f"{d.name}: name '{meta.get('name')}' != folder")
    desc = meta.get("description", "")
    if not desc: errors.append(f"{d.name}: empty description")
    if len(desc) > 1024: errors.append(f"{d.name}: description {len(desc)} > 1024 chars")
    n = len(text.splitlines())
    if n > 500: errors.append(f"{d.name}: SKILL.md {n} lines > 500")
    # backticked relative paths that should exist
    for rel in re.findall(r"`((?:references|templates|scripts)/[A-Za-z0-9_./-]+)`", text):
        if not (d / rel).exists(): errors.append(f"{d.name}: referenced path missing: {rel}")
    for rel in re.findall(r"`(\.\./production-readiness-audit/[A-Za-z0-9_./-]+)`", text):
        if "*" in rel: continue
        if not (d / rel).exists(): errors.append(f"{d.name}: referenced path missing: {rel}")
    if d.name in RANGES:
        a, b = RANGES[d.name]
        ck = d / "references" / "checklist.md"
        if not ck.exists(): errors.append(f"{d.name}: missing references/checklist.md"); continue
        heads = {int(x) for x in re.findall(r"^## (\d+)\.", ck.read_text(encoding="utf-8"), re.M)}
        missing = set(range(a, b + 1)) - heads
        if missing: errors.append(f"{d.name}: checklist missing domains {sorted(missing)}")
        for h in heads - set(range(a, b + 1)): warns.append(f"{d.name}: checklist has out-of-range domain {h}")
covered = set()
for a, b in RANGES.values(): covered |= set(range(a, b + 1))
if covered != set(range(1, 100)): errors.append(f"domain ranges do not cover 1-99: missing {sorted(set(range(1,100))-covered)}")
idx = SK / "production-readiness-audit/references/domain-index.md"
rows = re.findall(r"^\| (\d+) \|", idx.read_text(encoding="utf-8"), re.M) if idx.exists() else []
if len(rows) != 99: errors.append(f"domain-index has {len(rows)} rows, expected 99")
for w in warns: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"\n{len(list(SK.iterdir()))} skills checked · {len(errors)} errors · {len(warns)} warnings")
sys.exit(1 if errors else 0)
