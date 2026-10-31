# NSE Collector Speed & Integrity Audit — 2026-10-31

## Decision
**AUDIT COMPLETE — REMEDIATION REQUIRED (BLOCKED).** Read-only audit of branch fix/factor-registry-same-snapshot-reconcile at commit ed0815593b682fd66ee2db6e294906f8d8594317. No production collector, selector, ranking, or workflow behavior was changed.

## Scope inspected
- collector/nse_download.py
- .github/workflows/nse_collector.yml

## Findings

| Requirement | Current evidence | Result |
|---|---|---|
| Incremental collection | Existing valid daily files are reused; collector scans backward until requested session count. | PARTIAL |
| Duplicate-download avoidance | Cache hit skips network for that date, but validation does not verify expected trade date or stored content hash/manifest. | PARTIAL |
| Bounded retries | UDiFF has at most two attempts; legacy one; full-bhavcopy tries two URLs sequentially without shared retry/backoff policy. | PARTIAL |
| Caching | File-existence + schema/value check only; no ETag/Last-Modified metadata or immutable content-addressed cache. | PARTIAL |
| Parallel source collection | Requests are fully sequential; no bounded worker pool or per-host concurrency limiter. | FAIL |
| Immutable snapshot | No per-source SHA-256 manifest, atomic staging/promotion, or immutable run snapshot. | FAIL |
| Run duration | Workflow sets timeout-minutes: 60 and runs 200-session collection plus downstream engines in one job. | FAIL |
| Partial/blocked response safety | Schema/value checks exist for UDiFF and full-delivery files, but cache validation is weaker and does not verify date identity. | PARTIAL |

## Risk assessment
1. Sequential per-date source attempts across up to 500 calendar days can exceed the desired 10-minute run budget.
2. Cache validation checks symbol/series/close fields but not that rows belong to the filename's expected session date, nor that delivery columns remain complete.
3. No immutable provenance ties stored daily files to source URL, response timestamp, byte count, SHA-256, and validation result.
4. Unrestricted fan-out risks NSE throttling, 403/429 responses, incomplete downloads, and corrupted partial outputs. Safe initial concurrency should be capped at two in-flight requests per host, with per-request timeouts and bounded exponential backoff with jitter.
5. The current 60-minute workflow timeout conflicts with the requested maximum of 10 minutes.

## Safe remediation design (not yet implemented)
- Build a session calendar and derive the exact missing-date set from validated cache entries.
- Keep cached files immutable; validate filename date, row dates, required columns, row count/schema, and SHA-256 before reuse.
- Use a bounded executor (initial cap: 2 workers globally and per host), a shared host semaphore, and a minimum inter-request delay.
- Retry only transient network errors, HTTP 408/429/5xx, and incomplete ZIP/CSV responses; cap at 3 attempts with exponential backoff + jitter. Treat 403/404 as non-retryable for that source/date and fall back to the next source.
- Download to a temporary .part file, validate fully, compute SHA-256, then atomically promote into the run snapshot. Never expose partial files downstream.
- Write append-only manifest.jsonl records with trade date, source URL/name, HTTP status, retrieval UTC, content type, bytes, SHA-256, validation status, retry count, and cache/network origin.
- Produce a run-level immutable snapshot ID from sorted manifest hashes; downstream processing must consume that snapshot only.
- Split collection from downstream analysis. Set collector job timeout-minutes: 10; fail closed if required sessions are not reached. Keep downstream workflows separate and QA gates unchanged.
- Add tests for cache date mismatch, duplicate dates, 403/429/500, timeout, truncated ZIP, wrong CSV date, duplicate rows, missing delivery fields, hash mismatch, and interrupted atomic write.

## Acceptance gates for implementation
1. Warm-cache run: zero source downloads for already validated sessions.
2. Missing-date fixture: only missing dates fetched; no duplicate requests.
3. Concurrency never exceeds 2 requests per host.
4. Retry cap and 403/404 fallback proven with mocked responses.
5. Partial downloads never appear as final CSV files.
6. Manifest hashes match every stored file and snapshot ID is deterministic.
7. Collector job completes within 10 minutes on configured bounded test scope; full 200-session readiness remains fail-closed if source cannot supply data within budget.
8. Regression-check production selector, RANKING_SCORE, +1 PRESSURE_FADE, and all 672 diagnostics unchanged.

## Explicit non-changes
- Production selector: unchanged.
- RANKING_SCORE: unchanged.
- +1 PRESSURE_FADE: unchanged.
- 672 diagnostic matrix: unchanged.
- No PR merge or production promotion performed.