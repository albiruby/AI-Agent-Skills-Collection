---
name: blender-scene-project-pipeline
description: "Set up and maintain organized, reusable, version-aware Blender projects, scenes, collections, naming, units, asset paths, and production files. Use when a .blend file is disorganized with random names, scattered collections, or wrong units, or a new project needs folder layout, naming, and checkpoint rules."
---

# Blender Scene Project Pipeline
## Cross-harness execution contract

This skill is written for the vendor-neutral Agent Skills format. Apply its workflow in the current agent environment without assuming a particular model, AI product, orchestration framework, tool name, command syntax, or filesystem layout.

- Discover the capabilities actually exposed in the current session before attempting actions. Tool names and schemas vary between harnesses and installations.
- Use whichever supported path is available: Blender desktop/UI control, an exposed tool bridge or MCP server, Python execution inside Blender, Blender background/command-line mode, or a documented external API. These are alternatives, not guaranteed capabilities.
- For tool calls, inspect the current tool description and full argument schema. Never invent tool names, arguments, resource identifiers, or hidden capabilities.
- Use `bpy`, `bmesh`, and Blender data APIs only in a Python runtime that has Blender's Python modules available. Do not assume the agent's system Python can import `bpy`.
- Do not assume shell access, a running Blender process, desktop access, network access, or unrestricted filesystem access. Verify each capability before relying on it.
- Use paths supplied by the user or discovered in the active workspace. Avoid hard-coded machine-specific paths. Prefer portable path handling and preserve existing project structure.
- If direct execution is unavailable, continue with the useful work that remains possible: prepare version-aware scripts, exact manual steps, validation procedures, or export instructions. Clearly identify what the user must execute.
- A skill does not grant tools, permissions, application access, or approval. Respect the active environment's permission model and the user's requested scope.
- Do not use harness-specific template variables, inline-shell directives, hook syntax, sub-agent metadata, slash-command assumptions, or proprietary frontmatter. Keep instructions in ordinary Markdown.
- Verify changes through observable scene state, generated files, rendered previews, logs, or re-opened artifacts before reporting success. Distinguish completed, attempted, blocked, and unverified work.

# Role
Act as a Blender pipeline TD responsible for a clean, maintainable project structure.

# Workflow
1. Inspect the existing `.blend` and installed Blender version before modifying anything.
2. Establish project folder layout for `blend/`, `assets/`, `textures/`, `cache/`, `renders/`, `exports/`, `references/`, and `scripts/` as appropriate.
3. Set units, scale, frame rate, frame range, resolution, color management, render engine, and output paths according to the brief.
4. Create logical collections and scenes. Use predictable names for assets, materials, cameras, lights, rigs, actions, node groups, and exports.
5. Separate source/high-poly, production/low-poly, proxy, collision, helper, and render-only objects where useful.
6. Establish versioning and checkpoint rules. Save a new revision before destructive operations; do not overwrite the sole source without authorization.
7. Check external paths, linked libraries, fonts, image sequences, simulation caches, and packed resources.
8. Remove only confirmed unused data; do not delete assets whose dependencies are uncertain.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-project-bootstrap`: create a new scene/project baseline.
- `blender-collection-and-naming`: collection hierarchy and naming conventions.
- `blender-units-and-scale`: real-world scale, units, origins, and transform conventions.
- `blender-asset-path-management`: packed images, linked resources, fonts, caches, and relative paths.
- `blender-version-and-checkpoint-management`: version-aware project saves and non-destructive checkpoints.

# Validation
Reopen or inspect the saved file when possible. Verify scenes, collections, paths, output settings, and required dependencies. Report anything missing or unresolved.
