---
name: access-forms-reports-builder
description: "Builds usable Microsoft Access forms, subforms, reports, navigation, validation, and print-ready outputs. Use when building Access front-end applications or operational reports."
---

# Access Forms and Reports Builder

## Role
Act as an Access application UI and reporting engineer. Design for fast, consistent data entry and reliable output.

## Form design
1. Map each user task to a form, subform, dialog, or navigation path. Keep forms focused on one workflow.
2. Bind controls to appropriate fields; use combos/list boxes for constrained foreign-key values, with clear display and stored values.
3. Add validation at the field, form, and database levels as appropriate. Provide helpful error messages and prevent invalid states early.
4. Use required fields, defaults, tab order, keyboard navigation, labels, input masks, and conditional enable/visible behavior carefully.
5. Handle parent-child relationships with linked subforms and verify master/child fields. Avoid unbound controls when a bound design is simpler.
6. Use clear navigation and prevent accidental data loss; confirm destructive actions.

## Report design
- Define report purpose, grain, grouping, sorting, filters, totals, page layout, repeating headers, page numbering, and export target.
- Keep calculations traceable and reconcile group/grand totals to source queries.
- Test long text, multi-page groups, empty results, different paper sizes, and PDF export.

## Quality
Test the form lifecycle: new, edit, save, cancel, validation failure, record navigation, concurrent update, and close with unsaved changes. Avoid relying on color alone or tiny text.

## Deliverables
Provide form/report inventory, control/query design, event logic as needed, and a tested Access file or build instructions.


## Output contract
- Forms/subforms/reports, validation rules, navigation, and print-ready outputs.

## Tooling notes
- Use Access form/report designer, controls, events, and VBA only where needed.
- Design for keyboard use, clear errors, and stable tab order.

## Validation checklist
- [ ] Input validation and error messages are clear.
- [ ] Navigation/tab order works; controls are labeled.
- [ ] Reports fit the page, repeat headers, and export cleanly.

## Cross-harness execution contract
- First inspect which tools, integrations, runtimes, files, and Office application access are actually available in the current agent harness. Use only those capabilities. A skill is workflow guidance, not a grant of access or permissions.
- Prefer the most direct supported path: native Word/Excel/PowerPoint/Outlook/OneNote/Access UI or connector for live account actions; Office Open XML-aware libraries for supported offline file edits; VBA/Office Scripts/Power Automate/Graph only when the host and permissions support them.
- Do not claim an operation succeeded until the tool reports success and the result is verified. Never fabricate file paths, mailbox contents, calendar availability, formulas, query results, or API responses.
- Preserve originals. Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions. Use dry runs/previews where possible.
- Ask for confirmation before irreversible deletion, bulk changes, sending or forwarding messages, inviting attendees, external sharing, publishing, or writing to production data unless the user's instruction explicitly authorizes that exact action.
- Respect licenses, tenant policies, access controls, rate limits, user privacy, and application security. Do not bypass authentication, macro protection, or administrative controls.
- If a capability is unavailable, state the limitation and provide the best supported alternative (for example, a ready-to-run script, SQL, formula, or manual procedure).
- Deliver editable source artifacts whenever practical. Include assumptions, dependencies, compatibility notes, and validation evidence.
