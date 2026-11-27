# Reference: Platform Requirements Adapter

## Purpose

This guide prevents the skill pack from relying on stale or universal assumptions about store, documentation-site, or publishing requirements. Requirements vary by platform, asset type, app category, locale, and submission context.

## Required procedure

When a user asks for assets to be “store-ready,” “submission-ready,” or compliant with a named platform:

1. Identify the exact platform and destination surface (for example, app listing screenshot, feature graphic, product page, extension listing, documentation website).
2. Identify the exact asset category and submission context.
3. Retrieve current requirements from official platform documentation or official developer resources.
4. Record the source title/URL and date checked in the asset manifest or QA report.
5. Extract required dimensions, aspect ratios, formats, file-size limits, transparency rules, content restrictions, safe areas, localization requirements, and any other applicable constraints.
6. Apply those constraints to the output.
7. Validate the final file properties and content against the requirements.
8. Report any requirements that could not be verified.

## Source hierarchy

Prefer:

1. Current official platform/developer documentation.
2. Official submission console or validator feedback, if accessible and authorized.
3. Official platform announcements or policy pages.
4. Reputable secondary sources only as supporting context, never as the sole basis for a critical compliance claim.

## Do not

- Hardcode remembered dimensions as universal rules.
- Assume a screenshot size for one store placement applies to another.
- Assume requirements are unchanged from an earlier release.
- Claim store compliance because an image looks polished.
- Claim submission or publication when only files were prepared.

## Suggested requirement record

```text
Platform:
Destination / placement:
Asset type:
Official source URL:
Date checked:
Required dimensions / aspect ratio:
Allowed file formats:
Maximum file size:
Transparency / color requirements:
Text / safe-area requirements:
Other restrictions:
Validation result:
Unverified items:
```

If internet access or official documentation is unavailable, prepare assets to the user's supplied specification and label platform compliance as **not verified**.
