# CDSL FPI Frequency Coverage Map — Calendar, Quarterly, Fortnightly and Daily Routes — 2026-11-13

## Objective
Map official CDSL FPI data routes by frequency and vintage to prevent mixing incompatible observations and identify which route can support daily research.

## Official landing page
https://www.cdslindia.com/Publications/ForeignPortInvestor.html
The official landing page has separate links for Latest, Current Month, Archive, Calendar Year, Financial Year, Quarterly, Fortnightly Sector-wise, Debt Utilisation, AUC, and trade-wise data. Its page footer reads 05-Nov-2026. This is landing-page metadata, not necessarily the data-as-of date for every linked dataset.

## Route findings

### 1. Calendar-year monthly net investment
URL: https://www.cdslindia.com/eservices/Publications/FIICalendar
- Official page heading: Monthly FPI/FII Net Investments (Calendar Year - 2026).
- Has a Year selector.
- Schema groups Equity, Debt-General Limit, Debt-VRR, Debt-FAR, Hybrid, Mutual Fund subcategories, AIF and Total.
- Notes that data is compiled from reports submitted to SEBI/depositories by DDP/Custodians and represents trades conducted on and up to previous trading day(s).
- No data rows were exposed in the rendered page extraction; selected year was not changed. No row count/date coverage asserted.
- Page footer last updated 20-May-2020 is a page footer, not the data vintage.

### 2. Quarterly net investment
URL: https://www.cdslindia.com/eservices/Publications/FIIQuarterly
- Official page heading: Quarterly FPI/FII Net Investments (2026).
- Has a Year selector.
- Uses the same broad category family, including equity, debt subtypes, hybrid, mutual fund subcategories, AIF and Total.
- Explicit methodology note: quarterly Debt-FAR, Mutual Funds and AIF segment have been included w.e.f. September 2024.
- No quarterly rows were exposed in rendered extraction; selector was not changed. No row count/date coverage asserted.

### 3. Fortnightly sector-wise FPI data
Official landing page lists a regular fortnightly archive through 15-Oct-2026 and 31-Oct-2026. The visible archive extends back to 15-Jan-2020, with an apparent historical gap between 2022 and 2023 in the extracted list. The landing page also contains a duplicate 15-Sep-2025 label. This is link-list evidence only; individual archive file contents were not downloaded or validated.
Use this route only for its stated fortnightly sector-wise purpose, not as daily aggregate FPI flow.

### 4. Daily trend archive (new format)
Official landing page lists daily trend files from 01-Sep-2024 through 04-Apr-2025 in the visible archive, with no newer daily trend files in that visible section. This is an archive-list boundary, not proof that CDSL daily confirmed FPI data ends in April 2025; current month/latest/daily page is a separate route.
Do not claim a continuous daily history or assume archive list completeness beyond what the page exposes.

### 5. Financial-year series
Current eServices FY page remains a separate annual aggregation (data-as-of 12-Nov-2026 in the previously audited observation). The legacy Publications FY page has a distinct older vintage. Do not merge those versions.

## Research frequency contract
| Frequency | Route | Use | Status |
|---|---|---|---|
| Daily | Latest / Current Month / Daily archive | Potential daily confirmed FPI context | Daily archive visible through 04-Apr-2025 only; full raw coverage unverified |
| Fortnightly | Sector-wise archive | Sector allocation / slower overlay | Visible archive through 31-Oct-2026; files not acquired |
| Monthly | Calendar-year selector | Monthly aggregation / slower overlay | Route identified; no selected-year rows acquired |
| Quarterly | Quarterly selector | Quarterly aggregation / slower overlay | Route identified; no rows acquired |
| Annual | Financial-year series | Long-horizon context | Rendered table arithmetic audited; raw file not acquired |

## Critical data boundary
CDSL notes its FPI data is compiled from DDP/Custodian reports and reflects trades on and up to previous trading days. It is confirmed-custodian-reported data, not same-day exchange provisional FII/FPI. Keep CDSL confirmed and NSE provisional series separate with their own dates, publication timestamps, frequency and vintage. Never backfill missing daily values from fortnightly, monthly, quarterly or annual totals.

## Next executable step
Use the official Calendar Year selector and Quarterly selector in a browser with real UI interaction, record selected year and returned rows, and export/preserve any offered file. Then acquire one recent fortnightly archive item (31-Oct-2026) as a controlled sample: record the exact linked file URL, MIME type, bytes, size and SHA-256 before parsing. Do not invent or reverse-engineer endpoints. Only after one file is genuinely acquired should schema and date/category coverage QA begin.

## Acceptance ledger
| Gate | State |
|---|---|
| Official CDSL frequency routes mapped | PASS |
| Calendar page schema/method note | PASS |
| Quarterly page schema/method note | PASS |
| Fortnightly archive listing observed | PASS |
| Daily archive visible-list boundary recorded | PASS |
| Calendar/quarterly selector query executed | NOT STARTED |
| Fortnightly file bytes acquired | NOT ACQUIRED |
| Daily full-history archive acquired | NOT ACQUIRED |
| Raw SHA-256 / schema QA | UNKNOWN / NOT STARTED |
| Daily confirmed-vs-provisional reconciliation | NOT STARTED |
| Daily factor acceptance | BLOCKED |

## Invariants
₹0 spend; free official sources only; no paid APIs/feeds or external contact; no synthetic rows/timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; no PR merge. Research-only.
