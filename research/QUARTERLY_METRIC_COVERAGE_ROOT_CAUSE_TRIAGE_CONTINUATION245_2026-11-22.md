# Quarterly Metrics Coverage Triage — Continuation 245

Date: 2026-11-22
Branch: audit/prospective-selector-tracking

## Continuity / evidence inspected
Reviewed the latest successful targeted quarterly CI Run #133 (44992195724), its artifact `quarterly-endpoint-schema-audit` (artifact ID 14741638800, 5,007,746 bytes), and the generated JSON/CSV outputs. This is a source-backed triage of the new artifact, not a repeat of the C243/C244 code repair.

## Verified result
- Run #133 completed SUCCESS, including the targeted regression suite, official NSE security-master refresh, bounded live endpoint/schema audit, source-linked XBRL extraction, normalized feature rebuild, unresolved filing timestamp/ISIN diagnostics, and artifact upload.
- Endpoint source: NSE corporate filings API. Result disclosure: 500 records; board/calendar: 2,966 records. Result source validation: 500/500 valid records.
- Extraction processed all 500 disclosures (no truncation), made 926 attachment attempts, and produced 500 ledger rows.
- 67 verified source-linked metric rows across 44 symbols.
- 426 rows remain BLOCKED_NO_VERIFIED_XBRL_METRICS.
- 7 rows are superseded by later disclosures.
- Coverage remains BLOCKED_INCOMPLETE_OR_UNVERIFIED_COVERAGE. Do not use blocked rows as zero/negative or as verified financial signals.
- Extractor report records 100 detailed errors: 99 official attachment retrieval failures (including explicit NSE archive HTTP 403 evidence) and one facts/basis-incomplete case.
- Feature table contains 67 rows, but event study is BLOCKED because the required processed 200-session price panel was not present in this targeted artifact. The report explicitly marks the endpoint/schema Step 1 PASS as limited to endpoint/schema readiness.

## Root-cause prioritization
The largest measured obstacle is official attachment retrieval failure, not disclosure endpoint availability: disclosure endpoint validation is 500/500 PASS, while 99 of the 100 surfaced extraction errors are attachment-fetch failures. The remaining 426 blocked ledger rows cannot all be attributed to those 99 error entries without a complete per-row reason join; no such extrapolation is made here.

## Decision / next action
Prioritize an evidence-preserving attachment retry/fallback audit using only NSE-authorized endpoints and the exact URLs already present in the disclosure records. Preserve per-host HTTP status, content type, bytes, timestamp, and source hash. Retry only 403/failed attachments in a bounded batch; do not scrape third-party mirrors, bypass access controls, or infer financial metrics from PDFs/headlines. Keep unresolved rows BLOCKED.

## Status
- Targeted quarterly workflow Run #133: PASS.
- Endpoint/schema Step 1: PASS, narrowly scoped.
- Financial metric coverage Step 2: BLOCKED (67 verified / 500 ledger rows; 426 blocked, 7 superseded).
- Event study: BLOCKED in this artifact because processed 200-session price panel is absent.
- Full prospective audit Run #381: still in progress at the time of this report; no full-workflow PASS claimed.

## Invariants
Audit branch only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged. ₹0 spend; free official sources only; no synthetic data, fabricated timestamps, unofficial mirrors, or access-control bypass. UNKNOWN/BLOCKED never becomes PASS.
