# Subskill 06 — Motion and Physical Interaction

## Purpose
Make movement coherent, readable, and physically plausible.

## Action design
For each action, define:
- Starting pose/state.
- Trigger or intention.
- Movement path.
- Contact point.
- Object response.
- Ending pose/state.

## Physical logic
Check:
- Gravity and support.
- Weight and momentum.
- Reach and joint range.
- Hand/object contact.
- Object permanence and continuity.
- Foot placement and balance.
- Collision and occlusion.
- Cause and effect.

If the user intentionally wants impossible or surreal motion, preserve the intended style while making the action visually legible.

## Complexity control
- Limit simultaneous actions.
- Avoid many small finger movements unless essential.
- Reduce complex handoffs or interlocking mechanisms.
- Prefer one clear interaction over multiple overlapping interactions.
- Keep props stable and easy to identify.
- Use explicit start/end states for transformations.

## Character motion
Maintain anatomy, gait, proportions, and outfit during movement. Avoid unnecessary spins or rapid movement when identity consistency is critical.

## Output
Provide concise chronological action beats and identify likely motion risks.

## Strict validation layer
This subskill sets the basic motion logic. For any shot with hand-object contact, carrying, pouring, opening, or other physical interaction (risk tier R2 or higher), also use:
- `15` risk tiers and gates, `16` interaction protocol, `17` contact logic, `18` gravity and dynamics, `19` hand-object interaction, `20` continuity, `21` error taxonomy, `22` frame-by-frame QA, `23` failure recovery.
"Physical plausibility" is not a prompt instruction by itself; encode the contact beats and verify them in the frames.
