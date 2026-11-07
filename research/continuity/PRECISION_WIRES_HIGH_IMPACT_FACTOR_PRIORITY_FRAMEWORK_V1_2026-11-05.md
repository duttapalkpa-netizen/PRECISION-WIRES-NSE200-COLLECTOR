# PRECISION-WIRES V11.3 — High-Impact Factor Research Priority Framework v1
Date: 2026-11-05
Scope: research-only prioritisation overlay; no production code or selector changes.

## Purpose and interpretation
The 100% → 90% → 80% → 70% → 60% → 50% → 40% tiers are **research-priority hypotheses**, not measured predictive contributions, model coefficients, score weights, pass thresholds, or claims of causal impact. They determine the order and depth of evidence collection and validation. No factor receives a validated contribution percentage until out-of-sample evidence supports it.

## Initial high-impact research queue
| Priority tier | Factor families to test first | Research questions |
|---|---|---|
| 100% | Price structure, price/volatility expansion, range compression and breakout quality | Does the price/volatility state lead 1–5 session expansion, and is the signal stable across market regimes? |
| 90% | Relative volume (RVOL), volume expansion, VWAP behaviour, delivery quantity/percentage | Does participation confirm price expansion, and does delivery distinguish accumulation from transient turnover? |
| 80% | Relative strength versus NIFTY 50/NIFTY 500, sector strength, sector leadership and breadth | Does stock/sector leadership add incremental predictive lift beyond price and volume? |
| 70% | Accumulation, absorption, supply exhaustion, tightness/base quality and demand persistence | Does evidence of absorption improve precision and reduce adverse excursion? |
| 60% | Fresh catalysts, corporate announcements, earnings/results, order wins, policy/event repricing and timestamped news | Does a verified catalyst improve lead time and target-hit probability after publication/session-cutoff controls? |
| 50% | Effective float, free float, liquidity, turnover, spread/slippage proxies and supply velocity | Which float/liquidity states support executable expansion without creating unrealistic backtest fills? |
| 40% | Market regime and macro/geopolitical context as risk modifiers (NIFTY trend, India VIX, global risk, rates, FX, commodities, policy shocks) | When do these variables change conditional hit rates, drawdowns or failure risk? They remain modifiers, not automatic stock rejection rules. |

Factors below 40% remain in the later queue (30% → 10% → 1% → 0.1%) and must not displace the high-impact validation sequence.

## Validation protocol
1. Freeze the data cutoff and feature-availability timestamp for every prediction. No look-ahead, revised-vintage leakage, or post-cutoff catalyst use.
2. For each tier and factor family, run separate 24-month and 12-month rolling walk-forward tests. Training, validation and test windows must be chronological and non-overlapping at each fold.
3. Evaluate target labels at +2%, +3%, +5%, +10%, +15% and +20% within H+1, H+3 and H+5 trading sessions, with explicit entry/exit, gap, circuit, liquidity and transaction-cost assumptions.
4. Report sample count, coverage, precision, recall, target hit rate, false-positive rate, MFE, MAE, time-to-target, expectancy after costs, calibration, lift over baseline, confidence intervals and regime-wise stability.
5. Perform ablation (remove one factor family at a time), incremental-lift tests, correlation/collinearity checks and selected interaction tests. Correlation is not causation.
6. Preserve UNKNOWN separately from PASS/FAIL. Missing or stale sources cannot be silently imputed as negative evidence. Macro variables remain risk modifiers.
7. Promote a factor from a research tier only after reproducible OOS evidence, source provenance, stable results across both rolling horizons and an independent reproduction check. Record negative and null findings.

## Data/provenance requirements
Every factor observation must retain source, source URL or source identifier, publication/release timestamp where relevant, observed/retrieved timestamp, reference period, vintage/revision status, symbol/ISIN mapping where relevant, missingness state and payload/file SHA-256. News/catalyst features must obey publication-time and trading-session cutoffs. Historical macro data must preserve release vintages.

## Separation from production
This document is an isolated research-priority overlay only. It does **not** change or authorize changes to:
- Production Selector
- RANKING_SCORE
- +1 PRESSURE_FADE
- PRECISION-WIRES V11.3 CORE-672 (56 × 12 diagnostics)
- Engines A/B/C/D/E or opportunity-preservation rules
- Hard Gate conditions

No factor is enabled in production by virtue of its tier. Research results must first be reviewed and explicitly approved through the existing release process.

## First execution order
Start with the 100%, 90% and 80% tiers on a common frozen dataset; then 70%, 60%, 50% and 40%. Run 24-month and 12-month OOS folds for every tier. Keep source coverage and sample attrition visible; do not call a factor “high impact” solely because it has a high in-sample correlation.
