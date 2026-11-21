# Uzbekistan UZB — Q2-2026 CBU/IMF portfolio dual-leg reconciliation (Continuation 123)
Date: 2026-11-21 (Asia/Kolkata)

## Decision
The official Central Bank of Uzbekistan quarterly BOP dataset exposes separate portfolio investment asset and liability rows through 2026-Q2. Its Q2-2026 values are assets **USD 0.01m** and liabilities **USD 1,960.49m**. The existing archived IMF panel contains exact UZB Q2 rows. Under the previously validated bounded display OBS_VALUE/1,000,000, IMF values are assets **USD 0.009793617m** and liabilities **USD 1,960.492268m**. Residuals are +USD 0.000206m and -USD 0.002268m, both within ±USD 0.005m (half of the BCU dataset's 0.01m display unit). Numeric dual-leg comparison PASS at displayed precision.

However, BCU's downloadable XLSX page says “million USD, end of period” while presenting a Balance of Payments table with financial-account transaction categories. BCU's GDDS metadata separately confirms quarterly BOP compilation and BPM6, but the specific time-basis note in the XLSX preview should be confirmed from the underlying workbook/methodological notes. The BCU dataset update date is 29-Sep-2026; the archived IMF broad CSVs were retrieved 19-Nov-2026. These are not matched vintage timestamps. Therefore UZB national numeric dual-leg comparison is PASS at published precision; period-basis clarification and same-vintage equivalence remain PARTIAL / NOT_ESTABLISHED; aggregate NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate rejection
- Re-fetched Master Continuity & Acceptance Ledger: `docs/PRECISION_WIRES_V11_3_CONTINUITY_ACCEPTANCE_LEDGER.md`, pre-task blob SHA `26dd48d4660851a15f97c9aa2986fd21e50846f3`.
- Re-fetched GCR Master Priority Queue: `docs/GCR_MASTER_PRIORITY_QUEUE_AND_ZAF_Q2_2026_SOURCE_MAPPING_20261120.md`, pre-task blob SHA `75aefdf595a1ef60b0535963a5cddc876b10d7e5`.
- Reused immutable cohort report `docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md`; UZB follows URY in fixed order.
- Scoped repository searches for UZB/Uzbekistan Q2-2026 national dual-leg report returned no prior dedicated country report. No IMF re-query, no cohort rebuild, and no repeated PASS country work.
- Reused archived IMF normalized panel Git blob SHA `2a8db2878cac6323bbad74ffa4035dc70e5e6b98`.

## 2. Official national source — CBU
- Issuer: Central Bank of the Republic of Uzbekistan.
- Official quarterly BOP dataset: https://cbu.uz/en/statistics/e-gdds/data/127982/
- Dataset page update timestamp: **29-Sep-2026 11:21**; XLSX size shown as 70.2 KB.
- The period header explicitly runs 2005-Q1 through 2026-Q2. The row labels include “Portfolio investment: assets” and “Portfolio investment: liabilities” as separate entries within section C, Financial account.
- Unit annotation in the page preview: “million USD, end of period”. Preserve this literal source annotation; the underlying workbook bytes were not acquired, so the phrase's exact meaning for the BOP transaction rows has not yet been resolved.
- The Q2-2026 column is the final period column in the preview. The corresponding portfolio rows report:
  - Portfolio investment: assets = **0.01 million USD**.
  - Portfolio investment: liabilities = **1,960.49 million USD**.
- The official H1-2026 review release (29-Sep-2026) reports net portfolio investment inflows of around USD 2 billion over the first half-year, providing broad consistency context but not a replacement for the Q2 separate legs: https://cbu.uz/en/press_center/releases/4616748/
- The H1 release states it is prepared in accordance with IMF BPM6 and the External Debt Statistics Guide.
- Do not use IIP stocks to replace BOP flows.

## 3. Official national metadata / revision policy
- Official Uzbekistan GDDS-DQAF BOP metadata PDF: https://cbu.uz/sdmx/metadata/UZB_GDDS_DQAF_EXT_BOP00_Balance%20of%20payments.pdf
- It states the Central Bank's Foreign Exchange Regulation and Balance of Payments Department compiles BOP under IMF BPM6; all known international transactions are covered and no known coverage exceptions are stated.
- Recording basis: accrual basis with some adjustments.
- BOP compiled and published quarterly.
- Revision policy: BOP data can be revised each quarter when a new publication is issued, depending on availability of new information; revisions are indicated in the publication with explanations.
- The metadata source-data list names customs/central bank/airline/border surveys for trade, state statistics and service-provider sources for services, and debt/register/bank correspondent-account sources for other components. It does not explicitly describe portfolio-investment source collection in the inspected excerpt; do not invent a portfolio-specific source map.
- The current Q2 data page's own revision note says the retrospective revision concerned service imports and primary/secondary income from 2020-Q1 through 2026-Q1. It does not state a portfolio-investment revision for those periods.

## 4. Existing archived IMF exact Q2 observations — no re-query
- Normalized panel: `docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv`, Git blob SHA `2a8db2878cac6323bbad74ffa4035dc70e5e6b98`.
- Dataflow IMF.STA:BOP(21.0.0); DSD IMF.STA:DSD_BOP(24.0.0); indicator P_F; frequency Q; unit USD; entries A_NFA_T and L_NIL_T.
- Exact UZB 2026-Q2 rows:
  - A_NFA_T raw OBS_VALUE = **9793.61706018728**, SCALE=6, PRECISION=6; source CSV SHA-256 `677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e`.
  - L_NIL_T raw OBS_VALUE = **1960492267.78624**, SCALE=6, PRECISION=6; source CSV SHA-256 `713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba`.
- These raw values and SCALE remain unchanged. The comparison display OBS_VALUE/1,000,000 is a derived presentation field, not a mutation or universal scale rule.

## 5. Numeric comparison
| Leg | CBU Q2 2026 (USDm) | IMF raw OBS_VALUE | IMF derived display (USDm) | CBU−IMF residual (USDm) |
|---|---:|---:|---:|---:|
| Portfolio assets | 0.01 | 9,793.61706018728 | 0.009793617060 | +0.000206382940 |
| Portfolio liabilities | 1,960.49 | 1,960,492,267.78624 | 1,960.492267786240 | -0.002267786240 |

- BCU preview reports two decimal places in USD millions; half-unit rounding tolerance = ±0.005 USDm.
- Both leg residuals are within ±0.005 USDm. Numeric dual-leg comparison PASS at the displayed precision.
- The implied asset-minus-liability net is approximately -USD 1,960.48m from the BCU legs; this is arithmetic only, not a separately captured BCU net row.

## 6. Gate matrix
| Check | Status |
|---|---|
| UZB in immutable 63-country Q2 cohort | PASS |
| No prior dedicated UZB report found in scoped repo search | PASS (scoped search only) |
| Official CBU quarterly BOP dataset located | PASS |
| Q2-2026 period and separate portfolio legs | PASS |
| BCU assets / liabilities values captured from page preview | CAPTURED |
| BCU page update date | 29-Sep-2026 11:21 |
| BCU unit annotation “million USD, end of period” | CAPTURED; meaning for BOP flow rows REVIEW |
| UZB BPM6 / quarterly / accrual metadata | PASS |
| UZB quarterly revision policy | PASS |
| Exact IMF Q2 rows reused | PASS |
| Asset numeric comparison | PASS within ±0.005 USDm |
| Liability numeric comparison | PASS within ±0.005 USDm |
| Same-vintage alignment | NOT_ESTABLISHED |
| Exact underlying BCU XLSX bytes / size / SHA-256 | NOT_CAPTURED |
| Full UZB validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## 7. Next exact action
- Do not repeat the BCU page text extraction or IMF panel retrieval.
- Obtain the actual BCU XLSX bytes through a byte-preserving supported route; archive exact URL, retrieval timestamp, byte count and SHA-256. Inspect workbook headers/notes to resolve “end of period” wording, sign and flow/stock basis.
- Compare the workbook's Q2 portfolio rows with the Q2 BOP report/analytical presentation and verify the current dataset vintage against BCU's quarterly revision policy.
- If exact workbook retrieval or vintage metadata remains unavailable, keep UZB PARTIAL / NOT PASS and advance to VNM only after checking the immutable roster and prior country reports. No IMF re-query.

## 8. Protected constraints
₹0; official/free sources only. No synthetic values, no inferred sign/scale transform, no stock-as-flow, no net-to-leg back-solving, no cross-country vintage assumption, no IMF re-query, no cohort rebuild, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Sources
- CBU Q2-2026 BOP dataset and XLSX preview: https://cbu.uz/en/statistics/e-gdds/data/127982/
- CBU H1-2026 BOP/IIP/external debt release: https://cbu.uz/en/press_center/releases/4616748/
- CBU Uzbekistan GDDS-DQAF BOP metadata: https://cbu.uz/sdmx/metadata/UZB_GDDS_DQAF_EXT_BOP00_Balance%20of%20payments.pdf
- Archived IMF normalized panel: `docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv`.
- Immutable Q2-2026 cohort: `docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md`.
