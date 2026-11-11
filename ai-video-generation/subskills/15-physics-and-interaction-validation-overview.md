# Subskill 15 — Physics & Interaction Validation (Overview and Gates)

## Purpose
Make physical plausibility a **systematic, checkable layer** of the production process instead of a vague wish ("make it physically plausible"). This subskill is the hub for subskills 16–23.

## Core insight
Video models learn physics statistically from data; they do not run a physics engine. They are good at producing a believable *moment* and much less dependable at preserving a believable *chain of events*: reach → contact → grip → lift → carry → release, with correct object response at every step.

Reported evidence (secondary sources, verify before quoting; see `references/research-sources.md`):
- Non-contact dynamics (light, fabric, environmental motion, simple fluids) tend to hold up better than contact-based actions.
- Hand-object contact, object permanence, state changes (open/closed, full/empty, broken/intact), and chained cause-and-effect remain the weak zones.
- Complex multi-object or chained-physics prompts can succeed only part of the time; treat them as multi-take jobs.
- Benchmarks (PhyWorldBench, PhyGenBench, VideoScience-Bench, Ego2Act, Physion-Eval) consistently report that visual polish and physical correctness are separate dimensions.

Therefore: **a skill cannot force a model to obey physics.** It can (1) design shots that avoid unnecessary risk, (2) encode interactions so the model has less room to guess, (3) detect failures reliably, and (4) recover systematically.

## The four gates

| Gate | When | What happens | Subskills |
|---|---|---|---|
| A. Risk gate | Before writing the prompt | Classify shot risk (R0–R4), decide simplify / split / hybrid | 15, 16, 19 |
| B. Encoding gate | While writing the prompt | Convert the action into an interaction spec, then into prompt language | 16–20 |
| C. Inspection gate | After generation | Frame-by-frame QA at checkpoints, classify errors with the taxonomy | 21, 22 |
| D. Recovery gate | After a failed inspection | Walk the recovery ladder; change one variable at a time | 23 |

No clip containing physical interaction is "approved" until it has passed Gate C. A single attractive frame never approves a shot.

## Shot risk tiers

| Tier | Typical content | Default policy |
|---|---|---|
| R0 | No interaction: landscapes, ambient motion, camera moves, light/weather | One attempt is often enough. Normal-speed review. |
| R1 | Body motion with no object contact: walking, turning, waving, dancing | Check balance, foot contact, anatomy. Light frame review. |
| R2 | One simple object contact: pick up a cup, press a button, sit down | Interaction spec required. Full Gate C on the contact window. Plan several takes. |
| R3 | Multi-step or constrained contact: pick up and carry, pour, open a door and pass through, handoff, tool use | Interaction spec and continuity ledger required. Prefer splitting into shots. Plan many takes. |
| R4 | Precision, mechanical, or causal-state actions: tying, folding, assembling, eating, breaking/shattering, mixing liquids, product-mechanism demos, scientific demonstrations, exact counts | Do not rely on one generation. Plan hybrid production (real footage, compositing, simulation, or an implied/off-screen action) unless the user accepts risk. |

Planning heuristic for take budgets (not a statistic; adjust to the model and credits): R0–R1: 1–3 takes; R2: 3–5; R3: 4–8; R4: 6+ or go hybrid. State the assumption to the user when credits matter.

## Raising or lowering the tier
Raise the tier when: close-up on fingers, multiple hands, small or thin objects, transparent/reflective objects, liquids that must change level, long continuous takes, fast motion, handoffs, occlusion of the contact, or exact counts.
Lower the tier when: one hand, large simple handle, object resting on a stable surface, medium shot, short clip, slow deliberate motion, a cutaway that implies the action.

## Intentional surreal or "anti-physics" shots
If the user wants impossible behavior (a watering can that floats to the character), treat it as a designed effect:
1. State the rule of the impossible event ("the can glides to her open palm").
2. Give it a visible cause or signal (glow, gesture, wind, string, music beat).
3. Keep everything else physically consistent so the effect reads as deliberate.
Accidental levitation and intentional levitation look different to a viewer: intentional events have a trigger, a path, and a consistent behavior.

## Honest reporting
- Never claim a clip is physically correct without inspecting the frames.
- If the agent cannot view video, say so and give the user the checklist and scripts (`scripts/`) instead of pretending to have reviewed it.
- Separate **objective defects** (object moves before contact) from **taste** (the grip looks slightly stiff).

## Output
For any R2+ request produce: risk tier, interaction spec (`templates/interaction-spec.md`), encoded prompt, fallback plan, and the QA checkpoints to apply.
