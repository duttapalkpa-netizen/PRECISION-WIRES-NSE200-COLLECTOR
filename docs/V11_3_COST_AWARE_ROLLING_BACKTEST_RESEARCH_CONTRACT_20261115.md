# V11.3 Cost-Aware Rolling Backtest — Research Contract (Draft, 2026-11-15)

## Status
RESEARCH SPECIFICATION ONLY — NOT IMPLEMENTED, NOT BACKTESTED, NOT ACCEPTED. No production selector, ranking, pressure-fade, or CORE-672 code is modified.

## Purpose
Define a reproducible, leakage-safe evaluation for +5% within H+1, +10% within H+3, +20% within H+5, using the user-stated 0.22% transaction-cost assumption and rolling/expanding walk-forward evaluation. No synthetic observations.

The inspected `pipeline/walk_forward_backtest.py` is explicitly labelled V11.4 and measures future HIGH-price excursions. It contains no 0.22% cost calculation or complete executable trade ledger. Gross hit-rate/lift must not be presented as net strategy returns.

## Non-negotiable invariants
1. Features at cutoff T use only observations dated at or before T.
2. Outcomes use only subsequent sessions up to the declared horizon.
3. A cutoff is eligible only when its full outcome horizon has matured; exclude the final five sessions for H+5.
4. Preserve actual symbol-session rows and provenance. No synthetic rows, fabricated dates, forward-filled executable prices, or fabricated fills.
5. UNKNOWN remains distinct from PASS/FAIL.
6. Report gross movement, costs, net return, hit rate, precision, recall, lift, and portfolio performance separately.
7. Do not change Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, or 672 diagnostics.
8. No paid API, spend, external contact, or PR merge without explicit approval.

## Cost convention
- Config key: `TOTAL_ROUND_TRIP_COST_PCT`.
- Required value: `0.22` percentage points (0.22%, not 0.0022 percentage points).
- Apply once per completed round trip: `NET_RETURN_PCT = GROSS_RETURN_PCT - 0.22`.
- Do not charge 0.22% separately on each side unless user confirms it is a per-side rate.
- Persist value, units, and convention in every run manifest and metrics file.
- This is a simplified all-in user assumption, not a broker-specific fee schedule. Slippage/market impact remain separately unmodelled unless explicitly parameterized with evidence.

## Frozen execution conventions (user-approved)
1. Signal cutoff is T; entry is the next global trading session OPEN.
2. Target is intraday HIGH touch at +5% H+1, +10% H+3, or +20% H+5.
3. Stop-loss is -3% from entry. If stop and target both touch in one OHLC bar, resolve conservatively as stop-first.
4. If neither target nor stop triggers, exit at the final session CLOSE of the declared horizon.
5. Apply 0.22 percentage-point total round-trip cost exactly once to completed trades.
6. Gap below stop exits at that session OPEN. Gap above target is filled at the observed OPEN (never at a better unobserved price).
7. A symbol missing any global session row, invalid OHLC, or zero/non-finite volume is NOT_EXECUTABLE/UNKNOWN; do not fabricate fills.
8. Circuit/price-band lock feasibility is not established by the inspected 200-session OHLC artifact. Until a verified restriction source is joined, report this as an explicit limitation and do not claim circuit-feasible execution.
9. Position sizing, overlapping positions, capital allocation and concurrency are not approved/defined. Report per-trade outcomes only; do not claim portfolio CAGR/drawdown.

These conventions are fixed for the isolated research simulator only and do not change production selector/ranking/pressure-fade/CORE-672 logic.

## Required per-trade ledger
`CUT_OFF, SYMBOL, SIGNAL_TIMESTAMP, ENTRY_SESSION, ENTRY_PRICE, ENTRY_STATUS, TARGET_PCT, HORIZON_SESSIONS, EXIT_SESSION, EXIT_PRICE, EXIT_REASON, GROSS_RETURN_PCT, COST_PCT, NET_RETURN_PCT, TARGET_HIT, STOP_HIT, EXECUTABLE, DATA_STATUS, SOURCE_FILE, SOURCE_ROW_OR_KEY`.
No executed-trade row without verifiable entry and exit prices. Non-executable rows remain visible with explicit status and null price/return fields.

## Required per-horizon metrics
Eligible/matured cutoffs; candidate/executable/excluded counts by reason; gross/net hit rates; mean, median and 5th/25th/75th/95th percentile net returns; win/loss ratio, average win/loss, expectancy; MAE/MFE where OHLC supports; precision, recall, base rate and lift with denominators; confidence intervals and cutoff dispersion; cost sensitivity at 0.00%, 0.22%, 0.44% (base remains 0.22%).

## Reproducibility manifest
Git commit SHA, script SHA-256, source artifact SHA-256, source rows, unique symbols/sessions, date range, parameter JSON/hash, cost convention, exclusions, output hashes, Python/pandas/numpy versions, and run ID.

## Minimum acceptance tests
1. +1.00% gross at 0.22% cost => +0.78% net; -1.00% gross => -1.22% net.
2. Cost applied exactly once per completed round trip.
3. Unit guard rejects ambiguous units and rejects 0.0022 when units are percentage points.
4. H+1/H+3/H+5 use exactly 1/3/5 subsequent trading sessions.
5. Last five sessions ineligible for H+5; no partial-horizon labels.
6. Perturbing post-T observations cannot change T features/rank/entry decision.
7. Training and calibration strictly time-ordered before cutoff.
8. Same-bar target/stop follows frozen conservative rule.
9. Gap-through-target fill respects executable OHLC bounds.
10. Missing/invalid OHLC, circuit lock, zero volume, absent symbol-session => no invented fill.
11. Duplicate symbol-date keys fail closed; date normalization deterministic.
12. Gross/net independently recomputable from ledger.
13. Metric denominators reconcile to ledger and exclusions.
14. Identical inputs/config yield byte-stable canonical outputs, excluding run IDs/timestamps.
15. Regression tests prove production selector/ranking/pressure-fade/672 files untouched.

## Verified gaps
- Current V11.4 walk-forward source uses future HIGH excursions and has no 0.22% cost calculation.
- Gross Top-30 precision is not net return or executable-trade performance.
- Inspected production 672 artifact has only 3 distinct column-state patterns across 672 columns; separate blocker.
- No inspected evidence establishes executable entry/exit, stop-loss, circuit-fill, or portfolio-capital assumptions.

## Acceptance gates
- G0 execution convention approval: PASS for the eight frozen per-trade conventions above; circuit/price-band feasibility remains an explicit data limitation, not a verified PASS.
- G1 isolated research-only implementation and unit tests: NOT_STARTED.
- G2 historical replay on verified source artifact with matured horizons: NOT_STARTED.
- G3 independent ledger arithmetic/hash reconciliation: NOT_STARTED.
- G4 0.22% base-case and sensitivity report: NOT_STARTED.
- G5 final paper eligibility: BLOCKED until G0–G4 and all other project hard gates pass.

## Safe next action
After CI runtime PASS, verify actual OHLC and signal input artifacts, provenance and hashes; only then run a bounded corrected replay. Do not reuse stale H+3/H+5 outcome labels. No performance claim before independent reconciliation.
