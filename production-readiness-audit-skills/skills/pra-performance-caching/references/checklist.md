# Checklist — Domains 40–45

## 40. Web Performance
- [ ] Initial page load · TTFB · FCP · LCP · INP · CLS · TBT (diagnostic) · Speed Index
- [ ] JS execution time · main-thread blocking · long tasks · request count · waterfall · third-party overhead · resource prioritization · render-blocking resources
- [ ] Server response time · client rendering cost · hydration cost · API response time · CMS query latency · cache hit ratio · cold starts
- [ ] Mobile network performance · low-end device performance · regression · budget
- [ ] Targets: LCP ≤ 2.5 s · INP ≤ 200 ms · CLS ≤ 0.1 · field data at p75 · realistic budgets for JS, images, fonts, third parties

## 41. Image & Media Performance
- [ ] Format · compression · dimensions · responsive sizes · `srcset`/`sizes` · CDN · transformation
- [ ] Lazy vs eager loading · hero priority · preloading · fetch priority · decoding · aspect ratio · width/height reservation · focal point · mobile variants
- [ ] Gallery loading · carousel loading · offscreen loading · duplicate requests · oversized/unused/broken images · fallback
- [ ] Video: compression · autoplay · preload · poster · background video · third-party embeds · media bandwidth · asset cache headers

## 42. Font & Rendering Performance
- [ ] Format · weight files · subset · licensing · loading strategy · preload · `font-display` · fallback · swapping · layout shift
- [ ] Unused font files · unnecessary weights · variable fonts · typography rendering consistency
- [ ] Critical CSS · CSS loading · unused CSS · CSS size · specificity · render-blocking styles

## 43. JavaScript & Bundle Performance
- [ ] Bundle size · initial JS · route-specific JS · third-party JS
- [ ] Dynamic imports · lazy components · tree shaking · code splitting · dead-code elimination · duplicate dependencies · heavy libraries · unnecessary polyfills
- [ ] Unnecessary client components & hydration · expensive rendering · re-render frequency · memoization effectiveness
- [ ] Event-listener overhead · animation overhead · memory consumption/leaks · Web Workers · bundle-analyzer output · source-map exposure

## 44. Backend & Data Fetching Performance
- [ ] API response time · Sanity query latency · GROQ complexity · projection · over-/under-fetching · N+1 · duplicate requests · waterfalls · parallel fetching · deduplication
- [ ] Server caching · Data Cache · Full Route Cache · Router Cache · Sanity CDN · invalidation · ISR · on-demand revalidation · cache tags · cache paths · revalidation webhook
- [ ] Timeouts · retries · connection overhead · payload size · compression · pagination · large datasets · unnecessary dynamic rendering

## 45. Caching & CDN
- [ ] CDN config · caching of static assets, images, fonts, HTML, API · `Cache-Control` · ETag · stale behavior · invalidation · expiration
- [ ] ISR config · on-demand revalidation · Sanity CDN · Vercel CDN · consistency
- [ ] Preview cache isolation · draft-data isolation · authenticated-data caching · sensitive-response caching · cache-poisoning risks · cache-key correctness
- [ ] Geographic delivery · cache hit ratio · cache-related debugging
