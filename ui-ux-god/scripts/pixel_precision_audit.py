#!/usr/bin/env python3
"""
pixel_precision_audit.py
Pillow-only pixel inspection for rendered UI screenshots.

Features:
1. Outer margin symmetry (left vs right ink bounds).
2. Header/top-band optical centering (bbox center vs ink center-of-mass).
3. Horizontal divider detection and completeness/asymmetry checks.
4. Annotated overlay PNG.
5. Before/after visual diff with changed-pixel percentage and bounding box.

No numpy or OpenCV required. Python 3.9+.

Usage:
  python pixel_precision_audit.py --image desktop-1440.png --out annotated.png --json report.json
  python pixel_precision_audit.py --before before.png --after after.png --out diff.png
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

DEFAULT_BG_TOLERANCE = 18
DEFAULT_DIFF_TOLERANCE = 12


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Pixel-precision UI screenshot audit (Pillow-only).")
    parser.add_argument("--image", help="Single screenshot to analyze.")
    parser.add_argument("--out", help="Annotated output PNG (single mode) or diff PNG (diff mode).")
    parser.add_argument("--json", help="Write a JSON report to this path.")
    parser.add_argument("--before", help="Before screenshot (diff mode).")
    parser.add_argument("--after", help="After screenshot (diff mode).")
    parser.add_argument("--tolerance", type=int, default=DEFAULT_BG_TOLERANCE,
                        help=f"Foreground/background color distance threshold (default {DEFAULT_BG_TOLERANCE}).")
    parser.add_argument("--diff-tolerance", type=int, default=DEFAULT_DIFF_TOLERANCE,
                        help=f"Per-channel diff threshold for change detection (default {DEFAULT_DIFF_TOLERANCE}).")
    parser.add_argument("--min-line-ratio", type=float, default=0.35,
                        help="Minimum divider width as a fraction of image width (default 0.35).")
    parser.add_argument("--header-height", type=int, default=120,
                        help="Top band height for the optical-centering check (default 120).")
    parser.add_argument("--theme", choices=["auto", "light", "dark"], default="auto",
                        help="Hint for expected background; auto samples the border (default auto).")
    parser.add_argument("--quiet", action="store_true", help="Suppress console output.")
    args = parser.parse_args(argv)

    if args.before or args.after:
        if not (args.before and args.after):
            parser.error("Diff mode requires both --before and --after.")
        if not args.out:
            parser.error("Diff mode requires --out.")
        return args

    if not args.image:
        parser.error("Single mode requires --image.")
    if not args.out:
        args.out = str(Path(args.image).with_name(Path(args.image).stem + "-annotated.png"))
    return args


def sample_background(img):
    """Estimate the dominant background color from the border strips."""
    w, h = img.size
    pixels = img.load()
    samples = Counter()
    step = max(1, min(w, h) // 120)

    for x in range(0, w, step):
        samples[pixels[x, 0]] += 1
        samples[pixels[x, h - 1]] += 1
    for y in range(0, h, step):
        samples[pixels[0, y]] += 1
        samples[pixels[w - 1, y]] += 1

    # Quantize to reduce noise from antialiasing.
    quantized = Counter()
    for (r, g, b), count in samples.items():
        quantized[(r // 8 * 8, g // 8 * 8, b // 8 * 8)] += count
    (qr, qg, qb), _ = quantized.most_common(1)[0]
    return (qr + 4, qg + 4, qb + 4)


def make_foreground_mask(img, bg, tolerance):
    """Return a Pillow 'L' mask: 255 where the pixel differs from bg by > tolerance."""
    bg_img = Image.new("RGB", img.size, bg)
    diff = ImageChops.difference(img, bg_img).convert("L")
    return diff.point(lambda p: 255 if p > tolerance else 0)


def column_ink_counts(mask):
    w, h = mask.size
    data = mask.tobytes()
    counts = [0] * w
    for y in range(h):
        row = y * w
        for x in range(w):
            if data[row + x]:
                counts[x] += 1
    return counts


def row_ink_counts(mask):
    w, h = mask.size
    data = mask.tobytes()
    counts = [0] * h
    for y in range(h):
        row = y * w
        total = 0
        for x in range(w):
            if data[row + x]:
                total += 1
        counts[y] = total
    return counts


def row_runs(mask, y):
    """Return (first_x, last_x) of foreground pixels in row y, or None."""
    w, _ = mask.size
    data = mask.tobytes()
    row = y * w
    first = None
    last = None
    for x in range(w):
        if data[row + x]:
            if first is None:
                first = x
            last = x
    if first is None:
        return None
    return first, last


def detect_dividers(mask, min_line_ratio):
    """Detect horizontal divider-like bands using row ink coverage."""
    w, h = mask.size
    rows = row_ink_counts(mask)
    min_count = max(int(w * min_line_ratio), 60)
    candidates = []
    y = 0
    while y < h:
        if rows[y] < min_count:
            y += 1
            continue
        start = y
        while y < h and rows[y] >= min_count:
            y += 1
        end = y - 1
        height = end - start + 1
        if height > 6:
            continue
        # Pick the row with the widest run in the band.
        best = None
        for yy in range(start, end + 1):
            run = row_runs(mask, yy)
            if not run:
                continue
            if best is None or (run[1] - run[0]) > (best[1] - best[0]):
                best = run
        if not best:
            continue
        x1, x2 = best
        candidates.append({
            "y": start,
            "height": height,
            "x1": x1,
            "x2": x2,
            "span": x2 - x1 + 1,
        })
    # Merge candidates on adjacent y with similar spans.
    merged = []
    for c in candidates:
        placed = False
        for m in merged:
            if abs(m["y"] - c["y"]) <= 4 and abs(m["x1"] - c["x1"]) <= 8 and abs(m["x2"] - c["x2"]) <= 8:
                m["y"] = min(m["y"], c["y"])
                m["x1"] = min(m["x1"], c["x1"])
                m["x2"] = max(m["x2"], c["x2"])
                m["span"] = m["x2"] - m["x1"] + 1
                m["height"] = max(m["height"], c["height"])
                placed = True
                break
        if not placed:
            merged.append(dict(c))
    return merged


def analyze_single(image_path, out_path, json_path, tolerance, min_line_ratio, header_height, theme, quiet):
    img = Image.open(image_path).convert("RGB")
    w, h = img.size

    bg = sample_background(img)
    mask = make_foreground_mask(img, bg, tolerance)

    findings = []
    annotated = img.copy()
    draw = ImageDraw.Draw(annotated)

    # Page center guide.
    center_x = w // 2
    for y in range(0, h, 16):
        draw.line([(center_x, y), (center_x, min(y + 8, h - 1))], fill=(0, 180, 90), width=1)

    # 1. Outer margin symmetry.
    cols = column_ink_counts(mask)
    ink_cols = [i for i, c in enumerate(cols) if c > max(3, int(h * 0.002))]
    if ink_cols:
        left_margin = ink_cols[0]
        right_margin = (w - 1) - ink_cols[-1]
        margin_delta = abs(left_margin - right_margin)
        if margin_delta > 4 and left_margin > 8 and right_margin > 8:
            findings.append({
                "id": "PIX-MARGIN-001",
                "severity": "P1" if margin_delta > 12 else "P2",
                "category": "visual-margin-asymmetry",
                "evidence": {
                    "leftMarginPx": left_margin,
                    "rightMarginPx": right_margin,
                    "deltaPx": margin_delta,
                    "canvasWidthPx": w,
                },
                "rootCause": f"Rendered content bounding box has uneven outer margins (left {left_margin}px vs right {right_margin}px).",
            })
            draw.line([(left_margin, 0), (left_margin, h)], fill=(255, 60, 60), width=2)
            draw.line([(w - 1 - right_margin, 0), (w - 1 - right_margin, h)], fill=(255, 60, 60), width=2)

    # 2. Top-band optical centering.
    band_h = min(header_height, h)
    band_l = int(w * 0.30)
    band_r = int(w * 0.70)
    band = mask.crop((band_l, 0, band_r, band_h))
    bbox = band.getbbox()
    if bbox:
        ys, xs = [], []
        data = band.tobytes()
        bw, bh = band.size
        for y in range(bh):
            base = y * bw
            for x in range(bw):
                if data[base + x]:
                    xs.append(x)
                    ys.append(y)
        if len(xs) > 30:
            optical_x = band_l + (sum(xs) / len(xs))
            bbox_center_x = band_l + (min(xs) + max(xs)) / 2.0
            delta_optical = round(optical_x - (w / 2.0), 2)
            delta_bbox = round(bbox_center_x - (w / 2.0), 2)
            if abs(delta_bbox) > 2.5 or abs(delta_optical) > 4.0:
                findings.append({
                    "id": "PIX-HEADER-CTR-001",
                    "severity": "P1" if abs(delta_bbox) > 4.0 else "P3",
                    "category": "header-optical-centering-drift",
                    "evidence": {
                        "bandXPx": [band_l, band_r],
                        "bandHeightPx": band_h,
                        "deltaBBoxPx": delta_bbox,
                        "deltaOpticalPx": delta_optical,
                    },
                    "rootCause": f"Top header center element is visually shifted by {delta_bbox}px (bbox) / {delta_optical}px (optical center-of-mass).",
                })
                x1, y1, x2, y2 = bbox
                draw.rectangle(
                    [band_l + x1 - 3, y1 - 3, band_l + x2 + 3, y2 + 3],
                    outline=(255, 50, 50),
                    width=2,
                )

    # 3. Horizontal divider detection.
    dividers = detect_dividers(mask, min_line_ratio)
    div_idx = 1
    for d in dividers:
        span = d["x2"] - d["x1"] + 1
        left_gap = d["x1"]
        right_gap = (w - 1) - d["x2"]
        asymmetry = abs(left_gap - right_gap)
        fill_ratio = span / float(w)
        if asymmetry > 6 or (0.78 <= fill_ratio <= 0.992 and (left_gap > 2 or right_gap > 2)):
            findings.append({
                "id": f"PIX-DIV-{div_idx:03d}",
                "severity": "P1" if asymmetry > 10 else "P2",
                "category": "pixel-divider-incomplete-or-asymmetric",
                "evidence": {
                    "yPx": d["y"],
                    "xStartPx": d["x1"],
                    "xEndPx": d["x2"],
                    "spanPx": span,
                    "canvasWidthPx": w,
                    "leftGapPx": left_gap,
                    "rightGapPx": right_gap,
                    "asymmetryPx": asymmetry,
                    "fillRatio": round(fill_ratio, 3),
                },
                "rootCause": (
                    f"Divider spans {span}px of {w}px canvas ({fill_ratio * 100:.1f}%), "
                    f"with left gap {left_gap}px and right gap {right_gap}px."
                ),
            })
            draw.line([(d["x1"], d["y"]), (d["x2"], d["y"])], fill=(255, 140, 0), width=2)
            div_idx += 1

    annotated.save(out_path)

    report = {
        "image": str(image_path),
        "dimensions": f"{w}x{h}",
        "background": list(bg),
        "theme": theme,
        "totalFindings": len(findings),
        "findings": findings,
        "annotatedOutput": str(out_path),
    }
    if json_path:
        Path(json_path).write_text(json.dumps(report, indent=2), encoding="utf-8")

    if not quiet:
        print(f"Pixel Precision Audit complete: {len(findings)} finding(s) detected.")
        if json_path:
            print(f"Report saved -> {json_path}")
        print(f"Annotated image -> {out_path}")

    return report


def analyze_diff(before_path, after_path, out_path, diff_tolerance, quiet):
    before = Image.open(before_path).convert("RGB")
    after = Image.open(after_path).convert("RGB")

    if before.size != after.size:
        if not quiet:
            print(f"Warning: size mismatch {before.size} vs {after.size}; resizing after to before.", file=sys.stderr)
        after = after.resize(before.size, Image.LANCZOS)

    diff = ImageChops.difference(before, after)
    gray = diff.convert("L")
    changed = gray.point(lambda p: 255 if p > diff_tolerance else 0)
    bbox = changed.getbbox()

    hist = gray.histogram()
    total = before.size[0] * before.size[1]
    changed_pixels = sum(hist[diff_tolerance + 1:])
    percent = (changed_pixels / total) * 100.0 if total else 0.0

    # Visualize: dim the before image, then highlight changed pixels in red.
    base = before.copy()
    base = Image.blend(base, Image.new("RGB", base.size, (255, 255, 255)), 0.55)
    red = Image.new("RGB", base.size, (220, 30, 30))
    base.paste(red, (0, 0), changed)
    draw = ImageDraw.Draw(base)
    if bbox:
        draw.rectangle(bbox, outline=(0, 120, 255), width=2)
    base.save(out_path)

    report = {
        "before": str(before_path),
        "after": str(after_path),
        "comparedDimensions": f"{before.size[0]}x{before.size[1]}",
        "changedPixelPercent": round(percent, 3),
        "changedBoundingBox": list(bbox) if bbox else None,
        "diffOutput": str(out_path),
    }
    if not quiet:
        print(json.dumps(report, indent=2))
    return report


def main():
    args = parse_args(sys.argv[1:])
    try:
        if args.before and args.after:
            report = analyze_diff(args.before, args.after, args.out, args.diff_tolerance, args.quiet)
        else:
            report = analyze_single(
                args.image,
                args.out,
                args.json,
                args.tolerance,
                args.min_line_ratio,
                args.header_height,
                args.theme,
                args.quiet,
            )
        if args.json and not (args.before and args.after):
            Path(args.json).write_text(json.dumps(report, indent=2), encoding="utf-8")
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
