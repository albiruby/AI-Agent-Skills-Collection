#!/usr/bin/env python3
"""Validate the merged Pixel Art Master Studio package (stdlib only)."""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
errors: list[str] = []
found: list[str] = []

required_shared = [
    ROOT / "shared" / "PIXEL_ART_STANDARDS.md",
    ROOT / "references" / "pixel-art-quality-checklist.md",
    ROOT / "templates" / "pixel-art-production-brief.md",
    ROOT / "templates" / "asset-manifest.csv",
]
for path in required_shared:
    if not path.is_file():
        errors.append(f"missing shared file: {path.relative_to(ROOT)}")

for folder in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
    skill_file = folder / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"{folder.name}: missing SKILL.md")
        continue
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---"):
        errors.append(f"{folder.name}: missing frontmatter")
        continue
    end = text.find("\n---", 3)
    if end < 0:
        errors.append(f"{folder.name}: unterminated frontmatter")
        continue
    front = text[3:end]
    body = text[end + 4:].lstrip()
    name_m = re.search(r"^name:\s*(.+)$", front, re.M)
    desc_m = re.search(r"^description:\s*(.+)$", front, re.M)
    if not name_m:
        errors.append(f"{folder.name}: missing name")
        continue
    name = name_m.group(1).strip().strip('"').strip("'")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append(f"{folder.name}: invalid name {name!r}")
    if name != folder.name:
        errors.append(f"{folder.name}: name != folder ({name})")
    if not desc_m:
        errors.append(f"{folder.name}: missing description")
    else:
        desc = desc_m.group(1).strip().strip('"').strip("'")
        if len(desc) > 1024:
            errors.append(f"{folder.name}: description too long")
        if not re.search(r"(?i)\buse (when|whenever)\b", desc):
            errors.append(f"{folder.name}: description lacks Use when trigger")
    h1 = re.search(r"(?m)^#\s+(.+)$", body)
    if not h1:
        errors.append(f"{folder.name}: missing H1")
    else:
        title = h1.group(1).strip()
        if title.lower() in {"instructions", "skill", "title"} or title.isupper():
            errors.append(f"{folder.name}: placeholder/ALL CAPS H1 {title!r}")
    if "## Non-negotiable studio standards" not in body:
        errors.append(f"{folder.name}: missing studio standards block")
    if len(body.strip()) < 500:
        errors.append(f"{folder.name}: body unexpectedly short")
    found.append(name)

if len(found) != 26:
    errors.append(f"expected 26 skills, found {len(found)}")
if "pixel-art-studio-director" not in found:
    errors.append("master skill missing")

for json_file in ROOT.rglob("*.json"):
    try:
        json.loads(json_file.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{json_file.relative_to(ROOT)}: invalid JSON: {exc}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print(f"VALIDATION PASSED: {len(found)} skills")
for item in found:
    print(" -", item)
