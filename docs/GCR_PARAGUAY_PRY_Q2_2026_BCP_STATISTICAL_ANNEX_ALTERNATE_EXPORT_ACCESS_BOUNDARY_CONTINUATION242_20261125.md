# GCR — Paraguay (PRY) Q2-2026 BCP statistical-annex alternate export access boundary

Date: 2026-11-25 (Asia/Kolkata)
Continuation: 242

Decision: **A distinct official BCP Statistical Annex export was discovered and its current download locator resolved. The annex is described by BCP as containing balance-of-payments statistics, but the XLSX payload is rejected by the available document reader (HTTP 400 unsupported XLSX MIME) and a separate byte-download attempt failed. The workbook contents, Q2 portfolio asset/liability legs, raw bytes, headers and hash remain unverified. PRY remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity and duplicate-prevention preflight
- Re-fetched the current Master Continuity Ledger, GCR Priority Queue, Historical Task Registry and fixed 63-country national validation matrix; searched the Library Mother File/GCR context.
- Re-read controlling PRY C60 report: `docs/GCR_PARAGUAY_PRY_Q2_2026_BCP_BOP_IIP_SOURCE_BOUNDARY_AUDIT_CONTINUATION60_20261120.md`. It had confirmed the exact Q2 BOP/IIP XLSX locator, but the same XLSX MIME reader and direct byte route were blocked. Those exact routes were not retried.
- PRY is a fixed-cohort member and matrix status remains SOURCE_FOUND / PARTIAL with both national legs NOT_CAPTURED. No dedicated PRY dual-leg validation report existed beyond C60 in the scoped repository search.
- C237–C241 and accepted PASS work were skipped. No IMF re-query, cohort rebuild or panel rebuild.

## 2. Distinct official BCP statistical annex route
- Official BCP BOP/IIP page: https://www.bcp.gov.py/balanza-de-pagos-y-posicion-de-inversion-internacional . It says the BOP/IIP statistics cover flows and positions, include the financial account and IIP, and are disseminated quarterly and annually with a three-month lag.
- Distinct official BCP Statistical Annex page: https://www.bcp.gov.py/en/web/institucional/anexo-estadistico- . BCP describes this file as containing aggregate and sectoral economic statistics, monetary/financial variables, balance of payments, foreign trade and foreign-exchange income, periodically updated.
- The page's current download link resolves to:
  https://www.bcp.gov.py/documents/20117/213069/Anexo_Estad%C3%ADstico_del_Informe_Econ%C3%B3mico_23_11_2026.xlsx/1fc7fda2-74cf-e07c-be5b-535f02a89ba3?t=1795456089070
- This is a distinct official workbook from the C60 Q2-specific BOP/IIP workbook. The BCP page itself establishes the annex's broad subject coverage, not that it contains Q2-2026 portfolio A/L rows or an equivalent BOP table.
- Clicking the current annex XLSX through the document reader returned HTTP 400 / Unsupported content-type for the XLSX MIME. A separate direct byte-download attempt also failed. No claim is made about origin-server status or internal workbook contents.
- No raw bytes, headers, content length, sheet names, schema, period labels, row values, publication/revision metadata or SHA-256 were captured.

## 3. Period and source-scope boundary
- BCP's BOP/IIP page confirms quarterly/annual dissemination with a three-month lag. The separate statistical annex is periodically updated, but its exposed page does not provide a table inventory, exact Q2 coverage, observation vintage or separate portfolio A/L schema.
- The BOP publication calendar currently states the next quarterly BOP date as 30-Dec-2026. This is release-calendar metadata, not evidence of a newly published Q2 dual-leg table in the annex.
- Do not treat direct-investment annexes, securities-market data, banking balance sheets, IIP closing stocks, net-only portfolio values or annual projections as Q2 portfolio transaction legs.

## 4. Acceptance boundary
| Gate | Status |
|---|---|
| PRY fixed 63-country cohort membership | PASS (reused) |
| Prior C60 exact Q2 workbook route reviewed and not repeated | PASS |
| Distinct official BCP Statistical Annex page | PASS |
| Annex page states BOP statistics are included | PASS |
| Current annex XLSX locator resolved | PASS |
| Annex workbook raw bytes / headers / size / SHA-256 | NOT_CAPTURED |
| Annex sheet/schema and Q2-2026 period coverage | NOT_VERIFIED |
| Q2-2026 portfolio asset transaction leg | NOT_CAPTURED |
| Q2-2026 portfolio liability transaction leg | NOT_CAPTURED |
| Sign/unit/BPM6 row mapping | UNKNOWN |
| Observation-specific revision/vintage bridge | UNKNOWN |
| IMF national numeric comparison | NOT_DONE |
| PRY national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 5. Duplicate prevention and next action
- Close the current Statistical Annex XLSX reader-click and same-URL direct byte-download attempts for this runtime; do not repeat them unchanged.
- Reopen only if a genuinely different supported XLSX-capable browser/byte-transfer route or a distinct official BCP API/export provides inspectable data and revision metadata.
- If the annex is obtained, first archive exact URL, retrieval timestamp, response headers, byte count and SHA-256; then inspect sheet/table scope, period, portfolio asset and liability transaction rows, units, signs, BPM6 concepts and revision vintage. Reuse existing IMF exact-key rows only.
- Otherwise retain PRY PARTIAL / NOT PASS and advance to another eligible fixed-cohort member after full route-history preflight.

## 6. Protected invariants
₹0; official/free sources only; no synthetic values, fabricated timestamps, annual-to-quarter allocation, stock-as-flow substitution, net-to-leg back-solving, unsupported sign/scale/FX conversion, paid services or external contact. No IMF re-query/cohort rebuild. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 remain unchanged. No production integration or merge.
