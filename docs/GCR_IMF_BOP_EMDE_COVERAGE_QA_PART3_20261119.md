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
- SCALE code meaning is now verified: DSD_BOP SCALE enumerates IMF CL_UNIT_MULT(1.0.2); code 6 = Millions, description 10^6. The IMF API raw OBS_VALUE behaves as base-USD values in national-source crosswalks, so OBS_VALUE/1e6 matches USD-million tables in Brazil (94/94) and India (10/12; 2 REVIEW in 2026-Q1 liabilities/combined net). Preserve raw values; do not generalize numeric conversion to all EMDE countries until country-period crosswalks pass. Sign convention, FX policy and point-in-time vintage history remain open.

## Evidence
- Coverage QA run 44475665715 SUCCESS; artifact 14506017682; ZIP SHA-256 `e900f76a31589f83c19d49eefc3720919a91b83e118d244921adf1ff0f948f4a`.
- Authoritative SCALE code-list capture run 44477031402 SUCCESS; artifact 14506293939; ZIP SHA-256 `ffac629793da363b934321e00f43aaec7eabcd609bc9a029cb46356712a01858`. Targeted CS_MASTER_SYSTEM response SHA-256 `50e82604b231e9e02ba8472d46e227276acec393360e60071c980f8d5caf2768`; CL_UNIT_MULT raw XML SHA-256 `24e3ea87063cdfe091cdb0b2daa71731835fd0049661a4fffbd8f760fb45e561`.
- India RBI BPM6 crosswalk run 44477031402 SUCCESS; artifact 14505649659; ZIP SHA-256 `8db4f9536a57df1e8635855af5bb90225de0f800e6e9164bd20d99d1f355b4e2`; 10/12 comparisons PASS, 2 REVIEW.
- Full detailed QA files: `docs/evidence/imf_bop_emde_20261119/coverage_qa/`; scale codelist evidence: `docs/evidence/imf_bop_20261119/scale_unit_multiplier_authoritative/`; India crosswalk: `docs/evidence/imf_bop_20261119/india_scale_reconciliation/`.
- Invariants unchanged: ₹0; free official sources only; no synthetic data; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. UNKNOWN is not PASS.
