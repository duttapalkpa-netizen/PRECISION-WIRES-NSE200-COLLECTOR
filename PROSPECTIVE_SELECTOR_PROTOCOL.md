# Prospective Selector Protocol — Audit Only

## Frozen baseline and boundary
- Production \`main\` stays frozen at \`4188644b59e3aa335d23911a8bd250865afda871\`.
- This workflow runs only on \`audit/prospective-selector-tracking\`; it does not edit ranking weights or replace Top-30 picks.
- Top-30 selection remains based on the existing \`RANKING_SCORE\`.
- The outside-Top-30 watchlist has five names per selector and cutoff.

## Pre-registered comparison
- Primary comparator: \`CURRENT_WINNER_PROB\`.
- One primary challenger: \`P10_P20_MEAN\` (mean of \`P10_H3_PCTL\` and \`P20_H5_PCTL\`).
- Both lists are generated without reading future outcomes. Other selectors are descriptive only and are not eligible for this experiment's promotion gate.
- Each \`(CUT_OFF, SYMBOL, SELECTOR)\` pick is append-only. Rank, score, and source hash are never rewritten after capture.
- Outcomes are filled only when the full forward horizon exists: max high over T+1..T+1 for +5% H+1, T+1..T+3 for +10% H+3, and T+1..T+5 for +20% H+5. Missing/incomplete outcomes remain unresolved, not negative.

## Promotion gate
Collect at least 20 new, fully matured prospective cutoff dates, preferably 30. No retrospective cutoff used to choose the challenger counts toward this total. Report each target separately:
1. paired daily precision delta and 95% date-bootstrap CI;
2. paired winner-capture/recall delta and 95% CI;
3. valid pick counts and missing/maturity counts;
4. Top-30 remains unchanged; report its results as context, not as an arm that was modified;
5. no promotion unless the challenger meets the pre-registered precision threshold (at least +1% relative point estimate), the lower 95% paired precision-delta bound is non-negative, and winner capture does not decline. All three targets are evaluated separately; any failure blocks promotion for that target.

The +1% relative precision threshold is a target, not a guaranteed result. This is not a profitability guarantee: a later risk-adjusted backtest must include costs, liquidity, slippage, gaps and circuit constraints. The ledger is research evidence only, not a trading instruction.
