# Deliverable Checklists

Use the relevant checklist before handing off an artifact. Check only what was actually performed; state what could not be verified.

## 1. Universal handoff

- [ ] The requested outcome, audience, and file format are understood.
- [ ] Inputs and authoritative sources are identified; facts are traceable.
- [ ] Missing information is marked as an assumption or placeholder, not invented.
- [ ] The original files are preserved; work was done on copies where needed.
- [ ] The final artifact opens without errors in the intended application.
- [ ] The file name, location, version, and handoff note are clear.
- [ ] Passed checks, warnings, and unverified items are reported.
- [ ] No secrets, credentials, or unnecessary personal data are included.

## 2. Word documents

- [ ] Title, purpose, audience, and decision/action are clear.
- [ ] Heading hierarchy uses semantic styles (Title/Heading 1-3/Normal).
- [ ] Table of contents and page numbers are present when needed and updated.
- [ ] Sections, headers/footers, page orientation, and margins are intentional.
- [ ] Tables fit the page; no cut-off columns or orphaned headings.
- [ ] Lists, captions, cross-references, and footnotes are native and consistent.
- [ ] Language, spelling, terminology, dates, numbers, and units are consistent.
- [ ] Images have alt text; decorative images are marked as decorative.
- [ ] Hyperlinks work and use meaningful text.
- [ ] Document properties (title, author, subject, language) are set appropriately.
- [ ] Tracked changes/comments are resolved or intentionally retained.
- [ ] PDF export preserves layout, links, tags, and reading order.

## 3. Excel workbooks

- [ ] Sheet architecture separates raw data, inputs, calculations, outputs, and checks.
- [ ] Inputs are clearly marked and use data validation where helpful.
- [ ] Formulas are consistent across rows/columns and free of accidental hard-coded values.
- [ ] Key formulas are tested against independent calculations and boundary cases.
- [ ] No `#REF!`, `#VALUE!`, `#DIV/0!`, circular-reference, or silent error masking remains.
- [ ] Workbook was recalculated in Excel or a verified engine; cached values are correct.
- [ ] Tables, named ranges, and structured references are used consistently.
- [ ] Number formats, currencies, percentages, dates, and time zones are correct.
- [ ] PivotTables/Power Query refresh behavior is understood and, where possible, tested.
- [ ] Charts are truthful: axes, scales, labels, and source ranges are correct.
- [ ] Print areas, page setup, freeze panes, and protection are intentional.
- [ ] Chicken-and-egg/external links and volatile functions are documented or removed.
- [ ] Sensitive data is not hidden in unused sheets, comments, or defined names.

## 4. PowerPoint decks

- [ ] The storyline has a clear audience, decision, and sequence.
- [ ] Every slide has one primary takeaway in its title.
- [ ] Layouts use the theme/master and remain editable.
- [ ] Text fits at presentation size; no clipping, collisions, or tiny footnotes carrying essential content.
- [ ] Typography, spacing, margins, and alignment are consistent.
- [ ] Charts match source data; axes/scales are not misleading.
- [ ] Images are relevant, licensed, properly cropped, and not stretched.
- [ ] Alt text is present; reading order is logical.
- [ ] Contrast is sufficient; color is not the only carrier of meaning.
- [ ] Speaker notes are present where delivery depends on them.
- [ ] Animations/transitions are purposeful and do not block reading.
- [ ] The deck was reviewed in slide sorter and in presentation/PDF output.

## 5. Outlook messages and meetings

- [ ] Recipients, To/Cc/Bcc, and Reply All intent are correct.
- [ ] Names, addresses, and distribution lists are verified, not invented.
- [ ] Subject is specific; opening states purpose and desired action.
- [ ] Dates, times, time zones, deadlines, and recurrence are correct.
- [ ] Attachments exist, open, and are the intended version.
- [ ] Sensitive content, confidentiality, and external sharing are appropriate.
- [ ] Draft vs send vs propose vs book is clearly distinguished.
- [ ] The action was confirmed by the tool before reporting success.
- [ ] Follow-up/reminder is created only if requested.
- [ ] Meeting invites include agenda, duration, location/link, and required attendees.

## 6. OneNote notebooks

- [ ] Notebook/section/page structure matches how the user will retrieve information.
- [ ] Titles and page hierarchy are consistent and searchable.
- [ ] Sources, dates, participants, and decisions are captured.
- [ ] Action items have owner, due date, and status.
- [ ] Tags are used consistently and explained.
- [ ] Internal links work; no duplicate or orphan pages.
- [ ] Content is in the correct section; sensitive notes are not in a broadly shared notebook.
- [ ] Sync/conflict state is checked after editing.
- [ ] Images/files have context and accessible descriptions where relevant.

## 7. Access databases

- [ ] Tables have primary keys, appropriate data types, and referential integrity.
- [ ] Relationships and indexes match query patterns.
- [ ] Queries are parameterized and tested with empty/null/boundary data.
- [ ] Forms validate input and provide clear error messages.
- [ ] Reports are tested with real page sizes and long text.
- [ ] VBA compiles; error handling and cleanup are present.
- [ ] Multi-user deployment model is defined (single file vs split front/back end).
- [ ] Backup, compact/repair, and restore procedures are documented.
- [ ] Macro security/trusted locations are appropriate for the environment.
- [ ] Permissions and sensitive data handling are reviewed.
- [ ] Performance tested with realistic data volume and concurrent users.

## 8. Automation and Microsoft 365 workflows

- [ ] Trigger, schedule, actors, and system of record are explicit.
- [ ] Permissions use least privilege; consent/ownership is documented.
- [ ] Idempotency, duplicate detection, retries, and throttling are handled.
- [ ] Failure paths produce visible errors and a recovery path.
- [ ] Schemas, nulls, attachments, file names, and time zones are validated.
- [ ] Pagination is handled; "first page only" is not assumed.
- [ ] Audit logging excludes secrets and unnecessary personal data.
- [ ] Tested with happy path, duplicate trigger, permission loss, malformed payload, and downstream outage.
- [ ] Rollback/disable procedure exists.
- [ ] Owner, alerting, and credential/connection renewal are assigned.

## 9. Accessibility gate

- [ ] Semantic headings/styles are used in Word, PowerPoint, and OneNote.
- [ ] Reading order is logical in slides, documents, and PDFs.
- [ ] Images/charts have alt text; complex visuals have a text explanation.
- [ ] Contrast meets the applicable standard; color is not the only signal.
- [ ] Tables have header rows and are not used purely for layout.
- [ ] Links use descriptive text; no "click here".
- [ ] Captions/transcripts exist for media.
- [ ] Motion has a reduced-motion alternative.
- [ ] Keyboard navigation/focus works for interactive artifacts.
- [ ] PDF export preserves tags and reading order.

## 10. Security and privacy gate

- [ ] No secrets, API keys, passwords, or tokens in files, notes, comments, or metadata.
- [ ] Personal/confidential data is minimized and shared only with authorized recipients.
- [ ] External links, embedded objects, and macros are reviewed.
- [ ] Sensitivity labels/DLP/retention policies are respected.
- [ ] Sharing permissions use least privilege and appropriate expiration.
- [ ] Originals/backups exist before destructive changes.
- [ ] The agent did not bypass MFA, macro protection, consent, or admin controls.

## 11. Final handoff note

Include:

- What was delivered and where.
- What was verified and how.
- What could not be verified (for example, native rendering, recalculation, delivery).
- Assumptions and placeholders.
- Required next action (review, send, publish, migrate).
- Rollback or recovery notes for consequential changes.
