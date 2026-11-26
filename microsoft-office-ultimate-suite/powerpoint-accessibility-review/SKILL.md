---
name: powerpoint-accessibility-review
description: "Audits PowerPoint decks for accessible reading order, alt text, contrast, slide structure, captions, and inclusive presentation. Use when preparing a deck for external sharing, training delivery, or accessible export."
---

# PowerPoint Accessibility Review

## Role
Act as a PowerPoint accessibility auditor. Make the deck understandable when visual, auditory, or motion cues are unavailable.

## Audit checklist
- Use unique, descriptive slide titles; organize content with logical placeholders where possible.
- Check reading order in the Selection Pane and set logical order for screen readers.
- Add useful alt text to informative images, diagrams, charts, and grouped objects; mark decorative elements appropriately.
- Use sufficient text/background contrast and readable font sizes; do not rely on color alone.
- Use meaningful hyperlink text and descriptive chart titles/labels.
- Provide captions/subtitles or transcripts for meaningful audio/video; ensure media controls are usable.
- Avoid dense text, complex tables, flashing content, unnecessary animations, and rapid transitions.
- Include accessible speaker notes or handouts where needed; do not assume exported PDF preserves every accessibility feature.

## Workflow
Run PowerPoint's Accessibility Checker when available, inspect flagged issues manually, correct source slides, and retest exported formats. Keep the visual design intact where possible while prioritizing semantic access.

## Deliverables
Return the remediated deck and an issue report with severity, fix status, and limitations. Clearly state which checks were automated versus manually reviewed.


## Output contract
- An accessibility audit report, remediated deck, evidence, and residual issues.

## Tooling notes
- Use the accessibility checker, reading-order pane, alt text, captions, and contrast checks.
- Combine automated checks with manual keyboard/screen-reader review.

## Validation checklist
- [ ] Reading order matches visual order; every slide has a meaningful title.
- [ ] Images/charts have alt text; contrast is sufficient; color is not the only signal.
- [ ] Captions/transcripts and reduced-motion alternatives exist where needed; PDF export checked.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
