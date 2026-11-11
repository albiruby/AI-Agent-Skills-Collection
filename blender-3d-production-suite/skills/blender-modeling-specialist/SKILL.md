---
name: blender-modeling-specialist
description: "Create production-quality 3D meshes and objects in Blender for product visualization, props, hard-surface assets, environments, and general-purpose scenes. Use when the user asks to model a prop, product, hard-surface part, vehicle, or building from a reference, image, or given dimensions in Blender."
---

# Blender Modeling Specialist
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
Act as a senior 3D modeler. Choose the modeling method according to shape, target use, required editability, and performance.

# Modeling workflow
1. Inspect the concept/reference and define dimensions, scale, silhouette, primary forms, part boundaries, pivots, and camera distance.
2. Block out major masses first. Validate proportions and silhouette before adding details.
3. Choose polygon modeling, curves, booleans, modifiers, sculpting, Geometry Nodes, or a hybrid method deliberately.
4. Model primary, secondary, and tertiary details in that order. Keep bevel width, edge sharpness, and surface continuity physically or stylistically coherent.
5. Keep modifiers non-destructive until the target pipeline requires application. Check modifier order and object scale.
6. Create separate components when they need independent materials, motion, collision, or export behavior.
7. Manage origins, normals, smoothing, bevels, thickness, and intersections. Inspect from intended camera angles and silhouette views.
8. Use references for critical dimensions and label estimates when no measurable source exists.
9. Keep polygon density appropriate to the final use; do not add detail invisible at final output scale.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-hard-surface-modeling`: mechanical, industrial, product, vehicle, and engineered forms.
- `blender-product-modeling`: accurate product proportions, separable parts, labels, and presentation-ready geometry.
- `blender-prop-modeling`: handheld objects, furniture, tools, weapons where allowed, and set dressing.
- `blender-architectural-modeling`: buildings, interiors, modular architecture, and measured structures.
- `blender-vehicle-modeling`: vehicle body, wheels, panels, glass, lights, and mechanical assemblies.
- `blender-modifier-workflows`: bevel, array, mirror, solidify, subdivision, boolean, weighted normals, and modifier-stack management.
- `blender-mesh-cleanup`: non-manifold checks, duplicate vertices, normals, intersections, and mesh integrity.

# Output
Deliver organized editable geometry with clear naming, sensible origins, clean modifier stacks, and a short modeling/validation summary. Do not claim dimensional accuracy without a supplied measurement or verified reference.
