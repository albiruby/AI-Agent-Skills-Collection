#!/usr/bin/env python3
"""Build a labeled contact sheet from extracted frames.

Usage: contact_sheet.py <frames_dir> <out.png> [--cols 6] [--thumb 320] [--fps 10] [--start 0] [--roi x,y,w,h]

Each thumbnail is labeled with its frame number and time (start + (N-1)/fps).
--roi draws the region used by roi_motion.py so you can verify it covers the object.
Requires Pillow.
"""
import argparse, glob, os, sys
try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("Pillow is required: pip install pillow")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("frames_dir")
    ap.add_argument("out")
    ap.add_argument("--cols", type=int, default=6)
    ap.add_argument("--thumb", type=int, default=320, help="thumbnail width in px")
    ap.add_argument("--fps", type=float, default=10.0)
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--roi", default=None, help="x,y,w,h in original frame pixels")
    a = ap.parse_args()

    files = sorted(glob.glob(os.path.join(a.frames_dir, "frame_*.png")))
    if not files:
        sys.exit(f"No frame_*.png files in {a.frames_dir}")
    first = Image.open(files[0])
    tw = a.thumb
    th = max(1, int(first.height * tw / first.width))
    label_h = 18
    cols = max(1, a.cols)
    rows = (len(files) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * (th + label_h)), (20, 20, 20))
    draw = ImageDraw.Draw(sheet)
    for i, f in enumerate(files):
        src = Image.open(f).convert("RGB")
        if a.roi:
            rx, ry, rw, rh = [int(v) for v in a.roi.split(",")]
            ImageDraw.Draw(src).rectangle([rx, ry, rx + rw, ry + rh], outline=(255, 0, 0), width=max(2, src.width // 200))
        im = src.resize((tw, th))
        x = (i % cols) * tw
        y = (i // cols) * (th + label_h)
        sheet.paste(im, (x, y + label_h))
        t = a.start + i / a.fps
        draw.text((x + 4, y + 3), f"#{i+1}  t={t:.2f}s", fill=(255, 255, 255))
    sheet.save(a.out)
    print(f"Saved {a.out}: {len(files)} frames, {cols}x{rows} grid.")

if __name__ == "__main__":
    main()
