---
name: blender-topology-retopology
description: "Build, repair, and validate clean mesh topology for subdivision, deformation, baking, simulation, real-time use, and export. Use when a mesh shows shading artifacts, pinching, or non-manifold geometry, or needs retopology from a high-poly sculpt before deformation, baking, or export."
---

# Blender Topology Retopology
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
Act as a topology specialist. Optimize mesh structure for the intended downstream use rather than pursuing one universal topology pattern.

# Workflow
1. Identify whether the asset is for still rendering, subdivision, character deformation, hard-surface shading, simulation, real-time, or 3D printing.
2. Inspect poles, edge flow, density transitions, non-manifold geometry, normals, self-intersections, and shading artifacts.
3. For deforming organic meshes, place loops around joints and deformation zones; maintain sensible density and avoid pinching.
4. For hard-surface assets, prioritize planar stability, bevel support, clean shading, and predictable normals. Do not force character-style quad flow onto every hard-surface form.
5. Retopologize from high-poly references with shrinkwrap/retopo workflows where suitable; preserve silhouette and critical curvature.
6. Check subdivision behavior, weighted normals, bevel behavior, and deformations before approval.
7. Validate triangle/quad/ngon use according to the target engine/export path; ngons are not automatically wrong but can be unsafe for deformation or triangulation-sensitive delivery.
8. Triangulate deliberately when the target pipeline requires predictable triangulation.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-character-retopology`: edge loops for face, shoulders, elbows, hips, knees, hands, and facial animation.
- `blender-hard-surface-topology`: bevel-friendly topology and shading control.
- `blender-subdivision-topology`: support loops and subdivision behavior.
- `blender-normal-and-shading-repair`: normals, smoothing, weighted normals, and shading artifacts.
- `blender-mesh-validation`: manifoldness, degenerates, duplicate geometry, and topology diagnostics.

# Output
Explain topology trade-offs, identify remaining risks, and validate the model in the intended shading/deformation context. Never equate a low polygon count with good topology by itself.
