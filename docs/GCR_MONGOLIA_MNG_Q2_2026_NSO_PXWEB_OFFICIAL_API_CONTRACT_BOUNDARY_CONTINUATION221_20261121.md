# Mongolia (MNG) Q2-2026 — NSO PxWeb official API contract boundary and no-guess decision
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 221 / Research Verification 53
Decision: OFFICIAL NSO TERMS CONFIRM OPEN-DATA API AVAILABILITY, JSON/XML FORMATS, CC BY 4.0 AND RATE LIMIT; OFFICIAL PAGE DOES NOT SPECIFY API BASE PATH, HTTP METHOD, TABLE-QUERY SCHEMA OR DIMENSION KEYS. PRIOR API BRIDGE FAILURE NOT REPEATED. NO NATIONAL OBSERVATIONS CAPTURED; MNG PARTIAL / NOT PASS.

## 1. Continuity preflight and duplicate prevention
- Re-fetched Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, MNG C179 source/API gate and MNE C220 alternate-host boundary.
- MNE C220 alternate PDF rendering is complete; its table export URL and national legs remain unresolved. No repeat of CBCG route.
- MNG C179 already attempted the documented `https://data.1212.mn/api/v1` route; web retrieval returned inaccessible and container DNS resolution failed. That exact endpoint attempt was not repeated.
- Selected a narrow new task: inspect the current official NSO Terms of Use and live official table page to determine whether they expose enough authoritative API contract detail to make a compliant, exact query without guessing.

## 2. New official evidence
- Current official NSO Terms of Use: https://www.nso.mn/en/terms_of_use
- The terms explicitly state that OPEN DATA is available through the API and that the integrated statistical database can be accessed in JSON and XML formats.
- The terms impose a maximum rate of one request per second per IP address and up to 100,000 responses per request; API rate-limit bypass is prohibited.
- Open data is licensed CC BY 4.0 with attribution; the terms say to cite the National Statistical Committee/NSO source.
- Live official PxWeb table: https://data.1212.mn/pxweb/en/NSO/NSO__Economy,%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter.px/
- Live page confirms 69 Indicator values, 71 Quarter values, `2026-2` among the period values, unit million USD, quarterly frequency, source Bank of Mongolia, and that the table represents BOP transactions including portfolio investment.
- The current live page's information-updated date is 11/9/2026, differing from C179's captured 10-Aug-2026 page state. Preserve as a new page snapshot only; it does not resolve national observation vintage.

## 3. API-contract boundary — no unsupported query
- The official terms confirm API existence, supported output formats and rate limits, but do not specify the API root, table metadata URL pattern, request method, request body schema, JSON-stat2 support, or exact dimension keys.
- The live PxWeb table page exposes no API documentation link or query contract in its rendered page text. It identifies variable names but the 69 indicator value labels and their codes are not exposed in the current text extraction.
- Public third-party client documentation describes possible API paths and POST JSON-stat2 workflows, but it is not an official NSO technical contract. It is insufficient authority to claim an exact official request or to invent an API query for this audit.
- C179's previous API base attempt failed at the retrieval bridge; retrying that same route would be duplicate work. No alternative official API endpoint was established.
- Therefore no API request was sent in this continuation. No response bytes, headers, HTTP status, retrieval timestamp or SHA-256 are claimed.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Fixed MNG 63-country cohort membership | PASS (reused C179) |
| Official NSO API availability | PASS |
| Official JSON/XML formats | PASS |
| Official API rate-limit/licensing terms | PASS |
| Official API root/path and HTTP method | NOT_DOCUMENTED_IN_INSPECTED_OFFICIAL_SOURCE |
| Official metadata/query request schema | NOT_DOCUMENTED_IN_INSPECTED_OFFICIAL_SOURCE |
| Indicator codebook / 69 indicator labels | NOT_CAPTURED |
| Separate portfolio asset/liability indicator rows | NOT_VERIFIED |
| Q2-2026 national portfolio asset/liability values | NOT_CAPTURED |
| API response bytes / SHA-256 | NOT_CAPTURED |
| National sign/scope/vintage bridge | NOT_ESTABLISHED |
| IMF exact-key comparison | NOT_DONE |
| MNG national validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 5. Decision and next action
- Close this official-contract inspection: it proves API availability and usage constraints, not a callable exact endpoint. Do not guess paths, methods, dimension codes, or query JSON based on third-party clients.
- Reopen MNG only when an official NSO API manual/OpenAPI document or a successful browser-export/network contract provides exact base URL, endpoint path, method, dimension keys and response format; alternatively, obtain the official NSO/Bank of Mongolia Q2 export.
- If that evidence is unavailable, preserve MNG PARTIAL / NOT PASS and advance to the next eligible fixed-cohort member after checking its exact prior reports and the queue. No IMF re-query or cohort rebuild.

## 6. Protected invariants
₹0; official/free sources only. No synthetic values/timestamps, guessed API paths or indicator codes, net-to-leg back-solving, annual/H1 allocation, stock-as-flow, unsupported sign/scale/FX conversion, duplicate IMF request, cohort rebuild, tolerance widening or aggregate promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## 7. Official sources
- NSO Terms of Use: https://www.nso.mn/en/terms_of_use
- Official NSO PxWeb BOP table: https://data.1212.mn/pxweb/en/NSO/NSO__Economy,%20environment__Balance%20of%20Payments/DT_NSO_0100_001V10_quarter.px/
- Prior MNG gate: docs/GCR_MONGOLIA_MNG_Q2_2026_NSO_PXWEB_BOP_QUARTERLY_SOURCE_AND_API_GATE_CONTINUATION179_20261121.md