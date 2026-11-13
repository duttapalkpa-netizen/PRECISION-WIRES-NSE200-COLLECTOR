# NSE Corporate Announcements RSS — First Raw Acquisition and Replay Audit
Date: 2026-11-14
Workflow run: 43489286657 (run number 1)
Branch: `research/corporate-events-rss-collector-v1-20261114`
Head commit: `daf88704dd0f7464e0258ce4b5b9a082e7f86dfa`
Conclusion: workflow PASS; official RSS snapshot acquired and parsed; source completeness remains UNKNOWN.

## Execution
- Workflow: NSE Corporate Announcements RSS — isolated read-only acquisition
- Trigger: push on isolated research branch
- Job: `acquire` — completed / success
- Steps: checkout PASS; Python setup PASS; 4 parser tests PASS; bounded official fetch PASS; artifact upload PASS; final enforcement skipped as expected because acquisition succeeded.
- Job runtime: under 1 minute based on Actions timestamps.
- Workflow timeout: 8 minutes.
- No writes to repository contents from the workflow; `contents: read`, checkout credentials disabled.

## Exact source and response
- Requested URL: https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml
- Final URL: same exact URL; no redirect observed.
- HTTP status: 200
- Content-Type: `application/xml`
- Response bytes: 6,270
- Raw XML SHA-256: `21de2c9b2d1f39cad81600cdca22556e813d2854eeee28d5082c913ec95aa1a4`
- Retrieval interval: 2026-11-13T19:08:23Z to 2026-11-13T19:08:24Z
- Parser status: PASS
- RSS items parsed: 13
- Required fields present across all 13: title 13/13, link 13/13, pubDate 13/13, description 13/13.
- GUID present: 0/13. Missing GUID: 13/13. Therefore GUID-based identity/deduplication is unavailable in this snapshot; do not synthesize GUIDs.
- Link values: 13 unique / 13; pubDate original strings: 13 unique / 13. These are snapshot observations, not stable source IDs.
- Original pubDate strings range from `14-Nov-2026 00:35:58` to `14-Nov-2026 00:00:02`. They contain no timezone suffix; retained verbatim and not normalized to UTC.
- XML includes RSS 2.0 channel; item title is issuer/company name and description carries issuer text/subject. Do not infer symbol from links or titles.

## Artifact and hashes
- Artifact ID: `14069815552`
- Artifact name: `nse-corporate-announcements-rss-43489286657`
- Artifact ZIP size: 4,273 bytes
- Artifact ZIP SHA-256: `624617b0e9ef1de4220d5672c5fcb9f4fd97a7bae15b35600602e128b63fb966`
- Members: `announcements.xml`, `announcements.jsonl`, `manifest.json`
- Artifact retention expiry: 2026-12-13T19:08:24Z
- JSONL: 13 records, 11,622 bytes, SHA-256 `b918f872cabca6b6d053e4f5eeb12850e1086233d27e2dbb8f79ffdc902a6511`
- Manifest: 1,292 bytes, SHA-256 `7fd9fd4236ab223a8988095a4644cae4c48e88ce6438ad24bbd08d2c28fb287b`

## Interpretation / limitations
1. Official RSS endpoint is reachable from GitHub Actions runner for this single snapshot. This does not prove continuous availability or historical completeness.
2. All 13 items have title, link, pubDate and description. All lack GUID. Preserve link as source URL, but do not promote it to an immutable event ID without a separate source contract.
3. pubDate values are timezone-naive strings. Keep original strings; timestamp normalization/ordering across sources remains UNKNOWN.
4. The snapshot is a rolling feed view, not a complete archive. Need repeated snapshots and overlap/gap reconciliation against official filings before estimating coverage or event completeness.
5. No symbol was synthesized; no PDF/XBRL attachments were downloaded or interpreted.
6. Corporate Events P0 remains BLOCKED pending repeat snapshots, official page item-level reconciliation, retention policy/replay tests and symbol/date/source-URL provenance validation.

## Acceptance
| Criterion | Status |
|---|---|
| Bounded runner execution | PASS |
| Four parser unit tests | PASS |
| Official endpoint HTTP 200 | PASS |
| Raw XML archived before parse | PASS |
| Raw XML SHA-256 recomputed from artifact | PASS |
| 13/13 items retained with source fields | PASS |
| GUID coverage | 0/13 — UNKNOWN / limitation |
| Timezone semantics of pubDate | UNKNOWN |
| Historical completeness / missing-item rate | UNKNOWN |
| Repeat snapshot / overlap reconciliation | NOT RUN |
| Corporate Events P0 Hard Gate | BLOCKED |

## Safety and invariants
Research branch only; no PR/merge. Workflow uses read-only contents permission and disabled checkout credentials. No paid API, synthetic data, invented symbol/GUID/timezone, or production selector/ranking/CORE-672 changes.
