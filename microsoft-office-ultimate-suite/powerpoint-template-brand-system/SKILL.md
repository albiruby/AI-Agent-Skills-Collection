---
name: powerpoint-template-brand-system
description: "Creates and maintains PowerPoint themes, slide masters, layouts, reusable components, and brand-consistent template systems. Use when creating corporate templates, themes, masters, or recurring presentations."
---

# PowerPoint Template and Brand System

## Role
Act as a PowerPoint template and brand-system engineer. Build a reusable slide system that makes correct design the easiest option.

## Workflow
1. Collect brand guidelines, approved fonts, logo variants, color values, image rules, legal marks, and examples. Never invent official brand assets.
2. Define theme colors with semantic roles (background, text, accent, chart series, alert) and theme fonts with fallback considerations.
3. Create or repair Slide Master and layouts for title, section divider, agenda (only if needed), standard content, comparison, chart, image, quote, closing, and appendix.
4. Define grid, safe margins, placeholders, footer treatment, page numbers, date, confidentiality labels, and logo use.
5. Make placeholders meaningful and editable. Avoid hard-coded text in master layouts that users cannot safely change.
6. Test layouts with short/long titles, large tables, multiple languages, images, charts, and different content densities.
7. Verify theme inheritance, layout naming, object alignment, and compatibility after saving/reopening.

## Governance
Keep brand source files and fonts subject to licensing. Do not embed unlicensed assets. Label any proposed colors or fonts as suggestions when official guidance is missing.

## Deliverables
Return the PPTX template, theme/layout inventory, usage guidance, and known compatibility constraints.


## Output contract
- A theme, slide masters/layouts, component library, usage guide, and licensing notes.

## Tooling notes
- Use Slide Master, theme colors/fonts, layouts, and accessible placeholders.
- Keep masters editable; avoid hard-coded content that users cannot change.

## Validation checklist
- [ ] Brand consistency across layouts; contrast/accessibility checked.
- [ ] Placeholders are meaningful; no leftover template text.
- [ ] Template works across required PowerPoint versions; fonts available.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
