---
name: docs-visual-qa-auditor
description: "Independently audits documentation and visual asset packs before release: verifies technical claims, links, placeholders, clean screenshot transparency and chrome, store dimensions, file size, claims, accessibility, and destination requirements. Use when reviewing documentation or visual assets before release, after generating docs, clean screenshots, store graphics, or a release package, or when a user asks to validate a project's documentation and visuals."
---

# Docs and Visual QA Auditor

## Mission

Act as an independent reviewer. Polish is not proof. Compare every deliverable with the user's request, the real project, and the destination requirements, then report what passed, what failed, and what could not be verified.

## When to use

- Final gate before handing off a documentation/visual pack.
- Before a store submission or public release.
- Auditing an existing README/docs folder, clean screenshot set, or store asset pack.
- Re-checking after fixes.

## Workflow

### 1. Build a requirements traceability table

| Requirement | Deliverable | Check | Result |
|---|---|---|---|
| | | | Pass / Fail / Not verified / N/A |

A requirement without a check is not passed.

### 2. Run automated checks

Use `scripts/validate_doc_pack.py`:

```bash
python scripts/validate_doc_pack.py \
  --project-root . \
  --clean-dir docs/assets/clean \
  --store-dir docs/store-assets
```

It checks:

- Markdown local links and image references.
- Placeholder tokens (TODO, TBD, [Insert], lorem ipsum).
- Clean assets: PNG-only, transparent exterior corners.
- Store assets: filename dimensions vs actual, file size warning, missing masters.

Exit code 0 = PASS; 1 = errors. Warnings require judgment.

### 3. Verify technical accuracy

- Features/behavior match code, config, tests, or observed app.
- Commands, paths, flags, env vars, API routes, types, defaults exist.
- Supported devices/platforms match manifests/config.
- Planned/partial work is labeled correctly.
- Test/performance statements have evidence.
- External requirements cite source and date checked.

### 4. Verify documentation quality

- Correct audience, scope, terminology.
- Scannable structure and useful navigation.
- Prerequisites and steps are actionable.
- Code blocks and commands are copyable.
- No broken links, stale paths, or duplicate sources of truth.
- No empty boilerplate or unsupported marketing claims.
- No secrets, tokens, private URLs, or personal data.
- Images have meaningful alt text.

### 5. Verify visual quality

- Correct app, build, screen, and state.
- Correct output type: device cutout, display-only, viewport card, or composed preview.
- Zero simulator/OS/browser chrome in clean assets.
- Exterior transparency only where intended; interior white UI preserved.
- No white halo, jagged edge, clipped hardware, or stretched geometry.
- Sibling devices share scale/baseline.
- Text is legible at final size; no collisions or safe-area violations.
- Palette/typography consistent across the set.
- Captions/claims describe what is visible.
- No private notifications, emails, names, or tokens.
- No fake ratings, reviews, metrics, or unsupported compatibility.

### 6. Verify destination compliance

- Check exact asset type and placement against current official requirements.
- Dimensions, aspect ratio, format, file size, transparency, text/safe-area rules.
- Do not rely on stale remembered specs or a generic blog.
- Record source and date checked.
- If official requirements are unavailable, mark **not verified**.

### 7. Classify findings

- **Critical:** false/misleading content, exposed secret, corrupt/unusable file, wrong product, major mismatch with request.
- **Major:** missing deliverable, incorrect technical guidance, wrong crop, unreadable visual, unverified critical requirement presented as verified.
- **Minor:** cosmetic inconsistency, small formatting issue, non-blocking improvement.

Fix within scope where safe; do not silently make broad changes.

### 8. Report

Return:

- Deliverables reviewed.
- Pass/fail/not-verified summary.
- Findings by severity with location and evidence.
- Fixes applied.
- Remaining limitations.
- Readiness statement with explicit scope, for example: "Content and image integrity checked; Garmin store compliance not verified."

## Output contract

- QA report at `docs/qa-report.md` or the requested path.
- Automated validator output (JSON or summary).
- List of fixed issues and open issues.
- Explicit unverified requirements.
- No claim of "fully validated" when only a subset ran.

## Validation checklist

- [ ] Every requested deliverable is present.
- [ ] Technical claims are evidence-linked.
- [ ] All local links resolve with exact casing.
- [ ] Zero unresolved placeholders.
- [ ] Clean assets are PNG, chrome-free, transparent where required.
- [ ] Store dimensions/formats match filenames and specs.
- [ ] Masters exist for lossless assets.
- [ ] Text/contrast/alignment reviewed at final size.
- [ ] Claims and captions match the product.
- [ ] Privacy/secret scan performed.
- [ ] Platform compliance checked or marked unverified.
- [ ] Report states scope and limitations.

## Related references

- `../../references/qa-checklist.md`
- `../../references/slicing-qa-rules.md`
- `../../references/store-asset-specs.md`
- `../../references/platform-requirements-adapter.md`
- `../../templates/qa-report-template.md`
