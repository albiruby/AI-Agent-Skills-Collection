#!/usr/bin/env bash
# Technical probe of a video file (QA Pass 0).
# Usage: video_probe.sh <video>
set -euo pipefail
if [ $# -lt 1 ]; then echo "Usage: $0 <video>" >&2; exit 1; fi
command -v ffprobe >/dev/null || { echo "ffprobe not found (install ffmpeg)." >&2; exit 2; }
f="$1"
[ -f "$f" ] || { echo "File not found: $f" >&2; exit 1; }
ffprobe -v error -show_entries format=duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,nb_frames,sample_rate,channels -of default=noprint_wrappers=1 "$f"
echo "---"
if ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$f" | grep -q audio; then
  echo "audio: present"
else
  echo "audio: none"
fi
