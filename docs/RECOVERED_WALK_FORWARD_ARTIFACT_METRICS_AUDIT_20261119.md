# Recovered Walk-Forward Artifact: Metrics and Integrity Audit
Date: 2026-11-19
Status: ARTIFACT RECOVERED; METRICS PARTIALLY VERIFIED; RUN CANCELLED; PROMOTION NOT AUTHORIZED

## Recovery provenance
- Workflow: Audit-only Prospective Watchlist Tracking; run #319; run ID 40112393704.
- Branch: `audit/prospective-selector-tracking`.
- Head SHA: `7d7faaa3e50e216f4fc6cacfe75b88d3c58b4381`.
- Run status: completed / conclusion CANCELLED. The existence of an artifact does not convert the workflow to PASS.
- Artifact: `prospective-watchlist-audit`; artifact ID 12566997895; created 2026-10-24T16:47:31Z; expires 2027-01-22T16:37:12Z; size 8,963,598 bytes.
- GitHub artifact digest: `sha256:00a990117ac19971396eb5c039cb73c103e40f7ac3d1c93f31ca4839c6e56b7e`.
- Downloaded ZIP SHA-256 independently recomputed and matched exactly: `00a990117ac19971396eb5c039cb73c103e40f7ac3d1c93f31ca4839c6e56b7e`.
- ZIP contains `outputs/backtest/walk_forward_metrics.json`, `outputs/prospective/watchlist_ledger.csv`, `data/qa/qa_report.json`, and extensive quarterly-results source files. It does NOT contain `walk_forward_universe_probabilities.csv`, a dataset manifest, or the requested full reproducibility bundle in the inspected file listing.
- Metrics JSON SHA-256: `c9e0c929914bc1f2f2550ccd38cb7b2410d0247f500f774b471887d638859c79`; size 5,579 bytes.
- QA JSON SHA-256: `e914f2fce4693acef7f4e89feceaafe6da7732f25df7dd0fa51fb4d2b55d25ee`; size 282 bytes.

## Recovered walk-forward metrics (as recorded in artifact)
- Engine label: V11.4 Historical Winner Separation Engine.
- Sessions requested/tested: 100 / 100.
- Candidate rows: 3,000; Top-N: 30.
- Ranking: `WINNER_PROBABILITY_PCTL` with penalty-state adjustment.
- Target precision: T5_H1 33.31%; T10_H3 22.72%; T15_H5 15.21%; T20_H5 7.82%.
- Target recall: T5_H1 4.55%; T10_H3 3.96%; T15_H5 3.50%; T20_H5 3.91%.
- Base rates: T5_H1 8.63%; T10_H3 6.54%; T15_H5 4.84%; T20_H5 2.23%.
- Lift over base rate: T5_H1 3.86x; T10_H3 3.48x; T15_H5 3.14x; T20_H5 3.51x.
- Full-universe calibration records: T5_H1 n=246,661, Brier 0.075997, ECE 0.017666; T10_H3 n=246,269, Brier 0.059030, ECE 0.002677; T20_H5 n=245,850, Brier 0.020919, ECE 0.000874.
- State rows: CONTINUATION_READY 2,541; HIDDEN_WINNER_RECOVERY 459. CONTINUATION_READY had higher recorded hit rates than HIDDEN_WINNER_RECOVERY across T5_H1/T10_H3/T15_H5/T20_H5.
- Transition signature rows: DEMAND_CONFIRMATION 1,222; EXHAUSTION_BUILD 283; PRESSURE_BUILD 194; PRESSURE_FADE 371; STABLE_TRANSITION 930. DEMAND_CONFIRMATION showed the highest recorded H10_H3 (24.96%) and H15_H5 (16.28%) among these signatures; PRESSURE_FADE had H20_H5 8.31%, marginally above DEMAND_CONFIRMATION 8.31% (values nearly equal; do not rank without exact unrounded comparison).
- Crucial diagnostic: winner/nonwinner mean winner-probability values are almost indistinguishable in the aggregate separation block (0.086364 vs 0.086580; winner lower). Winner-specific interaction is also near-flat (63.325 vs 63.313), and latent-winner evidence is slightly lower for winners (93.859 vs 93.907). Thus the recorded Top-N precision/lift does not prove robust winner-probability separation or a well-ranked probability scale.
- QA report says PASS: 200 raw files, 200 sessions, 200 processed dates, 2,963 symbols, 100% delivery quantity and delivery percentage coverage, final-selection data ready, no issues. This QA result applies to the archived dataset as summarized by the artifact; dataset manifest and source hashes were not present in the inspected ZIP listing, so independent dataset provenance is still incomplete.

## Interpretation and decision
- This is stronger evidence than the previously recovered selected-pick ledger alone: it records 100 tested sessions, Top-30 precision/recall/base-rate/lift and full-universe calibration summaries.
- It is NOT evidence of 100% accuracy. The reported recall is only about 3.5%–4.5%, so the Top-30 list captures a small share of all winners. The high lift means ranking enriches winners relative to the base rate, not that most selected picks hit targets.
- These are historical label/selection metrics, not executable entry/exit returns, not net-of-cost results, and not prospective validation. The workflow run itself is CANCELLED.
- The missing universe-probability CSV, dataset manifest, full cutoff-level rows, and reproducibility bundle prevent independent recomputation of TP/FP/FN/TN, paired cutoff confidence intervals, leakage audit and calibration curves.
- Do not tune thresholds to maximize this same historical sample. Any candidate filter/weight change must be a shadow/challenger experiment on strictly chronological held-out cutoffs, with paired per-cutoff confidence intervals, frozen Top-30 protocol, explicit recall guardrail, and a new untouched validation window.
- A 100% target-hit rate is not a sound acceptance target: it can be manufactured by shrinking the shortlist to zero/one rare pick or by overfitting. Optimize precision subject to minimum coverage/recall, sample size, drawdown and transaction-cost constraints. No production selector change is authorized.
- GCR remains separate and BLOCKED until timestamp/vintage-aligned macro inputs, official sector TRI, exact index IDs and verified symbol-sector crosswalk are available.
- V11.3 cost-aware replay remains NOT_AUTHORIZED / NOT_RUN pending explicit G0 execution assumptions.
- No new NSE collection, no workflow rerun, no production selector/ranking/pressure-fade/CORE-672/Engines A-E/IPO-PLX V2 changes.

## Exact next actions
1. Recover a non-cancelled successful run's complete artifact if one exists; inspect all artifacts before considering any rerun.
2. Recover `walk_forward_universe_probabilities.csv`, dataset manifest and full cutoff-level reproducibility outputs from existing archives only. If absent/expired, record NOT_AVAILABLE; do not recollect NSE data without a new instruction.
3. Independently recompute target-specific TP/FP/FN/TN, precision, recall, cutoff-paired deltas and bootstrap confidence intervals.
4. Diagnose the near-zero/negative winner-vs-nonwinner probability separation and probability calibration before proposing any selector improvement.
5. Run filter/weight challengers only as non-production shadow tests on held-out chronological cutoffs; protect recall/coverage and do not lower the 50 matured H+3 observations per State rule.
