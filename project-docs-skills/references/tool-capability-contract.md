# Reference: Tool Capability Contract

## Purpose

These skills run across different AI models and harnesses. Never assume a tool exists because another platform has it. Discover the actual capability, use it truthfully, and state the completion level.

## Discover before use

Before an operation, determine:

- Filesystem/repository read and write access.
- Shell/script execution and working directory.
- Image inspection and processing (crop, alpha, resize, compose).
- Browser automation or simulator/emulator/device control.
- Diagram rendering.
- Official platform documentation access.
- Archive creation.
- Permission requirements for external or destructive actions.

Use only documented interfaces and permitted paths. Do not invent tools or APIs.

## Capability fallback matrix

| Need | Preferred | Fallback |
|---|---|---|
| Inspect project | Repository/filesystem | Ask for files/archive |
| Capture app | Simulator/browser/device | Process supplied captures or give manual steps |
| Crop/clean image | Image processing tool | Provide exact crop plan; request better source |
| Compose visual | Image/design tool | Provide composition spec or editable SVG/HTML |
| Draw architecture | Diagram renderer | Mermaid or text diagram |
| Check store requirements | Official docs | Use supplied spec; mark compliance unverified |
| Package | Filesystem + archive | Organize files individually |
| Validate | Script + visual review | Manual checklist; mark visual checks unverified |

## Cross-platform command notes

- Windows: use `python`; `python3` is often a Store alias, not a real interpreter.
- macOS/Linux: `python3` is usually available; use it if `python` is absent.
- Quote paths containing spaces.
- Prefer relative paths from the skill/pack directory.
- Pillow is required by the bundled scripts; numpy is optional. Install only with permission.
- Do not claim a transformation ran because a command was suggested.

## Truthful completion states

- **Created:** file exists and was saved.
- **Processed:** transformation ran and output exists.
- **Reviewed:** visual/content inspection was performed.
- **Validated:** named checks were actually executed.
- **Ready for review:** deliverables exist but approval or a check remains.
- **Store-compliance not verified:** current official requirements were not checked.
- **Published/submitted:** only when the external action actually completed.

Never collapse these into a generic "done".

## Shared pack assets

When the skills are installed as a pack, shared references/templates live at the pack root and are referenced with `../../references/` and `../../templates/`. If a skill folder is copied alone, those files are absent; copy them too or install the whole pack.
