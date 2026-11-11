#!/usr/bin/env python3
"""Heuristic motion check inside a region of interest (ROI).

Purpose: help detect A1 (object moves before the hand touches it).
Draw the ROI tightly around the OBJECT at rest, away from the hand's path.
The script reports, per frame, the percentage of ROI pixels that changed
versus the previous frame (RGB, per-pixel tolerance). Changes before the
first-contact time suggest unintended object motion, or the hand/shadow
entering the ROI early. Confirm by eye.

Usage:
  roi_motion.py <frames_dir> --roi x,y,w,h [--fps 10] [--start 0] [--contact T]
                [--pixel-tol 20] [--threshold 1.0]

--roi         pixel box x,y,w,h in frame coordinates
--contact     first-contact time in seconds; flags frames before it
--pixel-tol   per-pixel RGB difference (0-255) that counts as "changed" (default 20)
--threshold   percent of changed ROI pixels that counts as motion (default 1.0)

Limits: heuristic only. Compression noise, lighting changes, camera moves, and a
hand entering the ROI also produce changes. Use a short, tight ROI and compare
frames visually (contact_sheet.py --roi draws the ROI). Requires Pillow and numpy.
"""
import argparse, glob, os, sys
try:
    import numpy as np
    from PIL import Image
except ImportError:
    sys.exit("Pillow and numpy are required: pip install pillow numpy")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("frames_dir")
    ap.add_argument("--roi", required=True)
    ap.add_argument("--fps", type=float, default=10.0)
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--contact", type=float, default=None)
    ap.add_argument("--pixel-tol", type=float, default=20.0)
    ap.add_argument("--threshold", type=float, default=1.0)
    a = ap.parse_args()

    x, y, w, h = [int(v) for v in a.roi.split(",")]
    files = sorted(glob.glob(os.path.join(a.frames_dir, "frame_*.png")))
    if len(files) < 2:
        sys.exit("Need at least 2 frames.")

    prev = None
    flagged = []
    print("frame  time(s)  changed_px_%  note")
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB")
        crop = np.asarray(im.crop((x, y, x + w, y + h)), dtype=np.int16)
        t = a.start + i / a.fps
        if prev is not None:
            diff = np.abs(crop - prev).max(axis=2)
            pct = float((diff > a.pixel_tol).mean() * 100.0)
            note = ""
            if pct >= a.threshold:
                note = "CHANGE"
                if a.contact is not None and t < a.contact:
                    note = "CHANGE BEFORE CONTACT (check A1)"
                    flagged.append((i + 1, t, pct))
            print(f"{i+1:5d}  {t:7.2f}  {pct:11.2f}  {note}")
        prev = crop
    print("---")
    if a.contact is not None:
        if flagged:
            print(f"{len(flagged)} frame(s) show ROI change before contact at t={a.contact}s:")
            for n, t, p in flagged:
                print(f"  frame {n} (t={t:.2f}s) changed={p:.2f}%")
            print("Inspect these frames by eye. A sustained run starting well before contact suggests A1;")
            print("a short burst right before contact may be the hand or its shadow entering the ROI.")
        else:
            print("No ROI change above threshold before the contact time.")
    else:
        print("Provide --contact to flag pre-contact motion.")

if __name__ == "__main__":
    main()
