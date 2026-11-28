# Installation

## Prerequisites

- An agent harness that discovers `SKILL.md` files (OpenCode, Claude Code, Codex, Gemini CLI, Cursor, or compatible).
- Optional but recommended for web audits:
  - Node.js 18+
  - Playwright in the target project: `npm install -D playwright && npx playwright install chromium`
  - Or a system browser channel: Edge (`--channel msedge`) or Chrome (`--channel chrome`)
- Python 3.9+ with Pillow for `pixel_precision_audit.py` and `validate_package.py`:
  - `pip install pillow`

No numpy or OpenCV is required.

## Option A — Install the whole pack

The skill files reference `../../references`, `../../templates`, `../../scripts`, and `../../shared`. Install the **whole pack folder**, not individual skill folders, so those paths resolve.

### PowerShell

```powershell
.\install.ps1 -Destination "$HOME\.config\opencode\skills"
```

### Bash

```bash
bash ./install.sh ~/.claude/skills
```

The installer copies the pack as `<destination>/ui-ux-god/`. It skips an existing pack unless `-Overwrite` / `--overwrite` is passed.

## Option B — Junction / symlink (recommended for local development)

Keep one source of truth and let the harness scan it.

### Windows

```powershell
New-Item -ItemType Junction `
  -Path "$HOME\.config\opencode\skills\ui-ux-god" `
  -Target "D:\Skills by Albireo\ui-ux-god"
```

### macOS / Linux

```bash
ln -s "/path/to/ui-ux-god" "$HOME/.claude/skills/ui-ux-god"
```

## Option C — Project-local

```bash
cp -R ui-ux-god .opencode/skills/ui-ux-god
```

or:

```powershell
Copy-Item -Recurse ".\ui-ux-god" ".\.opencode\skills\ui-ux-god"
```

## Verify discovery

OpenCode example:

```bash
opencode api get "/api/skill?location%5Bdirectory%5D=$(python -c 'import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))' "$PWD")"
```

Look for the 32 `uiux-*` / `ui-ux-god` entries.

## Validate the pack

```bash
python scripts/validate_package.py
```

Expected: `All package checks passed.`

## First run

```text
Use `ui-ux-god` to audit http://localhost:3000 at 375, 768, and 1440.
Catch layout, micro-detail, contrast, focus, and responsive issues.
Fix only verified P1/P0 issues and prove each fix with before/after evidence.
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `Playwright not found` | Install Playwright in the target project, or use `--channel msedge` |
| Browser executable missing | `npx playwright install chromium`, or use a system channel |
| `../../references/...` not found | Install the whole pack, not individual skill folders |
| Pixel script import error | `pip install pillow`; Python 3.9+ |
| Skill not discovered | Confirm the harness scans nested `SKILL.md`; check the path/junction |
| Duplicate skills | Do not install the same pack in two scanned directories |
