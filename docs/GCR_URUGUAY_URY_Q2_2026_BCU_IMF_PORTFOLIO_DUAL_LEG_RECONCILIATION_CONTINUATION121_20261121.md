# Uruguay URY — BCU Q2-2026 portfolio dual-leg extraction and archived IMF comparison (Continuation 121)
Date: 2026-11-21 (Asia/Kolkata)

## Decision
The official Banco Central del Uruguay (BCU) Q2-2026 BOP report contains a sector-institutional portfolio investment transaction table. Summing its explicitly labelled sector rows yields portfolio asset transactions +USD 519m and portfolio liability transactions -USD 192m. BCU reports portfolio investment net +USD 710m; the separate legs imply +711m, a USD 1m published-rounding difference.

The already archived IMF panel contains exact URY Q2 rows, but raw observations are 518,514,442.91881 (A_NFA_T) and -191,945,243.218418 (L_NIL_T), each SCALE=6. The bounded comparison display OBS_VALUE/1,000,000 yields +USD 518.5144429m and -USD 191.9452432m. Against BCU's +519m / -192m, residuals are +USD 0.4855571m and -USD 0.0547568m respectively, both within ±USD 0.5m whole-million rounding. Derived IMF net is +USD 710.4596861m vs BCU published +USD 710m, residual -USD 0.4596861m, also within ±USD 0.5m. Numeric dual-leg comparison PASS at published precision; same-vintage / full scope equivalence remains NOT_ESTABLISHED, so full URY validation is PARTIAL / NOT PASS and aggregate NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate rejection
- Re-fetched Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `3a46c4dd898033f42269eea7d35d6ed88d9c6607`.
- Re-fetched GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `2122a932e6c14d32870988ce29530b1384f1fe35`.
- Reused immutable 63-country Q2-2026 cohort report `docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md`, blob SHA `1f767e22095865c8e5f87c2cfca55d9104b91e3e`; URY is in the fixed cohort following UKR.
- Scoped GitHub repository searches for URY/Uruguay Q2-2026 national dual-leg validation found no prior dedicated URY report. No IMF re-query, no cohort rebuild, and no repeat of PASS country tasks.

## 2. Official BCU Q2-2026 source and direct national values
- Issuer: Banco Central del Uruguay (BCU).
- Official report: “Informe de Balanza de Pagos y Posición de Inversión Internacional — Segundo trimestre 2026”.
- Exact PDF: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Balanza%20de%20Pagos/informe_m6.pdf
- Official report PDF inspected; lines 0–8 identify the BCU report and Q2 2026 period. The report states figures are preliminary (e.g. lines 73–77).
- Table 9, “Inversión de Cartera por Sector Institucional”, printed page 15 / PDF lines 681–703, reports (USD millions):
  - Public sector asset: -47
  - Private sector asset: +566
  - Public sector liability: -204
  - Private sector liability: +12
  - Portfolio investment net: +710
- Explicit sector-row aggregation:
  - Portfolio asset leg = -47 + 566 = **+519 USDm**.
  - Portfolio liability leg = -204 + 12 = **-192 USDm**.
  - Asset-minus-liability identity = 519 - (-192) = **+711 USDm**.
  - BCU published portfolio net = **+710 USDm** (Table 1, PDF lines 64–69; Table 9 lines 689–697); difference +1 USDm is consistent with published rounding caveat at lines 73–75 and 701–703.
- Narrative at lines 681–683 says portfolio investment had a capital outflow of USD 710m, within an increase in external assets of USD 519m and a reduction in liabilities of USD 192m. Thus sign interpretation is directly supported by the same BCU source.
- Do not use the separate IIP stock portfolio asset/liability values in Table 2 as transaction flows.

## 3. Existing archived IMF exact Q2 rows — no re-query
- Reused committed normalized panel file: `docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv`.
- Git blob SHA: `2a8db2878cac6323bbad74ffa4035dc70e5e6b98` (retrieved through the existing Git blob route; 1,849,027 characters).
- Source artifact context already recorded in prior research: IMF.STA:BOP(21.0.0), DSD IMF.STA:DSD_BOP(24.0.0), indicator P_F, unit USD, frequency Q; preserve all raw attributes.
- Exact URY 2026-Q2 panel rows:
  - A_NFA_T: OBS_VALUE = **518514442.91881**, SCALE=6, PRECISION=6, DERIVATION_TYPE=O; embedded raw-source SHA-256 `677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e`.
  - L_NIL_T: OBS_VALUE = **-191945243.218418**, SCALE=6, PRECISION=6; embedded raw-source SHA-256 `713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba`.
- Both rows have TIME_PERIOD=2026-Q2, REF_AREA=TZA, INDICATOR=P_F, UNIT_MEASURE=USD, FREQ=Q, and source origin O in the archived normalized panel.
- Exact IMF raw observations remain unchanged. Do not treat SCALE=6 as permission for a universal multiplier; prior calibration evidence supports a derived OBS_VALUE/1,000,000 display in a bounded 118/118 historical benchmark but does not establish country-specific semantic equivalence for URY or all 154 EMDEs.

## 4. Numeric comparison — PASS at published precision; vintage boundary remains open
The bounded cross-country comparison display OBS_VALUE/1,000,000 is used only as a derived presentation field; original raw observations and SCALE=6 remain unchanged. Prior research empirically supports this derived display in 118/118 historical benchmark comparisons, but it is not a universal conversion rule for all 154 EMDEs.
- IMF A_NFA_T display: +USD 518.51444291881m; BCU: +USD 519m; residual BCU−IMF = **+USD 0.48555708119m** (within ±USD 0.5m).
- IMF L_NIL_T display: -USD 191.945243218418m; BCU: -USD 192m; residual BCU−IMF = **-USD 0.054756781582m** (within ±USD 0.5m).
- IMF asset-minus-liability derived display net: +USD 710.459686137228m; BCU published net: +USD 710m; residual BCU−IMF = **-USD 0.459686137228m** (within ±USD 0.5m).
All three checks pass at BCU's whole-million published precision. This numeric agreement does not by itself establish same-vintage identity, complete scope equivalence or revision alignment.

## 5. Gate matrix
| Check | Status |
|---|---|
| URY membership in immutable 63-country cohort | PASS |
| No prior dedicated URY report found in scoped repo search | PASS (scoped search) |
| Official BCU Q2-2026 BOP report | PASS |
| Q2 period and USDm unit | PASS |
| Portfolio asset leg +519 USDm from explicit sector rows | PASS |
| Portfolio liability leg -192 USDm from explicit sector rows | PASS |
| BCU net +710 USDm vs legs +711 USDm | REVIEW: USD1m rounding difference |
| Archived IMF exact URY Q2 rows captured | PASS (reused; no new query) |
| IMF raw rows/attributes preserved | PASS |
| Derived OBS_VALUE/1,000,000 display for URY | NUMERICALLY CONSISTENT at ±0.5m; raw preserved |
| National-vs-IMF asset comparison | PASS (±USD0.5m) |
| National-vs-IMF liability comparison | PASS (±USD0.5m) |
| Same-vintage / scope / definition equivalence | NOT_ESTABLISHED |
| Numeric URY dual-leg validation | PASS at published precision |
| Aggregate admission | NOT_AUTHORIZED |
| Raw BCU PDF bytes / byte count / SHA-256 | NOT_CAPTURED |

## 6. Next exact action
- Do not repeat the BCU national extraction or IMF panel retrieval. Do not issue a new IMF query.
- Next highest-value work: inspect the existing IMF BOP source metadata/codelists and BCU methodology/SDDS data notes specifically for Uruguay's Q2 portfolio assets/liabilities sign, valuation, institutional scope, period basis and scale; determine whether the observed large residual is a unit/definition mismatch or true data discrepancy.
- Obtain and archive the BCU PDF raw bytes/hash using a byte-preserving route before any future revision comparison.
- If no direct official crosswalk explains the residual, keep URY PARTIAL / NOT PASS and advance to the next fixed-cohort country only after preflight.

## 7. Protected constraints
₹0; official/free sources only. No synthetic values, no inferred scale/sign transform, no stock-as-flow, no net-to-leg back-solving, no cross-country vintage assumption, no IMF re-query, no cohort rebuild, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Sources
- BCU Q2-2026 BOP/IIP report, especially Table 9 and its narrative: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Balanza%20de%20Pagos/informe_m6.pdf
- BCU SDDS Uruguay: https://www.bcu.gub.uy/Estadisticas-e-Indicadores/Documents/FMI/sddsuruguay.html
- Archived IMF normalized panel: `docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv`, Git blob SHA `2a8db2878cac6323bbad74ffa4035dc70e5e6b98`.
- Immutable 63-country cohort: `docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md`.
