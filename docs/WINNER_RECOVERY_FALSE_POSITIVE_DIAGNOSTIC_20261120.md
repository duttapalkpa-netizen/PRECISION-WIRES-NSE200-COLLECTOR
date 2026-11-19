# Winner Recovery and False-Positive Diagnostic — Existing Artifact Only
Date: 2026-11-20
Status: DESCRIPTIVE DIAGNOSTIC COMPLETE; NO MODEL CHANGE; SHADOW EXPERIMENT NOT YET RUN

## Scope and provenance
- Source is the already recovered GitHub Actions artifact `prospective-watchlist-audit`, run #319 / ID 40112393704, artifact ID 12566997895, branch `audit/prospective-selector-tracking`, head SHA `7d7faaa3e50e216f4fc6cacfe75b88d3c58b4381`.
- Artifact ZIP SHA-256 matched GitHub digest: `00a990117ac19971396eb5c039cb73c103e40f7ac3d1c93f31ca4839c6e56b7e`.
- Inspected `walk_forward_metrics.json`, `watchlist_ledger.csv`, `qa_report.json`, and exact source `pipeline/walk_forward_backtest.py` at branch ref. No NSE data collected; no workflow dispatched; no production file changed.
- The run conclusion remains CANCELLED. Its summary JSON and QA PASS do not change the workflow conclusion or authorize promotion.

## Key interpretation correction: two different probability diagnostics
- `winner_probability_separation` in the metrics JSON is calculated on the Top-30 prediction frame only, classifying H+3 +10% winners vs non-winners. Its mean gap is -0.000216 (winner 0.086364 vs non-winner 0.086580): the generic `WINNER_PROBABILITY` is not separating the selected Top-30 rows.
- `full_universe_probability_calibration` is a separate target-specific, time-split Platt-calibrated probability panel. Its mean winner-minus-nonwinner gaps are positive: T5_H1 +0.008946; T10_H3 +0.003695; T20_H5 +0.000611. These are full-universe calibration statistics, not Top-30 ranking separation. The code explicitly keeps these diagnostics separate.
- Therefore the earlier statement that winner/non-winner probabilities were "almost indistinguishable" applies to the generic Top-30 `WINNER_PROBABILITY` only; it must not be conflated with target-specific full-universe probabilities.

## State-level diagnostic within the Top-30 prediction sample
Rows sum to 3,000 (100 cutoffs × 30 picks). Rates are historical high-excursion hit rates; no cutoff-level CI is available.

| State | Rows | +5% H+1 | +10% H+3 | +15% H+5 | +20% H+5 |
|---|---:|---:|---:|---:|---:|
| CONTINUATION_READY | 2,541 | 34.23% | 23.32% | 15.75% | 7.96% |
| HIDDEN_WINNER_RECOVERY | 459 | 28.05% | 19.18% | 12.14% | 7.04% |

- CONTINUATION_READY exceeds HIDDEN_WINNER_RECOVERY by 6.18 pp (+5 H+1), 4.13 pp (+10 H+3), 3.61 pp (+15 H+5), and 0.92 pp (+20 H+5).
- The smaller HIDDEN_WINNER_RECOVERY sample has lower hit rates on all four reported targets. This identifies a useful audit priority, not proof that the state is intrinsically inferior: the metrics lack per-cutoff paired intervals and the 459 rows are clustered across dates/symbols.
- Median generic winner probability is 0.08620 for CONTINUATION_READY and 0.09013 for HIDDEN_WINNER_RECOVERY, while median percentile is 99.11 and 99.67 respectively. The percentile/state ranking is not transparently monotonic with realised hit rates. Audit percentile and score construction before changing weights.

## Transition-signature diagnostic within Top-30
| Signature | Rows | +10% H+3 | +15% H+5 | +20% H+5 |
|---|---:|---:|---:|---:|
| DEMAND_CONFIRMATION | 1,222 | 24.96% | 16.28% | 8.31% |
| EXHAUSTION_BUILD | 283 | 19.71% | 13.53% | 5.26% |
| PRESSURE_BUILD | 194 | 20.43% | 12.71% | 7.73% |
| PRESSURE_FADE | 371 | 22.66% | 15.08% | 8.31% |
| STABLE_TRANSITION | 930 | 21.04% | 14.83% | 7.78% |

- DEMAND_CONFIRMATION has the highest recorded +10% H+3 (24.96%) and +15% H+5 (16.28%) rates.
- EXHAUSTION_BUILD has the lowest rates for all three targets; relative to DEMAND_CONFIRMATION it trails by 5.25 pp, 2.75 pp and 3.04 pp respectively.
- PRESSURE_FADE is not uniformly weak: its +20% H+5 hit rate (8.31%) is effectively tied with DEMAND_CONFIRMATION (8.31%). This descriptive result is not grounds to change the protected +1 PRESSURE_FADE rule.
- PRESSURE_BUILD has only 194 rows and EXHAUSTION_BUILD 283; treat these estimates as low-sample exploratory, not stable ranking evidence.

## Winner-recovery diagnosis and next highest-value experiment
1. Primary audit hypothesis: HIDDEN_WINNER_RECOVERY is underperforming because its recovery score/state assignment may admit too many weak or late candidates. Test this as a non-production shadow challenger only; do not remove the state or change the live selector.
2. First recover the missing `walk_forward_predictions.csv` and `walk_forward_universe_probabilities.csv` from an existing successful, non-cancelled run artifact. They are absent from run #319 ZIP. If unavailable, stop rather than rebuild from newly collected data.
3. With full row-level files, produce per-cutoff state/signature counts, precision, recall, FP/FN and paired bootstrap confidence intervals; deduplicate/cluster by cutoff and symbol as appropriate. Separate target horizons.
4. Compare current ranking against fixed, pre-registered shadow variants: (a) exclude or down-weight EXHAUSTION_BUILD only in shadow; (b) retain DEMAND_CONFIRMATION and PRESSURE_FADE as separate strata; (c) revise HIDDEN_WINNER_RECOVERY thresholds only as a candidate. Do not optimize thresholds on the same evaluation window.
5. Acceptance: improvement must be repeatable on chronological held-out cutoffs, with positive paired precision delta and no unacceptable recall/coverage deterioration. Also require minimum sample and cost-aware validation before any promotion. H+3 per-State calibration still requires at least 50 fully matured observations.
6. Diagnose `WINNER_PROBABILITY` vs target-specific P5/P10/P20 fields and percentile rank: report rank correlation, decile hit rates, Brier/ECE and calibration by cutoff. The current summary JSON is insufficient to infer which weight change improves ranking.
7. If existing row-level artifacts cannot be recovered, record NOT_AVAILABLE; do not run new NSE collection or infer missing row-level false positives.

## Decision
- Winner Recovery / False-Positive descriptive diagnosis: COMPLETE from available summary metrics.
- Full false-positive identity list, missed-winner identity list, per-cutoff paired uncertainty and shadow challenger test: BLOCKED / NOT_AVAILABLE pending row-level existing artifacts.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2: unchanged.
- GCR remains UNKNOWN/BLOCKED; no GCR attribution.
- V11.3 cost-aware replay remains NOT_AUTHORIZED / NOT_RUN.
- ₹0; official/free sources only; no synthetic data; UNKNOWN is never PASS.
