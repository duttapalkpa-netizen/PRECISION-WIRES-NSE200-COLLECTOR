# BCB SGS Portfolio Raw Capture Pipeline — Continuation 39 Part-8
Date: 2026-11-19
Scope: implement a bounded, isolated research-only raw collector for Brazil official SGS portfolio series 22905/22906/22925/22940; trigger one GitHub Actions run and preserve exact state.

## Progress Log
Completed before this part: Brazil IMF public registry row corroboration; BCB official ODbL dataset discovery for SGS 22905/22906/22925/22940; Chile revision calendar and current-vintage category discovery.
Rejected / do not repeat: IMF transaction-ID-2 probes (known HTTP 500); BOP6/BOP_BPM6 alias inference; treating SGS 22905 aggregate net as assets or liabilities; using rendered values as raw archive or fabricating retrieval/hash metadata.

## Implemented
1. Added `scripts/research/capture_bcb_sgs_portfolio_raw.py`.
   - Requests official BCB SGS JSON endpoints separately for each series.
   - Saves exact response bytes to distinct raw JSON files.
   - Records retrieval UTC, status, final URL, selected response headers, byte count and SHA-256.
   - Parses JSON and validates nonempty array, row schema, date format, finite numeric values, duplicate dates and monotonic ordering.
   - Records first/last observation, row counts, semantic limitations and per-series status in manifest.
   - Fails closed if any series request or QA fails; does not synthesize missing observations.
2. Added isolated workflow `.github/workflows/bcb_sgs_portfolio_raw_capture.yml`.
   - Separate from NSE production collector.
   - Five-minute job timeout, minimal requests dependency, uploads evidence bundle even on failure.
   - Push path trigger and manual workflow_dispatch.
3. Updated existing `.github/workflows/nse_collector.yml` paths-ignore so these research-only changes do not start the full NSE collector. No production pipeline logic changed.

## GitHub commits and run
- NSE collector isolation change commit: `6e975b7f375fed914c626eda92b4fcd9e87f7b80`.
- Collector script commit: `d0a545fb54bea345bf2e4b94c6644310ce09a7bf`.
- New bounded workflow commit: `4e0ef24ac94990e7b34d2c73099414310537071f`.
- Workflow run ID: `44538278638`, run #1, workflow `BCB SGS Portfolio Raw Capture (Research Only)`.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44538278638
- Run was observed as `queued` at 2026-11-19T13:55:18Z and again on subsequent status read. No conclusion/artifact exists yet. Do not claim collection or QA PASS until completed artifact is inspected.
- Direct local container download attempt failed; web reader could render BCB SGS 22906 JSON but could not open 22905/22925/22940 raw endpoints. These are not raw archival evidence.

## Data semantics
- 22905: broad monthly portfolio investment net; explicitly not split into assets/liabilities.
- 22906: monthly net acquisition of financial assets.
- 22925: monthly net incurrence of liabilities inflows.
- 22940: monthly portfolio debt securities inflows.
- Preserve series separately. Do not combine signs or claim exact IMF crosswalk without instrument, sign, valuation and scope checks.

## Acceptance matrix
| Gate | Status | Evidence |
|---|---|---|
| Isolated collector script committed | PASS | commit above |
| Isolated bounded workflow committed | PASS | commit above |
| Full NSE collector trigger suppression | PASS | paths-ignore updated before workflow push |
| Workflow triggered | PASS | run ID 44538278638 |
| Workflow execution | QUEUED | latest status read |
| Raw bytes / headers / hashes | NOT_DONE | no artifact yet |
| Four-series schema QA | NOT_DONE | no execution result yet |
| Brazil IMF identity / PA chronology | BLOCKED | owner-side evidence still missing |
| GCR synchronized panel / relative-attraction score | NOT_READY | raw capture, matched country panel and validation remain open |

## Next action
Poll only run `44538278638`; inspect its job steps/logs and artifact. If success, independently recompute all four raw-file hashes from artifact, validate manifest and record exact artifact ID/digest. If failure, patch only the failed bounded collector and use a new run; do not rerun unrelated workflows. Then build matching India/Chile/US/other-country source families and vintage-aligned panel. Brazil PA revision chronology still needs authorized official provider-side export.

## Invariants
₹0, official/free sources only, no credentials, no synthetic values, no guessed timestamps/hashes, no unapproved aliases/crosswalks, UNKNOWN is not PASS. No production integration, macro weights, EMDE aggregate, selector/ranking/pressure-fade/CORE-672/Engines A-E changes.
