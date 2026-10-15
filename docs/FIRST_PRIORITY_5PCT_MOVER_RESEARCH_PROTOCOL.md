# PRECISION-WIRES V11.3 — First-Priority +5% Mover Research Protocol

**Status:** Research specification / audit-only. This document does not change the production selector, `RANKING_SCORE`, or the frozen `+1 PRESSURE_FADE` rule.

## 1. Primary objective

The first research priority is to identify Indian cash-market stocks that can achieve a **+5% move within the next one trading session (H+1)**. The news collection is deliberately narrow: use only items published in the **24 hours before the decision cutoff**. Do not collect years of news to solve a one-session prediction problem.

Historical price/volume data is still required to calculate indicators, establish the candidate universe, and evaluate outcomes. The 24-hour restriction applies to the news/catalyst layer, not to the technical-history panel.

## 2. Define the label before measuring performance

Use a frozen, timestamped decision cutoff for each session, and record the price at which a candidate could actually have been selected.

Report two separate outcomes so that an intraday excursion is not confused with a close-to-close gain:

1. **Primary target-touch label:** after the decision/entry cutoff, did the official NSE intraday HIGH reach at least +5% versus the recorded decision reference price during the next eligible trading session? A target touch counts only if the target was tradable after the decision time. If entry timing or intraday bars are unavailable, label the outcome `UNKNOWN`; do not infer a target touch from daily OHLC when the chronology is ambiguous.
2. **Secondary close label:** did the official NSE CLOSE finish at least +5% above the same reference price by the H+1 close?

Use official NSE prices where available. Adjust for corporate actions where relevant. Exclude or separately flag stocks with trading suspensions, circuits that prevent realistic entry/exit, severe liquidity constraints, or unresolved corporate-action price adjustments. Never silently treat missing data as a negative outcome.

## 3. News scope: last 24 hours only

Collect the minimum news needed for catalyst classification, with source URL and publication timestamp:

- Exchange filings and company announcements (NSE/BSE) first for stock-specific catalysts.
- Credible reports from Reuters, AP, BBC, Al Jazeera, Bloomberg, and reputable Indian business outlets.
- Fresh orders, earnings surprises, guidance, regulatory decisions, ownership/deal disclosures, material corporate actions, commodity shocks, policy changes, and genuinely market-moving geopolitical developments.

Deduplicate syndicated copies. Preserve original publication time, not scrape time. Separate confirmed facts from analyst interpretation. If a source is blocked, record it as unavailable and use a verified alternative; do not invent a headline. If no material story exists, set catalyst to `NO_MATERIAL_NEWS`, not a negative score.

## 4. Candidate pipeline

1. Freeze the session cutoff and universe.
2. Generate the technical/price-volume candidate pool using existing V11.3 logic.
3. Attach the last-24-hour news/catalyst evidence only to candidates with a verified match.
4. Evaluate price energy, relative strength, sector context, volume/absorption, breakout path, liquidity, circuits, and event risk.
5. Rank the audit candidates for the H+1 +5% objective; preserve existing production ranks and scores.
6. Apply live confirmation separately (opening integrity, volume/absorption, VWAP/ORB and sector/NIFTY context). A headline alone is never an entry signal.
7. Save a pre-outcome, append-only prediction ledger with cutoff, candidate, rank, sources, price reference, and label maturity date.

Macro, FII/DII, crude, FX, yields, VIX and geopolitical news remain risk/opportunity modifiers, not automatic hard rejection gates. Missing factor data means `UNKNOWN`.

## 5. Required evaluation

For each mature out-of-sample session and for the aggregate 100-session test, report:

- Precision = true positive candidates / all selected candidates.
- Recall/capture = true positive candidates selected / all true +5% movers in the eligible universe.
- Candidate count, number of true movers, false positives, missed winners, and unresolved labels.
- Top-10/Top-30 capture, sector and liquidity breakdown, and the distribution of missed +5% winners outside the selected set.
- Performance with and without the 24-hour news/catalyst layer, using the same cutoff, universe, price reference and label.
- Trading frictions: spread/slippage, volume capacity, circuit/entry feasibility, and whether the target was actually tradable.
- Confidence intervals or uncertainty notes; no claim of predictive value from a handful of examples.

Use chronological walk-forward evaluation and mature labels only. Avoid look-ahead leakage: no story published after the cutoff, no future revised filing, no post-outcome ranking edits. A candidate is not a winner merely because it appears in a retrospective list.

## 6. Relationship to the Macro-Geo event study

The publication-time macro/geopolitical event study is **secondary explanatory research**. It may describe broad market/sector responses to timestamped news, but it must not block the primary +5% mover study, and its output must not be fed into production ranking without separate validation.

Events dated after the latest available market-panel close must be written to an exclusions/pending report as `PENDING_PANEL_NOT_YET_AVAILABLE`; do not fail all otherwise valid observations because one current-day event has no following close yet. Events predating the panel must be marked `EVENT_BEFORE_PANEL_HISTORY`. If no mature event windows remain, return operational PASS with research BLOCKED—not a fabricated successful study.

## 7. Freeze and promotion rule

This is audit-only. Do not alter the production selector, `RANKING_SCORE`, or `+1 PRESSURE_FADE` based on this protocol alone. Promotion requires a separate review of prospective, mature out-of-sample results, missed-winner analysis, liquidity/circuit feasibility, and a documented decision.
