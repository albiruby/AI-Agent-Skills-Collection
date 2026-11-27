#!/usr/bin/env python3
"""
Clean Device & App Screenshot Slicer
------------------------------------
Converts raw simulator/emulator/window screenshots (for example Garmin Connect IQ
Simulator captures with OS title bars, menu bars, white canvas, and status bars)
into clean, chrome-free, transparent-background RGBA PNG assets.

Dependencies: Pillow (required), numpy (optional, auto-fallback to pure Pillow).
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import os
from pathlib import Path
from typing import Iterable, Tuple

from PIL import Image, ImageDraw, ImageFilter

try:
    import numpy as np  # type: ignore

    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


SUPPORTED_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}


def parse_hex_color(hex_str: str) -> Tuple[int, int, int]:
    cleaned = hex_str.strip().lstrip("#")
    if len(cleaned) != 6:
        raise ValueError(f"Expected 6-digit hex color, got: {hex_str}")
    return (int(cleaned[0:2], 16), int(cleaned[2:4], 16), int(cleaned[4:6], 16))


def detect_garmin_chrome_bounds(img: Image.Image) -> Tuple[int, int, int, int]:
    """
    Auto-detects the inner white canvas region of a Garmin Connect IQ Simulator window
    by scanning rows from top and bottom to skip OS title bar, menu bar, and status bar.
    Returns (left, top, right, bottom) crop box.
    """
    rgb = img.convert("RGB")
    w, h = rgb.size
    px = rgb.load()

    def row_white_ratio(y: int) -> float:
        step = max(1, w // 120)
        white = 0
        total = 0
        for x in range(int(w * 0.05), int(w * 0.95), step):
            r, g, b = px[x, y]
            if r >= 242 and g >= 242 and b >= 242:
                white += 1
            total += 1
        return white / max(1, total)

    def col_white_ratio(x: int, y0: int, y1: int) -> float:
        step = max(1, (y1 - y0) // 120)
        white = 0
        total = 0
        for y in range(y0, y1, step):
            r, g, b = px[x, y]
            if r >= 242 and g >= 242 and b >= 242:
                white += 1
            total += 1
        return white / max(1, total)

    # Find first row below title+menu bar where white canvas begins (high white ratio)
    # Usually CIQ Simulator has ~50-90px of top chrome (title bar + menu bar)
    top = 0
    for y in range(0, int(h * 0.28)):
        # A row inside the white simulator canvas has white left & right margins
        left_r, left_g, left_b = px[int(w * 0.08), y]
        right_r, right_g, right_b = px[int(w * 0.92), y]
        is_white_margins = (
            left_r >= 244 and left_g >= 244 and left_b >= 244
            and right_r >= 244 and right_g >= 244 and right_b >= 244
        )
        if is_white_margins and row_white_ratio(y) >= 0.40:
            # Verify next 6 rows are also white-margin canvas (skip thin white divider lines)
            if y + 6 < h:
                ok = True
                for dy in range(1, 7):
                    lr, lg, lb = px[int(w * 0.08), y + dy]
                    rr, rg, rb = px[int(w * 0.92), y + dy]
                    if not (lr >= 240 and lg >= 240 and lb >= 240 and rr >= 240 and rg >= 240 and rb >= 240):
                        ok = False
                        break
                if ok:
                    top = y
                    break

    # Find bottom row above status bar
    bottom = h
    for y in range(h - 1, int(h * 0.72), -1):
        left_r, left_g, left_b = px[int(w * 0.08), y]
        right_r, right_g, right_b = px[int(w * 0.92), y]
        is_white_margins = (
            left_r >= 244 and left_g >= 244 and left_b >= 244
            and right_r >= 244 and right_g >= 244 and right_b >= 244
        )
        if is_white_margins and row_white_ratio(y) >= 0.40:
            if y - 6 > top:
                ok = True
                for dy in range(1, 7):
                    lr, lg, lb = px[int(w * 0.08), y - dy]
                    rr, rg, rb = px[int(w * 0.92), y - dy]
                    if not (lr >= 240 and lg >= 240 and lb >= 240 and rr >= 240 and rg >= 240 and rb >= 240):
                        ok = False
                        break
                if ok:
                    bottom = y + 1
                    break

    # Trim dark window borders on left & right if present
    left = 0
    for x in range(0, int(w * 0.15)):
        if col_white_ratio(x, top, bottom) >= 0.70:
            left = x
            break

    right = w
    for x in range(w - 1, int(w * 0.85), -1):
        if col_white_ratio(x, top, bottom) >= 0.70:
            right = x + 1
            break

    # Safety fallback if detection collapsed
    if (right - left) < w * 0.4 or (bottom - top) < h * 0.4:
        return (0, 0, w, h)
    return (left, top, right, bottom)


def sample_border_bg_color(img: Image.Image) -> Tuple[int, int, int]:
    """Samples the median color along the outer 4 corners to identify background color."""
    rgb = img.convert("RGB")
    w, h = rgb.size
    px = rgb.load()
    pts = [
        (2, 2), (w - 3, 2), (2, h - 3), (w - 3, h - 3),
        (w // 2, 2), (w // 2, h - 3), (2, h // 2), (w - 3, h // 2),
    ]
    samples = [px[max(0, min(w - 1, x)), max(0, min(h - 1, y))] for x, y in pts]
    rs = sorted(c[0] for c in samples)
    gs = sorted(c[1] for c in samples)
    bs = sorted(c[2] for c in samples)
    mid = len(samples) // 2
    return (rs[mid], gs[mid], bs[mid])


def flood_fill_remove_bg(
    img: Image.Image,
    bg_color: Tuple[int, int, int],
    tolerance: int = 28,
    defringe: bool = True,
) -> Image.Image:
    """
    Removes exterior background connected to image borders using BFS flood fill.
    Preserves interior pixels of the same color (e.g. white text inside a watch screen).
    Applies optional 1-2px alpha fringe cleanup to eliminate bright halos on dark bezels.
    """
    rgba = img.convert("RGBA")
    w, h = rgba.size
    br, bg, bb = bg_color
    tol_sq = tolerance * tolerance * 3

    if HAS_NUMPY:
        arr = np.array(rgba, dtype=np.int16)
        dr = arr[:, :, 0] - br
        dg = arr[:, :, 1] - bg
        db = arr[:, :, 2] - bb
        dist_sq = dr * dr + dg * dg + db * db
        is_bg_candidate = (dist_sq <= tol_sq) | (arr[:, :, 3] < 10)
    else:
        px = rgba.load()
        is_bg_candidate = [[False] * w for _ in range(h)]
        for y in range(h):
            row = is_bg_candidate[y]
            for x in range(w):
                r, g, b, a = px[x, y]
                if a < 10 or ((r - br) ** 2 + (g - bg) ** 2 + (b - bb) ** 2) <= tol_sq:
                    row[x] = True

    visited = [[False] * w for _ in range(h)]
    queue = collections.deque()

    # Seed all 4 borders
    for x in range(w):
        for y in (0, h - 1):
            if is_bg_candidate[y][x] and not visited[y][x]:
                visited[y][x] = True
                queue.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if is_bg_candidate[y][x] and not visited[y][x]:
                visited[y][x] = True
                queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()
        if cx > 0 and not visited[cy][cx - 1] and is_bg_candidate[cy][cx - 1]:
            visited[cy][cx - 1] = True
            queue.append((cx - 1, cy))
        if cx + 1 < w and not visited[cy][cx + 1] and is_bg_candidate[cy][cx + 1]:
            visited[cy][cx + 1] = True
            queue.append((cx + 1, cy))
        if cy > 0 and not visited[cy - 1][cx] and is_bg_candidate[cy - 1][cx]:
            visited[cy - 1][cx] = True
            queue.append((cx, cy - 1))
        if cy + 1 < h and not visited[cy + 1][cx] and is_bg_candidate[cy + 1][cx]:
            visited[cy + 1][cx] = True
            queue.append((cx, cy + 1))

    out = rgba.copy()
    out_px = out.load()
    for y in range(h):
        vrow = visited[y]
        for x in range(w):
            if vrow[x]:
                out_px[x, y] = (0, 0, 0, 0)

    if defringe:
        # Soften 1px anti-alias boundary pixels that still lean strongly toward bg_color
        soft_tol_sq = (tolerance * 2.2) ** 2 * 3
        edge_updates = []
        for y in range(1, h - 1):
            for x in range(1, w - 1):
                if visited[y][x]:
                    continue
                if visited[y - 1][x] or visited[y + 1][x] or visited[y][x - 1] or visited[y][x + 1]:
                    r, g, b, a = out_px[x, y]
                    d_sq = (r - br) ** 2 + (g - bg) ** 2 + (b - bb) ** 2
                    if d_sq <= soft_tol_sq:
                        ratio = math.sqrt(d_sq / max(1.0, soft_tol_sq))
                        new_a = int(a * min(1.0, ratio * 0.85))
                        # Darken slightly away from bright white bg to avoid white halo
                        if br > 200 and bg > 200 and bb > 200 and new_a > 0:
                            r = max(0, int((r - br * (1.0 - ratio)) / max(0.25, ratio)))
                            g = max(0, int((g - bg * (1.0 - ratio)) / max(0.25, ratio)))
                            b = max(0, int((b - bb * (1.0 - ratio)) / max(0.25, ratio)))
                            r, g, b = min(255, r), min(255, g), min(255, b)
                        edge_updates.append((x, y, (r, g, b, new_a)))
        for x, y, val in edge_updates:
            out_px[x, y] = val

    return out


def apply_viewport_card(img: Image.Image, radius: int = 24, shadow: int = 24) -> Image.Image:
    """Wraps a clean web/mobile viewport screenshot with rounded corners and soft drop shadow."""
    rgba = img.convert("RGBA")
    w, h = rgba.size
    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), (w - 1, h - 1)], radius=radius, fill=255)
    rounded = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    rounded.paste(rgba, (0, 0), mask)

    if shadow <= 0:
        return rounded

    pad = shadow * 2
    canvas = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    shadow_layer = Image.new("RGBA", (w + pad * 2, h + pad * 2), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_layer)
    s_draw.rounded_rectangle(
        [(pad, pad + shadow // 3), (pad + w - 1, pad + h - 1 + shadow // 3)],
        radius=radius,
        fill=(0, 0, 0, 110),
    )
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=shadow * 0.7))
    canvas = Image.alpha_composite(canvas, shadow_layer)
    canvas.paste(rounded, (pad, pad), rounded)
    return canvas


def tight_crop_alpha(img: Image.Image, padding: int = 8) -> Image.Image:
    """Crops an RGBA image tightly around non-transparent pixels with uniform padding."""
    bbox = img.getbbox()
    if not bbox:
        return img
    cropped = img.crop(bbox)
    if padding <= 0:
        return cropped
    cw, ch = cropped.size
    out = Image.new("RGBA", (cw + padding * 2, ch + padding * 2), (0, 0, 0, 0))
    out.paste(cropped, (padding, padding), cropped)
    return out


def process_image(
    src_path: Path,
    dst_path: Path,
    preset: str,
    crop_top: int,
    crop_bottom: int,
    crop_left: int,
    crop_right: int,
    bg_hex: str | None,
    tolerance: int,
    padding: int,
    target_height: int | None,
    radius: int,
) -> dict:
    img = Image.open(src_path)
    orig_w, orig_h = img.size

    # 1. Chrome stripping
    if preset == "garmin-sim" and crop_top == 0 and crop_bottom == 0 and crop_left == 0 and crop_right == 0:
        box = detect_garmin_chrome_bounds(img)
        img = img.crop(box)
    elif any((crop_top, crop_bottom, crop_left, crop_right)):
        img = img.crop((
            crop_left,
            crop_top,
            max(crop_left + 1, orig_w - crop_right),
            max(crop_top + 1, orig_h - crop_bottom),
        ))

    # 2. Background slicing or viewport framing
    if preset in ("garmin-sim", "window-clean", "chroma-key"):
        if bg_hex:
            bg_color = parse_hex_color(bg_hex)
        elif preset == "chroma-key":
            bg_color = (0, 255, 0)
        else:
            bg_color = sample_border_bg_color(img)
        img = flood_fill_remove_bg(img, bg_color=bg_color, tolerance=tolerance, defringe=True)
        img = tight_crop_alpha(img, padding=padding)
    elif preset == "viewport-card":
        img = apply_viewport_card(img, radius=radius, shadow=20)
    else:
        img = img.convert("RGBA")

    # 3. Optional height normalization for consistent multi-device layouts
    if target_height and target_height > 0 and img.height > 0:
        scale = target_height / float(img.height)
        new_w = max(1, int(round(img.width * scale)))
        img = img.resize((new_w, target_height), Image.Resampling.LANCZOS)

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    final_path = dst_path.with_suffix(".png")
    img.save(final_path, format="PNG", optimize=True)

    # Compute QA metrics
    alpha_band = img.getchannel("A")
    alpha_hist = alpha_band.histogram()
    total_px = img.width * img.height
    transparent_px = alpha_hist[0]
    transparent_ratio = round(transparent_px / max(1, total_px), 3)
    corners = [
        img.getpixel((0, 0))[3],
        img.getpixel((img.width - 1, 0))[3],
        img.getpixel((0, img.height - 1))[3],
        img.getpixel((img.width - 1, img.height - 1))[3],
    ]

    return {
        "source": str(src_path),
        "output": str(final_path),
        "input_size": [orig_w, orig_h],
        "output_size": [img.width, img.height],
        "transparent_ratio": transparent_ratio,
        "corners_transparent": all(c == 0 for c in corners),
    }


def iter_inputs(input_path: Path) -> Iterable[Path]:
    if input_path.is_file():
        yield input_path
    elif input_path.is_dir():
        for p in sorted(input_path.iterdir()):
            if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS:
                yield p
    else:
        raise FileNotFoundError(f"Input path not found: {input_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Slice raw simulator/emulator/app screenshots into clean transparent PNGs."
    )
    parser.add_argument("--input", required=True, help="Input image file or directory")
    parser.add_argument("--output", required=True, help="Output PNG file or directory")
    parser.add_argument(
        "--preset",
        choices=["garmin-sim", "window-clean", "chroma-key", "viewport-card"],
        default="garmin-sim",
        help="Slicing preset (default: garmin-sim)",
    )
    parser.add_argument("--crop-top", type=int, default=0, help="Manual top chrome crop in pixels")
    parser.add_argument("--crop-bottom", type=int, default=0, help="Manual bottom chrome crop in pixels")
    parser.add_argument("--crop-left", type=int, default=0, help="Manual left border crop in pixels")
    parser.add_argument("--crop-right", type=int, default=0, help="Manual right border crop in pixels")
    parser.add_argument("--bg-color", default=None, help="Override background hex color (e.g. #FFFFFF or #00FF00)")
    parser.add_argument("--tolerance", type=int, default=28, help="Color distance tolerance for flood fill (default: 28)")
    parser.add_argument("--padding", type=int, default=8, help="Transparent padding around sliced object (default: 8)")
    parser.add_argument("--target-height", type=int, default=None, help="Normalize output height in px (preserves aspect)")
    parser.add_argument("--radius", type=int, default=24, help="Corner radius for viewport-card preset (default: 24)")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)
    results = []

    for src in iter_inputs(in_path):
        if in_path.is_dir():
            dst = out_path / (src.stem + ".png")
        else:
            dst = out_path if out_path.suffix.lower() == ".png" else out_path / (src.stem + ".png")
        res = process_image(
            src_path=src,
            dst_path=dst,
            preset=args.preset,
            crop_top=args.crop_top,
            crop_bottom=args.crop_bottom,
            crop_left=args.crop_left,
            crop_right=args.crop_right,
            bg_hex=args.bg_color,
            tolerance=args.tolerance,
            padding=args.padding,
            target_height=args.target_height,
            radius=args.radius,
        )
        results.append(res)

    print(json.dumps({"processed": len(results), "files": results}, indent=2))


if __name__ == "__main__":
    main()
