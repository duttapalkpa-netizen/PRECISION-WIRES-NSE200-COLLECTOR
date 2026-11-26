# GCR Continuation 255 — South Africa (ZAF) SARB EXCX135D daily FX Q2 coverage / historical endpoint access boundary
Date: 2026-11-26 (Asia/Kolkata)

## Decision
A distinct official SARB API route is confirmed, and its public no-date observation endpoint returns a limited visible sample of the `EXCX135D` series. The returned sample contains only three Q2 dates (1, 2 and 7 April 2026) followed by March 2026 observations; it does not provide complete Q2 coverage. The OpenAPI-documented date-bounded route for 1-Apr through 30-Jun-2026 remains inaccessible through the current web retrieval channel. The daily rate's own description is a weighted average of banks' daily rates at approximately 10:30 am, but no SARB BOP portfolio-flow conversion convention was established. Therefore no Q2 average, conversion, or revised asset residual is accepted. ZAF remains DATA_CAPTURED / PARTIAL / NOT PASS; asset REVIEW, liability PASS retained, vintage PENDING, FULL_PASS NO, aggregate NOT_AUTHORIZED.

## 1. Mandatory continuity preflight and task selection
- Re-fetched the current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and fixed 63-country Q2 matrix.
- Re-read Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md`.
- Re-opened controlling ZAF C127 methodology boundary and C215 official SARB API discovery report.
- Reused existing ZAF numeric results; did not repeat IMF retrieval, SARB PDF/table extraction, component arithmetic, OECD quarterly-average comparison or cohort rebuild.
- Selected only the unfinished C215 action: test the already documented official SARB historical observation endpoint and establish whether Q2 daily observations can be retrieved.

## 2. Official API contract and series identity
- Official OpenAPI: https://custom.resbank.co.za/SarbWebApi/swagger/v1/swagger.json
- OpenAPI documents:
  - `GET /WebIndicators/HistoricalExchangeRatesDaily` as “Gets the Historical Daily Exchange Rates”.
  - `GET /WebIndicators/Shared/GetTimeseriesObservations/{timeseriesCode}`.
  - `GET /WebIndicators/Shared/GetTimeseriesObservations/{timeseriesCode}/{startDate}/{endDate}` as a date-bounded observations endpoint.
- OpenAPI lines 987–1098 describe the two observation endpoints and their three required path parameters for the date-bounded form.
- The daily historical rates endpoint identifies `EXCX135D` as “Rand per US Dollar”.
- The series observations describe the rate as: “Weighted average of the banks' daily rates at approximately 10:30 am. Weights are based on the banks' foreign exchange transactions.”
- The observation unit is Rand per US Dollar (ZAR/USD); it is not USD per Rand.

## 3. New no-date observations endpoint test
- Exact official URL opened: https://custom.resbank.co.za/SarbWebApi/WebIndicators/Shared/GetTimeseriesObservations/EXCX135D
- The current retrieved response exposes 24 observations (visible lines 0–23), ordered newest to oldest.
- Q2-2026 observations visible in that returned sample:
  - 2026-04-07: 16.8258 ZAR/USD
  - 2026-04-02: 16.9611 ZAR/USD
  - 2026-04-01: 16.8446 ZAR/USD
- Remaining visible rows are dated 2026-03-31 through 2026-03-02. No May or June 2026 observations are present in the retrieved sample.
- This proves only that the no-date endpoint's current response as retrieved here exposes this 24-row sample. It does not prove the API's complete underlying historical database ends there, nor does it justify treating three April observations as Q2 coverage.

## 4. Date-bounded route attempt and separate snapshot endpoint
- Attempted the exact OpenAPI route with `EXCX135D/2026-04-01/2026-06-30`; the current web retrieval returned an inaccessible/internal-error response.
- A second conventional day-month-year path attempt and a percent-encoded slash date attempt also returned inaccessible/internal-error. These are retrieval-channel outcomes, not evidence that SARB's API itself is broken.
- The separate `HistoricalExchangeRatesDaily` snapshot endpoint returned a latest visible observation date of 2026-08-07 for EXCX135D, value 16.3213. This is a latest snapshot, not the required full Q2 daily history.
- The `HistoricalExchangeRatesMonthly` snapshot endpoint exposed only three selected monthly indicators and did not include EXCX135D monthly values. No monthly FX series was admitted.
- No complete Q2 response bytes, response headers, retrieval timestamp from the API, row count for the date-bounded request, raw export or SHA-256 was captured.

## 5. Methodology boundary — do not convert the SARB portfolio legs yet
- C127 documents IMF BPM6 preference for actual transaction rates; daily averages can approximate daily transaction rates; where unavailable, use the shortest applicable period. This is a general statistical principle, not a confirmed SARB-specific rule for this portfolio aggregate.
- EXCX135D is a weighted average of banks' daily rates at approximately 10:30 am. It is not shown by the retrieved metadata to be a transaction-weighted portfolio-flow conversion rate or the rate used by SARB to compile BOP portfolio flows.
- The no-date endpoint sample is incomplete for Q2. Do not calculate a quarter average from three April dates, use quarter-end FX, use OECD quarterly average as if SARB convention, or infer the correct sign/scale transformation.
- The existing C215/C127 numeric result is carried forward without recalculation: SARB liabilities -R9,023m remain prior PASS under the previously used comparator; assets -R68,769m remain REVIEW because the prior quarterly-average conversion residual was outside the strict half-R-million rounding bound. The exact residual is not recomputed here.

## 6. Acceptance table
| Gate | Status |
|---|---|
| Current Ledger / Queue / Registry / Matrix preflight | PASS |
| Library Mother File 1–53 re-read | PASS |
| Official SARB OpenAPI contract | PASS |
| EXCX135D identity and ZAR-per-USD unit | PASS |
| Daily series description / 10:30 weighted bank rate | PASS |
| No-date observations endpoint reachable | PASS — limited visible sample |
| Visible Q2 dates in sample | 3 dates (1, 2, 7 April only) |
| Complete Q2-2026 daily observation coverage | NOT_CAPTURED |
| Date-bounded Q2 endpoint response | INACCESSIBLE via current retrieval channel |
| Raw Q2 payload / headers / API retrieval UTC / SHA-256 | NOT_CAPTURED |
| Q2 daily average | NOT_CALCULATED |
| SARB BOP portfolio transaction FX convention | NOT_ESTABLISHED |
| ZAF asset reconciliation | REVIEW / NOT PASS |
| ZAF liability comparison | Existing PASS retained; not recalculated |
| ZAF vintage / full national validation | PENDING / PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 7. Exact next action and duplicate-prevention boundary
- Do not repeat the same no-date 24-row response, date-format guesses, historical daily snapshot, IMF fetch, SARB PDF extraction or OECD quarter-average arithmetic.
- Reopen only if an authorized, supported HTTP/API-capable route can retrieve the complete documented Q2 date-bounded response (or a distinct official SARB export provides full Q2 daily observations), with response headers, retrieval UTC, byte count and SHA-256.
- Then validate date coverage, duplicates, missing business days, unit direction and raw series metadata. Only after SARB's BOP-specific conversion convention is established may a daily-derived comparator be evaluated against the asset leg.
- If no full series or convention is available, keep asset REVIEW and move to another unfinished fixed-cohort task. No API account, paid service or external contact is authorized.

## 8. Protected invariants
₹0; free official sources only. No IMF re-query, no cohort rebuild, no synthetic observations, no fabricated timestamps, no unsupported FX/sign/scale transform, no tolerance widening, no net-to-leg back-solving and no aggregate promotion. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 Steps × 12 Filters), Engines A–E and IPO-PLX V2.0 remain unchanged. No merge, workflow dispatch or production integration.
