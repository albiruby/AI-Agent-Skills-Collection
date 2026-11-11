# Subskill 03 — Prompt Engineering

## Purpose
Translate the production brief into a prompt the selected model can interpret.

## Prompt principles
- Use concrete nouns and observable verbs.
- State the most important subject and action early.
- Use chronological action order.
- Describe spatial relationships explicitly: left/right from whose perspective, foreground/background, near/far.
- Distinguish camera movement from subject movement.
- Describe style with positive visual attributes before exclusions.
- Use reference images for properties they actually establish.
- Avoid synonym piles, repeated adjectives, conflicting instructions, and irrelevant negatives.
- Avoid over-specifying details that the model cannot reliably control.

## Priority hierarchy
1. Required subject/identity.
2. Main action and outcome.
3. Scene layout and key props.
4. Camera and composition.
5. Visual style and lighting.
6. Secondary details.
7. Negative constraints.

If prompt length must be reduced, preserve higher-priority items.

## Timing
Use timestamps only when the model benefits from temporal segmentation or the clip has several distinct beats. Otherwise use concise chronological prose. Never invent a duration or claim the model will honor a duration unsupported by the tool.

## Negative constraints
Use targeted exclusions tied to likely failure modes. Examples:
- "Keep the same jacket and hairstyle throughout."
- "Do not add extra people."
- "The camera remains fixed."
Avoid generic walls of "no bad quality, no distortion" language.

## Prompt variants
When useful, create:
- Main recommended prompt.
- Simplified fallback prompt for unstable generations.
- A targeted correction prompt for a specific failed output.

Do not produce multiple variants unless they materially help.

## Interaction prompts
For any physical interaction, write the contact sentence explicitly: name the part, the hand, the grip, state that the object stays still until contact, and describe the response that follows the hand. See `references/prompt-patterns-interactions.md` and subskill 16. Add targeted exclusions only after observing a specific failure.
