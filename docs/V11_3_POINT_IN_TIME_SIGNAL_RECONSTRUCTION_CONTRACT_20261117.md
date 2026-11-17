# V11.3 Point-in-Time Historical Signal Reconstruction — Research Contract

Date: 2026-11-17
Status: SPECIFICATION CHECKPOINT — implementation/replay NOT_STARTED; no acceptance claim.
Branch: research/v11-3-pit-signal-reconstruction-20261117

## Purpose
Create a research-only historical signal ledger by reconstructing the V11.3 A/B/C/D/E candidate logic separately at every historical NSE session cutoff. The ledger must not reuse V11.4 Top-30 winner-separation predictions as if they were V11.3 production signals, and must not use a current/latest candidate snapshot as historical data.

## Verified input artifact
Representative existing archive: GitHub Actions Run ID 43687120198, artifact ID 14151241008.
Input: data/processed/nse_eq_200_sessions.csv
Rows: 502,150; unique sessions: 200; symbols: 2,994.
Date range: 2026-02-09 through 2026-11-13.
Columns include SYMBOL, SERIES, OHLC, TTL_TRD_QNTY, DELIV_QTY, DELIV_PER, DATE, listing/history metadata.
Input CSV size: 83,264,515 bytes.
Input CSV SHA-256: 00a1b3af4c6be836cf5ad18c9332607701b5418a7057f2a0415c202458d3dbb0.
This is a verified representative artifact input, not yet independently proven to be the final accepted V11.3 signal source.

## Point-in-time rules
1. For cutoff T, calculate features and candidate scores using rows dated <= T only.
2. Recompute the approved A/B/C/D/E candidate formula at each cutoff; do not copy the single latest outputs/finalist snapshot across historical dates.
3. Do not import the V11.4 Top-30 prediction file as V11.3 signals. V11.4 outcomes may not be used as a substitute for V11.3 candidate selection.
4. Behavioral-DNA calibration at cutoff T may use only historical rows whose complete H+3 outcome is matured by T. H+3 must use the next three global NSE sessions; if a symbol lacks any of those exact sessions, that observation is ineligible for calibration.
5. Per-state minimum: 50 fully matured observations. Below 50, status is UNKNOWN / UNCALIBRATED; do not lower the threshold, synthesize rows, or promote the state to PASS.
6. No future information may enter feature generation, state assignment, calibration, ranking, or cutoff selection.
7. Keep every candidate row, including A/B/C/D/E booleans, component scores, calibration sample count/status, and explicit cutoff/symbol keys. Do not restrict the historical ledger to Top-30.
8. Preserve the agreed research execution policy for the later simulator: entry next global trading session OPEN; target intraday HIGH touch; stop-loss -3%; stop-first on same-bar ambiguity; stop gap at observed OPEN; horizon-end CLOSE if neither target nor stop; deduct 0.22 percentage points once per completed round trip.
9. Circuit/price-band execution cannot be claimed unless a separately validated historical restriction source is joined. Slippage/market impact remain unmodelled and must be disclosed.
10. This work is research-only. No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A-E, or production workflow changes. No PR merge or production integration without explicit user approval.

## Required output and provenance
- v11_3_point_in_time_signals.csv: all cutoff × eligible symbol rows, deterministic ordering.
- v11_3_point_in_time_calibration_audit.json: per-cutoff/per-state matured counts, calibration status and exact eligible horizon rule.
- manifest with source artifact SHA-256, code commit, row/symbol/session counts, date range, parameters, output SHA-256 values and exclusions.
- Explicit distinction between UNCALIBRATED, NOT_EXECUTABLE, UNKNOWN, PASS and FAIL.

## Minimum tests before replay
- Post-cutoff perturbation cannot change any earlier cutoff feature, score, state or signal.
- Every signal row has cutoff date <= every feature input date.
- H+3 calibration only counts exact next-three-global-session observations matured by cutoff.
- Missing any symbol session in the H+3 window excludes that calibration observation.
- 49 matured observations => UNKNOWN; 50 => eligible for calibration.
- No use of V11.4 Top-30 labels or future outcomes in V11.3 signal selection.
- Duplicate SYMBOL/DATE, invalid dates, invalid OHLC and non-traded bars fail closed or remain explicitly excluded.
- A/B/C/D/E values and component score arithmetic independently reconcile to the approved V11.3 formula.
- Identical input/config produces deterministic signal CSV and manifest payload (excluding runtime-specific metadata).
- Regression check confirms protected production files and workflows are unchanged.

## Acceptance sequence
A. Contract/source audit: COMPLETE for this specification checkpoint.
B. Isolated point-in-time generator implementation: NOT_STARTED.
C. Unit and leakage tests: NOT_STARTED.
D. Historical signal reconstruction: NOT_STARTED.
E. Cost-aware H+1/H+3/H+5 replay: NOT_STARTED.
F. Independent ledger arithmetic/hash reconciliation: NOT_STARTED.
G. Final acceptance: BLOCKED until B-F and all project hard gates pass.

## Known adjacent evidence — do not repeat
- Cost-aware replay unit-test workflow Run #7, ID 43696699661, completed SUCCESS. This validates the current simulator unit tests only, not historical replay.
- The current cost-aware module has no historical V11.3 signal source. The inspected 200-session archive has a current V11.3 candidate snapshot and separate V11.4 historical predictions; neither alone is a valid point-in-time V11.3 historical ledger.
- Existing V11.4 metrics are gross future-HIGH winner-separation statistics, not net V11.3 executable trade returns.
- Existing production diagnostics_672.py still requires its own independent signal-definition/evidence acceptance; this task must not patch it.

## Progress
- Existing artifact source/schema audit: 100% for this bounded review.
- Point-in-time signal contract: 100% for this specification checkpoint.
- Generator implementation: 0%.
- Leakage/unit tests: 0%.
- Historical reconstruction: 0%.
- Cost-aware replay and independent reconciliation: 0%.
- Overall project percentage: NOT_CALCULABLE pending full weighted acceptance ledger reconciliation.
