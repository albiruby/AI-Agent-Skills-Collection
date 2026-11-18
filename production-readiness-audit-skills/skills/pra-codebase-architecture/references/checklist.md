# Checklist — Domains 5–11

## 5. Codebase Quality
- [ ] Structure: folder & file structure · naming conventions · separation of concerns · single responsibility · tight coupling · circular dependencies
- [ ] Readability: readability · consistency · inconsistent patterns · comment quality · documentation quality · TODO/FIXME/HACK · debug statements · development-only code
- [ ] Waste: duplication · dead code · unused components/functions/imports/dependencies/assets · unnecessary abstractions · over-engineering · under-engineering · unnecessary conditionals/state/effects
- [ ] Complexity: excessive component complexity · excessive prop drilling · hardcoded values · magic numbers · repeated configuration
- [ ] Quality attributes: reusability · maintainability · extensibility · scalability · error-handling consistency · logging consistency
- [ ] Runtime hazards: race conditions · memory leaks · resource cleanup · asynchronous execution issues

## 6. Software Architecture
- [ ] Overall architecture · layer separation (presentation, business logic, data access, integration) · server/client boundaries
- [ ] Component & shared-component architecture · feature-based organization · domain boundaries · dependency direction · abstraction quality
- [ ] Data flow · state management · error propagation · configuration management
- [ ] Extensibility · scalability · reusability · maintainability · resilience · fault isolation · single points of failure
- [ ] External service dependencies · architectural consistency · unnecessary complexity · anti-patterns · technical debt · fit with requirements

## 7. Next.js Architecture
- [ ] Version · App Router config · `app/` structure · route groups · nested/root layouts · templates · pages · loading UI · error boundaries · global error · Not Found
- [ ] Route handlers · middleware/proxy (per version) · Server Components · Client Components · `use client` boundaries · Server Actions (if used)
- [ ] Data fetching (server/client) · static vs dynamic rendering · streaming · Suspense · partial rendering (if used)
- [ ] Metadata API · dynamic metadata · image/font optimization · script loading
- [ ] Caching · revalidation · route config · static params generation · dynamic params handling
- [ ] Redirects · rewrites · headers · cookies · Draft Mode · Preview Mode
- [ ] Production build config · runtime compatibility · Node vs Edge · server-only modules · client bundle exposure
- [ ] Hydration consistency & errors · server/client data mismatch · deprecated APIs · unsupported configuration · upgrade compatibility

## 8. React Architecture
- [ ] Component hierarchy · responsibility · composition · reuse · props design · props typing
- [ ] State management · ownership · synchronization · Context usage · derived state · controlled vs uncontrolled inputs
- [ ] Hooks usage · dependency arrays · `useMemo`/`useCallback`/`useEffect` misuse · memoization · unnecessary re-renders
- [ ] Lifecycle · event handling · listener cleanup · ref management · portals · Suspense · error boundaries
- [ ] Strict Mode compatibility · hydration · concurrent rendering compatibility · React version compatibility · deprecated patterns · unnecessary client-side rendering

## 9. TypeScript
- [ ] `strict` · `strictNullChecks` · `noImplicitAny` · type coverage · explicit return types where useful · type safety · interface/type consistency
- [ ] Union types · discriminated unions · generics · narrowing · nullability · optional properties
- [ ] Assertions · unsafe casts · `any` · `unknown` handling · `@ts-ignore` · `@ts-expect-error`
- [ ] Declaration files · third-party types · generated-type consistency
- [ ] Typing of: API responses · CMS data · form data · env vars · props · events · utilities
- [ ] Runtime validation vs compile-time typing

## 10. Styling & Design System Code
- [ ] Tailwind config · CSS architecture · global styles · CSS Modules · CSS variables · specificity · conflicting/duplicate/unused CSS · arbitrary values · inline styles
- [ ] Tokens: color · typography · spacing · breakpoint · radius · border · shadow · motion
- [ ] Responsive utilities · dark/light theme · design-system consistency · unnecessary visual overrides
- [ ] Fonts: loading · fallback · licensing
- [ ] Animation implementation · reduced-motion · layout stability · stacking contexts · z-index hierarchy · overflow · fixed/sticky positioning · browser compatibility

## 11. Component & UI Architecture
- [ ] Shared · page-specific · layout · navigation · footer · hero components · cards · carousels · marquees · modals · dialogs · dropdowns · menus · forms · buttons · links · accordions · tabs · galleries · image viewers · maps
- [ ] Loading indicators · skeletons · empty states · error states · toasts/notifications · UI primitives · variants · API consistency
- [ ] Accessibility · responsive behavior · keyboard interactions · focus handling · touch interactions
- [ ] Component isolation · visual consistency · regression risk · unnecessary duplication
