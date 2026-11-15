# V11.3 Historical Signal Input-Lineage Audit
Date: 2026-11-15
Scope: research-only input compatibility check before running the cost-aware historical replay.

## Decision
**Historical replay input gate: BLOCKED / NOT_READY.** The replay unit tests pass, and the 200-session raw archive passes, but no verified historical V11.3 signal ledger with the required `CUT_OFF,SYMBOL` schema has been identified. Do not run the full replay using V11.4 predictions as a silent substitute.

## Inspected source files
- `pipeline/v11_3_abcd_e.py`, blob SHA `34ad08f130254a0e8c5f09ae5a0e2d93590757df`.
- `pipeline/walk_forward_backtest.py`, blob SHA `d085f7a2d35a88b4c4eaba65144a429a06961b09`.
- `pipeline/v11_3_cost_aware_backtest.py`, main blob SHA `32b556717dab70d0b37de69a6e3d98105edd1702`.

## Findings
1. The V11.3 candidate script reads `data/processed/nse_eq_200_sessions.csv`, sorts by symbol/date, calculates features, and then selects only `g.iloc[-1]` for each symbol. It writes a current/latest snapshot to `outputs/finalists/v11_3_candidates.csv` and `v11_3_top30.csv`. This is not a historical per-cutoff signal ledger and cannot by itself populate the replay's many historical `CUT_OFF,SYMBOL` rows.
2. The V11.3 script imports `add_features` and `add_tomorrow_features` from `pipeline.walk_forward_backtest.py`. The inspected `add_tomorrow_features` function uses same-row causal features (acceleration, relative strength, RVOL, delivery gap, compression, readiness and exhaustion); despite its name, the inspected function body does not read future OHLC rows.
3. However, the V11.3 candidate script optionally reads `outputs/backtest/behavioral_dna_library.json` and uses its `hit10_h3` state rates to calculate the calibration component of its score. The corresponding walk-forward code creates that library from outcome fields such as `FUT1_HIGH_PCT`, `FUT3_HIGH_PCT`, and `FUT5_HIGH_PCT`. A single full-sample library must not be reused at earlier historical cutoffs; that would leak future outcome information into earlier signal scores.
4. `pipeline/walk_forward_backtest.py` is explicitly labelled V11.4. Its `walk_forward_predictions.csv` is therefore not automatically an approved V11.3 selector signal source. Reusing only its `CUT_OFF,SYMBOL` columns would change the source engine and must not be silently represented as V11.3.
5. The isolated cost-aware replay accepts OHLC columns `SYMBOL,DATE,OPEN_PRICE,HIGH_PRICE,LOW_PRICE,CLOSE_PRICE,TTL_TRD_QNTY` and signal columns `CUT_OFF,SYMBOL`. Unit tests do not establish that real production-compatible inputs exist or that the replay has been run.

## Required next work
- Locate a genuine archived V11.3 selector output with cutoff timestamps and source/version provenance, if one exists.
- If no such archive exists, draft an isolated research-only historical signal adapter that evaluates the approved V11.3 rules at each cutoff using data available only through that cutoff. It must preserve the protected production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and engines A–E; it must not import future-derived full-sample DNA calibration into earlier cutoffs.
- Define a cutoff-safe calibration rule before coding. A valid design must use only matured outcomes available by that cutoff, with an explicit minimum sample threshold and a fail-closed/UNKNOWN fallback. Do not invent a fallback or silently alter the score formula.
- Validate cutoff isolation, symbol/session uniqueness, signal provenance, and maturity windows before running the full replay.
- Only after the signal input gate passes, run the bounded research-only replay and independently reconcile trade rows, exclusions, costs, metrics and output hashes.

## Progress
- Source inspection and input-lineage diagnosis: 100% complete.
- Compatible historical V11.3 signal ledger found: 0% / NOT_FOUND.
- Cutoff-safe signal construction specification: 0% / NOT_STARTED.
- Historical cost-aware replay: 0% / NOT_STARTED.
- Independent replay reconciliation: 0% / NOT_STARTED.

## Safety and scope
No production code, selector, ranking score, pressure fade, CORE-672 diagnostic definitions, engines A–E, or production workflow changed. No synthetic signals, no guessed timestamps, no paid APIs, no spend, and no PR merge.
