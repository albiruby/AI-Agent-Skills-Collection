# Subskill 16 — Object Interaction Protocol

## Purpose
Give every object interaction a **complete, ordered physical sequence** so no step is skipped or implied. Most "the object flew away instead of being grabbed" errors come from compressing or omitting contact, grip, and transfer beats.

## Golden rules
1. **Objects are inert until a force acts on them.** An object only moves if a hand/body/tool is in contact, gravity acts, a surface beneath it moves, wind/fluid acts, or the user designed a visible magical cause.
2. **Cause precedes effect.** The hand touches before the object moves; the lever turns before the door opens.
3. **No skipped beats.** reach → contact → grip → lift is four beats, not one jump.
4. **One interaction at a time.** Do not overlap two contact events in the same few seconds unless essential.
5. **The object responds to the hand, not the other way around.** The hand's path is planned around the object's geometry.
6. **State changes are explicit.** Say what is different before and after (closed→open, on bench→in hand, empty→full).

## Universal interaction phases
| # | Phase | What must be visible | Common failure |
|---|---|---|---|
| 0 | Pre-state | Object at rest in a stable place; subject's pose known | Object already drifting |
| 1 | Intent | Gaze/body turns toward the object | Subject acts on the wrong object |
| 2 | Approach | Hand/body moves along a plausible path | Object moves toward hand (A1) |
| 3 | Alignment | Hand orientation matches the handle/surface | Wrong palm angle, fingers misaligned |
| 4 | Contact | Visible touch; no gap, no pass-through | Hand passes through or hovers (A2/A5) |
| 5 | Secure / grip confirmation | Fingers closed on the correct part; object still unmoved until now | Ghost grip (A4) |
| 6 | Transfer | Lift/push/pull/open; object follows the hand with believable weight | Object lags, floats, or leaps (A6/C1/C2) |
| 7 | Release | Fingers open or hand withdraws; object supported | Hover after release (A9) |
| 8 | Settle | Object responds (rests, swings, stops) | Object keeps drifting |
| 9 | Post-state | New state matches the brief | Wrong state/orientation (D5) |

## Verb protocols
Each protocol lists required beats, the contact point, the expected object response, what to watch, and a safer variant for unstable models.

### Grab / pick up
- Beats: gaze → approach → align hand to the named part (handle) → fingers close → brief grip pause → lift.
- Contact: name the part (handle, rim, strap), the hand (anatomical right/left), and the grip type (see subskill 19).
- Response: object stays put until fingers close; then rises with the hand; shadow and support surface change accordingly.
- Watch: pre-contact motion, pass-through, wrong part, non-follow.
- Safer variant: object already at hand height on a table edge; one hand; medium shot; or cut from "hand closes on handle" to "can held at her side".

### Hold
- Beats: stable grip → posture adapts to weight → object orientation stays consistent.
- Watch: object drifting in the hand, orientation flipping, fingers changing count.
- Safer: hold at the side or against the body (supported) rather than extended at arm's length.

### Lift
- Beats: slight settle/bend → grip tightens → object rises with the hand, same speed and path.
- Response: weight cue (arm tension, torso lean, slower start for heavy objects). Contents slosh if liquid.
- Safer: short lift height; avoid lifting overhead.

### Carry
- Beats: object stays attached to the same hand and same part for the whole carry; body counterbalances; gait remains natural.
- Watch: object changing hands, size, or distance from the body; feet sliding.
- Safer: short path; side-on or tracking shot; avoid turning while carrying.

### Place / set down
- Beats: approach surface → lower → object contacts surface (contact shadow appears) → hand releases → hand withdraws → object stays.
- Watch: object floats above the surface; passes into the surface; moves after release.
- Safer: flat, stable surface; large object; keep the hand in frame until after release.

### Push
- Beats: hand/body contacts → force builds → object starts moving → decelerates by friction → stops.
- Watch: object moves before contact, moves without a hand, slides forever.

### Pull
- Beats: grip → pull → object follows along the line of pull; the puller leans back.
- Watch: object moves in a different direction than the pull.

### Open (hinge door, lid, drawer, sliding door)
- Beats: reach handle → grip → move along the mechanism's path (arc for hinge, line for slide) → stop → hand releases.
- Specify the hinge side and swing direction. The opening must come from the mechanism's own path.
- Watch: door opens before contact, passes through the character, changes hinge side, handle disappears.
- Safer: character already holding the handle in frame 1; or an off-screen action.

### Close
- Reverse of open. Object returns to the original geometry. Check the latch/closed state.

### Press (button/switch)
- Beats: finger approaches → touch → small depression/click → hand withdraws → state change (light on).
- Watch: state changes before the press; finger passes through the panel.

### Turn (knob/dial/tap/valve)
- Beats: grip → rotation about the object's axis → stop → release; effect (water flows) begins only after rotation.

### Pour
- Beats: lift container → tilt gradually → liquid exits only after the lip passes the horizontal threshold → liquid falls along gravity → level in source falls, level in target rises/soil darkens → tilt back.
- Watch: liquid appears before tilt, flows upward, source level unchanged, target dry.
- Safer: wide/medium framing; short pour; spray/rose head (droplets) instead of a thin stream; avoid showing the interior.

### Hand off / pass
- Beats: giver extends → receiver reaches → both hands contact the object → giver releases → receiver secures → hands separate.
- Watch: object duplicates, shared ownership, floating between hands. High risk (R3); prefer a table drop/pickup or a cut.

### Throw / catch
- Highest risk. Beats: wind-up → release → ballistic arc → catch. Prefer to avoid or hybridize (R4).

### Put on / wear
- Beats: pick up → align to body → contact → settle. Hats, glasses and bags are high-risk for clipping.

### Sit / stand
- Support contact: hips settle onto the seat; weight transfers; the chair does not move unless pushed.

### Use a tool
- Tool is an extension of the hand: grip stays on the handle; the working end contacts the target; target responds proportionally. High risk when the effect is precise.

## Writing the interaction into the prompt
Use present-tense, chronological, concrete sentences, for example:
"Her right hand reaches the top handle of the green watering can on the bench. Her fingers close around the handle, then she lifts the can; the can stays still until she grips it."
Rules: name the part, name the hand, state that the object stays still until contact, state the lift as following the hand. Avoid ambiguous verbs ("grabs at", "gets", "takes" alone), vague handles ("the can"), and cinematic fluff in the contact sentence.

## Output
Complete `templates/interaction-spec.md` for every R2+ interaction, then encode it using `references/prompt-patterns-interactions.md`.
