# Checklist — Domains 96–99

## 96. Audit Modes
- [ ] Discovery · Audit-Only · Deep Audit · Security Audit · Performance Audit · CMS Audit · Production Readiness · Remediation · Verification · Maintenance · Incident
- [ ] Current mode stated; mode switches explicit

## 97. Audit Execution Rules
- [ ] Discovery first · inventory before deep audit · stack auto-detected · relevant features identified · scope & environment determined
- [ ] Docs, configuration, source, dependencies reviewed · non-destructive checks first · automated checks · runtime checks · browser testing · security tools within permission and scope
- [ ] Results verified · evidence recorded · findings written · risks prioritized · report produced · approval awaited before remediation when required

## 98. Safety & Change-Control Rules
- [ ] No source changes in Audit-Only · no file deletion without approval · no dependency change without evaluation · no destructive DB commands
- [ ] No production dataset changes · no CMS publishing · no CMS asset deletion · no domain/DNS changes · no production env-var changes · no credential rotation/revocation without permission
- [ ] No production load testing without approval · no out-of-scope pen-testing · no real production form submissions without permission · no deployment publishing/deletion · no disabling monitoring or security controls
- [ ] No secrets in reports · no personal data in logs/reports · no remediation-success claims before verification

## 99. Remediation & Verification Rules
- [ ] Fix by priority · controlled groups · no unrelated refactors · preserve design system · existing functionality · CMS data contract · route compatibility · backward compatibility
- [ ] Add tests for fixed bugs · run lint · typecheck · build · unit/integration · E2E · regression
- [ ] Check visual changes · responsive behavior · security implications · production configuration
- [ ] Document changes · update findings · re-audit affected areas · prepare rollback for risky changes
