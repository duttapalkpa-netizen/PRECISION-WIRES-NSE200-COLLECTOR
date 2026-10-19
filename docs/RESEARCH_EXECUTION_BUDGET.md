# Research Execution Budget (Audit Branch Only)

Effective date: 2026-10-19

## Hard cap
- Maximum active reasoning/work segment: 10 minutes.
- Maximum GitHub Actions workflow/job runtime for research tasks: 10 minutes.
- Do not start or repeat a full end-to-end audit when its expected runtime exceeds this cap.
- Prefer one bounded diagnostic, one narrow code fix, and targeted regression tests per work segment.
- Split large audits into independently runnable stages; persist artifacts between stages and resume from the last verified artifact.
- If a stage cannot finish within 10 minutes, stop it, mark it TIME_BUDGET_EXCEEDED/BLOCKED, preserve diagnostics, and reduce scope. Never report success based only on a workflow-level success if the required data checks failed.
- A green test run is not equivalent to a data gate passing.

## Research integrity invariants
- Audit branch only; production selector, RANKING_SCORE, and frozen +1 PRESSURE_FADE remain unchanged.
- Missing or stale values are UNKNOWN/BLOCKED, never zero or negative.
- No fabricated financial metrics, source URLs, timestamps, ISINs, or period ends.
- Quarterly Metrics Step 1 remains BLOCKED until endpoint/schema and source-linked metric extraction have verifiable accepted rows. Do not start Step 2 before Step 1 genuinely passes.
- Macro-Geo hard gate remains mandatory; no candidate release while blocked.
- Only score matured H+1/H+3/H+5 outcomes.
