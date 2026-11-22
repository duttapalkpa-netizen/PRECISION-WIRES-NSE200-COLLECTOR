# C273 Run #395 walk-forward failure: root cause and bounded repair

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`

## Continuity and scope
- Reused the existing C273 work and inspected Run #395's actual GitHub job and artifact metadata; no NSE acquisition or dataset QA was repeated manually.
- Run #395: `45018120031`, head commit `2861b308248413d9657cdfba19931385a0fc7870`, artifact `14751684904`.
- Artifact digest: `sha256:3e6fa054c44edae50661feb03d2a0968098f88bb3a2894cb5ed72f214b59af76`.
- Successful Run #395 stages include normalized NSE history acquisition, per-file acquisition manifest/hash validation, legacy equity master provenance, security-master freshness/provenance validation, adaptive dataset build, strict dataset QA, and quarterly results/calendar collection. The corrected-label walk-forward step failed; later optional steps were skipped.

## Verified failure
The job log reports:
```
KeyError: 'FUT1_END_DATE'
pipeline/walk_forward_backtest.py:547
_matured_state_target_metrics()
```
The maturity function correctly requires a non-null forward outcome and its horizon-end date. The source's `future_outcomes()` creates `FUT1_END_DATE`, `FUT3_END_DATE`, and `FUT5_END_DATE`. However, the Top-30 `predictions` row serializer exported the FUT* outcome percentages but omitted all three end-date fields. The function therefore received a prediction dataframe without the required maturity columns. This is a serializer/data-contract defect, not an NSE acquisition failure.

## Bounded repair committed
- Added `FUT1_END_DATE`, `FUT3_END_DATE`, and `FUT5_END_DATE` to each serialized prediction row.
- Commit: `c55c54226151a9acd973c415d98e02227f93dc0b`.
- New file blob SHA: `062d55a0ff6bc4982f051e4c1b24918e75c0d23d`.
- Read-back from the same isolated branch confirmed all three end-date fields are present in the prediction serializer.
- No production selector, rank, score, pressure-fade, CORE-672, Engine A-E, or IPO-PLX logic was changed.

## Validation state
- Run #395 remains **FAIL**; it cannot be relabelled PASS.
- Run #396 (`45018125140`) was still **IN_PROGRESS** at the time of this report. It had passed the early corrected-label unit-test step and was processing acquisition/quarterly-results steps. It started before repair commit `c55c542`, so it cannot validate that repair.
- The repair is **COMMITTED / READ-BACK VERIFIED / EXECUTION NOT YET VALIDATED**.
- No claim is made about matured denominators, State calibration counts, or a successful corrected-label walk-forward until a run using commit `c55c542` completes and its artifact is independently inspected.

## Exact next actions
1. Read Run #396 final status, job steps, logs and artifact; record its result without assuming it contains the repair.
2. Run a bounded validation on the repaired branch/commit `c55c54226151a9acd973c415d98e02227f93dc0b`; require the walk-forward stage to complete and the output to contain all three maturity end-date columns.
3. Reconcile per-State × target numerator/denominator from matured rows only; H+3 states with fewer than 50 fully matured observations remain UNKNOWN.
4. Inspect output artifact and verify manifest/SHA-256; preserve PASS/FAIL/BLOCKED/UNKNOWN distinctly.
5. Only after these checks, update the Master Continuity Ledger and C273 acceptance status. Do not claim PASS based on code commit or unit tests alone.

Constraints: ₹0 spend; free/official sources only; no synthetic or immature observations; UNKNOWN is never PASS.
