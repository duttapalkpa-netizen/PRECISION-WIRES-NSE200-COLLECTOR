# Cabo Verde (CPV) Q2-2026 — BCV official BOP source gate
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 153
Status: FIXED-COHORT MEMBERSHIP PASS; OFFICIAL BCV Q2-2026 BOP WORKBOOK LOCATOR / PERIOD COVERAGE PASS; WORKBOOK BYTES NOT_CAPTURED; NATIONAL PORTFOLIO DUAL-LEG EXPOSURE NOT_VERIFIED; BPM6/BPM5 METADATA CONFLICT; CPV PARTIAL / BLOCKED, NOT PASS.

## 1. Continuity preflight and duplicate rejection
- Re-fetched current Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, blob SHA `4e838cfff1695f84a1b4bb55cc340610f745090a`.
- Re-fetched current GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, blob SHA `4b080ae1148bb8ce7d04700047d191583da86fa1`.
- Reused immutable 63-country Q2-2026 cohort CSV: `docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv`, blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`. Exact CPV row confirms both A_NFA_T and L_NIL_T entries PRESENT; national validation pending; aggregate NOT_AUTHORIZED.
- Repository search for CPV/Cabo Verde Q2-2026 national portfolio dual-leg audit returned no prior dedicated CPV report. No cohort rebuild, no IMF query, no repeat completed country work.

## 2. Official BCV source discovery
- Official Banco de Cabo Verde BOP statistical page: https://www.bcv.cv/pt/Estatisticas/Quadros%20Estatisticos/Sector%20Externo/quadrosestatisticos/Paginas/BalancadePagamentos.aspx
- Page rendering date shown: 17-Nov-2026.
- The page lists “Balança de Pagamentos (Estatísticas do 1º trimestre de 2012 a 2º trimestre de 2026)” as an XLS download. This establishes an official national BOP dataset locator and reported coverage through Q2-2026, not the workbook's internal table layout or portfolio-leg availability.
- Exact XLS link resolved from the official page:
  https://www.bcv.cv/pt/Estatisticas/Quadros%20Estatisticos/Sector%20Externo/quadrosestatisticos/Documents/2026/Setembro/Balan%C3%A7a%20de%20Pagamentos%20%28Estat%C3%ADsticas%20do%201%C2%BA%20trimestre%20de%202012%20a%202%C2%BA%20trimestre%20de%202026%29.xls
- Web link-follow retrieval timed out. A separate direct container byte-download attempt also failed. No workbook bytes, HTTP headers, sheet names, cell values, file size, retrieval receipt or SHA-256 captured.
- A separate official BCV Statistical Bulletin PDF search result for “Boletim de Estatísticas março 2026” presents one aggregate “Investimento de Carteira” net line, not separately verified asset and liability legs; it is an earlier Q1 publication and cannot be used as Q2 evidence or as a substitute for the Q2 workbook.
- Official BCV statistical overview states external-sector statistics include BOP transaction flows quarterly and distinguishes IIP positions as quarter-end stocks: https://www.bcv.cv/en/Estatisticas/Quadros%20Estatisticos/Paginas/QuadrosEstatisticos.aspx

## 3. Methodology / vintage boundary
- IMF e-GDDS DQAF page for Cabo Verde states BOP is compiled/disseminated quarterly, data are presented in CVE, and foreign-currency transactions are converted at average monthly exchange rates. It also states provisional BOP data are revised quarterly and that no established revision policy is described:
  https://dsbb.imf.org/egdds/dqaf-base/country/CPV/category/BOP00
- The same e-GDDS metadata describes the national compilation basis as BPM5. However, the BCV March-2026 Statistical Bulletin's BOP table note says the statistics are compiled according to BPM6. These are conflicting version statements. The e-GDDS page does not expose a current metadata update date in the indexed text; treat its BPM5 statement as a possible legacy metadata entry, not as proof of current practice. Do not silently select BPM6 or BPM5 without current BCV methodology/version evidence.
- No observation-specific release/revision vintage for the Q2 workbook was obtained beyond the page's 17-Nov-2026 rendering date and the file's stated period coverage.

## 4. Existing IMF raw rows reused — no new request
From the already archived raw IMF CSV files:
- Asset source `docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`, Git blob SHA `15449e87c9057291a1f52f2f8cd9805df55f9fb8`. Exact CPV row: COUNTRY=CPV; ENTRY=A_NFA_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=364678.4706264281; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG=true.
- Liability source `docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`, Git blob SHA `15f379dc42e2760eb5f2384618e48f5ddc3177f1`. Exact CPV row: COUNTRY=CPV; ENTRY=L_NIL_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=0; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG blank.
- Preserve raw OBS_VALUE and SCALE separately. No conversion or comparison is admitted in this report. Git blob SHAs are Git object identifiers, not newly computed file SHA-256 digests.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| CPV in immutable 63-country Q2-2026 cohort | PASS |
| Both archived IMF Q2 legs present | PASS |
| Official BCV BOP dataset locator | PASS |
| BCV catalogue coverage through 2026-Q2 | PASS |
| Official workbook bytes / sheet structure / values | NOT_CAPTURED |
| Q2 portfolio assets and liabilities separately published | NOT_VERIFIED |
| National unit/sign/concept bridge | NOT_ESTABLISHED |
| Current BPM6 vs BPM5 methodology version | CONFLICT / NOT_ESTABLISHED |
| National publication/revision vintage | NOT_ESTABLISHED |
| Separate-leg numeric comparison | NOT_DONE |
| CPV full national validation | PARTIAL / BLOCKED; NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 6. Next bounded action
- Do not retry the identical BCV XLS URL through the same failed retrieval routes.
- Seek a genuinely different official BCV export/API route or a browser/desktop path that can preserve the original XLS bytes. Once available, inspect workbook sheets, period headers, separate portfolio asset/liability rows, unit, sign and revision notes; preserve exact file bytes, retrieval timestamp and SHA-256.
- Reconcile current BCV methodology version (BPM5 vs BPM6) from a dated official BCV methodology note. The IMF e-GDDS metadata alone is insufficient to resolve the conflict.
- Only after both national legs and the methodology/vintage bridge are verified, compare separately to the archived IMF raw rows. Do not use the Q1 aggregate net line, net portfolio balance, IIP stocks or annual IMF staff estimates as Q2 dual-leg substitutes.
- If no genuinely different supported source route exists, retain CPV PARTIAL/BLOCKED and advance to the next eligible fixed-cohort member.

## 7. Protected invariants
₹0; official/free sources only. No IMF re-query, no cohort rebuild, no synthetic values, no H1/annual interpolation, no net-to-leg back-solving, no IIP-stock-as-flow, no inferred sign/scale or FX transformation, no aggregate admission and no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
