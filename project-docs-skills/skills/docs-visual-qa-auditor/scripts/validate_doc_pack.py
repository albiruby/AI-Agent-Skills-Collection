#!/usr/bin/env python3
"""
Documentation & Visual Asset Pack QA Validator
----------------------------------------------
Audits a repository's Markdown documentation, clean sliced screenshots,
and store/preview visual assets for release readiness.

Exit code 0 = PASS (0 errors; warnings allowed).
Exit code 1 = FAIL (1 or more errors found).

Dependencies: Pillow (required for image checks).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Tuple

from PIL import Image


LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
DIM_RE = re.compile(r"(\d{3,4})x(\d{3,4})", re.IGNORECASE)
PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTBD\b"),
    re.compile(r"\[Insert\b", re.IGNORECASE),
    re.compile(r"\bLorem ipsum\b", re.IGNORECASE),
    re.compile(r"<\s*(Project Name|App Name|Feature \d+)\s*>"),
]


def check_markdown_files(project_root: Path) -> Tuple[List[str], List[str], int]:
    errors: List[str] = []
    warnings: List[str] = []
    md_files = []

    for name in ("README.md", "CHANGELOG.md"):
        p = project_root / name
        if p.is_file():
            md_files.append(p)

    docs_dir = project_root / "docs"
    if docs_dir.is_dir():
        md_files.extend(sorted(docs_dir.rglob("*.md")))

    for md in md_files:
        text = md.read_text(encoding="utf-8", errors="replace")
        # Strip fenced code blocks before placeholder/link scanning
        stripped = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

        for pat in PLACEHOLDER_PATTERNS:
            m = pat.search(stripped)
            if m:
                errors.append(f"[PLACEHOLDER] {md.relative_to(project_root)}: found '{m.group(0)}'")

        for raw_target in LINK_RE.findall(stripped):
            target = raw_target.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path_str = target.split("#")[0]
            if not target_path_str:
                continue
            resolved = (md.parent / target_path_str).resolve()
            if not resolved.exists():
                errors.append(f"[BROKEN_LINK] {md.relative_to(project_root)} -> '{target}' not found")

    return errors, warnings, len(md_files)


def check_clean_screenshots(clean_dir: Path, allow_opaque: bool = False) -> Tuple[List[str], List[str], int]:
    errors: List[str] = []
    warnings: List[str] = []
    if not clean_dir.is_dir():
        return errors, warnings, 0

    files = [p for p in sorted(clean_dir.iterdir()) if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
    for p in files:
        if p.suffix.lower() != ".png":
            errors.append(f"[CLEAN_FORMAT] {p.name}: clean sliced assets must be lossless .png, not {p.suffix}")
            continue
        with Image.open(p) as im:
            rgba = im.convert("RGBA")
            w, h = rgba.size
            if w < 100 or h < 100:
                warnings.append(f"[LOW_RES] {p.name}: very small dimensions ({w}x{h})")
            if not allow_opaque:
                corners = [
                    rgba.getpixel((0, 0))[3],
                    rgba.getpixel((w - 1, 0))[3],
                    rgba.getpixel((0, h - 1))[3],
                    rgba.getpixel((w - 1, h - 1))[3],
                ]
                if any(a > 10 for a in corners):
                    errors.append(
                        f"[OPAQUE_CORNERS] {p.name}: exterior corners are not transparent (alpha={corners}); "
                        "may still contain uncleaned simulator background or window chrome"
                    )
    return errors, warnings, len(files)


def check_store_assets(store_dir: Path, max_mb: float = 2.0) -> Tuple[List[str], List[str], int]:
    errors: List[str] = []
    warnings: List[str] = []
    if not store_dir.is_dir():
        return errors, warnings, 0

    master_dir = store_dir / "master"
    files = [
        p for p in sorted(store_dir.iterdir())
        if p.is_file() and p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
    ]
    if files and not master_dir.is_dir():
        warnings.append(f"[NO_MASTER_DIR] {store_dir}: missing 'master/' folder for lossless archival PNGs")

    max_bytes = int(max_mb * 1024 * 1024)
    for p in files:
        size_bytes = p.stat().st_size
        if size_bytes > max_bytes:
            warnings.append(f"[LARGE_FILE] {p.name}: {size_bytes / (1024 * 1024):.2f} MB exceeds {max_mb} MB target")

        with Image.open(p) as im:
            w, h = im.size
            m = DIM_RE.search(p.stem)
            if m:
                exp_w, exp_h = int(m.group(1)), int(m.group(2))
                if (w, h) != (exp_w, exp_h):
                    errors.append(f"[DIM_MISMATCH] {p.name}: expected {exp_w}x{exp_h} from filename, got {w}x{h}")

        if master_dir.is_dir():
            expected_master = master_dir / f"{p.stem}.png"
            if not expected_master.is_file():
                warnings.append(f"[MISSING_MASTER] {p.name}: no matching master/{p.stem}.png")

    return errors, warnings, len(files)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate project documentation and visual/store asset packs.")
    parser.add_argument("--project-root", default=".", help="Repository root directory")
    parser.add_argument("--clean-dir", default="docs/assets/clean", help="Clean sliced screenshots directory")
    parser.add_argument("--store-dir", default="docs/store-assets", help="Store preview assets directory")
    parser.add_argument("--allow-opaque-clean", action="store_true", help="Skip transparent corner check for clean screenshots")
    parser.add_argument("--max-store-mb", type=float, default=2.0, help="File size warning threshold in MB (default: 2.0)")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    clean_dir = Path(args.clean_dir)
    if not clean_dir.is_absolute():
        clean_dir = (root / clean_dir).resolve()
    store_dir = Path(args.store_dir)
    if not store_dir.is_absolute():
        store_dir = (root / store_dir).resolve()

    md_err, md_warn, md_count = check_markdown_files(root)
    cl_err, cl_warn, cl_count = check_clean_screenshots(clean_dir, allow_opaque=args.allow_opaque_clean)
    st_err, st_warn, st_count = check_store_assets(store_dir, max_mb=args.max_store_mb)

    all_errors = md_err + cl_err + st_err
    all_warnings = md_warn + cl_warn + st_warn
    status = "PASS" if not all_errors else "FAIL"

    report = {
        "status": status,
        "checked": {
            "markdown_files": md_count,
            "clean_screenshots": cl_count,
            "store_assets": st_count,
        },
        "errors": all_errors,
        "warnings": all_warnings,
    }
    print(json.dumps(report, indent=2))
    sys.exit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
