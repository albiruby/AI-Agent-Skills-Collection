# Gemini Image Consistency Skills

18 plug-and-play `SKILL.md` skills plus paste-ready kits that keep **Gemini image generation consistent**: one locked style, one locked theme, one locked palette, recognizable characters and matching assets. Written specifically for Google's image stack: the Gemini app, Google AI Studio, the Gemini API, Google Flow and Gemini CLI (Nano Banana family, Imagen).

## How consistency works
1. A **LOCK STYLE & THEME** block copied verbatim into every prompt.
2. **Anchor images** (one approved reference per character, style and place) attached to every request.
3. **Review and repair**: score outputs against the bible, fix drift one variable at a time.

Every prompt has two parts:
```
LOCK STYLE & THEME:
<identical block>

ASSET GENERATION PROMPT:
<only the asset-specific part>
```

## Plug and play: pick your surface
| Surface | What to use | Where |
|---|---|---|
| Gemini app | Create a Gem, paste the instructions | `plug-and-play/GEM-INSTRUCTIONS.md`, then `START-HERE.md` |
| Google Flow | Fill the 3 instruction slots | `plug-and-play/FLOW-3-SLOTS.md` |
| Google AI Studio | System instruction + prompts | `plug-and-play/AI-STUDIO-AND-API.md` |
| Gemini API | Batch script | `batch_generate.py`, `pack_to_json.py` (untested sketches; verify SDK and model ID) |
| Gemini CLI | Agent Skills + context file | copy `skills/*` to `.gemini/skills/` (or `.agents/skills/`), put `plug-and-play/GEMINI.md` in the project root; or `gemini skills install <repo-url>` / `gemini skills link .` |
| Any chat | Copy-ready prompts | `plug-and-play/PROMPT-TEMPLATES.md` |

## Skills
| # | Skill | Job |
|---|---|---|
| 0 | `image-consistency-orchestrator` | Router and workflow |
| 1 | `image-project-intake` | Brief with explicit assumptions |
| 2 | `visual-style-lock` | Style Lock Block |
| 3 | `theme-world-lock` | Theme, culture, motifs, taboos |
| 4 | `color-palette-lock` | Hex palette, ramps, key color |
| 5 | `character-identity-lock` | Character cards, Design Lock sentence, character sheet |
| 6 | `environment-prop-lock` | Locations, props, modular kit |
| 7 | `composition-camera-lock` | Camera, framing, aspect, light |
| 8 | `master-prompt-builder` | Two-part prompts, Gemini reference formula |
| 9 | `reference-image-workflow` | Anchors, references, edit vs regenerate |
| 10 | `gemini-image-prompting` | Models, settings, surfaces, prompt skeletons |
| 11 | `asset-manifest-batch-planner` | Asset IDs, coverage, generation order |
| 12 | `game-asset-sheet-spec` | Sprite sheets, tiles, UI, VFX geometry |
| 13 | `negative-constraints-guardrails` | Exclusions, IP and cultural care |
| 14 | `consistency-qa-reviewer` | Scorecard; Gemini as reviewer |
| 15 | `drift-correction-iteration` | Symptom-to-fix map |
| 16 | `instruction-slot-packager` | Fit the bible into Gem / AI Studio / Flow / GEMINI.md |
| 17 | `asset-postprocess-handoff` | Cleanup, slicing, export, provenance |

## Layout
```
skills/          18 skills, <name>/SKILL.md (each ends with "Gemini notes")
plug-and-play/   Gem, Flow, AI Studio/API, GEMINI.md, prompt templates, scripts
templates/       STYLE_BIBLE, PROJECT_BRIEF, CHARACTER_CARD, ASSET_MANIFEST, PROMPT_PACK, QA_SCORECARD
examples/        Timun Mas (filled Flow slots)
_template/       Blank SKILL.md
```

## FAQ
**Does Gemini load SKILL.md in the app?** The Gemini app uses Gems, so paste the compact instructions there. Gemini CLI discovers skills from `.gemini/skills/`. Google AI Studio and Flow take pasted instructions.
**Can it guarantee the exact same face?** No model does. Character sheet + anchors + verbatim Design Lock + QA greatly improve it.
**Model changes?** Names, reference limits and sizes change; the Gemini skill lists what was true when written and says to verify.

## Notes
AI-generated images from Google models may carry provenance marks; check Google's current terms before commercial use.

## License
MIT (see `LICENSE`).
