# Run #352 Raw NSE Artifact Retention Verification — Continuation 229

Date: 2026-11-22 (Asia/Kolkata)
Branch: `audit/prospective-selector-tracking`
Run: `44935745368`
Run head: `c97f8dd9109dcb5becf6352cea461e5692c8f9f7`
Artifact: `14719888911` (`prospective-watchlist-audit`)
Artifact ZIP size: 35,775,451 bytes
Artifact ZIP SHA-256: `623153a4516ba3ada34d406ce8bf217efb4abf6cbf3c01b905dd233944f82fec`

## 1. Continuity preflight and task selection
Re-read the Master Continuity Acceptance Ledger, GCR Master Priority Queue and Historical Task Registry (all through C228). Reused the C228 root-cause analysis and did not repeat the Run #339 / #416 historical ZIP inventory. Selected the next stated action: verify the next bounded workflow artifact and its retained raw-source proof.

## 2. Run outcome
The GitHub Actions job is `cancelled`, not successful. Steps 1–12 completed successfully; step 13 (corrected-label walk-forward audit) was cancelled; steps 14–31 were skipped; step 32 uploaded the audit artifact successfully. Therefore this is a partial data-retention proof, not an end-to-end prospective audit PASS.

## 3. Raw NSE retention verification
Independent ZIP inventory:
- 702 total archive entries.
- 200 `data/raw/sec_bhavdata_full_*.csv` raw NSE files.
- `data/raw/sessions.txt`: 200 unique dates, 2026-02-16 through 2026-11-20.
- `data/raw/acquisition_manifest.json`: schema v1, 200 entries, generated_at_utc `2026-11-21T18:37:48.984020+00:00`.
- `data/raw/acquisition_diagnostics.json`: 200 valid sessions, first/last dates consistent with sessions file.
- `data/qa/qa_report.json`: PASS; raw_files=200, sessions=200, processed_dates=200, symbols=2,999, delivery quantity/percentage coverage 100%, issues=[].
- `outputs/prospective/acquisition_manifest_validation.json`: PASS; requested_sessions=200, manifest_entries=200, verified_retained_files=200, fully_provenanced_entries=200, errors=[].

Independent per-entry byte/hash reconciliation was run against the actual ZIP members using each manifest `retained_file`:
- manifest entries: 200
- retained paths missing: 0
- SHA-256 mismatches against both retained_sha256 and source_sha256: 0
- retained/source byte-count mismatches: 0
- entries missing retrieval timestamp or source/requested URL: 0
- content-type mismatches against text/csv: 0

All 200 entries declare acquisition status `ACQUIRED_AND_HASHED` and provenance status `VERIFIED_AT_ACQUISITION`. This is contemporaneous acquisition provenance, not retrospectively inferred metadata.

## 4. Remaining packaging gap
No security-master file is present anywhere in this artifact inventory (no path containing `security_master` or `master`). The QA report records 2,999 symbols, but that does not substitute for retaining the security-master source file. Therefore the full C228 requested artifact bundle (raw files + sessions + diagnostics + security master + manifest) is not fully satisfied.

The artifact also contains no `data/processed/` panel. Do not treat this as evidence that the complete normalized panel was retained.

## 5. Quarterly metrics readback
The artifact includes quarterly reports and 486 XBRL evidence files. The quarterly report records 500 disclosure rows, 500/500 source validation, 2,971 calendar rows, 476 verified financial metric rows, 23 superseded revisions, and one blocked AGL row. AGL's XBRL returned HTTP 404 and its iXBRL fallback exposed zero required facts; keep it BLOCKED, not zero or PASS.

## 6. Acceptance decision
- C228 raw NSE CSV retention: PASS for this artifact (200/200).
- Sessions and acquisition diagnostics retention: PASS.
- Per-file acquisition-time URL/timestamp/content-type/bytes/SHA-256 provenance: PASS for 200/200, independently reconciled.
- Security-master retention: NOT PRESENT / BLOCKED.
- Complete C228 bundle acceptance: PARTIAL / NOT ACCEPTED.
- Run #352 end-to-end prospective audit: CANCELLED; corrected-label walk-forward and downstream Macro-Geo, selector, reproducibility, hard-gate and pick steps were not completed.

## 7. Protected invariants
Audit-only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E unchanged. No paid API, no synthetic data, no fabricated timestamps. ₹0. UNKNOWN never PASS.

## 8. Next non-duplicate action
Fix and test the missing security-master artifact path on the audit branch, then run a short bounded retention-only verification (not the full long prospective workflow). Keep the 200/200 raw-file retention proof closed for this exact artifact; do not repeat its hash audit absent a changed artifact.
