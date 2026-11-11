# Subskill 08 — Temporal Continuity and Multi-Shot Design

## Purpose
Preserve continuity within a clip and across shots when continuity is required.

## Within-shot continuity
Track:
- Character identity and appearance.
- Outfit, accessories, and held objects.
- Position and orientation.
- Lighting direction and intensity.
- Environment and prop placement.
- Weather and time of day.
- Object state before and after interaction.

## Across-shot continuity
Create a continuity ledger:
- Character state.
- Prop state.
- Screen direction.
- Location geography.
- Lighting and time.
- Previous shot end state and next shot start state.

Use a reference frame or generated keyframe when supported. Do not assume the model remembers previous generations automatically.

## Temporal planning
For each beat, specify what changes and what remains stable. Avoid impossible simultaneous states or unexplained object jumps.

## Multi-shot workflow
1. Define scene order and purpose.
2. Design each shot independently.
3. Establish continuity anchors.
4. Generate shots or keyframes.
5. Review transitions and state matching.
6. Repair discontinuities in editing or regenerate only the affected shot.

## Independent clips
Do not impose continuity between unrelated standalone videos unless the user requests a series or recurring narrative.

## Strict object tracking
For shots with interactions, keep a per-object ledger (identity, count, size, orientation, state, attachment) and use the first/last-frame or reference-image hand-off when the tool supports it. See subskill 20 and `templates/continuity-ledger.md`.
