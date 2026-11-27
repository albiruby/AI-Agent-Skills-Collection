#!/usr/bin/env python3
"""Generate a hue-shifted pixel-art palette ramp from one base color."""

import argparse
import colorsys
import json
import sys


def hex_to_rgb(value: str):
    value = value.strip().lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    if len(value) != 6:
        raise ValueError("expected #RRGGBB")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(c))) for c in rgb)


def clamp(v, lo=0.0, hi=1.0):
    return max(lo, min(hi, v))


def make_ramp(base, steps=5, hue_shift=18.0, light_range=0.32, sat_shift=0.10):
    r, g, b = [c / 255.0 for c in base]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    out = []
    for i in range(steps):
        t = i / (steps - 1) if steps > 1 else 0.5
        hh = (h + ((t - 0.5) * hue_shift) / 360.0) % 1.0
        ll = clamp(l + (t - 0.5) * light_range)
        ss = clamp(s + (t - 0.5) * sat_shift)
        rr, gg, bb = colorsys.hls_to_rgb(hh, ll, ss)
        out.append({
            "index": i,
            "role": "shadow" if i == 0 else ("highlight" if i == steps - 1 else "mid"),
            "hex": rgb_to_hex((rr * 255, gg * 255, bb * 255)),
        })
    return out


def main() -> int:
    p = argparse.ArgumentParser(description="Generate a hue-shifted palette ramp")
    p.add_argument("base", help="Base color, e.g. #3a6ea5")
    p.add_argument("--steps", type=int, default=5)
    p.add_argument("--hue-shift", type=float, default=18.0, help="Total hue swing in degrees")
    p.add_argument("--light-range", type=float, default=0.32)
    p.add_argument("--sat-shift", type=float, default=0.10)
    p.add_argument("--format", choices=["json", "hex", "css"], default="json")
    args = p.parse_args()
    if args.steps < 2:
        print("steps must be >= 2", file=sys.stderr)
        return 2
    ramp = make_ramp(hex_to_rgb(args.base), args.steps, args.hue_shift, args.light_range, args.sat_shift)
    if args.format == "hex":
        print(" ".join(x["hex"] for x in ramp))
    elif args.format == "css":
        print("\n".join(f"--ramp-{x['index']}: {x['hex']};" for x in ramp))
    else:
        print(json.dumps({"base": args.base, "ramp": ramp}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
