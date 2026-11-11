---
name: aseprite-prompt-design
description: Writes precise, production-oriented prompts for Aseprite agents and image-reference workflows, with constraints for style, dimensions, animation, and acceptance criteria. Use when the user asks to write or tighten a prompt or brief for an Aseprite agent or image-generation workflow.
---

# Prompt Design

## Prompt structure
1. Role and objective
2. Asset and gameplay purpose
3. Visual style and prohibited style drift
4. Canvas / frame dimensions
5. Palette and lighting
6. Pose or animation phases
7. Timing and loop rules
8. Layers and naming
9. Export requirements
10. Validation checklist
11. Tool-use constraints

## Reference images
- Treat references as visual guidance, not proof that a file has been created.
- Separate required elements from optional inspiration.
- Call out what must remain consistent across views and frames.
- Do not assume image-generation models can produce clean, editable Aseprite layers or exact frame timing.
- If an image model is used, treat its output as a reference or input unless it can genuinely deliver the required editable asset.
- Convert references into a clear pixel-art construction plan before editing the native document.

## Strong constraint language
Prefer observable criteria:
- “Keep the staff in the same hand in all frames.”
- “Use a transparent background.”
- “Keep the feet aligned to the same baseline.”
- “Create distinct charge, release, and recovery poses.”
Avoid vague-only requirements such as “make it professional” or “make it cool.”

## Prompt QA
Check for contradictions, missing dimensions, ambiguous timing, untestable claims, and requirements unsupported by the available MCP tools.
