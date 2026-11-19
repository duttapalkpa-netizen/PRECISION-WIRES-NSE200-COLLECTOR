# Existing NSE Walk-Forward Outputs — Reuse, Maturity and GCR Join Feasibility
Date: 2026-11-19
Status: PARTIAL EVIDENCE RECOVERED; FULL HISTORICAL VALIDATION NOT VERIFIED; GCR JOIN BLOCKED

## Scope and no-redownload rule
- Reused the existing `audit/prospective-selector-tracking` branch source and committed append-only ledgers. No NSE data collection, download, workflow dispatch, or backtest rerun was performed.
- Walk-forward source: `pipeline/walk_forward_backtest.py`, branch blob SHA `df6e55a72f0e62e59d8de58eff7c58d17e2ec34b`.
- Workflow: `.github/workflows/prospective_watchlist_tracking.yml`, blob SHA `d26af3fd3415050fd16902656079c6747ebeae1c`; declared `timeout-minutes: 10`, and runs corrected-label walk-forward plus several historical exploratory audits.
- The workflow expects `data/processed/nse_eq_200_sessions.csv` and creates `outputs/backtest/walk_forward_metrics.json`, `walk_forward_universe_probabilities.csv`, and prospective audit JSONs. The current branch Git tree does not contain the processed NSE dataset or those generated metrics/probability JSONs. They may exist as Actions artifacts, but no artifact was recovered/verified in this review.
- Existing committed `outputs/prospective/watchlist_ledger.csv` was directly fetched and analyzed; blob SHA `fe35e72058fe45ff3a91dbe5b66c2e8199a2fdfe`. It contains 290 selector-pick rows, 29 cutoff dates (2026-10-02 through 2026-11-18), 131 distinct symbols; 145 rows per selector. The latest cutoff 2026-11-18 has 10 rows, with zero matured outcomes at H+1/H+3/H+5.
- Existing `outputs/prospective/daily_feedback_ledger.csv` has 28 rows (blob SHA `c6f71bcf3c8b622f320c08c4a132fb41fb51b1d4`). Its notes explicitly mark early per-stock outcome checks provisional, official NSE cross-check unresolved, and intraday data UNKNOWN. It is not a verified official-price outcome ledger.

## Recovered pooled target-hit rates (exploratory ledger-derived only)
The following are pooled hit counts divided by matured selected-pick rows, using the committed watchlist ledger's MATURED_* and target-hit fields. These are not full-universe recall, not independent cutoff-level confidence intervals, not executable returns, and not a complete V11.4 model validation.

| Selector | Target | Matured picks | Hits | Pooled hit precision | Unresolved rows |
|---|---:|---:|---:|---:|---:|
| CURRENT_WINNER_PROB | +5% H+1 | 135 | 36 | 26.67% | 10 |
| CURRENT_WINNER_PROB | +10% H+3 | 124 | 23 | 18.55% | 21 |
| CURRENT_WINNER_PROB | +20% H+5 | 111 | 14 | 12.61% | 34 |
| P10_P20_MEAN | +5% H+1 | 136 | 28 | 20.59% | 9 |
| P10_P20_MEAN | +10% H+3 | 124 | 28 | 22.58% | 21 |
| P10_P20_MEAN | +20% H+5 | 111 | 13 | 11.71% | 34 |

- The +5% H+1 exploratory result favours CURRENT_WINNER_PROB by 6.08 percentage points (26.67% vs 20.59%).
- The +10% H+3 result favours P10_P20_MEAN by 4.03 percentage points (22.58% vs 18.55%).
- The +20% H+5 result favours CURRENT_WINNER_PROB by 0.90 percentage points (12.61% vs 11.71%).
- Do not call these improvements statistically significant: no paired cutoff bootstrap CI or independent recomputation from the missing universe-probability source was available in this review.
- The 29 cutoff dates are historical exploratory cutoffs already inspected, not new prospective matured dates. The latest cutoff is wholly immature. The per-selector pick rows are repeated across cutoffs and sometimes the same symbol is present under both selectors; do not treat 290 rows as 290 independent market events.
- Recall/capture cannot be reliably computed from the selected-pick ledger alone because the complete eligible outside-Top-30 universe and its matured winners/denominator are not included here. False-positive counts are likewise not a full universe confusion matrix.
- These hit rates are based on forward HIGH excursion labels from the existing ledger, not entry/exit replay, not close-confirmed returns, and not net returns after cost.

## Code-level maturity/leakage findings
- The walk-forward source explicitly states features at cutoff T use rows <=T and outcome labels use T+1..T+h. The corrected `_forward_window_max` requires all h future observations; `FUT{h}_END_DATE` records the final future date used. This is the intended maturity gate.
- Historical audit code selects outside the frozen Top-30 and compares five picks per selector/cutoff; unresolved labels are excluded rather than treated as misses. The strict 30-cutoff audit is exploratory only and sets `promotion_authorized=false`.
- The pipeline also has a synthetic/rotating diagnostic-slot construction: 672 columns are populated by rotating 25 measurable feature families. This is not evidence that CORE-672 contains 672 independent, validated predictive signals.
- The committed `config/universe.csv` on this branch contains only the header `SYMBOL`; no explicit universe members are committed in that file at this ref.
- H+3 calibration minimum is 50 fully matured observations per State by prior user decision. Recovered aggregate pick counts are not per-State matured counts; therefore no State is certified calibrated by this analysis.

## GCR linkage feasibility
- **Technical feasibility: conditional YES.** The historical per-symbol cutoff feature/output panel can in principle be joined to a separately archived macro/sector panel on explicit as-of timestamps, and then to official sector/stock TRI outcomes using a verified symbol/sector crosswalk.
- **Current empirical join: NO / BLOCKED.** The recovered V11.4 pipeline is built from NSE symbol/date OHLCV/delivery-derived features and forward stock HIGH/CLOSE labels; no synchronized GCR macro factor panel, vintage timestamps, sector TRI panel, or validated sector crosswalk is present in the recovered historical ledger.
- `config/macro_factor_registry.csv` describes factor groups/proxies and `config/macro_geo_sector_transmission_map.csv` records conditional hypotheses. Their sector empirical status is `HYPOTHESIS_NOT_VALIDATED`; they are not joined observations or backtest features.
- No backfilled macro value may be joined to a cutoff unless its publication/availability timestamp and source vintage prove it was available by that cutoff. No daily forward-fill, retrospective revised-value leakage, guessed sector mapping, or causal claim.
- Consequently, GCR cannot currently be credited with, explain, or improve these V11.4 historical hit rates. GCR remains UNKNOWN/BLOCKED and must have its own separate scorecard.

## Exact next actions (reuse only; no new NSE collection)
1. Recover the existing GitHub Actions artifact for a successful `prospective_watchlist_tracking.yml` run containing `walk_forward_metrics.json`, `walk_forward_universe_probabilities.csv`, strict-30/multiwindow/20-cutoff JSONs, and reproducibility report. Verify artifact expiry, run ID, artifact ID, dataset manifest and SHA-256. Do not rerun the 10-minute workflow until artifact recovery is exhausted.
2. From the recovered probability file, recompute all target-specific matured denominators, TP/FP/FN/TN, full outside-Top-30 winner denominator, paired cutoff deltas and bootstrap CIs. Preserve the exact existing selector protocol; mark retrospective selection bias.
3. Recover the exact source dataset only from that existing artifact or already archived verified artifact. If absent/expired, stop and report dataset unavailable; do not download new NSE data under this instruction.
4. For a GCR pilot, first prove availability of the existing macro factor archive and official sector TRI archive with as-of publication timestamps, source vintages, exact index identifiers and defensible symbol/sector crosswalk. Then test one small overlapping historical window; until all gates pass, keep GCR UNKNOWN.

## Acceptance
- Existing selector-ledger evidence: RECOVERED / EXPLORATORY.
- Full V11.4 historical metrics and matured universe denominator: NOT_VERIFIED.
- V11.3 cost-aware replay: NOT_AUTHORIZED / NOT_RUN (G0 trade execution conventions still require user approval).
- GCR-to-V11.4 join: technically possible in principle, empirically BLOCKED.
- No new NSE data collected; no workflow dispatched; no production files/invariants changed.
- ₹0, free official sources only; no synthetic data; UNKNOWN is never PASS.
