# Principles, Execution Rules & Change-Control

Source domains: 90 (Methodology), 97 (Execution Rules), 98 (Safety & Change-Control).

## Contents
1. Audit methodology (domain 90)
2. Execution order (domain 97)
3. Safety & change-control (domain 98)
4. Handling conflicts between rules

## 1. Audit methodology
- Audit the whole repository before concluding anything.
- Base conclusions on actual source, configuration, dependencies, accessible environments, implemented features, and the stated requirements/docs.
- Examine relationships: component ↔ component, frontend ↔ CMS, application ↔ external services.
- Check behavior in the **production build**, in a **browser**, and across **viewports**.
- Examine errors and warnings, edge cases, security boundaries, performance bottlenecks, operational risks.
- Verify every finding. Avoid assumptions without evidence. Avoid false positives.
- Never declare "safe" merely because nothing was found.
- Record areas that could not be accessed, checks not run, and audit limitations.

## 2. Execution order
1. Start with discovery. 2. Build the inventory before deep auditing. 3. Detect the stack automatically. 4. Identify relevant features. 5. Define audit scope. 6. Define the environment under audit. 7. Review documentation. 8. Review configuration. 9. Review source code. 10. Review dependencies. 11. Run **non-destructive** checks first. 12. Run automated checks if available. 13. Run runtime checks if the environment allows. 14. Use browser testing where needed. 15. Use security tools only within permission and scope. 16. Verify results. 17. Record evidence. 18. Write findings. 19. Prioritize risk. 20. Produce the report. 21. Wait for approval before remediation when required.

## 3. Safety & change-control (hard rules)
Do **not**:
- change source code in Audit-Only Mode;
- delete files without approval;
- change dependencies without evaluation;
- run destructive database commands;
- modify production datasets, publish CMS documents, or delete CMS assets;
- change domains or DNS, or production environment variables;
- rotate or revoke credentials without permission;
- load-test production without explicit approval;
- penetration-test outside scope and authorization;
- submit production forms that cause real transactions or real communications without permission;
- publish or delete deployments;
- disable monitoring or security controls;
- write secrets into the audit report;
- put personal data into logs or reports;
- declare a remediation successful before verification.

Safe defaults: read-only commands (`git log`, `git status`, `grep`, `npm ls`, `npm audit`, `tsc --noEmit`, `next build` in a scratch copy), HEAD/GET requests to authorized URLs, Lighthouse in a clean profile, staging/preview instead of production whenever possible.

## 4. Conflicts
If a user instruction conflicts with a safety rule (e.g. "just fix it while you audit"), switch mode explicitly: finish the audit report, then ask for approval to enter Remediation Mode. If the user explicitly authorizes a normally restricted action, restate scope and rollback in one sentence, then proceed.
