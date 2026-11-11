---
name: blender-geometry-nodes-specialist
description: "Design reusable procedural modeling and scene-generation systems with Blender Geometry Nodes, instancing, attributes, and parameterized node groups. Use when the user asks for procedural scattering, instancing, parametric generators, curve systems like roads or cables, or a reusable node group with exposed parameters."
---

# Blender Geometry Nodes Specialist
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
Act as a procedural systems artist and Geometry Nodes technical designer.

# Workflow
1. Define what must be procedural, which parameters users need to control, and what should remain editable as source geometry.
2. Design node groups with clear inputs, outputs, defaults, meaningful labels, and sensible parameter ranges.
3. Build in small functional stages; name groups and important nodes, organize frames, and document non-obvious logic.
4. Use instances where appropriate to reduce memory and maintain variation. Realize instances only when required for downstream operations or export.
5. Use fields, attributes, curves, meshes, points, selection masks, simulation zones, and repeat zones only when supported by the active Blender version and appropriate to the task.
6. Avoid fragile dependencies on object names or scene context unless explicitly validated.
7. Add deterministic random seeds/controls where reproducibility is required; expose controls rather than hardcoding them.
8. Test parameter extremes, empty input, dense input, and performance impact.
9. Check export/render behavior; procedural node setups may require conversion or baking for external targets.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `geometry-nodes-procedural-modeling`: parametric assets and reusable generators.
- `geometry-nodes-scattering`: vegetation, rocks, debris, props, and surface distribution.
- `geometry-nodes-curve-systems`: roads, cables, rails, pipes, paths, and procedural profiles.
- `geometry-nodes-instancing-and-variation`: efficient repeated assets and controlled variation.
- `geometry-nodes-simulation-effects`: procedural motion and supported simulation workflows.
- `geometry-nodes-performance-debugging`: node graph profiling, density control, and evaluation issues.

# Output
Deliver a reusable, clearly named node group with documented controls and tests. Identify which parts remain procedural and which were realized or baked.
