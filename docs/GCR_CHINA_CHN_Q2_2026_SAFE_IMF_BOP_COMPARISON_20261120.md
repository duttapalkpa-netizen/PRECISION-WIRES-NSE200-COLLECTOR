# GCR China (CHN) Q2-2026 — SAFE vs IMF Portfolio Flow Comparison
Date: 2026-11-20
Status: PARTIAL / NOT PASS — liability magnitude reconciles within publication rounding; asset magnitude reconciles but sign/direction does not. No national dual-leg validation PASS.

## Progress log
- Preflighted the Master Continuity Ledger, GCR priority queue, ZAF reconciliation, IMF EMDE panel and Q2 dual-leg cohort.
- Reused existing 63-country Q2-2026 both-leg cohort and existing 12-country exact-key IMF receipt. CHN was already in that sample. No roster/panel rebuild or new IMF requests.
- Excluded prior PASS work: IMF DSD capture, 154-member WEO membership, 9,299-row panel QA, 12-country exact-key QA, Brazil/India/Nigeria checks, and completed ZAF source extraction.
- Selected CHN because it is a large EMDE market in the fixed Q2 cohort and SAFE has a dated, direct USD-denominated national BOP release.

## 1. Existing IMF exact-key evidence
Receipt: `docs/evidence/imf_bop_emde_20261119/exact_sample_checks/summary.json`.
Run 44474458684; artifact 14505009889; ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`.
- CHN A_NFA_T exact request: HTTP 200; retrieved 2026-11-19T06:45:16.487611Z; raw CSV SHA-256 `8130166c964097628d9e686dd98a4eb281c4b6e00565cd46881e593f620ca7e1`.
- CHN L_NIL_T exact request: HTTP 200; retrieved 2026-11-19T06:45:16.914525Z; raw CSV SHA-256 `bdccef2d71d421304fa05f9db86557e896cd6b9db573db3e759d9f5eb8a20cc0`.
- Q2-2026 raw IMF A_NFA_T = +48,794,459,103.55 USD; L_NIL_T = +43,286,600,714.23 USD. Both series end at 2026-Q2. SCALE=6 (Millions) is retained as a separate source attribute; displayed values below divide raw OBS_VALUE by 1,000,000.

## 2. Official SAFE national source
SAFE release: “SAFE Releases China's Balance of Payments for the Second Quarter and for the First Half 2026”, index 000014453-2026-0068, dispatch date 2026-09-29.
URL: https://www.safe.gov.cn/en/2026/0929/2458.html
Table: “Abridged Balance of Payments, Q2 2026”; columns include USD 100 million. BPM6 source. Relevant lines:
- Line 30 Portfolio Investment: USD -55 × 100m = -USD 5.5bn.
- Line 31 Assets: USD -488 × 100m = -USD 48.8bn.
- Line 32 Liabilities: USD +433 × 100m = +USD 43.3bn.
- Identity: -488 + 433 = -55 (exact at published precision).
- SAFE note 2 says credit is positive, debit negative, and difference is their sum. Note 6 says rounded-off numbers; note 8 says BOP data is regularly revised.
- Q2 release is USD-denominated directly; no FX conversion was needed. SAFE's RMB and SDR columns are converted from the USD quarter data using period-average rates, but are not used here.

## 3. Magnitude comparison and sign assessment
| Entry | IMF raw / 1e6 (USDm) | SAFE published (USDm) | Absolute magnitude residual (USDm) | Signed comparison |
|---|---:|---:|---:|---|
| A_NFA_T / SAFE Portfolio Assets | +48,794.459104 | -48,800 | 5.540896 | SIGN CONFLICT / REVIEW |
| L_NIL_T / SAFE Portfolio Liabilities | +43,286.600714 | +43,300 | 13.399286 | Same sign; magnitude within rounding |

SAFE table precision is USD 100 million = USD 0.1bn increments; half-unit rounding bound = ±USD 50 million (±50 USDm). Both absolute-magnitude residuals are inside that display-rounding bound. The liability comparison is consistent in both sign and magnitude at the published precision. The asset comparison is not: SAFE reports a negative asset balance while IMF A_NFA_T is positive. Do not reverse the sign merely to force agreement. The source's credit/debit note alone does not establish an IMF-equivalent sign transformation for this asset line; exact source concept mapping and revision vintage are required.

## 4. Acceptance matrix
| Gate | Status |
|---|---|
| CHN in existing Q2-2026 both-leg cohort | PASS |
| IMF exact-key asset/liability receipts | PASS |
| SAFE official Q2-2026 USD BOP release retrieved | PASS |
| SAFE portfolio line identity (-488 + 433 = -55) | PASS |
| Liability signed/magnitude check | PASS at rounded publication precision |
| Asset magnitude check | PASS at rounded publication precision only |
| Asset sign/direction mapping | REVIEW / NOT_RESOLVED |
| CHN full dual-leg national validation | PARTIAL / NOT PASS |
| 63-country EMDE aggregate | NOT_AUTHORIZED |

## 5. Next exact action
Do not promote CHN to a fully validated country. Retrieve the detailed time-series data linked from SAFE Data and Statistics (not the end-June IIP stock table); inspect the underlying BPM6 portfolio transaction series and its asset sign convention/revision vintage. Compare the exact Q2 asset and liability rows against IMF. If no public detailed export or concept metadata can be recovered through the official route, preserve CHN as PARTIAL and move to the next largest unvalidated country in the fixed cohort. Do not substitute IIP stocks for BOP flows.

## Protected invariants
No netting, aggregate, imputation, forward-fill, synthetic observations, silent sign reversal, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
