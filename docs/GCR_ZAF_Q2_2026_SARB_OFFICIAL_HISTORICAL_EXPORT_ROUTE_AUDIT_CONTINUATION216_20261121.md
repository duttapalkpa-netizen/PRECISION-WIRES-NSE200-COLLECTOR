# South Africa (ZAF) Q2-2026 — SARB official historical export route audit
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 216 / Part-1
Status: OFFICIAL DAILY/MONTHLY SNAPSHOT ROUTES VERIFIED; Q2 DAILY SERIES NOT CAPTURED; ASSET FX REVIEW REMAINS OPEN.

## 1. Continuity preflight
- Re-fetched the current Master Continuity & Acceptance Ledger, GCR Master Priority Queue, Historical Task Registry and controlling C215/C215A report before selecting this continuation.
- C215 and C215A are already complete as route discovery and matrix gate-orientation correction respectively; neither was repeated.
- Existing ZAF liability PASS remains unchanged. Asset remains REVIEW because Q2 daily SARB FX observations and the applicable BOP transaction conversion convention are not established.
- No IMF re-query, cohort rebuild, matrix gate promotion, tolerance widening or production change.

## 2. Official SARB API checks
Official OpenAPI document: https://custom.resbank.co.za/SarbWebApi/swagger/v1/swagger.json
- The OpenAPI 3.0.4 contract documents `GET /WebIndicators/HistoricalExchangeRatesDaily` and the `GetTimeseriesObservations` endpoints, including the date-bounded form `/{timeseriesCode}/{startDate}/{endDate}`.
- Direct official daily endpoint tested:
  https://custom.resbank.co.za/SarbWebApi/WebIndicators/HistoricalExchangeRatesDaily
- It returned a live snapshot dated 2026-11-20. The Rand per US Dollar series is `EXCX135D`, value 17.4429. This endpoint response is a latest snapshot, not a Q2 history extract.
- Direct official monthly endpoint tested:
  https://custom.resbank.co.za/SarbWebApi/WebIndicators/HistoricalExchangeRatesMonthly
- It returned three current monthly indicators (nominal effective exchange rate, real effective rate, real prime lending rate); it did not return the daily Rand/USD observations needed for Q2. It is not a valid substitute.
- The date-bounded official time-series route for `EXCX135D`, 2026-04-01 through 2026-06-30, was attempted as documented in C215 and remained inaccessible through this retrieval surface. The unbounded `GetTimeseriesObservations/EXCX135D` route was also inaccessible. No observation rows, response headers, raw bytes, retrieval timestamp from SARB or SHA-256 were captured.
- This is a retrieval-channel limitation, not evidence that SARB does not hold the data.

## 3. Additional official publication route located
Official SARB Selected Historical Rates page:
https://www.resbank.co.za/en/home/what-we-do/statistics/key-statistics/selected-historical-rates.pdf
- The live page renders a Historical Exchange Rates section with Start Date and End Date controls, a View action, and download options labelled CSV, XML, DOC and PDF.
- The rendered page text does not expose the underlying export URL or selected series request parameters. No downloadable file locator, Q2 data rows or raw file was obtained in this continuation.
- SARB Current Market Rates page footnote states that the weighted average exchange rate of the rand is based on banks' daily rates at approximately 10:30am. This is a documented description of that weighted-average series; it does not establish that the same rate/aggregation is the BOP portfolio-transaction conversion convention. No such inference is made.

## 4. Gate disposition
| Gate | Status |
|---|---|
| C215 official OpenAPI route discovery | PASS (prior) |
| C215A ZAF matrix gate orientation | PASS (prior; preserved) |
| Official latest daily snapshot / EXCX135D identifier | PASS (latest snapshot only) |
| Official monthly endpoint inspected | PASS (not fit for daily Q2 requirement) |
| Official Selected Historical Rates date/export UI located | SOURCE_FOUND |
| Exact CSV/XML/PDF export URL and selected-series request identified | NOT_CAPTURED |
| Q2 2026 daily EXCX135D rows | NOT_CAPTURED |
| Raw Q2 response/file bytes and SHA-256 | NOT_CAPTURED |
| Complete date/duplicate/missing-day QA | NOT_DONE |
| SARB BOP transaction FX conversion convention | NOT_ESTABLISHED |
| ZAF asset reconciliation | REVIEW / NOT PASS |
| ZAF liability reconciliation | Existing PASS retained |
| ZAF full country validation / aggregate admission | PARTIAL / NOT PASS; NOT_AUTHORIZED |

## 5. Next exact action
1. Inspect the official Selected Historical Rates page's client-side request/export contract (the date controls and CSV/XML/PDF actions) to identify the exact SARB-owned export request for `EXCX135D`; do not guess query names or hidden URLs.
2. Request only 2026-04-01 through 2026-06-30; preserve the exact response bytes, response headers, UTC retrieval timestamp and SHA-256.
3. Validate the actual returned observation dates, duplicates, gaps, units and coverage before computing any mean.
4. Separately establish whether SARB's BOP transaction compilation uses a daily 10:30 weighted-average rate, another daily rate, or a different quarterly conversion method. Do not treat the Current Market Rates footnote as sufficient proof.
5. Only after both source capture and methodology are established, calculate a diagnostic quarterly rate and reconcile ZAF assets against the existing IMF A_NFA_T row. Preserve the liability PASS and all existing gates.

## 6. Protected invariants
₹0; free official sources only. No paid API, third-party proxy as evidence, synthetic data, fabricated timestamps, IMF re-query, cohort rebuild, sign/scale assumptions, tolerance widening or aggregate promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## 7. Official source references
- SARB OpenAPI: https://custom.resbank.co.za/SarbWebApi/swagger/v1/swagger.json
- SARB daily rates endpoint: https://custom.resbank.co.za/SarbWebApi/WebIndicators/HistoricalExchangeRatesDaily
- SARB monthly rates endpoint: https://custom.resbank.co.za/SarbWebApi/WebIndicators/HistoricalExchangeRatesMonthly
- SARB Selected Historical Rates page: https://www.resbank.co.za/en/home/what-we-do/statistics/key-statistics/selected-historical-rates.pdf
- SARB Current Market Rates page: https://www.resbank.co.za/en/home/what-we-do/statistics/key-statistics/current-market-rates
- Controlling prior report: docs/GCR_ZAF_Q2_2026_SARB_OFFICIAL_DAILY_FX_API_ROUTE_DISCOVERY_CONTINUATION215_20261121.md
