# Applicability & Coverage

Sources: domain 93 and the closing note of the master scope.

## Applicability per domain
Not all 99 domains apply to every project. Assign each one:
- **Applicable** — feature/risk exists in this project.
- **Not Applicable** — the feature does not exist (e.g. no login → authentication domain). Give the reason and the evidence ("no auth library, no /login route, no session cookies").
- **Not Verifiable** — applicable but you lack access/tool/permission (state what is missing).

Triage hints (stack-specific):
| Signal | Effect |
|---|---|
| No `next-auth`/`clerk`/`auth0`/custom session code, no protected routes | 17 N/A (still check Sanity Studio and preview auth in 26/28) |
| No database/ORM | SQL/NoSQL injection items N/A |
| No `app/api`, `route.ts`, or Server Actions | 18/35 reduce to external-integration checks |
| Single language, no i18n lib | 49 N/A |
| No payment/booking provider | those integration lines N/A |
| No Vercel/hosting access | 53 runtime parts Not Verifiable |
| Static export | Edge/ISR/on-demand revalidation items N/A |

## Coverage reporting (domain 93)
Report counts and lists for: total categories · completed · partially completed · not tested · N/A · critical routes covered · API endpoints covered · CMS document types covered · components covered · environments covered · browsers · viewports · tests executed/passed/failed/skipped · findings verified/unverified · evidence completeness · remaining uncertainties.

Reading source, running runtime tests, security testing and verifying production are **different activities**: report each separately. Use `templates/coverage-matrix.md`.
