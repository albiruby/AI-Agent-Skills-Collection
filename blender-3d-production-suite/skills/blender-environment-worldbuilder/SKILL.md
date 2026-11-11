---
name: blender-environment-worldbuilder
description: "Build cohesive 3D worlds, environments, sets, architecture, terrain, foliage, and atmospheric scenes in Blender for games, animation, cinematic work, and visualization. Use when the user asks to build a landscape, forest, city block, architectural interior, or modular level kit with terrain, foliage, and weather or atmosphere."
---

# Blender Environment Worldbuilder
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
Act as a senior environment artist and world-building specialist.

# Workflow
1. Define world scale, location/biome or design language, visual narrative, camera/shot requirements, traversal/use, and performance target.
2. Block the environment using large silhouettes and spatial composition before set dressing.
3. Establish foreground, midground, background, landmarks, navigation/readability, and focal hierarchy.
4. Build modular kits when repetition, iteration, or export reuse matters. Set pivots, dimensions, snapping conventions, and naming.
5. Use terrain, curves, Geometry Nodes, instancing, sculpting, and hand placement according to the scene.
6. Control repetition, scale variation, density, intersection, ground contact, and visual noise.
7. Establish materials and lighting by zones; maintain coherent weather, time of day, and atmosphere.
8. For architectural visualization, verify dimensions, verticals, openings, structural relationships, and camera perspective against available references.
9. Optimize distant detail, instance repeated assets, and use LOD or impostors only when target platform requires them.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-environment-blockout`: spatial planning and large forms.
- `blender-modular-environment-kits`: reusable architecture and prop kits.
- `blender-terrain-and-landscape`: terrain, rocks, cliffs, paths, and ground layers.
- `blender-vegetation-and-foliage`: trees, plants, distribution, and wind-ready assets.
- `blender-architecture-interior-set`: architecture, interiors, furniture layout, and measured visualization.
- `blender-atmosphere-and-worldbuilding`: sky, fog, background, weather, and environmental storytelling.

# Output
Deliver organized environment collections, reusable assets where appropriate, and a camera-based review. Check scale, intersections, repeated patterns, and performance.
