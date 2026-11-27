# Harness & Environment Compatibility Guide

This suite is designed to work identically across OpenCode, Claude Code, Gemini CLI, Gemini App, Cursor, Windsurf, Codex, and custom agent harnesses.

## Core Portability Rules

1. **No Hardcoded Tool Names**: Skills describe capabilities generically (read files, run Python scripts, inspect images) rather than assuming proprietary tool names.
2. **Relative Script Discovery**: Always locate bundled scripts relative to the skill directory (`skills/<skill-name>/scripts/<script>.py`).
3. **Cross-Platform Commands**:
   - Prefer Python 3 scripts over OS-specific bash utilities (`sed -i`, `convert`, `sips`) so the same workflow runs on Windows, macOS, and Linux.
   - Always quote file paths containing spaces.
4. **Graceful Degradation**:
   - If the agent cannot capture live screenshots (for example, headless sandbox without GUI simulator access), instruct the user clearly on the exact capture command or ask them to drop raw screenshots into `docs/assets/raw/`, then immediately run `slice_clean_device.py` and `compose_store_assets.py` on those files.
   - If custom brand fonts (`.ttf`/`.otf`) are not present in the repository, use system sans-serif/monospace fonts and record the fallback font in the build summary so the user can swap in a custom `.ttf` later.
   - If `numpy` is not installed, bundled scripts automatically fall back to pure Pillow processing.
5. **Visual Verification**:
   - Whenever the harness supports viewing images (multimodal file viewer), inspect every sliced PNG and composed store graphic before finishing.
   - If the harness is text-only, rely on `validate_doc_pack.py` automated checks (dimensions, alpha transparency ratio, border cleanliness, file size, broken links) and print a clear summary table for user review.
