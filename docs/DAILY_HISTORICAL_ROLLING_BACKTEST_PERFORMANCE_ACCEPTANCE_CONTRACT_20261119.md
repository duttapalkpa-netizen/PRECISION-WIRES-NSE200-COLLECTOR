# Daily Historical Rolling Backtest Performance Acceptance Contract
Date: 2026-11-19
Status: REQUIREMENT LOCKED; IMPLEMENTATION NOT YET VERIFIED

## Objective
Every daily research cycle must publish a reproducible, leakage-safe historical rolling-backtest scorecard for the currently validated research scope. The scorecard must show whether performance improved, deteriorated, or is statistically/operationally unchanged versus the previous comparable run. A daily report is not allowed to manufacture improvement by changing the sample, target, cost, universe, or denominator.

## Separate scorecards (never conflate)
1. V11.4 historical behavioural selector: target-excursion/label performance on matured historical cutoffs. Report Precision, Recall, F1, false-positive rate, missed-winner rate, target-hit rate, sample counts and confidence intervals, separately for +5% H+1, +10% H+3, +20% H+5 where supported.
2. V11.3 cost-aware trade replay: executable-style Win Rate, net return, expectancy, drawdown and cost sensitivity only after G0 entry/exit/stop/circuit/overlap/sizing assumptions are explicitly approved and the implementation is independently reconciled. Until then: NOT_AUTHORIZED / UNKNOWN; do not substitute selector hit rates.
3. GCR: its own predictive scorecard only after timestamp/vintage-aligned factors, official sector/stock TRI outcomes, defensible crosswalks and matured windows pass source-coverage gates. Until then: UNKNOWN / BLOCKED, not zero and not inherited from V11.4.

## Fixed rolling protocol
- Reuse the verified archived NSE historical dataset and existing outputs first; never redownload or rerun completed work without a documented reason.
- Each cutoff is a historical as-of date. Features and source values must have been available by that cutoff; no future leakage, revised-vintage leakage, or survivorship leakage.
- H+1/H+3/H+5 outcomes enter the denominator only after the full horizon has matured. Immature rows are excluded and counted separately.
- Keep the same universe, symbol eligibility, cutoff schedule, feature definitions, labels, target/horizon, costs, and execution assumptions across comparison runs. Any methodology change creates a new versioned series; do not compare it as a like-for-like daily improvement.
- Use chronological walk-forward/rolling windows, never random train/test splits for time-series claims. Record exact start/end cutoffs and per-window results.
- Deduplicate symbol/cutoff observations and publish exclusions/rejections with reason codes.
- Preserve raw source references, dataset hash, code commit, configuration hash, run ID, artifact ID, output hashes, timestamp and denominators.

## Daily scorecard fields
For each target/horizon and each rolling window: matured positive labels, matured negatives, eligible signals, TP, FP, FN, TN (where applicable), precision, recall, F1, false-positive rate, missed-winner rate, target-hit rate, coverage, confidence interval, and comparison with the prior like-for-like run. For approved trade replay additionally: gross/net return, costs, win/loss counts, expectancy, profit factor, max drawdown, exposure and overlapping-position assumptions.
Include a fixed-baseline comparison and a latest-window comparison. Show absolute percentage-point change and sample-count change. Mark improvement only when the same protocol and denominator logic are preserved; show uncertainty and avoid overclaiming statistical significance.

## Maturity and minimum sample rules
- H+3 behavioural calibration requires at least 50 fully matured observations per State, per the user's prior approval. Below 50 remains UNKNOWN/uncalibrated; do not lower threshold or synthesize observations.
- Other targets/windows must display actual n and confidence intervals. No PASS based solely on a small or immature sample.
- Never turn UNKNOWN, missing, stale, failed, or immature data into PASS or zero.

## Runtime and workflow policy
- Prefer short isolated jobs (20–60 seconds where feasible; hard ceiling 10 minutes for new audit jobs).
- Separate data validation, feature/label generation, metric aggregation, and hash/reproducibility checks into independently rerunnable jobs.
- Do not launch the existing 120-minute prospective workflow merely to obtain a daily scorecard. First inspect available workflow artifacts and reuse them.
- Publish a daily scorecard artifact and append a concise entry to the continuity ledger only after successful validation. Failed/partial runs publish status and blockers, never fabricated metrics.
- Daily cadence: use the already configured Nightly Rotation Backtest automation at 22:00 IST; do not create a duplicate schedule. This cadence is an intended trigger, not proof that the workflow or scorecard has been implemented.

## Acceptance gates
A daily scorecard is accepted only when:
A. verified dataset manifest and hashes exist;
B. exact cutoff and maturity filters are reproducible;
C. leakage and duplicate checks pass;
D. metric denominators reconcile to the trade/label ledger;
E. independent recomputation matches published metrics;
F. same-protocol baseline comparison is available;
G. all output files and configuration/code hashes are archived;
H. the run completes within the 10-minute limit.
Any failed gate => scorecard status BLOCKED/PARTIAL; no reliable performance rate claim.

## Current state at contract creation
- V11.4 exploratory walk-forward pipeline exists, but the latest audit did not retrieve/verify its output metrics artifacts. Candidate JSON output paths on audit/prospective-selector-tracking were not found as committed files; this does not prove workflow artifacts are absent.
- V11.3 cost-aware replay code exists, but G0 execution assumptions remain unapproved and no reconciled replay output was verified.
- GCR rolling performance remains BLOCKED/UNKNOWN due to missing synchronized factor-to-TRI outcome panel and validated crosswalk.
- Therefore current verified daily performance rate: NOT_AVAILABLE / UNKNOWN. Do not report an invented percentage.
- This contract locks the acceptance requirement; it does not claim implementation or backtest completion.

## Protected invariants
No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E, or IPO-PLX V2. ₹0 spend; official/free sources only; no synthetic data or fabricated timestamps; UNKNOWN is never PASS.
