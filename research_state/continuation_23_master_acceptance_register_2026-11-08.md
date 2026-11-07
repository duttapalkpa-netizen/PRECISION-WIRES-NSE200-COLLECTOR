# PRECISION-WIRES V11.3 — Continuation 23
Date: 2026-11-08
Page: গবেষণা যাচাই অব্যাহত 23
Branch: fix/iip-41-vintage-audit-clean

## Completed bounded task: canonical acceptance register V1
- Register file: research_state/MASTER_ACCEPTANCE_REGISTER_V1_2026-11-08.csv
- Register commit: 3ad3343f304a5b9913264df817e71f4b802c2950
- Register blob SHA: daa1fd2cfaf2ca89c089009973a81e43368fc4b7
- Readme/policy file: research_state/MASTER_ACCEPTANCE_REGISTER_V1_README_2026-11-08.md
- Readme commit: 78696ccdcc3abb30d92d98d00f5604269effb6a0
- Readme blob SHA: a934abff34e45b672c66df68a3388f465fe2602a
- Read-back verified both files from GitHub branch.
- CSV contains 721 data rows + header: 10 parent workstreams, 672 explicit CORE-672 diagnostic rows (56×12), and 39 cross-workstream/final-paper acceptance rows.
- Duplicate acceptance IDs: 0.
- 10 parent workstreams have provisional equal 10% weights. Weighting is explicit, documented, and versioned; child items are equally weighted inside their parent unless a future evidence-backed version changes it.

## Exact recovered final-paper acceptance requirements included
- Batch 006 PIB cell crosswalk.
- 693-candidate master ledger with source workbook, official PIB value, stage, vintage, and SHA-256 per bounded batch.
- 431 historical/out-of-window rows classified with evidence.
- NSE raw provenance and financial-record validation.
- Factor Registry/P0 and historical-regime audit.
- Event Study matured-window validation.
- Final Hard Gate reconciliation.
- Unverified source cells remain PENDING, never certified by inference.

## Status semantics
PASS requires exact evidence and acceptance test. PARTIAL earns credit only for objectively separable passed subtests. PENDING is unresolved, not FAIL. BLOCKED, UNKNOWN, NOT_CERTIFIED and QUARANTINED earn no PASS credit. Workflow SUCCESS alone is insufficient.

## Current progress reporting
- This bounded register-creation task: 100% (all enumerated rows generated, written, read back, dimensions and unique IDs verified).
- CORE-672 enumeration: 100% (56×12=672 rows enumerated); this does NOT mean all 672 diagnostics are implemented, live, tested or matured.
- Full project overall percentage: NOT YET CERTIFIABLE. Register denominator is now frozen for V1, but evidence/status reconciliation across all 721 rows is not yet complete. Do not repeat historical 36% as current.
- Historical 36%: stale baseline only.
- Do not calculate an overall score until all statuses, references, dependencies and objective partial-credit subtests have been reconciled.

## Already completed evidence — do not repeat
- April+May 2026 official IIP API vs PIB comparisons: 86/86 PASS in Run 42381121341 (#12), Artifact 13577128037, ZIP SHA-256 2337b9ed18d0057cac3a4c503a6d0657f0750df720f5a50878f14b3fc67d5059.
- Native April catalogue XLSX remains NOT RECOVERED; API is not a substitute for XLSX provenance.
- 41-month XLSX ingestion 39/41=95.1% ingestion ratio only; full IIP vintage audit BLOCKED_WITH_GAPS; 693 transitions with 431 unresolved.
- Previous batches 001–005: 54 structural rows validated; this is not source-cell certification.
- September IIP QA bounded pass; raw PIB PDF binary hash remains unavailable.
- Next-Day Radar one-off completed; daily automation not enabled.
- Legacy 37-row April PIB transcription preserved and QUARANTINED from current-series joins due to base-year conflict and omission of six use-based rows.

## Next highest-value action
Reconcile existing immutable evidence against the 721 register rows without rerunning completed jobs or data acquisition. First populate exact PASS evidence references for already-completed bounded work; then identify the smallest unresolved, high-dependency gap. Reconcile the 693-candidate ledger and Batch 006 evidence without promoting structural QA to source-cell certification.

## Invariants
Production selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 architecture unchanged. UNKNOWN is neither PASS nor FAIL. No synthetic rows, fabricated timestamps, guessed IDs, unsupported source promotion, Hard Gate relaxation, main merge or automation enablement. Research spend ₹0; free official sources only.
