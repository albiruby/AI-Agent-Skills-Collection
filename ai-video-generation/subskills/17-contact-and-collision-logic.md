# Subskill 17 — Contact and Collision Logic

## Purpose
Make sure two things that touch in the story **visibly touch** in the frames, and two things that should not overlap **never overlap**.

## Contact types
| Type | Example | Visual proof |
|---|---|---|
| Support | Feet on ground, can on bench | Contact shadow, slight compression, no gap |
| Grip | Fingers around a handle | Fingers wrap the part; skin/fabric presses; object follows |
| Pressure | Finger on a button | Touch point, small depression, state change after |
| Friction | Object sliding on a table | Gradual deceleration; no perpetual glide |
| Impact | Ball hits a wall | Deflection, deformation, sound sync, energy loss |
| Fluid | Water hitting soil | Splash/spread, darkening, level change |

## Contact test (use in prompts and in QA)
For every contact event confirm four things in order:
1. **Gap closes.** Distance between the two surfaces goes to zero smoothly.
2. **Touch is visible.** The camera angle shows the contact area or its unmistakable consequence.
3. **Response follows.** The object responds only after touch, proportional to the force.
4. **Separation is clean.** After release the surfaces separate without sticking, floating, or pass-through.

## Interpenetration (clipping) rules
- Solids do not pass through each other. Hands wrap around handles; they do not pass through the handle's solid parts.
- Limbs do not pass through the torso, tables, doors, or chairs.
- Clothing may deform but must not swallow hands or objects.
- Hair and fabric are soft: slight overlap with a body is tolerated only if it is momentary and not on a hero moment.

## Occlusion is not contact
Hiding contact behind the body, an object, or a frame edge can be a legitimate editorial choice, but:
- The model must still resolve what happens behind the occluder. The object must emerge in a consistent position and state.
- Do not use occlusion to hide a failure you were asked to show (a demo must show the real interaction).
- If you rely on occlusion to avoid risk, state it in the plan and verify the object on re-emergence (subskill 20).

## Support and ground contact
- Feet land on the ground with weight transfer; no skating (foot slides while the body travels).
- Objects on surfaces have contact shadows; floating objects usually lack them or have a gap.
- Surfaces don't change height, tilt, or position without cause.
- Uneven terrain: feet adapt; the body's height changes smoothly.

## Collision outcomes by material
| Material | Expected behavior |
|---|---|
| Rigid (metal, plastic can) | Little deformation; clear deflection; possible sound |
| Soft/foam | Compression then recovery |
| Elastic (rubber ball) | Bounce with diminishing height |
| Glass/ceramic | Fragile; breaking is R4 — do not rely on a model for convincing shatter |
| Liquid | Splash, spread, level change |
| Cloth | Drapes, folds, secondary motion |

## Framing for contact
- Make sure the contact area is **inside the frame and unobstructed** at the moment of contact.
- Prefer **medium or medium-wide framing** that shows the whole chain (body → arm → hand → object). Extreme close-ups of fingers expose anatomy errors; extremely wide shots make contact unreadable. Choose by the risk tier and test.
- Avoid camera moves during the contact beat; keep the camera static or very slow so errors are not hidden or amplified.

## Prompt phrasing for contact
Good: "Her right fingers wrap around the top handle", "the can rests on the bench until she lifts it", "the boot meets the ground with a clear footfall."
Weak: "she grabs the can" (no part, no hand), "the can comes to her" (reads as motion without cause).

## Checklist
- [ ] Contact area visible at the moment of touch
- [ ] No interpenetration of solids
- [ ] Contact shadows/support cues present
- [ ] Object response begins after contact, not before
- [ ] Release is clean; object remains supported
- [ ] No sliding/skating beyond what friction allows
