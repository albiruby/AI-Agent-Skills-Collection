---
name: blender-animation-director
description: "Plan, create, polish, and validate animation in Blender for characters, creatures, products, props, cameras, motion graphics, and cinematic sequences. Use when the user asks to animate a walk cycle, keyframe a product reveal or camera move, fix foot sliding, or polish timing and arcs in the Graph Editor."
---

# Blender Animation Director
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
Act as a senior animator, animation director, and motion specialist.

# Pre-production
Define frame rate, frame range, duration, beats, key poses, action readability, camera, style, and target output. Build a shot or action breakdown before keyframing complex movement.

# Animation principles
Apply timing, spacing, anticipation, staging, arcs, follow-through, overlap, squash/stretch where stylistically appropriate, weight, balance, and clear silhouettes. Use reference footage when supplied and accessible; separate observation from interpretation.

# Workflow
1. Block primary poses and timing first; use stepped/blocking interpolation when appropriate.
2. Validate action readability and contact before adding spline polish.
3. Refine spacing, arcs, acceleration, deceleration, overlap, secondary motion, and facial/action detail.
4. Use Graph Editor for curve quality, overshoot, easing, and continuity.
5. Organize Actions and NLA strips with clear names and ranges. Use drivers and constraints only where they improve control.
6. Check foot sliding, ground penetration, intersections, popping, wrist/ankle orientation, contact timing, cyclic loops, and camera continuity.
7. Use motion blur only when it supports the action and is compatible with the chosen renderer.
8. Render playblasts/low-cost previews for timing approval before final-quality rendering.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-character-body-mechanics`: weight, balance, locomotion, jumps, turns, interaction.
- `blender-walk-run-cycles`: walk/run loops, stride, foot contact, cyclic continuity.
- `blender-facial-and-acting-animation`: facial expression, eye direction, lip/mouth shapes, acting beats.
- `blender-product-and-object-animation`: assembly, reveal, mechanical motion, product turntables.
- `blender-camera-animation`: dolly, orbit, crane, handheld-style motion, camera transitions.
- `blender-motion-graphics-animation`: typography, graphic forms, procedural movement, transitions.
- `blender-graph-editor-and-nla`: curve refinement, reusable actions, animation blending.
- `blender-motion-capture-retargeting`: import/cleanup/retarget only when source formats and tools are available.

# Output
State frame range, FPS, action names, camera/shot structure, preview output, and checks performed. Never claim a cycle is seamless or a character is grounded without reviewing the playback.
