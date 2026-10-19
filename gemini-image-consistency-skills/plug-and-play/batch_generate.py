#!/usr/bin/env python3
"""Batch-generate images with the Gemini API from a JSON prompt pack.
Untested sketch: verify SDK usage and the model ID in the current Gemini API docs.
Usage: GEMINI_IMAGE_MODEL=<model-id> python batch_generate.py pack.json global_rules.txt out/
pack.json items: {"id": "...", "prompt": "...", "refs": ["anchor.png"], "aspect": "16:9"}
"""
import json, mimetypes, os, pathlib, sys, time
from google import genai
from google.genai import types

pack_path, rules_path, out_dir = sys.argv[1], sys.argv[2], pathlib.Path(sys.argv[3])
out_dir.mkdir(parents=True, exist_ok=True)
client = genai.Client()
model = os.environ["GEMINI_IMAGE_MODEL"]
system = pathlib.Path(rules_path).read_text(encoding="utf-8")

for item in json.load(open(pack_path, encoding="utf-8")):
    target = out_dir / f"{item['id']}.png"
    if target.exists():
        continue                                   # resume-friendly
    parts = [types.Part.from_bytes(data=pathlib.Path(r).read_bytes(),
                                   mime_type=mimetypes.guess_type(r)[0] or "image/png")
             for r in item.get("refs", [])]
    parts.append(item["prompt"])
    try:
        resp = client.models.generate_content(
            model=model, contents=parts,
            config=types.GenerateContentConfig(
                system_instruction=system,
                response_modalities=["TEXT", "IMAGE"],
                image_config=types.ImageConfig(aspect_ratio=item.get("aspect", "1:1"))))
        saved = False
        for part in resp.candidates[0].content.parts:
            if part.inline_data:
                target.write_bytes(part.inline_data.data); saved = True; break
        print(("saved " if saved else "no image for ") + item["id"])
    except Exception as e:
        print(f"error {item['id']}: {e}", file=sys.stderr)
    time.sleep(1)
