# Mongolia (MNG) Q2-2026 — official Open Data API documentation and table-route boundary
Date: 2026-11-25 (Asia/Kolkata)
Continuation: 234 / Research Verification 57
Decision: **A genuinely new official NSO Open Data documentation page now supplies a GET API route example, table metadata response fields and JSON/XML formats. This advances the API-contract evidence beyond C221, but the exact MNG table-specific API path has not been successfully retrieved and no indicator codebook or Q2 portfolio asset/liability observations were captured. MNG remains BLOCKED / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Mandatory continuity preflight and task selection
Re-fetched before selecting work:
- Current Master Continuity Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, blob SHA `61eba479d20bb0593fc58e1f0bac59242936354a`.
- Current GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, blob SHA `3e4a34e34821aa4344a86cad04221679a6970144`.
- Current 63-country Historical Task Registry: `docs/GCR_Q2_2026_HISTORICAL_TASK_REGISTRY_AND_DUPLICATE_PREVENTION_GATE_20261121.md`, blob SHA `553a7eadb71e2827bfc8b629fc9dd7921c0dadef`.
- Current fixed-cohort MNG matrix row and MNG C179/C190/C221/C222 history reviewed. C233 Serbia route-boundary handoff was checked; the known NBS July PDF route remains blocked and was not retried.
- Existing MNG work reused: C179 table/source gate; C190 failed metadata route boundary; C221 official terms/API availability boundary; C222 matrix evidence-reference correction. No repeated IMF retrieval, cohort rebuild, table scrape, or repeated prior endpoint test.

## 2. New official NSO Open Data API documentation
Official English NSO Open Data page:
https://www.1212.mn/en/data-base/open-data

It explicitly documents:
- API request method: GET.
- Example route: `https://data.1212.mn/api/v1/mn/NSO/Population, household/1_Population, household/DT_NSO_0300_003V1.px`.
- Table metadata output fields: `title`, `variables[]`, and for each variable `code`, `text`, `values[]`, `valueTexts[]`.
- Supported response formats: `application/json` / `text/json` and `application/xml` / `text/xml`.
This is official NSO documentation, not a third-party PxWeb-client assumption.

Official NSO terms:
https://www.nso.mn/en/terms_of_use
- Open data available through API; JSON/XML access.
- Maximum one request per second per IP; maximum 100,000 responses per request.
- CC BY 4.0 attribution conditions; no rate-limit bypass.

## 3. MNG table mapping and exact remaining boundary
Official MNG PxWeb table:
https://data.1212.mn/pxweb/en/NSO/NSO__Economy%2C%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter.px/

Re-opened official page confirms:
- Table title: BALANCE OF PAYMENTS, by quarter by Indicator and Quarter.
- Indicator dimension: 69 values.
- Quarter dimension: 71 values; visible examples include 2026-3, 2026-2, 2026-1.
- Table description includes portfolio investment in the general BOP scope.
- Measurement: million USD; frequency: quarterly; source: Bank of Mongolia.
- Information updated date shown: 11/9/2026. This is a page metadata marker, not proof of observation vintage.

The official API example plus the official table hierarchy now allows a candidate MNG metadata route to be mapped for a future GET test, but the MNG-specific API route has not been returned successfully. The current web retrieval surface marked the candidate URL inaccessible and returned no HTTP status, response headers, JSON/XML body, byte count or digest. No API query was submitted and no route success is claimed.

## 4. Gate matrix
| Gate | Status |
|---|---|
| Fixed 63-country cohort membership | PASS (reused; unchanged) |
| Official NSO API availability and permitted use | PASS (C221 reused) |
| Official GET API route example and table-metadata response schema | PASS (new official Open Data page) |
| Official JSON/XML response formats | PASS |
| Official rate-limit and CC BY 4.0 terms | PASS |
| Official MNG quarterly BOP table / unit / source / Q2 period label | PASS (reused C221; page reopened) |
| MNG table-specific API metadata response | NOT_CAPTURED |
| 69 indicator labels/codes from API metadata | NOT_CAPTURED |
| Portfolio asset and liability indicator identity | NOT_VERIFIED |
| Q2-2026 national portfolio A/L observations | NOT_CAPTURED |
| API response bytes / SHA-256 | NOT_CAPTURED |
| Sign, scope and vintage bridge | NOT_ESTABLISHED |
| IMF exact-key numeric comparison | NOT_DONE |
| MNG national validation | BLOCKED / PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 5. Decision and next exact action
1. The API documentation discovery is accepted as a source-contract improvement only.
2. Do not claim the table-specific route succeeded. Do not invent indicator codes or submit a PxWeb query without the actual metadata codebook.
3. Next executable action requires a supported GET-capable browser/client to retrieve the exact MNG table metadata using the official NSO-documented route pattern; preserve request URL, timestamp, status/headers, raw bytes and SHA-256.
4. From returned metadata, identify portfolio asset and liability indicator codes by their actual labels, then request only Q2-2026 cells using the documented table API contract. Keep the API rate at no more than one request/second/IP.
5. If the exact endpoint remains inaccessible, retain MNG BLOCKED and move to another eligible cohort member only after fresh route-history preflight.

## 6. Protected invariants
₹0; official/free sources only; no IMF re-query or cohort rebuild; no guessed indicator codes, fabricated timestamps, synthetic values, net-to-leg back-solving, annual/H1 allocation, IIP stock substitution, unsupported sign/scale/FX conversion, rate-limit bypass, or aggregate promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. UNKNOWN is never PASS.
