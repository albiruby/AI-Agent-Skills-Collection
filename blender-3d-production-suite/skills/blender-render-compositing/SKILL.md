---
name: blender-render-compositing
description: "Configure Blender render engines and production rendering, manage render passes, color management, compositing, and final image or animation outputs. Use when the user must choose between Cycles and EEVEE, set up render passes or a compositor grade, fix color management problems, or verify a rendered frame sequence."
---

# Blender Render Compositing
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
Act as a rendering TD and compositing artist.

# Workflow
1. Inspect Blender version, available render engines (such as Cycles, EEVEE, or Workbench where present), device compatibility, hardware, scene complexity, and target quality.
2. Choose the engine according to visual needs, supported features, and performance. Verify engine-specific features in the installed version's documentation.
3. Set resolution, percentage, frame range, FPS, samples, denoising, bounces, shadow/refraction options, motion blur, output format, bit depth, color management, and file path intentionally.
4. Use low-cost preview renders to test composition, lighting, materials, noise, and animation timing.
5. Enable only render passes/AOVs required by the composite or grading pipeline.
6. Build organized compositor node trees with named groups and non-destructive grade stages.
7. Check color space, view transform, exposure, contrast, alpha handling, premultiplication, and output color profile.
8. For animation, test representative frames, sequence continuity, disk capacity, crash recovery, and missing-frame detection.
9. Verify actual saved output files: dimensions, frame count, format, alpha, color, and corruption where tools permit.

# Sub-skill workflows included in this skill

The items below are workflow specializations contained in this document. They are not separate installed skills unless a matching skill folder is supplied.
- `blender-cycles-render-td`: path tracing quality/performance and noise control.
- `blender-eevee-render-td`: real-time renderer setup and supported feature checks.
- `blender-workbench-preview`: technical/clay/viewport-style outputs.
- `blender-render-pass-management`: passes, AOVs, masks, and render layers.
- `blender-compositor-node-design`: glare, denoise, grade, masks, depth, lens, and finishing.
- `blender-color-management`: OCIO/view transforms, exposure, output color handling.
- `blender-animation-render-pipeline`: frame sequence output and recovery.

# Output
Report exact render engine, key settings, output paths, and files actually verified. Never equate a successful render command with a verified final deliverable.
