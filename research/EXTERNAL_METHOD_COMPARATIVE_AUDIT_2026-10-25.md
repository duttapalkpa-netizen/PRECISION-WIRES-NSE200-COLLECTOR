# External Method Comparative Audit — 2026-10-25

## Safety and scope

This is a research-only audit note. It does **not** modify or replace the PRECISION-WIRES V11.3 production selector, `RANKING_SCORE`, frozen `+1 PRESSURE_FADE`, the 56 × 12 diagnostic architecture, Macro-Geo hard gates, or the Run #58 matured-outcome rule. No external strategy is approved for production use by this document.

Audit branch: `research/external-method-comparative-audit-2026-10-25`
Audit base commit: `fb9a60f50795791d443d70cb971eda9103dca6d9`

## Executive decision

| External method | Code-level observation | Historical-evidence status visible in the inspected repository | V11.3 disposition |
|---|---|---|---|
| `kumrohit/momentum_swing_india`: regime + volatility-adjusted momentum rank | Approximately 126-session momentum rank skipping the most recent 5 sessions; volatility adjustment; top quintile; trend, liquidity, 52-week-high proximity and entry triggers; index regime uses 50-EMA / 200-SMA. | The repository's own `docs/research_notes.md` explicitly lists a formal backtest of this exact rule set with adjusted Nifty 200 data and realistic next-open/slippage fills as an **open research direction**. Its research notes summarize external literature but do not establish that this exact implementation passed a reproducible out-of-sample test. | **Experiment-only candidate.** Conceptually complementary to V11.3 lead-time / relative-strength diagnostics, but do not insert its score into production ranking or impose its regime as a new hard gate. |
| `pkjmesra/PKScreener`: early-breakout / low-volume contraction | Its `docs/SCAN_WORKFLOWS.md` describes “volume is lowest in last N days” as an early-breakout detection signal. The project also lists consolidation, breakout, volume and VCP scanners. This is a screening heuristic, not by itself a complete trade rule. | The inspected workflow description documents the scan logic, but provides no isolated, reproducible historical result for this specific low-volume early-breakout signal that can be compared against V11.3's target-horizon labels. | **Feature hypothesis only.** Could be evaluated as a compression / supply-drying-up diagnostic in a separate research track. Do not treat low volume alone as bullish confirmation or a release condition. |
| `hardikjh/swing_trade`: backtest + risk framework | Entry is next trading day's open; trade walks forward through stop, target, or time stop; same-day stop is checked before target (conservative ambiguity handling); risk sizing uses a configured fraction of capital and stop distance; market and sector filters exist. | Its `LIMITATIONS.md` explicitly says transaction costs are not deducted, yfinance data can be imperfect, delisted names may be missing (survivorship bias), delivery data is absent, and the backtest assumes only one open position / first signal per day. Therefore its headline results cannot be accepted as net-of-cost, portfolio-realistic validation. | **Adopt selected test-design principles only, after local validation:** next-session execution, explicit same-bar stop/target convention, unresolved-trade exclusion, position-risk accounting, costs and drawdown reporting. Do not copy its thresholds or treat its results as evidence for V11.3. |

## Code references inspected

1. Momentum scanner:
   - README: https://github.com/kumrohit/momentum_swing_india/blob/main/README.md
   - Rules: https://github.com/kumrohit/momentum_swing_india/blob/main/docs/strategy.md
   - Research limitations / open work: https://github.com/kumrohit/momentum_swing_india/blob/main/docs/research_notes.md
2. PKScreener:
   - Workflow logic: https://github.com/pkjmesra/PKScreener/blob/main/docs/SCAN_WORKFLOWS.md
   - Scanner overview: https://github.com/pkjmesra/PKScreener/blob/main/README.md
3. Swing trade:
   - README: https://github.com/hardikjh/swing_trade/blob/main/README.md
   - Backtest engine: https://github.com/hardikjh/swing_trade/blob/main/src/backtester.py
   - Signal sizing: https://github.com/hardikjh/swing_trade/blob/main/src/signals.py
   - Parameters: https://github.com/hardikjh/swing_trade/blob/main/src/config.py
   - Explicit limitations: https://github.com/hardikjh/swing_trade/blob/main/LIMITATIONS.md
4. Existing V11.3 implementation inspected on the audit base:
   - Current provisional selector: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/audit/run93-corrective-fixes/pipeline/final_selection.py
   - Current event-study design (publication-time descriptive study, not a ranking engine): https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/audit/run93-corrective-fixes/pipeline/macro_geo_event_study.py
   - Macro-Geo workflow: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/blob/audit/run93-corrective-fixes/.github/workflows/macro_geo_p0_event_study.yml

## Compatibility with V11.3

- **Regime/momentum:** A slow, lagged momentum measure can be an additional diagnostic alongside the existing V11.3 signal set. It must not overwrite `RANKING_SCORE`, existing production ranking, or any frozen invariant. Any regime output must retain explicit `UNKNOWN` when input coverage is absent.
- **Low-volume early-breakout:** Treat contraction as a *setup* hypothesis only. It needs point-in-time volume history, a subsequent expansion/price-confirmation definition, and a false-breakout audit. It is not equivalent to a confirmed breakout and must not become a hard gate.
- **Backtest/risk:** Reuse only neutral evaluation practices in a separate research-only harness. Preserve V11.3's target labels (+2%, +5%, +10%, +20%) and matured H+1/H+3/H+5 outcomes; report other horizons separately and never score immature windows. Use next-session fills, explicit gap handling, conservative intraday stop/target ordering, realistic Indian costs/slippage, exposure constraints, drawdown, turnover, and a survivorship-aware point-in-time universe where the data permits.
- **Macro-Geo:** These three repositories do not repair the currently blocked historical event study. Do not bypass the hard gate or substitute recent RSS events for timestamped historical events with matured post-publication closes.

## Historical validation gate before accepting any feature

No method is accepted into production on the basis of README claims, a scan screenshot, or another repository's aggregate backtest. Run the following as a **separate, non-production experiment** using the canonical historical data and point-in-time information available in this repository:

1. Freeze a dated baseline snapshot of V11.3 outputs and verify hashes for the production selector, `RANKING_SCORE`, and `+1 PRESSURE_FADE`.
2. Generate candidate features without changing the baseline:
   - lagged 126-session volatility-adjusted momentum (exclude the latest 5 sessions);
   - low-volume contraction flag over a predeclared N-session window, with breakout confirmation kept as a separate feature;
   - risk-framework outputs for next-open entry, stop/target outcomes, time stop, costs and position-risk accounting.
3. For each candidate, compare baseline versus baseline-plus-feature on the **same symbols, dates, costs, and matured windows**. Report sample counts, coverage, +2/+5/+10/+20 target-hit rates by H+1/H+3/H+5 (and separately H+10/H+20 if available), MAE/MFE, time-to-target, false-breakout rate, turnover, net expectancy, drawdown, and performance by market regime.
4. Use chronological walk-forward splits, not random splits. Do not tune on the final holdout. Record unresolved / missing outcomes as unknown, not failures.
5. Require no leakage, no material coverage regression, stable out-of-sample improvement versus baseline, and all existing QA/hard gates passing before proposing any production change.
6. Append results and rejected hypotheses to the dated research ledger. Keep this experiment on its own branch until independently reviewed.

## What is and is not verified today

- Verified by source inspection: the stated rule concepts and the external repositories' documented limitations above.
- **Not verified:** a reproducible out-of-sample performance advantage for any of these methods on this repository's canonical NSE history; feature-level uplift against V11.3; and whether PKScreener's low-volume flag improves the 2/5/10/20% matured target outcomes.
- Therefore the current acceptance decision is **no production adoption yet**. The momentum feature, low-volume feature, and selected backtest conventions are approved only as candidates for an isolated comparative experiment. Production stays untouched until historical artifacts demonstrate improvement.

## Invariant checklist

- Production selector changed: **NO**
- `RANKING_SCORE` changed: **NO**
- Frozen `+1 PRESSURE_FADE` changed: **NO**
- UNKNOWN treated as negative: **NO**
- Synthetic / fabricated historical data used: **NO**
- Macro-Geo hard gate bypassed: **NO**
- External method promoted to production without local OOS evidence: **NO**
