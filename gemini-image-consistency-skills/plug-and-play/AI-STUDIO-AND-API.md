# Google AI Studio and Gemini API

## System instruction
Paste the compact block from `GEM-INSTRUCTIONS.md` (A) as the **system instruction**, or paste your own Slot 1 global rules. Then send per-asset prompts in the user turn with anchor images attached.

## Python sketch (google-genai SDK)
Verify SDK version, parameter names and the image model ID in the current docs before use. This sketch has not been run in this environment.
```python
import os
from google import genai
from google.genai import types

client = genai.Client()                      # reads GEMINI_API_KEY
MODEL = os.environ["GEMINI_IMAGE_MODEL"]     # set to the current image model ID

system = open("global_rules.txt").read()
ref = types.Part.from_bytes(data=open("ANCHOR_character_hero_v1.png","rb").read(), mime_type="image/png")
prompt = open("prompt_TM-WALK-RIGHT.txt").read()

resp = client.models.generate_content(
    model=MODEL,
    contents=[ref, prompt],                  # references first, then the prompt
    config=types.GenerateContentConfig(
        system_instruction=system,
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(aspect_ratio="16:9"),
    ),
)
for part in resp.candidates[0].content.parts:
    if part.inline_data:
        open("out.png", "wb").write(part.inline_data.data)
```

## Batch workflow
1. `python pack_to_json.py prompt_pack.md > pack.json`
2. Edit `pack.json` to add `refs` (anchor paths) and `aspect` per item if needed.
3. `GEMINI_IMAGE_MODEL=<id> python batch_generate.py pack.json global_rules.txt out/`
4. Review `out/` with the QA prompt, then post-process.
