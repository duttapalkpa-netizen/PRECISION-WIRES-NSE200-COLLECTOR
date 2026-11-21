# GCR — Official interactive-portal execution capability gate (Continuation 198)
Date: 2026-11-21 (Asia/Kolkata)

## Decision
**PROCESS-GATE PASS; interactive source execution NOT_AVAILABLE in this session; no country data was retrieved or promoted.** The current execution surface exposes static web retrieval and repository operations but no JS-capable interactive browser / Computer Use action. Therefore the BNR ROU route discovered in C197 cannot honestly be executed here. ROU remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED. This continuation records a reusable execution boundary and anti-repeat rule; it does not claim country-validation progress.

## 1. Mandatory continuity preflight
- Re-fetched the current Master Continuity & Acceptance Ledger, GCR Master Priority Queue, Historical Task Registry, and full Romania C95/C96 reports plus C197 before selecting this process task.
- Current pre-task blob SHAs:
  - Ledger: `94185abcaa762f9fd016e52e564338b216272b8f`
  - Priority Queue: `bc260d6b849550da408dd085089337ccdbe35cb3`
  - Historical Registry: `e9e25a4d25771aee68205ba4d8418312d150bfbf`
  - ROU C95: `37f744511aeab33539d1fca15be0bce08536cd90`
  - ROU C96: `6f3c046255ada664589286bdae276606588cc9a4`
  - ROU C197: `7de47ac518dc565f7734f50f3c27af52cd38e89a`
- Reused the immutable 63-country Q2-2026 cohort and already archived IMF rows; no cohort rebuild, no IMF GET, no national value re-extraction.
- Rejected duplicate work: ECB ROU SDW/API URLs in C95/C96 remain closed; C197's BNR locator was a new route-discovery PASS only, not an export.

## 2. Evidence for interactive execution boundary
### Romania — BNR
- C197 official route: https://www.bnr.ro/en/2550-interactive-database
- Official IMF SDDS/DQAF metadata confirms detailed BOP history via Statistics → Interactive Database and Statistics → Data Sets: https://dsbb.imf.org/sdds/dqaf-base/country/ROU/category/BOP00
- C197's captured BNR page was a JavaScript shell; no dynamic table catalogue, Q2 portfolio series locator, export action or bytes were exposed.
- No JS-capable browser / Computer Use action is available in this execution context; therefore no claim is made that the BNR UI was operated.

### Georgia — NBG (cross-check of the same class of limitation)
- C154 already records NBG's stale NSDP observation snapshot at Q3/2021 and the absence of Q2-2026 dual legs.
- Official NSDP page: https://nbg.gov.ge/en/page/nsdp . Its text identifies a Balance of Payments “Browse Data” control and a “Download in SDMX” label, but the captured page does not expose a distinct download href/target for BOP.
- Official Statistics Data page: https://nbg.gov.ge/en/statistics/statistics-data . The captured text exposes search inputs for Title and Code, not the generated data table or export payload.
- Official NBG Statistics page describes static Excel tables and interactive dashboards: https://nbg.gov.ge/en/page/statistics
- NBG 2024 Annual Report describes an API-based data-exchange method as a planned development; this is not evidence of a currently accessible public API endpoint: https://nbg.gov.ge/fm/პუბლიკაციები/ანგარিশები/წლიური_ანგარიში/2024/annual-eng-2024.pdf?v=ejibg
- This is a route-capability finding only. GEO remains PARTIAL / NOT PASS; no Q2 values, raw bytes or hash captured.

### Other already documented interactive routes
- Bosnia and Herzegovina CBBH Panorama Necto: C156 documents an anonymous portal and Excel/PDF export controls, but the dynamic workboard was not executed.
- Moldova BNM Reports Generator: C86 documents visible quarter/currency/periodicity selectors and Generate/Export controls, but no report was generated and no export bytes captured.
- These are not treated as failed data sources; they are unexecuted UI routes.

## 3. New operational rule
For every future country task, add an **Execution-Mode Gate before selection**:
1. Classify the proposed official route as static downloadable file, documented machine API, or interactive JavaScript portal.
2. If static/API: verify exact URL, format, public accessibility and byte-capture capability before choosing it.
3. If interactive: require an actually available JS-capable browser / Computer Use session before selecting the task as executable.
4. If no interactive browser is available, record `NOT_EXECUTED — UI CAPABILITY UNAVAILABLE`; do not repeat page-shell inspections or call route discovery an export.
5. Advance to the next highest-value fixed-cohort member with a static official release/download/API route. Keep the UI task queued as blocked by execution capability, not as source absence.
6. If the user supplies the official exported file, inspect that file as a new evidence path; preserve original bytes and provenance and do not overwrite prior evidence.
7. Never infer values from net-only totals, IIP stocks, stale NSDP rows, annual/H1 aggregates, or IMF-only values.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Current Ledger / Queue / Registry / ROU history preflight | PASS |
| Fixed cohort / archived IMF data reused without new request | PASS |
| ROU BNR official route discovery from C197 retained | PASS — locator only |
| Current session has JS-capable interactive browser action | NOT_AVAILABLE |
| BNR Q2-2026 UI query/export executed | NOT_EXECUTED |
| GEO NBG BOP SDMX href/API payload exposed in captured page | NOT_CAPTURED |
| CBBH / BNM portal exports executed | NOT_EXECUTED |
| Country data retrieved or validated in C198 | NO |
| Reusable Execution-Mode Gate documented | PASS |
| ROU / GEO / BIH / MDA country validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 5. Next task selection rule
Do not spend another continuation reopening BNR/NBG/CBBH/BNM JavaScript shells in this same non-interactive session. The next country task must be selected from the fixed 63-country cohort only after a fresh full-history preflight and should prioritize a static official Q2-2026 release/workbook/PDF/API whose exact content can be retrieved and hashed here. If no such route is executable, report the blocker rather than manufacturing a PASS.

## 6. Protected invariants
₹0; official/free sources only. No synthetic values, fabricated timestamps, IMF re-query, cohort rebuild, inferred sign/scale/FX, unsupported monthly aggregation, net-to-leg back-solving, stocks-as-flows, production changes or aggregate admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
