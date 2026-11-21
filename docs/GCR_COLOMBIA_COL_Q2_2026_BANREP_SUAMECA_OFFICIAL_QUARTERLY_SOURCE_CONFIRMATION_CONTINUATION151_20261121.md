# Continuation 151 — Colombia COL Q2-2026 BanRep official quarterly portfolio-flow source confirmation
Date: 2026-11-21
Status: PARTIAL / BLOCKED — official Q2 series identity and period coverage reconfirmed; exact series observations/export bytes, raw hash and revision-vintage bridge NOT_CAPTURED.

## Progress log
- Reused fixed 63-country Q2-2026 cohort and existing IMF panel receipts; no IMF re-query and no cohort rebuild.
- Reopened the current Master Priority Queue, Continuity Ledger, cohort, COL source-boundary audit and batch-10 execution record before proceeding.
- Excluded repeat work: previous SUAMECA multiple-download 502 route and already discovered series labels; no duplicate request to the same failing endpoint.

## New official BanRep evidence
1. BanRep Q2-2026 BOP/IIP report, published 1-Sep-2026:
   https://banrep.gov.co/es/publicaciones-investigaciones/informe-balanza-pagos/segundo-trimestre-2026?page=1
   - The report explicitly describes Q2-2026 net portfolio-instrument liquidations as partially offsetting net capital inflows.
   - It does not publish the separate numerical portfolio asset and liability transaction legs in the accessible narrative.
   - Its IIP section gives end-June portfolio positions; these are stocks and are excluded from the BOP flow test.
2. Official SUAMECA multiple-download catalogue:
   https://suameca.banrep.gov.co/descarga-multiple-de-datos/
   - The current catalogue lists separate quarterly series for (a) portfolio investment net acquisition of financial assets and (b) portfolio investment net incurrence of liabilities.
   - Both catalogue entries state current USD millions, quarterly frequency, coverage 31-Mar-2000 through 30-Jun-2026, last updated 1-Sep-2026.
   - This establishes that exact Q2-2026 series should exist in the official catalogue; it does not expose their exact values, series IDs or a downloadable raw payload in the captured search response.
3. BanRep's official user guide explains that the multiple-download service selects multiple historical variables and generates tables; the documented export function is available in desktop portal view:
   https://www.banrep.gov.co/es/preguntas-frecuentes/como-usar-nuevo-portal-estadisticas-economicas

## Acceptance
| Gate | Status |
|---|---|
| COL in fixed Q2-2026 both-leg cohort | PASS (existing cohort) |
| Official Q2 report / quarter context | PASS |
| Official separate quarterly portfolio asset and liability catalogue entries | PASS |
| Catalogue coverage reaches Q2-2026; unit USDm | PASS |
| Exact Q2 asset and liability observations | NOT_CAPTURED |
| Exact series IDs / export payload / raw bytes / SHA-256 | NOT_CAPTURED |
| Sign definition and same-vintage bridge | NOT_ESTABLISHED |
| Numeric IMF-national comparison | NOT_DONE |
| COL full national validation | PARTIAL / BLOCKED; NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## Next exact action
Use the documented desktop SUAMECA export control or another genuinely supported official export surface to retrieve both exact series together. Capture series IDs, Q2 observations, response bytes, retrieval timestamp, SHA-256 and revision metadata. Then compare both legs separately against the already archived IMF raw rows. If the public portal remains inaccessible, retain this blocker and move to the next fixed-batch country; do not retry the same 502 endpoint or substitute IIP positions / qualitative report narrative.

## Protected invariants
₹0; official/free sources only. No synthetic data, inferred values, net-to-leg back-solving, sign/scale assumptions, IMF re-query, cohort rebuild, aggregate admission or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
