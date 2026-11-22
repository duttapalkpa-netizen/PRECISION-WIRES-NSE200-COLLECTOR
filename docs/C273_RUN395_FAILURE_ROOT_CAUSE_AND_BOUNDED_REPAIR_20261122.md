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


## Follow-up correction after Run #396 and Run #397 (2026-11-22)

- Run #396 (`45018125140`) completed **FAIL** at walk-forward step 15 with the same `KeyError: FUT1_END_DATE`. Its head SHA was `73b865cc830280ef89012b1cc1e25c63ee5b50d1`, predating the first serializer change; it did not validate that change. Artifact `14752917639`, SHA-256 `8bbac34bb7c3c668fba262fd9dabe99ecd8c30333dc537bea86fc3c90d7da763`.
- Run #397 (`45018883341`) also completed **FAIL** with the same KeyError. Inspection of its checked-out source exposed the exact mistake in the first repair: commit `c55c542` added end-date fields to `universe_predictions`, but `_matured_state_target_metrics()` consumes `pred = pd.DataFrame(predictions)`, the separate Top-30 `predictions` dataframe. Thus the original repair changed the wrong serializer. Run #397 head SHA was `c55c54226151a9acd973c415d98e02227f93dc0b`; artifact `14753496627`, SHA-256 `47483ec441ec52dc9df33aaa4e8f0b18cb7b1b05eb02adabbf1bf28679ae7160`.
- Corrected the actual Top-30 `predictions.append({...})` row serializer to include `FUT1_END_DATE`, `FUT3_END_DATE`, and `FUT5_END_DATE`. Commit `7360870b768a6ed746451afa96ea918a3bffae07`; file blob `548a61688446ca538feb6a538bd6f61eb629a17c`. Read-back confirms all three fields in the Top-30 block consumed by `pd.DataFrame(predictions)`.
- Added a regression test that checks the exact Top-30 serializer block as well as existing 49/50-observation and independent State/Target denominator tests. Test file blob `7013571db8c116d7774a1ee7be3d0d68b728814f`; latest associated test commit `da9c57b0d32b2850b335117c75d80e25a86e98c7`. Regression test execution is pending; do not mark PASS until the current queued workflow confirms it.
- Run #398 (`45027842316`) on source-fix commit `7360870b768a6ed746451afa96ea918a3bffae07` was **IN_PROGRESS** during this report update, currently in NSE history acquisition. Run #402 (`45027949881`) for the regression-test commit was **PENDING** in the workflow queue. These statuses must be refreshed before acceptance.
- C273 remains **NOT PASS**. The first repair commit `c55c542` is superseded for the actual Top-30 fix; do not cite it as the completed fix. Acceptance still requires a successful walk-forward step on code containing the Top-30 serializer fix, successful regression tests, and artifact-level numerator/denominator inspection. H+3 n<50 remains UNKNOWN.
