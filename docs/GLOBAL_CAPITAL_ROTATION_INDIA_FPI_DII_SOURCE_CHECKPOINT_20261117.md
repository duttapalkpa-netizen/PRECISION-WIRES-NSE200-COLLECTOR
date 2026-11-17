# Global Capital Rotation — India FPI/DII Source Checkpoint
Date: 2026-11-17 (Asia/Kolkata)
Branch: research/global-capital-rotation-overlay-v1
Scope: bounded official-page verification; not full overlay acceptance.

## Fresh CDSL daily page observation
Official URL: https://www.cdslindia.com/eservices/publications/fiidaily
Page heading: Daily Trends in FII/FPI Investments on 17-NOV-2026
Reporting date: 17-NOV-2026
The page states that figures are compiled from custodian reports submitted to depositories on 17-Nov and represent trades conducted on and up to previous trading day(s). Reporting date is not an intraday execution timestamp.

Displayed net investment (INR crore):
- Equity subtotal: +5,107.61
- Debt-General subtotal: +137.23
- Debt-VRR subtotal: -2,379.67
- Debt-FAR subtotal: -424.29
- Hybrid subtotal: -4.74
- FPI category subtotal (sum above): +2,436.14
- Mutual Funds subtotal, separately displayed: +37.68
- CDSL page Total: +2,473.82

Arithmetic: 5,107.61 + 137.23 - 2,379.67 - 424.29 - 4.74 = 2,436.14. Adding separately displayed MF +37.68 gives page Total +2,473.82. Therefore page Total is not pure FPI.

## NSE source route observation
Official URL: https://www.nseindia.com/reports/fii-dii (redirected to https://www.nseindia.in/reports/fii-dii)
The page exposes two distinct CSV download controls:
1. FII/FPI & DII trading activity on NSE in Capital Market Segment.
2. FII/FPI & DII trading activity on NSE, BSE and MSEI in Capital Market Segment.
The page text alone does not expose the underlying download URLs or raw CSV bytes in this checkpoint. Do not infer or invent an endpoint. Keep these two scopes separate.

## Evidence boundary
- CDSL displayed-page observation and arithmetic: PASS (bounded source-display check).
- CDSL raw response bytes, byte count, retrieval timestamped immutable archive and SHA-256: NOT_DONE.
- NSE-only CSV raw bytes, exact download URL, byte count and SHA-256: NOT_DONE.
- Combined NSE+BSE+MSEI CSV raw bytes, exact download URL, byte count and SHA-256: NOT_DONE.
- Matched lag-aware FPI/DII panel, duplicate/calendar/schema QA: NOT_DONE.
- Global EM flow, synchronized relative-return study, sector-to-stock transmission and matured predictive validation: remain UNKNOWN / NOT_DONE as per continuity ledger.

## Next bounded actions
1. Obtain the two NSE CSVs through the official browser download controls; record exact final URLs, retrieval timestamp, byte length and SHA-256. Do not substitute guessed API endpoints.
2. Capture CDSL daily/archive raw bytes with exact URL, retrieval timestamp, byte length and SHA-256.
3. Parse each source independently; validate headers, categories, sign convention, duplicate dates, arithmetic, missingness and session alignment.
4. Build a matched date panel only after raw evidence passes; preserve CDSL custodian-reported lag and NSE provisional/exchange-scope semantics.
5. Then proceed to IMF BOP actual transaction extraction and synchronized global-vs-India relative-attraction validation.

## Protected invariants
No change to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E or Hard Gate. Research-only; no composite stock score, ranking, buy/sell instruction, automatic trigger, PR merge or production integration. ₹0 spend; official/free sources only. Missing/stale values remain UNKNOWN; no forward-fill or synthetic observations.

## Sources
- CDSL daily: https://www.cdslindia.com/eservices/publications/fiidaily
- CDSL archive: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
- NSE FII/DII: https://www.nseindia.com/reports/fii-dii
- SEBI FPI directory: https://www.sebi.gov.in/curation/fpi.html
