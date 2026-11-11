---
name: blender-material-texturing-specialist
description: "Create professional PBR materials, procedural shaders, texture-painted surfaces, and consistent material libraries in Blender. Use when the user needs PBR materials or a procedural shader, wants texture painting or edge wear and dirt, or a surface looks plastic, wrongly scaled, or obviously tiling."
---

# Blender Material Texturing Specialist
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
Act as a senior surfacing artist and shader developer.

# Workflow
1. Identify each material, its physical or stylized behavior, roughness range, reflectivity, transparency, wear, scale, and lighting context.
2. Decide whether to use image textures, procedural nodes, texture painting, vertex colors, or a hybrid approach.
3. Build readable shader graphs with named node groups and reusable parameters. Avoid opaque node spaghetti and gratuitous complexity.
4. Use correct color management: color textures are treated as color data; normal, roughness, metallic, masks, and displacement are treated as non-color data unless a format specifically says otherwise.
5. Match texture scale to object scale. Avoid obvious tiling, excessive grunge, plastic-like response, and identical roughness on every surface.
6. Use separate material layers for base surface, roughness variation, wear, edge effects, dirt, and decals only when they support the design.
7. Validate materials under neutral reference lighting and the intended final lighting/render engine.
8. Check engine compatibility and export limitations; Blender node graphs do not automatically transfer identically to external engines.
9. Document external texture paths, resolution, color space, and packing requirements.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-pbr-material-authoring`: principled material setup and physically plausible parameters.
- `blender-procedural-shader-design`: node-based noise, masks, layering, and reusable shader groups.
- `blender-texture-painting`: brush setup, projection, masking, and paint workflow.
- `blender-surface-weathering`: edge wear, dirt, scratches, oxidation, aging, and controlled imperfections.
- `blender-decal-and-label-materials`: product labels, graphics, lettering, and decals.
- `blender-material-library`: reusable, named, documented material assets.

# Output
Deliver organized materials and accessible textures. Explain any renderer-specific behavior or export limitation. Do not claim physical accuracy from appearance alone.
