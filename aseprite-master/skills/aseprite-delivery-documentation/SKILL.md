---
name: aseprite-delivery-documentation
description: Produces clear handoff notes for Aseprite asset work, documenting outputs, verified properties, assumptions, QA, and remaining limitations. Use when Aseprite work is finished and the user needs a handoff report stating what was made, exported, verified, assumed, and still missing.
---

# Delivery Documentation

## Handoff report
Use this structure:
- **Status:** complete / partial / blocked
- **Asset:** what was made
- **Source file:** verified path or unavailable
- **Exports:** verified paths and formats
- **Dimensions:** canvas and frame dimensions
- **Animation:** frame count, timing, loop behavior
- **Visual checks:** checks actually performed
- **Technical checks:** checks actually performed
- **Assumptions:** decisions made because the brief was incomplete
- **Known issues:** remaining defects or unsupported checks
- **Next step:** only if needed

## Reporting integrity
- Separate completed work from planned work.
- Distinguish tool-reported success from inspected visual correctness.
- Never claim a file was saved, exported, opened, or tested without evidence.
- Avoid vague claims such as “100% perfect” or “fully optimized.”
- If the result is partial, explain what is missing and why.
