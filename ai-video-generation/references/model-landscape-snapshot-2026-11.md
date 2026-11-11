# Model Landscape Snapshot — November 2026

> **Volatile. Verify before use** (subskill 24). Compiled on 2026-11-11 from secondary sources (comparison articles and vendor-adjacent guides), not from official documentation. Treat as leads to verify, not as specifications.

## Reported state of the field
| Model / tool | Reported highlights (secondary sources) | Notes |
|---|---|---|
| Google Veo 3.1 | Native audio; first/last-frame control; reference images ("ingredients"); extension; structured prompt formula [Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance] | Frequently described as strong on prompt adherence and physics; still verify contact-heavy shots |
| Kling 3.0 | Reported native 4K/60 fps; "Omni"/director-style controls; strong for high-motion and human motion in several tests | Verify limits and plan details |
| Runway Gen-4 / Gen-4.5 (+ Aleph editing) | Shot control, iteration, editing workflow | Verify current feature set |
| ByteDance Seedance 2.0 / 2.5 | Multimodal inputs (images, clips, audio); multi-shot narratives; high ranking on public arenas (reported) | Reference limits reported differently across sources; verify |
| Alibaba Wan (open-source) and HappyHorse-1.0 | Open-source option / newer entrant | Hardware and version details vary; verify |
| Luma, Pika, Hailuo/MiniMax, PixVerse | Image-to-video, social effects, quick iteration | Verify |
| OpenAI Sora 2 | Reported discontinued: web app April 2026, API scheduled to end 2026-09-24 | Do not build new workflows on it; confirm status |

## What this means for the physics layer
- Capabilities that help with interaction control — **first/last frame, reference images, extension, multi-reference input, video-to-video** — exist on several tools but differ in availability and limits. Use them for keyframe anchoring (subskill 23, L6) only after verifying.
- Reported test patterns across tools: non-contact dynamics tend to hold up; contact-heavy, state-change, and chained-physics shots are less reliable. Plan multiple takes and split shots.
- Leaderboards and "best of" lists change monthly and often reflect marketing. Choose by the task's critical requirement (contact reliability, references, audio, price), then test with a **10-second contact test** (a simple pick-up and set-down) before committing a large batch.

## How to refresh this file
1. Search each model's official docs and release notes.
2. Update the table with: feature, limit, source, date.
3. Move discontinued models to a "retired" row.
4. Keep the file dated.
