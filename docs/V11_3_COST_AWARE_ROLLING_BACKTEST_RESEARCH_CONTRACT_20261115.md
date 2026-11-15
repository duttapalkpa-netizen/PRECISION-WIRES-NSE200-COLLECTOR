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

## Decisions required before executable trade simulation
The inspected source has OHLC fields and target horizons, but does not fully define tradable entry/exit rules. Code must not silently choose:
1. Entry timing/price (e.g. next-session OPEN or another rule).
2. Intraday HIGH-touch target versus close-confirmed target.
3. Exit on target touch, horizon close, stop-loss, or another rule.
4. Stop-loss rule or explicit NO_STOP disclosure.
5. Same-bar target+stop ambiguity; conservative stop-first unless intraday sequence evidence exists.
6. Gap-through-target fill rule; never assume a better fill than OHLC supports.
7. Circuit/price-band/illiquid/no-trade and missing OHLC handling: no assumed fill; mark NOT_EXECUTABLE/UNKNOWN and count exclusions.
8. Position sizing, overlapping trades, capital allocation and concurrency. Until defined, report per-trade outcomes only; do not claim portfolio CAGR/drawdown.

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
- G0 user-approved entry/exit and stop/circuit conventions: BLOCKED pending decision.
- G1 isolated research-only implementation and unit tests: NOT_STARTED.
- G2 historical replay on verified source artifact with matured horizons: NOT_STARTED.
- G3 independent ledger arithmetic/hash reconciliation: NOT_STARTED.
- G4 0.22% base-case and sensitivity report: NOT_STARTED.
- G5 final paper eligibility: BLOCKED until G0–G4 and all other project hard gates pass.

## Safe next action
Obtain explicit approval for trade simulation conventions. Until then, do not encode execution assumptions or publish net-performance claims.
