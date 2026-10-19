---
name: instruction-slot-packager
description: Packs a style bible into the limited instruction fields in Google's tools - Google Flow's 3 instruction slots, a Gemini Gem, an AI Studio system instruction, or a Gemini CLI GEMINI.md - splitting rules into a global slot and asset-type canon slots with character budgets and trimming priorities. Use when the user has a limited number of instruction fields, wants "global rules", "master instruction", "system instruction", or needs copy-ready blocks. Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Instruction Slot Packager

## Purpose
Persistent instructions apply to every generation without being retyped. Use them for rules that never change, and still repeat the lock inside each prompt for safety.

## Slot design (for 3 slots; adapt to N)
| Slot | Name | Contents |
|---|---|---|
| 1 | Global rules | THEME, STYLE, OUTLINE, SHADING, PALETTE, SCALE, EXCLUSIONS, BACKGROUND, OUTPUT, CONSISTENCY |
| 2 | Subject canon | Character cards (Design Locks), proportions, facing rules, sheet geometry, frame consistency |
| 3 | World/asset canon | Tiles, props, items, VFX, UI, backgrounds, reject-and-regenerate rules |

With 1 slot: global rules + a compact subject canon. With 2 slots: global; combined canon. With more: add a slot for camera/composition or for brand/IP rules.

## Budget guidance
Aim for about 1,500-2,200 characters per slot unless the tool states a limit; verify the real limit in the tool. If over budget, trim in this order: examples -> adjectives -> secondary asset types -> duplicated phrases. Never trim the exclusions or the palette line.

## Process
1. Read the bible; mark each rule as GLOBAL (all assets), CANON (by type) or LOCAL (one asset).
2. Fill Slot 1 with GLOBAL only. Use labeled lines (`STYLE:`, `PALETTE:`).
3. Fill Slot 2 and 3 with CANON by asset family. Do not repeat Slot 1 text; reference it ("Same style lock as the global rules").
4. Check contradictions: no slot may override another; if conflict, Slot 1 wins.
5. Count characters per slot.
6. Output each slot as a separate fenced `text` block with a heading, ready to paste.
7. Keep the per-prompt LOCK STYLE & THEME block anyway; it protects consistency if a slot is off or truncated.

## Output template
```
### Slot 1 - Global rules
<fenced block>
### Slot 2 - <name>
<fenced block>
### Slot 3 - <name>
<fenced block>
Version: <bible version> | Characters: <n/n/n>
```

## Maintenance
When the bible changes: bump version, update the affected slots, regenerate only affected assets, and note this in the changelog.

## Pitfalls
- Using slots for per-asset details; they bloat and conflict.
- Different wording of the same rule in slot and prompt. Copy from one source.
- Forgetting that a slot may be disabled in some sessions.

## Gemini notes
- Gemini targets: Gem instructions, AI Studio system instruction, Google Flow instruction slots, Gemini CLI `GEMINI.md`. Ready-made blocks are in `plug-and-play/`. Verify real length limits in each surface before pasting.
