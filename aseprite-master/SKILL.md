---
name: aseprite-master
description: Orchestrates complete Aseprite pixel-art workflows including sprite generation, character sheets, frame-by-frame animation, effects, tilesets, MCP automation, QA, and game-ready export. Use whenever an AI agent must create, edit, animate, inspect, or export Aseprite assets.
---

# Aseprite Master Orchestrator

## Mission

Produce coherent, technically valid, game-ready pixel-art assets in Aseprite. Turn a natural-language brief into a staged plan, use only discovered tools, inspect real outputs, correct defects, and deliver a verifiable handoff.

## Core behavior

1. Understand the intended asset, visual style, dimensions, palette, animation, target engine, and deliverables.
2. Ask only for missing details that materially block execution. Otherwise choose sensible defaults and state them.
3. Inspect the current project and discover available Aseprite MCP tools before taking actions.
4. Make a concise plan with stages, dependencies, acceptance criteria, and checkpoints.
5. Create or edit assets in a working copy when possible.
6. Execute the workflow through actual available tools. If a capability is unavailable, explain the limitation and use a supported alternative only when safe.
7. Inspect results after each major stage; do not treat successful tool execution as proof of visual correctness.
8. Fix issues, re-check, then export and report exact verified outputs.

## Sub-skill routing

Load the relevant sub-skill(s) as needed:

- Brief decomposition, task planning, orchestration: `skills/aseprite-production-planning/SKILL.md`
- Precise pixel edits and cleanup: `skills/aseprite-pixel-level-editing/SKILL.md`
- Reusable animation blueprints: `skills/aseprite-animation-blueprints/SKILL.md`
- Consistency across assets and frames: `skills/aseprite-sprite-consistency/SKILL.md`
- MCP capability tests and recovery: `skills/aseprite-mcp-benchmark-recovery/SKILL.md`
- Reference image to pixel-art workflow: `skills/aseprite-reference-to-sprite/SKILL.md`
- Sprite or character creation: `skills/aseprite-sprite-generation/SKILL.md`
- Character design, silhouette, palette and style consistency: `skills/aseprite-art-direction/SKILL.md`
- Frame-by-frame animation: `skills/aseprite-animation-studio/SKILL.md`
- Spell, impact, particles and other visual effects: `skills/aseprite-vfx-animation/SKILL.md`
- Tilesets, props, environment assets: `skills/aseprite-tilesets-environments/SKILL.md`
- MCP discovery and safe operation: `skills/aseprite-mcp-operations/SKILL.md`
- Spritesheets, slicing, export and metadata: `skills/aseprite-export-pipeline/SKILL.md`
- Visual and technical validation: `skills/aseprite-qa-debugging/SKILL.md`
- Engine integration and asset contracts: `skills/aseprite-game-engine-handoff/SKILL.md`
- Reusable prompts and references: `skills/aseprite-prompt-design/SKILL.md`
- Project handoff and documentation: `skills/aseprite-delivery-documentation/SKILL.md`

Load only the skills needed for the current job, but combine them when the task crosses domains.

## Required workflow

### Stage 1 — Brief
Extract:
- Asset type and purpose
- Style reference and style constraints
- Canvas size and frame dimensions
- Palette or color limits
- Required poses, directions, states, and animation loops
- Frame rate or per-frame timing
- Transparency/background rules
- Target engine and export format
- File naming and destination

If unknown, infer a practical default for a prototype and clearly label it as an assumption.

### Stage 2 — Feasibility and tool discovery
- Enumerate the MCP tools and schemas actually exposed by the connected server.
- Identify operations for reading project state, creating/opening files, editing pixels/layers/frames, previews, and exports.
- Verify whether a tool edits the active document, returns a path, returns image data, or merely reports metadata.
- Never assume the server exposes every Aseprite feature.
- If no visual inspection path exists, use available previews, exports, metadata, or request a reference image; disclose remaining uncertainty.

### Stage 3 — Plan
Create an ordered plan. Prefer small reversible operations over a single opaque batch. Establish checkpoints after:
1. canvas and document setup,
2. base silhouette / key pose,
3. palette and detail,
4. animation blocking,
5. timing and cleanup,
6. export and validation.

### Stage 4 — Build
- Keep silhouettes readable at native resolution.
- Use consistent pixel clusters; avoid accidental anti-aliasing unless stylistically requested.
- Preserve a coherent palette, light source, outline policy, and material language.
- For animation, establish key poses and motion arcs before polishing.
- Keep layers meaningful and names descriptive.
- Use explicit frame and layer indices only after verifying indexing conventions.
- Avoid destructive edits to originals; use a duplicate or checkpoint if supported.

### Stage 5 — Validate
Use `skills/aseprite-qa-debugging/SKILL.md`. Check both the image and document structure. Fix issues and validate again.

### Stage 6 — Export and handoff
Use `skills/aseprite-export-pipeline/SKILL.md` and `skills/aseprite-delivery-documentation/SKILL.md`. Report only paths and formats confirmed by tool output or filesystem inspection.

## Non-negotiable rules

- No fake data, fake screenshots, fabricated tool responses, or invented output paths.
- No claim of “finished” without checking the resulting asset.
- No silent changes to requested dimensions, style, frame count, timing, or transparency.
- No destructive overwrite when a safe copy/checkpoint is possible.
- No unnecessary complexity: use the smallest reliable workflow that meets the brief.
- Keep user-facing status concise; make technical detail available in the handoff.
- If blocked, state the exact missing capability and the best supported next step.

## Default acceptance criteria

Unless the user specifies otherwise:
- Asset opens in Aseprite or the confirmed compatible editor.
- Dimensions and frame count match the specification.
- Transparent pixels are actually transparent where required.
- Palette and style are coherent across frames/assets.
- Animation reads clearly at native size and at intended speed.
- No accidental stray pixels, clipping, broken loops, or inconsistent pivots.
- Exported files exist at the reported paths and can be inspected.
