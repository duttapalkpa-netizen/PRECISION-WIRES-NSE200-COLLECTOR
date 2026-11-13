# Corporate Events P0 — RSS Collector Implementation Readiness Audit
Date: 2026-11-14
Base revision: `e4347e9197efd0e2fbf0d4b71eea9bac99192a42` (Appendix 22 continuation)
Scope: read-only repository inventory and workflow permission/runtime review. No code or workflow execution.

## Repository inventory (GitHub main, recursive tree)
- The complete tracked tree returned 49 entries with `truncated=false`.
- No tracked path matches RSS, corporate, announcement or event naming.
- Existing workflow files: `.github/workflows/nse_collector.yml`, `nse_57_backfill.yml`, `prospective_watchlist_tracking.yml`, `cga_capex_fy2026_27_smoke.yml`, `validate_iip_41_vintage_audit.yml`, `validate_macro_evidence_snapshot_v2.yml`.
- No dedicated Corporate Events/RSS collector, parser, QA test, artifact manifest or scheduled acquisition workflow exists in the tracked main tree.

## Existing workflow safety/operational fit
Inspected `.github/workflows/nse_collector.yml` (blob `8860fd4f7bb43164ad1b514c884f5e9adf750973`):
- permissions: `contents: read` (appropriate minimum for read-only acquisition).
- runner: `ubuntu-latest`.
- timeout: 60 minutes (not compatible with the user's preferred <10-minute run target as a dedicated small acquisition task).
- triggers include workflow_dispatch, push to main and weekday schedule.
- workflow runs full 200-session collector, QA, 100-session walk-forward, Engines A/B/C/D/E, IPO-PLX, macro context and final selection. It is not suitable for a focused RSS fetch; adding RSS there would couple a P0 source task to a long production-adjacent pipeline.
- artifact upload currently packages processed/reference/context/live/QA/finalists/diagnostics/backtest/IPO paths; no explicit raw RSS archive path or dedicated checksum manifest.
Inspected `.github/workflows/prospective_watchlist_tracking.yml` (blob `850b7c266bfa29e01f70722dbf342988730fc351`):
- permissions: `contents: write`, timeout 120 minutes and pushes audit ledger to its own branch. Not appropriate for a read-only P0 source collector.

## Minimal isolated collector contract (recommendation, not implemented)
Create a separate manually dispatched workflow on an isolated research branch, only after explicit approval to add/run it:
1. `permissions: contents: read`; no checkout push, PR, secrets, paid APIs or external contact.
2. `timeout-minutes: 8`; one bounded attempt per approved official URL; no unbounded retries. Record actual UTC start/end, DNS/connect/TLS/HTTP outcome, final URL, redirect chain, response content-type, byte count and SHA-256. If network/DNS fails, record failure metadata only; never fabricate a payload.
3. Fetch only the exact NSE RSS URLs linked from the official NSE RSS page; do not substitute `archives` for `nsearchives` or infer redirects. Keep the exact requested URL and observed final URL separate.
4. Preserve raw response bytes immutably before parsing. XML parser must disable external entities/DTD/network resolution; reject malformed XML, record parse errors, never silently drop malformed items.
5. Parse channel/item fields losslessly: title, link, guid (including isPermaLink attribute), pubDate as original string, description/content as raw source field. Keep raw XML and parsed JSONL/CSV separate. No inferred symbol, normalized timestamp, or fabricated unique key.
6. Deduplicate only on an actual source GUID; if absent, retain records and mark identity UNKNOWN. Do not deduplicate on title/date.
7. Produce manifest with source URL, final URL, retrieval UTC, HTTP status, content type, bytes, SHA-256, parser version, item count, min/max original pubDate, parse warnings, and artifact path.
8. Upload raw XML + manifest + parse output as a workflow artifact with bounded retention; never commit raw files to Git.
9. QA checks: valid XML, item count equals parsed record count, every item retained, exact hash recomputation, no synthetic timestamps, duplicate GUID report, source pubDate parseability reported separately (not rewritten), and repeat-download comparison clearly marked as two snapshots rather than presumed identical.
10. Keep Corporate Events P0 BLOCKED until raw bytes, item-level official cross-check, date coverage, retention, and replayability are proven.

## Readiness decision
- Existing repo contains no dedicated RSS implementation: CONFIRMED (complete, non-truncated tree).
- Existing main collector has read-only permissions but a 60-minute full-pipeline footprint: CONFIRMED.
- Existing prospective audit workflow has write permissions and 120-minute timeout: CONFIRMED; exclude it.
- A new isolated read-only workflow is the correct architecture: RECOMMENDED, NOT IMPLEMENTED.
- Official raw XML availability and GitHub Actions outbound DNS/network access: UNKNOWN; must be tested by the dedicated bounded runner, not inferred from Feeder.
- Corporate Events P0: BLOCKED.

## Non-actions / invariants
No source fetch, no code/workflow edits, no action run, no artifact creation, no PR/merge. No paid service or synthetic data. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Hard Gate unchanged.
