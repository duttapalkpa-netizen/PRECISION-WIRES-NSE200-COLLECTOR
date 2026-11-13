# NSE Indices Public Historical Data Route — India VIX Alternate Route Audit — 2026-11-13

## Objective
Identify a second official, free public route for India VIX historical OHLC, without relying on the previously inspected NSE India VIX page's empty rendered state or any paid NSE Data & Analytics product.

## Official route evidence
1. NSE India's official India VIX product page links users to "Search Historical value of India VIX" and describes India VIX as expected volatility over the next 30 calendar days, calculated from NIFTY options bid-ask prices:
   https://www.nseindia.com/static/products-services/indices-indiavix-index
2. NSE Indices public Historical Data Reports page provides selectors for Index Type, Sub-IndexType, Index, and time period, plus a CSV-format option. It exposes the historical OHLC table and a separate table with Date, Open, High, Low, Close, Prev. Close, Change and % Change fields:
   https://www.niftyindices.com/reports/historical-data
3. NSE's official Historical Reports index separately links to the NSE India Historical Data - India Vix page:
   https://www.nseindia.com/static/resources/historical-reports-capital-market-daily-monthly-archives

## What is newly established
- An official NSE Indices historical-data interface exists independently of the previously audited NSE India dedicated VIX page.
- The NSE Indices interface explicitly offers a CSV-format output and has an OHLC schema compatible in core fields with the VIX research input.
- The official NSE India VIX product page links to historical values, supporting official provenance of the historical-data route.
- This is a new route to test before declaring India VIX raw acquisition blocked.

## Strict limitations
- The historical-data page's currently rendered default state contains no selected index/time period and no observations. No date query was executed in this audit.
- No POST endpoint, request body, undocumented API, or third-party reverse-engineered implementation is accepted as a source contract. Do not use an endpoint merely because it appears in third-party code.
- No CSV bytes, response metadata, row count, date range, or SHA-256 were acquired.
- CSV export is a page capability, not proof that a selected India VIX query returns data.
- This report does not establish that this route is free of access conditions beyond the public page interface; do not purchase or contact anyone.

## Controlled next test
Use the public page UI:
1. Open https://www.niftyindices.com/reports/historical-data
2. Select the index type/sub-index and explicitly select "India VIX" if offered.
3. Query a bounded interval (first test: 01-Jan-2024 through 31-Dec-2024).
4. Record the exact visible selected index and dates before submission.
5. Export CSV through the page's CSV control.
6. Preserve original bytes and retrieval metadata; calculate SHA-256 before parsing.
7. Validate headers, date parsing, uniqueness, chronological coverage, numeric OHLC, Low <= Open/Close <= High, and cross-check overlapping dates against an independent official NSE route. Do not require equality for fields not present in both sources.
8. If India VIX is not selectable or export fails, capture the exact observed UI/error and keep acquisition BLOCKED. Do not infer endpoint failure from the static page rendering.

## Acceptance state
| Gate | State |
|---|---|
| Official route identity | PASS |
| Official VIX historical-value linkage | PASS |
| UI has date/index selectors | PASS |
| CSV-format control | PASS |
| India VIX selection actually tested | NOT STARTED |
| Bounded query actually executed | NOT STARTED |
| Raw CSV acquired | NOT ACQUIRED |
| Raw SHA-256 | UNKNOWN |
| Schema/date coverage QA | NOT STARTED |
| Factor acceptance | BLOCKED |

## Project invariants
₹0 spend; free official sources only; no paid feeds/APIs or external contact; no synthetic rows/timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; no PR merge. Research-only.
