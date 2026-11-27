#!/usr/bin/env python3
"""Pixel Art QA validator (Pillow-only, no numpy required).

Checks PNG sprites, tilesets, or sheets for:
- unique visible colors and optional palette compliance
- semi-transparent alpha fringe
- orphan/stray 1-pixel islands
- seamless tile edge mismatch
- grid-cell divisibility
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from PIL import Image

RGB = Tuple[int, int, int]
RGBA = Tuple[int, int, int, int]


def parse_hex(value: str) -> RGB:
    value = value.strip().lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    if len(value) != 6:
        raise ValueError(f"Invalid hex color: {value}")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]


def parse_palette(text: Optional[str]) -> Optional[Set[RGB]]:
    if not text:
        return None
    values = [v for v in text.replace(";", ",").replace(" ", ",").split(",") if v.strip()]
    return {parse_hex(v) for v in values}


def parse_cell(text: Optional[str]) -> Optional[Tuple[int, int]]:
    if not text:
        return None
    parts = text.lower().replace("*", "x").split("x")
    if len(parts) != 2:
        raise ValueError("--cell must look like 32x32")
    return int(parts[0]), int(parts[1])


def analyze(path: Path, max_colors: Optional[int], palette: Optional[Set[RGB]],
            allow_semi_alpha: bool, check_seams: bool,
            cell: Optional[Tuple[int, int]], max_orphan_ratio: float) -> Dict[str, object]:
    img = Image.open(path).convert("RGBA")
    w, h = img.size
    px = img.load()
    pixels: List[RGBA] = [px[x, y] for y in range(h) for x in range(w)]
    visible = [p for p in pixels if p[3] > 0]
    visible_count = len(visible)
    unique_colors: Set[RGB] = {p[:3] for p in visible}
    semi_alpha = sum(1 for p in pixels if 0 < p[3] < 255)

    issues: List[str] = []
    if max_colors is not None and len(unique_colors) > max_colors:
        issues.append(f"color count {len(unique_colors)} exceeds max_colors={max_colors}")
    if not allow_semi_alpha and semi_alpha > 0:
        issues.append(f"{semi_alpha} semi-transparent pixels (possible anti-alias fringe)")
    if palette is not None:
        extra = sorted(unique_colors - palette)
        if extra:
            sample = ", ".join("#%02x%02x%02x" % c for c in extra[:10])
            issues.append(f"{len(extra)} colors outside approved palette: {sample}")
    if cell is not None:
        cw, ch = cell
        if w % cw or h % ch:
            issues.append(f"{w}x{h} is not divisible by cell {cw}x{ch}")

    orphan = 0
    if visible_count:
        for y in range(h):
            for x in range(w):
                p = px[x, y]
                if p[3] == 0:
                    continue
                same = False
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and px[nx, ny] == p:
                        same = True
                        break
                if not same:
                    orphan += 1
    orphan_ratio = round(orphan / visible_count, 4) if visible_count else 0.0
    if orphan_ratio > max_orphan_ratio:
        issues.append(f"orphan/stray ratio {orphan_ratio:.1%} exceeds {max_orphan_ratio:.0%}")

    report: Dict[str, object] = {
        "file": str(path),
        "width": w,
        "height": h,
        "visible_pixels": visible_count,
        "unique_colors": len(unique_colors),
        "semi_transparent_pixels": semi_alpha,
        "orphan_pixels": orphan,
        "orphan_ratio": orphan_ratio,
        "verdict": "PASS" if not issues else "FAIL",
        "issues": issues,
    }
    if palette is not None:
        report["palette_colors"] = len(palette)
        report["colors_outside_palette"] = len(unique_colors - palette)
    if check_seams:
        top = [px[x, 0][:3] for x in range(w)]
        bottom = [px[x, h - 1][:3] for x in range(w)]
        left = [px[0, y][:3] for y in range(h)]
        right = [px[w - 1, y][:3] for y in range(h)]
        hdiff = sum(1 for a, b in zip(top, bottom) if a != b) / max(1, w)
        vdiff = sum(1 for a, b in zip(left, right) if a != b) / max(1, h)
        report["seams"] = {
            "horizontal_edge_mismatch_ratio": round(hdiff, 4),
            "vertical_edge_mismatch_ratio": round(vdiff, 4),
        }
        if hdiff > 0 or vdiff > 0:
            # Seams are advisory unless the image is explicitly a seamless tile.
            report["issues"].append("tile edges do not match; verify seamless tile intent")  # type: ignore[union-attr]
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Pixel Art Master Studio QA validator (Pillow-only)")
    parser.add_argument("images", nargs="+", type=Path, help="PNG file(s) to check")
    parser.add_argument("--max-colors", type=int, default=None)
    parser.add_argument("--palette", default=None, help="Comma/space separated approved hex colors")
    parser.add_argument("--allow-semi-alpha", action="store_true", help="Allow partial alpha (VFX)")
    parser.add_argument("--check-seams", action="store_true")
    parser.add_argument("--cell", default=None, help="Grid cell WxH, e.g. 32x32")
    parser.add_argument("--max-orphan-ratio", type=float, default=0.08)
    args = parser.parse_args()

    palette = parse_palette(args.palette)
    cell = parse_cell(args.cell)
    reports = []
    for path in args.images:
        try:
            reports.append(analyze(path, args.max_colors, palette, args.allow_semi_alpha,
                                   args.check_seams, cell, args.max_orphan_ratio))
        except Exception as exc:  # pragma: no cover - user input errors
            reports.append({"file": str(path), "verdict": "ERROR", "error": str(exc)})

    print(json.dumps({"results": reports}, indent=2))
    return 0 if all(r.get("verdict") == "PASS" for r in reports) else 1


if __name__ == "__main__":
    sys.exit(main())
