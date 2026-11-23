# NSE Session-Spine Correction Readiness — Continuation 63
Date: 2026-11-23 (Asia/Kolkata)
Project: PRECISION-WIRES V11.3 / NSE historical archive QA
Status: ROOT CAUSE VERIFIED; OFFLINE DATE-SEMANTIC REQUIREMENTS VERIFIED; 200-SESSION RESTORATION BLOCKED PENDING PERMITTED RAW DATA ACCESS.

## 1. Mandatory continuity preflight
- Read the Library Mother File through Continuation 57 and the current GitHub Master Continuity Ledger through Continuation 62.
- Re-opened the controlling NSE semantic audit, Failure & Lessons Learned 2026-11-23, FBIL Continuation 58, NSE CSV Continuations 59–60, and CDSL Continuations 61–62.
- Skipped completed work: accepted 200-file byte/hash verification, NSE archive acquisition QA, canonical panel build, archive schema regression, Macro-Geo report-integrity regression, FBIL route audit, NSE provisional CSV source/rights boundary, and CDSL current-snapshot/archive retries.
- No workflow dispatch, no new NSE download, no production integration, and no Macro-Geo rerun.

## 2. Independent artifact re-verification
- Downloaded GitHub Actions artifact 14757294944 from run 45027842316.
- ZIP SHA-256 independently recomputed: `212a84103f2a9f47681865c7e165fe0247001b02d9563a5cef578636fb0b1898`.
- Manifest entries: 200; retained CSV files: 200; every retained file byte count and SHA-256 matches the manifest: 200/200.
- Requested dates in `sessions.txt`: 200 unique dates, 2026-02-16 through 2026-11-20.
- Independently parsed each CSV's internal `DATE1`: only 188 unique observed exchange dates.
- Exactly 12 requested dates have internal DATE1 equal to the previous trading day and their retained file SHA-256 is identical to that prior day's file:
  - 2026-03-03 → 2026-03-02 (Holi)
  - 2026-03-26 → 2026-03-25 (Shri Ram Navami)
  - 2026-03-31 → 2026-03-30 (Mahavir Jayanti)
  - 2026-04-03 → 2026-04-02 (Good Friday)
  - 2026-04-14 → 2026-04-13 (Ambedkar Jayanti)
  - 2026-05-01 → 2026-04-30 (Maharashtra Day)
  - 2026-05-28 → 2026-05-27 (Bakri Id)
  - 2026-06-26 → 2026-06-25 (Muharram)
  - 2026-09-14 → 2026-09-11 (Ganesh Chaturthi)
  - 2026-10-02 → 2026-10-01 (Gandhi Jayanti)
  - 2026-10-20 → 2026-10-19 (Dussehra)
  - 2026-11-10 → 2026-11-09 (Diwali-Balipratipada)
- Result: 200/200 byte-integrity PASS; semantic 200-session coverage FAIL / NOT ACCEPTED. The current QA report's 200 session count is requested-slot count, not distinct observed DATE1 count.

## 3. Code-level root cause
- `collector/nse_download.py` skips Saturday/Sunday only; it does not exclude the official NSE capital-market holiday calendar.
- The legacy cached-file validator checks CSV shape/series/positive close but does not compare internal DATE1 with the requested date.
- `validate_full_delivery` checks schema and numeric content but does not assert the source date equals the requested date.
- UDiFF normalization has an expected-date check, but that does not protect the legacy download/cache path that supplied the affected holiday duplicates.
- `qa/validate_dataset.py` counts rows in `sessions.txt` and accepts `sessions >= 200`; it does not reconcile manifest trade_date against each CSV's internal DATE1, holiday membership, duplicate file hashes, or unique observed dates.
- Root cause: verified. No code was modified in this continuation.

## 4. Official holiday-calendar cross-check and 12 earlier candidate sessions
- Official NSE Capital Market trading-holiday circular: NSE/CMTR/71775, dated 12-Dec-2025. It identifies 26-Jan-2026 as the only weekday holiday before the current archive's first requested date, 16-Feb-2026.
- The 12 immediately preceding weekday dates that are not listed as 2026 Capital Market holidays are:
  `2026-01-29, 2026-01-30, 2026-02-02, 2026-02-03, 2026-02-04, 2026-02-05, 2026-02-06, 2026-02-09, 2026-02-10, 2026-02-11, 2026-02-12, 2026-02-13`.
- These are calendar-derived candidate dates only. No raw files, download receipts, or hashes exist for them in this continuation; they are NOT_CAPTURED and cannot be counted toward 200.

## 5. Conservative source-use boundary
- NSE Terms of Use, updated 29-Oct-2025, prohibit systematic or automated data collection on the website and restrict copying/storage absent prior written permission, subject to the specific downloadable-content terms.
- No project-specific written permission or data agreement authorizing automated archival of these raw daily files was found in the reviewed record.
- Therefore this continuation did not run the collector, probe/replay undocumented requests, or acquire the 12 additional files. This is a conservative operational gate, not a legal opinion.
- No synthetic rows, calendar-filled prices, manual date relabeling, proxy values, or prior-session forward-fill are permitted.

## 6. Required corrective acceptance contract
Before any corrected 200-session claim:
1. Use the official NSE Capital Market holiday calendar as an explicit date exclusion source; do not equate weekdays with trading sessions.
2. For every retained file, parse internal DATE1 and require exact equality with manifest trade_date.
3. Reject any date in the official holiday list; quarantine a repeated previous-session payload instead of counting it as a new session.
4. Require 200 unique internal DATE1 values, 200 unique manifest trade_date values, one-to-one date equality, and zero duplicate-date payload collisions.
5. QA status must fail closed if unique observed dates < requested sessions, even when file count and hashes pass.
6. Preserve all 188 valid existing raw files unchanged. Add the 12 earlier dates only after the source access/retention permission boundary is resolved and raw bytes are obtained through a permitted official route.
7. Only after corrected raw archive QA passes should the corrected session spine feed label-v2/walk-forward tests. Recompute all denominators and metrics from row-level outputs; previous target metrics remain PROVISIONAL / NOT ACCEPTED.

## 7. Acceptance matrix
| Gate | Status |
|---|---|
| Artifact ZIP SHA-256 reverified | PASS |
| 200/200 retained file hashes and byte counts | PASS |
| 188 unique internal DATE1 dates confirmed | PASS |
| 12 holiday duplicate mappings confirmed | PASS |
| Collector holiday exclusion | NOT_IMPLEMENTED |
| Manifest DATE1 equality QA | NOT_IMPLEMENTED |
| 12 earlier raw sessions | NOT_CAPTURED |
| Corrected 200 unique sessions | BLOCKED |
| Historical walk-forward metrics | UNKNOWN / NOT_ACCEPTED |
| Production selector/ranking changes | NONE |

## 8. Exact next action
- Implement and run a bounded offline date-semantic QA regression on the already retained artifact; keep it research-only and fail closed on DATE1/manifest/holiday mismatch.
- Do not run any new automated NSE acquisition until the raw-data usage/retention permission boundary is explicitly resolved. If no permitted zero-cost route is available, retain 188 valid dates as the only accepted observed history and keep the 200-session acceptance BLOCKED.
- Do not dispatch the existing broad prospective workflow: it combines acquisition, multiple backtests and Macro-Geo work and is not a bounded QA run.
- After the offline QA gate is proven, determine whether a permitted official route or user-supplied lawfully acquired files can supply the 12 candidate dates. Only then restore 200 unique sessions and rerun the label/backtest audit.

## 9. Invariants
₹0; official sources only; no paid API; no fabricated timestamps or synthetic observations; UNKNOWN never PASS; no proxy substitution; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; no merge or production integration.
