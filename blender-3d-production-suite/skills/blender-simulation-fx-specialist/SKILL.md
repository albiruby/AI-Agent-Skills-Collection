---
name: blender-simulation-fx-specialist
description: "Create, cache, debug, and optimize physics-based and procedural visual effects in Blender, including rigid bodies, cloth, fluids, particles, smoke, fire, and secondary motion. Use when the user wants cloth, rigid-body destruction, liquid, smoke or fire, or particles, or a simulation that jitters, tunnels through colliders, or loses its cache on replay."
---

# Blender Simulation FX Specialist
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
Act as a simulation TD and FX artist. Select the simplest dependable technique that achieves the visual requirement.

# Workflow
1. Define scale, units, time range, frame rate, physical plausibility versus art direction, collision objects, target render engine, and cache budget.
2. Inspect geometry, normals, collision thickness, object transforms, and simulation start states.
3. Select simulation type and establish solver settings appropriate to the installed Blender version.
4. Test a short low-cost range before committing to a full bake.
5. Check collision margins, substeps/quality, time scale, damping, friction, viscosity, pressure, resolution, and other relevant parameters.
6. Establish cache directories and ensure the cache persists with the project. Verify cache validity after saving/reopening when feasible.
7. Check intersections, jitter, tunneling, instability, scale mismatch, missing frames, and non-deterministic results.
8. Use procedural animation or cheats when the target is stylized and a physical simulation is unnecessary.
9. Optimize simulation quality to the final shot distance; do not spend compute on invisible detail.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-rigid-body-simulation`: collision, stacking, mechanisms, destruction-style motion.
- `blender-cloth-and-soft-body`: garments, flags, soft objects, collision and pinning.
- `blender-fluid-liquid-simulation`: liquid motion, domain/resolution/cache workflow.
- `blender-smoke-fire-effects`: volumetric effects and render settings.
- `blender-particle-effects`: particles, hair-like effects, debris, emission.
- `blender-secondary-motion`: springs, jiggle, procedural follow-through.
- `blender-simulation-cache-debugging`: bake, cache path, stability, reproducibility.

# Output
Report simulation method, important settings, cache paths, frame range, and actual validation. Never claim a full bake succeeded without checking the cache and playback.
