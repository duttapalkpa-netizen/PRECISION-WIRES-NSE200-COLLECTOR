# GCR Saudi Arabia (SAU) Q2-2026 SAMA ↔ IMF portfolio BOP reconciliation
Date: 2026-11-20
Decision: **Both portfolio legs numerically PASS at SAMA published rounding; national source values are explicitly estimates (e); same-vintage alignment remains REVIEW; full SAU validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## Progress log / continuity preflight
- Re-fetched Master Continuity Ledger, GCR priority queue, IDN sign-crosswalk report, IDN comparison, CHN workbook-access audit, cross-country benchmark and fixed 63-country cohort.
- Excluded completed PASS work: IMF DSD/registry capture, WEO roster, 9,299-row panel QA, 63-country cohort derivation, 12-country exact-key receipt and completed country source extractions. Did not repeat the unresolved IDN same-vintage work; moved to next large-market member of the fixed cohort, SAU.
- Reused exact IMF SAU observations from the existing 12-country receipt; no new IMF requests or panel rebuild.

## 1. Existing IMF exact-key evidence
Receipt: `docs/evidence/imf_bop_emde_20261119/exact_sample_checks/summary.json`.
Run 44474458684; artifact 14505009889; ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`.
- SAU A_NFA_T exact request: HTTP 200; retrieved 2026-11-19T06:45:22.313639Z; 5,201 bytes; raw CSV SHA-256 `7574486199f032a8eabfdc2dc38e21f0f70247165537a5732777032de0cbc76d`.
- SAU L_NIL_T exact request: HTTP 200; retrieved 2026-11-19T06:45:22.787613Z; 4,980 bytes; raw CSV SHA-256 `b2c557662bcfaf22771a3ef50f4d43c48f664abea32d31118adcab5c58cdd926`.
- Both exact requests match all 46 broad-panel observations and attributes, 2015-Q1 through 2026-Q2; no missing keys or attribute/value mismatches.
- IMF Q2-2026 raw OBS_VALUE:
  - A_NFA_T = +9,663,782,086.456987 USD.
  - L_NIL_T = +6,381,234,539.086 USD.
  - Both carry SCALE=6 (Millions); comparison display divides raw value by 1,000,000. Preserve raw values and SCALE separately.

## 2. Official national source — SAMA
Saudi Central Bank (SAMA), September 2026 Monthly Statistical Bulletin, External Sector, Table 1: Balance of Payments, Contd.6, printed page 131 / PDF page 131.
Official PDF:
https://www.sama.gov.sa/en-US/Statistics/MonthlyStatistics/Monthly_Statistical_Bulletin_For_Sep_2026.pdf
- Quarterly table period Q1 2024–Q2 2026; Q2 2026 explicitly marked **e = Estimated**. Footnote defines p=provisional, e=estimated, r=revised.
- Unit: USD million.
- Q2 2026 portfolio investment:
  - 3.2 Portfolio investment = +3,283 USDm.
  - 3.2.1 Net acquisition of financial assets = +9,664 USDm.
  - 3.2.2 Net incurrence of liabilities = +6,381 USDm.
  - Identity: 6,381 − 9,664 = −3,283 if expressed as liabilities less assets; table portfolio investment balance is +3,283 under SAMA's financial-account presentation. This balance identity is not used to infer either leg; the two component lines are independently compared.
- SAMA's table explicitly names the two IMF-like concepts “Net acquisition of financial assets” and “Net incurrence of liabilities”; no FX conversion is required because both sources are USD.
- The September 2026 Monthly Statistical Bulletin page is dated September 2026; SAMA's Monthly Statistics page identifies the September 2026 bulletin as published 29 October 2026.

## 3. Like-for-like numerical comparison
| Leg | SAMA Q2-2026 (USDm, estimated) | IMF raw OBS_VALUE (USD) | IMF USDm (raw / 1e6) | IMF − SAMA residual (USDm) | SAMA whole-million rounding bound | Result |
|---|---:|---:|---:|---:|---:|---|
| Portfolio assets / A_NFA_T | +9,664 | +9,663,782,086.456987 | +9,663.782086 | -0.217914 | ±0.5 | PASS |
| Portfolio liabilities / L_NIL_T | +6,381 | +6,381,234,539.086 | +6,381.234539 | +0.234539 | ±0.5 | PASS |

Both residuals are within the ±0.5 USDm half-unit rounding bound for SAMA's whole-USD-million display. Signs and component labels match. No sign flip, currency conversion, netting, or fitted tolerance was used.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| SAU in existing 63-country Q2 both-leg cohort | PASS |
| IMF exact-key retrieval and 46/46 broad-key matches | PASS |
| SAMA official Q2-2026 national BOP table | PASS |
| SAMA portfolio asset/liability concept labels | PASS |
| SAMA Q2 national vintage | PASS — explicitly Estimated (e) |
| Asset numerical comparison | PASS at published rounding |
| Liability numerical comparison | PASS at published rounding |
| Same-vintage SAMA↔IMF alignment | REVIEW / NOT_ESTABLISHED |
| SAU full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 5. Interpretation and next action
This is a strong two-leg magnitude/sign benchmark, but not a full national-source vintage PASS: SAMA labels Q2 2026 as an estimate, while the IMF receipt gives a 2026-11-19 retrieval timestamp without proving that the IMF observations were sourced from the exact same SAMA estimate vintage. Retain the estimate label and do not infer an exact same-vintage match from small residuals alone.
Next action: seek a dated SAMA historical revision/vintage archive for the Q2 2026 estimated portfolio legs or a subsequent revised Q2 publication. If no versioned archive is public, keep SAU PARTIAL and advance within the fixed cohort. No new IMF query is needed.

## Protected invariants
No aggregate, netting, imputation, forward-fill, synthetic observations, silent sign transform, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
