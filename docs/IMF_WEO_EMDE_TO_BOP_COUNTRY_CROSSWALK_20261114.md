# WEO April 2026 EMDE to IMF BOP COUNTRY Code Crosswalk

Audit date: 2026-11-14 (Asia/Kolkata)  
Scope: dataset-specific mapping of the 154 WEO EMDE membership names to the exact IMF Data Portal BOP `COUNTRY` dimension codelist. No observations or aggregate calculated.

## Outcome

**PASS — 154/154 WEO EMDE members mapped to 154 unique BOP country codes; zero duplicate codes, zero UNKNOWN and zero ambiguous names.**

- WEO membership source: IMF WEO April 2026 Database Appendix, 154 names; raw PDF SHA-256 `b8a538c3158bf0553a3ae45d4797cd5648cbea684eb4be848a52c1d64d994395`; artifact 14115992695 from Run #43600131132.
- Target codelist: `IMF.STA:CL_BOP_COUNTRY(1.0.0)`, 345 codes.
- Codelist source: Portal-owned BOP Dataflow `IMF.STA:BOP(21.0.0)` structure response with references=all; raw response SHA-256 `e9414015aaf3480d8254f2935eb4f723f8b50196f104881d7cf29454bfb12ce5`; artifact 14122440301 from Run #43615378167.
- Matching: 109 normalized exact label matches and 45 explicit reviewed aliases. No fuzzy matching.
- Resulting 154 BOP country codes are unique.

## Critical disambiguation

The first direct normalized-name attempt found a dangerous same-name collision:

- WEO “Micronesia” maps in the WEO-to-IMF area source to area code FM, “Micronesia, Federated States of”.
- The BOP codelist contains both `FSM` = “Micronesia, Federated States of” and `U057` = “Micronesia” (a regional aggregate).
- The crosswalk explicitly selects `FSM` and excludes aggregate `U057`. This is why an unreviewed exact text match is not sufficient.

Other notable mappings:
- WEO “West Bank and Gaza” → BOP code `WBG`, exact BOP codelist label. This is a dataset-specific code mapping, not a geopolitical/legal-status assertion.
- WEO “Namibia” → `NAM`, direct BOP codelist label. The mapping is independent of any separate CL_AREA crosswalk code.

## Stored output

- CSV: `data/research/imf_weo_emde_to_bop_country_crosswalk_2026_04.csv`
- Rows: 154
- SHA-256: `62ad409cc71c1056994a418e55b5e2a9367bd04c844a6bb5957bda5f0b0dd815`
- Manifest: `data/research/imf_weo_emde_to_bop_country_crosswalk_2026_04.manifest.json`

## Acceptance boundary

This is a membership-to-dimension-code crosswalk only. It does **not** prove any country reports portfolio-investment observations. The next gate must compare these 154 codes against actual reporter codes returned by the exact BOP dataflow, separately for:
- asset-side `A_NFA_T`;
- liability-side `L_NIL_T`;
- selected frequency and period range.

Missing reporter observations remain UNKNOWN; WEO membership must never be treated as reporter coverage. No EMDE aggregation is permitted yet.

## Invariants

Research-only; ₹0 spend; official free sources only; no paid APIs, no credentials/auth bypass, no synthetic data/timestamps, no external contact, no PR merge, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, all five engines and Hard Gate unchanged.


## Independent integrity audit

- Run #43624431543 — SUCCESS; workflow commit `60b7a7819048e16c122a0ec760753353d805607c`; artifact ID `14125337955`; artifact ZIP SHA-256 `3ae91eae37286936b797719e2e7ae765e53fdba00916974ccbd2f553a4f4b9ee`.
- The validator re-read the committed CSV and verified SHA-256 `62ad409cc71c1056994a418e55b5e2a9367bd04c844a6bb5957bda5f0b0dd815`, 154 unique WEO names, 154 unique BOP country codes, 109 exact normalized matches, 45 explicit aliases, no duplicate codes, and the special Micronesia/West Bank and Gaza/Namibia checks.
- Integrity result: **PASS**.
