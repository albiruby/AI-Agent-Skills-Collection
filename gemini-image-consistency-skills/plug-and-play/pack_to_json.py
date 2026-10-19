#!/usr/bin/env python3
"""Convert a markdown Prompt Pack into JSON.
A prompt is any '### <heading>' followed by a fenced ```text block that starts with
'LOCK STYLE & THEME'. The first token of the heading becomes the id.
Usage: python pack_to_json.py prompt_pack.md > pack.json
"""
import json, re, sys

text = open(sys.argv[1], encoding="utf-8").read()
items = []
for m in re.finditer(r"^### (.+?)\n(.*?)(?=^### |\Z)", text, re.S | re.M):
    heading, body = m.group(1).strip(), m.group(2)
    block = re.search(r"```text\n(LOCK STYLE & THEME:.*?)```", body, re.S)
    if block:
        items.append({"id": heading.split()[0], "title": heading,
                      "prompt": block.group(1).strip(), "refs": [], "aspect": "16:9"})
json.dump(items, sys.stdout, ensure_ascii=False, indent=2)
print(f"\n# {len(items)} prompts", file=sys.stderr)
