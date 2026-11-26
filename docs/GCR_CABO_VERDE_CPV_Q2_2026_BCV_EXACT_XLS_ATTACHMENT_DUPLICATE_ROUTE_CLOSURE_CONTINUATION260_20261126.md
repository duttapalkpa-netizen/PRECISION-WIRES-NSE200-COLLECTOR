# GCR Cabo Verde (CPV) Q2-2026 — BCV exact XLS attachment identity and duplicate-route closure
Date: 2026-11-26 (Asia/Kolkata)
Continuation: 260
Decision: THE CURRENT OFFICIAL BCV BOP PAGE'S XLS ATTACHMENT TARGET HAS NOW BEEN RESOLVED. ITS EXACT URL IS IDENTICAL TO THE C153 OFFICIAL Q2-2026 XLS LOCATOR. The document reader rejects the XLS MIME type (HTTP 400 unsupported content type). Because the same URL and failed retrieval route were already closed in C153, no byte-download retry was made. This resolves C256's identity uncertainty but yields no new workbook bytes or national values. CPV remains SOURCE_FOUND / PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## 1. Mandatory continuity and Library preflight
- Re-fetched the current GitHub Master Continuity Ledger, GCR Priority Queue, Historical Task Registry, fixed 63-country cohort and national validation matrix before work.
- Re-read Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md`, CPV C213 methodology resolution, C153 original source gate and C256 updated locator boundary.
- Skipped completed PASS work: fixed cohort membership, archived IMF A_NFA_T/L_NIL_T raw receipts, BCV BPM6 methodology, BOP-flow vs IIP-stock distinction and BPM6 sign/gross-reporting methodology.
- No IMF re-query, cohort rebuild, panel rebuild or production workflow run.

## 2. Current official page and exact attachment target
- Official BCV BOP statistical page:
  https://www.bcv.cv/pt/Estatisticas/Quadros%20Estatisticos/Sector%20Externo/quadrosestatisticos/Paginas/BalancadePagamentos.aspx
- The currently accessible official page lists “Balança de Pagamentos (Estatísticas do 1º trimestre de 2012 a 2º trimestre de 2026)” as an XLS attachment. The rendered page shows the BOP document link; the page describes quarterly external-sector BOP flows and separately lists IIP as a stock dataset.
- Following the BOP XLS link resolved the exact target:
  https://www.bcv.cv/pt/Estatisticas/Quadros%20Estatisticos/Sector%20Externo/quadrosestatisticos/Documents/2026/Setembro/Balan%C3%A7a%20de%20Pagamentos%20%28Estat%C3%ADsticas%20do%201%C2%BA%20trimestre%20de%202012%20a%202%C2%BA%20trimestre%20de%202026%29.xls
- The reader returned HTTP 400 / unsupported content type `application/vnd.ms-excel`.
- Exact comparison with C153 shows the same URL character-for-character. C153 already records this exact official XLS URL, a failed web link-follow retrieval and a failed separate direct container byte-download. Therefore this is not a new file or alternate transfer route. It is the same closed route, now independently resolved from the current page.
- No new download attempt was made. No bytes, headers, content length, sheet names, rows, cell values, retrieval receipt or SHA-256 are claimed.

## 3. Reused source/methodology and data boundary
- C213 official BCV June-2016 external-sector methodology remains PASS: BPM6, BOP transaction flows vs IIP stocks, portfolio functional category, gross financial-account reporting and BPM6 sign convention.
- C153 archived IMF raw CPV rows remain unchanged and must be reused only; do not query IMF again:
  - A_NFA_T OBS_VALUE=364678.4706264281 USD, SCALE=6.
  - L_NIL_T OBS_VALUE=0 USD, SCALE=6.
- These IMF rows do not validate national observations. No conversion/comparison is admitted because BCV workbook rows and national unit/sign/vintage remain unavailable.
- Do not use the separate IIP XLS, IIP stocks, net portfolio balance, aggregate financial-account lines, or annual/H1 values as substitutes for separate Q2 portfolio transaction assets and liabilities.

## 4. Acceptance result
| Gate | Status |
|---|---|
| Current Ledger / Queue / Registry / fixed cohort / matrix preflight | PASS |
| Library Mother File and C153/C213/C256 review | PASS |
| Current official BCV BOP XLS page/link opened | PASS |
| Exact XLS attachment URL resolved | PASS |
| Exact URL identity vs C153 | SAME URL — DUPLICATE CLOSED |
| XLS reader MIME response | 400 unsupported application/vnd.ms-excel |
| New raw workbook bytes / headers / size / SHA-256 | NOT_CAPTURED; no retry |
| Workbook schema, period headers and Q2 portfolio A/L rows | NOT_VERIFIED |
| National unit/sign/concept bridge | NOT_ESTABLISHED |
| Observation-specific vintage | NOT_ESTABLISHED |
| National numeric comparison | NOT_DONE |
| CPV national validation | SOURCE_FOUND / PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 5. Decision and next action
- C260 closes C256's exact attachment-identity uncertainty: the current page link is the same C153 XLS endpoint. Do not repeat the identical browser click or direct byte-download route.
- Reopen CPV only if a genuinely distinct official BCV API/export, a different file version/URL with new revision evidence, or a supported byte-preserving route not used in C153 becomes available.
- Otherwise keep CPV gates unchanged and advance to the next eligible fixed-cohort country after full report-history and duplicate-prevention preflight.
- No national values or hashes are fabricated; no gate promotion is permitted.

## 6. Protected invariants
₹0; free official sources only; no IMF re-query/cohort rebuild; no synthetic data, net-to-leg back-solving, IIP-stock-as-flow, H1/annual interpolation, guessed sign/scale/FX, fabricated timestamps/hashes, tolerance widening, aggregate admission or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL. No workflow dispatch, merge or production integration.
