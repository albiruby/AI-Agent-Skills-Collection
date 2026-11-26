# Technology Adapters

Adapters add concrete, technology-specific verification to the universal audit. They do not replace product context, domain selection, or evidence standards.

## Selection table

| Adapter | Detection signals | Highest-yield blind spots |
|---|---|---|
| [`nextjs-vercel.md`](nextjs-vercel.md) | `next` dependency, `app/` or `pages/`, `middleware.ts`, `next.config.*`, Vercel deployment | Authorization inside server actions/route handlers, cache scope and revalidation, `NEXT_PUBLIC_` exposure, preview/draft protection, deployment skew |
| [`wordpress.md`](wordpress.md) | `wp-config.php`, `wp-content/`, `wp-json`, WooCommerce | Capability vs nonce, REST/AJAX exposure, stored XSS, uploads, personalized-content caching, wp-cron |
| [`ecommerce-and-payments.md`](ecommerce-and-payments.md) | Cart/checkout/order/payment models, provider SDKs, webhooks | Price recomputation, inventory races, duplicate charge/order, webhook replay, refund/entitlement gaps, currency rounding |
| [`supabase-postgres.md`](supabase-postgres.md) | Supabase client/config, RLS policies, migrations, PostgreSQL | RLS gaps, `security definer`, service-role exposure, tenant isolation, storage/realtime policies, constraint and migration drift |
| [`static-spa.md`](static-spa.md) | Static build output, client router, service worker, CDN config | SPA fallback and indexability, secrets in bundles, client-trusted APIs, stale service-worker cache, deep links |
| [`ai-enabled-product.md`](ai-enabled-product.md) | LLM SDKs, prompts, RAG, tool calling, evals | Indirect prompt injection, tool authorization, unsafe output rendering, cross-tenant retrieval, PII to providers, cost/latency, eval drift |

## How to use

1. Confirm the technology from local evidence, not from assumptions.
2. Load only the adapters that match the target's actual runtime and risk.
3. Combine adapters where boundaries overlap (for example, Next.js + Supabase + e-commerce).
4. Keep the universal domain briefs as the frame; adapters add checks, not scope.
5. If no adapter exists, follow the unknown-technology path in `references/03-adaptive-selection.md`.

Do not load an adapter merely because the technology is popular or might be used elsewhere in the organization.

## Adapter versus profile

- A **profile** describes the product/business shape: SaaS, marketplace, booking, publishing.
- An **adapter** describes implementation behavior: framework, hosting, database, CMS, payment platform.
- A **capability** describes what the product can do: auth, payments, uploads, search, AI.

A single audit can load multiple profiles, capabilities, and adapters. Record which ones were used and why.

## Rules

- Adapters must remain evidence-oriented; a technology pattern is a lead, not a finding.
- Do not duplicate universal guidance; link to the relevant domain brief.
- Version-specific behavior must be verified, not assumed.
- Prefer observable behavior and local configuration over general best practices.
- Include false positives and conditions where a check is irrelevant.
- Never include destructive commands or require production mutation.
- State when an adapter was not applicable because the technology was not confirmed.

## Adding an adapter

Follow `references/11-adapter-authoring.md`. Keep the structure consistent:

`Purpose → Detection signals → Applicability → Boundaries and data flows → Audit procedures → Verification methods → Common failure modes → Evidence requirements → Safety constraints → Related modules`

Adapters are added when repeated audits show a real gap, not to mirror a framework's documentation.
