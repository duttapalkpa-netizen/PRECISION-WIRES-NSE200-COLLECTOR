# Macro-Geo Source Policy Repair and Run #383 Cancellation — Continuation 251

Date: 2026-11-22
Branch: `audit/prospective-selector-tracking`
Run #383: `44992957027`
Run conclusion: `cancelled` (not a GitHub failure conclusion)
Run head: `6eed3272521cea3ab1b4eb255b55f5eeb3ceaabf`
Artifact: `14743330788`
Artifact SHA-256: `6c3fd376e7a1473e3ddc1f5ea58c18abcf92a46d8016e9a4bbd2105dd6953acb`

## Continuity and failure evidence
Read the Master Continuity Ledger and C250 source-policy audit before proceeding. Run #383 had 14 completed successful steps, including corrected-label walk-forward, 200-session NSE history, strict manifest validation, Security Master provenance, dataset QA, quarterly endpoint/schema audit, XBRL extraction, and normalized quarterly feature build.

The only active step at cancellation was `python pipeline/macro_geo_collect_p0.py`. The job log records:
`2026-11-22T06:26:25Z ##[error]The operation was canceled.`
The job conclusion is `cancelled`; no failed step was recorded. The artifact is partial and does not contain the expected Macro-Geo P0 collection manifest or repair report. Do not infer that P0 collection passed or that a code exception caused the cancellation.

Artifact QA confirms 200 raw NSE files, 200 sessions (2026-02-16 to 2026-11-20), 2,999 symbols, 100% delivery quantity and delivery percentage coverage, QA PASS. These completed stages are not repeated.

## C251 source-policy code repair
1. `pipeline/macro_geo_collect_p0.py`: benchmark/sector/India VIX series now record official-row counts separately. Yahoo-only observations remain `AVAILABLE_SECONDARY`; required P0 series gate now accepts only `AVAILABLE` rows with official observations.
2. `pipeline/macro_geo_repair_p0.py`: removed the community GitHub USD/INR mirror. If FRED USD/INR fails, group remains BLOCKED pending a verified direct official RBI/FBIL source. EIA Brent fallback remains identified as US EIA RBRTE official data. FRED observations are explicitly attributed to the Federal Reserve Bank of St. Louis and marked AVAILABLE. Repair aggregate status now requires AVAILABLE only.
3. Added five regression checks in `qa/test_macro_geo_official_source_policy.py` for secondary-source exclusion, official-row accounting, mirror removal, EIA identity, and strict repair acceptance.

## Commits
- Regression tests: `a88d001a03a88dae21015fbd11f7abe8ccb00b84`
- Collector official-row gate: `c38266fca0566d1244498625db43ad2b88456512`
- Repair mirror removal/strict gate: `0fa47564fbe532f66ed7d69ddff80faaefbe9517`
- FRED official provenance status correction: `e81aeb913f426917f27f602da926c1f56201478a`

## CI state
The source changes triggered Run #386, ID `44994006387`, head `0fa47564fbe532f66ed7d69ddff80faaefbe9517`. At report creation it was PENDING. A later commit (`e81aeb9...`) updated the same repair file and may cause a subsequent run; inspect the latest run and do not call this code CI-PASS until targeted tests and workflow evidence confirm it.

## Status
- Run #383 completed stages: PASS at step level.
- Run #383 overall: CANCELLED.
- C251 code: COMMITTED, CI VERIFICATION PENDING.
- Macro-Geo four-group completeness: UNKNOWN/BLOCKED until a complete run artifact and official source coverage prove otherwise.
- USD/INR direct official RBI/FBIL path: BLOCKED / not yet verified.
- GDELT/RSS remains media-publication discovery; its timestamps are not verified event-occurrence times.

## Next exact actions
1. Inspect latest run after C251 commits; retrieve logs and artifacts.
2. Run `python -m unittest qa.test_macro_geo_official_source_policy -v` and full QA suite.
3. Confirm EIA Brent fallback and FRED source labels in artifact; verify Yahoo cannot satisfy P0 gate.
4. Keep USD/INR BLOCKED if no direct official RBI/FBIL source is verified.
5. Update this ledger with exact final CI run, artifact ID, digest, and test results.

## Invariants
Audit branch only; ₹0 spend; no synthetic data, fabricated timestamps, third-party mirrors or access-control bypass. UNKNOWN/BLOCKED never PASS. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), and Engines A–E unchanged.
