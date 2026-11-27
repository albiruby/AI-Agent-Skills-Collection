# Platform Visual Asset Specifications

Reference dimensions and formats for common app stores and software distribution channels.

## Garmin Connect IQ Store

| Asset | Recommended Filename | Dimensions (px) | Format | Notes |
| :--- | :--- | :--- | :--- | :--- |
| App Cover / Icon | `COVER_500x500.jpg` | `500 x 500` | JPG / PNG | Square, crisp device silhouette + title |
| Hero Banner | `HERO_1440x720.jpg` | `1440 x 720` | JPG / PNG | 2:1 aspect, multi-device showcase + value prop |
| Feature Screens (1-5) | `SCREEN_1_<slug>.jpg` | `1440 x 900` | JPG / PNG | 16:10 or 3:2 aspect, up to 5 store preview slides |
| Lossless Masters | `master/*.png` | Same as above | PNG | Archival uncompressed masters for future edits |

## Apple App Store

| Asset | Dimensions (px) | Format | Notes |
| :--- | :--- | :--- | :--- |
| App Icon | `1024 x 1024` | PNG (no alpha) | Flat background, zero rounded corner mask |
| iPhone 6.9" / 6.7" | `1290 x 2796` | PNG / JPG | Up to 10 screenshots, `mobile_panel` layout |
| iPad Pro 13" | `2048 x 2732` | PNG / JPG | Required if iPad supported |

## Google Play Store

| Asset | Dimensions (px) | Format | Notes |
| :--- | :--- | :--- | :--- |
| App Icon | `512 x 512` | PNG | 32-bit PNG |
| Feature Graphic | `1024 x 500` | JPG / PNG | `hero_overlap` layout |
| Phone Screenshots | `1080 x 1920` | JPG / PNG | 9:16 portrait, 2 to 8 screens |

## Web, SaaS, GitHub & Product Hunt

| Asset | Recommended Filename | Dimensions (px) | Format | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Open Graph (OG) | `OG_1200x630.png` | `1200 x 630` | PNG / JPG | Social link preview card |
| GitHub Social Preview | `GITHUB_SOCIAL_1280x640.png` | `1280 x 640` | PNG | 2:1 aspect, safe 40pt margin |
| Product Hunt Gallery | `SCREEN_1_<slug>.png` | `1270 x 760` | PNG / JPG | `feature_showcase` or `hero_overlap` |
| Chrome Web Store Marquee | `MARQUEE_1400x560.png` | `1400 x 560` | PNG / JPG | `hero_overlap` layout |

## Requirement verification rule

These are working defaults, not a guarantee. Stores change dimensions, formats, text rules, and safe areas.

1. Identify the exact placement and asset type.
2. Check current official developer/store documentation.
3. Record the source URL and date checked in the manifest or QA report.
4. Apply the current rules.
5. Mark compliance **not verified** if official sources are unavailable.

Do not hardcode an old dimension because it is in this table. Do not assume one placement's size applies to another.
