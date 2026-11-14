# IMF BOP EMDE historical reach-back and cross-period reconciliation

Audit date: 2026-11-14 UTC
Branch: `research/imf-bop-access-audit-v1`
Dataset: `IMF.STA:BOP(21.0.0)`
DSD: `IMF.STA:DSD_BOP(24.0.0)`
Crosswalk: IMF WEO April 2026 EMDE list, 154 countries, exact dataset-specific BOP country codes.
Series: Portfolio financial flows (`P_F`), USD, quarterly; assets `A_NFA_T`, liabilities `L_NIL_T`.
No synthetic observations, interpolation, forward fill, aggregation, or inferred zero values.

## 1. Historical reach-back execution

- Run #43626075930: SUCCESS.
- Workflow: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43626075930
- Commit: `126d82d2b04772d09e3d4bf894a45e4cd015c536`.
- Job ID: `132542048096`; all steps SUCCESS.
- Artifact ID: `14125219608`; ZIP SHA-256 `539e34fca42394d5ae53da27d44243f7aea6c79a1631178465f351b5d8bf1157`.
- Period: 2000-Q1 to 2014-Q4 (60 quarterly periods); wildcard COUNTRY key `*`; both requests HTTP 200 and exact SDMX JSON parsing PASS.
- Assets response: 332,012 bytes; SHA-256 `93025fe023aac9d301f6799d13ada7b0f04d27703012d8b3e1373db6c5527226`; 143 total reporter series, 100/154 EMDE reporter codes present, 54 absent from this query interval, 43 non-EMDE codes.
- Liabilities response: 320,793 bytes; SHA-256 `78ffa2a1492667cc2979f357acafecb490875a80f609726838f1be5ea44b5d25`; 142 total reporter series, 99/154 EMDE reporter codes present, 55 absent from this query interval, 43 non-EMDE codes.
- Target set: exact 43 codes carried forward from the prior coverage audit: 40 common no-series codes plus DZA, ETH, ZWE. The historical query found observations for only ETH and HTI within this 43-code set, on both assets and liabilities. Thus 2/43 target reporters had observations per side (4.65%); 41/43 had no observations in 2000-Q1 to 2014-Q4 for each side. Important raw-response nuance: the historical liabilities response includes a ZWE series key with an empty observations object; this is not an observation and is not counted as reporter coverage.
- ETH: assets 28 observations, 2003-Q1 to 2009-Q4; liabilities 28 observations, same interval.
- HTI: assets 32 observations, 2004-Q4 to 2012-Q3; liabilities 32 observations, same interval.
- Both ETH and HTI observations are contiguous within their first-to-last reported spans; this does not imply coverage outside those spans.

## 2. Reconciliation with the already accepted 2015–2025 run

Prior recent-period evidence reused (not re-run):
- Run #43624740474; artifact ID 14125517628; ZIP SHA-256 `daaedd6c4d186ac87ba6694ff3ae4816b544ba487fd12589b1b128b87f6cc861`.
- Assets raw body SHA-256 `68f865c2578f5d3dd21a145de71c0cb1f731041bf7b626fb5d1d3cd64e704664`.
- Liabilities raw body SHA-256 `b6875e20f20b279b2ce17131a42ba4af320adbc61f9c3bd28e9fb1067e597db1`.

Exact target reporters and periods:
| Code | Assets observations | Liabilities observations | Observation spans |
|---|---:|---:|---|
| ETH | 28 historical + 4 recent = 32 | 28 historical + 0 recent = 28 | Assets 2003-Q1–2009-Q4 and 2024-Q1–2024-Q4; liabilities 2003-Q1–2009-Q4 |
| HTI | 32 historical + 0 recent = 32 | 32 historical + 0 recent = 32 | Both 2004-Q4–2012-Q3 |
| DZA | 0 historical + 20 recent = 20 | 0 | Assets 2021-Q1–2025-Q4 |
| ZWE | 0 | 0 historical + 36 recent = 36 | Liabilities 2017-Q1–2025-Q4 |

All four observed spans are contiguous within each stated interval (no internal quarter gaps). These are short/reporting windows, not full-period completeness:
- ETH assets: 56 consecutive missing quarters from 2010-Q1 through 2023-Q4 between the historical and recent segments; only 4 recent quarters.
- ETH liabilities: no series returned from 2010-Q1 through 2025-Q4 after the 2003–2009 span.
- HTI assets and liabilities: no series returned before 2004-Q4 or after 2012-Q3 within the 2000–2025 tested horizon.
- DZA assets: no series returned in 2000-Q1–2020-Q4; liabilities have no series in either tested window.
- ZWE liabilities: no series returned in 2000-Q1–2016-Q4; assets have no series in either tested window.

## 3. Combined 2000–2025 result for the 43 priority codes

- Only 4/43 target countries have at least one observation in either tested window: DZA, ETH, HTI, ZWE.
- 39/43 have no observations for either assets or liabilities in either tested window (2000-Q1–2014-Q4 plus 2015-Q1–2025-Q4). One zero-observation ZWE liabilities series key exists in the historical raw response; it is preserved as an empty series key, not counted as data.
- Assets: 3/43 have observations (DZA, ETH, HTI); 40/43 have no series returned.
- Liabilities: 3/43 have observations (ETH, HTI, ZWE); 40/43 have no series returned.
- Two countries have both sides represented somewhere in the combined period: ETH and HTI. This does not mean same-quarter overlap or continuous coverage.
- The 43-row cross-period summary CSV is `data/research/imf_bop_emde_43_cross_period_matrix_20261114.csv`, SHA-256 `d331ba2f80c253c7d1e95dc2ba0c662fa27d4444aa21f12e9c881e200741704a` (2,547 bytes). It reports observations by side and time window, without inserting zeros into source data; zero counts mean no observation returned in the exact query; the status wording explicitly distinguishes this from an empty SDMX series key.

## 4. Interpretation and gate decision

Historical reach-back PASS as an acquisition and audit task. It found older observations for ETH and HTI and shows that the previous 2015–2025 "no series in range" label did not mean no historical reporting.

However, 39 of the 43 priority reporters still have no returned observations across the two tested windows. The four with any data have narrow, separated or one-sided spans. Reporter completeness, same-quarter bilateral coverage, observation status flags, revisions/vintages, and the cause of missing series are not resolved.

**Decision: HISTORICAL REACH-BACK QUERY PASS; CROSS-PERIOD RECONCILIATION PASS; EMDE COVERAGE GATE NOT PASS; AGGREGATION BLOCKED.**

Do not interpret absent observations as economic zero, non-reporting certainty, or a valid net-flow value. No EMDE portfolio-flow aggregate is eligible.

## 5. Series and observation attribute inspection

The already acquired raw SDMX responses requested `attributes=all`; no additional API request was needed. The exact DSD attribute order was applied to the series and observation arrays for all four reporters with nonempty observations (ETH, HTI, DZA, ZWE).

- Every observed series reports `SCALE=6` and `METHODOLOGY=BPM6`; `DECIMALS_DISPLAYED` and `OVERLAP` are null.
- `IFS_FLAG=true` on the observed asset series for ETH, HTI and DZA. It is null on the observed liability series for ETH, HTI and ZWE. The flag's interpretation is not inferred here; its codelist/definition must be verified before use.
- Every observed quarter has `PRECISION=6`, `DERIVATION_TYPE=O`, `ACCESS_SHARING_LEVEL=PUBLIC_OPEN`, and `SECURITY_CLASSIFICATION=PUB`.
- Observation-level `STATUS`, `ACCESS_SHARING_NOTES`, and `SOURCE` are null throughout the inspected series. Null is preserved; no flag/status is inferred.
- Historical ZWE liabilities contains a series key but zero observations. This is the reason the matrix now uses `NO_OBSERVATIONS_IN_EITHER_TESTED_WINDOW`, not the overly strong wording “no series returned”.
- No scale multiplier or unit conversion is applied; SCALE/PRECISION remain metadata.

## 6. Next highest-value action

Before another broad query, inspect the exact SDMX observation attributes and series attributes for the four reporters with returned observations (ETH, HTI, DZA, ZWE), including observation status/confidentiality/estimation flags and any revision/vintage markers exposed by the dataflow. In parallel, use the exact BOP codelist/dataflow metadata to establish whether the 39 no-series countries are eligible for these portfolio flow dimensions and quarterly USD representation. Keep all unresolved causes UNKNOWN. Only after this metadata audit decide whether a narrower older-period query or a different documented series is justified.

## 7. Invariants

₹0 spend; free official public sources only; no credentials, authentication bypass, paid APIs, synthetic data/timestamps, external contact, PR merge, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E and Hard Gate unchanged.
