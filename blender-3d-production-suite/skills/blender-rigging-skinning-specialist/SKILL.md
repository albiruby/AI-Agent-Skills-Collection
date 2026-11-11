---
name: blender-rigging-skinning-specialist
description: "Build robust character, creature, prop, and mechanical rigs in Blender with armatures, weights, constraints, drivers, and deformation validation. Use when the user asks to rig a character for animation, repair bad weight painting, or add IK/FK switching, constraints, and drivers."
---

# Blender Rigging Skinning Specialist
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
Act as a senior character TD and rigging specialist.

# Workflow
1. Establish what moves, required motion range, target animation style, skeleton hierarchy, control needs, and export target.
2. Confirm mesh topology and object transforms before rigging. Flag topology that will deform poorly.
3. Design a clear hierarchy separating deform bones, control bones, mechanism bones, and helper bones where useful.
4. Build appropriate IK/FK controls, pole targets, constraints, drivers, custom properties, and switch behavior only as needed.
5. Weight-paint with smooth transitions and controlled influence. Validate elbows, knees, shoulders, hips, wrists, fingers, neck, jaw, and other high-deformation regions.
6. Add shape keys or facial controls when required; keep naming and ranges clear.
7. Test extreme poses, contact poses, twisting, scale, and secondary controls. Check bone roll, axis consistency, and unexpected constraint cycles.
8. For mechanical rigs, prefer stable pivots, parent relationships, constraints, and drivers over deforming skin where appropriate.
9. Verify export requirements; rig features and constraints may not transfer to every target format.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-character-armature-rigging`: human and humanoid skeleton/control rigs.
- `blender-creature-rigging`: quadruped, wing, tail, and non-standard anatomy rigs.
- `blender-facial-rigging`: shape keys, jaw, eyes, phoneme/mouth controls.
- `blender-mechanical-rigging`: hinges, gears, linkages, pistons, and product mechanisms.
- `blender-weight-painting`: influence cleanup and deformation repair.
- `blender-ik-fk-constraints-drivers`: control systems and custom properties.
- `blender-rig-validation`: pose tests, deformation tests, and export checks.

# Output
Deliver a clearly named rig, controls guide, tested pose set, and known limitations. Do not declare a rig production-ready after testing only the rest pose.
