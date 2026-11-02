# Step 7 — Focused Macro Source Remediation Evidence (2026-11-02)

## Scope and safety boundary

This note records evidence-only work for F14 (inflation), F07 (domestic growth/capex) and F20 (fiscal policy/government expenditure). It does not change production inputs, Factor Registry mappings, selector logic, ranking, or diagnostic definitions.

Hard gate remains **BLOCKED**. `UNKNOWN` remains neither PASS nor FAIL. No paid/licensed PMI feed was accessed.

## Successful official-source QA runs

| Workstream | Run | Result | Evidence |
|---|---:|---|---|
| OEA WPI item-wise + release-status crosswalk + adapter + same-snapshot recheck | 41391252404 (#20) | SUCCESS | Artifact 13116954178; SHA-256 `d827484077b88bf316bfa66594b104080c893c73d96be402f5be648868bd05f9` |
| MoSPI NAS GDP bounded live smoke | 41391252381 (#11) | SUCCESS | Artifact 13117776814; SHA-256 `4b600978ab9532dbbe5afb99b2db4e8c65c6ee2df8b68393993f19d8ea249608` |
| MoSPI CPI 2024=100 bounded live smoke | 41391252299 (#7) | SUCCESS | Artifact 13116879627; SHA-256 `0561f81e2d45f4440e5fc9091b406ecd4a385eaa3e4cdff576f9ef6bd5df95e5` |
| CGA FY2026-27 Sep capex live QA | 41391252331 (#8) | SUCCESS | Artifact 13117456554; SHA-256 `9f47fd2fae4e2c0f849c5cf95d63be3c9679aa4516853d6fc316fe587425d0ae` |
| CGA monthly historical extraction + vintage audit | 41391252306 (#2) | SUCCESS | Artifact 13117208086; SHA-256 `50896ddf8430e3fcd67ed8835369f6d6d057c58d7bc32d6ab489eb9d9f1d0d92` |
| NSE 200-session collector benchmark | 41391252264 (#192) | SUCCESS | Artifact 13117681373; SHA-256 `48f6f75ef268b250aecdb7ff2f8c111e356c6e37ce433afa1d7098488ca397c4` |

## F14 — inflation

- Official OEA WPI workbook downloaded over strict TLS from `https://eaindustry.nic.in/indx_download_2223/wpi_monthly_index_202610.xlsx`.
- 42 monthly periods, April 2023–September 2026; 47,598 normalized item-period observations; 1,136 distinct item codes. The workbook has 42 observations without item codes; these remain explicitly unkeyed.
- Raw workbook SHA-256: `6f5dc662771aa0a2bfc152c777f6dd89684499c2e0802c20a7518d6eed184609`.
- Normalized CSV SHA-256: `63ad51283d3f5732ee22dfb95b478582932eb784d0928383524b9f999eea9cb4`.
- Crosswalk: 4 FINAL months, 2 PROVISIONAL months, 36 UNKNOWN months; October 2026 has zero rows and is scheduled for 16 November 2026.
- Full-schema adapter: 47,598 rows, all required fields present, actual retrieval timestamp retained, month-level release evidence kept distinct from item-level revision evidence. Adapter SHA-256: `6384b0f30cd4cc3d2790b49dec5cc720097ea03e4f5a3c891599b3f2356018d9`.
- Same-snapshot recheck: `inflation_components=AVAILABLE` for schema/data coverage only. F14 remains `PARTIAL_SOURCE_COVERAGE` because `macro_indicators=DATA_QUALITY_WARN` and `india_bond_yields=NOT_CONNECTED`. Item-wise revision history is not published in the reviewed official evidence. No F14 promotion.

## F07 — domestic growth and public expenditure

- MoSPI GDP bounded live evidence: official NAS table `AEQEAFY2607QTR`, Q1 FY2026-27 constant prices, release date 31 August 2026. Extracted real GDP ₹8,136,153.44 crore (₹81.36 lakh crore) and YoY growth 7.817%. Raw workbook SHA-256: `216357110a24e07609d899f956441426691ca64aceb1385f9675c198731ba301`.
- This is one quarter only, not a full quarterly historical GDP panel. Current-price GDP and a complete release-vintage history were not collected.
- CGA official September 2026 capex QA: April–September cumulative YTD actual ₹654,547 crore against BE ₹1,221,821 crore; utilization 53.6%. Official release timestamp 30 October 2026, 17:02 IST. Data are provisional/unaudited and cumulative, not September standalone monthly flow.
- CGA monthly history extraction: 143 months, April 2014–February 2026, with no missing month in the extracted panel. Standalone monthly flows are derived from within-FY cumulative values. Vintage status remains `VINTAGE_UNVERIFIED_SINGLE_LATEST_SNAPSHOT`; source page last-updated date is not treated as workbook publication timestamp.
- PMI remains `NOT_CONNECTED`; underlying dataset requires a licensed feed and no credentials/licence were supplied.
- F07 remains `NOT_CONNECTED`: `macro_indicators=DATA_QUALITY_WARN`, `global_policy_events=DATA_QUALITY_WARN`, `sector_fundamentals=NOT_CONNECTED`, `government_capex=DATA_QUALITY_WARN`.

## F20 — fiscal policy and government expenditure

- CGA/PIB September 2026 YTD capex evidence above is a bounded official observation, not a complete monthly vintage series.
- F20 remains `PARTIAL_SOURCE_COVERAGE`: `corporate_events=AVAILABLE`, `global_policy_events=DATA_QUALITY_WARN`, `macro_indicators=DATA_QUALITY_WARN`, `government_capex=DATA_QUALITY_WARN`, `domestic_policy_events=NOT_CONNECTED`.
- No policy-event coverage is inferred from headlines or capex data.

## Separate NSE cache validation

Run #192 validated exactly 200 sessions, 7 January–30 October 2026. Warm-cache check: 200/200 hits, zero misses, 16.273541 seconds, 12.29 sessions/second. All 200 CSV byte sizes and SHA-256 values matched the immutable manifest. Snapshot ID: `f90c01c1d7e228ab7282a96fef4dfb3ceca7f67675938926dac009f9cb92d72c`; manifest SHA-256: `d23b294d8b9a4b93f3aeab06778a01be4646f7071b549953ea073383d7422`.

Provenance limitation remains: these records originate from pre-existing cache files with unavailable original network URLs and authoritative server retrieval timestamps. The cache integrity PASS does not close that provenance gap.

## Final disposition

- Focused official-source collection, parsing, domain QA, hash checks and same-snapshot linkage: **PASS for the bounded scopes above**.
- F14, F07 and F20 full historical/factor evidence: **NOT COMPLETE**.
- Factor Registry: 35 groups; 0 fully available; 25 partial; 10 not connected.
- Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE` and 672 diagnostic definitions: unchanged.
- Hard gate: **BLOCKED** until complete, point-in-time, source-backed evidence closes all required gates.
