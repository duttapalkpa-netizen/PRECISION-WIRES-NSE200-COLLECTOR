# Step 6 — Source Coverage CSV/JSON Status Consistency Defect

**Date:** 2026-11-02  
**Repair branch:** `fix/source-coverage-status-reconcile`  
**Base:** `audit/run145-factor-registry-gap-audit` at `8d9197c55623c6d025c2de4ef33ec257e0dcaa97`

## Defect evidence

Run `41283471559`, artifact `13074955372`, contains `outputs/macro_geo/same_snapshot_reconciliation.json` with status `SAME_WORKFLOW_SNAPSHOT_WITH_RECONCILIATION_GAPS` and check `source_coverage_csv_json_statuses_match=false`.

Comparing `outputs/macro_geo/source_coverage.csv` with `outputs/macro_geo/source_coverage.json` identified two substantive status mismatches:

| Source group | CSV status | JSON status | Correct status |
|---|---|---|---|
| `macro_indicators` | `AVAILABLE` | `DATA_QUALITY_WARN` | `DATA_QUALITY_WARN` |
| `inflation_components` | `AVAILABLE` | `DATA_QUALITY_WARN` | `DATA_QUALITY_WARN` |

Both groups contain observations, but their historical completeness remains partial. The JSON report correctly retained `DATA_QUALITY_WARN`; the CSV writer incorrectly promoted them to `AVAILABLE` whenever row count was nonzero. This was a report-consistency defect, not evidence that either source had complete coverage.

## Root cause

`pipeline/collect_india_macro_series.py` maintained separate status logic for JSON and CSV. JSON always applied `DATA_QUALITY_WARN` to the two partial-history groups, while the CSV branch used `AVAILABLE if rows > 0`. This allowed one source snapshot to produce contradictory statuses.

## Repair applied on this branch

- Added `apply_macro_series_coverage_overrides(cov, cdf, qa)` to construct one authoritative status map and apply it to both outputs.
- `macro_indicators`, `government_capex` and `inflation_components` now remain `DATA_QUALITY_WARN` in both JSON and CSV until their declared quality conditions are satisfied.
- Selected paths, row counts and notes are updated from the same mapping.
- Replaced deprecated `selectolax.parser.HTMLParser` import with the maintained `selectolax.lexbor.LexborHTMLParser` backend. This was required because selectolax 1.0 raises an ImportError for the deprecated Modest backend.

## Regression evidence

Initial test Run `41340507789` failed before test collection because the old selectolax import was deprecated. This exposed a real compatibility issue and was corrected.

Follow-up Run `41340560881` completed SUCCESS on this repair branch. Artifact `13097271838`, ZIP SHA-256 `d8c1bbcac70dc49519ee8fbc4865d3422266bdd05959ce7e1717fe00b4c6680d`, was downloaded and inspected. It records 6/6 passing tests, including `test_macro_series_json_and_csv_statuses_share_one_override`.

## Remaining Step 6 acceptance

The unit regression proves the writer uses identical statuses for the two representations. It does not regenerate the full Macro-Geo source snapshot or prove that the earlier run's full CSV/JSON outputs are now reconciled. A fresh same-workflow P0 + macro-series + Factor Registry + event-study + hard-gate run must regenerate both reports, then `same_snapshot_reconciliation.json` must show `source_coverage_csv_json_statuses_match=true` and all required checks true. Until that artifact is inspected, Step 6 remains BLOCKED.

## Frozen invariants

Production selector, `RANKING_SCORE`, frozen `+1 PRESSURE_FADE` and 672 diagnostics remain unchanged. No missing value is converted to zero or negative evidence; no source is promoted solely because rows exist.