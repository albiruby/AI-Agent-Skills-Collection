# Evaluation Harness

Test whether the pack produces real, production-aware pixel art rather than "pixel-looking" output.

## Cases

| Case | Focus |
|---|---|
| [`cases/01-character-animation.md`](cases/01-character-animation.md) | Character, animation, pivot, palette, QA |
| [`cases/02-tileset-engine.md`](cases/02-tileset-engine.md) | Tileset transitions, seams, engine integration |
| [`cases/03-ai-cleanup.md`](cases/03-ai-cleanup.md) | Generated image cleanup, authenticity, palette, alpha |

## Protocol

1. Give the agent only the brief and authorized assets/tools. Do not expose the seeded issues.
2. Use a fresh session with the pack installed.
3. Capture files, script output, and visual/QA evidence.
4. Score with [`scorecard.md`](scorecard.md).
5. Repeat at least twice; record variance.

## Pass criteria

- No fabricated assets, engine tests, or tool claims.
- Grid/palette/pivot/alpha rules are correct.
- Animation loops and engine settings are verified or marked untested.
- AI-generated output is labeled honestly and cleaned.
- Handoff includes sources, manifest, and limitations.

## Limitations

Results depend on the harness, image tools, engine access, and model. This is a sample, not a certification.
