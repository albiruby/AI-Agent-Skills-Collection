---
name: pra-codebase-architecture
description: Audit code quality, software architecture, Next.js App Router architecture, React patterns, TypeScript strictness, Tailwind/CSS design-system code and UI component architecture. Use when the user asks for a code review, architecture review, "cek kualitas kode", hydration errors, use client boundaries, server/client leakage, any/ts-ignore usage, dead code, circular dependencies, Tailwind or design token consistency, component duplication, or technical debt in a Next.js/React/TypeScript project. Covers audit domains 5-11.
---

# Code, Architecture, Next.js, React, TS, Styling, UI (Domains 5–11)

Parent: `production-readiness-audit`. Prerequisite: inventory from `pra-discovery`. Full lists: `references/checklist.md`.

## Procedure
1. **Static signals (read-only)**
   - `npx tsc --noEmit` · `npx eslint .` (use project config; do not auto-fix) · check `tsconfig.json` for `strict`, `noImplicitAny`, `strictNullChecks`, `noUncheckedIndexedAccess`.
   - Counts via grep: `any`, `@ts-ignore`, `@ts-expect-error`, `as unknown as`, `console.log`, `debugger`, `TODO|FIXME|HACK`, `dangerouslySetInnerHTML`.
   - Dead code: `npx knip` or `ts-prune`/`depcheck` if allowed (they only read); otherwise grep for unused exports/components.
   - Cycles: `npx madge --circular --extensions ts,tsx .` if available.
2. **Next.js architecture**
   - Router and layout tree; `loading.tsx`, `error.tsx`, `global-error.tsx`, `not-found.tsx` present where needed.
   - Server/Client boundary: `'use client'` placed as low as possible; no server-only code (secrets, `fs`, Sanity write client) imported into client components; `server-only` package used for sensitive modules.
   - Data fetching: parallel vs waterfall, `fetch` cache options, `revalidate`, tags, `generateStaticParams`, `dynamic`/`dynamicParams`, `notFound()` on missing slug.
   - Metadata API: `generateMetadata`, `metadataBase`, OG images; Draft/Preview mode; `middleware`/`proxy` matcher correctness (name differs by Next version — check docs for the installed version).
   - `next.config.*`: images `remotePatterns` (no wildcard hosts), headers/redirects/rewrites, `poweredByHeader`, source maps, experimental flags, deprecated options.
   - Runtime: Node vs Edge compatibility of imported libraries.
   - Hydration: look for `Date.now()/Math.random()/window/localStorage` in render, invalid HTML nesting, browser-only branches, extension-sensitive markup; check the browser console in the production build.
3. **React**: effect misuse (derived state in effects, missing cleanup, fetch-in-effect where server fetching fits), dependency arrays, unstable keys, context re-render storms, memoization misuse, controlled/uncontrolled mixing, event-listener/observer/timer cleanup, Strict Mode double-invoke safety, Suspense/error boundaries.
4. **TypeScript**: unsafe casts at API/CMS boundaries; runtime validation (zod/valibot) where external data enters; typed env access; generated Sanity types in sync; discriminated unions for CMS block types.
5. **Styling**: Tailwind config/content globs correct (no purged classes in prod), design tokens vs arbitrary values, CSS variables, z-index scale, fixed/sticky stacking, reduced-motion, font loading/fallback/licensing, dark-mode handling if present, `overflow` traps, layout shift.
6. **Components/UI**: shared vs page-specific, variant APIs, duplicated components, states (loading/empty/error), keyboard/focus handling in modals/menus/carousels (details in `pra-accessibility-responsive`).
7. **Architecture**: layering (presentation / business / data / integration), dependency direction, feature organization, config management, single points of failure, over/under-engineering, fit with project size.

## Calibration
- `any` in a utility = Low; `any` on CMS/API boundary feeding rendering = Medium.
- Hydration error in production console = Medium–High depending on page.
- Server secret reachable from a client component = Critical (also log in `pra-security`).
- Style preference ≠ finding. Report only what harms correctness, maintainability, security, performance, or accessibility, and say how.

## Output
Findings (`CODE-NNN`) with file:line, plus an architecture summary (diagram or bullet map), debt register, refactor candidates (clearly labelled *recommendations*, not blockers).

## Pitfalls
Recommending rewrites during an audit · judging by personal style · flagging every `'use client'` as wrong (interactive leaf components need it) · ignoring the installed Next.js version's conventions.
