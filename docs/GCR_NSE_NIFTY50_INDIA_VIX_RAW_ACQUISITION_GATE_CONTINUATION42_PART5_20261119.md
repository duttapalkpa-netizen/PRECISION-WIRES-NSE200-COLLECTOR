# GCR — NSE NIFTY 50 + India VIX Raw Acquisition Gate (Continuation 42, Part-5)
Date: 2026-11-19
Stage: OBSERVATION ONLY
Decision: SOURCE ROUTE VERIFIED; RAW ACQUISITION NOT DONE; DATASET NOT ACCEPTED.

## 1. Purpose
This gate checks official NSE/NSE Indices retrieval paths and repository collector coverage so that security bhavcopy is not mistaken for index history.

## 2. Official route evidence
### NIFTY historical index
- Official NSE Indices page: https://www.niftyindices.com/reports/historical-data
- Page exposes Historical Index Data, index selection, date range, Submit and CSV-format output.
- NIFTY 50 is selectable. NSE Indices FAQ states NIFTY 50 historical data is available from 03-Jul-1990 and distinguishes NIFTY price index from NIFTY-TR.
- The server-rendered response in this inspection showed no selected index/date-range output and “No Data Found”; no raw export was acquired.

### India VIX
- Official NSE page: https://www.nseindia.in/reports-indices-historical-vix
- Page exposes 1D/1W/1M/3M/6M/1Y/Custom date presets and a Download CSV control.
- Current server-rendered page did not expose selected-date data; search rendering showed “No Records”.
- NSE describes India VIX as expected volatility over the next 30 calendar days derived from NIFTY option best bid/ask prices. It is not interchangeable with CBOE VIX.

### NSE archives
- Official historical reports directory: https://www.nseindia.in/static/resources/historical-reports-capital-market-daily-monthly-archives
- It lists separate Historical Index Data, Historical Data - India Vix, and Archives of Daily/Monthly Reports (Indices).
- Official all-reports page: https://www.nseindia.in/all-reports
- It lists daily CM reports including UDiFF Common Bhavcopy Final ZIP and security-wise delivery positions. These are security-level files, not substitutes for NIFTY index OHLC or India VIX.

## 3. Repository code boundary inspected
- Existing collector/nse_download.py downloads/normalizes NSE security-level CM UDiFF bhavcopy (and legacy security-wise bhavdata fallback). Its output is security-level SYMBOL/SERIES/ISIN/DATE/OHLC/volume/turnover/delivery.
- It does not implement NIFTY 50 index-history or India VIX historical CSV retrieval.
- Existing .github/workflows/nse_collector.yml runs a broad 200-session collector, dataset builder, QA, walk-forward and engines, with a 60-minute timeout. It is not appropriate to trigger just to fetch two index series.
- No new script/workflow was created because exact official request schema/download contract has not been directly verified. Do not copy undocumented third-party endpoint patterns into production.

## 4. Acceptance criteria for future raw capture
1. Use official page UI and explicit date range; record index name and price-index vs TRI choice.
2. Preserve original downloaded CSV bytes unchanged.
3. Record canonical page URL, resolved download URL, retrieval UTC timestamp, HTTP status/content type if available, byte count and SHA-256.
4. Parse a separate normalized copy; retain original column names and schema/version metadata.
5. Validate date parse, unique trading dates, ascending chronology, numeric OHLC, positive close, OHLC bounds and selected date-range boundaries.
6. Compare overlap against a second official route/export where possible; never compare price index to TRI.
7. Report actual row count, first/last dates, missing sessions against official NSE holiday calendar, duplicate count and exclusions.
8. Keep India VIX in published units; do not rescale or substitute CBOE VIX.
9. No forward-fill over holidays or missing sessions.

## 5. Current status
| Item | Status |
|---|---|
| Official NIFTY historical route | VERIFIED |
| NIFTY 50 selectable / historical depth described | VERIFIED as page documentation |
| NIFTY selected-range raw CSV acquired | NOT_DONE |
| NIFTY raw byte count / SHA-256 | UNKNOWN |
| Official India VIX historical route | VERIFIED |
| India VIX selected-range raw CSV acquired | NOT_DONE |
| India VIX raw byte count / SHA-256 | UNKNOWN |
| Repository NSE security bhavcopy collector | INSPECTED; not index/VIX collector |
| GCR event-study outcome dataset | NOT_ACCEPTED |

## 6. Sources
- NSE Indices Historical Data: https://www.niftyindices.com/reports/historical-data
- NSE Indices FAQ: https://www.niftyindices.com/static/products-services/indices-faqs
- NSE India Historical Data - India VIX: https://www.nseindia.in/reports-indices-historical-vix
- NSE Historical Reports: https://www.nseindia.in/static/resources/historical-reports-capital-market-daily-monthly-archives
- NSE All Reports: https://www.nseindia.in/all-reports
- Repository collector inspected: collector/nse_download.py and .github/workflows/nse_collector.yml

## 7. Stage and invariants
This gate closes the source-route/code-boundary review only. Observation overall remains OPEN. Planning and Organizing NOT STARTED. GCR NOT COMPLETE; aggregate/production admission NOT AUTHORIZED.
₹0; official/free sources only; no sample-data substitution, fabricated timestamps, guessed endpoints, synthetic values, forward-fill or interpolation. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
