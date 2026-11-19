# Run #407 Row-Level Walk-Forward Recovery and Integrity Audit — 2026-11-20

## Executive verdict
**ROW-LEVEL DATA RECOVERED; INTEGRITY REVIEW PARTIAL / NOT PASS.** A successful existing NSE workflow artifact contains the processed 200-session dataset, 3,000 Top-30 prediction rows, 251,724 full-universe probability rows and 9,182 missed-winner diagnostic rows. No workflow was dispatched and no new data was collected in this audit.

## Artifact provenance and byte integrity
- Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`
- Workflow: NSE Historical Backbone + Adaptive V11.3 + IPO-PLX
- Run #407 / ID `44542948987`; branch `main`; head SHA `d013577157bc1f24322cd100aaf60c40a20c4d17`; conclusion SUCCESS.
- Job `collect-and-test`: completed SUCCESS.
- Artifact ID `14539426731`; name `precision-wires-adaptive-407`; size 61,902,773 bytes; expires 2027-02-17T14:22:02Z.
- GitHub artifact digest and independently recomputed ZIP SHA-256 match: `b958d9184eb2df4715364b5825d243593c1c9d9d1290a171ae3ab2833950dfd7`.
- Key file SHA-256:
  - `data/processed/nse_eq_200_sessions.csv`: `b59b6c5410d4182c718c9e1010acb727ab0c607b4e9030568264d204a9308470`
  - `outputs/backtest/walk_forward_predictions.csv`: `06dc89983aa748bae5e03eee8e3ad4be5bd2add008e5b00dc350e5e65399d843`
  - `outputs/backtest/walk_forward_universe_probabilities.csv`: `b46de0967bd22ef548f6ee27550386160d8d3967c9aeb4680be5b807f7f612e1`
  - `outputs/backtest/walk_forward_metrics.json`: `9a79719ec8482953044cae38b6ab9329c20849fef64b69dfd85e81c3d3b99061`
  - `outputs/backtest/missed_winner_lab.csv`: 3,784,320 bytes; SHA-256 `6c97f7c452a49f14309a4a8958ed98ca8812311b19f14cbe4eae5b08d79c5867`
  - `data/qa/qa_report.json`: SHA-256 `81d21799277b651d63e736ff5a1e6267e15ba04dbd7849cf1f737228a3d57c36`
  - `data/processed/symbol_session_coverage.csv`: SHA-256 `7ddeab2d31eb52c52de55662d1361bf8e68850ab86a11e2a375584c2642f7ecc`
- ZIP contains no source dataset manifest. The computed hashes above are a recovery audit record, not a substitute for the original collector manifest/provenance.

## Recovered dataset shape and structural QA
- Processed dataset: 200 sessions, QA JSON says 2,997 symbols, 100% delivery quantity and delivery percentage coverage, final selection data ready, issues empty.
- Prediction table: 3,000 rows, 100 cutoffs (2026-06-26 through 2026-11-12), exactly 30 rows per cutoff, no duplicate rows, one missing `FUT1_HIGH_PCT`.
- Full-universe probability table: 251,724 rows, 100 cutoffs, no duplicate keys. Missing values: 295 each in RECOVERY_SCORE / SEPARATION_SCORE / RARE20_SPECIALIST_SCORE / RANKING_SCORE; 297 LATENT_WINNER_EVIDENCE; 178 FUT1_HIGH_PCT; 2 WINNER_INTERACTION_SCORE. H+3 and H+5 outcome columns have no missing values.
- Missed-winner lab: 9,182 rows across 100 cutoffs and 1,958 distinct symbols; reasons: RANKED_OUT 6,611; LOW_WINNER_PROBABILITY 2,552; CONTAMINATED 19. This lab is specifically built for missed +10% H+3 and/or +20% H+5, not H+1.

## Independent Top-30 confusion matrix against the recovered eligible full universe
Labels: FUT1_HIGH_PCT >= 5%; FUT3_HIGH_PCT >= 10%; FUT5_HIGH_PCT >= 20%. Selected set is the 30 recorded prediction rows per cutoff. Rows with unknown H+1 outcome are excluded from the H+1 denominator.

| Target | TP | FP | FN | TN | Precision | Eligible-universe recall | Eligible base rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| +5% H+1 | 648 | 2,351 | 21,871 | 226,676 | 21.61% | 2.88% | 8.95% |
| +10% H+3 | 1,198 | 1,802 | 8,537 | 240,187 | 39.93% | 12.31% | 3.87% |
| +20% H+5 | 612 | 2,388 | 1,454 | 247,270 | 20.40% | 29.62% | 0.82% |

These are excursion-hit labels from historical OHLC maxima, not executable entry/exit returns, not net of slippage/taxes, and not prospective validation. Low recall on H+1 and H+3 means Top-30 covers only a small share of all eligible winners.

## Metric consistency blocker
The bundled `walk_forward_metrics.json` reports:
- Precision: H+1 21.60%, H+3 39.93%, H+5 20.30%.
- Recall: H+1 2.74%, H+3 11.50%, H+5 29.06%.
- Base rate: H+1 9.16%, H+3 4.04%, H+5 0.81%.

Independent recomputation from the paired prediction/full-universe CSVs gives the table above. H+1/H+3 recall and base-rate differences are consistent with a denominator-scope difference: the source code computes recall/base rate using all rows in `all_by_date`, while the universe CSV is built after history-depth and feature-availability filters. This must be explicitly named as broad-market denominator versus eligible-selector denominator. H+5 precision also differs (20.30% in JSON versus 20.40% from the CSV rows); the JSON implies 609 hits while the prediction CSV contains 612 rows at/above 20%. This remains an unresolved artifact-internal discrepancy and blocks an overall PASS until the exact source calculation / serialization is reconciled.

## State sample guardrail
Full-universe state counts:
- NON_STRONG 88,319
- FALSE_STRENGTH 57,511
- HIDDEN_WINNER_RECOVERY 49,166
- ALREADY_EXPANDED 27,655
- NOT_YET_MOVED 12,774
- REPRICING_PRESSURE 6,728
- STRONG 6,470
- EXPANSION_READY 2,085
- CONTINUATION_READY 992
- DATA_CONTAMINATED 24

The >=50 fully matured-observation rule is not met for DATA_CONTAMINATED (24); it must remain UNKNOWN / uncalibrated. Other listed states exceed 50 rows, but a complete per-state calibration acceptance still requires explicit maturity/eligibility verification and state-specific calibration metrics. Do not change the threshold.

## Important diagnostic findings (shadow only)
- Top-30 is dominated by HIDDEN_WINNER_RECOVERY (2,872 rows) and CONTINUATION_READY (128 rows). The former has 1,184 +10% H+3 hits and 608 +20% H+5 hits; the latter 14 and 4 respectively. Descriptive only; state distribution is not evidence for production reweighting.
- Missed winners include high-excursion cases whose probability percentile/ranking did not secure Top-30 slots (examples in the row-level lab include MENONBE, CHEMCON, OMAXE, PPL, GNRL, SAKSOFT; identities must always be interpreted with their cutoff dates).
- Exact false-positive and missed-winner rows are now recoverable from the paired CSVs; a later analysis can generate cutoff-clustered confidence intervals and diagnostic attribution without another data collection.

## Decision and next action
- Artifact recovery: PASS (ZIP digest verified; required row-level CSVs present).
- Structural row-level QA: PARTIAL (missing values and source manifest gaps documented).
- Metric consistency: BLOCKED (H+5 precision discrepancy; recall/base-rate denominator definitions need formal reconciliation).
- Strategy performance / executable return validation: NOT_ESTABLISHED.
- GCR: UNKNOWN/BLOCKED; this artifact is not evidence of GCR predictive performance.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or IPO-PLX changes.
- Next: audit the exact denominator and metric serialization from the same source snapshot; then calculate cutoff-clustered paired bootstrap intervals and false-positive / missed-winner driver summaries. No new NSE collection is needed for that analysis.
