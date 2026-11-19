# GCR — 2026-Q2 Synchronous Dual-Leg Coverage Cohort
Date: 2026-11-19 (Asia/Kolkata)
Scope: derive a deterministic candidate cohort from the already archived 154-member IMF BOP panel coverage QA. This is a panel-availability gate only; it is not national-source validation or aggregate authorization.

## Progress Log
- Reused source coverage matrix: docs/evidence/imf_bop_emde_20261119/coverage_qa/coverage_by_country_entry_detailed.csv (308 country-entry rows; 154 members; 47 expected quarters 2015-Q1 to 2026-Q3).
- Recomputed both-leg availability directly from each row's explicit missing_periods list. Included a country only when neither A_NFA_T nor L_NIL_T marks 2026-Q2 missing.
- Result: 63/154 countries have both asset and liability entries in 2026-Q2 (40.91%). 2026-Q3 has only 2/154 countries with both legs; Q2 is therefore the latest materially broad common period in this snapshot.
- This count includes Brazil and Pakistan, which also have Q3 values; Q2 is still present for both. Country-readiness latest-period counts can show 61 at Q2 because they record each series' maximum period, not whether Q2 exists. This is not a contradiction.

## Candidate cohort
- AGO — Angola
- ALB — Albania
- ARG — Argentina
- ARM — Armenia, Republic of
- AZE — Azerbaijan, Republic of
- BDI — Burundi
- BGD — Bangladesh
- BIH — Bosnia and Herzegovina
- BLR — Belarus, Republic of
- BLZ — Belize
- BOL — Bolivia
- BRA — Brazil
- CHL — Chile
- CHN — China, People's Republic of
- COL — Colombia
- CPV — Cabo Verde
- CRI — Costa Rica
- DOM — Dominican Republic
- ECU — Ecuador
- GEO — Georgia
- GIN — Guinea
- GMB — Gambia, The
- HND — Honduras
- HUN — Hungary
- IDN — Indonesia
- IND — India
- KAZ — Kazakhstan, Republic of
- KOS — Kosovo, Republic of
- LAO — Lao People's Democratic Republic
- LKA — Sri Lanka
- LSO — Lesotho, Kingdom of
- MAR — Morocco
- MDA — Moldova, Republic of
- MEX — Mexico
- MKD — North Macedonia, Republic of
- MNE — Montenegro
- MNG — Mongolia
- MYS — Malaysia
- NGA — Nigeria
- NPL — Nepal
- PAK — Pakistan
- PAN — Panama
- PER — Peru
- PHL — Philippines
- POL — Poland, Republic of
- PRY — Paraguay
- ROU — Romania
- RWA — Rwanda
- SAU — Saudi Arabia
- SLB — Solomon Islands
- SLV — El Salvador
- SRB — Serbia, Republic of
- THA — Thailand
- TJK — Tajikistan, Republic of
- TLS — Timor-Leste, Democratic Republic of
- TUR — Türkiye, Republic of
- TZA — Tanzania, United Republic of
- UKR — Ukraine
- URY — Uruguay
- UZB — Uzbekistan, Republic of
- VNM — Vietnam
- WSM — Samoa
- ZAF — South Africa

## Acceptance boundary
- Panel-level 2026-Q2 both-leg availability: PASS for 63 listed members, as a deterministic roster derivation from the archived detailed matrix.
- Country national-source sign/scale validation: NOT IMPLIED; only individually benchmarked countries have external national-source PASS evidence.
- Source vintage alignment across all 63 members: UNKNOWN / NOT_DONE.
- BPM6/BPM7 compatibility and country-level sign conventions: NOT universally established.
- Missingness outside 2026-Q2 remains unchanged; no filling, zero substitution, interpolation, forward-fill or synthetic observations.
- Aggregate/net-flow admission: BLOCKED / NOT_AUTHORIZED. Do not sum this cohort or label it a complete EMDE universe.

## Reproducibility
- Input file: docs/evidence/imf_bop_emde_20261119/coverage_qa/coverage_by_country_entry_detailed.csv
- Input Git blob SHA: 1a7fd6f3e5955f08c2fcaf5a8fa81ac6b5b2f091
- Input rows parsed: 308; unique country codes: 154; expected periods: 47.
- Output roster: docs/evidence/imf_bop_emde_20261119/coverage_qa/2026Q2_both_legs_candidate_cohort.csv
- Output rows: 63; both required entry codes present for every row; aggregate_admission explicitly NOT_AUTHORIZED.

## Next exact actions
1. Prioritize official national-source scale/sign/vintage validation for the 63-country cohort, beginning with the largest EMDE markets not yet covered by national benchmarks.
2. Keep Chile Q1/Q2 as REVIEW_VINTAGE_MISMATCH until exact portfolio-series vintage bridge is available; official revision timing does not substitute for exact old/new portfolio rows.
3. Keep India 2026-Q1 liability/combined net REVIEW until the 1,512.508347 USD million residual is explained by direct vintage/definition evidence.
4. Keep Brazil PA/Dataflow mismatch BLOCKED until official IMF correction or Brazil-specific crosswalk and owner-side PA history export are obtained.

## Invariants
₹0; official/free sources only. No synthetic data, no inferred sign/scale transform, no cross-country vintage assumption, no aggregate. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.