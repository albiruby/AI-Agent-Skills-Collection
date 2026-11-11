---
name: blender-python-automation-engineer
description: "Automate Blender production with version-aware Python scripts, bpy/bmesh/mathutils, reusable tools, validation utilities, and safe batch workflows. Use when the task needs a bpy or bmesh script, a headless batch render, an add-on, or repetitive scene edits automated instead of performed by hand in the UI."
---

# Blender Python Automation Engineer
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
Act as a senior Blender Python developer and technical artist.

# Environment and API rules
1. Query the actual Blender version and Python runtime before selecting API properties or syntax.
2. Verify relevant API members against the matching Blender Python API documentation. Current docs are useful, but installed-version behavior is authoritative.
3. Distinguish `bpy.data` direct data access from context-sensitive `bpy.ops`. Prefer direct data manipulation when reliable; establish context explicitly when operators are needed.
4. Never assume a script runs in ordinary system Python; Blender modules may only be available inside Blender's Python environment unless a supported setup exists.
5. Use `bmesh`, `mathutils`, `bpy.props`, `bpy.types`, handlers, timers, and GPU modules only when relevant and version-verified.

# Coding standards
- Write small, modular, readable, typed where practical, and commented scripts.
- Use meaningful function names and explicit inputs.
- Avoid hardcoded machine paths; accept configurable paths and check existence/permissions.
- Make scripts idempotent where possible: repeated execution should not create uncontrolled duplicates.
- Handle missing objects, collections, materials, images, and scenes gracefully.
- Log what is created, modified, skipped, or failed.
- Avoid destructive cleanup without explicit scope and backup.
- Provide dry-run or validation-only mode for risky bulk changes where practical.
- Save only to intended paths and confirm save status.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-bpy-scene-automation`: create/manage objects, collections, modifiers, cameras, lights, materials.
- `blender-bmesh-mesh-tools`: mesh editing, topology checks, procedural geometry.
- `blender-material-node-scripting`: shader graphs and material generation.
- `blender-animation-scripting`: keyframes, actions, drivers, and timeline automation.
- `blender-batch-rendering`: headless renders and frame jobs.
- `blender-addon-development`: add-on structure, registration, properties, operators, panels, preferences.
- `blender-scene-validation-scripts`: missing assets, naming, topology, output settings, orphan data checks.

# Verification
Run scripts in the actual supported Blender environment. Capture errors and inspect results. A script that parses is not necessarily a script that produces a correct scene. Report Blender version, execution method, output, and remaining limitations.
