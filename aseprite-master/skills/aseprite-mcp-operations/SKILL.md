---
name: aseprite-mcp-operations
description: Safely discovers and uses the connected Aseprite MCP server, validates tool schemas, manages files and documents, and recovers from operation failures. Use when an agent first connects to the Aseprite MCP server, must call its tools with the correct schemas and indices, or needs to recover from a failed operation.
---

# Aseprite MCP Operations

## First contact
1. List available MCP tools and read their descriptions and input schemas.
2. Group tools by capability: inspect/read, create/open, canvas/layers/frames, pixel operations, preview/render, save/export, filesystem.
3. Identify required arguments, defaults, return types, indexing conventions, and side effects.
4. If the tool list is empty or incomplete, report that honestly; do not fabricate a tool call.

## Tool invocation rules
- Use only exact tool names and parameters exposed by the connected server.
- Validate paths and document state before destructive or stateful actions.
- Confirm whether indexes are zero-based or one-based before using numeric indices.
- Confirm coordinate origin, canvas bounds, color encoding, and frame timing units.
- Prefer small batches that can be inspected.
- Read tool output and verify the operation actually changed the expected state.
- Do not assume a tool call automatically saves the file.
- Do not assume a reported success means the visual result is correct.

## File safety
- Prefer working copies, versioned outputs, or explicit checkpoints.
- Do not overwrite the user's source file without permission if the operation is destructive or difficult to reverse.
- Use absolute paths only when confirmed by tool output or the user.
- Never invent a sandbox path or claim an export exists without verification.

## Recovery
If a call fails:
1. Capture the exact error.
2. Determine whether the failure is schema, state, path, unsupported feature, or visual issue.
3. Re-inspect the document before retrying.
4. Correct only the failed assumption or argument.
5. Retry once with a bounded change; do not loop indefinitely.
6. If blocked, describe the missing capability and offer a practical alternative.

## Batching
Batch repetitive deterministic operations only after validating the operation on a small sample. For pixel-level operations, prefer a tiny test area before a large canvas operation.
