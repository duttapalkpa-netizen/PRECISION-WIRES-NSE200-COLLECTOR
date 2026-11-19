# GCR — IMF BOP SCALE reconciliation against RBI India BPM6 Table 197
Date: 2026-11-19
Status: **INDIA FOUR-QUARTER EMPIRICAL SCALE/SIGN CHECK PASS; GLOBAL SCALE RULE PARTIAL / BRAZIL PENDING**

## Progress Log
### Completed
- IMF BOP EMDE raw panel independently inspected; 9,299 normalized observations reconcile exactly to the two broad raw CSVs: 9,299/9,299 keys, 0 missing, 0 duplicate, 0 source-attribute mismatches.
- Retrieved official RBI Table 197 (Standard Presentation of India's Balance of Payments as per BPM6 — Quarterly — US Dollar), published 31 July 2026, unit US$ million.
- Compared IMF Data Portal India `P_F` series `A_NFA_T` and `L_NIL_T` with RBI Table 197's `Portfolio Investment by India` and `Portfolio Investment in India` net values for four quarters: 2024-Q2 through 2025-Q1.
- All eight observations agree within RBI's displayed integer-million rounding: max absolute difference 0.490 million USD.
- Exact BOP country and WEO membership mapping remain 154/154 PASS.

### Rejected / not authorized
- Do not multiply the Data Portal API's raw `OBS_VALUE` by 10^6 a second time. That produces amounts incompatible with the RBI benchmark by six orders of magnitude.
- Do not treat the four-quarter India result as a universal proof for all 154 EMDE members.
- Brazil comparison is NOT_DONE / BLOCKED: existing BCB SGS cross-source audit has a 2010-01 structural break and 201/381 monthly mismatches; it is not an acceptable scale benchmark without exact indicator/vintage reconciliation.
- No assets/liabilities aggregation, net-flow construction, currency conversion, missing-value filling, macro factor weighting or production admission.

## 1. Official reference and metadata
- RBI source: https://rbi.org.in/SCRIPTs/PublicationsView.aspx?id=24022
- Table 197 is explicitly quarterly, BPM6, US$ million, and revision-subject. The published table labels the relevant rows `Portfolio Investment in India` and `Portfolio Investment by India`.
- IMF BOP dataflow: `IMF.STA:BOP(21.0.0)`; DSD `IMF.STA:DSD_BOP(24.0.0)`; indicator `P_F`; entries `A_NFA_T` and `L_NIL_T`; country `IND`; unit `USD`; frequency `Q`.
- Source panel artifact: run 44474620936, artifact 14505452613, ZIP SHA-256 `b23854fa433b46b29bb2d8094ec9bc14d2cd6c58fdc1771fa9428ca6ae3aed17`.
- Normalized panel SHA-256 `e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a`.
- IMF `CL_UNIT_MULT(1.0.2)` code 6 label = `Millions`; captured in run 44474877779 / artifact 14505992737 (artifact ZIP SHA-256 `f70981e1511a709526851eee59548ca237f8ac4c9a02c8d0eb1e8c9410b1017e`). Generic SDMX glossary defines UNIT_MULT as the power-of-ten multiplier and says code 6 denotes millions. This metadata definition is not, by itself, proof of how the IMF Data Portal observation API serializes numeric payloads.

## 2. Empirical payload representation test
For the tested IMF Data Portal quarterly series, dividing raw API `OBS_VALUE` by 1,000,000 produces values that match RBI's published US$ million table. The unscaled raw API values are therefore empirically in base USD for these tested India series/periods; `SCALE=6` is retained as source metadata and must not be applied a second time as a multiplication.

The RBI table's `Portfolio Investment by India` credit-minus-debit net is compared to the sign-reversed `A_NFA_T` value; `Portfolio Investment in India` net is compared to `L_NIL_T`. This is a source-to-source empirical sign mapping for the tested India series only.

| Quarter | RBI by India net (US$m) | IMF A_NFA_T raw / 1e6, sign reversed | Difference | RBI in India net (US$m) | IMF L_NIL_T raw / 1e6 | Difference |
|---|---:|---:|---:|---:|---:|---:|
| 2024-Q2 | 48 | 47.510 | -0.490 | 897 | 897.230 | +0.230 |
| 2024-Q3 | 35 | 34.990 | -0.010 | 19,815 | 19,815.071 | +0.071 |
| 2024-Q4 | 63 | 62.610 | -0.390 | -11,435 | -11,434.647 | +0.353 |
| 2025-Q1 | 136 | 135.999 | -0.001 | -5,995 | -5,994.631 | +0.369 |

- 8/8 comparisons within ±0.5 million USD (RBI displayed integer rounding); maximum absolute difference = 0.490 million USD.
- Detailed machine-readable values: `docs/evidence/IMF_BOP_IND_SCALE_RECONCILIATION_2024Q2_2025Q1.csv`.
- No values were rewritten in the source panel; the division and sign reversal are only comparison transformations in this validation table.

## 3. Interpretation boundary
- **PASS (India-specific):** Data Portal API payload representation and sign orientation empirically reconcile with RBI Table 197 over four quarters.
- **PARTIAL (global):** Do not apply this transform to all 154 EMDE countries until Brazil and additional national benchmarks confirm identical API serialization and sign convention.
- **BLOCKED (Brazil):** Existing Brazil BCB SGS cross-source reconciliation reports 201 mismatches out of 381 monthly periods beginning at 2010-01; exact source-series/vintage mapping is unresolved. The older BCB SDMX Central registered file uses a different dataflow/DSD and must not be silently substituted for IMF Data Portal `IMF.STA:BOP`.
- Preserve `SCALE=6`, `UNIT=USD`, raw observations and provenance. Keep both legs separate. Do not aggregate or calculate net flow until Brazil and more country benchmarks pass.

## 4. Exact next actions
1. Resolve Brazil Data Portal `P_F` vs BCB official quarterly/monthly source mapping, including the known 2010 structural break and revision vintage.
2. Add at least two further country benchmarks from official national sources with the same series semantics.
3. Only after cross-country confirmation, approve a versioned transform for the GCR panel and rerun all 154-country coverage and aggregation checks.
4. Then review BPM6/BPM7 basis, revisions and vintage alignment before constructing any EMDE aggregate.

## Invariants
No changes to Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, or Engines A–E. ₹0 spend; no paid API; no synthetic observations; UNKNOWN is not PASS.
