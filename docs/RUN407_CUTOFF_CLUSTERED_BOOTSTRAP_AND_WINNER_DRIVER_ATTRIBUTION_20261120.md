# Run #407 Cutoff-Clustered Bootstrap and Winner Driver Attribution — 2026-11-20

## Scope and integrity
- Source: successful NSE workflow run #407, run ID `44542948987`, commit `d013577157bc1f24322cd100aaf60c40a20c4d17`, artifact ID `14539426731`.
- Artifact SHA-256 independently recomputed: `b958d9184eb2df4715364b5825d243593c1c9d9d1290a171ae3ab2833950dfd7`, matching GitHub's artifact digest.
- Files inspected: `walk_forward_predictions.csv` (3,000 rows; 100 cutoffs × 30), `walk_forward_universe_probabilities.csv` (251,724 rows; 100 cutoffs), `missed_winner_lab.csv` (9,182 rows), `walk_forward_metrics.json`, and the 200-session processed NSE CSV.
- No data collection, workflow dispatch, or production-selector change was performed.
- Bootstrap: 20,000 paired resamples of the 100 cutoff clusters, seed 20261120, percentile 95% intervals. Cutoffs—not individual stock rows—were resampled to preserve within-cutoff dependence.

## Top-30 pooled results and cutoff-clustered 95% CIs
| Target | TP | FP | FN* | TN* | Precision | Precision 95% CI | Recall* | Recall* 95% CI | Lift* | Lift* 95% CI |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| +5% H+1 | 648 | 2,351 | 21,871 | 226,676 | 21.61% | 19.34–24.07% | 2.88% | 2.61–3.17% | 2.41× | 2.19–2.67× |
| +10% H+3 | 1,198 | 1,802 | 8,537 | 240,187 | 39.93% | 36.80–43.20% | 12.31% | 11.58–13.12% | 10.33× | 9.75–10.95× |
| +20% H+5 | 612 | 2,388 | 1,454 | 247,270 | 20.40% | 18.30–22.70% | 29.62% | 26.95–32.58% | 24.86× | 22.63–27.28× |

*Important denominator qualification:* these TP/FP/FN/TN and recall/lift calculations use the exported 251,724-row universe file. The source metrics JSON computes recall/base-rate against its internal `all_by_date` frame, which is larger/different: JSON recalls are 2.7439%, 11.4993%, 29.0553%, versus exported-universe recomputations 2.8776%, 12.3061%, 29.6225%. The source code at the artifact commit explicitly calculates `universe` and `base_rate` from `all_by_date=df[df.DATE.isin(cutoffs)]`, while the universe CSV is written from `universe_pred`. Therefore precision is independently reproducible from the Top-30 file, but recall/FN/TN/lift are provisional until the internal all_by_date denominator and exported universe are reconciled. Do not present the starred values as final validated full-market recall.

## Paired subgroup attribution within Top-30 (descriptive, 100 cutoff clusters)
### State
| State | n | +10% H+3 hit | Paired difference vs all other Top-30 rows, 95% CI | +20% H+5 hit | Paired difference vs others, 95% CI |
|---|---:|---:|---:|---:|---:|
| CONTINUATION_READY | 128 | 10.94% | -30.36 pp [-36.30, -24.17] | 3.13% | -18.09 pp [-21.83, -13.79] |
| HIDDEN_WINNER_RECOVERY | 2,872 | 41.23% | +30.33 pp [+24.23, +36.37] | 21.17% | +18.11 pp [+13.68, +21.91] |

### Transition signature
| Signature | n | +10% H+3 hit | Paired difference vs others, 95% CI | +20% H+5 hit | Paired difference vs others, 95% CI |
|---|---:|---:|---:|---:|---:|
| DEMAND_CONFIRMATION | 133 | 16.54% | -24.45 pp [-31.05, -17.57] | 3.01% | -18.26 pp [-21.82, -14.28] |
| EXHAUSTION_BUILD | 348 | 44.25% | +4.82 pp [-1.30, +10.88] | 14.66% | -6.55 pp [-11.01, -1.84] |
| PRESSURE_BUILD | 183 | 18.03% | -23.34 pp [-29.71, -16.55] | 7.65% | -13.62 pp [-17.76, -8.78] |
| PRESSURE_FADE | 1,327 | 51.85% | +21.36 pp [+17.58, +25.11] | 25.85% | +9.74 pp [+6.63, +12.77] |
| STABLE_TRANSITION | 1,009 | 29.83% | -15.21 pp [-18.90, -11.50] | 19.82% | -0.86 pp [-3.89, +2.29] |

These are exploratory subgroup associations within an already selected Top-30 sample, not causal effects or evidence to change ranking logic. In this artifact, PRESSURE_FADE is the strongest observed signature for H+3/H+5 among selected rows. This does not authorize changing protected +1 PRESSURE_FADE logic.

## Missed-winner and false-positive driver evidence
- Missed-winner lab contains 9,182 rows: `RANKED_OUT` 6,611 (72.0%), `LOW_WINNER_PROBABILITY` 2,552 (27.8%), `CONTAMINATED` 19 (0.2%).
- Of these, 7,827 are labelled `10_H3`, 710 `10_H3+20_H5`, and 645 `20_H5`.
- `TOP_DRIVER_GAPS` is populated for 5,685 rows (61.9%): RELATIVE_STRENGTH;PROGRESSION 4,344, PROGRESSION 718, RELATIVE_STRENGTH 623. It is missing for 3,497 rows; no inference should be filled into those gaps.
- Median diagnostics in missed-winner rows: POSITIVE_DIAGNOSTICS 10 (median), NEGATIVE_DIAGNOSTICS 1. Thus many misses were not devoid of positive signals; ranking/relative ordering and progression gaps are plausible audit targets, not proven causal drivers.
- Top-30 H+3 winners versus non-winners: median RVOL20 3.42 vs 2.11; RS5 -10.43 vs -6.35; RS20 -13.39 vs -16.54; RET5 -11.03 vs -6.72; EXHAUSTION_RISK 50.37 vs 42.71. Top-30 H+5 winners show median RS5 -19.12 vs -6.66, RS20 -19.49 vs -14.07, RET5 -19.82 vs -7.02, and EXHAUSTION_RISK 52.33 vs 43.95. These are unadjusted medians, not independent feature effects.
- In missed-winner lab, `RANKED_OUT` median WINNER_PROBABILITY_PCTL 91.74 and RANKING_SCORE 84.73; `LOW_WINNER_PROBABILITY` medians are 46.02 and 46.63. This suggests separate ranking-order and probability-generation failure modes warranting shadow-only analysis.

## Decision and next action
1. **Do not tune production.** The evidence is descriptive and denominators are not fully reconciled.
2. Next highest-value audit: reconcile `all_by_date` versus `universe_pred` row membership and forward-label construction; export an explicit cutoff-level denominator ledger with matured counts, eligible rows and winner counts.
3. Then repeat paired bootstrap on the reconciled full universe and run a chronological shadow-only challenger focused on rank-order / progression and relative-strength misses.
4. Keep the 50 fully matured observations per State rule for H+3 Behavioral DNA calibration. The 128/2,872 Top-30 state counts are not equivalent to matured per-State calibration counts.

## Protected invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2 unchanged. GCR is not included in this NSE result. UNKNOWN is never PASS.
