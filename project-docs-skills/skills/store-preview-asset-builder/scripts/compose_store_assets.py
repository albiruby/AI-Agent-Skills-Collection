#!/usr/bin/env python3
"""
Store & Preview Visual Asset Compositor
---------------------------------------
Renders publication-ready store Covers, Hero Banners, Multi-Device Feature Showcases,
Web/GitHub OG banners, and Mobile Store Panels from a declarative JSON manifest
and clean transparent device/app screenshots.

Outputs both lossless master PNGs (in <output-dir>/master/) and store-ready
optimized JPG/PNG files (in <output-dir>/).

Dependencies: Pillow (required).
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import List, Optional, Tuple

from PIL import Image, ImageDraw, ImageFilter, ImageFont


DEFAULT_FONT_CANDIDATES_BOLD = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
    "C:/Windows/Fonts/segoeuib.ttf",
]

DEFAULT_FONT_CANDIDATES_REGULAR = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
    "C:/Windows/Fonts/segoeui.ttf",
]


def hex_to_rgb(hex_str: str) -> Tuple[int, int, int]:
    s = hex_str.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))


def load_font(custom_path: Optional[str], size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = []
    if custom_path:
        candidates.append(custom_path)
    candidates.extend(DEFAULT_FONT_CANDIDATES_BOLD if bold else DEFAULT_FONT_CANDIDATES_REGULAR)
    for path in candidates:
        if path and os.path.isfile(path):
            try:
                return ImageFont.truetype(path, size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def make_vertical_gradient(w: int, h: int, top_hex: str, bottom_hex: str) -> Image.Image:
    r1, g1, b1 = hex_to_rgb(top_hex)
    r2, g2, b2 = hex_to_rgb(bottom_hex)
    grad = Image.new("RGBA", (w, h))
    draw = ImageDraw.Draw(grad)
    denom = max(1, h - 1)
    for y in range(h):
        t = y / denom
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b, 255))
    return grad


def draw_decorative_accents(canvas: Image.Image, accent_hex: str, style: str = "pixel-squares") -> None:
    if style == "none":
        return
    w, h = canvas.size
    draw = ImageDraw.Draw(canvas)
    ar, ag, ab = hex_to_rgb(accent_hex)
    color = (ar, ag, ab, 150)

    # Subtle framing geometric accents positioned safely near margins
    positions = [
        (int(w * 0.06), int(h * 0.36), 16),
        (int(w * 0.05), int(h * 0.72), 14),
        (int(w * 0.93), int(h * 0.28), 18),
        (int(w * 0.91), int(h * 0.68), 15),
    ]
    for x, y, sz in positions:
        if style == "dots":
            draw.ellipse([(x, y), (x + sz, y + sz)], outline=color, width=2)
        else:
            draw.rectangle([(x, y), (x + sz, y + sz)], outline=color, width=2)


def add_drop_shadow(img: Image.Image, offset: Tuple[int, int] = (0, 14), blur: int = 18, alpha: int = 130) -> Tuple[Image.Image, Tuple[int, int]]:
    rgba = img.convert("RGBA")
    pad = blur * 2 + max(abs(offset[0]), abs(offset[1]))
    sw = rgba.width + pad * 2
    sh = rgba.height + pad * 2
    shadow = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    alpha_mask = rgba.getchannel("A")
    black_sil = Image.new("RGBA", rgba.size, (0, 0, 0, alpha))
    shadow.paste(black_sil, (pad + offset[0], pad + offset[1]), alpha_mask)
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=blur))
    shadow.paste(rgba, (pad, pad), rgba)
    return shadow, (pad, pad)


def fit_image(path: Path, max_w: int, max_h: int) -> Image.Image:
    im = Image.open(path).convert("RGBA")
    scale = min(max_w / max(1, im.width), max_h / max(1, im.height))
    nw = max(1, int(round(im.width * scale)))
    nh = max(1, int(round(im.height * scale)))
    return im.resize((nw, nh), Image.Resampling.LANCZOS)


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> List[str]:
    if not text:
        return []
    words = text.split()
    lines: List[str] = []
    cur: List[str] = []
    for word in words:
        trial = " ".join(cur + [word])
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] <= max_width or not cur:
            cur.append(word)
        else:
            lines.append(" ".join(cur))
            cur = [word]
    if cur:
        lines.append(" ".join(cur))
    return lines


def draw_centered_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    cx: int,
    y: int,
    font: ImageFont.ImageFont,
    fill: Tuple[int, int, int, int],
    max_width: int,
    line_gap: int = 6,
) -> int:
    lines = wrap_text(draw, text, font, max_width)
    cur_y = y
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((cx - tw // 2, cur_y), line, font=font, fill=fill)
        cur_y += th + line_gap
    return cur_y


def render_cover(spec: dict, theme: dict, base_dir: Path) -> Image.Image:
    w, h = spec.get("width", 500), spec.get("height", 500)
    canvas = make_vertical_gradient(w, h, theme["bg_top"], theme["bg_bottom"])
    draw_decorative_accents(canvas, theme["accent"], theme.get("decor", "pixel-squares"))
    draw = ImageDraw.Draw(canvas)

    images = spec.get("images", [])
    if images:
        dev = fit_image((base_dir / images[0]["src"]).resolve(), int(w * 0.68), int(h * 0.68))
        shadowed, pad = add_drop_shadow(dev, offset=(0, 10), blur=14, alpha=140)
        x = (w - dev.width) // 2 - pad[0]
        y = int(h * 0.04) - pad[1]
        canvas.alpha_composite(shadowed, (x, y))

    title_font = load_font(theme.get("font_bold"), max(24, int(h * 0.095)), bold=True)
    sub_font = load_font(theme.get("font_regular"), max(12, int(h * 0.036)), bold=False)

    ty = int(h * 0.77)
    ty = draw_centered_text(draw, spec.get("title", ""), w // 2, ty, title_font, (*hex_to_rgb(theme["title_color"]), 255), int(w * 0.90))
    if spec.get("subtitle"):
        draw_centered_text(draw, spec["subtitle"], w // 2, ty + 4, sub_font, (*hex_to_rgb(theme["subtitle_color"]), 255), int(w * 0.90))
    return canvas


def render_hero_overlap(spec: dict, theme: dict, base_dir: Path) -> Image.Image:
    w, h = spec.get("width", 1440), spec.get("height", 720)
    canvas = make_vertical_gradient(w, h, theme["bg_top"], theme["bg_bottom"])
    draw_decorative_accents(canvas, theme["accent"], theme.get("decor", "pixel-squares"))

    images = spec.get("images", [])
    left_zone_w = int(w * 0.56)
    center_x = int(left_zone_w * 0.49)
    center_y = int(h * 0.51)

    if len(images) >= 3:
        # Draw left & right recessed devices first, then center foreground device on top
        side_h = int(h * 0.80)
        main_h = int(h * 0.88)
        left_im = fit_image((base_dir / images[0]["src"]).resolve(), int(left_zone_w * 0.52), side_h)
        mid_im = fit_image((base_dir / images[1]["src"]).resolve(), int(left_zone_w * 0.56), main_h)
        right_im = fit_image((base_dir / images[2]["src"]).resolve(), int(left_zone_w * 0.52), side_h)

        spread = int(mid_im.width * 0.58)
        for im, dx, blur in [(left_im, -spread, 14), (right_im, spread, 14), (mid_im, 0, 20)]:
            sh, pad = add_drop_shadow(im, offset=(0, 12), blur=blur, alpha=160)
            px = center_x + dx - im.width // 2 - pad[0]
            py = center_y - im.height // 2 - pad[1]
            canvas.alpha_composite(sh, (px, py))
    elif len(images) == 2:
        dev_h = int(h * 0.82)
        im0 = fit_image((base_dir / images[0]["src"]).resolve(), int(left_zone_w * 0.55), dev_h)
        im1 = fit_image((base_dir / images[1]["src"]).resolve(), int(left_zone_w * 0.55), dev_h)
        spread = int(im0.width * 0.42)
        for im, dx in [(im0, -spread), (im1, spread)]:
            sh, pad = add_drop_shadow(im, offset=(0, 12), blur=16, alpha=150)
            canvas.alpha_composite(sh, (center_x + dx - im.width // 2 - pad[0], center_y - im.height // 2 - pad[1]))
    elif len(images) == 1:
        im0 = fit_image((base_dir / images[0]["src"]).resolve(), int(left_zone_w * 0.86), int(h * 0.82))
        sh, pad = add_drop_shadow(im0, offset=(0, 14), blur=18, alpha=150)
        canvas.alpha_composite(sh, (center_x - im0.width // 2 - pad[0], center_y - im0.height // 2 - pad[1]))

    # Right text block
    draw = ImageDraw.Draw(canvas)
    tx = int(w * 0.59)
    max_tw = int(w * 0.36)
    eyebrow_font = load_font(theme.get("font_regular"), max(16, int(h * 0.030)), bold=False)
    title_font = load_font(theme.get("font_bold"), max(38, int(h * 0.110)), bold=True)
    sub_font = load_font(theme.get("font_regular"), max(20, int(h * 0.044)), bold=False)
    meta_font = load_font(theme.get("font_bold"), max(16, int(h * 0.030)), bold=True)
    meta2_font = load_font(theme.get("font_regular"), max(15, int(h * 0.028)), bold=False)

    cur_y = int(h * 0.24)
    if spec.get("eyebrow"):
        draw.text((tx, cur_y), spec["eyebrow"].upper(), font=eyebrow_font, fill=(*hex_to_rgb(theme["muted_color"]), 255))
        cur_y += int(h * 0.055)

    for line in wrap_text(draw, spec.get("title", ""), title_font, max_tw):
        draw.text((tx, cur_y), line, font=title_font, fill=(*hex_to_rgb(theme["title_color"]), 255))
        bbox = draw.textbbox((0, 0), line, font=title_font)
        cur_y += (bbox[3] - bbox[1]) + 12

    cur_y += 10
    if spec.get("subtitle"):
        for line in wrap_text(draw, spec["subtitle"], sub_font, max_tw):
            draw.text((tx, cur_y), line, font=sub_font, fill=(*hex_to_rgb(theme["subtitle_color"]), 255))
            bbox = draw.textbbox((0, 0), line, font=sub_font)
            cur_y += (bbox[3] - bbox[1]) + 8

    cur_y += 18
    if spec.get("highlight"):
        for line in wrap_text(draw, spec["highlight"], meta_font, max_tw):
            draw.text((tx, cur_y), line, font=meta_font, fill=(*hex_to_rgb(theme["caption_color"]), 255))
            bbox = draw.textbbox((0, 0), line, font=meta_font)
            cur_y += (bbox[3] - bbox[1]) + 8

    if spec.get("meta"):
        for line in wrap_text(draw, spec["meta"], meta2_font, max_tw):
            draw.text((tx, cur_y), line, font=meta2_font, fill=(*hex_to_rgb(theme["muted_color"]), 255))
            bbox = draw.textbbox((0, 0), line, font=meta2_font)
            cur_y += (bbox[3] - bbox[1]) + 6

    return canvas


def render_feature_showcase(spec: dict, theme: dict, base_dir: Path) -> Image.Image:
    w, h = spec.get("width", 1440), spec.get("height", 900)
    canvas = make_vertical_gradient(w, h, theme["bg_top"], theme["bg_bottom"])
    draw_decorative_accents(canvas, theme["accent"], theme.get("decor", "pixel-squares"))
    draw = ImageDraw.Draw(canvas)

    eyebrow_font = load_font(theme.get("font_regular"), max(16, int(h * 0.024)), bold=False)
    title_font = load_font(theme.get("font_bold"), max(34, int(h * 0.062)), bold=True)
    sub_font = load_font(theme.get("font_regular"), max(18, int(h * 0.028)), bold=False)
    cap_font = load_font(theme.get("font_bold"), max(18, int(h * 0.028)), bold=True)

    cur_y = int(h * 0.05)
    if spec.get("eyebrow"):
        cur_y = draw_centered_text(draw, spec["eyebrow"].upper(), w // 2, cur_y, eyebrow_font, (*hex_to_rgb(theme["muted_color"]), 255), int(w * 0.84))
        cur_y += 6

    cur_y = draw_centered_text(draw, spec.get("title", ""), w // 2, cur_y, title_font, (*hex_to_rgb(theme["title_color"]), 255), int(w * 0.88))
    cur_y += 8

    if spec.get("subtitle"):
        cur_y = draw_centered_text(draw, spec["subtitle"], w // 2, cur_y, sub_font, (*hex_to_rgb(theme["subtitle_color"]), 255), int(w * 0.84))

    images = spec.get("images", [])
    n = len(images)
    if n > 0:
        margin_x = int(w * 0.08)
        usable_w = w - margin_x * 2
        gap = int(w * 0.03)
        slot_w = (usable_w - gap * (n - 1)) // n
        top_y = max(cur_y + 24, int(h * 0.24))
        caption_band = int(h * 0.11)
        max_dev_h = max(100, h - top_y - caption_band)

        for idx, item in enumerate(images):
            cx = margin_x + idx * (slot_w + gap) + slot_w // 2
            im = fit_image((base_dir / item["src"]).resolve(), slot_w, max_dev_h)
            sh, pad = add_drop_shadow(im, offset=(0, 14), blur=16, alpha=145)
            px = cx - im.width // 2 - pad[0]
            py = top_y + (max_dev_h - im.height) // 2 - pad[1]
            canvas.alpha_composite(sh, (px, py))

            if item.get("caption"):
                cap_y = top_y + max_dev_h + 14
                draw_centered_text(
                    draw,
                    item["caption"],
                    cx,
                    cap_y,
                    cap_font,
                    (*hex_to_rgb(theme["caption_color"]), 255),
                    slot_w,
                )

    return canvas


def render_mobile_panel(spec: dict, theme: dict, base_dir: Path) -> Image.Image:
    w, h = spec.get("width", 1080), spec.get("height", 1920)
    canvas = make_vertical_gradient(w, h, theme["bg_top"], theme["bg_bottom"])
    draw_decorative_accents(canvas, theme["accent"], theme.get("decor", "dots"))
    draw = ImageDraw.Draw(canvas)

    eyebrow_font = load_font(theme.get("font_regular"), max(20, int(w * 0.030)), bold=False)
    title_font = load_font(theme.get("font_bold"), max(44, int(w * 0.072)), bold=True)
    sub_font = load_font(theme.get("font_regular"), max(24, int(w * 0.036)), bold=False)

    cur_y = int(h * 0.06)
    if spec.get("eyebrow"):
        cur_y = draw_centered_text(draw, spec["eyebrow"].upper(), w // 2, cur_y, eyebrow_font, (*hex_to_rgb(theme["muted_color"]), 255), int(w * 0.85))
        cur_y += 10

    cur_y = draw_centered_text(draw, spec.get("title", ""), w // 2, cur_y, title_font, (*hex_to_rgb(theme["title_color"]), 255), int(w * 0.88))
    cur_y += 12

    if spec.get("subtitle"):
        cur_y = draw_centered_text(draw, spec["subtitle"], w // 2, cur_y, sub_font, (*hex_to_rgb(theme["subtitle_color"]), 255), int(w * 0.84))

    images = spec.get("images", [])
    if images:
        top_y = max(cur_y + 36, int(h * 0.25))
        max_h = h - top_y - int(h * 0.05)
        im = fit_image((base_dir / images[0]["src"]).resolve(), int(w * 0.84), max_h)
        sh, pad = add_drop_shadow(im, offset=(0, 18), blur=22, alpha=150)
        canvas.alpha_composite(sh, ((w - im.width) // 2 - pad[0], top_y + (max_h - im.height) // 2 - pad[1]))

    return canvas


RENDERERS = {
    "cover": render_cover,
    "hero_overlap": render_hero_overlap,
    "feature_showcase": render_feature_showcase,
    "mobile_panel": render_mobile_panel,
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Compose store-ready visual preview assets from a JSON manifest.")
    parser.add_argument("--manifest", required=True, help="Path to asset manifest JSON file")
    parser.add_argument("--output-dir", required=True, help="Output directory for store assets (creates master/ subfolder)")
    args = parser.parse_args()

    manifest_path = Path(args.manifest).resolve()
    base_dir = manifest_path.parent
    data = json.loads(manifest_path.read_text(encoding="utf-8"))

    default_theme = {
        "bg_top": "#0D2452",
        "bg_bottom": "#040A18",
        "title_color": "#5CE1FF",
        "subtitle_color": "#F1F5F9",
        "caption_color": "#FACC15",
        "muted_color": "#94A3B8",
        "accent": "#38BDF8",
        "decor": "pixel-squares",
        "font_bold": None,
        "font_regular": None,
    }
    theme = {**default_theme, **data.get("theme", {})}

    out_dir = Path(args.output_dir).resolve()
    master_dir = out_dir / "master"
    out_dir.mkdir(parents=True, exist_ok=True)
    master_dir.mkdir(parents=True, exist_ok=True)

    rendered = []
    for asset in data.get("assets", []):
        layout = asset.get("layout", "feature_showcase")
        if layout not in RENDERERS:
            raise ValueError(f"Unsupported layout '{layout}'. Valid options: {list(RENDERERS.keys())}")
        img = RENDERERS[layout](asset, theme, base_dir)
        out_name = asset["output"]
        stem = Path(out_name).stem
        ext = Path(out_name).suffix.lower() or ".jpg"

        master_path = master_dir / f"{stem}.png"
        img.save(master_path, format="PNG", optimize=True)

        final_path = out_dir / out_name
        if ext in (".jpg", ".jpeg"):
            img.convert("RGB").save(final_path, format="JPEG", quality=92, optimize=True, progressive=True)
        else:
            img.save(final_path, format="PNG", optimize=True)

        rendered.append({
            "output": str(final_path),
            "master": str(master_path),
            "layout": layout,
            "size": [img.width, img.height],
            "bytes": final_path.stat().st_size,
        })

    print(json.dumps({"rendered": len(rendered), "assets": rendered}, indent=2))


if __name__ == "__main__":
    main()
