---
name: pra-seo-i18n
description: Audit technical SEO, structured data (JSON-LD), content SEO and internationalization of a website - crawlability, indexability, robots.txt, sitemap, canonicals, metadata, Open Graph, redirects, duplicate content, Organization/LocalBusiness/Restaurant/Event/Article/JobPosting schema, hreflang and localization. Use when the user asks about SEO, "kenapa tidak terindex", sitemap/robots, meta tags, OG image, rich results, schema markup, canonical, noindex on production, Search Console, or multilingual setup. Covers audit domains 46-49.
---

# SEO, Structured Data, Content SEO, i18n (Domains 46–49)

Parent: `production-readiness-audit`. Launch-critical check first: **is production accidentally `noindex`, or are previews/staging indexable?** Lists: `references/checklist.md`.

## Procedure
1. **Crawl/index controls (46)**: fetch `/robots.txt` (production allows crawling; staging/preview disallows or is protected; sitemap URL declared), `/sitemap.xml` (valid, absolute production URLs, only canonical/indexable/200 pages, includes dynamic CMS pages, excludes archived/draft/404, `lastmod` sane), `x-robots-tag` header and `<meta name="robots">`, `metadataBase`, canonical per page (self-referencing, absolute, matching the canonical host/protocol/trailing slash), redirect hygiene (301/308 for permanent moves; no chains/loops; apex↔www single canonical), 404/soft-404 behavior, internal broken links, orphan pages, pagination, duplicate URLs via query params.
2. **Metadata**: unique `<title>` and meta description per page (length sanity ~≤60/≤160 chars), Open Graph + Twitter cards (`og:image` absolute, ≥1200×630, reachable, correct for CMS entity pages), favicon/app icons, `lang`, viewport, theme color; `generateMetadata` falls back when CMS SEO fields are empty; CMS SEO fields actually mapped.
3. **On-page**: one `h1`, heading hierarchy, semantic HTML, meaningful anchor text, image alt text, internal linking, thin/duplicate content across entities (templated text repeated), content freshness (dates, events), readable URLs.
4. **Structured data (47)**: inventory JSON-LD in the rendered HTML: `Organization`, `WebSite`, `WebPage`, `BreadcrumbList`, `LocalBusiness`/`Restaurant`/`Hotel` (entity pages), `Event`, `Article`/`BlogPosting`, `JobPosting`, `ImageObject`, `ContactPoint`, `sameAs`. Validate JSON syntax and required/recommended properties (Rich Results Test, Schema Markup Validator — run manually or note as not run); data must **match visible content** (address, hours, dates, URLs); no duplicate/conflicting blocks; no markup for content not on the page; JSON-LD serialization escapes `<`.
5. **Content SEO (48)**: search intent per page, unique titles/descriptions, keyword relevance without stuffing, brand-specific content for each entity, cannibalization between similar pages, completeness of location/hours info, author/date for articles, CMS SEO field mapping and fallbacks.
6. **Search Console/Bing**: property verified (DNS preferred), sitemap submitted, coverage errors, manual actions — Not Verifiable without access; list as an action item.
7. **i18n (49)** — only if multiple languages/regions: locale routing, language switcher, `hreflang` (reciprocal, with `x-default`), canonical per locale, localized metadata, translation completeness/fallbacks, date/number/currency/time-zone formats (e.g. WIB), `lang` attributes, no duplicate untranslated copies indexed. Otherwise N/A (note if Indonesian-only with `lang="id"` set correctly).

## Calibration
- Production `noindex`/`Disallow: /` or previews indexable → Critical/High (launch blocker).
- Missing/incorrect canonical or sitemap with wrong domain → High–Medium.
- Missing OG image on entity pages → Low–Medium. Structured data contradicting page content → Medium (policy risk).
- Short meta descriptions → Informational.

## Output
Indexability matrix (URL · status · canonical · robots · in sitemap), metadata coverage table, structured-data validation results, findings (`SEO-NNN`).

## Pitfalls
Checking only the homepage · trusting `next-sitemap` config without reading output · marking schema "valid" without comparing to visible content · forgetting that CMS archived/draft entities leak into the sitemap.
