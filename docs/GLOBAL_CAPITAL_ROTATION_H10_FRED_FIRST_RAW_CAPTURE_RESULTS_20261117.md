# Global Capital Rotation — First Raw Capture Results and Corrections
Date: 2026-11-17 (Asia/Kolkata)
Status: H.10 RAW + OFFICIAL CROSSWALK CAPTURED; EXACT CROSSWALK ROW VERIFIED; FRED CSV TIMEOUT; FULL-HISTORY COMPARISON BLOCKED

## New captured artifact
- Workflow: H.10 and FRED raw evidence capture #1.
- Run ID: 44059623660.
- Artifact ID: 14316998800.
- Artifact name: h10-fred-raw-capture-44059623660.
- Artifact ZIP size: 2,270,670 bytes.
- Artifact ZIP SHA-256: aff5960c6a87b75e28d06097924c61f6a24f39f9b6825932ce6190631b24af82.
- Artifact downloaded and unpacked for independent inspection.

## Raw H.10 XML evidence
- Source: https://www.federalreserve.gov/releases/h10/data/FRB_h10_xml.zip
- HTTP 200; content type application/x-zip-compressed; byte length 2,088,268.
- Raw H.10 ZIP SHA-256: c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77 (matches previously captured raw payload hash).
- ZIP integrity: PASS; four members; H10_data.xml uncompressed size 27,426,691 bytes.
- Parsed exactly one target Series SERIES_NAME=JRXWTFB_N.B.
- Observation count 5,445; OBS_STATUS=A 5,231; OBS_STATUS=ND 214; duplicate date count 0.
- First observation 2006-01-02 = 101.4155 (A); last observation 2026-11-13 = 122.6503 (A).
- ND values remain missing; no zero substitution or forward fill.
- Important metadata conflict: the raw XML Series UNIT attribute is Index:_1997_Jan_100, while the current H.10 release HTML table was previously observed to label the daily index JAN06=100. Do not silently resolve this conflict. Keep UNIT metadata discrepancy open pending Board clarification / validated transformation history.

## Official DDP/FRED Crosswalk CSV
- Source: https://www.federalreserve.gov/data/documents/DDP-FRED%20Data%20Series%20Crosswalk.csv
- HTTP 200; content type application/octet-stream; byte length 1,775,573.
- Raw CSV SHA-256: 536ba3dc62d10f51d70208a6f35aea022bb4d41d9feb2659de22cf649065852d.
- Header columns: ddp_release, board_series_id, fred_series_id.
- Data rows: 50,313.
- Exact verified row: ddp_release=H10; board_series_id=JRXWTFB_N.B; fred_series_id=DTWEXBGS.
- A second row also shares the FRED code DTWEXB but has a distinct board_series_id V0.JRXWTFB_N.B; do not confuse it with target mapping.
- First capture script incorrectly searched for board_series_id=H10/H10/JRXWTFB_N.B and returned zero matches. Root cause: it concatenated the release/namespace prefix into the board_series_id column. Correct schema interpretation is release=H10 and board_series_id=JRXWTFB_N.B. Parser corrected in commit f2402feff4dba0f27d82fc9e89e9243d8458e1eb.

## FRED CSV acquisition failure
- Candidate URL: https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS
- Run #1 failed to read the FRED response before timeout; no FRED CSV file or hash was created.
- The second/third workflow attempts had a syntax error introduced while adding XML parsing; root cause recorded and fixed in commit 21682a98f2ec4becbbeb579e90e53f5a0993441a.
- Fourth capture run: Run ID 44060344559 was in progress at the time of this record; do not claim its outcome until polled.

## Regression evidence
- Overlay regression workflow #239 associated with corrected script commit 21682a98f2ec4becbbeb579e90e53f5a0993441a: job 133959847699 completed SUCCESS (unit tests).
- Its separate raw capture job failed due the syntax error at that commit; the script was corrected afterward.

## Current acceptance
- H.10 raw capture + SHA-256: PASS.
- H.10 ZIP integrity + target series parse + status/date counts: PASS.
- Exact official DDP/FRED Crosswalk row: PASS.
- FRED raw CSV + SHA-256: NOT_DONE (timeout in first successful script run).
- Full date/value reconciliation: NOT_RUN.
- Historical vintage/revision archive: NOT_DONE.
- Collector/registry migration: BLOCKED / NOT_AUTHORIZED.

## Next actions
1. Complete the corrected capture run and inspect artifact/manifest. If FRED CSV still times out, use a bounded date-range CSV request or split time windows and record each payload/hash.
2. Reconcile the full 5,445 H.10 observations against FRED on overlapping dates; report active matches, value mismatches, missingness differences and duplicate dates.
3. Resolve raw XML UNIT vs release HTML JAN06=100 discrepancy before using this field in any model; no silent relabel or second application of 1.014163.
4. Build vintage snapshots and revision-diff tests before any migration.

## Invariants
Research-only; no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN never PASS. No synthetic values, fabricated hashes or timestamps. ₹0 spend.

## Follow-up verification and segmented-retrieval correction (2026-11-17)
- Capture Run #4: 44060344559; conclusion FAILURE. Job 133960296156 completed capture step successfully and uploaded artifact ID 14318466122, but acceptance step failed because FRED graph CSV read timed out. Artifact ZIP SHA-256 reported by GitHub: 342c3555026d5ffcc8104e71ce02a5998530d513a5367dbba4856c2d9910f7e1.
- Run #4 manifest independently printed: H.10 ZIP integrity PASS; H.10 target series 5,445 rows (A=5,231; ND=214), zero duplicate dates; crosswalk 50,313 rows and exactly one target mapping. Only error: fred_dtwexbgs.csv TimeoutError. Thus the syntax error was fixed; persistent blocker is the monolithic FRED download latency.
- Overlay Run #239: 44060344569; tests job 133960300838 SUCCESS; raw capture job failed for the same FRED timeout. Do not label the complete workflow PASS.
- New corrective implementation committed after Run #4: bounded five-window FRED retrieval (2006–2010, 2011–2015, 2016–2020, 2021–2025, 2026 YTD through 2026-11-13), each raw CSV saved separately with independent URL, retrieval time, byte length, SHA-256, row/date coverage and missing-value count. No synthetic concatenated raw payload. Each window has a 45-second request timeout.
- Code commit: 4fc63d7727e08aac8140540abb9a830a07fd7993.
- Script blob SHA after re-fetch: d7d5a731135b538b54aed4e1ae3f579c984f50a4.
- Segmented capture execution: PENDING at checkpoint creation; no new run ID/artifact or capture PASS claimed yet.
- New acceptance remains BLOCKED until all five windows are fetched and independently validated, then full date/value/missingness reconciliation is performed. XML UNIT metadata conflict remains open.
