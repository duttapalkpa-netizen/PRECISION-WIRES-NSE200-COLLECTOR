# IMF BOP India portfolio annual-to-quarterly reconciliation

Date: 2026-11-14 (UTC)
Branch: `research/imf-bop-access-audit-v1`
Dataset: `IMF.STA:BOP(21.0.0)`
DSD: `IMF.STA:DSD_BOP(24.0.0)`
Method: direct, unauthenticated, public SDMX 3.0 JSON retrieval; no scaling, unit conversion, forward fill, synthetic values, or aggregation across countries.

## 1. Acquisition evidence

GitHub Actions Run #43623518481: SUCCESS
Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43623518481
Workflow commit: `111167ff11fbba42b226d8ee33634f111be0a893`
Artifact ID: `14125515371`
Artifact ZIP SHA-256: `4127f4b691e46967dc8e0f91d6ff5536e9bc01224de0d488f90e5a4acd13327c`

The artifact contains the raw response bodies, per-series JSON provenance records, parsed observation rows, and summary acceptance record. The ZIP was downloaded and inspected locally. All three HTTP 200 responses parsed; exact returned series keys matched the requested keys; values were non-null and finite; periods were unique.

| Series | Exact key | Periods | Rows | Raw response bytes | Raw body SHA-256 |
|---|---|---:|---:|---:|---|
| India portfolio liabilities, annual | `IND.L_NIL_T.P_F.USD.A` | 2015–2025 | 11 | 7,846 | `6eba68f8779efa5636afea8d4a9de4ce26478c67150144c1e4f128e4f6d3a4e4` |
| India portfolio assets, quarterly | `IND.A_NFA_T.P_F.USD.Q` | 2015-Q1–2025-Q4 | 44 | 10,201 | `aff39180e21eec8f71308ac269f9191eb0138b5471808bfa710c6a582be1d24f` |
| India portfolio liabilities, quarterly | `IND.L_NIL_T.P_F.USD.Q` | 2015-Q1–2025-Q4 | 44 | 10,185 | `6ebe3c2eabd7f9019ffd80d51e01de359bc1f64aee66c8609877654ad4558ccc` |

The previously accepted annual India asset series contains 11 rows (2015–2025), CSV SHA-256:
`60e557c922763f145284c6243e4612d6c05c0ce756c6f2d8846e0ea2fc7c8697`.
Its compact SDMX JSON response SHA-256 is
`85cca14cabf7a674ba37c00f88e3140f562480130bdde57d4902562fa6e0e23a`.

## 2. Annual versus quarterly reconciliation

For each year 2015–2025, the four quarterly observations were summed and compared with the corresponding annual observation for the same country, accounting entry, indicator, unit, and methodology.

`difference = sum(Q1, Q2, Q3, Q4) - annual OBS_VALUE`

| Year | Asset difference (USD) | Liability difference (USD) |
|---:|---:|---:|
| 2015 | -0.000000024 | 0.0000039 |
| 2016 | -0.000000030 | 0.0000004 |
| 2017 | 0 | -0.0000020 |
| 2018 | 0.000000170 | -0.0000020 |
| 2019 | 0.000000900 | 0.0000070 |
| 2020 | -0.000000100 | 0.0000030 |
| 2021 | -0.000000020 | 0.0000004 |
| 2022 | -0.000000200 | 0.0000030 |
| 2023 | 0 | 0 |
| 2024 | 0.000000050 | -0.0000002 |
| 2025 | 0.000000260 | 0.00000017 |

Maximum absolute discrepancy:
- Assets: USD 0.0000009
- Liabilities: USD 0.0000070

These are sub-cent representation-level differences from summing decimal strings represented in JSON; both sides reconcile within USD 0.00001 for every year. No material annual/quarterly mismatch was found.

## 3. Acceptance result

- [x] Three requested India series returned HTTP 200.
- [x] Exact series keys matched the request.
- [x] Annual liability series: 11/11 periods (2015–2025).
- [x] Quarterly asset series: 44/44 periods (2015-Q1–2025-Q4).
- [x] Quarterly liability series: 44/44 periods (2015-Q1–2025-Q4).
- [x] No duplicate periods, null values, or non-finite values in the extracted observations.
- [x] Annual-to-quarterly arithmetic reconciled for assets and liabilities across all 11 years.
- [x] Raw response bodies and provenance records retained in the run artifact.

**Work-package status: PASS — narrow India annual/quarterly portfolio asset/liability acquisition and arithmetic reconciliation.**

## 4. Scope boundary / remaining work

This does not complete the full India BOP panel, revision/vintage analysis, all account components, or 154-economy EMDE coverage. The annual liability and quarterly series are a focused portfolio-investment slice only. The annual/quarterly agreement is an internal consistency check, not independent source corroboration. Do not treat it as proof of broader cross-country coverage or capital-rotation conclusions.

Next work should preserve observation attributes and series metadata, then extend the acquisition to the remaining explicitly approved India portfolio dimensions before attempting EMDE expansion. EM aggregate flow remains BLOCKED until the required country coverage, definitions, flags, and aggregation rules are independently verified.

## 5. Project invariants

No changes to Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, engines A–E, or Hard Gate. No PR merge or production integration. No paid service, credential use, or synthetic observation/timestamp.
