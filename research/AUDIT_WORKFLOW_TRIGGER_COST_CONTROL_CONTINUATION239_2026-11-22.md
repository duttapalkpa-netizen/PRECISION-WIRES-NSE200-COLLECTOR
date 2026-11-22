# Audit Workflow Trigger Cost Control — Continuation 239

Date: 2026-11-22 (Asia/Kolkata)
Branch: audit/prospective-selector-tracking
Status: WORKFLOW CONFIGURATION COMMITTED; ACTIVE RUN #372 STILL IN PROGRESS AT LAST CHECK

## 1. Continuity preflight
- Re-read C237 and C238 reports and inspected live GitHub Actions runs on the audit branch.
- Run #369 (`44991273271`, head `9ab2ef4...`) failed at the unittest step before data acquisition. The later test fixture correction was committed as `220e5cc...`.
- Run #372 (`44991296424`, head `8351e4d...`) subsequently reported the complete unittest discovery step as `completed / success`. At the latest inspection, it was still running the 200-session NSE acquisition; Security Master steps 8-9 had not yet started.
- Run #373 (`44991411103`, head `cb66a685...`) was pending at the time of inspection. It was triggered by the C238 research-report-only commit.
- Selected a bounded workflow-cost improvement: prevent documentation-only research report commits from launching the full 10-minute multi-stage audit.

## 2. Change committed
Updated `.github/workflows/prospective_watchlist_tracking.yml` push path filters by removing `research/**`.
- Code/data/workflow paths remain eligible to trigger the audit.
- Research report-only commits no longer trigger the full acquisition/backtest workflow.
- Scheduled weekday runs and manual workflow_dispatch remain unchanged.
- This reduces repeated full workflow executions caused solely by adding continuity reports.

Commit:
- Workflow trigger filter: `4cd9548255f866326e68a11e32d50e4392dbcded`

## 3. Verification and remaining status
| Item | Status |
|---|---|
| Workflow push filter updated | CODED |
| Existing Run #372 unittest step | PASS |
| Run #372 200-session acquisition | IN PROGRESS at last check |
| Run #372 Security Master collector / validator | NOT YET REACHED |
| Run #373 report-only triggered run | PENDING at last check; started before trigger-filter commit |
| New workflow trigger behavior | CONFIGURATION REVIEWED; not yet independently exercised |
| Full prospective audit | NOT VERIFIED |
| Daily MII equivalence | UNKNOWN / NOT ESTABLISHED |

The run states are snapshots from the inspection time, not claims of final completion. No attempt was made to cancel active runs or dispatch another long run.

## 4. Invariants
Audit-only branch. No production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, production workflow, data or model logic changed. ₹0; no paid APIs, synthetic data, guessed source contracts, or fabricated timestamps. UNKNOWN never PASS.
