# Existing Dataset Availability and Workflow Scope Audit — 2026-11-20

## Verdict
**BLOCKED — no verified reusable processed NSE dataset is present in the inspected repository trees.** An audit-only export cannot be run safely from the current checked-in state. No workflow was dispatched and no data was downloaded.

## Evidence inspected
- Main branch HEAD: `82c24bdef151b93f1c5f8d53ffc473a1c7bcde51`.
- Audit branch HEAD: `46411147f490abbf05f920073b7139b258e42b1e`.
- Main branch recursive tree contains only `data/processed/.gitkeep` under `data/processed`; no normalized processed NSE dataset is committed.
- Audit branch recursive tree contains `pipeline/walk_forward_backtest.py` and `.github/workflows/prospective_watchlist_tracking.yml`, but no processed NSE dataset, row-level prediction export, or dataset manifest.
- The audit workflow has a 10-minute job timeout, but it is not an export-only workflow: it explicitly runs `collector/nse_download.py --sessions 200`, `collector/build_200_sessions.py`, strict QA, quarterly-results collection/XBRL extraction, walk-forward backtest, Macro-Geo P0 collection/repair/coverage, several retrospective studies, and reproducibility checks. Dispatching it would violate the current no-new-NSE-collection constraint and would not be a bounded export-only task.
- Previously inspected artifacts #319 and #302 lack `walk_forward_predictions.csv`, `walk_forward_universe_probabilities.csv`, and a dataset manifest. Their QA JSON does not supply the missing source bytes or row-level records.

## Decision
- Do not dispatch `prospective_watchlist_tracking.yml`.
- Do not create or label a new export workflow as reusable until an existing processed dataset is located and its manifest/hash is verified.
- Row-level TP/FP/FN/TN, exact false-positive/missed-winner identities, and paired cutoff confidence intervals remain NOT_RECOMPUTABLE.
- Next permissible step: locate an already-existing complete processed dataset/artifact from another retained source, or obtain the user's explicit approval for a new collection path. No production selector or scoring changes.

## Integrity
No workflow run, new NSE download, or code change to production logic was performed. UNKNOWN remains distinct from PASS.
