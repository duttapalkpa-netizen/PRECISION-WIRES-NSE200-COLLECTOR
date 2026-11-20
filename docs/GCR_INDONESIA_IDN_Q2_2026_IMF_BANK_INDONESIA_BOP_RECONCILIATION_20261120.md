# GCR Indonesia (IDN) Q2-2026 IMF ↔ Bank Indonesia portfolio BOP reconciliation
Date: 2026-11-20
Decision: liability comparison PASS at published precision; asset magnitude corroborates but signed comparison REVIEW; full dual-leg national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## Progress log and preflight
- Re-fetched Master Continuity Ledger, GCR priority queue, CHN detailed-workbook blocker, CHN comparison, ZAF comparison, cross-country report and fixed 63-country cohort before work.
- Excluded completed PASS work: IMF DSD/registry capture, WEO 154-member roster, 9,299-row panel QA, fixed 63-country cohort, existing 12-country exact-key retrieval, and prior country comparisons. No panel rebuild or new IMF query.
- IDN was selected from the fixed 63-country Q2 both-leg cohort; the pre-existing 12-country exact-key receipt already contains both IDN series.

## 1. IMF exact-key source receipt (reused)
Receipt: `docs/evidence/imf_bop_emde_20261119/exact_sample_checks/summary.json`.
Run 44474458684; artifact 14505009889; ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`.
- IDN A_NFA_T: HTTP 200; retrieved 2026-11-19T06:45:17.435091Z; raw CSV 5,174 bytes; SHA-256 `db7198b4c2ccc7bcbe6c45312506913c71507339c6e7bd609c5e1ff6500aae8b`.
- IDN L_NIL_T: HTTP 200; retrieved 2026-11-19T06:45:17.874893Z; raw CSV 5,000 bytes; SHA-256 `4ec6d04eae8187bd4235c6120f3be5f67972ff32ebfea1accf6cd0a1ab2b4108`.
- Both exact requests match broad panel keys/attributes for all 46 observations; no missing or attribute/value mismatches; period coverage 2015-Q1 through 2026-Q2.
- Q2-2026 IMF raw values: A_NFA_T = +1,487,605,237.21664 USD; L_NIL_T = +11,440,221,641.9221 USD. Both CSV rows carry UNIT=USD, SCALE=6; preserve raw OBS_VALUE and SCALE separately; comparison in USDm uses raw / 1,000,000.

## 2. Official Bank Indonesia national source
Bank Indonesia, Indonesian Economic and Financial Statistics (SEKI), Table V.7 “Financial Account: Portfolio Investment”, official PDF:
https://www.bi.go.id/SEKI/tabel/TABEL5_7.pdf
English table is printed page 137 / PDF table page; unit Millions of USD. Q2** 2026 column:
- Portfolio investment total: +9,953 USDm.
- A. Assets: -1,488 USDm.
- B. Liabilities: +11,440 USDm.
- BI footnote: * Temporary Data; ** Very Temporary Data. Q2 2026 is marked ** (very temporary).
The BI SDDS external-sector page independently reports latest BOP observation Q2/26 and portfolio investment financial account aggregate, but its summary view does not expose separate assets/liabilities. Do not use IIP positions as BOP flows.
Q2 press release dated 2026-08-21 describes the capital and financial account as surplus, supported by portfolio inflows, but the detailed V.7 table is the benchmark for the two legs.

## 3. Reconciliation (each leg separately)
| Leg | BI Q2-2026 (USDm) | IMF raw OBS_VALUE (USD) | IMF USDm (raw / 1e6) | Absolute magnitude residual (USDm) | Signed decision |
|---|---:|---:|---:|---:|---|
| Assets / A_NFA_T | -1,488 | +1,487,605,237.21664 | +1,487.605237 | 0.394763 | REVIEW — sign conflict |
| Liabilities / L_NIL_T | +11,440 | +11,440,221,641.9221 | +11,440.221642 | 0.221642 | PASS |

BI table precision is whole USD million; half-unit display-rounding bound is ±0.5 USDm. Both absolute-magnitude residuals are within that bound. The liability sign and magnitude match at the BI display precision. Asset magnitude matches within rounding but the sign differs: BI reports -1,488 while IMF A_NFA_T is +1,487.605237 USDm. Do not flip the sign merely to force agreement. BI's table note identifies temporary status but does not itself document the exact A_NFA_T sign transformation. An explicit concept/sign crosswalk and vintage bridge are still required.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| IDN in existing 63-country Q2 both-leg cohort | PASS |
| Existing IMF exact-key receipts and 46/46 broad-key matches | PASS |
| BI official detailed Q2 portfolio assets/liabilities table | PASS |
| BI Q2 very-temporary vintage identified | PASS |
| Liability signed/magnitude comparison | PASS at rounded precision |
| Asset magnitude comparison | PASS at rounded precision only |
| Asset sign/direction mapping | REVIEW / NOT_RESOLVED |
| IDN full dual-leg national validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## 5. Next exact action
Retrieve the Bank Indonesia table's detailed methodology/metadata explaining asset transaction sign and exact BPM6 mapping to IMF A_NFA_T; identify whether the BI Q2** vintage has subsequent revisions and whether an exact same-vintage detailed series is available. Do not infer sign mapping from aggregate financial-account balance or from IIP stocks. If no official explicit crosswalk is available, preserve IDN as PARTIAL and move to the next eligible country in the same fixed cohort.

## Protected invariants
No netting, aggregation, imputation, forward-fill, synthetic observations, silent sign reversal, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
