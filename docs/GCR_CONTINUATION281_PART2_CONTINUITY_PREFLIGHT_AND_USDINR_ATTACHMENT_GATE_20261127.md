# GCR Continuation 281 — Part-2 continuity preflight and USD/INR attachment identity gate (27-Nov-2026)

Date: 2026-11-27 (Asia/Kolkata)
Conversation: গবেষণা যাচাই অব্যাহত 62, Part-2

## 1. Mandatory continuity preflight
- Re-fetched the default-branch Master Continuity Ledger; current blob SHA before this report: 8e33fe13365fe642605d12640a1f283232cb27fe.
- Re-read the complete C280 official USD/INR historical-source verification report, the ledger tail through C280, GCR Master Priority Queue, and the 63-country Historical Task Registry.
- Re-opened the Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md` (curated addenda through C57) and the 24-Nov Data Export Recovery Audit Phase 1.
- Applied the no-duplicate rule: C278 archive-contract regression PASS, NSE raw archive QA, canonical panel rebuild, CDSL repeated retry, and export Phases 4–6 were not repeated.

## 2. Selected unfinished task
Continue only the C280 handoff: obtain the original official RBI/FBIL USD/INR historical reference-rate Excel file, then preserve and validate its exact bytes. This is not a new source-discovery task; C280 already confirmed source identity and IMF metadata's historical-availability statement.

## 3. Library attachment preflight
- Queried Library for recent XLS/XLSX-class files, sorted newest first.
- The two newest 27-Nov uploads were materialized and inspected as workbooks:
  - 7,949,825-byte workbook: sheets `Methodology`, `OOS target-adverse grid`, `Candidate events`, `Test-period summary`, `Cooldown robustness`; its own methodology identifies an NSE bhavcopy-derived short-horizon research screen.
  - 3,304,048-byte workbook: `NSE DATA CENTRE` and NSE contract/index reference sheets; its contents identify NSE bhavcopy and contract/reference material.
- Neither is an RBI/FBIL USD/INR historical reference-rate workbook. They were not repurposed, renamed in Library, or uploaded again. The original Library files remain unchanged.
- No exact original USD/INR historical workbook was identified among the newest 27-Nov uploads. This scoped check is not a claim that every older Library file was exhaustively re-parsed.

## 4. Evidence boundary and acceptance
- C280 official source family and historical-availability statement: CONFIRMED (carried forward).
- Original RBI/FBIL USD/INR workbook bytes in this turn: NOT_FOUND / NOT_ATTACHED.
- Workbook schema, date span, distinct-date count, duplicate/missingness QA, units, retrieval metadata and SHA-256: NOT_RUN.
- USD/INR ingestion: BLOCKED / UNKNOWN; no PASS or AVAILABLE promotion.
- Macro-Geo P0: last artifact-backed 6/8; strict GCR hard gate BLOCKED; `candidate_release_allowed=false`; overall GCR NOT_COMPUTABLE / NOT_CERTIFIED.
- FPI/DII remains a separate blocker; no substitution, new ingestion or terms circumvention attempted.

## 5. Exact next action
User/authorized operator must download the original USD historical date-range Excel directly from the official RBI/FBIL interface and attach that exact unmodified file in the conversation. On receipt:
1. Preserve original bytes and calculate SHA-256 before parsing.
2. Record exact source URL, retrieval time, response metadata and workbook identity.
3. Inspect sheets/schema, units and observation-date semantics.
4. Test duplicate dates, missingness, numeric validity and date coverage (minimum 60 distinct valid dates spanning at least 90 calendar days).
5. Admit only checks supported by the original workbook; no interpolation, forward-fill, synthetic rows or third-party mirror substitution.

If the official download fails, record the exact UI error/outcome and keep the task BLOCKED. Do not repeat the same page-extraction attempt without a genuinely new supported route or source evidence.

## 6. Protected invariants
₹0 spend; official/free sources only; UNKNOWN is neither PASS nor FAIL; no credential bypass or external contact. H+3 State calibration remains at least 50 fully matured observations per State. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 remain unchanged. No merge, production integration, threshold change or broad workflow run.
