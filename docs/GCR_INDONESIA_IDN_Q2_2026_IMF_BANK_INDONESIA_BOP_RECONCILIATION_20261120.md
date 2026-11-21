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


## Continuation 185 addendum — official BPM5-to-BPM6 sign crosswalk resolved (2026-11-21)
- The previously unresolved asset sign question is resolved by Bank Indonesia's own official BOP metadata: although compiled with BPM6 concepts, published financial-account asset/liability sides remain presented under BPM5 as positive inflow/credit and negative outflow/debit (Section 4.3, official metadata updated July 2024).
- The IMF BPM6 Compilation Guide Table 8.10 establishes that BPM5 increases in assets are negative debits, while BPM6 increases in assets are positive; liability increases are positive under both conventions. Thus BI asset sign is reversed for comparison with IMF A_NFA_T; liability sign is retained for L_NIL_T. This is a source-defined convention bridge, not an inferred or residual-tuned adjustment.
- After this documented mapping, BI Q2-2026 asset +1,488 USDm vs IMF +1,487.605237 USDm gives absolute residual 0.394763 USDm; liability +11,440 vs IMF +11,440.221642 USDm gives residual 0.221642 USDm. Both are within BI's ±0.5 USDm whole-million display-rounding bound.
- The asset-sign gate and both numeric rounding checks are now PASS. Full IDN dual-leg national validation remains PARTIAL / NOT PASS because BI marks Q2 2026 as **Very Temporary** and exact BI↔IMF same-vintage identity / subsequent revision bridge remains NOT_ESTABLISHED. Aggregate remains NOT_AUTHORIZED.
- Detailed C185 report: `docs/GCR_INDONESIA_IDN_Q2_2026_BI_BPM5_TO_IMF_BPM6_SIGN_CROSSWALK_CONTINUATION185_20261121.md` (commit d7c62b821f7b7cb439c46cbc691eb674924b7099).


## Continuation 186 superseding national-vintage addendum (2026-11-21)
- The C185 sign mapping remains correct, but the older BI Q2** values in this base report are superseded for current national comparison by Bank Indonesia's Q3-2026 BOP report published 20-Nov-2026.
- Latest official BI Q2 provisional portfolio legs: assets -1,466 USDm; liabilities +11,399 USDm; total +9,934 USDm (PDF Table 7 p.37). BI Box 1 p.28 says Q1–Q2 2026 portfolio data were updated due to LLD and ULN updates.
- Reusing the IMF snapshot retrieved 19-Nov-2026 and applying the established BPM5→BPM6 bridge gives latest BI mapped values +1,466 and +11,399 versus IMF +1,487.605237 and +11,440.221642 USDm. Residuals +21.605237 / +41.221642 USDm exceed ±0.5 rounding. Same-vintage identity NOT_ESTABLISHED; overall PARTIAL / NOT PASS.
- See C186 report `docs/GCR_INDONESIA_IDN_Q2_2026_BI_NOV2026_REVISION_VINTAGE_RECHECK_CONTINUATION186_20261121.md`. Aggregate NOT_AUTHORIZED.
