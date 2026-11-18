# BCB SGS Capture-to-Diff Automation Audit — 2026-11-18

## Objective
Remove the manual second push previously required to start the two-vintage comparator after a prospective SGS snapshot. Keep all changes isolated to the research branch.

## Design change
Updated `.github/workflows/bcb_sgs_prospective_vintage_snapshot.yml` so one run now performs, in order:
1. Fetch four official BCB SGS series and write a unique timestamped raw snapshot.
2. Commit and push immutable raw snapshot directory.
3. Run `scripts/research/diff_bcb_sgs_vintages.py` against the two latest real snapshots.
4. Commit and push the deterministic QA JSON.
5. Upload the snapshot directory and QA JSON as a workflow artifact.

This avoids relying on a second push-triggered workflow. GitHub documents that a push made with GITHUB_TOKEN will not trigger a separate push workflow; keeping capture and comparison in the same run avoids this restriction. Official reference: https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow

## Test execution
- Workflow changes initially contained an invalid artifact path block due to escaped newline characters; two parse failures occurred before any job started (runs 44240725826 and 44240735245). The YAML path block was corrected before the successful test; these failed runs did not alter source data.
- Successful end-to-end run: `44240790343`, conclusion SUCCESS.
- Capture, raw snapshot commit, comparator, QA commit and artifact upload steps all succeeded.
- Third real snapshot ID: `20261118T045654Z`; captured at `2026-11-18T04:56:54.577207+00:00`.
- Manifest SHA-256: `958b09b6c6538d3c4adebbae8343f8c01ea5448aa315edaafc4fb1a9fc3c5cc5`.
- QA output: `data/qa/BCB_SGS_VINTAGE_REVISION_DIFF_20261118T045654Z.json`; blob SHA `8a4af300c2d7e21942b1adb0fa15132755a6c97d`.
- QA status: `PASS_TWO_VINTAGES_COMPARED`; snapshot_count=3; compared latest two snapshots 044659Z and 045654Z; 1,524 unchanged, 0 changed, 0 added, 0 removed.
- Capture artifact ID `14400155068`; size 83,206 bytes; digest SHA-256 `6b3988ee2ea3b3f20b1df934d496106ffff02b6ef48d775c12404f7b095e6c11`.
- Final branch head after QA commit: `ca6edfd6b737fa5e46b3e1b55965167ba9a523ad`.

## Interpretation
- The chained workflow is validated end-to-end. Each subsequent research-branch trigger-file update now causes one capture and an immediate comparison in the same run; no second manual workflow-file push is required.
- The short interval between the two newest captures is only a pipeline test, not a meaningful monthly revision window.
- No differences were observed across the latest two snapshots. This does not prove no revisions occurred before the first snapshot or explain the February-2026 SGS 22942 discrepancy.
- The original March-2026 vintage remains NOT_PROVEN; specific revision cause remains UNKNOWN.

## Acceptance
- Research-branch capture trigger: PASS.
- Immutable raw snapshot capture: PASS.
- Same-run comparator execution: PASS.
- QA JSON commit and artifact upload: PASS.
- Latest comparison: 1,524 unchanged; 0 changed/added/removed.
- Monthly monitoring interval: PENDING next BCB external-sector release.
- Brazil pilot: NOT_ACCEPTED.
- Production integration: NOT_AUTHORIZED.

## Protected invariants
Research-only; ₹0; official/free sources only; no synthetic observations, invented timestamps, raw overwrites, or unsupported revision attribution. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and Hard Gate unchanged.
