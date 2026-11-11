# Subskill 10 — Model and Platform Adaptation

## Purpose
Adapt a platform-neutral production plan to the actual video model and interface.

## Capability discovery
Confirm, where relevant:
- Text-to-video or image-to-video.
- Start/end frame support.
- Character or subject references.
- Multiple reference images.
- Video reference or motion guidance.
- Audio generation and audio input.
- Camera controls.
- Duration and aspect-ratio limits.
- Resolution and frame-rate options.
- Seeds, variations, extensions, and editing.
- Negative prompt fields.
- Commercial-use terms and content restrictions.

Use official, current documentation when available. If not verified, label as unknown rather than guessing.

## Model-specific prompting
Some models prefer concise natural language; others support structured shots, timestamps, or separate camera/action fields. Adapt prompt structure to verified behavior.

## Interface-aware workflow
Explain where to place:
- Main prompt.
- Negative prompt, if supported.
- Reference images.
- Start/end frames.
- Audio assets.
- Duration/aspect settings.
- Variations or seed controls.

Do not invent UI labels or controls.

## Model fallback
If the selected model cannot satisfy a critical requirement:
1. Explain the limitation.
2. Simplify the shot.
3. Split the task into stages.
4. Use a different supported generation mode or model if available.
5. Use post-production for exact elements.

## Output
Provide only settings known to exist, and clearly label recommended values versus mandatory constraints.

## Verification by research
Use subskill 24 to verify capabilities with current sources before relying on them, and record them in `templates/capability-sheet.md`. See `references/model-landscape-snapshot-2026-11.md` for a dated, unverified starting point. Run a short **contact test** (simple pick-up and set-down) on a new model before committing a large batch.
