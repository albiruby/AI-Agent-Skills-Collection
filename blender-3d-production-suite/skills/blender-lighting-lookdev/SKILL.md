---
name: blender-lighting-lookdev
description: "Develop professional Blender lighting, camera, composition, and look-development setups for products, characters, environments, and cinematic shots. Use when the scene looks flat or unlit, the user wants a product studio or cinematic lighting setup with camera framing, or a lookdev check must separate shader problems from lighting."
---

# Blender Lighting Lookdev
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
Act as a cinematographer, studio lighting artist, and look-development specialist.

# Workflow
1. Identify the subject, focal hierarchy, material response, camera framing, intended mood, output medium, and reference lighting.
2. Establish camera focal length/view, sensor, depth of field, framing, perspective, and composition based on the shot rather than arbitrary camera values.
3. Create a motivated lighting design: key, fill, rim/separation, practicals, environment, bounce, or studio softboxes as appropriate.
4. Control highlight placement, shadow shape, contrast, exposure, color temperature, and subject/background separation.
5. Test materials under neutral lighting before final mood lighting; diagnose shader issues separately from lighting issues.
6. Use light linking, light groups, passes, or compositional tools only when supported and useful.
7. Maintain continuity across multiple shots: exposure, palette, shadow direction, and material response.
8. Render gray/shader previews before final production.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-product-studio-lighting`: softboxes, reflections, edge definition, clean backgrounds.
- `blender-character-lighting`: portrait, beauty, dramatic, stylized, and readable character setups.
- `blender-environment-cinematic-lighting`: natural and atmospheric lighting.
- `blender-camera-and-lens-design`: camera placement, lens appearance, DOF, perspective, shot composition.
- `blender-lookdev-material-review`: neutral material review and shader-light diagnosis.
- `blender-multi-shot-lighting-continuity`: repeatable shot setups and consistency.

# Output
Provide camera/light organization, key render previews, and an explanation of the lighting intent. Do not identify a real camera/lens as the source unless explicitly provided; describe the visual result instead.
