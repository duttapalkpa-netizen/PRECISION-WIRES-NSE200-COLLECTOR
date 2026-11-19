# GCR — WEO G200 EMDE BOP Quarterly Coverage QA (2026-11-19)

## Decision
**Panel integrity PASS; aggregate admission BLOCKED.** This audit independently reconciles the entire normalized panel to both raw IMF source CSVs and quantifies missingness. It does not calculate an EMDE aggregate or net flow.

## Universe and panel
- Membership edition: IMF WEO October 2026, group G200 (Emerging Market and Developing Economies), 154 unique members.
- IMF BOP Dataflow: IMF.STA:BOP(21.0.0); DSD: IMF.STA:DSD_BOP(24.0.0).
- Indicator P_F; entries A_NFA_T and L_NIL_T; quarterly, requested window 2015-Q1–2026-Q3.
- Normalized observations: 9,299; unique keys: 9,299; duplicates: 0.
- Raw source non-empty rows: 9,299; exact key matches: 9,299; source attribute columns compared: 30; attribute mismatches: 0.
- The raw-to-normalized comparison is 9,299/9,299 exact rows and 278,970 source-field cell comparisons; all matched.

## Coverage results
- Country-entry pairs with data: 225/308 (73.05%); no-data pairs: 83.
- Countries with both asset and liability legs: 111/154.
- One-sided: 3 (DZA and ETH have assets only; ZWE has liabilities only).
- No observations for either leg: 40/154.
- Complete 47/47 quarter series: 4; partial series: 221.
- Series with internal gaps: 13; internal missing quarters: 71.
- Latest-period distribution (series, not countries): {'2015-Q4': 2, '2016-Q4': 2, '2020-Q3': 2, '2021-Q1': 2, '2023-Q2': 2, '2024-Q2': 2, '2024-Q4': 6, '2025-Q1': 4, '2025-Q2': 2, '2025-Q4': 27, '2026-Q1': 46, '2026-Q2': 124, '2026-Q3': 4}.
- 2026-Q3: only 2 countries report both legs (Brazil and Pakistan); latest coverage is asynchronous.

## Source attributes
- DERIVATION_TYPE: {'O': 9299}. All 9,299 observations are code O (Reported official data).
- UNIT: {'USD': 9299}; only USD was returned by the all-units wildcard query.
- SCALE: {'6': 9299}; official IMF concept scheme `IMF:CS_MASTER_SYSTEM(1.0.2)` names it “Scale”; its Arabic label `عدد الخانات العشرية` translates to “number of decimal places”. The concept has no English description and no referenced codelist. In the BOP DSD it is a series-level attribute, distinct from the separate `UNIT` dimension and from legacy `UNIT_MULT`; do not multiply values by 10^6 or round them based on this field. Raw values and SCALE=6 are preserved.
- PRECISION: {'6': 9119, '': 180}; blanks preserved, not filled.
- No forward-fill, zero substitution, synthetic observations, currency conversion, rescaling or aggregation.

## Acceptance
- Raw-source-to-normalized panel integrity: PASS.
- WEO G200 to BOP country code mapping: 154/154 PASS (separately validated).
- Country/period coverage: PARTIAL; must remain visible at country × entry × quarter level.
- Full EMDE aggregate: BLOCKED / NOT_AUTHORIZED. 43/154 members lack at least one leg, reporting is asynchronous, only two members have 2026-Q3 data, and 13 series have internal gaps.
- SCALE label semantics are partially clarified (decimal-place scale, not proven unit multiplier), but no formal English definition/codelist or rounding rule exists; keep it as metadata and apply no transformation. Sign convention, FX policy and point-in-time vintage history remain open. Do not calculate net inflow or use this panel in a backtest/production signal until these are resolved.

## Files
- `coverage_by_country_entry_detailed.csv`: all 308 member-entry combinations with every missing quarter.
- `country_readiness.csv`: both-leg readiness for all 154 members.
- `quarterly_country_coverage.csv`: reporting breadth by quarter.
- `summary.json`: machine-readable audit totals.

## Invariants
₹0; free official sources only; no synthetic data; no fabricated timestamps; no paid APIs. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. UNKNOWN is not PASS.
