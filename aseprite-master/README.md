# Aseprite Master Skill Pack

A modular, agent-oriented skill pack for Aseprite pixel-art production, sprite generation, frame-by-frame animation, pixel-level editing, reference conversion, MCP benchmarking/recovery, QA, and game-ready export.

## Structure

- `SKILL.md` — master orchestrator and production rules
- `skills/*/SKILL.md` — focused sub-skills, loaded when relevant
- `templates/` — reusable planning, review, character-bible, MCP capability, and handoff templates

## Compatibility

The pack uses the common `SKILL.md` pattern with YAML frontmatter (`name`, `description`) and Markdown instructions. It is designed to be adapted to OpenCode, Hermes Agent, or another agent that supports skill files. Tool names and parameters are intentionally not hard-coded: discover the actual MCP server tools and their schemas before use.

## Install

Copy the `aseprite-master` directory into the agent's configured skills directory. Consult the specific agent's documentation for its exact skill discovery path. If the agent requires a different manifest format, adapt the frontmatter without changing the workflow instructions.

## Safety and reliability

- Never claim a tool exists before discovering it.
- Never invent MCP tool names, arguments, file paths, or output locations.
- Treat the real Aseprite document and exported files as the source of truth.
- Validate visually and structurally after meaningful changes.
- Do not overwrite source assets without an explicit, safe workflow; prefer a working copy.

## Expanded workflows in v1.1

Additional sub-skills cover pixel-level editing, reusable animation blueprints, cross-frame/asset consistency, MCP capability benchmarking and recovery, and reference-to-sprite conversion. New templates support character bibles and MCP capability reports.
