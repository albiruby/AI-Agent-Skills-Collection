# Cross-Layer and Systemic Analysis

## 1. Goal

Discover failures that arise between components, not only defects inside individual files or services. Apply this method to the architecture that actually exists.

## 2. Trace an end-to-end transaction

For every critical journey, map applicable stages:

1. User or external trigger.
2. Client/UI state and validation.
3. Transport/request boundary.
4. Authentication and authorization.
5. Business rules and orchestration.
6. Persistence or external side effect.
7. Queue, webhook, scheduled task, or notification.
8. Cache, search index, analytics, or derived view.
9. User-visible confirmation and recovery.

For each stage, record owner, input/output, authoritative state, failure mode, retry behavior, and observability.

## 3. Partial-failure questions

- Can stage A succeed while stage B fails?
- Is there a compensating action or reconciliation process?
- Does the user see an accurate pending/failed/succeeded state?
- Can retry duplicate an already-completed operation?
- Is an operation idempotent or guarded by a unique key/constraint?
- Can events arrive late, twice, out of order, or not at all?
- Is there a timeout after which the system's state becomes ambiguous?
- Can stale caches or indexes misrepresent the authoritative state?

## 4. Common interaction boundaries

Only inspect those that exist:

- Browser ↔ frontend server.
- Frontend ↔ API/server action.
- API ↔ database/cache.
- Application ↔ identity provider.
- CMS ↔ rendering layer/cache/CDN.
- Payment provider ↔ webhook ↔ order/billing state.
- Object storage ↔ metadata/database.
- Queue ↔ worker ↔ database.
- Application ↔ email/SMS/push provider.
- Application ↔ analytics/experimentation platform.
- CI/CD ↔ artifact registry ↔ runtime.
- Application ↔ AI/model/tool provider.

## 5. Cross-layer consistency

Check whether the same concept has consistent meaning and lifecycle across layers. Examples:

- User identity and tenant ownership.
- Currency, amount precision, and rounding.
- Timezone and date boundaries.
- Content publication state.
- Entitlement and subscription status.
- File ownership and access URLs.
- Soft deletion and visibility.
- Cache keys and authorization scope.
- Error and retry semantics.

## 6. Deployment and version overlap

Where deployment access or configuration is available, consider:

- Old and new application versions running simultaneously.
- Database migration before/after application rollout.
- Backward/forward compatibility of events and API payloads.
- Cache invalidation at release time.
- Rollback after irreversible schema/data changes.
- Background workers running older code against new data.

## 7. Report systemic findings

When multiple symptoms share a root cause, report the root cause and list affected paths. Avoid presenting every downstream symptom as an independent finding unless remediation differs.
