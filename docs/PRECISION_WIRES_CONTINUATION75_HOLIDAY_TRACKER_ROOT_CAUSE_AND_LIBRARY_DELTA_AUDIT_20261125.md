# PRECISION-WIRES V11.3 — Continuation 75: Holiday Tracker Root-Cause & Library Delta Audit
**Date:** 25-Nov-2026 (IST) | **Page:** গবেষণা যাচাই অব্যাহত 56, Part-2  
**Status:** PRE-FLIGHT PASS; AUDIT-ONLY ROOT CAUSE RECONFIRMED; IMPLEMENTATION / REGRESSION TEST OPEN  
**Mode:** Read-only research audit; ₹0

## 1. Mandatory preflight and no-repeat controls
- Re-fetched the default-branch Master Continuity & Acceptance Ledger through C74.
- Re-read C72 pre-task decision, C73 export inventory audit, C74 daily pre-market report, 25-Nov Failure & Lessons Register, and the Library Mother File (continuations 1–53).
- Reused C74's accepted Run #410 / #421 artifact hashes and holiday evidence; no repeat artifact downloads, broad workflow dispatch, or NSE data acquisition.
- C74's holiday-maturity lesson PW-LSN-20261125-001 is the controlling unfinished task. No accepted PASS task was reopened.

## 2. C74 issue — audit-only code inspection
Fetched `prospective_watchlist_tracker.py` from branch `audit/prospective-selector-tracking`; blob SHA-1 `f28f7c752c4eaadeb5583f4434190a124a4910d9`.
- `outcome()` selects the next 1/3/5 rows after cutoff from each symbol's sorted price rows. It has no official NSE session-spine / holiday validation.
- `drop_duplicates("DATE")` removes duplicate dates but does not establish that a date is an official trading session or that duplicate-content rows are semantically valid.
- Maturity is set when the next h rows exist and their HIGH_PRICE values are non-null. Thus a holiday-labelled or otherwise invalid row can incorrectly advance a horizon.
- `OUTCOME_LAST_DATE` is only populated inside the H+5 branch. H+1/H+3 maturity can be written without an outcome-end date; this reproduces the C74 observed inconsistency.
- Captured picks/ranks/scores are treated as immutable; this audit does not propose changing them.

## 3. Required fail-closed correction contract (audit-only branch)
1. Add an explicit, versioned official NSE trading-session spine as a required tracker input; missing/unparseable calendar must stop the tracker or leave all affected outcomes PENDING, never infer sessions from price rows.
2. For each cutoff and horizon H+1/H+3/H+5, derive the exact next 1/3/5 official sessions strictly after cutoff. Holiday rows must never count.
3. Require one valid price observation per expected session and symbol; reject missing, duplicate, non-session, out-of-order, or conflicting rows. Do not silently deduplicate conflicting price records.
4. Persist a horizon-specific end date (e.g. `T1_OUTCOME_LAST_DATE`, `T3_OUTCOME_LAST_DATE`, `T5_OUTCOME_LAST_DATE`) or an equivalent normalized outcome table. A matured flag is valid only when its matching end date equals the expected official horizon end date.
5. Keep high-touch target-hit labels distinct from executable/cost-adjusted returns. No production ranking, selector, score, or threshold changes.
6. Add regression fixtures for 23-Nov-2026 → H+1 25-Nov, H+3 27-Nov, H+5 01-Dec; 24-Nov holiday must be excluded. Add a second holiday-adjacency case and cases for missing session, duplicate date, duplicate-content date, missing HIGH_PRICE, and missing calendar.
7. Re-run at least two retained audit artifacts and compare deterministic row-level outputs before any label acceptance. No workflow run until tests and runtime bounds are reviewed.

## 4. Current Library delta — inventory only
- Recursive Library snapshot: 1,445 items returned across 15 pages, no listing warnings; 399 `.dat` files, aggregate stored size 278,932,615 bytes.
- Inventory-bearing `export_manifest(2).json` remains 210,361 bytes and declares 821 export files (807 `.dat`, 12 `.json`, one `.txt`, one `.html`).
- `/ChatGPT_Data_Export_2026-11-25` currently contains 7 files: `library_files.json`, `message_feedback.json`, `sectioned_conversations.json`, `shared_conversations.json`, `THIRD_PARTY_NOTICES.txt`, `user.json`, `user_settings.json`. The sectioned-conversations file is 2 bytes.
- Two dated incoming folders currently contain 13 and 7 items respectively; additional 6 date-stamped .dat uploads are present in `/PRECISION-WIRES/Research Uploads`. This is a snapshot of upload activity, not proof of Export membership.
- Raw count difference 807 expected .dat vs 399 Library .dat is 408, but this is **not** a verified missing-file count: Library items may include unrelated files, renamed files, duplicates, and files from other batches. Manifest-to-Library exact path/size join and SHA-256 verification remain NOT_DONE. No payload is promoted on filename alone.

## 5. Status and next exact action
- C75 preflight and audit-only static root-cause review: PASS.
- PW-LSN-20261125-001 correction implementation: OPEN.
- Regression tests / second-artifact verification: NOT_DONE.
- Export manifest expected-vs-actual payload mapping: NOT_DONE; package provenance remains UNKNOWN.
- 23-Nov cohort H+1 remains PENDING until 25-Nov market close; H+3 expected 27-Nov and H+5 expected 01-Dec. Do not mark success/failure before the respective close.
- Next highest-value action: implement and test the calendar-aware correction on the audit-only branch, with official NSE session-spine input and per-horizon outcome dates. Keep production integration separate and unauthorized.

## 6. Controls
No workflow dispatch, no NSE acquisition, no paid source, no external contact, no merge/delete/move, and no Production Selector / `RANKING_SCORE` / `+1 PRESSURE_FADE` / CORE-672 (56×12) / Engines A–E / IPO-PLX V2.0 changes. ₹0. UNKNOWN is neither PASS nor FAIL.
