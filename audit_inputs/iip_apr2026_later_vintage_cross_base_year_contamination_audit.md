# IIP April 2026 later-vintage cross-base-year contamination audit

Audit date: 2026-11-08
PR branch: `qa/iip-apr2026-crosscheck-validation`

## Executive finding

The 23 values previously recorded in `later_vintage_index_values` are not comparable 2022-23-base observations. They match, row-for-row, the April 2026 column in the official MoSPI/PIB May 2026 release's separate monthwise table, which explicitly states `Base: 2011-12=100`.

The same release separately presents current-series tables at `Base: 2022-23=100` (Statement II-A, lines 56-60) for NIC-2025, but those are distinct tables and values. The release explicitly says the Output-PPI 2022-23 series supersedes the earlier WPI-based 2022-23 series (lines 8-10 and 27-28). The monthwise table at lines 144-169 is explicitly 2011-12 base and must not be joined to the 2022-23 first-release ledger.

Official source:
- PIB/MoSPI May 2026 release, Release ID 290616:
  https://www.pib.gov.in/newsite/archiveContent.aspx?lang=2&reg=48&relid=290616
- Relevant evidence: lines 56-60 (2022-23 NIC-2025 Statement II-A), lines 144-169 (monthwise table explicitly Base 2011-12=100).

## Row-level verification

All 23 April-2026 values in the prior ledger's `later_vintage_index_values` field match exactly the corresponding April-2026 values for NIC 10-32 in the 2011-12-base monthwise table (23/23 exact numeric matches; 0 mismatches). This is a source-series identification, not proof of comparability. The source table itself declares the incompatible base year.

## Corrective action

1. Preserved the three later-vintage IDs, release dates, and observed numeric values as raw evidence.
2. Added explicit source metadata: `later_vintage_source_base_year=2011-12`, source table name, and official PIB URL.
3. Cleared `latest_later_index` and `revision_delta_latest_minus_first` because cross-base-year subtraction is invalid.
4. Changed `revision_detected` to `UNKNOWN` and assessment to `SOURCE_BASE_YEAR_MISMATCH_NOT_COMPARABLE`.
5. Updated the offline validator and regression tests so that cross-base-year values cannot be treated as valid revisions or relabelled 2022-23.
6. Kept `LATER_VALUES_MATCH_2011_12_MONTHWISE_TABLE`, `REVISION_STATUS_UNKNOWN_NOT_COMPARABLE`, and `RAW_PDF_SHA256_PENDING` explicit.

## Current acceptance status

- First-release April 2026 NIC-2025 ledger: preserved, 23 rows.
- Later-vintage source lineage: identified as 2011-12 monthwise values, therefore not comparable.
- Valid 2022-23 same-series later-vintage revision check: still pending.
- Raw first-release PDF SHA-256: still pending.
- IIP sub-audit and project-wide hard gate: BLOCKED; no promotion to PASS.
- No source values were synthesized, converted, rebased, or backfilled.
- No production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, or 672 diagnostic logic changed.
- Spend: ₹0; official public sources only.

This note supersedes the earlier interpretation that the three later-vintage values constituted comparable 2022-23 observations. It does not erase the historical audit trail; it corrects the evidence classification.
