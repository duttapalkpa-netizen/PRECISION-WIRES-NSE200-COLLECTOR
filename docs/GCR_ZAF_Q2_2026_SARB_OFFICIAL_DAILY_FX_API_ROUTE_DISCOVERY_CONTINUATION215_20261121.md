# South Africa (ZAF) Q2-2026 — SARB official daily FX API route discovery
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 215
Status: NEW OFFICIAL API ROUTE IDENTIFIED; HISTORICAL Q2 OBSERVATIONS NOT_CAPTURED; ASSET FX RECONCILIATION REMAINS REVIEW / NOT PASS.

## 1. Continuity preflight and selection
- Re-fetched the Master Continuity & Acceptance Ledger, GCR Master Priority Queue, Historical Task Registry and 63-country national validation matrix before selection.
- Re-opened the controlling ZAF Q2 reconciliation and C127 FX-methodology boundary report.
- Existing status: SARB portfolio liabilities -R9,023m reconcile to archived IMF L_NIL_T within the previously documented rounding bound; portfolio assets -R68,769m remain REVIEW because the earlier OECD quarterly-average conversion leaves an asset residual outside the strict rounding bound. Do not widen tolerance or infer a sign/FX convention.
- Selected a distinct official-source route: SARB's own documented API exposes a historical daily exchange-rate endpoint and a date-bounded time-series observations endpoint. This route was not the previously used OECD/FRED quarterly-average comparator.

## 2. Official SARB API contract discovered
- Official Swagger/OpenAPI document: https://custom.resbank.co.za/SarbWebApi/swagger/v1/swagger.json
- Official API base: https://custom.resbank.co.za/SarbWebApi
- OpenAPI title/version: SarbWebApi v1; OpenAPI 3.0.4.
- Endpoint `GET /WebIndicators/HistoricalExchangeRatesDaily` is explicitly described as “Gets the Historical Daily Exchange Rates”.
- The live endpoint returned a current daily snapshot dated 2026-11-20 and includes:
  - Name: “Rand per US Dollar”
  - TimeseriesCode: `EXCX135D`
  - Value: 17.4429
  - Date: 2026-11-20
- The same OpenAPI document explicitly defines:
  - `GET /WebIndicators/Shared/GetTimeseriesObservations/{timeseriesCode}`
  - `GET /WebIndicators/Shared/GetTimeseriesObservations/{timeseriesCode}/{startDate}/{endDate}`
  - Both return arrays of Observation objects; the date-bounded endpoint accepts a series code and explicit start/end date path parameters.
- Thus, the official API contract exposes a plausible direct historical route for SARB's own ZAR-per-USD series. The live latest-date snapshot confirms the series identifier and unit direction; it does not itself prove the Q2 historical payload or the conversion convention used for BOP transactions.

## 3. Bounded retrieval attempt and evidence boundary
- Attempted the documented date-bounded route for the SARB Rand-per-US-dollar series:
  `https://custom.resbank.co.za/SarbWebApi/WebIndicators/Shared/GetTimeseriesObservations/EXCX135D/2026-04-01/2026-06-30`
- The current web retrieval channel returned an inaccessible/internal-error response for this historical URL. No Q2 observations, row count, raw payload bytes, response headers, retrieval timestamp from the API, or SHA-256 were captured.
- Do not represent the endpoint as broken or the data as unavailable at SARB; the observed limitation is the current retrieval channel. The official API contract and latest daily snapshot are confirmed; historical Q2 payload remains unverified.
- No alternate guessed route, query-string parameter, undocumented endpoint or fabricated data was used.

## 4. Updated acceptance
| Gate | Status |
|---|---|
| Existing fixed 63-country Q2 cohort / archived IMF rows | PASS (reused) |
| SARB official OpenAPI contract retrieved | PASS |
| Official daily historical FX endpoint identified | PASS |
| Official ZAR-per-USD series code EXCX135D confirmed in latest snapshot | PASS |
| Latest daily API observation date 2026-11-20 and value 17.4429 | PASS (latest snapshot only) |
| Date-bounded historical observation endpoint documented | PASS |
| Q2-2026 daily FX observations captured | NOT_CAPTURED |
| Q2 historical raw payload / SHA-256 / response metadata | NOT_CAPTURED |
| Exact Q2 average calculation and day-count policy | NOT_DONE |
| SARB BOP transaction conversion convention established | NOT_ESTABLISHED |
| ZAF asset residual resolution | REVIEW / NOT PASS |
| ZAF liability residual | Existing PASS retained; not recalculated |
| ZAF full national validation / aggregate admission | PARTIAL / NOT PASS; NOT_AUTHORIZED |

## 5. Next exact action
1. Retrieve the date-bounded endpoint through a supported HTTP/API-capable browser or a local reproducible fetch from the official SARB host, preserving the exact response bytes, headers, retrieval UTC and SHA-256.
2. Validate all returned dates from 2026-04-01 through 2026-06-30, missing/duplicate observations, unit direction and daily coverage; do not assume weekends/holidays should have observations.
3. Compute a transparent daily mean only as a diagnostic unless SARB's BOP transaction conversion convention confirms that this is the correct quarter aggregation. Compare the daily-derived diagnostic to the previously used OECD quarterly average, but do not substitute it automatically.
4. Reconcile the exact asset leg separately against IMF A_NFA_T. Keep the existing liability PASS unchanged unless a separate reason emerges.
5. If the official BOP FX convention or historical API payload cannot be established, retain REVIEW / NOT PASS and do not widen the rounding bound.

## 6. Protected invariants
₹0; free official sources only. No IMF re-query, cohort rebuild, synthetic observations, fabricated timestamps, unapproved FX/sign/scale transforms, tolerance widening or aggregate promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## 7. Official source references
- SARB OpenAPI/Swagger: https://custom.resbank.co.za/SarbWebApi/swagger/v1/swagger.json
- SARB latest daily FX endpoint: https://custom.resbank.co.za/SarbWebApi/WebIndicators/HistoricalExchangeRatesDaily
- SARB selected historical rates page: https://www.resbank.co.za/en/home/what-we-do/statistics/key-statistics/selected-historical-rates.pdf
- SARB September 2026 Quarterly Bulletin XLSX download information: https://www.resbank.co.za/en/home/publications/publication-detail-pages/quarterly-bulletins/download-information-from-xlsx-data-files/2026/-download-information-from-xlsx-data-files
- Earlier controlling ZAF reports: `docs/GCR_ZAF_Q2_2026_IMF_SARB_OECD_FX_RECONCILIATION_20261120.md` and `docs/GCR_ZAF_Q2_2026_FX_CONVERSION_METHODOLOGY_BOUNDARY_CONTINUATION127_20261121.md`.


## Continuation 215A — ZAF matrix gate-orientation defect corrected (2026-11-21)
- Independent post-write read-back exposed a pre-existing matrix inconsistency: the controlling ZAF report states asset residual REVIEW and liability comparison PASS, while the matrix had asset_gate=PASS and liability_gate=REVIEW. This was a status inversion, not a research conclusion.
- Corrected ZAF only: asset_gate REVIEW; liability_gate PASS; status_ASSET_PASS NO; status_LIABILITY_PASS YES; asset_status DATA_CAPTURED; liability_status LIABILITY_PASS. Preserved DATA_CAPTURED stage, vintage PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED.
- Matrix correction commit `86dfe96ae4b3a71a78a0eebbabd4fd36bd4ac4e3`; blob SHA-1 `a4ed9fcf8732dd81a1d1563aaf5388ed6c2bbd0a`.
- This correction is grounded in the controlling ZAF reconciliation and C127 boundary report; it does not claim the new SARB API historical payload was captured or the asset FX issue resolved. It prevents a false asset PASS and restores the correct liability PASS.
