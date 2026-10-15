# Run #57 / #89 Findings and Next Stage

**Branch:** `audit/prospective-selector-tracking`  
**As of:** 2026-10-15  
**Status:** completed audit runs; historical findings only; no production promotion.

## 1. Execution verification

- Run #57 (Macro-Geo P0): SUCCESS. The event study reports `COMPUTED_EXPLORATORY`, 4,103 panel rows across 11 series, 29 eligible events and 88 event-window rows. This is exploratory market-context research, not a causal estimate.
- Run #89 (Prospective Watchlist Audit): SUCCESS. All listed workflow steps completed, including strict dataset QA, corrected-label walk-forward, target-first H+1 +5% selector experiment, reproducibility check, latest label-free picks, and prospective-ledger append.
- Dataset QA: 200 raw files / 200 sessions / 200 processed dates; 2,950 symbols; delivery quantity and delivery percentage coverage each 100%; no QA issues.
- Reproducibility check: `PASS_BYTE_FOR_BYTE_REPRODUCIBLE`.
- Artifacts: [Run #89 prospective-watchlist-audit](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/38745608920/artifacts/11981988823) and [Run #57 macro-geo-p0-event-study](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/38745402233/artifacts/11980373239).

## 2. Primary +5% H+1 findings

Target definition in this experiment: next eligible session high at least +5% above the frozen cutoff reference price. The comparison is retrospective, uses 30 fully labelled cutoffs and selects five names per cutoff from outside the frozen `RANKING_SCORE` Top 30.

| Selector | Hits / 150 picks | Pooled precision | Mean daily capture |
|---|---:|---:|---:|
| Current winner-probability baseline | 38/150 | 25.33% | 0.7179% |
| P10/P20 mean | 23/150 | 15.33% | 0.4152% |
| P5/H1 only | 48/150 | 32.00% | 0.8978% |
| P5/H1 exhaustion-guarded | 42/150 | 28.00% | 0.7757% |

These are **historical exploratory** metrics, not live win rates or guaranteed returns. The P5/H1-only selector leads this specific 30-cutoff comparison on pooled precision and mean capture, but it is not approved for production. Before interpreting the apparent lift as robust, inspect the full artifact confidence intervals, per-cutoff variability, false positives/missed winners, liquidity/circuit feasibility and leakage controls.

A separate strict 30-matured-cutoff comparison found that the current winner-probability selector beat the P10/P20-mean selector for the +5% H+1 target: pooled precision 24% vs 14%; paired mean precision difference -10 percentage points for P10/P20 mean, with its 95% interval [-16.67 pp, -3.33 pp]. That reinforces that H+3/H+5 objectives must not replace the primary H+1 +5% target.

## 3. Macro-Geo result and data limitations

Run #57 completed the event study with `COMPUTED_EXPLORATORY`; 29 events were eligible and no events were pending or excluded before panel history in that run. It remains descriptive because event selection can be biased, windows overlap, no matched-control design/multiple-testing correction is present, and publication timestamps/headlines are proxies rather than independently verified causal events.

Run #89 still reports critical source gaps: 34 sources inventoried, 5 available and 29 not connected. Several official or publisher feeds can be blocked/unavailable. A missing or blocked source must remain `UNKNOWN`; do not interpret it as no catalyst. Macro-Geo stays secondary and must never gate the H+1 selector.

## 4. Next stage — stock-specific last-24-hour news ablation

**Start with an audit-only feature-readiness and join stage; do not alter ranking yet.**

1. Freeze each historical cutoff and decision timestamp. Build a canonical stock-news/filings table with at least `SYMBOL`, `PUBLISHED_AT` (timezone-aware), `PUBLISHER`, `HEADLINE`, `CANONICAL_URL`, `SOURCE_TYPE`, `VERIFICATION_STATUS`, and deduplication key.
2. Join only stories published in the 24 hours strictly before that cutoff. Prevent post-cutoff information leakage. Exchange/company disclosures take priority; use trusted media where accessible. Store unavailable feeds and missing timestamps as `UNKNOWN`, not negative.
3. Keep the technical history long enough for price/volume, EMA, relative strength, liquidity and market-structure features. The 24-hour restriction applies only to news/catalyst evidence.
4. Run paired, same-cutoff experiments: (A) price/volume-only baseline; (B) identical baseline plus the last-24-hour stock-specific news feature. Same universe, reference prices, labels, and eligible cutoffs.
5. Report precision, recall/capture, false positives, missed +5% winners, Top-10/Top-30 capture, per-cutoff bootstrap intervals, sector/liquidity/circuit breakdown, news coverage and UNKNOWN rate. A no-news label is allowed only when coverage is adequate and the search window is actually observed.
6. Add a separate prospective shadow ledger that records picks before outcomes. Mature labels only after the next eligible session is complete. No retrospective label may enter selection.
7. Promotion gate: require robust paired improvement across cutoffs, full reproducibility, leakage QA, feasible liquidity/circuit/entry assumptions, and explicit review. Until then, all results remain exploratory.

## 5. Immutable safeguards

- Do not modify production `RANKING_SCORE`.
- Do not modify the frozen `+1 PRESSURE_FADE`.
- Do not make Macro-Geo a hard gate.
- Do not use future labels in ranking or prospective picks.
- Do not claim intraday tradability from daily OHLC alone.
- Do not claim successful news ablation until a symbol-level news table and paired result artifact actually exist.
