---
name: theme-world-lock
description: Defines and locks the theme, world, setting, mood, culture, motifs and cast for an image project as a Theme Lock Block. Use when images must feel like they belong to one story or brand world - folklore settings, fantasy or sci-fi worlds, brand universes, children's books, game worlds - or when the user says "lock the theme", "same world", "keep the mood", "culturally accurate". Written for Gemini image generation (Nano Banana family, Imagen) in the Gemini app, AI Studio, API, Google Flow and Gemini CLI.
---

# Theme & World Lock

## Purpose
Style is how it is drawn; theme is what world it depicts. This skill fixes the world so that unrelated prompts still produce images from the same place.

## Theme dimensions
| Dimension | Decide |
|---|---|
| Premise | One sentence: what story or brand does this serve? |
| Setting | Place, climate, era, architecture family |
| Culture / source | Which culture, folklore or genre; real-world references to respect |
| Mood | 3 words plus audience rating (family-friendly, teen, adult) |
| Motifs | 5-8 recurring shapes, patterns, symbols (e.g. batik lattice, banyan roots) |
| Materials | Wood, stone, fabric, metal vocabulary |
| Cast | Named recurring characters (details go to `character-identity-lock`) |
| Time and weather | Default time of day, weather, season |
| Taboos | What breaks the world (modern items, wrong region, off-tone humor) |

## Process
1. Pull premise, culture and mood from the brief; ask only about gaps.
2. For real cultures and folklore: use the user's sources first; otherwise state what you assume and flag `[verify]`. Prefer respectful, specific details over generic stereotypes (specific clothing, architecture, patterns of the region rather than a blended "exotic" look).
3. Write the Theme Lock Block (about 60-80 words).
4. List 5-8 **motifs** and 5 **taboos** separately in the bible; motifs can be called by name in prompts.
5. Check against the style lock: no contradictions (e.g. "gritty realism" vs "cute chibi").

## Output format
```
LOCK THEME:
THEME: <premise, setting, culture, era, mood, audience>
MOTIFS: <list>
MATERIALS: <list>
TABOO: <list>
```

## Example (short)
```
THEME: Original 2D top-down adventure inspired by Javanese folklore - rural village, tropical forest and hill path; family-friendly, warm folk-tale mood.
MOTIFS: batik diamond lattice, banyan roots, bamboo fences, clay roof tiles.
TABOO: modern objects, neon colors, guns, non-Javanese architecture.
```

## Pitfalls
- A theme that is only adjectives ("epic, magical"). Anchor in places, objects and materials.
- Mixing cultures by accident because the prompt said "ethnic". Name the specific culture.
- Putting character details in the theme; keep them in character cards.

## Gemini notes
- Newer Gemini image models can use real-world knowledge and, where enabled, web search grounding. For a real culture or place, supply the specific details yourself and verify them. For an invented world, keep grounding off so real-world looks do not leak in.
