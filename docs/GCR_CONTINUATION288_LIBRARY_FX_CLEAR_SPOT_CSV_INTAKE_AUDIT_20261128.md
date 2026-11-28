# GCR Continuation 288 — Library FX Clear Spot Individual CSV intake and QA audit
Date: 28-Nov-2026

## Preflight
- Re-read current Master Continuity Ledger, GCR Master Priority Queue, 63-country Historical Task Registry and C287 alternative-source survey.
- Searched and listed Library's latest uploads; inspected all five `Fx_Clear_Spot_Individual2026-11-28*.csv` files and the new `Daily Interbank Forex Rates (USD vis-a-vis INR)(2).xlsx`.
- No Library upload, overwrite, rename or deletion performed. No repeat of C282-C287 completed audits.

## New files found and raw-byte fingerprints
All five CSVs have header: `Trade Date,Quantity,Trade Price,Trade Timestamp`. CSV byte hashes:
| File | Bytes | Data rows | Trade-date span | Unique dates | SHA-256 |
|---|---:|---:|---|---:|---|
| Fx_Clear_Spot_Individual2026-11-28 (2).csv | 5,987,743 | 158,152 | 2025-01-01–2025-04-30 | 76 | `e0f97ee7167fb2ea072b35169db9ace57cc0b61339e99304f0d8d3237a76a340` |
| Fx_Clear_Spot_Individual2026-11-28 (3).csv | 6,894,722 | 180,488 | 2025-05-02–2025-10-01 | 101 | `764b33036a304a1dea55756eb4403e4af9b1272facbea93d8308287d1d4eb9c5` |
| Fx_Clear_Spot_Individual2026-11-28 (4).csv | 3,040,944 | 79,455 | 2025-10-01–2025-12-31 | 61 | `1324770bd32559d9728e455e67e1a84ef5fdcf7748b157ac99366e3375c87413` |
| Fx_Clear_Spot_Individual2026-11-28 (1).csv | 5,060,564 | 132,236 | 2026-01-01–2026-06-18 | 82 | `077306322d2ab2691209b600affadc103e0cfb1dbb718bb0e344ccbac3a5b86d` |
| Fx_Clear_Spot_Individual2026-11-28.csv | 4,210,282 | 110,231 | 2026-06-29–2026-11-27 | 12 | `47694e2455cf5cfa74fd2bb1a5f9906bc8f79ee764e26f0391ce87b74ace2e9f` |

## Combined QA findings
- Total: 660,562 data rows, 331 distinct Trade Dates, observed date endpoints 2025-01-01 and 2026-11-27.
- Combined exact duplicate count (Trade Date + Quantity + Trade Price + Trade Timestamp): 213,519; unique exact tuples after deduplication: 447,043. Do not silently deduplicate for acceptance; preserve raw files and record duplicate rules first.
- One cross-file overlap: 2025-10-01 appears in files (3) and (4), with 1,048 common exact tuples.
- Intra-file exact duplicate rates: file (2) 4,626 (2.93%); file (3) 34,324 (19.02%); file (4) 13,586 (17.10%); file (1) 56,308 (42.58%); base file 103,627 (94.01%).
- 1,123 non-positive Trade Price rows in the 2025 files: file (2) has 801 (269 negative, 532 zero); file (3) has 322 (135 negative, 187 zero). No non-positive prices in the other three files.
- Null fields: 0 across all files; timestamp strings match HH:MM:SS shape in all five files.
- 2026 coverage is sparse in later months: 2026 month-level distinct Trade Dates Jan 20, Feb 19, Mar 18, Apr 19, May 5, Jun 3, Jul 7, Aug 1, Sep 1, Oct 0, Nov 1. This is captured-date metadata, not a verified expected-session completeness test.
- Trade Date order is not monotonic in files (1) and the base file. Preserve original order; do not sort/repair the raw artifact.

## Interpretation boundary
- The filename suggests an FX Clear Spot Individual extract, but CSV content itself has no source publisher, URL, currency pair, instrument/security identifier, settlement convention, units, trade-status/side, or field definition.
- The same file contains prices near 80–96 and non-positive values (in 2025), so it is unsafe to infer that every row is a USD/INR spot transaction. Without instrument/pair semantics, no valid daily OHLC aggregation can be made.
- These are transaction-level fields (quantity, trade price, time), not the RBI DBIE six-column report (Date, Interbank Open/High/Low/Close, RBI Reference Rate) and not the RBI/FBIL reference fixing archive.
- The separately uploaded `Daily Interbank Forex Rates (USD vis-a-vis INR)(2).xlsx` is 5,302 bytes; parsed sheet has only source/title, August-2000 availability note, unit, Date header and dash row, with no observations. It is an empty/incomplete report template, not a successful data export.
- Exact publisher/source provenance and permitted use remain UNKNOWN. A public web search for the exact filename/header did not identify a reliable official source. No external source has been asserted.

## Acceptance and next action
- Raw files are readable and byte hashes captured: narrow file-integrity PASS.
- Header/field shape and null/timestamp syntax: PASS as basic structural checks only.
- Duplicate integrity, non-positive prices, sparse later 2026 dates, missing pair/instrument semantics, source provenance and licensing/usage rights: BLOCKED / UNKNOWN.
- Do not ingest, merge, calculate OHLC, or use these records for the GCR USD/INR interbank panel until user supplies the original source page/export metadata or official documentation that defines the dataset, instrument/pair, units and transaction statuses. Then build a source-aware deduplication and calendar coverage audit.
- Preserve all five raw files unchanged; no duplicate Library upload.

## GCR state and invariants
The new files do not close the official RBI DBIE interbank OHLC blocker. USD/INR interbank remains BLOCKED/UNKNOWN; reference-rate stream remains separate. FPI/DII blockers unchanged. Macro-Geo P0 last artifact-backed 6/8. Strict GCR hard gate BLOCKED; candidate_release_allowed=false; overall NOT_COMPUTABLE / NOT_CERTIFIED. ₹0; CORE-672 (56x12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.


## User-supplied source provenance evidence — CCIL FX-Clear USD/INR SPOT (28-Nov-2026)
- User supplied a screenshot of `ccilindia.com` showing the FX-Clear page, Forex Market > USD/INR selected, SPOT tab selected, timestamp 28-Nov-2026 13:46:12, the `Individual Trade Details` date-range inputs and `Download CSV` control. The page explicitly labels `Source: FX Clear hosted at Clearcorp` and `Spot Rates are in Rupees`.
- The official CCIL FX-Clear page is https://www.ccilindia.com/en/fx-clear. Its rendered content independently shows SPOT / C-SPOT / R-SPOT sections, the same Individual Trade Details date range + Download CSV control, a maximum range of 182 days / 6 months, and the source/rupee note. This confirms the CSV family is from CCIL FX-Clear's USD/INR SPOT Individual Trade Details export, based on the user's screenshot and matching official page structure.
- Correction to earlier C288 wording: source provenance is no longer UNKNOWN. Mark publisher/portal/product/pair/market segment as SOURCE_CONFIRMED: CCIL > FX-Clear > USD/INR > SPOT > Individual Trade Details. The original screenshot is the user-supplied evidence; official page structure is corroboration.
- This does NOT establish every CSV row's exact export range, whether all five exports are complete or overlap intentionally, the full semantics of Quantity/Trade Price/Trade Timestamp, trade-side/status, or any licensing/reuse rights. Official page's 182-day maximum per download explains why multiple exports may be required, but does not validate the uploaded coverage.
- The dataset remains transaction-level, not RBI DBIE daily interbank OHLC + RBI reference rate, and not the FBIL reference fixing series. Keep it as a separate CCIL USD/INR spot transaction tape. Do not relabel it as RBI/FBIL data.
- QA blockers remain: 213,519 combined exact duplicate tuples, 1,123 non-positive Trade Price rows, sparse 2026 late-month dates, and missing data dictionary for field semantics / duplicate policy. Do not silently deduplicate or create OHLC until the source export definition and transaction semantics are established.
- Next action: reconcile CSV date coverage against 182-day export windows; identify whether duplicate rows are repeated trades, export overlap, or repeated page rows; validate quantity/price semantics and non-positive rows against official CCIL documentation. Keep raw files unchanged. No paid access or external contact.
