# Project context: consistent image generation with Gemini

This project uses the Image Consistency Skills (see `.gemini/skills/` or `.agents/skills/`).

## Rules for the agent
1. Read `STYLE_BIBLE.md` before writing any image prompt. If it does not exist, run the `image-consistency-orchestrator` skill first.
2. Every image prompt has two parts: `LOCK STYLE & THEME:` (copied verbatim from the bible) then `ASSET GENERATION PROMPT:`.
3. Never paraphrase, shorten or "improve" the lock block. Only subject and action change.
4. Use anchor images from `anchors/` as references; never use a generated copy as a reference.
5. Keep prompts in English, one fenced block per prompt, IDs from `MANIFEST.md`.
6. After every 5-10 assets run `consistency-qa-reviewer` and log results in `QA_LOG.md`.
7. When the bible changes, bump its version, list assets to regenerate in `CHANGELOG.md`.
8. Do not name copyrighted characters, living artists or real people in prompts.
