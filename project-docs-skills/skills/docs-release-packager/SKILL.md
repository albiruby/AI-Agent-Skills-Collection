---
name: docs-release-packager
description: "Organizes and packages validated documentation, clean screenshots, store graphics, manifests, and QA evidence for repository delivery, store handoff, release archive, or developer handoff. Use when multiple deliverables need a stable structure, naming, asset manifest, integrity check, and a clear statement of what is final, editable, or still unverified."
---

# Docs Release Packager

## Mission

Turn a set of working files into a clear, complete handoff. The receiver should understand what each file is, where it came from, and what remains to be done without re-reading the chat.

## When to use

- A documentation/visual pack is ready for review or delivery.
- Assets need consistent names, folders, and a manifest.
- A release archive, store handoff, or repository docs update must be assembled.
- Multiple source/working/final versions exist and need separation.

## Workflow

### 1. Confirm destination and scope

- Repository docs update, standalone package, store asset folder, docs site, or archive.
- What is included vs excluded.
- Who receives it and what they must do next.
- Whether publication/submission is requested or only preparation.

### 2. Separate asset states

Adapt to the project, but keep states clear:

```text
source/        original captures, logos, editable diagrams
working/       intermediate crops, manifests, editable design sources
docs/          Markdown documentation and diagrams
assets/clean/  cleaned screenshots
store-assets/  destination-ready graphics + master/
qa/            QA report and validation output
```

Do not mix raw simulator windows with final clean assets. Do not place editable sources in the final store folder unless requested.

### 3. Apply naming rules

- Descriptive, stable, filesystem-safe.
- Lowercase kebab-case or the project's existing convention.
- Include project/screen/platform/sequence/variant where useful.
- Keep filename dimensions for store assets when the pipeline expects it (for example `COVER_500x500.jpg`).
- Avoid `final2`, `new`, `copy`, and ambiguous dates.

### 4. Build the asset manifest

Use `../../templates/asset-manifest.csv` and include:

- File/path.
- Description.
- Intended use/destination.
- Dimensions and format.
- Source capture/document.
- Processing notes.
- Platform spec source and check date.
- Validation status.
- Remaining issues.

Do not invent metadata. Mark unknown fields as unknown.

### 5. Check package integrity

- Every referenced file exists.
- No empty/corrupt/temp files.
- Markdown links resolve inside the package.
- Clean assets are PNG and transparent where required.
- Store assets match dimensions and have masters.
- Originals are preserved when required.
- No secrets, personal data, caches, build artifacts, or unrelated files.
- Archive paths are relative and sensible.

### 6. External release discipline

Preparing files is not publishing.

- Do not upload, submit, deploy, or change visibility without explicit authorization and an available integration.
- State clearly: **prepared**, **reviewed**, **validated**, **submitted**, or **published**.
- If submission cannot be performed, provide the exact package and manual steps.

### 7. Delivery report

Provide:

- Package path/link and short contents summary.
- What was validated and how.
- What remains unverified or requires manual action.
- Which files are final vs editable vs original.
- Rollback/replacement guidance if the package replaces existing assets.

## Output contract

- Organized deliverable tree.
- `docs/store-assets/manifest.json` (if store assets) and/or `asset-manifest.csv`.
- QA report if available.
- Delivery note with status and open items.
- No claim of publication unless it actually happened.

## Validation checklist

- [ ] Destination, scope, and receiver are clear.
- [ ] Source, working, final, and archived assets are separated.
- [ ] Naming is consistent and deterministic.
- [ ] Manifest covers all visual deliverables.
- [ ] Every referenced file exists; no broken links.
- [ ] No empty/corrupt/temp files.
- [ ] No secrets or personal data.
- [ ] Final assets match requested formats/dimensions.
- [ ] Editable sources preserved where useful.
- [ ] Status is stated precisely.

## Handoff

- The receiver gets the package path, contents summary, validation status, and next actions.
- If QA has open critical/major findings, do not present the package as ready.
