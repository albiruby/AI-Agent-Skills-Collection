---
name: aseprite-game-engine-handoff
description: Prepares Aseprite assets for game-engine integration, including pivots, animation states, naming, collision/hitbox notes, and importer requirements. Use when exported sprites must be delivered into Unity, Godot, Unreal, or another engine and the user needs pivots, state names, sheet slicing, or hitbox notes defined.
---

# Game Engine Handoff

## Establish the contract
Confirm target engine and importer version if relevant. Determine:
- Required source/export format
- Sprite dimensions and pixels-per-unit assumptions
- Animation names and state names
- Pivot/origin convention
- Sprite sheet slicing rules
- Filtering and compression expectations
- Collision, hurtbox, or hitbox requirements
- Naming conventions and folder layout

## Animation state design
Use clear names such as `idle`, `walk`, `run`, `jump`, `fall`, `land`, `attack`, `cast`, `hurt`, `death`. Match the user's actual state machine; do not add unrequested states.

## Pivot and alignment
- Keep feet/ground contact aligned for locomotion unless a deliberate hop is required.
- Keep attack origin and weapon reach consistent.
- Document per-frame offsets if the engine cannot use a shared pivot.
- Verify frame bounds and padding so weapons/effects are not clipped.
- Separate VFX from the character if independent timing or layering is needed.

## Hitbox documentation
Do not infer exact gameplay hitboxes from art alone. Ask for gameplay intent or label hitbox notes as provisional. Distinguish visual sprite bounds from collision bounds.

## Handoff package
Include:
- Source file
- Exported sheet or frames
- Frame dimensions and count
- Animation names and timing
- Pivot/origin convention
- Suggested collision/hitbox notes, clearly labeled
- Import instructions only for the confirmed engine
- Known limitations and validation performed
