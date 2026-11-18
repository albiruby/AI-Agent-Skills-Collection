---
name: pra-backup-recovery-incident
description: Audit backup, restore, disaster recovery, rollback and incident-response readiness, and support incident-mode diagnosis. Use when the user asks "kalau data hilang bagaimana?", about Sanity dataset/asset backups, repository backup, restoring a deleted document or deployment, RTO/RPO, rollback to a previous Vercel deployment, domain or credential compromise plans, incident runbooks, or when an incident is happening (outage, leaked secret, defaced site, bad deploy, CMS data deletion). Covers audit domains 65-69 and Incident Mode.
---

# Backup, Recovery, DR, Rollback, Incident (Domains 65–69)

Parent: `production-readiness-audit`. A backup that has never been restored is a hope, not a backup. Lists: `references/checklist.md`.

## Audit procedure
1. **Backup scope (65)** — for each asset class record *what, where, how often, retention, encryption, who can access, who owns, verified when, failure alerting*:
   - Source: Git remote(s), mirror/second remote, local clones are not a backup plan; org-level protections.
   - Sanity: dataset export (`sanity dataset export <dataset>` includes assets by default; schedule via CI/cron to private storage), dataset backups feature availability per plan (confirm in docs), schema is in Git, Studio config in Git.
   - Config: env var inventory (names + where values live — password manager/Vercel; values never in repo), DNS zone export, domain registrar details, integration configs (email, maps, analytics), documentation.
2. **Restore (66)**: documented procedure per asset; has a restore been rehearsed? Time it. Restore targets: new repo from backup, dataset import into a scratch dataset (never over production), deleted document recovery via document history, deleted asset recovery, previous deployment restoration, DNS recreation, SSL reissue, environment rebuilt from docs only. Verify data integrity after restore (counts, references, assets).
3. **Disaster scenarios (67)**: hosting outage, CMS outage, DNS outage, domain compromise, credential compromise, accidental data deletion, bad deployment, repository loss, third-party/email outage, data corruption, security breach. For each: detection, owner, first-hour actions, workaround (e.g. static fallback, alternate contact channel), communication. State **RTO/RPO** targets and whether current setup can meet them.
4. **Rollback (68)**: Vercel instant rollback / redeploy previous deployment available and permitted for the right people; release identification (tags, deployment IDs); schema/content compatibility between versions (rolling back code that expects newer CMS fields); env/DNS rollback; cache invalidation after rollback; webhook compatibility; rollback tested; emergency deploy procedure.
5. **Incident response (69)**: plan exists? owner/on-call, severity levels, escalation, provider contacts (Vercel, Sanity, registrar), internal/external comms templates, security-incident and data-breach handling (legal timelines under applicable law), secret-leak procedure (revoke → rotate → purge → review logs), evidence preservation, timeline, RCA, post-incident review, preventive actions.

## Incident Mode (when something is actually broken)
1. Stabilize first: identify blast radius, **freeze deploys**, preserve evidence (logs, deployment IDs, timestamps) before changing anything.
2. Triage by type — bad deploy → roll back (with approval); CMS bad content → restore from history; leaked secret → revoke/rotate (owner action) then search history and logs for misuse; DNS/domain → registrar lockdown and verification; outage at provider → check status pages, communicate.
3. Propose the least-destructive fix; get explicit approval for each production-affecting step; verify via smoke test; write the timeline and follow-ups (use `pra-reporting-risk` templates).

## Calibration
- No backup of CMS content/assets and no export process → High.
- Single person holds all accounts / no recovery method → High (see `pra-maintenance-governance`).
- No tested rollback → Medium–High. No incident owner/runbook for a small site → Medium/Low.
- Backups exist but never restored → Medium (unverified).

## Output
Backup register, restore-test results (or "not tested"), DR scenario table with RTO/RPO, rollback procedure review, incident readiness gaps (`BCP-NNN`).

## Pitfalls
Running a restore over production · exporting production data (with personal data) to unprotected storage · writing a 40-page plan nobody will use — prefer a one-page runbook per scenario.
