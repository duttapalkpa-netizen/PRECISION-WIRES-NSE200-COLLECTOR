# GCR Official India FPI Raw Capture Harness — Continuation 70
Date: 2026-11-19 (Asia/Kolkata)
Scope: research-only, read-only HTTP GET capture. No production changes.

## Objective
Resolve the Continuation 69 NSDL/CDSL daily-flow freshness conflict by securing byte-level source evidence from the official landing pages before parsing or ingestion. This is a capture harness, not an FPI data ingestion or reconciliation PASS.

## CI isolation guard — applied first
Updated `.github/workflows/nse_collector.yml` before adding the research script/workflow/trigger.
- Guard commit: `e51b40cff82dc4ae24a7068b74afabee35e3a370`
- Added all three exact paths to `paths-ignore`:
  - `.github/workflows/gcr_india_fpi_raw_capture.yml`
  - `scripts/research/capture_india_fpi_official_pages.py`
  - `scripts/research/gcr_india_fpi_raw_capture_trigger.txt`
This ordering follows the prior accidental-NSE-run lesson.

## Added read-only capture harness
- Script: `scripts/research/capture_india_fpi_official_pages.py`
- Script commit: `41ecee60c32aec20a384ec11ba23023b0af7f666`
- Workflow: `.github/workflows/gcr_india_fpi_raw_capture.yml`
- Workflow commit: `092ed5dd2cf78a5265bb07aa11172317ce4bee90`
- Trigger marker commit: `f2c359ce095638f1c081e4d09b3545400c071670`
- Workflow timeout: 6 minutes.
- Dependencies: Python standard library only.
- Requests: exactly six public HTTPS GETs, one per official page; no POST, no credentials, no guessed ASP.NET form submission.
- Pages:
  1. NSDL Latest.aspx
  2. NSDL Monthly.aspx
  3. NSDL Archive.aspx
  4. NSDL FPI_Fortnightly_Selection.aspx
  5. CDSL ArchiveDataAfter2009.aspx
  6. CDSL ForeignPortInvestor.html
- For each response, script writes raw body bytes (including HTTP error body where available), status, final URL, headers, content type, UTC retrieval timestamp, byte count and SHA-256 into `outputs/gcr_india_fpi_raw_capture/`.
- Manifest and summary JSON are uploaded as a GitHub Actions artifact even if the capture step fails.

## Execution state
The trigger marker has been committed. The workflow run ID, terminal conclusion and artifact ID are not yet independently available through the connected GitHub Actions read tools in this execution. Therefore runtime capture is **PENDING / NOT_VERIFIED**. Do not claim six pages captured or any source freshness resolved until the run and artifact are inspected.

## Brazil workstream — retained boundary
No Brazil endpoint was repeated. The Brazil registration 40-event lifecycle remains PASS. PA transaction ID 2 / Changelog remains BLOCKED after the already documented HTTP 500 probes. BOP6 vs BOP_BPM6 identity remains unresolved. The next valid closure route is actual official PA GUI/export evidence; if owner-side interaction is required, preserve it as an external dependency and do not request credentials.

## Acceptance
- CI isolation guard committed before research trigger: PASS.
- Capture script/workflow/trigger committed: PASS.
- Six official raw responses, status, headers, UTC, hashes and artifact: PENDING / NOT_VERIFIED.
- NSDL/CDSL schema parsing and matched-date reconciliation: NOT_DONE.
- GCR synchronized panel, factor registry closure and OOS event study: BLOCKED / NOT_DONE.
- Brazil PA changelog and Dataflow identity: BLOCKED.
- Production admission: NOT_AUTHORIZED.

## Invariants
₹0; official/free sources only. No synthetic data, no inferred timestamps, no forward-fill, no proxy promotion. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
