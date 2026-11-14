# IMF BOP India Portfolio Assets/Liabilities — Annual/Quarterly Acquisition and Reconciliation

Audit date: 2026-11-14 (Asia/Kolkata)  
Branch: `research/imf-bop-access-audit-v1`  
Scope: India-only narrow public observation acquisition; no EMDE aggregate and no production integration.

## Outcome

**PASS — 110 raw observations acquired across four exact India series; annual/quarterly reconciliation passed within a predeclared raw-value tolerance of 0.00001.**

The Portal-owned dataflow crosswalk is now proven from the Portal API's own SDMX 2.1 structure response:

- Dataset/dataflow: `IMF.STA:BOP(21.0.0)`
- Exact referenced DSD: `IMF.STA:DSD_BOP(24.0.0)`
- Dataflow request: `https://api.imf.org/external/sdmx/2.1/dataflow/IMF.STA/BOP/21.0.0?references=all`
- HTTP 200; 3,965,650 bytes; SHA-256 `e9414015aaf3480d8254f2935eb4f723f8b50196f104881d7cf29454bfb12ce5`.
- Direct DSD dimensions, in order: COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY, TIME_PERIOD. TIME_PERIOD is the observation dimension.
- The earlier SDMX Central registry candidates (BOP_GBPM6, BPM6_BOP_Q and BOP 2.6.0) are not substituted for this Portal-owned DSD.

## Acquired series

| Series | Exact key | Rows | Period |
|---|---|---:|---|
| Annual assets | `IND.A_NFA_T.P_F.USD.A` | 11 | 2015–2025 |
| Annual liabilities | `IND.L_NIL_T.P_F.USD.A` | 11 | 2015–2025 |
| Quarterly assets | `IND.A_NFA_T.P_F.USD.Q` | 44 | 2015-Q1–2025-Q4 |
| Quarterly liabilities | `IND.L_NIL_T.P_F.USD.Q` | 44 | 2015-Q1–2025-Q4 |

Total: **110 observations**. All four exact API responses returned HTTP 200 with the declared SDMX-JSON 2.0.0 media type. Series dimension order and requested key values were checked against the returned structure; all observations were non-null, finite and had unique periods. All 44 quarters per quarterly series are present.

### Code meanings verified from the Portal-owned structure/codelists

- `IND`: India
- `A_NFA_T`: Assets, Net acquisition of financial assets
- `L_NIL_T`: Liabilities, Net incurrence of liabilities
- `P_F`: Portfolio investment, Total financial assets/liabilities
- `USD`: US dollar
- `A` / `Q`: Annual / Quarterly

Assets and liabilities remain separate series. No netting or portfolio aggregate is calculated.

## Annual-versus-quarterly reconciliation

For each year, the four quarterly raw `OBS_VALUE` strings were summed with Decimal arithmetic and compared to the corresponding annual observation. No scale multiplier or currency conversion was applied.

| Side | Years checked | Max absolute difference | Tolerance | Result |
|---|---:|---:|---:|---|
| Assets | 11 | 0.0000009 | 0.00001 | PASS_WITH_TOLERANCE |
| Liabilities | 11 | 0.000007 | 0.00001 | PASS_WITH_TOLERANCE |

This is an arithmetic coherence check on the acquired series, not an independent validation of IMF economic methodology or revision history.

## Metadata and preservation rules

- Series attributes: `SCALE=6`, `METHODOLOGY=BPM6`; quarterly asset series also carries `IFS_FLAG=true`.
- Observation attributes: `PRECISION=6`, `DERIVATION_TYPE=O` (Reported official data), `ACCESS_SHARING_LEVEL=PUBLIC_OPEN` (Public/Unrestricted), `SECURITY_CLASSIFICATION=PUB` (Public/Unrestricted).
- `STATUS`, `ACCESS_SHARING_NOTES` and `SOURCE` remain null where the source returned null.
- SCALE and PRECISION are retained as metadata only. No multiplier, scaling or currency conversion has been applied.
- Raw response bodies, parsed JSON, exact URLs, retrieval timestamps, response SHA-256 values and workflow artifacts are preserved.

## Raw response provenance

| Series | Response bytes | Response SHA-256 |
|---|---:|---|
| Annual assets | 7,845 | `85cca14cabf7a674ba37c00f88e3140f562480130bdde57d4902562fa6e0e23a` |
| Annual liabilities | 7,846 | `6eba68f8779efa5636afea8d4a9de4ce26478c67150144c1e4f128e4f6d3a4e4` |
| Quarterly assets | 10,201 | `aff39180e21eec8f71308ac269f9191eb0138b5471808bfa710c6a582be1d24f` |
| Quarterly liabilities | 10,185 | `6ebe3c2eabd7f9019ffd80d51e01de359bc1f64aee66c8609877654ad4558ccc` |

Combined CSV: `data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.csv`  
Rows: 110; SHA-256: `260ccc247ec564737bb3afe0a820c2435e37a58f588603241274537eca99f1b9`.

Manifest: `data/research/imf_bop_india_portfolio_assets_liabilities_annual_quarterly_2015_2025.manifest.json`.

## GitHub Actions evidence and corrections

- Dataflow metadata / exact DSD reference: Run #43615378167 SUCCESS; artifact 14122440301; ZIP SHA-256 `2411f5837d7145ed6450a1423b17282f240cda6b7b6d61d842e4c18a6e88c125`.
- Annual assets narrow response: Run #43616059985 SUCCESS; artifact 14122421554; ZIP SHA-256 `cc951e2655dc4592ab82d848e0beebc43970132de1f4f3edc5c3ef8b56aaed23`.
- Liability/quarterly first parser attempt: Run #43623450125 FAILED after all three HTTP 200 responses because the validator incorrectly treated the ordered dataset-level attribute array as a mapping. Raw responses and failed artifact were retained (artifact 14125291402; ZIP SHA-256 `20d24b5109a9c44dd485a357687d789d5417ed5215f41b4bdf90ccbfe1c86a87`).
- Correction: preserve dataset attributes as the source's ordered array; do not call mapping methods on it. No API query/key change was needed.
- Corrected acquisition: Run #43623518481 SUCCESS; workflow commit `111167ff11fbba42b226d8ee33634f111be0a893`; artifact 14125515371; ZIP SHA-256 `4127f4b691e46967dc8e0f91d6ff5536e9bc01224de0d488f90e5a4acd13327c`.

Earlier 404s caused by incorrectly adding `/structure/` to the SDMX 2.1 REST path remain diagnostic evidence; the correct resource path has no such prefix. The initial SDMX-JSON parser's failure on the nested `dataSets[0].series[*].observations` shape is also retained in the historical audit record; the corrected parser reads the series-level observation map.

## Acceptance and remaining limits

- Portal dataset-to-Portal-owned dataflow/DSD crosswalk: PASS.
- India annual assets and liabilities: PASS (11 rows each).
- India quarterly assets and liabilities: PASS (44 rows each).
- Annual/quarterly arithmetic reconciliation: PASS_WITH_TOLERANCE on both sides.
- Full 154-economy EMDE reporter coverage: NOT DONE.
- Revision/vintage history: NOT DONE.
- EM portfolio-flow aggregation: BLOCKED.

This is not a full EMDE panel. WEO EMDE membership does not establish that an economy reports a usable BOP observation. Keep missing reporters UNKNOWN; do not infer, forward-fill, net or impute.

## Invariants

Research-only; ₹0 spend; official free sources only; no paid APIs; no credentials or authentication bypass; no synthetic data/timestamps; no external contact; no PR merge; no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, all five engines and Hard Gate remain unchanged.
