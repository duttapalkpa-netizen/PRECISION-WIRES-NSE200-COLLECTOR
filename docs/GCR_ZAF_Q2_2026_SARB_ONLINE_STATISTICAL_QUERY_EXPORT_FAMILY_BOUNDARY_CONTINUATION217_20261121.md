# South Africa (ZAF) Q2-2026 — SARB alternate official export-family boundary audit
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 217 / Research Verification 52 Part-2
Status: OFFICIAL ONLINE STATISTICAL QUERY EXPORT WORKFLOW VERIFIED; NOT AN EXCX135D DAILY-FX SUBSTITUTE; Q2 DAILY FX STILL NOT CAPTURED.

## 1. Mandatory continuity preflight
- Re-fetched current Master Continuity & Acceptance Ledger; blob SHA-1: 29b21b8e602c7effc1991fb6d65e2a7dc43eb361.
- Re-fetched GCR Master Priority Queue; blob SHA-1: a45177a8fab8c7b3d6fe92eacc3662fecd8fad90.
- Re-fetched Historical Task Registry; blob SHA-1: 4abfab65396b4b4a8ccdb41158c4b8082fd5ec93.
- Re-fetched controlling ZAF C215/C215A/C216 record. Existing liability PASS, asset REVIEW, vintage PENDING, FULL_PASS NO and aggregate NOT_AUTHORIZED are preserved.
- Excluded completed C215 route discovery, C215A matrix correction and C216 Selected Historical Rates UI discovery; no repeated API route attempts or matrix gate promotion.

## 2. New official SARB route family verified
Official page: https://www.resbank.co.za/en/home/what-we-do/statistics/releases/online-statistical-query
The live SARB page states that the Online Statistical Query facility selects and downloads Quarterly Bulletin time series, as one series or multiple series as a dataset. The documented sequence is:
1. Select a series by KBP code or keyword (wildcard supported; KBP prefix automatically added).
2. Select a matching time series and an available version.
3. Select a time-series version.
4. Select display frequency and observation range, including start and end date.
5. View results and export Excel, CSV, PDF or DOC.
The page also documents a 29-Sep-2026 change to KBP1 Week 5 date formatting, replacing week-based labels with exact calendar dates.

## 3. Scope boundary — no false substitution
- C215/C216 target is the SARB daily FX series EXCX135D (Rand per US Dollar), Q2 2026 daily observations.
- The Online Statistical Query page explicitly describes a KBP-prefixed Quarterly Bulletin time-series workflow. The inspected page does not establish that EXCX135D is a valid KBP code, that this query facility exposes the daily FX series, or that its export contains the required daily observations.
- Therefore this route is a distinct official export family and a possible research lead, not an established retrieval route for EXCX135D.
- No KBP code was guessed, no export URL was invented, and no KBP data was relabelled as daily FX.
- The date-bounded SARB API route remains inaccessible through the current retrieval surface; this is not evidence that SARB does not hold the data.

## 4. Acceptance disposition
| Gate | Status |
|---|---|
| Current ledger/queue/registry preflight | PASS |
| Official Online Statistical Query page located | PASS |
| KBP code/version/date-range/export workflow documented | PASS |
| Online Statistical Query proven to expose EXCX135D | NOT_ESTABLISHED |
| Exact CSV/Excel request for EXCX135D | NOT_CAPTURED |
| Q2 2026 daily EXCX135D rows | NOT_CAPTURED |
| Raw payload/headers/retrieval UTC/SHA-256 | NOT_CAPTURED |
| Date/duplicate/gap QA | NOT_DONE |
| SARB BOP portfolio-transaction FX convention | NOT_ESTABLISHED |
| ZAF asset reconciliation | REVIEW / NOT PASS |
| ZAF liability reconciliation | Existing PASS retained |
| ZAF full country validation / aggregate admission | PARTIAL / NOT PASS; NOT_AUTHORIZED |

## 5. Next exact action (C218)
1. Inspect SARB's official Online Statistical Query KBP code search/version results only to determine whether a documented KBP daily USD/ZAR series exists; do not assume it maps to EXCX135D.
2. In parallel, inspect the SARB Selected Historical Rates page's actual client-side export contract through an HTTP-capable route, but do not guess hidden request names.
3. Only if an exact official series and export request are proven, retrieve 2026-04-01 through 2026-06-30 and preserve raw bytes, response headers, UTC retrieval timestamp and SHA-256.
4. Validate returned dates, duplicates, missing observations, units and coverage.
5. Independently establish SARB's BOP transaction conversion convention before using any quarterly mean for the ZAF asset leg.

## 6. Protected invariants
₹0; free official sources only. No IMF re-query, cohort rebuild, synthetic data, fabricated timestamps, guessed series codes, unapproved FX/sign/scale transforms, tolerance widening or aggregate promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## 7. Official source references
- SARB Online Statistical Query: https://www.resbank.co.za/en/home/what-we-do/statistics/releases/online-statistical-query
- SARB Selected Historical Rates: https://www.resbank.co.za/en/home/what-we-do/statistics/key-statistics/selected-historical-rates
- SARB OpenAPI: https://custom.resbank.co.za/SarbWebApi/swagger/v1/swagger.json
- Controlling C216 report: docs/GCR_ZAF_Q2_2026_SARB_OFFICIAL_HISTORICAL_EXPORT_ROUTE_AUDIT_CONTINUATION216_20261121.md