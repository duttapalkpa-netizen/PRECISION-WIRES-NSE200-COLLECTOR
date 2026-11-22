# NSE Integrated Filing Archive Host Fallback — Continuation 246

Date: 2026-11-22
Branch: audit/prospective-selector-tracking

## Continuity check
Reviewed C245's actual Run #133 artifact, the extractor implementation and its existing host-fallback tests before editing. This change addresses a concrete mismatch visible in the artifact rather than repeating the previous generic 403 diagnosis.

## Evidence-backed defect
The NSE integrated-filing API returned attachment URLs on `nsearchives.nseindia.in`. The collector's fallback logic only recognized `nsearchives.nseindia.com` and `archives.nseindia.com`. Consequently, a URL on the current `.in` archive host generated a one-element candidate list; after HTTP 403 there was no second official archive host attempt. The artifact's per-host diagnostics repeatedly showed only the initial `.in` URL, confirming this exact gap.

## Change
- Added the current `nsearchives.nseindia.in` host to the official attachment discovery allowlist.
- Added a bounded same-path fallback from `nsearchives.nseindia.in` to the established NSE archive host `archives.nseindia.com` after 403.
- Added reciprocal fallback for legacy archive URLs to the current NSE `.in` archive host.
- Added a regression test: first host returns HTTP 403, second official host returns HTTP 200; assert exact fallback URL and exactly two requests.
- No third-party mirror, altered path, access-control bypass, or aggressive retry added.

## CI verification state
- Code commit: b8a9f541ec98fbf427caec27905cc4e4f4fba5da
- Regression test commit: 6eed3272521cea3ab1b4eb255b55f5eeb3ceaabf
- Targeted test Run #135 (44992957011): regression-suite step completed SUCCESS, including the new .in-to-.com fallback test. The overall job remains IN_PROGRESS because bounded live XBRL extraction, feature rebuild, diagnostics and artifact upload have not completed. Therefore unit/regression acceptance is PASS, but end-to-end extraction acceptance remains PENDING.
- Run #134 (44992948452) was triggered on the intermediate code-only commit and is not the final acceptance run.

## Next action
Inspect Run #135's targeted regression result. If PASS, run a bounded official-source extraction on the same failed URLs and compare per-host diagnostics and newly verified metric counts. Do not claim the 426 blocked rows are resolved unless source-linked XBRL facts are actually fetched, parsed, and validated.

## Invariants
Audit branch only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged. ₹0 spend, official free sources only, no synthetic metrics or fabricated timestamps. UNKNOWN/BLOCKED never becomes PASS.
