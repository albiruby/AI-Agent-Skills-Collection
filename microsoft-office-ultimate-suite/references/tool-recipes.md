# Tool Recipes for Office Deliverables

Concrete implementation guidance for agents that must create or modify Office artifacts. Use only tools actually available in the harness. Verify current API/library behavior before relying on version-specific details.

## 1. Choose the execution route

| Route | Best for | Limits |
|---|---|---|
| Native Office app / connector | Live account actions, full-fidelity layout, recalculation, pivots, macros | Requires desktop app, permissions, or connector |
| OOXML-aware library | Offline DOCX/XLSX/PPTX creation and structural edits | May not calculate, render, or preserve every feature |
| Office Scripts / VBA | Repeatable workbook/document automation | Platform, tenant, and macro policy dependent |
| Microsoft Graph | Mail, calendar, OneNote, SharePoint, Teams, files | Requires correct delegated/app permissions and consent |
| Power Automate | Connector-based workflows, approvals, scheduled jobs | Connector licensing, environment, and governance limits |
| Manual procedure | No execution tool available | User must perform steps; agent cannot claim completion |

Never claim an artifact was created, sent, calculated, or rendered unless the tool confirmed it and the result was inspected.

## 2. Word (DOCX)

### python-docx patterns

- Start from an existing template when brand/layout matters: `Document("template.docx")`.
- Use built-in styles (`Title`, `Heading 1`, `Normal`, `Caption`, `List Bullet`) instead of manual font/spacing; this preserves navigation and accessibility.
- Add tables with `add_table(rows, cols)`; set `table.style`, header repeat, column widths, and cell margins. Avoid merged-cell layouts for complex forms.
- Images: `add_picture(path, width=...)`; set alt text via the inline shape's `docPr` XML (`descr` attribute).
- Headers/footers: `section.header.paragraphs[0]`; add page fields with raw OOXML (`PAGE`, `NUMPAGES`).
- Table of contents: insert a `TOC` field via OOXML. python-docx does not populate it; the user must update fields in Word (or a renderer must do so).
- Content controls, tracked changes, and some field types are not fully supported by python-docx. Use native Word when these are requirements.
- Preserve existing styles and section structure when editing; avoid rebuilding a document from scratch unless authorized.

### Validation

- Reopen in Word or a high-fidelity renderer; check styles, TOC update, page numbers, headers/footers, tables, images, hyperlinks, and alt text.
- Export to PDF and inspect page breaks, orphan headings, table overflow, and font substitution.
- Check document properties (title, author, language) and accessibility checker where available.
- For DOCX integrity: unzip and verify `word/document.xml`, `styles.xml`, and relationships; do not hand-edit XML unless necessary and backed up.

## 3. Excel (XLSX)

### openpyxl patterns

- Create/load workbooks with `openpyxl`; write formulas as strings (`"=SUM(B2:B10)"`). Formula values are not calculated by openpyxl.
- Use tables (`Table`), defined names, data validation, conditional formatting, freeze panes, print areas, and sheet protection.
- Separate sheets: `README`, `Inputs`, `Raw`, `Calc`, `Output`, `Checks`.
- Prefer structured references in formulas when the workbook supports them; keep formulas auditable and avoid hidden magic numbers.
- openpyxl cannot reliably create/maintain PivotTables or all chart/feature combinations. Use Excel, a template, or a library that explicitly supports the feature.
- Check external links and volatile functions; remove or document them.
- For large files, avoid loading unnecessary sheets; use read-only/write-only modes where appropriate.

### Recalculation and validation

- Recalculate in Excel or a verified headless engine (for example, LibreOffice with recalculation enabled) before trusting results. A written formula is not a calculated result.
- Compare key totals against independent calculations; check `#REF!`, `#VALUE!`, `#DIV/0!`, circular references, and blank/zero denominators.
- Verify formatting, number formats, column widths, print layout, and that no required input is hard-coded.
- Test boundary cases: zero, negative, blank, duplicate keys, missing lookups, maximum rows, locale-specific separators.
- If the file must open in Excel for web/Mac/older versions, check function compatibility and avoid unsupported dynamic-array spill assumptions.

## 4. PowerPoint (PPTX)

### python-pptx patterns

- Use slide layouts and placeholders rather than absolute text boxes where possible; this preserves editability and theme behavior.
- Set `word_wrap`, font sizes, and paragraph spacing deliberately. python-pptx does not auto-fit text; overflow must be checked visually.
- Add speaker notes with `slide.notes_slide.notes_text_frame.text`.
- Charts: use native chart objects with explicit categories/series; do not paste chart images unless the user wants a static visual.
- Tables: keep rows/columns readable; avoid using tables as layout grids.
- Images: preserve aspect ratio, set crop intentionally, and add alt text.
- Grouping, SmartArt, and some animations are limited. Use native PowerPoint for advanced motion/brand systems.

### Validation

- Reopen in PowerPoint; check placeholders, text overflow, font substitution, chart data, notes, and alt text.
- Review the full deck in slide sorter for consistency, then each slide for collisions/clipping at presentation size.
- Check reading order and contrast; export to PDF and inspect.
- Confirm charts match the source data and do not truncate axes or mislead.

## 5. Outlook and Microsoft Graph

- Drafting is not sending. Create a draft unless the user explicitly authorized sending the exact message.
- Common endpoints: `/me/messages`, `/me/sendMail`, `/me/events`, `/me/contacts`, `/me/mailFolders`. Use `/users/{id}` only with the required mailbox permissions.
- Request the least privilege: `Mail.ReadWrite`, `Mail.Send`, `Calendars.ReadWrite`, `Contacts.ReadWrite`, `Notes.ReadWrite`, `Files.ReadWrite` as applicable.
- Pagination uses `@odata.nextLink`; do not assume the first page is complete.
- Handle throttling (`429`, `Retry-After`) with bounded backoff; do not retry sends blindly.
- Use delta queries for sync where supported; verify current API behavior.
- Before sending/inviting: verify recipients, To/Cc/Bcc, subject, body, attachments, time zone, date, and whether the action is draft, send, or proposal.
- Never invent email addresses, availability, attachments, or approvals.

## 6. OneNote

- Microsoft Graph OneNote access uses delegated authentication; app-only authentication is not supported per Microsoft documentation. Verify current support before designing.
- Create pages with HTML content; structure sections/pages deliberately and keep source links.
- Respect notebook permissions and tenant policies; do not assume a personal notebook is shareable.
- Check for duplicate pages, broken internal links, and sync conflicts after updates.

## 7. SharePoint and Teams

- Graph: `/sites/{site-id}/drives`, `/drives/{drive-id}/items`, `/teams/{team-id}/channels`.
- Use upload sessions for large files; simple upload for small files.
- Sharing links and permissions are security boundaries: verify internal/external sharing, expiration, and least privilege.
- Versioning and retention are not the same as backup; confirm the organization's recovery model.
- Teams tabs/files inherit SharePoint permissions; check whether channel membership matches document access expectations.
- External sharing, guest access, and anonymous links require explicit governance approval.

## 8. Access

- Prefer DAO for local Access data and ADO when appropriate; use parameterized queries.
- Split front end/back end for multi-user deployments; keep a pristine backup and a development copy.
- Compile VBA, compact/repair, and test on a copy before deployment.
- Review macro security, trusted locations, database passwords, and user-level permissions.
- Access is not a server database: evaluate concurrency, file size, availability, backup, and remote-access needs; recommend SQL Server/Azure SQL when appropriate.
- Do not run destructive queries or schema changes without explicit authorization and a backup.

## 9. VBA

- `Option Explicit`; declare types; use `LongPtr` for handles on 64-bit Office.
- Use error handlers (`On Error GoTo`) and restore `ScreenUpdating`, `EnableEvents`, `Calculation`, and `DisplayAlerts` in cleanup.
- Avoid `.Select`/`.Activate`; operate on objects directly.
- Prefer late binding when version compatibility matters; document references.
- Test on copies with representative data; do not run untrusted macros.
- Macro security and tenant policy can block execution; never bypass protection.

## 10. Office Scripts

- TypeScript with the `ExcelScript` namespace; use `workbook.getActiveWorksheet()`, `getRange`, `getTable`, and explicit value types.
- Scripts are supported in eligible Microsoft 365 Excel environments; availability depends on platform, tenant, licensing, and permissions.
- Design for idempotency and clear failure messages; avoid hard-coded sheet names when possible.
- Power Automate can pass parameters and schedule scripts; verify connector limits and error handling.
- Office Scripts do not replace VBA for desktop-only or non-Excel Office automation.

## 11. Validation matrix

| Deliverable | Library-only checks | Native/renderer checks |
|---|---|---|
| DOCX | Structure, styles, text, relationships | Layout, TOC update, pagination, rendering, accessibility checker |
| XLSX | Formulas, names, tables, validation rules | Recalculation, pivots, charts, print layout, Excel compatibility |
| PPTX | Slide/placeholder structure, text, notes, charts | Text fit, fonts, animations, visual consistency, accessibility |
| Outlook | Draft fields, recipients, payload | Actual send/delivery, calendar responses, permissions |
| OneNote | Page HTML/structure | Sync, permissions, rendering in clients |
| Access | Schema, queries, VBA compile | Multi-user behavior, deployment, performance |
| SharePoint/Teams | Permissions metadata, item structure | Effective access, sharing behavior, client rendering |

State which checks were actually performed. "Created the file" is not validation.

## 12. Safety and data handling

- Work on copies for destructive edits, migrations, bulk formatting, or uncertain conversions.
- Never include secrets, credentials, or unnecessary personal data in artifacts, examples, or logs.
- Confirm before sending, sharing externally, deleting, overwriting, or publishing.
- Respect DLP, sensitivity labels, retention, and tenant policy.
- Do not bypass macro security, MFA, consent, or access controls.
- Keep an audit trail of what changed, where, and how it was verified.
