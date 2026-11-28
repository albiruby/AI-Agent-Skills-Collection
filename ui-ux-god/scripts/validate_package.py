#!/usr/bin/env python3
"""
validate_package.py
Structural validator for the ui-ux-god skill pack.

Checks:
- every skills/<name>/SKILL.md exists and has frontmatter
- exactly name + description
- name == folder, kebab-case
- description <= 1024 chars and contains a "Use when..." trigger
- H1 title present, not ALL CAPS
- referenced local paths (../../references|templates|scripts|shared|examples|evals/...)
  resolve from the skill folder
- skill-pack.json parses, skill paths and resources exist
- no empty files

Usage:
  python scripts/validate_package.py
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MANIFEST = ROOT / "skill-pack.json"

REQUIRED_DIRS = ["skills", "shared", "references", "templates", "scripts", "examples", "evals"]
LOCAL_REF_RE = re.compile(r"`(\.\./\.\./(?:references|templates|scripts|shared|examples|evals)/[^`\s]+)`")
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class Validator:
    def __init__(self):
        self.issues = []
        self.checked = 0

    def fail(self, path, message):
        self.issues.append(f"{path}: {message}")

    def run(self):
        for d in REQUIRED_DIRS:
            if not (ROOT / d).is_dir():
                self.fail(d, "required directory is missing")

        skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
        if not skill_files:
            self.fail("skills", "no SKILL.md files found")

        names = set()
        for file in skill_files:
            self.checked += 1
            rel = file.relative_to(ROOT).as_posix()
            text = file.read_text(encoding="utf-8")
            lines = text.splitlines()

            if not lines or lines[0].strip() != "---":
                self.fail(rel, "must start with YAML frontmatter")
                continue

            try:
                close = lines.index("---", 1)
            except ValueError:
                self.fail(rel, "frontmatter is not closed")
                continue

            frontmatter = lines[1:close]
            keys = []
            for line in frontmatter:
                m = re.match(r"^([A-Za-z_-]+)\s*:", line)
                if m:
                    keys.append(m.group(1))
            extra = [k for k in keys if k not in ("name", "description")]
            missing = [k for k in ("name", "description") if k not in keys]
            if missing:
                self.fail(rel, f"missing frontmatter key(s): {', '.join(missing)}")
            if extra:
                self.fail(rel, f"extra frontmatter key(s): {', '.join(extra)}")

            name = ""
            desc = ""
            for line in frontmatter:
                if line.startswith("name:"):
                    name = line.split(":", 1)[1].strip().strip('"').strip("'")
                if line.startswith("description:"):
                    desc = line.split(":", 1)[1].strip().strip('"').strip("'")

            folder = file.parent.name
            if not name:
                self.fail(rel, "name is empty")
            else:
                if not KEBAB_RE.match(name):
                    self.fail(rel, f"name '{name}' is not kebab-case")
                if name != folder:
                    self.fail(rel, f"folder '{folder}' != name '{name}'")
                if name in names:
                    self.fail(rel, f"duplicate name '{name}'")
                names.add(name)

            if not desc:
                self.fail(rel, "description is empty")
            else:
                if len(desc) > 1024:
                    self.fail(rel, f"description is {len(desc)} chars (max 1024)")
                if not re.search(r"(?i)\buse (when|whenever)\b", desc):
                    self.fail(rel, "description lacks a 'Use when...' trigger")

            h1 = next((line for line in lines if line.startswith("# ")), None)
            if not h1:
                self.fail(rel, "missing H1")
            elif re.match(r"^#\s+[A-Z0-9\s&:()\-]{6,}$", h1) and h1.upper() == h1:
                self.fail(rel, f"H1 looks ALL CAPS: {h1}")

            for m in LOCAL_REF_RE.finditer(text):
                target = m.group(1)
                if not (file.parent / target).exists():
                    self.fail(rel, f"referenced path does not exist: {target}")

            if len(text.strip()) < 400:
                self.fail(rel, "file is suspiciously short")

        self.check_manifest()
        self.check_empty_files()
        return self.issues

    def check_manifest(self):
        if not MANIFEST.is_file():
            self.fail("skill-pack.json", "manifest is missing")
            return
        try:
            data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            self.fail("skill-pack.json", f"invalid JSON: {exc}")
            return

        skills = data.get("skills", [])
        if not isinstance(skills, list) or not skills:
            self.fail("skill-pack.json", "skills[] is missing or empty")
            return

        declared = len(skills)
        actual = len(list(SKILLS_DIR.glob("*/SKILL.md")))
        if declared != actual:
            self.fail("skill-pack.json", f"declares {declared} skills but {actual} SKILL.md files exist")

        for item in skills:
            path = item.get("path")
            if not path:
                self.fail("skill-pack.json", f"skill '{item.get('id', '?')}' has no path")
                continue
            if not (ROOT / path).is_file():
                self.fail("skill-pack.json", f"missing skill path: {path}")

        resources = data.get("resources", {})
        if isinstance(resources, dict):
            for group, entries in resources.items():
                if not isinstance(entries, list):
                    continue
                for entry in entries:
                    if not (ROOT / entry).exists():
                        self.fail("skill-pack.json", f"missing resource: {entry}")

    def check_empty_files(self):
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            if ".git" in path.parts or "__pycache__" in path.parts:
                continue
            if path.stat().st_size == 0:
                self.fail(path.relative_to(ROOT).as_posix(), "file is empty")


def main():
    validator = Validator()
    issues = validator.run()
    print(f"Checked {validator.checked} SKILL.md file(s) in {ROOT}")
    if issues:
        print(f"\nFAIL: {len(issues)} issue(s):")
        for issue in issues:
            print(f"  - {issue}")
        return 1
    print("All package checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
