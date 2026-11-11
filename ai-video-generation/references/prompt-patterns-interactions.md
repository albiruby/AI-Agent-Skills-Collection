# Prompt Patterns for Physical Interactions (copy-ready)

Replace bracketed parts. Keep the contact sentence short and concrete. Adapt to the model's verified prompt style (subskill 10).

## General block
```
[Shot size, static camera]. [Subject, outfit] in [location]. [Object: material, color, key part] rests on [surface] and stays still until [subject] grips it.
Action: [subject]'s [right/left] hand reaches for the [named part], fingers close around it, [short pause], then [lift/transfer verb] the [object] with [weight cue]; [object response following the hand].
End state: [position/state].
```

## Pick up and carry (single hand)
"Medium shot, static camera. A woman in a green apron stands by a wooden bench in a sunny garden. A green metal watering can with a top handle rests on the bench and stays still. Her right hand reaches the top handle, her fingers wrap around it, she pauses for a moment, then lifts the can; the can rises with her hand. She carries it at her side toward the plants, leaning slightly to counterbalance."

## Set down
"She lowers the can until its base touches the bench; a soft contact shadow appears; she opens her fingers and withdraws her hand; the can stays on the bench."

## Pour / water plants (droplet version, lower risk)
"She tilts the can slowly toward the plants; water sprays in small droplets from the rose head, arcs downward and darkens the soil; she tilts the can back upright."

## Open a hinged door
"The door opens inward on the left hinge. Her right hand turns the handle downward, pushes, and the door swings open along its arc; she steps through after the door is open."

## Press a button
"His index finger touches the round button; it depresses slightly; the light above turns on after the press."

## Push a cart / object
"Both hands grip the cart handle; she leans forward and pushes; the cart starts slowly, rolls, then slows when she eases off."

## Hand off an object (high risk)
"She holds out the cup with her left hand; he reaches with his right hand; both hands touch the cup; she releases; he holds the cup alone."

## Sit down
"She turns, bends her knees, lowers onto the chair seat; her weight settles; the chair stays in place."

## Per-model notes
- If the tool uses a structured formula (for example [Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]), place the contact sentence inside **Action** and keep it intact.
- If the tool supports timestamps, split into beats: 0–2 s approach, 2–4 s contact and grip, 4–6 s lift and carry.
- If the tool supports negative prompts, use targeted terms tied to observed failures (for example "object moving before hand touches it", "extra fingers"). Do not paste a generic wall of negatives.

## Anti-patterns
- "She grabs the can" (no part, no hand, no beat).
- "The can flies into her hand" (unless intentionally magical).
- Long adjective chains in the contact sentence.
- Two or more contact events in the same few seconds.
- Mixing "slow motion" with fast actions.
- Using close-up macro of fingers on an untested model.

## Fallback prompt pattern (simplified)
Remove: carry, turn, second hand, secondary action, camera motion. Keep: reach → grip → lift a short distance → hold at side.
