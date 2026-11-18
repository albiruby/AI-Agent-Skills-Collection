# Checklist — Domains 25–32

## 25. CMS Architecture
- [ ] Platform & Sanity project config · project ID · dataset config · production/development dataset separation
- [ ] Schema · document types · fields · references · arrays · images · Portable Text · slugs · relationships · reusable objects · singletons
- [ ] Versioning · draft/published behavior · preview configuration
- [ ] Query architecture · GROQ quality & performance · pagination · filtering · sorting · projection efficiency · consistency
- [ ] Data contract CMS ↔ frontend · schema evolution · migration strategy · content portability · CMS scalability

## 26. Sanity Security & Permissions
- [ ] Project & organization ownership · user access · roles (administrator, editor, contributor, viewer, developer)
- [ ] API token permissions · read-only token usage · write-token exposure · token scope · expiration/rotation
- [ ] Dataset visibility (public/private) · CORS & allowed origins · preview origins
- [ ] Access revocation · former-member access · Studio access · production dataset access
- [ ] Auditability of changes · content-publishing permissions

## 27. Schema & Data Integrity
- [ ] Required/optional fields · validation · defaults · unique values · slug uniqueness
- [ ] References: broken · circular · integrity · orphaned documents
- [ ] Types: array items · image · file · object · Portable Text · nested objects · enums
- [ ] Constraints: field · string length · numeric · date · URL
- [ ] Duplicate documents/content · missing/invalid values · unused assets · invalid image references
- [ ] Inconsistent structures · schema/data mismatch · migration safety · backward compatibility · frontend type compatibility

## 28. CMS Publishing Workflow
- [ ] Draft creation/editing · preview · publishing · unpublishing · archiving · deletion · scheduled (un)publishing (if used)
- [ ] Review · approval workflow · editorial & publishing permissions · version history · content rollback
- [ ] Slug-change handling · preview correctness · draft isolation · published-data consistency
- [ ] Webhook trigger · revalidation behavior · failed publishing · duplicate-webhook handling
- [ ] Editor usability · publishing documentation

## 29. Content Quality & Integrity
- [ ] Correct: page title · heading · body copy · brand identity · terminology · spelling · grammar · punctuation
- [ ] Correct: contact details · address · opening hours · social links · external URLs · event dates & status · CTA destinations
- [ ] Correct: image assignment & ordering · logo · gallery assignment
- [ ] Missing/placeholder/lorem/duplicate/outdated/unpublished/incorrectly published content · broken content links
- [ ] Formatting · mobile readability · editorial & brand-tone consistency · content ownership · approval

## 30. Media & Asset
- [ ] Image inventory · validity · resolution · dimensions · aspect ratio · crop · focal point · orientation · compression · WebP/AVIF · optimization · delivery · CDN · transformations · URL validity
- [ ] Missing/broken/duplicate/unused/oversized assets · incorrect formats · transparency handling
- [ ] SVG safety & optimization · logo quality
- [ ] Fonts: files · loading
- [ ] Video: format · compression · poster · autoplay · audio (if used)
- [ ] Rights & licensing · naming · metadata · alt text · ownership · replacement workflow · deletion implications

## 31. Content Model & Business Scalability (multi-entity sites; Samsara Group = brands)
- [ ] Entity fields: slug · name · tagline · category · speciality · card image · logo · theme
- [ ] Hero: eyebrow · title · intro · gallery · description · content sections
- [ ] Menu panels/images/heading · address · opening hours · Instagram URL · action buttons
- [ ] Ordering · status · featured · SEO title/description · social image · search visibility
- [ ] Optional section rendering · empty-section handling · template consistency · onboarding · removal · archiving · slug changes · gallery size handling
- [ ] Entity-specific content · shared template · data-driven pages · **no hardcoded entity assumptions**
- See `scalability-test-cases.md`

## 32. Data Lifecycle & Retention
- [ ] Document creation · update · publication · unpublication · archival · deletion
- [ ] Asset replacement/deletion · slug migration · content versioning · historical retention
- [ ] Export · restoration · content backup · orphan/reference/duplicate cleanup
- [ ] Retention policy · deletion policy · CMS migration · recovery testing
