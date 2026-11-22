# NSE Attachment 403 Diagnostics — Continuation 243

Date: 2026-11-22
Branch: audit/prospective-selector-tracking

## Continuity / evidence reviewed
- Rechecked prior quarterly coverage report C242 and Run #128 artifact findings.
- Rechecked Run #372: XBRL extraction and normalized metric feature validation completed successfully; corrected-label walk-forward remained in progress at last observation.
- Rechecked Run #129: targeted tests were still in progress at the last status check; its current head SHA predates this C243 patch.
- Rechecked Run #377: cancelled after superseding pushes. Do not count it as a pass.
- No production branch or selector changes.

## Root-cause diagnostic improvement
The existing fetch routine tried both official NSE archive hosts when the first host returned HTTP 403, but after both failed it raised only a generic HTTP error. That discarded useful evidence about which official hosts were tried and their response metadata.

Changed `pipeline/quarterly_pdf_xbrl_metrics.py`:
- Added `AttachmentFetchError`, retaining per-host attempt records.
- For each official-host attempt, capture URL, HTTP status, Content-Type, and response byte count.
- Preserve request exceptions when no HTTP response is received.
- Attach the attempt diagnostics to the blocked row's error record.
- No bypass, proxy, unofficial mirror, or access-control circumvention was added.

Changed `qa/test_quarterly_pdf_xbrl_metrics.py`:
- Added a regression test simulating HTTP 403 from both official archive hosts.
- Test asserts both attempts and response Content-Type are retained.

Commits:
- Code: 8da955850e07763d9f40148124716c7db26b2f48
- Test: 66e1a030d2633ca86c3a16df359c4873f0b61a87

## Verification
| Item | Status |
|---|---|
| Existing Run #128 targeted workflow (previous code) | PASS |
| Existing Run #372 XBRL extraction | PASS |
| C243 code committed to audit branch | CODED |
| New dual-host 403 regression test | CODED; not yet CI-verified |
| Full NSE attachment remediation | BLOCKED / not claimed |
| Metric coverage (C242 evidence) | PARTIAL: 68 verified; 425 blocked; 7 superseded |

## Next exact action
Run the targeted quarterly-results test workflow against commit `66e1a030d2633ca86c3a16df359c4873f0b61a87`, then inspect the next official NSE run's `official_host_attempts` output. Only after that evidence can we decide whether the 403 is a consistent archive-host policy issue, a URL/path-specific denial, or a request-context issue.

## Invariants
Audit branch only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E and production workflow unchanged. ₹0 research spend; no paid APIs, synthetic data, fabricated timestamps, unofficial mirrors, or access-control bypass. UNKNOWN/BLOCKED never becomes PASS.
