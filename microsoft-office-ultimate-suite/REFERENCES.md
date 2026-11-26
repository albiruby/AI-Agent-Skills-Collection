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

## Design principle
Prefer stable, documented production interfaces. Microsoft Graph `beta` endpoints can change and should not be assumed production-stable. For OneNote Graph integration, use delegated authentication; app-only authentication is not supported.
