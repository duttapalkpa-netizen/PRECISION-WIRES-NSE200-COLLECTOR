# GCR — IMF BOP EMDE Portfolio Flows Panel (Part 2)
Date: 2026-11-19 (UTC capture 06:43–06:45)
Status: acquisition PASS; 12-country exact-key independent reconciliation PASS; full EMDE aggregate BLOCKED by incomplete coverage.

## 1. Executive result
- Official WEO October 2026 workbook was downloaded anonymously (HTTP 200). Sheet `Country Group Composition`, group code `G200`, yielded exactly 154 unique Emerging Market and Developing Economies (EMDE) country codes.
- Official IMF BOP country codelist `IMF.STA:CL_BOP_COUNTRY(1.0.0)` returned HTTP 200. All 154 WEO member codes matched; missing/unmapped codes = 0.
- IMF public SDMX 3.0 BOP data endpoint returned two quarterly CSV datasets for 2015-Q1 through 2026-Q3, one for portfolio investment asset flows and one for liability flows. No credentials/cookies/API key were used.
- Captured all reported units (the response contained USD only); no FX conversion, scale conversion, aggregation, fill or synthetic observation was performed.

## 2. Exact data definition
- Dataset/dataflow: `IMF.STA:BOP(21.0.0)`
- DSD: `IMF.STA:DSD_BOP(24.0.0)`
- Indicator: `P_F` — Portfolio investment, Total financial assets/liabilities.
- Asset entry: `A_NFA_T` — Assets, Net acquisition of financial assets.
- Liability entry: `L_NIL_T` — Liabilities, Net incurrence of liabilities.
- Frequency: quarterly (`Q`).
- Period request: 2015-Q1 to 2026-Q3.
- Country set: WEO October 2026 `G200`, 154 members.
- Unit dimension wildcard returned `USD` only. The raw attribute `SCALE=6` and `PRECISION=6` are retained exactly. No interpretation of SCALE as multiplier, no power-of-ten conversion.

## 3. Acquisition and coverage
Workflow: [44474218174](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44474218174)
Artifact: 14505862034; ZIP size 5,997,777 bytes; ZIP SHA-256 `1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f`.
- WEO workbook: 5,480,592 bytes; SHA-256 `2aa4f70a05931197b41ed7e0202dc56eee8d816858ac14521e4f8f5dbc38696c`.
- IMF BOP country codelist XML: 5,737,234 bytes; SHA-256 `190c0ab3196a85bba890e2fd0cf40eebda654de2eb8e7d1f16c9644572d59f39`.
- Asset raw CSV: 484,139 bytes; SHA-256 `677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e`; 4,681 nonempty observations, 45 empty rows, 113 countries.
- Liability raw CSV: 451,290 bytes; SHA-256 `713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba`; 4,618 nonempty observations, 43 empty rows, 112 countries.
- Normalized panel: 9,299 observations (4,681 assets + 4,618 liabilities), 9,299 unique keys, 0 duplicates, 114 distinct countries with at least one entry.
- Country-entry coverage: 225 of 308 pairs (154 × 2) have observations = 73.05%.
  - Both asset and liability entries present: 111 countries.
  - No observations for either entry: 40 countries.
  - Asset only: DZA (22 observations), ETH (4 observations).
  - Liability only: ZWE (36 observations).
  - Thus 43 countries do not have both required flow legs; they cannot be silently included in a complete net-flow panel.
- Per-country time coverage is heterogeneous. Most countries end at 2026-Q2, only two have 2026-Q3; other country series end earlier (some as early as 2015-Q4/2020/2021/2024/2025). Do not assume synchronized latest-quarter coverage.
- Coverage matrix retains each country's observation count and first/last period. Empty rows remain visible in raw CSVs; normalized panel contains only nonempty observations. No forward-fill or gap imputation.

## 4. Independent exact-key cross-check
Workflow: [44474458684](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44474458684)
Artifact: 14505009889; ZIP size 26,684 bytes; ZIP SHA-256 `588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7`.
- Stratified sample: ARG, BGD, BRA, CHN, IDN, IND, MEX, NGA, POL, SAU, TUR, ZAF.
- 12 countries × 2 entries = 24 exact-key GET requests.
- HTTP 200: 24/24; exact series validation PASS: 24/24.
- Exact observation rows: 1,106; exact-vs-multi-country raw values AND all source attributes match: 1,106/1,106.
- Missing from broad panel: 0; attribute/value mismatches: 0; failed series: 0.
- Each exact sample series matched the multi-country panel period-by-period.

## 5. Interpretation limits and rejected shortcuts
- This panel is portfolio-investment financial-account flows, not CPIS/PIP positions.
- Assets and liabilities remain separate. BPM6 financial account describes net acquisition of financial assets and net incurrence of liabilities; do not treat the two entries as same-direction inflows. No derived net inflow has been calculated.
- WEO `G200` is a versioned analytical group membership. It is not a substitute for an independently defined investable-market universe, and membership must remain versioned.
- The panel has 111/154 countries with both legs and 40/154 with neither; full 154-country EMDE aggregation is therefore NOT_AUTHORIZED by this evidence.
- No weighting, aggregation, FX conversion, unit scaling, or cross-country sum has been run. No observation with blank `OBS_VALUE` was converted to zero.
- `P_MV` remains rejected for this BOP flow extraction: its prior exact tests returned empty observations. `P_F` is the tested flow indicator.
- The separate SDMx Global Registry `IMF:BOP(2.6.0)` DSD is not assumed equivalent to IMF Data Portal `IMF.STA:DSD_BOP(24.0.0)`. No schema crosswalk has been silently applied.

## 6. Durable GitHub archive
Evidence directory: `docs/evidence/imf_bop_emde_20261119/`
- `emde_membership.csv`
- `coverage_by_country_entry.csv`
- `emde_portfolio_flows.csv`
- `raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`
- `raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`
- `summary.json`, `provenance.json`, `source_artifact_receipt.json`
- `exact_sample_checks/summary.json` plus all 24 exact-key raw CSVs.
Archive commit: `a6eb5865c0a77d6bdaf1c6a3c6925e6e1e69bdf0`.

## 7. Next acceptance gates
1. Complete source semantics for `SCALE`, `PRECISION`, `IFS_FLAG`, `DERIVATION_TYPE`, `STATUS` from the exact IMF concept scheme; do not infer multiplier from the label.
2. Determine per-country reporting currency and whether the all-USD panel is a complete USD subset or whether other currency series exist in the dataset. No conversion until exact unit metadata is verified.
3. Decide and pre-register coverage threshold for a valid EMDE aggregate; missing 43 country-entry pairs must remain explicit.
4. Compare any IMF-provided group aggregate (if available) with a country-level sum only after group membership, units, time coverage, sign conventions, and aggregation method align.
5. Align validated flows to rates/FX/volatility/benchmark returns, then build no-lookahead relative-attraction and sector transmission tests.
6. Run walk-forward tests with transaction costs and missingness gates. Until then, no production factor, no score weight, no trading admission.

## Decision
- WEO 154-member membership and BOP codelist mapping: PASS.
- Public IMF BOP flow capture for WEO EMDE members: PASS.
- 12-country / 24-series independent exact-key cross-check: PASS.
- Full EMDE panel completeness: PARTIAL (225/308 country-entry pairs; 111 countries with both legs).
- EMDE group aggregate / net-flow series: BLOCKED / NOT_AUTHORIZED.
- GCR relative-attraction formula, sector transmission, and rolling backtest: NOT_DONE.
- No Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E changes. ₹0; no paid APIs, credentials, synthetic rows or fabricated timestamps.


## 8. Source semantics and durable raw-source addendum (2026-11-19)
- Dedicated public SCALE concept route probe: run 44474593356, artifact 14505692823, ZIP SHA-256 `218bb0f75f725e44beb2250b06075ddd8796b0a0dff5bd442a5fd57ddeae519b`.
- Exact concept scheme resolved: `IMF:CS_MASTER_SYSTEM(1.0.2)`; the `SCALE` concept's CoreRepresentation points to `IMF:CL_UNIT_MULT(1.0+.0)`. The public latest codelist resolved to `CL_UNIT_MULT(1.0.2)); code `6` is labelled **Millions** (10^6). This identifies the code label but does not itself authorize applying a conversion to this panel.
- All 9,299 observations carry `SCALE=6`. Preserve `OBS_VALUE` and `SCALE` as separate raw fields. No multiply/divide by 10^6, rescaling or conversion is performed until reconciled against the IMF portal's displayed values and official national-source values for Brazil and India.
- Durable raw source addendum commit `79bfbeb3abd2a0e223ae77d2ed740727404dd112` adds the original WEO October-2026 workbook (`raw/WEOOct2026all.xlsx`) and IMF BOP country codelist XML (`raw/CL_BOP_COUNTRY.xml`) alongside the already archived normalized panel, raw observation CSVs and exact sample receipts.
- The earlier evidence archive commit `a6eb5865c0a77d6bdaf1c6a3c6925e6e1e69bdf0` remains the base archive commit.
- Full acceptance remains: acquisition PASS; membership mapping PASS; exact-key query-shape reconciliation PASS; coverage PARTIAL; scale conversion BLOCKED; BPM/revision-vintage controls NOT_DONE; EMDE aggregate BLOCKED / NOT_AUTHORIZED.

## 9. Independent WEO Appendix cross-check and final membership archive (2026-11-19)
- WEO October 2026 Database Appendix was downloaded from the official IMF dataset page and parsed independently from the workbook.
- Appendix top-level Emerging and Developing Economies list: 154 labels, 154 unique.
- Same-vintage workbook Country Group Composition G200: 154 members, 154 unique ISO3.
- Appendix-to-workbook identity crosswalk: 154/154 PASS; unmapped/ambiguous 0. All 154 workbook ISO3 codes also exist in IMF BOP CL_BOP_COUNTRY (1,727 codelist codes).
- WEO membership validation run 44474629873 / artifact 14506160317 / ZIP SHA-256 acdf014f5f19ba5e0d23dca7a8d57a4b1813b002a3274495d557f0cd05c0fbb1.
- Raw WEO workbook SHA-256 2aa4f70a05931197b41ed7e0202dc56eee8d816858ac14521e4f8f5dbc38696c; Appendix PDF SHA-256 cd4e2829d7e621d43134728bfc128547f776e909e08ef1d38b837e2d39e5ae2a.
- Durable files: docs/evidence/imf_bop_emde_20261119/weo_membership_validation/ includes raw Appendix PDF, workbook, BOP codelist, exact 154-row membership, crosswalk and validation summary. Persistence run 44475086587 SUCCESS; final main commit 13bdd96d.

## 10. Full panel missingness audit (2026-11-19)
- Independent full-panel QA run 44475089564 / artifact 14505623598 / ZIP SHA-256 5f24a529aa0d3c918d598faedeb057c39e328ff043f1f1a86fec587fc1fa8cd8.
- Raw-to-normalized comparison: 9,299/9,299 exact rows; 30 source attribute columns; 278,970 source-field cell comparisons; 0 mismatches.
- 225/308 country-entry pairs have observations (73.05%); 83 empty pairs; 111 countries have both legs; 3 are one-sided (DZA/ETH assets only; ZWE liabilities only); 40/154 have neither.
- 4 complete 47-quarter series; 221 partial series; 13 series have internal gaps totaling 71 missing quarters. Only Brazil and Pakistan have both legs through 2026-Q3. No forward-fill, zero substitution, synthetic rows, rescaling, FX conversion or aggregation.
- Coverage report: docs/GCR_IMF_BOP_EMDE_COVERAGE_QA_PART3_20261119.md; detailed QA files: docs/evidence/imf_bop_emde_20261119/coverage_qa/.
- Full EMDE aggregate remains BLOCKED / NOT_AUTHORIZED.

## 11. SCALE concept metadata resolution (2026-11-19)
- Dedicated DSD/concept/codelist capture run 44475051442 / artifact 14505852262 / ZIP SHA-256 391981ce19d89d8ccc6377580e33345a9d75adffdc3f4197c4e4c743a66e3cf3.
- SCALE concept in CS_MASTER_SYSTEM(1.0.2) enumerates CL_UNIT_MULT; code 6 = Millions (10^6). This resolves the code meaning, not whether the data API has already normalized OBS_VALUE.
- Numeric conversion remains BLOCKED: do not multiply/divide by 10^6 until direct IMF portal display and official national-source values reconcile. Preserve OBS_VALUE, UNIT=USD, SCALE=6 exactly.
- Detailed report: docs/GCR_IMF_BOP_SCALE_SEMANTICS_20261119.md. No netting or aggregate is authorized.
