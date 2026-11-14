# IMF BOP 39-country annual-frequency exact-series reachability audit

Audit date: 2026-11-14 UTC
Branch: `research/imf-bop-access-audit-v1`
Dataset: `IMF.STA:BOP(21.0.0)`
DSD: `IMF.STA:DSD_BOP(24.0.0)`
Exact series: `P_F` (portfolio financial flows), `USD`; assets `A_NFA_T`, liabilities `L_NIL_T`; frequency `A`.
Observation window evaluated: 2000–2025 inclusive.
Target set: the exact 39 BOP country codes classified as having no non-empty quarterly observations across the previously audited 2000-Q1–2014-Q4 and 2015-Q1–2025-Q4 windows. The 39-code set is loaded from the prior 43-row cross-period matrix, not hand-entered.

## 1. Verified execution and provenance

- Workflow: `.github/workflows/imf_bop_39_country_annual_frequency_audit.yml`.
- Final corrected workflow commit: `f5c535c0c7635b81034f18ad185de37b24479050`.
- Run #43630656519 — SUCCESS; job #132556279712 — SUCCESS.
- Artifact #14128182046; ZIP size 134,541 bytes; SHA-256 `058ae62904bec701959175076d3d2aa9de20f402eb3425083bbfad2d36accc12`.
- Assets response: HTTP 200; 360,608 bytes; SHA-256 `711431c957199292cfb37e884a3e9344e7e519e23e9bb4baea2ff9f5523addfc`; 211 series across the complete response.
- Liabilities response: HTTP 200; 352,754 bytes; SHA-256 `a256a5f5baaef80f48e7d3747c39db80d644078b896abe49a5190f21003b60aa`; 208 series across the complete response.
- The endpoint's annual TIME_PERIOD dimension is populated only when the complete annual response is requested. An earlier server-side annual time filter returned an empty TIME_PERIOD dimension; that diagnostic failed closed and was not used as evidence. The corrected workflow requests the full exact annual series response and filters actual observations locally to 2000–2025.
- Parser verifies the exact series dimension order COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY; checks exact account/indicator/unit/frequency keys; rejects invalid indexes, null/non-finite values and duplicate years; and distinguishes non-empty series, empty series keys and no returned series keys.
- Artifact ZIP downloaded and inspected. Both 39-row matrices and raw responses are retained in the artifact.

## 2. Results for the 39 quarterly-gap reporters

| Metric | Assets annual A_NFA_T | Liabilities annual L_NIL_T |
|---|---:|---:|
| Target countries | 39 | 39 |
| Countries with ≥1 annual observation in 2000–2025 | 33 | 31 |
| Empty series key (no observations) | 5 | 4 |
| No series key returned | 1 | 4 |
| Annual observation coverage | 84.62% | 79.49% |

Combined cross-side result:
- 31/39 have non-empty annual observations on both assets and liabilities (79.49%).
- 2/39 have assets annual observations only: `FSM`, `SSD`.
- 0/39 have liabilities annual observations only.
- 6/39 have no non-empty annual observations on either side: `CAF`, `ERI`, `GNQ`, `SOM`, `TCD`, `TKM`.
- Of those six, five have empty series keys in at least one side; `ERI` has no series key returned on either side. An empty key is not an observation.

The 31 countries with annual observations on both sides are:
`ARE, ATG, BEN, BFA, BRB, CIV, COG, COM, DMA, GAB, GNB, GRD, IRN, KEN, KNA, LBY, LCA, MDV, MHL, MLI, MWI, NER, NRU, OMN, PLW, SEN, SLE, SYR, TGO, TUV, VCT`.

## 3. Interpretation — important distinction

This audit establishes **annual-frequency data reachability** for the exact BOP portfolio-flow account/indicator/USD combination. It does not establish:
- quarterly-frequency eligibility or quarterly completeness;
- full 2000–2025 continuity (some countries have only one or a few years);
- formal reporter eligibility or a legal/statistical reporting obligation;
- that a missing series means the country is ineligible, non-reporting, suppressed, or has an economic zero;
- that annual observations may be substituted into the quarterly backtest or aggregated with quarterly data.

The annual dimension is distinct from quarterly. The 39 countries were selected because the prior quarterly tests returned no observations; this audit shows that this absence is frequency-specific for most of the target set. Keep annual and quarterly series in separate coverage classes.

## 4. Gate disposition

| Gate | Status |
|---|---|
| Annual exact-series acquisition (assets and liabilities) | PASS |
| Exact 39-country target set reconciled to prior quarterly matrix | PASS |
| Annual 39-row assets matrix | PASS |
| Annual 39-row liabilities matrix | PASS |
| Annual non-empty observations on both sides | 31/39 observed; not a completeness PASS |
| Annual assets-only reporters | 2 (FSM, SSD) |
| Annual no non-empty observations on either side | 6 (CAF, ERI, GNQ, SOM, TCD, TKM) |
| Quarterly reporter eligibility for 39 | UNKNOWN |
| Quarterly coverage acceptance | NOT PASS |
| EMDE aggregation | BLOCKED |

The 39-country quarterly UNKNOWN state is not promoted to PASS/FAIL by this annual-frequency result. No aggregation, annual-to-quarterly conversion, scaling, interpolation, forward-fill, or synthetic observations were performed.

## 5. Diagnostic history and error control

- Run #43630501862 failed closed because a server-side annual time filter produced no annual TIME_PERIOD dimension. It did not produce a coverage decision.
- Run #43630564954 parsed the complete response but its first implementation did not apply the intended local year filter to the per-country period list. It is superseded and not used for the 2000–2025 counts.
- Run #43630618730 failed at Python syntax validation after a newline-escaping error. It did not produce coverage evidence.
- Final corrected Run #43630656519 applies the 2000–2025 local filter to each observation and passes. Earlier diagnostic artifacts/runs remain preserved; none is relabelled as a valid final result.

## 6. Next highest-value action

For the 31 both-side annual reporters and the 2 assets-only reporters, inspect annual observation attributes and year continuity/gaps; do not assume all annual series are complete. For the six with no non-empty annual observations, inspect exact country-specific dataflow/series availability and official country metadata notes if publicly accessible. For the 39-country quarterly gate, annual reachability cannot replace the missing quarterly evidence. Keep all formal eligibility causes UNKNOWN unless an authoritative reporter-specific rule is found.

## 7. Protected invariants

₹0 spend; public official IMF API only; no credentials, authentication bypass, paid services, external contact, synthetic rows/timestamps, aggregation, PR merge, or production integration. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56 × 12), engines A–E, and Hard Gate unchanged.
