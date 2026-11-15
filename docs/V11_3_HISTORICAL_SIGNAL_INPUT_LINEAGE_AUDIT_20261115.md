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


## Superseding resolution — 2026-11-15
The earlier NOT_FOUND / NOT_STARTED checkpoint is superseded by the final evidence below. The final replay did not reuse Run #146's processed data: it rebuilt the processed file from raw archive Run #4 and enforced exact 200/200 session-date equality. See the Page 29 final evidence section in the continuity ledger and the completed scoped report.


## 2026-11-15 — Page 29 final historical-signal, replay and selection-quality evidence (supersedes earlier NOT_STARTED checkpoint)

### Verified source lineage
- Raw archive source: workflow Run #4 / ID `43734398604`, artifact ID `14170166475`, SHA-256 `3c15ceb5cd6cb3270515090eb8393d22f8ca609a6032d0d7e128c5b78fb57494`; manifest PASS, 200 raw files, 200 sessions, 2026-01-21 through 2026-11-13.
- IMPORTANT REJECTION: processed dataset from earlier Run #146 did not have the same 200-date set as the verified raw archive. It is not accepted as the final replay input. Final workflow now downloads Run #4's raw archive, rebuilds the processed dataset from those exact raw files, and asserts exact raw-session/processed-DATE equality before signals are generated.
- Final processed dataset: 500,733 rows; 2,997 symbols; 200 sessions; first 2026-01-21; last 2026-11-13; delivery quantity and delivery percentage coverage both 100%; QA PASS, no issues, final-selection data readiness true. SHA-256 `8c433c8163dd5a52faf02ffe29e77571043c5791716c65d8c04cfca98ee857b1`.

### Historical V11.3 research signals
- Added `pipeline/v11_3_historical_signals_research.py` on the research branch. It evaluates cutoff-causal features and the V11.3 A/B/C/D/E feature/score structure; it does not call or change the production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, or production workflows.
- Adaptive RET20 now matches the V11.3 `min(20, history_depth-1)` rule. Calibration uses only H+3 labels whose full three-session window matured before the current cutoff. Minimum 100 matured samples/state is a research-only threshold; below it remains UNKNOWN. Calibration label is next 3 consecutive global-session HIGH excursion >=10% from cutoff CLOSE.
- Final signal manifest PASS: 484,985 scored cutoff-symbol rows; 5,880 selected signals; 196 cutoffs; max 30 per cutoff. Signal SHA-256 `0e57446e98c372fb832bcfa5a4957791142e88a8f10bacc04e3dc61a945a0df3`; full calibration audit SHA-256 `8ac7fd3f1c1f7727778603f64d52c89261085ded03c55775f5b8a3356d7af435`.
- Four cutoff-safe regression tests PASS, including adaptive RET20 and UNKNOWN/fail-closed calibration tests.

### Cost-aware replay and independent execution audit
- Final replay workflow Run #16 / ID `43738312823`, branch commit `6c4432962efa278ec5ea7f8e9aa93c92c31bdbbc`, artifact ID `14171590981`, artifact SHA-256 `c57469193b0f0fb6019202409b819118388a25897f0b698463f25a4e359a1360`.
- 17,640 trade rows; 17,023 executable; 617 excluded. Per horizon: H+1 5,802 executable / 78 excluded; H+3 5,676 / 204; H+5 5,545 / 335.
- Execution: next global session OPEN; targets +5/H1, +10/H3, +20/H5; -3% stop; intraday HIGH target; stop-first same-bar ambiguity; no target/stop exits at horizon close; one-time 0.22 percentage-point round-trip cost. Slippage/impact not modelled.
- Independent audit PASS, blockers=[]; execution reconciliation errors=0; net arithmetic errors=0; exclusion policy errors=0. Trade ledger SHA-256 `05773a572055f7018220ceaf8581cde95bac83b64bb8c6d0005d268563c23670`; metrics SHA-256 `3b813a5b6b825dc4a20c75a46d3e4c468a45bd865500d2c3f6b4bc409e4a7daf`; independent audit JSON SHA-256 `56a00314ab0417fd6b4548dc828319dbc92babbdc60a408d5f793cb072f9cf51`.
- Base 0.22% cost mean net returns: +5/H1 `-0.8127%`; +10/H3 `-0.8767%`; +20/H5 `-0.9262%`. Mean net returns remain negative at 0.00%, 0.22%, and 0.44% cost. Profitability gate is therefore BLOCKED; no production/trading promotion.

### Full-universe selection-quality and cost-sensitivity audit
- Audit workflow Run #1 / ID `43738744068`, commit `a07126551632acdc48ed6c49e88fa771b87dd754`, artifact ID `14171208561`, artifact SHA-256 `253295eedd33d6e01df880d2f38e3f0e4be38d7153b31207b58d5c7cc2ddb9aa`; status PASS, blockers=[].
- H+1: precision 12.87%, recall 2.02%, lift 1.68x, FDR 87.13%, missed winners 36,228.
- H+3: precision 9.04%, recall 1.91%, lift 1.60x, FDR 90.96%, missed winners 26,317.
- H+5: precision 2.83%, recall 1.89%, lift 1.59x, FDR 97.17%, missed winners 8,132.
- Non-overlapping cohort drawdown proxy: H+1 -57.78% (98 cohorts), H+3 -34.56% (49 cohorts), H+5 -25.70% (32 cohorts). This is explicitly a cohort proxy, not a capital-constrained overlapping portfolio drawdown.
- Selection-quality JSON SHA-256 `79ef94ebcc14c5c465354270c9ab7a71cfa6c99f32102243c886cbe33cf00971`.

### Research report and acceptance state
- Completed scoped report: `docs/V11_3_HISTORICAL_SIGNAL_COST_AWARE_BACKTEST_RESEARCH_REPORT_20261115.md`, commit `65d6c3352763181b529045cdd044456e56ade530`.
- Scoped progress: raw-to-processed lineage 100% PASS; research signal generation 100% PASS; replay execution 100% complete; independent execution audit 100% PASS; full-universe quality/cost audit 100% PASS; scope-specific report 100% complete.
- Profitability acceptance: BLOCKED (negative expectancy, low recall, high false-discovery rate). Full production-selector equivalence: NOT ESTABLISHED. Project-wide final paper/release: BLOCKED by separate Macro-Geo Step 4 / Factor Registry and CORE-672/system-wide acceptance gates; this work package does not close them. Overall project percentage remains NOT_CALCULABLE.
- Calibration/execution basis mismatch is explicitly retained as a limitation: calibration target is measured from cutoff CLOSE, while replay target is measured from next-session OPEN. Future work must test an execution-aligned matured label without altering production logic.
- PR #37 remains Draft/Open/Unmerged. No merge or production integration. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and engines A–E remain unchanged. Research spend ₹0; no paid APIs or synthetic data.
