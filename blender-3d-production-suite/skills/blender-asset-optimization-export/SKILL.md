---
name: blender-asset-optimization-export
description: "Optimize Blender assets and scenes for rendering, real-time engines, simulation, 3D printing, and reliable interchange/export. Use when an asset is too heavy for a game engine, needs LODs or texture atlases, or must be exported to glTF, FBX, USD, or STL and verified by re-import."
---

# Blender Asset Optimization Export
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
Act as an optimization and asset pipeline specialist.

# Workflow
1. Confirm target use and format before optimizing: offline render, real-time game engine, web 3D, USD pipeline, animation exchange, 3D printing, or another destination.
2. Inspect geometry count, material slots, draw/instance structure, texture dimensions, shader complexity, modifiers, rig, animation, simulation dependencies, and external resources.
3. Set measurable budgets only when supplied or justified; label proposed budgets as proposed.
4. Optimize using appropriate methods: instancing, mesh simplification, LODs, texture atlases, image compression, shader simplification, modifier application, collection organization, and cache cleanup.
5. Preserve high-quality source assets where required. Keep source and export variants separate.
6. Check transforms, normals, pivots, units, UVs, material assignments, armature, actions, shape keys, and animation range before export.
7. Select export format based on target support. Verify exporter settings and feature support for the installed Blender version and destination software.
8. For glTF/GLB, FBX, USD, OBJ, Alembic, STL, or other formats, do not assume all Blender shader nodes, constraints, simulations, or modifiers transfer. Bake/convert features only as required by the target.
9. Re-import exported files into a clean scene or target tool when possible and compare geometry, materials, scale, hierarchy, and animation.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-polycount-and-mesh-optimization`: mesh budgets, decimation, retopo, instancing.
- `blender-lod-generation`: distance/quality variants for real-time use.
- `blender-texture-memory-optimization`: resolution, compression, atlases, channel packing.
- `blender-shader-optimization`: shader graph simplification and target compatibility.
- `blender-gltf-glb-export`: web/real-time delivery validation.
- `blender-fbx-export`: rig/animation/transform considerations and re-import checks.
- `blender-usd-export`: scene/asset interchange and supported feature validation.
- `blender-stl-3d-print-preflight`: watertightness, scale, thickness, normals, printability.

# Output
Report optimization changes, trade-offs, target format, export settings, and re-import/test results. Never claim universal compatibility from a successful file write alone.
