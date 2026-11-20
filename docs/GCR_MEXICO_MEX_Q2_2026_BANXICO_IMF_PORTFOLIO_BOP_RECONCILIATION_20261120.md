# Mexico MEX Q2-2026 Banxico vs IMF portfolio BOP reconciliation — 2026-11-20

Decision: **Both national-vs-IMF portfolio legs PASS at Banxico's published whole-USD-million rounding. Exact same-vintage identity remains NOT_ESTABLISHED; full national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## Continuity preflight
- Re-fetched current Master Continuity Ledger, GCR Priority Queue, TUR reconciliation and vintage cross-check, POL source-gate audit, SAU vintage audit and CHN access audit.
- TUR's TCMB ZIP timeout and +USD87m liability discrepancy were already documented; no repeated download attempt or IMF retrieval.
- Selected Mexico (MEX), next eligible member of the existing 12-country exact-key IMF sample. Reused artifact 14505009889; no new IMF GET, no panel rebuild and no cohort rebuild.

## Existing IMF exact-key receipt
Receipt: run 44474458684 / artifact 14505009889 / ZIP SHA-256:
588101c0deff3b431098e0f3205005d3d5913f3014137065b074890b353ecdf60

- MEX A_NFA_T raw CSV: 4,893 bytes; SHA-256 a404aca5a719b9558e75b9483b925d18011fa2d9199937d275956782a84c5014.
- MEX L_NIL_T raw CSV: 4,741 bytes; SHA-256 1a7de8eb3d258875fbffbde987ce22db437eadbdd9c93e05acec12a4ab7785c7.
- Q2-2026 IMF values (OBS_VALUE USD; SCALE=6 / Millions): A_NFA_T +8,937,255,098 USD = +8,937.255098 USDm; L_NIL_T +10,561,285,114 USD = +10,561.285114 USDm.

## Official national source — Banco de México
Official publication page: https://www.banxico.org.mx/publicaciones-y-prensa/balanza-de-pagos/balanza-pagos-comercio-invers.html
Official Q2 2026 PDF: https://www.banxico.org.mx/publicaciones-y-prensa/balanza-de-pagos/{E333A05C-EB45-9A4A-6F1D-591845A64896}.pdf
- Publication date: 25-Aug-2026. Cuadro 3, PDF page 6, unit million USD:
  - II. Portfolio investment (A−B), Q2 2026 = -1,624.
  - A. Net acquisition of financial assets = +8,937.
  - B. Net incurrence of liabilities = +10,561.
  - Identity: 8,937 − 10,561 = -1,624.
- Concepts map directly to IMF A_NFA_T and L_NIL_T. Both sources are USD-denominated; no FX conversion or sign transformation is required.
- Banxico's footnote says the release incorporates revisions in some BOP items as additional information becomes available, and components may be revised in future releases. It does not say these specific portfolio legs were revised in this release.

## Like-for-like Q2 comparison
| Leg | Banxico Q2 2026 (USDm) | IMF exact Q2 2026 (USDm) | IMF − Banxico residual (USDm) | Rounding bound | Result |
|---|---:|---:|---:|---:|---|
| Portfolio assets / A_NFA_T | +8,937 | +8,937.255098 | +0.255098 | ±0.5 | PASS |
| Portfolio liabilities / L_NIL_T | +10,561 | +10,561.285114 | +0.285114 | ±0.5 | PASS |

Both residuals fall within the ±0.5 USDm half-unit bound of Banxico's whole-million display. No tolerance widening, fitted adjustment, netting or imputation was used.

## Vintage assessment
- Banxico Q2 release publication date: 2026-08-25.
- Banxico explicitly says BOP components may be revised in future releases.
- IMF exact receipt timestamp: 2026-11-19. This does not prove the IMF values were sourced from the identical Banxico release vintage.
- Exact Banxico↔IMF same-vintage bridge / versioned Q2 portfolio revision history: NOT_ESTABLISHED.
- Strong numeric agreement does not close the independent vintage gate.

## Acceptance matrix
- Existing IMF exact receipt and raw CSV hashes: PASS.
- Banxico official Q2 2026 source and publication date: PASS.
- Portfolio asset and liability concept/sign mapping: PASS.
- Asset numeric comparison: PASS at published rounding.
- Liability numeric comparison: PASS at published rounding.
- Exact same-vintage identity: NOT_ESTABLISHED.
- MEX full national dual-leg validation: PARTIAL / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## Next exact action
Seek a versioned Banxico Q2-2026 data vintage or dated revision record for the two portfolio components, and establish whether the IMF 2026-11-19 values use that same national vintage. If no public versioned record exists, preserve MEX as PARTIAL and advance to the next eligible cohort member. Do not infer same-vintage from small residuals; no new IMF query or cohort rebuild is needed.

## Protected invariants
No cross-country aggregation, netting, imputation, forward-fill, synthetic observations, silent sign transform or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.
