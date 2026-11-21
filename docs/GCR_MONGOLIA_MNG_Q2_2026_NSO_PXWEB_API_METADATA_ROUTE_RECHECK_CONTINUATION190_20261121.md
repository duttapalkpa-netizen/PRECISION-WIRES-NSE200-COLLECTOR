# Mongolia (MNG) Q2-2026 — NSO PxWeb API metadata-route recheck (Continuation 190)
Date: 2026-11-21 (Asia/Kolkata)
Decision: OFFICIAL NSO PXWEB TABLE REMAINS ACCESSIBLE AND ITS METADATA CONFIRMS QUARTERLY BOP FLOW SCOPE, SOURCE BANK OF MONGOLIA, UNIT MILLION USD, AND Q2-2026 PERIOD EXAMPLE. A DIRECT REST METADATA ENDPOINT WAS TESTED USING THE DOCUMENTED PXWEB V1 ROUTE SHAPE, BUT THE RETRIEVAL BRIDGE RETURNED “URL NOT ACCESSIBLE”; NO HTTP RESPONSE, RAW JSON, INDICATOR CODEBOOK OR OBSERVATIONS CAPTURED. MNG REMAINS PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and selection
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, C189 GIN report, MNG C179 report and immutable fixed 63-country cohort.
- C189's Guinea page/link-target route is closed for repetition; MNG C179 contains a still-open, distinct actionable dependency: obtain the official PxWeb indicator codebook and Q2-2026 portfolio asset/liability observations.
- Reused the immutable cohort file without modification; exact MNG row remains both IMF legs present, national validation pending, aggregate NOT_AUTHORIZED. Cohort SHA/Git blob: `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`.
- No IMF re-query, cohort rebuild, or duplicate country-row extraction.

## 2. Official PxWeb table re-opened
- Official NSO table: https://data.1212.mn/pxweb/en/NSO/NSO__Economy%2C%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter.px/
- The official page is directly accessible and lists Indicator (69 values) and Quarter (70 values); page examples include `2026-2`.
- Table metadata states BOP summarizes transactions between residents and non-residents, including portfolio investment; compilation source is Bank of Mongolia; unit is million USD; frequency is quarterly.
- Current page shows information updated 10-Aug-2026 and next update 09-Sep-2026. Preserve this metadata timestamp as the page's stated update marker only, not as proof of a Q2 statistical vintage.
- The indicator list is not rendered in the extracted text; it shows “Select at least one value” and zero selected cells. Thus no portfolio indicator code or Q2 cell value can be claimed.

## 3. Direct API metadata route test
- Tested the PxWeb v1 metadata route shape for the exact official table:
  `https://data.1212.mn/api/v1/en/NSO/NSO__Economy%2C%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter`
- The web retrieval surface returned “URL not accessible”. It did not provide an HTTP status, response headers, content type, byte count, body or SHA-256. Do not label this as an HTTP 4xx/5xx response or claim the server itself rejected the endpoint.
- Earlier C179 container-side attempt to the API host failed DNS resolution. No successful API response has been captured by either route.
- The official table page's metadata link leads to the NSO questionnaire metadata page, which contains no machine-readable table codebook in the extracted view. It does not replace the PxWeb table metadata JSON.
- No indicator codes were guessed from BPM6 concepts or translated labels. No query body was fabricated or submitted because the dimension codebook is still unavailable.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Ledger / queue / registry / C179 / C189 / fixed cohort preflight | PASS |
| MNG immutable cohort membership | PASS (reused) |
| Official NSO quarterly BOP table accessible | PASS |
| BOP includes portfolio investment in its general scope | PASS (metadata description) |
| Source Bank of Mongolia / unit million USD / quarterly | PASS (table metadata) |
| Q2-2026 quarter dimension example | PASS (page example) |
| Exact 69 indicator labels/codes | NOT_CAPTURED |
| Portfolio asset and liability indicator identity | NOT_VERIFIED |
| Q2-2026 national asset/liability observations | NOT_CAPTURED |
| API metadata JSON / response bytes / SHA-256 | NOT_CAPTURED |
| Sign, series scope and statistical vintage | NOT_ESTABLISHED |
| Numeric comparison with archived IMF exact rows | NOT_DONE |
| MNG full national dual-leg validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 5. Rejected shortcuts and next exact action
- Do not infer that general table scope means portfolio asset and liability series are present as separate indicators.
- Do not guess dimension codes, values, signs or revisions; do not back-solve from net.
- Do not repeat the same inaccessible API URL through the same retrieval surface.
- Next: use a genuinely different supported official export mechanism or an NSO/Bank of Mongolia published data attachment to obtain the indicator list and Q2-2026 values. Preserve original request/response bytes, metadata, timestamp and SHA-256 before parsing. If no new supported route appears, retain MNG PARTIAL and advance to the next eligible cohort member after fresh preflight.
- No IMF re-query, no cohort rebuild, no paid service, no synthetic values or timestamps. ₹0; official/free sources only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN never PASS.
