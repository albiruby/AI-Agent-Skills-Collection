# Subskill 11 — Quality Control and Iteration

## Purpose
Evaluate the generated video against the brief and improve it systematically.

## Review dimensions
Score each from 1–5:
1. Brief adherence.
2. Subject/reference fidelity.
3. Action clarity.
4. Temporal coherence.
5. Anatomy and physical interaction.
6. Camera/composition.
7. Visual style.
8. Lighting/color.
9. Audio/text correctness.
10. Technical delivery.

## Critical failures
Reject or repair if:
- The main subject is wrong.
- A required character or product identity is materially altered.
- A critical action does not happen.
- Anatomy or object interaction is visibly broken.
- The style contradicts the brief.
- Unwanted text/audio changes the meaning.
- The output violates platform or user constraints.

## Iteration loop
1. Describe the observed failure precisely.
2. Identify its likely cause.
3. Decide whether to simplify, clarify, reference, split, or post-edit.
4. Change only the relevant prompt section.
5. Regenerate or repair.
6. Compare against the same criteria.

## Avoid
- Rewriting the entire prompt for a single localized error.
- Adding more adjectives without diagnosing the cause.
- Repeating a failed generation strategy unchanged.
- Calling an output perfect without inspection.
- Treating model randomness as proof that the prompt is correct.

## Reporting
Separate objective defects from subjective preferences. State what improved, what remains imperfect, and whether the output meets the user's stated acceptance criteria.

## Physics and interaction gate
- Any clip with physical interaction must pass the checkpoint review in subskill 22 before approval.
- Classify defects with the IDs and severities in subskill 21.
- Critical failures also include: an object moving before contact (A1), a hand passing through an object (A2), ghost grip (A4), an object duplicating or vanishing (D1/D2), wrong finger count on a hero beat (B1), and an incorrect liquid or state change that the brief requires (C9/D5).
- Recovery follows the ladder in subskill 23; do not repeat a failed strategy unchanged.
- Never approve from a single hero frame.
