# Paraguay (PRY) Q2-2026 BCP BOP/IIP Source-Boundary Audit — Continuation 60
Date: 2026-11-20 (Asia/Kolkata)
Status: **OFFICIAL QUARTERLY BOP/IIP DATASET AND EXACT Q2 WORKBOOK LOCATOR CONFIRMED; XLSX BYTE RETRIEVAL BLOCKED; PRY NATIONAL VALIDATION PARTIAL / NOT PASS.**

## 1. Continuity preflight and duplicate rejection
- Reopened the existing fixed 63-country Q2-2026 synchronous dual-leg cohort and current GCR Master Priority Queue before selection.
- Philippines (PHL) was not repeated: existing report docs/GCR_PHILIPPINES_PHL_Q2_2026_BSP_IMF_PORTFOLIO_DUAL_LEG_RECONCILIATION_20261120.md already records raw+parsed BSP capture PASS, release parity PASS, numeric asset/liability 2/2 PASS, and same-vintage NOT_ESTABLISHED. Its bounded official vintage review is closed as NOT_ESTABLISHED.
- Repository search found no dedicated PRY Q2-2026 national portfolio dual-leg validation report. PRY is in the existing 63-country cohort.
- No IMF re-query, cohort rebuild, panel rebuild, or repeated PHL work was performed.

## 2. Official BCP source discovery
- Banco Central del Paraguay (BCP) official BOP/IIP page: https://www.bcp.gov.py/balanza-de-pagos-y-posicion-de-inversion-internacional
- The page states BOP and IIP statistics cover flows and positions between Paraguay and the rest of the world, include current account, financial account and IIP, and are disseminated quarterly and annually with a three-month lag.
- The page exposes a single “Descargar” (Download) link for the BOP/IIP dataset.
- Exact linked Q2-2026 workbook URL: https://www.bcp.gov.py/documents/20117/1373920/Balanza%2Bde%2Bpagos%2By%2BPosici%C3%B3n%2Bde%2BInversi%C3%B3n%2BInternacional%2BQ2_2026.xlsx/24ef1522-c07b-518f-3845-2b6a00e24835?t=1790799251159
- The web retrieval route returned HTTP 400 “Unsupported content-type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet”. A separate direct byte-download attempt in the execution environment also failed.
- No XLSX bytes, ZIP package, sheet names, rows, values, workbook metadata, or SHA-256 were obtained. The failure is a retrieval limitation; it is not evidence that the workbook is absent or empty.

## 3. Scope boundary
- An IMF Article IV report contains annual/projected BOP totals and portfolio investment net projections, but it is not the official national Q2-2026 portfolio asset/liability transaction dataset. It is not used for numeric admission.
- Annual portfolio net values or projections cannot be allocated into Q2. Net-only values cannot replace separate asset and liability legs.
- No sign transform, scale conversion, or asset/liability value is inferred without inspecting the official workbook and its metadata.

## 4. Gate matrix
| Gate | Status |
|---|---|
| PRY membership in fixed 63-country Q2-2026 cohort | PASS |
| Duplicate-report search | PASS (no dedicated PRY report found) |
| Official BCP quarterly BOP/IIP source discovery | PASS |
| Exact Q2-2026 XLSX locator | PASS |
| XLSX byte retrieval | BLOCKED |
| Raw bytes / SHA-256 / workbook inspection | NOT_CAPTURED |
| Separate Q2 portfolio asset transaction value | NOT_EXTRACTED |
| Separate Q2 portfolio liability transaction value | NOT_EXTRACTED |
| Sign convention / BPM6 mapping | NOT_ESTABLISHED |
| Units / quarterly period / revision vintage | NOT_ESTABLISHED |
| IMF exact-row numeric comparison | NOT_DONE |
| PRY national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 5. Next exact action
1. Do not repeat the same unsupported-MIME request or same direct download attempt.
2. Resume only when a distinct supported XLSX-capable retrieval route or BCP official API/export route is identified.
3. Acquire exact workbook bytes and SHA-256 before parsing.
4. Inspect Q2-2026 portfolio asset and liability transaction rows separately, plus units, sign convention, BPM6 concepts, period labels, publication/revision metadata and whether values are quarterly or cumulative.
5. Reuse the existing archived IMF exact-key rows only after national source extraction; compare legs separately with explicit rounding bounds.
6. If no distinct official route is available, preserve PRY PARTIAL / NOT PASS and advance to the next unvalidated country in the fixed cohort.

## 6. Protected invariants
No synthetic values, fabricated timestamps, annual-to-quarter allocation, stock-as-flow substitution, net-only substitution, inferred sign transform, IMF re-query, cohort rebuild, paid API, or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.

## Evidence
- BCP official BOP/IIP data page: https://www.bcp.gov.py/balanza-de-pagos-y-posicion-de-inversion-internacional
- Exact official Q2-2026 XLSX locator: https://www.bcp.gov.py/documents/20117/1373920/Balanza%2Bde%2Bpagos%2By%2BPosici%C3%B3n%2Bde%2BInversi%C3%B3n%2BInternacional%2BQ2_2026.xlsx/24ef1522-c07b-518f-3845-2b6a00e24835?t=1790799251159
