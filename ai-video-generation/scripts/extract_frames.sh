#!/usr/bin/env bash
# Extract frames from a video for frame-by-frame QA.
# Usage: extract_frames.sh <video> <outdir> [fps=10] [start_seconds] [end_seconds]
# Frames are named frame_000001.png ... Frame N corresponds to time start + (N-1)/fps.
set -euo pipefail
if [ $# -lt 2 ]; then echo "Usage: $0 <video> <outdir> [fps=10] [start] [end]" >&2; exit 1; fi
command -v ffmpeg >/dev/null || { echo "ffmpeg not found." >&2; exit 2; }
video="$1"; out="$2"; fps="${3:-10}"; start="${4:-}"; end="${5:-}"
[ -f "$video" ] || { echo "File not found: $video" >&2; exit 1; }
mkdir -p "$out"
args=(-v error -y)
[ -n "$start" ] && args+=(-ss "$start")
[ -n "$end" ] && args+=(-to "$end")
args+=(-i "$video" -vf "fps=${fps}" "$out/frame_%06d.png")
ffmpeg "${args[@]}"
n=$(ls "$out"/frame_*.png 2>/dev/null | wc -l | tr -d ' ')
echo "Extracted $n frames at ${fps} fps into $out (start=${start:-0}s)."
echo "Tip: use a higher fps (24-30) on a narrow window around the contact."
