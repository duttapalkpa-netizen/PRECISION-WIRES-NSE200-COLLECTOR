# WEO October 2026 — EMDE Membership and BOP Country Crosswalk (Part 1)

Date: 2026-11-19

## Result
- Official WEO October 2026 workbook downloaded directly from IMF: HTTP 200.
- Workbook filename: `WEOOct2026all.xlsx`; 5,480,592 bytes; SHA-256 `2aa4f70a05931197b41ed7e0202dc56eee8d816858ac14521e4f8f5dbc38696c`.
- Authoritative sheet: `Country Group Composition`; group code `G200`; group name `Emerging Market and Developing Economies`.
- Exactly 154 membership rows; 154 unique WEO country codes; zero duplicate codes.
- IMF BOP country codelist `IMF.STA:CL_BOP_COUNTRY(1.0.0)` downloaded HTTP 200; 345 codes; raw 204,795 bytes; SHA-256 `54647ef3ac6439ecd059fd80a7954c35e447415d53bf41fbee02728e7cfb6bcb`.
- Exact code-ID crosswalk: 154/154 mapped, 0 unmapped, 0 duplicate WEO codes. No fuzzy name matching or guessed aliases.
- One display-name difference: WEO `NRU: Nauru, Republic of`; BOP codelist names include `Nauru`, `Naoero, Republic of` and localized labels. Country code NRU matches exactly; label difference preserved, not treated as a code mismatch.
- Official October 2026 WEO Database Appendix also downloaded HTTP 200; 985,701 bytes; SHA-256 `cd4e2829d7e621d43134728bfc128547f776e909e08ef1d38b837e2d39e5ae2a`.
- Workflow run [44474502699](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44474502699) SUCCESS; artifact 14505617102; 6,204,691 bytes; ZIP SHA-256 `3246d18f7ef6a1d74c2a08ddc37a94542fc0d42c14acf14470e0a8d7bb2783bb`.
- Artifact files: raw WEO workbook, raw WEO Appendix PDF, raw IMF BOP country codelist XML, 154-row crosswalk CSV, summary JSON. Retention until 2027-02-17.

## Durable compact membership index
- `docs/evidence/WEO_OCT2026_EMDE_G200_BOP_CODES_154.csv` contains all 154 WEO group codes and exact BOP country-code matches.
- Source crosswalk and raw files remain in artifact 14505617102. Artifact must be re-downloaded before retention expiry if a byte-identical raw archive is needed.

## Interpretation guardrails
- This is the October 2026 WEO vintage membership edition, not a timeless EM universe. Preserve the vintage with any panel.
- Exact code-ID match is a technical country-code crosswalk, not evidence that every country has BOP observations in every quarter.
- The 154-member list does not establish panel completeness, data availability, unit/sign compatibility, or authority to aggregate.
- Continue to preserve missing country-quarter observations as missing. No forward-fill, synthetic rows, fuzzy aliasing, or silent substitutions.
- Do not calculate a net portfolio-flow factor until `SCALE`, signs, reporting status, revisions/vintages and coverage thresholds are resolved.

## Next work
1. Query the exact IMF BOP portfolio flow keys for all 154 codes and both accounting entries `A_NFA_T` and `L_NIL_T`, keeping `P_F`, USD, quarterly fixed.
2. Produce a country × accounting-entry × quarter coverage matrix, including empty/partial series, duplicate-key QA, raw hashes, retrieval timestamps and source attributes.
3. Validate `SCALE=6` semantics and sign conventions before any summation; no EM aggregate yet.
