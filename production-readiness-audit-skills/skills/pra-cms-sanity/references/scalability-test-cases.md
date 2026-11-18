# Scalability Test Matrix — CMS-driven multi-entity pages

Generalized from the Samsara Group case (5 brands). "Entity" = brand / venue / location / event / article type with its own page template. Test by code reading (does the template guard every optional field?), by staging/preview fixtures, or by static analysis of query projections. **Do not create documents in production.**

| # | Case | Expected result |
|---|---|---|
| 1 | Entity with minimum required fields only | Page renders, no empty headings/blocks, no console errors, valid metadata |
| 2 | Entity with all fields filled | Every section renders; no overflow; correct order |
| 3 | No logo | Fallback (name text or neutral mark), no broken image box |
| 4 | No card/listing image | Listing card still renders with placeholder; no layout shift |
| 5 | No gallery | Gallery section hidden entirely |
| 6 | Gallery with 1 image | No broken carousel controls/ infinite loop glitches |
| 7 | Gallery with 10 images | Lazy loading, correct ordering, usable carousel |
| 8 | Gallery with 50 images | No performance collapse; pagination/virtualization or sensible limit; weight within budget |
| 9 | No menu / catalog | Menu section hidden, nav links to it removed |
| 10 | Many menu panels/items | Layout holds; keyboard-accessible; images lazy |
| 11 | No location/address/hours | Section hidden; no "undefined"; structured data omits empty fields |
| 12 | Very long description | Wraps/truncates deliberately; no overflow on 320 px |
| 13 | Very long name | Header/card/nav do not break; OG image/title handle length |
| 14 | Empty or custom sections | Empty ones skipped; custom block types render or fail soft (no crash on unknown `_type`) |
| 15 | Entity archived | Not listed, not in sitemap; direct URL → 404 or redirect per policy |
| 16 | Entity draft | Not publicly visible; visible only in authorized preview |
| 17 | **New entity added in CMS only** | Appears in listing, gets its own page, sitemap, metadata — **no code change or redeploy beyond revalidation** |
| 18 | New entity added | Existing entities (e.g. the five original brands) unaffected: same output, no regression |
| 19 | Slug change | Old URL redirects (or documented 404); internal links update; sitemap updated |
| 20 | Theme/brand colors missing or invalid | Falls back to safe defaults; contrast preserved |
| 21 | Social/URL fields malformed or hostile (`javascript:`) | Rejected/hidden; no XSS |
| 22 | Ordering ties / missing order | Deterministic order |

Static-analysis hints: grep templates for hardcoded slugs/names (`=== 'brand-name'`), per-entity `if` chains, hardcoded images in `public/`, per-entity route folders that duplicate a dynamic route, `generateStaticParams` limited to a fixed list, listing pages with hardcoded arrays.

Report as a pass/fail/not-testable table; each fail becomes a `CMS-NNN` finding with the code location.
