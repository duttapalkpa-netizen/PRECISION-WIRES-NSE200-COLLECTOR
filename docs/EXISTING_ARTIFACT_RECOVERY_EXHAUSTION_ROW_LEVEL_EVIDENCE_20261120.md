# Existing Artifact Recovery Exhaustion — Row-Level Winner Evidence
Date: 2026-11-20
Status: RECOVERY AUDIT COMPLETE; ROW-LEVEL PREDICTIONS NOT AVAILABLE IN INSPECTED ARTIFACTS

## Scope
- Objective: recover existing `walk_forward_predictions.csv` and `walk_forward_universe_probabilities.csv` for false-positive/missed-winner analysis, without new NSE collection or workflow dispatch.
- Inspected existing prospective-watchlist workflow runs on `audit/prospective-selector-tracking`, including runs #319 (40112393704), #302 (40070035553), #301 (40069965859), #300 (40069943403), #299 (40069932160), #298 (40067318516), and earlier #284–#297 artifact-bearing failures/cancellations.
- The listed branch history returned 43 runs for workflow ID 381790326; the inspected run records were CANCELLED or FAILURE, not a successful completed validation run. Do not describe these runs as PASS.
- No new data download, workflow dispatch, or backtest execution was performed.

## Run #302 artifact verification
- Run ID 40070035553; run #302; branch `audit/prospective-selector-tracking`; artifact ID 12550639923; artifact name `prospective-watchlist-audit`; artifact size 8,858,141 bytes; created 2026-10-24T06:34:05Z; expires 2027-01-22 (GitHub artifact metadata).
- GitHub artifact digest: `sha256:6e20634289f2b2838ee79d156bfce52f6ee2bff68a0a40adeefa732fe9c52da5`.
- Downloaded ZIP SHA-256 independently computed: `6e20634289f2b2838ee79d156bfce52f6ee2bff68a0a40adeefa732fe9c52da5` (exact match).
- ZIP contains `outputs/prospective/watchlist_ledger.csv` (110 rows; SHA-256 `1bc2712ef3b3bb36faa82346a496a16aecec8971748cb3133705364ceb3c8166`), `data/qa/qa_report.json` (282 bytes; SHA-256 `e914f2fce4693acef7f4e89feceaafe6da7732f25df7dd0fa51fb4d2b55d25ee`), and many quarterly-results raw disclosure/XBRL files.
- QA JSON states PASS: 200 raw files, 200 sessions, 200 processed dates, 2,963 symbols, 100% delivery quantity and delivery percentage coverage, no issues. This QA statement is limited to the QA file contents; it does not make the workflow run successful or prove prediction-artifact availability.
- ZIP file listing was searched for `walk_forward_predictions.csv`, `walk_forward_universe_probabilities.csv`, prediction outputs, and dataset manifest. None were present.
- Other inspected larger prospective-watchlist artifacts (including run #319 artifact ID 12566997895) also lacked the required row-level prediction and universe-probability CSVs. Tiny ~3.9 KB artifacts from failed runs are not usable validation bundles.

## Consequence
- False-positive symbol-level list: NOT_AVAILABLE.
- Missed-winner symbol-level list: NOT_AVAILABLE.
- Per-cutoff paired TP/FP/FN/TN and bootstrap confidence intervals: NOT_RECOMPUTABLE from available artifacts.
- Shadow challenger test for HIDDEN_WINNER_RECOVERY / EXHAUSTION_BUILD: NOT_RUN; no row-level predictions to rank or evaluate.
- The prior aggregate State/signature hit rates remain descriptive summary metrics only. Do not infer individual candidate identities, causes or new selector weights from aggregate summaries.
- The 200-session QA PASS and 100-session metrics JSON must remain separate from workflow conclusion (CANCELLED/FAILURE).

## Next permitted path
1. Keep monitoring/reusing existing archived artifacts only; inspect any newly surfaced successful, non-cancelled run artifact for the two exact row-level CSVs and dataset manifest.
2. If the files are not present in existing artifacts, request explicit approval before any new workflow execution. Do not recollect NSE data under the current no-new-data instruction.
3. If later authorized, use a short, bounded, audit-only export job that reuses the existing processed dataset and emits row-level predictions, full universe probabilities, dataset manifest/hash, code/config SHAs and reproducibility metadata; no production changes.
4. Only after those files exist, calculate per-cutoff and target-specific confusion metrics, paired CIs, and shadow challengers. Maintain >=50 matured H+3 observations per State for calibration.

## Invariants
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A–E, IPO-PLX V2 unchanged.
- GCR remains UNKNOWN/BLOCKED; V11.3 cost-aware replay remains NOT_AUTHORIZED/NOT_RUN.
- ₹0; official/free sources only; no synthetic data; UNKNOWN is never PASS.
