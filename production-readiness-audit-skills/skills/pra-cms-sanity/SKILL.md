---
name: pra-cms-sanity
description: Audit a Sanity CMS integration and CMS-driven content - project/dataset config, schema and document architecture, GROQ queries, tokens and permissions, CORS origins, schema/data integrity, broken references, draft/publish and preview workflow, webhooks and revalidation, content and media quality, multi-entity scalability (e.g. adding a new brand/venue/location without code changes), data lifecycle and backups. Use when the user mentions Sanity, Studio, GROQ, schema, dataset, Portable Text, CMS content check, "cek konten", "tambah brand baru tanpa ubah kode", image assets, webhook revalidate, or CMS permissions. Covers audit domains 25-32.
---

# CMS, Data, Content, Media (Domains 25–32)

Parent: `production-readiness-audit`. Production data is **read-only** for you: no publishing, deleting, patching, or asset removal without approval. Lists: `references/checklist.md`; scalability matrix: `references/scalability-test-cases.md`.

## Procedure
1. **Config (25)**: `sanity.config.*`, `sanity.cli.*`, `projectId`/`dataset` (from code and env), API version pinning (`apiVersion` fixed date, not `'v1'`/missing), `useCdn` strategy (CDN for public reads, no CDN for preview/drafts), separate dev/preview/production datasets (verify prod frontend reads the production dataset and previews do not write to it), Studio hosting/embedding and its access.
2. **Schema architecture (25/27)**: list document types, singletons, objects, references, arrays, images/files, Portable Text (custom blocks/marks/annotations), slugs. Look for: required-field validation for fields the frontend assumes exist; slug `unique` validation; max lengths; enum/`list` options; `hidden`/`readOnly` logic; initial values; orderings and previews for editors; deprecated fields still queried; duplicated shapes that should be reusable objects.
3. **Frontend ↔ CMS contract (25/27)**: every GROQ query — projections instead of `...`/`*[]` over-fetch, parameters instead of string interpolation (injection/escaping), `defined()`/coalesce for optional data, pagination (`[0...N]`), ordering, reference expansion (`->`) depth, drafts excluded in published queries (`!(_id in path("drafts.**"))` or perspective `published`), image `asset->` handling; TypeScript types vs actual schema (typegen drift); behavior on `null` results (`notFound()`), empty arrays, missing images.
4. **Security & permissions (26)** — dashboard-level items are usually Not Verifiable without manage access; ask the owner for screenshots/lists: project/org owners, members & roles (ex-members/interns removed), API tokens (name, role, last used, expiry), dataset visibility (public vs private; public datasets expose all published docs), CORS origins (no `*` with credentials; includes production + preview domains only), webhook secrets. In code: write tokens never in client; read tokens scoped.
5. **Data integrity (27)** — if read access to the dataset exists, run **read-only** GROQ (or export via `sanity dataset export` to a scratch location if permitted): missing required fields, duplicate slugs, broken references (`*[references(^._id)]` inverse checks, or `count(*[_type=="x" && !defined(field->)])`), orphaned documents/assets, invalid image refs, empty arrays, enum values outside options, inconsistent structures, placeholder text, `lorem`, test documents, draft-only documents that should be published (and vice-versa).
6. **Publishing workflow (28)**: draft → preview (Draft Mode secret, preview token, correctness vs published) → publish → webhook → `revalidateTag/Path`; verify webhook signature validation, idempotency/duplicate handling, failure behavior, slug-change redirects, unpublish/delete → 404 (not stale page), content history/rollback, editor permissions, editor documentation.
7. **Content & media quality (29/30)**: titles/headings/copy/typos, contact data, addresses, hours, social URLs, external links and CTA targets, event dates/status, correct image/logo assignment and order, missing/placeholder content, duplicates, outdated items; media: dimensions/resolution/aspect/crop/hotspot/focal point, format and weight, alt text (including decorative handling), SVG safety, video format/poster/autoplay, unused/oversized/duplicate assets, license/ownership (hand to `pra-privacy-legal`). Quote data with IDs, not personal contacts beyond what is public on the site.
8. **Multi-entity scalability (31)**: apply `references/scalability-test-cases.md` — the site must render correctly for minimum/maximum/odd data and must accept a *new* entity (brand, venue, location, event) **without code changes** and without breaking existing ones. Test by reading template code and, where allowed, with preview/staging fixtures; never create production documents.
9. **Lifecycle & retention (32)**: creation→publication→archival→deletion flows, asset replacement/deletion effects, slug migration, versioning, export/backups (cross-link `pra-backup-recovery-incident`), orphan cleanup, CMS migration path, recovery tests.

## Calibration
- Write-capable token exposed / public dataset containing private data → Critical.
- Production frontend reading a dev dataset, or preview writing to production → High.
- Query without null handling that 500s when an optional field is empty → Medium–High (user-facing crash).
- Missing slug uniqueness validation → Medium. Missing alt text in CMS model → Medium (a11y/SEO).
- Typos or wrong hours in published content → Medium (business impact), High if contact/pricing/legal facts.

## Output
Schema map, query inventory with issues, permission review (with Not Verifiable list), data-integrity results, scalability matrix results, content/media defect list (`CMS-NNN`).

## Pitfalls
Writing to the dataset "to test" · trusting Studio UI validation as proof of data validity (API writes bypass it) · assuming `useCdn: true` is safe for drafts · auditing the schema but not the published data, or the reverse.
