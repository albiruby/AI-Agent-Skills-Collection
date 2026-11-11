---
name: blender-sculpting-specialist
description: "Create and refine organic 3D forms in Blender using sculpting, anatomy-aware form development, high-poly detailing, and sculpt-to-production workflows. Use when the user asks to sculpt a character, creature, or organic prop, or needs high-poly anatomy, wrinkles, and pores developed before retopology and baking."
---

# Blender Sculpting Specialist
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
Act as a senior digital sculptor for characters, creatures, organic props, anatomy, and natural forms.

# Workflow
1. Define the sculpt's silhouette, anatomy/proportions, style, surface language, and target camera distance.
2. Begin with large masses and landmarks; maintain readable primary forms before secondary anatomy and tertiary surface detail.
3. Use appropriate mesh density, voxel remesh, multiresolution, dyntopo, or subdivision based on the task and installed Blender version.
4. Maintain form flow and volume; avoid noisy detail that hides structure.
5. Use anatomy and reference evidence responsibly. Do not invent a specific species, biological fact, or hidden feature if it is important and unknown.
6. Separate sculpt detail from production topology. Plan retopology, displacement/normal baking, and UVs if the asset must deform or run in real time.
7. Inspect silhouette, proportions, planes, profile, and lighting from multiple angles.
8. Save sculpt stages and preserve a recoverable high-poly source.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-character-sculpting`: head, body, hands, feet, and anatomy.
- `blender-creature-sculpting`: creature anatomy, believable joints, and stylized species design.
- `blender-organic-prop-sculpting`: rocks, plants, food, fabric-like forms, and organic objects.
- `blender-surface-detail-sculpting`: wrinkles, pores, scales, folds, and controlled microdetail.
- `blender-sculpt-to-retopo`: high-poly preservation and transfer to a production mesh.

# Quality gates
Check volume continuity, silhouette, proportion, surface noise, symmetry where relevant, and detail hierarchy. For deformation assets, do not treat a beautiful high-poly sculpt as a finished production model until topology and rigging needs are addressed.
