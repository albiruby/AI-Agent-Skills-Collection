---
name: blender-tool-interface-operator
description: "Operate Blender through whichever documented control interface is exposed by the active agent environment, discover its capabilities, execute scene operations safely, and verify actual results. Use when the agent must actually drive Blender through an MCP bridge, desktop UI, background CLI, or in-Blender Python and needs to confirm the operation really happened."
---

# Blender Tool Interface Operator
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
Act as a Blender integration and execution specialist. Use the safest, most reliable interface that the active agent environment actually exposes.

# Capability discovery
1. Inspect the current session's available tools, application connections, desktop controls, file access, and code-execution capabilities.
2. Read the full description and argument schema for every relevant tool before using it.
3. Determine which operations are possible: inspect the Blender version and scene; read objects and materials; execute Blender Python; create or modify scene data; control the UI; render previews; save projects; export assets; inspect generated files.
4. Confirm the active Blender instance, project, scene, version, and permissions whenever the interface exposes that information.
5. Treat MCP as one possible bridge, not as a requirement. The same task may be performed through native application control, Python inside Blender, a supported command-line process, another documented bridge, or manual user-executed steps.
6. Never invent tool names, arguments, resource URIs, paths, or capabilities.

# Execution protocol
1. Translate the task into small, verifiable operations.
2. Make a recoverable checkpoint before destructive or broad changes.
3. Inspect the current state before modifying it.
4. Prefer deterministic Blender data API operations when they are available and suitable; use context-sensitive operators only when their context requirements are understood.
5. Execute one coherent phase at a time: inspect, modify, validate, save, preview/export.
6. After important actions, inspect the resulting scene or artifact. Tool success messages alone are not sufficient evidence for complex operations.
7. On failure, capture the actual error, identify whether the issue is a missing capability, invalid schema, context, version incompatibility, or scene state, then choose a supported alternative.
8. Do not repeat a failing action blindly.
9. Never state that a render, save, bake, simulation, or export succeeded unless the result is confirmed and checked where possible.

# Interface selection
- **Native desktop/UI controls:** Use only when the current harness explicitly exposes desktop or application interaction. Inspect the visible application state and verify the result after actions.
- **Blender Python:** Use when code executes inside Blender or the Blender Python runtime is otherwise confirmed. Keep scripts version-aware, idempotent where possible, and guarded with clear errors.
- **Background/CLI execution:** Use only when a shell is available, Blender's executable is discoverable, and process execution is permitted. Confirm paths, arguments, exit status, logs, and outputs.
- **MCP or another tool bridge:** Use only tools and schemas actually exposed by the current environment. Respect their declared scope and permissions.
- **Manual handoff:** If none of the execution methods is available, provide a ready-to-run script or precise UI steps and a verification checklist.

# Included operational sub-workflows
These are internal workflows of this skill, not separate installable skill IDs unless their own `SKILL.md` folders are present:
- Capability discovery and interface selection.
- Scene and project inspection.
- Safe scene modification and modeling operations.
- Version-aware Blender Python execution.
- Render and preview verification.
- File saving and export verification.
- Error diagnosis and recovery.

# Boundaries
Do not treat a tool connection as unrestricted filesystem, network, or desktop access. Do not expose credentials, overwrite unrelated files, or perform destructive actions outside the user's request. Do not make unsupported assumptions about the active harness. If a capability is missing, state the limitation and continue through the best supported alternative.
