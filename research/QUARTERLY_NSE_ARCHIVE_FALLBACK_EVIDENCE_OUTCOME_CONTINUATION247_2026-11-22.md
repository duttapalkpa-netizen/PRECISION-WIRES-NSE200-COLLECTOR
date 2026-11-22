# Quarterly NSE Archive Fallback — Evidence Outcome C247

Date: 2026-11-22
Branch: audit/prospective-selector-tracking

## Continuity check
Reviewed the C245 coverage triage and C246 host-fallback report before selecting this follow-up. PASS work was not repeated. No standalone `GITHUB_MASTER_CONTINUITY_LEDGER.md` was located in the prior repository inspection; continuity is recorded in the numbered research reports and workflow evidence.

## C246 acceptance evidence
- Final targeted workflow Run #135: `44992957011`, head `6eed3272521cea3ab1b4eb255b55f5eeb3ceaabf`, completed SUCCESS.
- All job steps completed successfully: targeted quarterly regression tests, official NSE security-master refresh, endpoint/schema audit, source-linked XBRL extraction, normalized feature rebuild, filing timestamp/ISIN diagnostics, and artifact upload.
- Artifact: `quarterly-endpoint-schema-audit`, ID `14742483865`, 9,411,646 bytes.
- Artifact SHA-256: `109f64d618567e99f65e559c7e3aad5d9e794bf94834dfa29773ee9c5e2cbad5`.

## Measured coverage outcome
Compared with C245's artifact (67 verified metric rows, 426 blocked, 7 superseded), Run #135 produced:
- 476 verified source-linked metric rows across 275 symbols.
- 1 blocked row.
- 23 superseded revision rows.
- 500/500 result disclosure source-validation records valid; 500 disclosures processed without truncation.
- 501 attachment attempts.
- Only two residual errors surfaced: one official NSE XBRL URL returned HTTP 404 (AGL), and one iXBRL attachment had zero parseable facts / incomplete basis metadata (AGL).
- Verified rows retain source URL, disclosure timestamp, period, basis, Revenue, PAT, EPS, and source-linked evidence. The CSV has 476 rows and 275 distinct symbols.

This is a strong observed improvement after the bounded official-host fallback change: verified rows increased by 409; blocked rows fell from 426 to 1; superseded rows are separately identified. Do not claim the fallback alone caused every recovered row unless per-attempt host-level attribution is separately established. No third-party mirrors or synthetic facts were used.

## Remaining blockers
- Financial metric coverage remains `BLOCKED_INCOMPLETE_OR_UNVERIFIED_COVERAGE` in the generated report despite the much higher verified count; preserve this gate until the full coverage contract is satisfied.
- Event study remains `BLOCKED_MISSING_EVENT_OR_PRICE_PANEL` because `data/processed/nse_eq_200_sessions.csv` is absent from this targeted artifact.
- Filing timestamp diagnostics: `creation_Date` present for 500/500; `broadcast_Date` present for 463/500 and missing for 37/500. Missing broadcast time must not be silently replaced with creation time as though it were broadcast time.

## Next action
Continue the already-running full prospective audit Run #383 (`44992957027`) and inspect its corrected-label walk-forward result before any downstream Macro-Geo or selector conclusions. Do not start duplicate collection while that run is active. If its run completes, inspect each step and artifacts; otherwise preserve its in-progress state and select only an independent, non-overlapping task.

## Invariants
Audit branch only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged. ₹0 spend; free official sources only; no synthetic data, fabricated timestamps, unofficial mirrors, or access-control bypass. UNKNOWN/BLOCKED never becomes PASS.
