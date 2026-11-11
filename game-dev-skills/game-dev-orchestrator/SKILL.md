---
name: game-dev-orchestrator
description: Entry point for the Game Dev Skills pack. Use first for ANY game development request (idea, prototype, full game, port, fix, launch). Routes to the right specialist skills, defines the pipeline, and enforces the intake checklist. Use when classifying an incoming game-dev request, running the intake checklist, and routing it to the right specialist skill in the pack.
---

# Game Dev Orchestrator

## Purpose
Single entry point. Classify the request, run the intake, pick skills, and keep outputs consistent across the whole pack.

## Intake (ask only what is missing, max 5 questions, otherwise state assumptions)
1. **Pitch**: one sentence (genre + fantasy + hook).
2. **Platforms**: Web / Android / iOS / Windows / macOS / Linux / Console / VR-AR.
3. **Dimension & view**: 2D / 2.5D / 3D; top-down, side, isometric, first/third person.
4. **Team & budget**: solo / small / studio; timeline; skill level; code-only or visual editor OK.
5. **Goal**: jam prototype / portfolio / commercial / educational / live-service.
Record answers in a `PROJECT_BRIEF.md` block and reuse it in every later skill.

## Pipeline & routing
| Phase | Skill |
|---|---|
| Concept | game-concept-gdd, game-genre-playbook |
| Technology | game-engine-selector, game-tech-stack-architect, game-platform-compatibility |
| Design | game-mechanics-systems, game-level-world-design, game-narrative-quest, game-ai-npc-behavior, game-procedural-generation |
| Look & feel | game-art-style-theme, game-asset-pipeline, game-ui-ux-hud, game-audio-design |
| Tech systems | game-physics-input-controls, game-multiplayer-networking, game-performance-optimization |
| Quality | game-qa-playtesting, game-accessibility-localization-legal |
| Business | game-monetization-liveops, game-publishing-launch |
| Execution | game-agent-task-planner (turns everything into agent-ready tasks) |

## Rules
- Prototype the **core loop first** (vertical slice before breadth). Cut scope before cutting quality.
- Every deliverable states: assumptions, decisions + rationale, risks, next step.
- Never hardcode engine/library versions from memory: tell the user to verify current versions, licenses, store policies and fees.
- Prefer the simplest stack that meets platform + team constraints.
- Keep outputs engine-agnostic until game-engine-selector has decided.

## Output contract
Return: (1) PROJECT_BRIEF, (2) skill chain chosen with reason, (3) first deliverable from the first skill, (4) what is needed to continue.
