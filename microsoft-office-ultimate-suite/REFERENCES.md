# Official Microsoft References

These links are starting points for verifying current application/API capabilities. Feature availability may depend on Microsoft 365 plan, platform, tenant settings, permissions, and product version.

## Excel automation
- Office Scripts overview: https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel
- Office Scripts introduction: https://support.microsoft.com/en-us/excel/office-scripts/introduction-to-office-scripts-in-excel
- Office Scripts fundamentals: https://learn.microsoft.com/en-us/office/dev/scripts/develop/scripting-fundamentals

## Outlook and Microsoft Graph
- Outlook mail API overview: https://learn.microsoft.com/en-us/graph/outlook-mail-concept-overview
- Outlook calendar API overview: https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview
- Mail, calendar, and contacts REST API overview: https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/office-365-rest-apis-for-mail-calendars-and-contacts

## OneNote and Microsoft Graph
- OneNote API overview: https://learn.microsoft.com/en-us/graph/integrate-with-onenote
- Use the OneNote REST API: https://learn.microsoft.com/en-us/graph/api/resources/onenote-api-overview?view=graph-rest-1.0
- Create OneNote pages: https://learn.microsoft.com/en-us/graph/onenote-create-page
- Get OneNote content and structure: https://learn.microsoft.com/en-us/graph/onenote-get-content

## VBA and Office automation
- Office VBA reference: https://learn.microsoft.com/en-us/office/vba/

## SharePoint, Teams, and Planner
- SharePoint Graph API overview: https://learn.microsoft.com/en-us/graph/api/resources/sharepoint
- Teams API overview: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview
- Planner API overview: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview
- SharePoint sharing and permissions: https://learn.microsoft.com/en-us/sharepoint/sharing-and-permissions

## Copilot and governance
- Microsoft 365 Copilot overview: https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-overview
- Microsoft Purview: https://learn.microsoft.com/en-us/purview/purview
- SharePoint Advanced Management: https://learn.microsoft.com/en-us/sharepoint/advanced-management
- Copilot readiness and adoption: https://learn.microsoft.com/en-us/copilot/microsoft-365/

## Word, PowerPoint, and Outlook automation
- Word VBA reference: https://learn.microsoft.com/en-us/office/vba/api/overview/word
- PowerPoint VBA reference: https://learn.microsoft.com/en-us/office/vba/api/overview/powerpoint
- Outlook VBA reference: https://learn.microsoft.com/en-us/office/vba/api/overview/outlook

## Design principle
Prefer stable, documented production interfaces. Microsoft Graph `beta` endpoints can change and should not be assumed production-stable. For OneNote Graph integration, use delegated authentication; app-only authentication is not supported.
