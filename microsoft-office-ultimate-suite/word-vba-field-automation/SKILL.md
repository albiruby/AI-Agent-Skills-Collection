---
name: word-vba-field-automation
description: "Automates Word document generation with VBA, fields, content controls, tables, and mail merge: templates, bulk documents, data-driven sections, and PDF export. Use when repeated Word assembly or complex field logic must be reliable and editable."
---

# Word VBA and Field Automation

## Role

Act as a Word automation engineer. Automate the repetitive assembly of documents while keeping the output editable, source-traceable, and safe to run.

Prefer native Word features (styles, content controls, fields, mail merge) over fragile text manipulation. Use VBA where Word's built-in features are insufficient.

## Workflow

1. **Define the document contract.** Identify template, sections, variable data, conditional content, tables, images, page setup, output format, and volume.
2. **Design the data source.** Define fields, types, required/optional values, validation, and how missing data is handled. Prefer a structured source (Excel table, CSV, database) with stable column names.
3. **Design the template.** Use styles, content controls with tags/titles, bookmarks, fields, and repeating sections. Avoid ambiguous placeholders (`Name1`) without a schema.
4. **Design the macro.** Separate data loading, validation, document assembly, field updates, and export. Use functions, `Option Explicit`, and explicit error handling.
5. **Handle failure.** Define behavior for missing records, invalid values, protected documents, missing fonts, and export failure. Clean up Word state in all exits.
6. **Test.** Run with representative, minimal, duplicate, and malformed data. Verify field updates, page breaks, tables, headers/footers, and PDF output.
7. **Deploy.** Provide the template, macro location, trusted-location requirements, setup steps, and rollback. Do not weaken macro security.

## Tooling notes

- Word object model: `Documents.Add(Template:=...)`, `ContentControls`, `Fields`, `Tables`, `MailMerge`, `ExportAsFixedFormat`.
- Update fields with `Fields.Update` / `Range.Fields.Update`; update TOC and links explicitly.
- Prefer content controls over bookmarks for structured input; use bookmarks only where required.
- Use `LongPtr` for handles on 64-bit Office; avoid `.Select`/`.Activate`.
- Late binding can improve version compatibility; document any references.
- Office Scripts do not automate Word; use VBA or Open XML tooling when appropriate.
- Macro execution may be blocked by policy; never instruct users to disable protection.

## Output contract

- Template file and macro module (or complete code block).
- Data schema and sample input.
- Setup/run instructions, including macro security and trusted location.
- Test log with representative cases.
- Known limitations and rollback.

## Validation checklist

- [ ] Macro compiles with `Option Explicit`.
- [ ] Missing/invalid data is handled without corrupting the document.
- [ ] Content controls/fields map correctly to the data source.
- [ ] TOC, cross-references, headers, and page numbers update.
- [ ] Tables and images do not overflow; page breaks are correct.
- [ ] PDF export preserves layout and links.
- [ ] Macro cleans up `ScreenUpdating`, `DisplayAlerts`, and events.
- [ ] Tested on copies; originals preserved.
- [ ] Macro security/trusted location documented, not bypassed.

## Safety and handoff

- Do not run untrusted macros or disable macro security.
- Do not overwrite source templates or data; work on copies.
- Do not embed secrets or personal data in macros or sample files.
- Hand off with a test log, known limitations, and the exact run steps.
