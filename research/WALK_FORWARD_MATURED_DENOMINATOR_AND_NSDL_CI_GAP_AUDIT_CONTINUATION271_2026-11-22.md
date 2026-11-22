# Walk-Forward Matured-Denominator and NSDL CI Gap Audit — C271

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`
Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`

## Continuity / live dependency
Re-fetched the Master Continuity Ledger and reports C268, C269 and C270 before work. Current ledger blob SHA: `b48f491e67624fe043340a53ae2bb989f7e06838`; C270 blob SHA: `3d1d92312d148017d3d27c9f604c78e182d6828e`. PASS archive QA and manifest work was not repeated.

Run #318 / ID `45014759390`, head `399b0a61535f84bfbee8347321e51c590ff9ff55`, was re-polled twice. It remains `in_progress`, updated_at `2026-11-22T10:55:27Z`; steps 1–7 SUCCESS, step 8 P0 market/media collection IN_PROGRESS, steps 9–19 pending. NSDL step 11 has not started. No artifact or completion conclusion exists. Because the workflow uses concurrency group `macro-geo-p0-audit-v5` with `cancel-in-progress: true`, no duplicate run or edits to its workflow/collector were made.

## Highest-value read-only methodology findings
Inspected `pipeline/walk_forward_backtest.py` and `.github/workflows/prospective_watchlist_tracking.yml` at current branch HEAD.

1. Forward outcomes are based on next observed sessions T+1..T+h, and training labels require `FUT{h}_END_DATE < cutoff`. This is a positive no-look-ahead control in the inspected code; it is not by itself a full independent audit of every feature.
2. The Top-30 state report currently writes `rows = len(g)` for each state, while target hit rates call `_hit_rate`, which drops missing outcomes. Thus `rows` is not the matured denominator for each target. A state can have fewer fully matured H+3/H+5 outcomes than its displayed row count. It is therefore unsafe to use this field as proof of the user-required >=50 matured observations per State.
3. The script does not currently emit per-state, per-target matured numerator/denominator fields or an explicit calibration eligibility flag tied to the >=50 fully matured observations rule. This is a reporting/acceptance gap, not evidence that any state has passed.
4. The main Top-30 precision/lift uses valid outcome rows in the selected top-30 and a full-universe base rate on valid outcomes. The `winner_probability_separation` block is computed only on Top-30 `pred`; the separate full-universe calibration block is computed on `universe_pred`. These populations must remain separately labeled. The C270 near-zero Top-30 winner/nonwinner mean gap is not a full-universe calibration result.
5. The current workflow runs `python -m unittest discover -s qa -p "test_*.py" -v` before the walk-forward job. The new `qa/test_macro_geo_nsdl_flows.py` should therefore be included by discovery on that prospective workflow, but the dedicated Macro-Geo workflow's regression command explicitly lists only `qa.test_macro_geo_engine qa.test_macro_geo_repair_p0`; the NSDL regression is not explicitly wired into that workflow command. No change made while Run #318 is active.
6. NSDL unit tests cover failed-date visibility, the FPI-vs-DII alignment distinction, and status semantics. These are test fixtures only, not research observations.

## Status
- PASS: continuity re-fetch; read-only source inspection; existing workflow command identified; no duplicate workflow.
- IN_PROGRESS: Run #318, still at step 8.
- BLOCKED / pending evidence: NSDL exact date response for 2026-07-17 and 2026-08-26; official daily USD/INR history; mature event windows.
- UNKNOWN: state-specific matured sample eligibility until denominators are explicitly reported and verified.
- No code or workflow changes in C271. No new data or artifacts claimed.

## Rejected / guardrails
- Rejected treating state `rows` as matured sample size.
- Rejected interpreting Top-30 probability gap as full-universe calibration.
- Rejected claiming the >=50-per-State threshold has passed without target-specific matured denominators.
- No guessed NSDL POST contract, no host switch, no inferred flows, no monthly-to-daily USD/INR conversion, no synthetic event windows, no paid APIs.
- Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged.

## Exact next actions
1. Poll Run #318 until completion; inspect NSDL step 11, attempt log, coverage status and artifact; independently verify artifact SHA-256.
2. After Run #318 is no longer active, add `qa.test_macro_geo_nsdl_flows` explicitly to the Macro-Geo workflow regression command, then run targeted tests/CI and verify PASS.
3. In the audit-only walk-forward report, add per-state and per-target matured denominators, numerators, and explicit `CALIBRATED` only when >=50 fully matured observations exist; otherwise `UNKNOWN`. Keep production selector and score invariants unchanged. Add regression tests for incomplete horizons and state-specific denominators.
4. Reconcile C270's Top-30 winner separation with full-universe calibration using exact populations and matured labels; do not treat hit-rate lift as profitable trade return.
5. Continue official NSDL date-response and FBIL daily USD/INR evidence checks. Wait for genuine post-publication NSE closes before event study. Re-run strict hard gate only after source evidence changes.
