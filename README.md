# AI Agent Skills Collection

[![Validate frontmatter](https://github.com/albiruby/AI-Agent-Skills-Collection/actions/workflows/validate.yml/badge.svg)](https://github.com/albiruby/AI-Agent-Skills-Collection/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-113-brightgreen.svg)](#packs)
[![SKILL.md format](https://img.shields.io/badge/format-SKILL.md-orange.svg)](SKILL_TEMPLATE.md)

A curated collection of **113 skills** for AI coding agents and assistants, built on the open [Agent Skills](SKILL_TEMPLATE.md) format (`SKILL.md` + YAML frontmatter). Each skill gives an agent a clear role, a step-by-step workflow, and a required output structure for one kind of task — and its `description` carries explicit **"Use when…"** triggers so the right skill loads at the right time.

## Quick start

**1. Pick a skill** from the [packs](#packs) table below.

**2. Install it** — copy the skill folder into the directory your agent scans:

```bash
# OpenCode, Claude Code, and most Agent Skills-compatible tools
cp -r game-dev-skills/game-engine-selector ~/.claude/skills/

# Or install a whole pack (Blender ships an installer)
bash blender-3d-production-suite/install.sh /path/to/your/skills-root
```

**3. Or skip installing** — paste any `SKILL.md` directly into a chat as custom instructions. Every skill is harness-neutral: it works the same as a skill file, a system prompt, or a pasted message.

> **Folder = name.** Every skill folder matches its frontmatter `name`, so installs never collide and discovery works out of the box.

## Packs

| Pack | Skills | What it covers |
|---|---:|---|
| [`web-app-dev-skills`](web-app-dev-skills/) | 22 | Full web & mobile product lifecycle: PRDs, UX flows, architecture, database schemas, API contracts, implementation plans, testing, security, DevOps, docs |
| [`game-dev-skills`](game-dev-skills/) | 23 | Engine-agnostic game development: concept & GDD, engine selection, mechanics, art/audio/UI, level design, netcode, QA, monetization, launch |
| [`blender-3d-production-suite`](blender-3d-production-suite/) | 19 | Professional Blender production: modeling, sculpting, retopo, UV/baking, materials, rigging, animation, FX, lighting, rendering, Python automation, export |
| [`gemini-image-consistency-skills`](gemini-image-consistency-skills/) | 19 | Consistent Gemini image generation: locked style/theme/palette/character bibles, master prompts, reference-image workflow, batch manifests, QA review |
| [`aseprite-master`](aseprite-master/) | 18 | Pixel-art production: sprite generation, frame-by-frame animation, art direction, tilesets, VFX, MCP automation, QA, game-engine export |
| [`human-cognition-agency-skills`](human-cognition-agency-skills/) | 8 | Proactive-but-bounded agent behavior: cognition, decision-making, agency, verification, metacognition, adaptive learning, social intelligence |
| [`ai-video-generation`](ai-video-generation/) | 1 (+24 subskills) | AI video production: briefs, prompt engineering, references, camera & continuity, physics/interaction validation, frame-by-frame QA, failure recovery |
| [`garmin-connect-iq-development`](garmin-connect-iq-development/) | 1 | Garmin wearables in Monkey C: watch faces, widgets, data fields, sensors, adaptive UI, performance, test matrix, Connect IQ Store readiness |
| [`prompt-to-storyboard`](prompt-to-storyboard/) | 1 | Raw idea → complete Gemini image storyboard: locked Style Bible, shot list, paste-ready prompt per panel |
| [`prompt-to-storyboard-flow`](prompt-to-storyboard-flow/) | 1 | Raw idea → consistent 10-second Google Flow (Veo) storyboard: lock block, timecoded shot list, paste-ready video prompt |

## How a skill is structured

```markdown
---
name: game-engine-selector            # matches the folder name
description: Choose an engine or framework… Use when the user asks which
  engine to build with, such as Unity vs Godot vs Phaser.
---

# Game Engine Selector

## Purpose
…
```

The `description` is the skill's router: it states what the skill produces **and** the concrete situations that should trigger it. Skills with vague descriptions never load when they should — see [`SKILL_TEMPLATE.md`](SKILL_TEMPLATE.md) for the house style.

## Repository conventions

- **Frontmatter** is exactly two keys: `name` and `description`. Nothing else.
- **Folder = `name`** for every skill, at every level.
- **A title H1** opens every `SKILL.md`, in plain title case (no `# Instructions`, no ALL CAPS).
- **Every `description` ends with a "Use when…" trigger** and stays under 1024 characters.
- **No version suffixes in folder names** (`-v1`, `-universal`, `NN-` prefixes) — versions live in each pack's README/CHANGELOG.
- CI ([`.github/workflows/validate.yml`](.github/workflows/validate.yml)) enforces frontmatter shape on every push and pull request.

Want to contribute a pack or skill? Read [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) © albiruby. Individual packs may cite upstream inspiration in their READMEs; each skill page notes what it derives from.
