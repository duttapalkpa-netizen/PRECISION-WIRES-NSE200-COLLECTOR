# GCR — WEO G200 EMDE BOP Quarterly Coverage QA (2026-11-19)

## Decision
**Panel integrity PASS; aggregate admission BLOCKED.** This independent audit reconciles the full normalized panel against both raw IMF source CSVs and quantifies missingness. It does not calculate an EMDE aggregate or net flow.

## Universe and panel
- Membership edition: IMF WEO October 2026, group G200, 154 unique members.
- IMF BOP Dataflow: IMF.STA:BOP(21.0.0); DSD: IMF.STA:DSD_BOP(24.0.0).
- Indicator P_F; entries A_NFA_T and L_NIL_T; quarterly, 2015-Q1–2026-Q3.
- Normalized observations: 9,299; unique keys: 9,299; duplicates: 0.
- Raw source non-empty rows: 9,299; exact key matches: 9,299; 30 source attribute columns compared; 278,970 source-field cell comparisons; mismatches: 0.
- Raw-to-normalized exact rows and attributes: 9,299/9,299.

## Coverage results
- Country-entry pairs with data: 225/308 (73.05%); no-data pairs: 83.
- Countries with both asset and liability legs: 111/154.
- One-sided: 3 (DZA and ETH assets only; ZWE liabilities only).
- No observations for either leg: 40/154.
- Complete 47/47 quarter series: 4; partial series: 221.
- Series with internal gaps: 13; internal missing quarters: 71.
- Only two countries (Brazil and Pakistan) have both legs at 2026-Q3. Coverage is asynchronous.
- 2026-Q3 latest-period distribution across 308 series: 4 series; 2026-Q2: 124 series.
- No forward-fill, zero substitution, synthetic observations, rescaling, FX conversion or aggregation.

## Source attributes
- DERIVATION_TYPE: O for all 9,299 observations.
- UNIT: USD for all 9,299.
- SCALE: 6 for all 9,299; preserved.
- PRECISION: 6 for 9,119; blank for 180; blanks preserved.
- STATUS blank for all observations; blanks preserved.

## Acceptance
- Raw-source-to-normalized panel integrity: PASS.
- WEO G200 to BOP country code mapping: 154/154 PASS.
- Country/period coverage: PARTIAL; visible at country × entry × quarter level.
- Full EMDE aggregate: BLOCKED / NOT_AUTHORIZED. 43/154 members lack at least one leg; only two countries have both legs at 2026-Q3; 13 series have internal gaps.
- SCALE is partially clarified as a decimal-place attribute, but no formal English definition/codelist or rounding rule exists; sign convention, FX policy and point-in-time vintage history remain open. Do not calculate net inflow or use this panel in backtests/production until resolved.

## Evidence
- Coverage QA run 44475665715 SUCCESS; artifact 14506017682; ZIP SHA-256 `e900f76a31589f83c19d49eefc3720919a91b83e118d244921adf1ff0f948f4a`.\n- SCALE concept run 44475665715 SUCCESS; artifact 14506356045; ZIP SHA-256 `7465214f27dddbece13f5812b49269b566b4139461da986292a65b29828cbdd2`; concept scheme raw XML SHA-256 `9ef243509d7b3edc93b5ef2326ba49c89ced79044ae38674c806d1310367420d`.
- Full detailed QA files: `docs/evidence/imf_bop_emde_20261119/coverage_qa/` (country readiness, all 308 country-entry combinations, quarterly coverage, summary).
- Panel persistence run 44475086587 SUCCESS; final main commit `13bdd96d`.
- Invariants unchanged: ₹0; free official sources only; no synthetic data; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. UNKNOWN is not PASS.
