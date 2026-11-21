# Romania (ROU) Q2-2026 — BNR Interactive Database official route discovery (Continuation 197)
Date: 2026-11-21 (Asia/Kolkata)
Decision: **A genuinely distinct official BNR Interactive Database route is now identified and independently reopened; route-discovery PASS only. The interactive dataset/export was not executed in this retrieval session; no Q2 portfolio A/L observations, raw bytes or SHA-256 captured. ROU remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Mandatory continuity and duplicate-prevention preflight
- Re-fetched current Master Continuity & Acceptance Ledger, GCR Master Priority Queue, Historical Task Registry and the complete ROU reports C95 and C96 before selecting the next task.
- Reused the immutable 63-country Q2-2026 cohort and existing IMF raw archive. No IMF GET, cohort rebuild, or repeat of the previously inaccessible ECB SDW API endpoints.
- C95 established BNR as compiler, BPM6, separate net asset/liability dissemination, monthly/quarterly release and revision metadata; exact Q2 values were not captured.
- C96 documented Romania's portfolio compilation method, partial external-custodian coverage, and closed the same ECB API/web retrieval surface. It explicitly allowed reopening only through a supported BNR Interactive Database / Data Sets export or a verified ECB byte-preserving route.
- Repository searches for ROU + BNR Interactive Database / Data Sets found no C197 or earlier dedicated report documenting an executed BNR Interactive Database export. This is a new source-family route, not a retry of ECB API.

## 2. New official BNR route evidence
- Official National Bank of Romania interactive database landing page independently opened:
  https://www.bnr.ro/en/2550-interactive-database
- The official BNR site page identifies the Statistics > Interactive Database navigation section. The page itself is a JavaScript-driven shell in the current text retrieval; it does not expose the database's loaded table catalogue or export controls in the captured page text.
- IMF SDDS/DQAF metadata supplied by Romania and posted 29-Jan-2026 explicitly states that detailed and longer BOP series (starting 2005) are available through:
  1. Statistics – Interactive Database (Balance of payments), and
  2. Statistics – Data Sets (Balance of payments and international investment position).
  It states quarterly BOP data are disseminated simultaneously on the NBR website and NSDP, and the interactive database is updated periodically after releases/revisions.
- The official metadata also states the current data system uses monthly and quarterly direct reports, securities-holdings datasets and other source systems for portfolio investment. It warns that reporting gaps exist for Romanian debt instruments held by non-residents through external custodians. That national coverage caveat remains material and cannot be removed by a numeric match alone.
- This BNR route is genuinely distinct from the previously exhausted ECB SDW API endpoints and from the ECB portal HTML series pages.

## 3. Execution boundary
- Opened the official BNR Interactive Database landing page in this session; its dynamically loaded database controls and export endpoint were not exposed to the text retrieval bridge.
- The BNR Data Sets route is confirmed by official DSBB metadata, but an exact Q2 portfolio table locator, series IDs, interactive query, export format and downloadable response were not exposed in this bounded retrieval.
- No browser-driven selection/export was executed; no Q2 observation values, source revision cutoff, raw payload, response headers, retrieval receipt, byte count or SHA-256 were captured.
- This is route-discovery PASS only. It is not data retrieval PASS, numeric PASS, or national validation PASS. Do not claim the BNR export was downloaded.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| Ledger / Queue / Registry / full ROU history preflight | PASS |
| Fixed 63-country cohort / archived IMF rows reused | PASS |
| Official BNR Interactive Database route identified and reopened | PASS — locator only |
| Official BNR Data Sets route confirmed in DSBB metadata | PASS — route family only |
| Dynamic table catalogue / exact Q2 portfolio table locator | NOT_CAPTURED |
| Separate Q2 portfolio asset observation | NOT_CAPTURED |
| Separate Q2 portfolio liability observation | NOT_CAPTURED |
| Export bytes / headers / receipt / SHA-256 | NOT_CAPTURED |
| Series scope, units, signs, monthly/quarterly basis and vintage | NOT_ESTABLISHED |
| National portfolio coverage completeness | PARTIAL / NOT_ESTABLISHED (external-custodian gap) |
| ROU national validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 5. Next bounded action
- Use an actual interactive browser session capable of running the BNR page's JavaScript controls; navigate Statistics → Interactive Database → Balance of payments, identify the Q2-2026 portfolio investment asset and liability transaction rows, select the relevant total-economy sector and period, and use the official export control.
- Capture untouched CSV/XLS/XLSX or other native export bytes, exact table/series identifiers, units, sign conventions, quarter and revision/vintage metadata, retrieval timestamp, byte count and SHA-256 before reading values.
- Confirm whether the output is quarter-specific or cumulative/summed-through-period; do not sum monthly series unless the official metadata confirms the required flow basis and revision consistency.
- If the interactive export cannot be operated, keep ROU PARTIAL / NOT PASS and advance to the next eligible fixed-cohort country. Do not retry the exact ECB endpoints already closed.
- Preserve the external-custodian coverage caveat in any later validation result.

## 6. Protected invariants
₹0; official/free sources only. No synthetic data, fabricated timestamps, unsupported monthly aggregation, net-to-leg inference, stock-as-flow, unverified FX/sign/scale, IMF re-query, cohort rebuild, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
