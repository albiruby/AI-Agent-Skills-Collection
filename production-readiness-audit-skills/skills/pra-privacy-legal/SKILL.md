---
name: pra-privacy-legal
description: Audit privacy, personal-data handling and legal/compliance readiness of a website - personal data inventory, forms and career/CV uploads, analytics and tracking scripts, cookie consent, data retention and deletion, vendors, Indonesian UU PDP (Pelindungan Data Pribadi) and other applicable obligations, privacy policy, terms, copyright, font/image/video/music licensing, open-source license compliance. Use when the user asks about privacy policy, cookie banner, GDPR/UU PDP, "data pribadi", licensing of assets/fonts, terms of use, or legal readiness before launch. Covers audit domains 23-24. Gives audit findings, not legal advice.
---

# Privacy, Personal Data, Legal (Domains 23–24)

Parent: `production-readiness-audit`. You are not a lawyer: report factual gaps and flag items for **legal review**; never state that the site "is compliant". Lists: `references/checklist.md`.

## Procedure
1. **Personal data inventory** — find every place personal data enters or leaves:
   - Forms (contact, career/CV upload, newsletter, reservation), route handlers, Server Actions, email providers, CRM, CMS submissions.
   - Analytics/tag managers/pixels/session replay, embedded maps/videos/social widgets (third-party requests leak IP/UA), fonts loaded from third-party CDNs, error-tracking payloads, server/runtime logs with IP/email.
   - For each: data fields, purpose, legal basis/consent, processor/vendor, storage location & country, retention, who can access, how deleted.
2. **Consent & cookies**: list cookies/localStorage keys set before consent (check in browser/network). Non-essential trackers must wait for consent where the applicable law requires it; consent must be withdrawable; consent state respected by tags.
3. **Policies & disclosures**: Privacy Policy and Terms exist, are linked from footer and from forms, match actual collection (vendors, purposes, retention, contact for data requests); cookie disclosure; career-application disclosure; company identity and official contact.
4. **Indonesian obligations (UU PDP, UU No. 27/2022)**: check against the actual flows — lawful basis/consent, purpose limitation, data-subject rights handling (access, correction, deletion, withdrawal), breach notification procedure, processor agreements, cross-border transfer conditions, DPO requirement applicability. Mark applicability judgments for the owner/legal counsel; also note GDPR/other regimes only if the audience warrants.
5. **Retention & deletion**: where CV/resumes and form data live (email inbox? Sanity? third-party), who can read them, how long kept, deletion procedure; attachments security (access control, no public URLs); personal data in logs/analytics.
6. **Licensing & IP**: images, video, music, **fonts** (web license for the domain), icons, illustrations, stock, brand logos/trademarks (client-owned vs third-party), open-source license obligations (from `license-checker`), copyright notice, user-generated content terms. Request proof/ownership for assets whose provenance is unknown — mark *Suspected* not Confirmed.
7. **Other disclosures**: accuracy of consumer information (prices, hours, claims), accessibility obligations that apply, industry-specific requirements (F&B/hospitality: halal, alcohol/age notices if relevant) — flag for owner confirmation.

## Calibration
- Collecting CVs/personal data with no privacy notice and no retention plan → High (launch-dependent).
- Analytics/pixel firing before consent where consent is required → Medium–High.
- Unlicensed commercial font or stock asset → Medium–High (legal exposure), Suspected until proven.
- Policy mentions vendors not actually used / omits ones used → Medium.
- Missing cookie policy on a site with no non-essential cookies → Informational.

## Output
Data-flow table, vendor list, consent findings, policy gap list, licensing register, items needing legal sign-off (`PRIV-NNN`). Never include real personal data samples; use field names only.

## Pitfalls
Giving legal conclusions · testing forms with real personal data or sending real emails (use authorized test inbox) · forgetting third-party embeds · forgetting that email inboxes are data stores.
