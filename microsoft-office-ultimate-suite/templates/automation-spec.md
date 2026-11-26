# Automation Specification

## 1. Purpose

- Business outcome:
- Trigger (schedule/event/manual):
- Frequency and volume:
- Service-level expectation:
- Owner:

## 2. Systems and data

| System | Role | System of record? | Access method | Permissions |
|---|---|---|---|---|
| | | | | |

- Input schema:
- Output schema:
- Files/attachments:
- Time zones/locales:

## 3. Flow

1. Trigger:
2. Validate input:
3. Transform:
4. Write/act:
5. Notify:
6. Log/audit:

## 4. Reliability

- Idempotency key/duplicate detection:
- Retry policy and backoff:
- Timeout:
- Rate limits/pagination:
- Partial failure handling:
- Dead-letter/manual recovery:
- Rollback/disable procedure:
- Alerting and owner:

## 5. Security and governance

- Least-privilege scopes:
- Consent/connection ownership:
- Secret storage/rotation:
- DLP/sensitivity/retention:
- Personal data minimization:
- Audit logging:

## 6. Testing

- [ ] Happy path
- [ ] Duplicate trigger
- [ ] Malformed/missing payload
- [ ] Permission loss/expired token
- [ ] Rate limiting/throttling
- [ ] Downstream outage/timeout
- [ ] Partial success and retry
- [ ] Rollback/disable

## 7. Handoff

- Deployment/environment:
- Runbook:
- Monitoring:
- Known limitations:
