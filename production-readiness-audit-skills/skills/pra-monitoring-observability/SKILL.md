---
name: pra-monitoring-observability
description: Audit monitoring and observability readiness - uptime/availability checks, application error tracking (Sentry etc.), logging and redaction, real-user monitoring and Core Web Vitals, analytics accuracy and consent, alert routing, and operational dashboards. Use when the user asks "kalau website down siapa yang tahu?", whether monitoring/alerting/analytics is set up, Sentry/Vercel Analytics/Speed Insights/Uptime checks, log retention, alert noise, GA4/Tag Manager accuracy, or post-launch visibility. Covers audit domains 57-64.
---

# Monitoring, Errors, Logs, RUM, Analytics, Alerts (Domains 57–64)

Parent: `production-readiness-audit`. Question to answer: **if production breaks at 2 a.m., who finds out, how fast, and what do they see?** Lists: `references/checklist.md`.

## Procedure
1. **Inventory (57)**: what tools exist (Vercel Analytics/Speed Insights/Logs, Sentry/Highlight/LogRocket, UptimeRobot/Better Stack/Checkly, GA4/Plausible/PostHog, Search Console, Sanity webhook logs), who owns each, which environments they cover (production-only — previews must not pollute data), cost, retention, access list. Mark gaps; a missing tool is a finding only if the risk justifies it (a brochure site needs uptime + basic errors, not APM).
2. **Uptime (58)**: external synthetic checks for home, a deep brand/detail page, a CMS-dependent page, form endpoint (health, not submission), DNS and SSL expiry, key third parties; interval (1–5 min), multi-region, confirmation retries (avoid false positives), keyword assertion (not just 200), status page/maintenance windows, availability target (e.g. 99.9%) stated.
3. **Errors (59)**: client SDK + server/route-handler/Server-Action capture, React error boundaries reporting, hydration errors, unhandled rejections, source maps uploaded **privately** (not public), release/commit tagging, environment tags, PII scrubbing, sampling and quotas, grouping, alert thresholds, ownership. Verify with a **test event in staging** (not a production fault injection).
4. **Logging (60)**: runtime/build/webhook/form logs: structured (JSON), levels, request/correlation IDs, redaction of tokens/PII/emails, retention (Vercel log retention is short — drains if needed), access control, volume/cost, alertability. Grep code for `console.log(` of objects that may contain PII/tokens.
5. **RUM & Web Vitals (61)**: field LCP/INP/CLS/TTFB by page, device, geography; regression alerts; budgets; coverage of mobile and Indonesian networks.
6. **Analytics (62)**: tag installed once (no duplicate events), correct property per environment, internal/preview traffic filtered, events for CTAs/forms/external order-booking clicks/career applications, campaign attribution (UTM), consent-aware loading (cross-check `pra-privacy-legal`), data retention, KPI definitions agreed with the business, reports/dashboards usable.
7. **Alerting (63)**: critical outage, error spike, failed deploy, SSL/domain expiry, security/dependency alerts, usage/cost thresholds, CMS/webhook failures, form delivery failures; routing (email/Slack/phone), escalation, severity, dedupe/noise, acknowledgement, **tested alert path**.
8. **Dashboard (64)**: one place showing availability, error rate, deploy status, Web Vitals, API/CMS status, traffic/conversions, usage vs quota, cost, security alerts, backup status, incident history.

## Calibration
- No uptime monitoring and no error tracking at launch of a business-critical site → Medium–High (launch condition).
- Alerts go to a single unattended inbox / ex-employee → Medium.
- Public source maps or PII in logs/error payloads → Medium–High.
- Duplicate analytics events skewing KPIs → Low–Medium.

## Output
Monitoring coverage matrix (signal · tool · owner · alert · tested?), gap list, alert routing table, findings (`MON-NNN`) and a minimal viable monitoring recommendation sized to the project.

## Pitfalls
Recommending enterprise stacks for a small site · injecting production faults to test alerts · assuming installed = working (verify events arrive) · ignoring ownership.
