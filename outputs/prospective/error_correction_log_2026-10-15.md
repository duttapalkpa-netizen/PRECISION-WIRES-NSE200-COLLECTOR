# PRECISION-WIRES Daily Error-Correction Record

- Recorded at: 2026-10-15 (Asia/Kolkata)
- Target session reviewed: 2026-10-14 cutoff -> 2026-10-15 outcomes, plus 2026-10-13 cutoff -> 2026-10-14 outcomes.
- Evidence status: provisional workbook-derived OHLC/volume/delivery; official NSE cross-check pending. First-hour VWAP/opening/volume/breakout-hold data unavailable, therefore UNKNOWN. Do not describe these outcomes as official-verified.
- Production invariants: do not modify production selector, `RANKING_SCORE`, or frozen `+1 PRESSURE_FADE` based on this retrospective feedback. Keep retrospective and prospective evidence separate. UNKNOWN is not negative.

## Observed failures / near misses

1. KOTYARK (cutoff 2026-10-13; both selectors rank 2): next-session high +3.609%, close -1.998% vs reference; gap-up then close below reference. Corrective lesson: a positive opening gap is not breakout confirmation; require reliable first-hour VWAP/volume/hold evidence or label UNKNOWN.
2. MADHUCON (cutoff 2026-10-13; both rank 3): high +4.975%, narrowly below +5%; close +2.488%; turnover noted around ₹0.99 lakh. Corrective lesson: never round a near miss into a hit; apply a liquidity/slippage eligibility check before actionable labels.
3. POLICYBZR (cutoff 2026-10-13; both rank 5): high +0.544%, close -0.656%. Corrective lesson: selector consensus is not sufficient evidence of next-session expansion; retain catalyst, market/sector and confirmation checks.
4. FOCUS (cutoff 2026-10-14; current rank 2, P10/P20 rank 3): high +0.874%, close -2.398%, volume ratio 0.572x. Corrective lesson: weak relative volume plus close deterioration should prevent a confirmed-breakout label; do not alter score post hoc.
5. PNCINFRA (cutoff 2026-10-14; current rank 1, P10/P20 rank 2): gap-down, high below reference, close -3.775%, volume ratio 0.069x. Corrective lesson: explicitly log gap failure and volume contraction; wait for confirmation rather than relying on rank.
6. TAKE (cutoff 2026-10-14; current rank 5): opened about -4.974% gap, high +4.974%, close +4.974% vs reference; near miss, not a +5% hit. Corrective lesson: exact threshold comparisons, and flag large opening gaps as separate risk.
7. TAMBOLIIN (cutoff 2026-10-14; P10/P20 rank 4): high +3.844%, volume ratio 0.276x, low turnover. Corrective lesson: liquidity and participation must be disclosed; high delivery percentage alone is not proof of demand or tradability.
8. UDAYJEW: next-session row unavailable. Outcome remains UNRESOLVED; never infer missing prices/outcomes.
9. USK (cutoff 2026-10-14; current rank 3, P10/P20 rank 5): high +7.387%, but close -0.685% vs reference and volume ratio 0.126x. Corrective lesson: distinguish high-touch target hit from close-confirmed/actually tradable outcome; reversal risk must be explicit.

## Mandatory process changes for every next-session report

- First retrieve the immediately prior saved watchlist and ledger; compare every named pick, including user-supplied names, against official NSE OHLC/close/volume and delivery where available.
- Verify cutoff date and target trading session; if the next calendar day is not a trading day, use the next actual session.
- Reconcile external prices against official NSE bhavcopy before calling a close verified. If official source or prior watchlist is unavailable, mark comparison UNRESOLVED and report the block.
- Do not infer first-hour VWAP, opening-gap behavior, volume confirmation or breakout-hold from daily candles. If reliable intraday data is missing, mark each field UNKNOWN.
- Separate target-high touch, close-based result, and confirmed/actually tradable breakout. Never round near misses into hits.
- Add liquidity/turnover, spread/slippage, circuit and surveillance checks; UNKNOWN must remain UNKNOWN, not a pass or a fail.
- Freeze each day's cutoff, picks, selector ranks/consensus and forecast before the next session; append outcomes in a new dated row only. Do not rewrite historical rows or backfill hindsight into forecasts.
- Calculate H+1 +5%, H+3 +10%, H+5 +20% only when each horizon is mature; report precision, recall/capture, missed winners and costs/liquidity/circuit effects only when universe-level data supports them.
- Do not promote selectors or change production `RANKING_SCORE` based on this feedback alone. Preserve production selector and frozen `+1 PRESSURE_FADE`.

## Status

This is a process-error record, not proof that GitHub Actions automatically executes the loop. The daily workflow must explicitly consume this record and append the next dated feedback record. Current observed data remain provisional pending official NSE reconciliation.
