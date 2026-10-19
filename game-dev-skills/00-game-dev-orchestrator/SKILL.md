---
name: game-dev-orchestrator
description: Entry point for the Game Dev Skills pack. Use first for ANY game development request (idea, prototype, full game, port, fix, launch). Routes to the right specialist skills, defines the pipeline, and enforces the intake checklist.
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
| Concept | 01-game-concept-gdd, 05-game-genre-playbook |
| Technology | 02-game-engine-selector, 03-game-tech-stack-architect, 16-game-platform-compatibility |
| Design | 04-game-mechanics-systems, 10-game-level-world-design, 11-game-narrative-quest, 12-game-ai-npc-behavior, 21-game-procedural-generation |
| Look & feel | 06-game-art-style-theme, 07-game-asset-pipeline, 08-game-ui-ux-hud, 09-game-audio-design |
| Tech systems | 13-game-physics-input-controls, 14-game-multiplayer-networking, 15-game-performance-optimization |
| Quality | 17-game-qa-playtesting, 20-game-accessibility-localization-legal |
| Business | 18-game-monetization-liveops, 19-game-publishing-launch |
| Execution | 22-game-agent-task-planner (turns everything into agent-ready tasks) |

## Rules
- Prototype the **core loop first** (vertical slice before breadth). Cut scope before cutting quality.
- Every deliverable states: assumptions, decisions + rationale, risks, next step.
- Never hardcode engine/library versions from memory: tell the user to verify current versions, licenses, store policies and fees.
- Prefer the simplest stack that meets platform + team constraints.
- Keep outputs engine-agnostic until 02-game-engine-selector has decided.

## Output contract
Return: (1) PROJECT_BRIEF, (2) skill chain chosen with reason, (3) first deliverable from the first skill, (4) what is needed to continue.
