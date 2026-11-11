---
name: blender-uv-baking-specialist
description: "Prepare production-ready UV maps and bake texture data from high-poly to low-poly Blender assets with controlled texel density and artifact validation. Use when the user asks to unwrap a model, pack UV islands, fix seams or inconsistent texel density, or bake normal and AO maps from a high-poly onto a low-poly mesh."
---

# Blender UV Baking Specialist
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
Act as a UV layout and texture-baking specialist.

# Workflow
1. Confirm target texture resolution, number of texture sets, UV tile strategy, target renderer/engine, and real-time/offline use.
2. Plan seams around hidden, low-curvature, or natural boundaries where appropriate; avoid seams through focal/deformation areas when possible.
3. Unwrap and pack UV islands with consistent orientation, sufficient padding, minimal distortion, and intentional texel density.
4. Keep UV maps named and organized. Identify which UV map is for textures, lightmaps, or other target-specific purposes.
5. Prepare high/low correspondence, cage or ray distance, object transforms, material assignments, and bake output settings.
6. Bake only maps required by the target: normal, ambient occlusion, curvature, diffuse/base color, roughness, metallic, emission, displacement, or custom masks.
7. Verify correct tangent-space convention and target format. Do not assume a normal-map convention without checking the renderer/engine.
8. Inspect seams, skewing, overlaps, projection misses, cage artifacts, gradients, and padding at full resolution.
9. Save bake sources and ensure baked textures are correctly named, color-space tagged, and stored.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-uv-unwrapping`: seam planning, unwrapping, island cleanup.
- `blender-texel-density`: consistent pixel density and resolution budgeting.
- `blender-uv-packing`: island packing, padding, rotation, and atlas planning.
- `blender-high-to-low-baking`: normal/AO/curvature and other bake workflows.
- `blender-bake-artifact-diagnosis`: skew, cage, seam, projection, and tangent-space fixes.

# Output
Provide UV maps and baked textures, their resolution/color-space, and verification notes. Never report a successful bake without checking the generated images.
