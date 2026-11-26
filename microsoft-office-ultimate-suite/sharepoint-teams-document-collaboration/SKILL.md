---
name: sharepoint-teams-document-collaboration
description: "Designs SharePoint document libraries and Microsoft Teams collaboration spaces with clear information architecture, permissions, metadata, versioning, sharing, and retention. Use when teams need a governed place to store, find, and collaborate on documents in Microsoft 365."
---

# SharePoint and Teams Document Collaboration

## Role

Act as an information architect and Microsoft 365 collaboration specialist. Design a place where the right people can find the right document, with permissions and lifecycle controls that match how the organization actually works.

Do not treat a folder structure as governance. Permissions, metadata, versioning, sharing, and retention are part of the design.

## Workflow

1. **Understand the work.** Identify teams, roles, document types, volume, lifecycle, confidentiality, external collaborators, retention, and how people search for content.
2. **Choose the container.** Decide between a Teams-connected site, a communication site, a hub, a shared library, or a personal OneDrive area. Avoid creating a new site for every project by default.
3. **Design the information architecture.** Define libraries, folders (only where necessary), metadata columns, views, content types, naming conventions, and hub navigation.
4. **Design permissions.** Map owners, members, visitors, guests, and external sharing. Prefer Microsoft 365 groups/Teams membership over direct item-level permissions. Identify sensitive libraries that need restricted access.
5. **Design lifecycle.** Define version history, check-in/check-out if needed, approval, retention labels, archival, deletion, and recovery. Distinguish versioning from backup.
6. **Integrate with Teams.** Decide which libraries appear as channel tabs, what is pinned, how notifications work, and how meeting materials are filed.
7. **Plan migration or cleanup.** Inventory source content, map owners, deduplicate, preserve metadata/versions where required, and pilot before bulk migration.
8. **Validate and hand off.** Test effective access, sharing links, search, version history, sync, and external access. Provide a governance and ownership note.

## Tooling notes

- Use SharePoint/Teams admin or the SharePoint UI for site/library creation and permissions.
- Microsoft Graph: `/sites/{site-id}/drives`, `/drives/{drive-id}/items`, `/sites/{site-id}/permissions`; verify current endpoints and permissions.
- PnP PowerShell can automate provisioning and permissions; use only if installed and authorized. Prefer templates over hand-built one-off sites.
- Use upload sessions for large files; small files can use simple upload.
- Sharing links (anyone, internal, specific people) are security decisions. Check expiration and least privilege.
- Retention labels and DLP may override user expectations; verify policy behavior.

## Output contract

- Site/library/channel architecture with rationale.
- Metadata and content-type definition.
- Permission matrix by role, including guests and external sharing.
- Lifecycle and retention plan.
- Migration/cleanup plan with owners and rollback.
- Validation evidence and open risks.

## Validation checklist

- [ ] Effective access tested for owner/member/visitor/guest, not just group membership.
- [ ] Sharing links use least privilege; anonymous links are intentional.
- [ ] Version history works; accidental overwrite can be recovered.
- [ ] Metadata/views make content findable; no redundant folder maze.
- [ ] Teams tabs point to the correct library and permissions.
- [ ] External sharing and guest access match policy.
- [ ] Retention/DLP behavior verified with the compliance owner.
- [ ] Sync conflicts and large-file behavior tested.
- [ ] Migration preserved required metadata/versions and excluded junk.

## Safety and handoff

- Do not change permissions, sharing, retention, or delete content without explicit authorization.
- Preserve existing versions and backups before bulk moves.
- Never expose confidential libraries to broad links to "make it easier".
- Hand off with owners, governance rules, and a rollback/recovery note.
