# AI Video Generation Skills (v2.0)

A reusable, platform-agnostic skill package for AI video production, now with a **Physics & Interaction Validation layer** and a **web-research protocol**.

## Package contents
- `SKILL.md` — master skill, workflow, gates, load matrix.
- `subskills/` — 24 focused subskills:
  - 01–14: production (brief, concept, prompts, references, camera, motion, style, continuity, audio, platform adaptation, QA, export, social, safety).
  - 15–23: **Physics & Interaction Validation** (risk gates, interaction protocol, contact logic, dynamics, hands, object continuity, error taxonomy, frame-by-frame QA, failure recovery).
  - 24: **Web research and capability verification**.
- `templates/` — project profile, video brief, QA scorecard, physics risk assessment, interaction spec, continuity ledger, frame QA log, iteration log, capability sheet, shot list.
- `references/` — physics cheatsheet, interaction prompt patterns, model-landscape snapshot (dated; verify), research sources.
- `examples/` — worked examples (grab a watering can, water the plants, open a door).
- `scripts/` — frame-level QA tools (ffmpeg + Python).
- `PLUG-AND-PLAY.md` — condensed paste-ready version for chat UIs.
- `CHANGELOG.md`.

## Installation
Copy the whole folder into the skill directory supported by your agent and keep the structure intact. If your runner requires the folder name to match the skill `name`, rename the folder to `ai-video-generation`. If your platform uses a different manifest, adapt the YAML frontmatter in `SKILL.md`; the instructional content is platform-neutral.

If your tool has no skill support, paste `PLUG-AND-PLAY.md` as a custom instruction.

## Recommended invocation
Use the master skill for any video-generation request. Load only the relevant subskills (see the **Load matrix** in `SKILL.md`):
- Simple text-to-video without contact: master + 01, 02, 03, 10.
- Hand-object action: add 15, 16, 17, 19, 22.
- Carry, pour, door, handoff: add 18, 20, 21, 23 and the physics templates.
- Product demo or precise mechanism: all of 15–24 and plan hybrid production.
- Unknown or new model: start with 24.

## Physics layer in one minute
1. **Tier** the shot (R0–R4). R3 → split. R4 → hybrid.
2. **Spec** the interaction (part, hand, grip, beats, object stays still until contact).
3. **Encode** it in the prompt (`references/prompt-patterns-interactions.md`).
4. **Inspect** frame by frame at contact checkpoints; classify defects (IDs A–F).
5. **Recover** with the ladder L0–L9; change one variable per attempt.

## QA scripts
Require `ffmpeg`/`ffprobe`; the Python scripts need Pillow and numpy.
```
scripts/video_probe.sh clip.mp4
scripts/extract_frames.sh clip.mp4 frames 10            # whole clip at 10 fps
scripts/extract_frames.sh clip.mp4 frames_hi 24 2.0 3.5 # window 2.0–3.5 s at 24 fps
python3 scripts/contact_sheet.py frames sheet.png --fps 10 --roi 290,140,90,120
python3 scripts/roi_motion.py frames --fps 10 --roi 290,140,90,120 --contact 2.5
```
`roi_motion.py` is a heuristic: it reports the percentage of changed pixels inside a box around the resting object and flags changes before the first-contact time (possible A1). A sustained run starting well before contact suggests unintended object motion; a short burst just before contact is usually the hand or its shadow. Always confirm by eye.

Test status: the scripts were run on synthetic videos (one with deliberate pre-contact drift, one clean control). The drift was flagged from the first moving frame; the control produced only a short burst as the hand entered the box. They have not been validated on real AI-generated footage.

## Important
This package does not guarantee perfect generation. Video models are probabilistic, learn physics statistically, and have tool-specific limits. The skill improves planning, prompt clarity, consistency, detection of failures, and recovery, while staying honest about those limits. Model-specific facts in `references/model-landscape-snapshot-2026-11.md` came from secondary sources and must be re-verified (subskill 24).
