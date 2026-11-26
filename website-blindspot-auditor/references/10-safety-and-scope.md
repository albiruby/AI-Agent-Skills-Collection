# Safety, Authorization, and Scope

## 1. Default permission

Assume read-only access. Safe default activities include reading project files, reviewing configuration without exposing secrets, inspecting existing tests, and running non-destructive local checks when they do not modify project state or contact unauthorized systems.

## 2. Actions requiring explicit authorization

Obtain explicit approval for the specific action before:

- Editing or deleting source files.
- Installing, upgrading, or removing dependencies.
- Changing environment variables, secrets, permissions, or deployment configuration.
- Modifying database records, schemas, migrations, or storage objects.
- Running load, fuzz, destructive, or state-changing tests.
- Sending real emails, payments, notifications, or webhooks.
- Testing production accounts, data, endpoints, or infrastructure.
- Scanning systems beyond the user's owned/authorized scope.

A general request to “audit the website” is not blanket permission for destructive or intrusive testing.

## 3. Production and third-party boundaries

Do not probe external services, customer systems, or public targets as if ownership were established. If authorization is unclear, restrict work to supplied source, documentation, local configuration, or a safe sandbox and disclose the limitation.

## 4. Secrets and personal data

- Never reveal secret values, access tokens, credentials, private keys, or personal data in the report.
- Redact values and report file/location plus exposure implications.
- Do not copy production records into reports or logs.
- Prefer synthetic test data.
- Do not send sensitive data to external tools or services unless authorized and appropriate.

## 5. Testing safety

- Prefer isolated local or staging environments.
- Use payment-provider sandbox modes and synthetic identities.
- Avoid destructive payloads and denial-of-service behavior.
- Apply request limits and stop if unexpected impact appears.
- Do not bypass controls on a live system to “prove” a hypothesis.
- Record environment and test conditions.

## 6. Changes and remediation

An audit recommendation is not permission to implement it. If the user authorizes fixes, scope changes narrowly, preserve existing conventions, add or update tests, and report changed files and validation results. Ask before data migrations, irreversible actions, or production deployment.

## 7. Legal and compliance caution

Identify potentially relevant obligations from project context, but do not give legal certification. Describe observed gaps and recommend qualified legal/privacy review where necessary.

## 8. Stop conditions

Stop an active test if it causes unexpected state change, impacts an unrelated user/system, exposes sensitive information, or exceeds the agreed scope. Report what happened without repeating sensitive details.
