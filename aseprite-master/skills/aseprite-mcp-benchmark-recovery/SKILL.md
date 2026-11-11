---
name: aseprite-mcp-benchmark-recovery
description: Tests Aseprite MCP capabilities safely, establishes a baseline, measures operation reliability, and recovers from tool errors without fabricating results. Use when an agent must verify what the connected Aseprite MCP server can actually do before production work, or when a tool call fails and needs a bounded recovery instead of blind retries.
---

# MCP Benchmark and Recovery

## Purpose
Determine what the connected server can actually do, how it reports success, and which operations are safe enough for production workflows.

## Baseline test
1. Discover tools and read schemas.
2. Categorize operations: inspect, create/open, edit, frame/layer operations, preview, save, export.
3. Identify any operations with destructive side effects.
4. Use a disposable test document or safe copy.
5. Run one small representative operation per capability.
6. Verify the resulting document state or exported file.
7. Record outcome, error, side effect, and verification method.

## Benchmark log fields
- tool name exactly as exposed
- operation tested
- input shape (omit secrets)
- initial state
- result/error
- observable state change
- verification method
- repeatability
- recovery method
- status: verified / partially verified / unavailable

## Reliability rules
- Do not benchmark on the user's only source asset.
- Do not run destructive tests without explicit approval.
- Do not use speed alone as the success metric; correctness and repeatability matter more.
- Distinguish “tool returned success” from “asset change verified.”
- Avoid large batch tests until a single operation is validated.
- Never claim a percentage success rate without a defined sample and actual recorded results.

## Error taxonomy
- schema mismatch
- missing or disconnected server
- unsupported capability
- document not open / wrong active document
- invalid path or permission
- invalid frame/layer/coordinate index
- save/export failure
- timeout or partial completion
- operation succeeded but visual output is incorrect

## Recovery protocol
1. Stop repeating the same failing call.
2. Capture the exact error and current document state.
3. Check tool schema and assumptions.
4. Re-open or inspect the target if safe.
5. Make one bounded correction.
6. Retry once where appropriate.
7. Verify outcome.
8. If still blocked, report the limitation and a safe alternative.

## Final capability report
List verified capabilities, partially verified capabilities, unavailable capabilities, known hazards, and recommended workflow. Do not infer capability from the Aseprite application itself; the MCP server may expose only a subset.
