# Checklist — Domains 81–89

## 81. Testing Strategy
- [ ] Documentation · scope · environments · test data · ownership · reporting · automation · maintenance
- [ ] Types: unit · integration · component · E2E · visual regression · accessibility · security · performance · load · compatibility · CMS integration · API · smoke · regression · UAT · production smoke

## 82. Unit Testing
- [ ] Utility functions · business logic · data transformation · validation · formatting · URL helpers · date helpers · CMS data mapping
- [ ] Conditional rendering logic · state transitions · error handling · edge cases · boundary conditions · null/undefined handling
- [ ] Test isolation · reliability · coverage of critical logic

## 83. Integration Testing
- [ ] Next.js ↔ Sanity · GROQ queries · data mapping · image handling · metadata generation · webhook handling · revalidation
- [ ] API routes · Server Actions (if used) · form submission · email integration · maps · analytics · external links · authentication (if used)
- [ ] Error propagation · timeout behavior · external-service failure

## 84. End-to-End Testing
- [ ] Journeys: homepage · about · brand discovery · brand detail · event discovery/detail · journal discovery · article detail · career · contact · navigation · mobile navigation · CTA · form submission · external destination
- [ ] Direct URL access · browser refresh · browser history · invalid route · CMS update propagation · preview behavior · production behavior

## 85. Visual Regression
- [ ] Pages: homepage · about · brand listing · brand pages · event · journal · career · contact (desktop & mobile)
- [ ] Components: navigation · footer · hero · gallery · carousel · modal · dropdown
- [ ] Responsive breakpoints · typography · image cropping · spacing · design tokens · motion · CMS content variations · empty states · long content · cross-browser rendering

## 86. Security Testing
- [ ] Authentication (if any) · authorization · broken access control · XSS · CSRF · SSRF · injection · open redirect · CORS · rate limit · request validation · file upload
- [ ] Webhook signature · secret exposure · security headers · dependency scanning · configuration · session (if any) · error disclosure · sensitive-data exposure · unauthorized CMS access · preview data leakage

## 87. Performance Testing
- [ ] Lighthouse · PageSpeed Insights · Web Vitals · bundle · network · image · font analysis · API latency · CMS latency
- [ ] Mobile · desktop · slow network · low-end device · concurrent visitors · traffic spike · large gallery · large content · third-party impact · cache behavior · regression comparison

## 88. Production Smoke Test
- [ ] Homepage loads · main & mobile navigation · all critical routes · all brand pages · CMS content correct · images & fonts load · links & CTAs work · forms · maps · external integrations
- [ ] Metadata · canonical URLs · robots rules · sitemap accessible · HTTPS · no critical console errors · no critical network errors · monitoring receives events · rollback remains possible

## 89. User Acceptance Testing
- [ ] Stakeholder · content · design · brand · functional · mobile · desktop approvals
- [ ] Accessibility review · SEO review · legal/privacy approval · CMS-editor approval · production-readiness approval
- [ ] Known issues documented · launch decision recorded
