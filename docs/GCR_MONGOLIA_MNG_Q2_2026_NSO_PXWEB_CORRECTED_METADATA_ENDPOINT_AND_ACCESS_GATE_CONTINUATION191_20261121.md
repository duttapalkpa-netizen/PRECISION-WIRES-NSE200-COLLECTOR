# Mongolia (MNG) Q2-2026 — corrected NSO PxWeb metadata endpoint and access gate (Continuation 191)
Date: 2026-11-21 (Asia/Kolkata)
Decision: A CODE-LEVEL REVIEW OF THE PUBLIC MONGOLSTATS PXWEB CLIENT REVEALED THAT THE C190 METADATA URL OMITTED THE REQUIRED TABLE FILENAME SUFFIX `.px`. C191 CORRECTED THE ENDPOINT AND TESTED THE DOCUMENTED API ROUTE, BUT THE WEB RETRIEVAL BRIDGE STILL RETURNS “URL NOT ACCESSIBLE”. THE OFFICIAL TABLE NOW SHOWS INFORMATION UPDATED 09-NOV-2026 AND Q2-2026 IN ITS QUARTER DIMENSION, BUT THE INDICATOR CODEBOOK AND OBSERVATIONS REMAIN UNCAPTURED. THIS CORRECTS THE ROUTE ERROR; IT DOES NOT COMPLETE NATIONAL DUAL-LEG VALIDATION. MNG REMAINS PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity and error-correction preflight
- Re-fetched current Master Ledger, Priority Queue, Historical Registry, C179 MNG source report, C190 API-route report, C189 GIN report and immutable 63-country cohort.
- MNG remained the selected open dependency. No IMF re-query, cohort rebuild or repeated country extraction.
- C190 route correction: C190 tested a metadata URL ending in `DT_NSO_0100_001V10_quarter` without the PxWeb table filename extension. The public mongolstats client source shows that its metadata request appends the table filename (example form `DT_NSO_...px`) to the API base/path. C190's exact endpoint was therefore incomplete. This error is explicitly corrected here; C190 is not retroactively described as a successful metadata test.

## 2. Current official NSO table metadata
- Official table: https://data.1212.mn/pxweb/en/NSO/NSO__Economy%2C%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter.px/
- Current page extraction states:
  - Indicator dimension: 69 values.
  - Quarter dimension: 71 values; examples include 2026-3, 2026-2 and 2026-1.
  - Description: official BOP transaction statement includes portfolio investment and other investment flows.
  - Source: Bank of Mongolia.
  - Measurement: million USD.
  - Frequency: quarterly.
  - Information updated date: 11/9/2026 (09-Nov-2026).
- The 09-Nov date is the page's information-updated marker, not independently proven observation-level revision vintage. The page still renders zero selected cells and does not expose the 69 indicator labels in the text extraction.
- The prior C179/C190 10-Aug-2026 page marker is superseded as a current page display observation by the currently rendered 09-Nov marker; this does not prove exactly which Q2 cells changed.

## 3. Corrected documented PxWeb metadata endpoint
- The public `mongolstats` source (third-party client documentation; used only to establish request construction, not as national statistical evidence) defines API base `https://data.1212.mn/api/v1`, appends language and database, URL-escapes each path segment, and calls the table metadata resource using the actual table filename, e.g. `DT_NSO_...px`.
- Corrected endpoint tested:
  `https://data.1212.mn/api/v1/en/NSO/NSO__Economy%2C%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter.px`
- The web retrieval bridge returned “URL not accessible”. No HTTP status, headers, content type, response body, byte count or SHA-256 was provided. Do not interpret this as a confirmed server-side 4xx/5xx response.
- The exact endpoint is now syntactically aligned with the documented PxWeb client construction, but the codebook remains unavailable through this retrieval surface. No indicator codes or query payload were guessed.
- The NSO table's “More meta data information” link opens a general NSO website page without the indicator codebook; it does not substitute for the PxWeb metadata JSON.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Ledger / Queue / Registry / C179 / C190 / C189 / cohort preflight | PASS |
| Fixed MNG cohort membership | PASS (reused) |
| Official NSO BOP PxWeb table accessible | PASS |
| Current page update marker 09-Nov-2026 | PASS (page metadata only) |
| Quarterly / million USD / Bank of Mongolia source | PASS (table metadata) |
| Q2-2026 period shown in dimension examples | PASS |
| Exact 69 indicator labels and codes | NOT_CAPTURED |
| Portfolio asset and liability indicators separately identified | NOT_VERIFIED |
| Q2-2026 national asset/liability values | NOT_CAPTURED |
| Corrected API metadata JSON / raw bytes / SHA-256 | NOT_CAPTURED |
| Sign, scope and observation vintage | NOT_ESTABLISHED |
| Archived IMF exact-key numeric comparison | NOT_DONE |
| MNG full national dual-leg validation | PARTIAL / NOT PASS |
| Aggregate authorization | NOT_AUTHORIZED |

## 5. Rejected shortcuts and next action
- Do not use third-party package descriptions as national observation evidence.
- Do not guess the 69 indicator labels, indicator codes, signs or Q2 values.
- Do not repeat the corrected API URL through the same blocked web retrieval surface.
- Next: seek a genuinely different supported official export route or downloadable NSO/Bank of Mongolia Q2 BOP data file; if none is available, preserve MNG PARTIAL and advance to the next eligible cohort member after fresh preflight.
- No IMF re-query, no cohort rebuild, no paid API, no synthetic values/timestamps, no net-to-leg back-solving, no stock-as-flow, no unsupported sign/scale/FX conversion. ₹0; official/free sources only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN never PASS.
