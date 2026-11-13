# NSE General Announcements Primary UI Surface — CSV Export Contract Boundary
Date: 2026-11-14

## Fresh official-page inspection
Official page:
https://www.nseindia.com/companies-listing/corporate-filings-announcements
Web retrieval: `turn687576view0`, current retrieval 2026-11-14.

At lines 139–166 the page exposes a dedicated **Announcements** panel:
- Company (Company Name or Symbol)
- Subject (keyword)
- Search By selector
- Date range presets: 1D, 1W, 1M, 3M, 1Y, Custom, Clear
- Play Announcements
- Download (.csv)
- Convert XBRL into Excel
- Refresh

The page contains multiple additional filing panels below this section, including distinct Company/Subject filters and other filing-specific fields (e.g., Debenture Trustee and ISIN). Therefore the page is a multi-panel filing dashboard; do not treat the whole page as one homogeneous announcement dataset.

## Important correction to prior investigation
The earlier research focused on the XBRL-only route and the limited Latest Announcements widget on the `corporate-filings-application` page. This newly inspected `corporate-filings-announcements` page exposes a dedicated general Announcements panel with a CSV control and date presets. It is a stronger official UI candidate for the RSS cross-check than the XBRL-only route.

This still does NOT prove the CSV export's exact request URL, response schema, pagination, or historical completeness. The page reader exposes controls but does not execute UI interactions or return downloaded CSV bytes. No guessed endpoint was called.

## Source-bound field contract (visible UI only)
- Issuer selector: company name or symbol
- Subject selector: keyword
- Search By: selector present; exact option values not exposed in text retrieval
- Date filter: preset or Custom; exact date input format not exposed
- Export: CSV control visible; exact filename, HTTP status, Content-Type, bytes and SHA-256 not captured
- Refresh and Play controls visible; their behavior not executed in this audit

## Recommended bounded acquisition
Use this exact official page in a browser session:
1. Open Announcements panel.
2. Set Search By to the source's publication/broadcast date option (verify actual label in UI).
3. Set Custom date range to 13-Nov-2026 through 14-Nov-2026.
4. Leave Company and Subject blank for broad capture; if the result set is too large, split by date only, not by guessed symbol.
5. Execute the page's GO/Refresh control, then Download (.csv).
6. Preserve the downloaded raw CSV bytes before parsing; record exact page URL, observed form labels/selected values, request URL from browser network log, status, final URL, response headers, retrieved_at_utc, byte count, SHA-256, row count and original column names.
7. Reconcile RSS records only by exact source symbol + normalized subject family + source attachment URL / stable filing identifier; do not use date alone. Preserve the original RSS pubDate string and timezone-naive state.

## Acceptance
| Check | Result |
|---|---|
| Official general Announcements panel found | VERIFIED |
| Company and Subject filters | VERIFIED |
| Search By selector | VERIFIED (option values unknown) |
| Custom date control | VERIFIED |
| CSV export affordance | VERIFIED |
| Exact request/response contract | NOT CAPTURED |
| CSV raw bytes/hash | NOT CAPTURED |
| 13-item RSS row-level reconciliation | NOT RUN |
| Corporate Events P0 | BLOCKED |

No code/workflow/production change, no paid API, no PR/merge, no synthetic data. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.

Source: Official NSE General Announcements page, `turn687576view0`, especially lines 139–166.
