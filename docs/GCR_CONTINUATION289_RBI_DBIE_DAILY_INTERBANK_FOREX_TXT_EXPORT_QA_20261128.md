# GCR Continuation 289 — RBI DBIE Daily Interbank Forex Rates TXT export intake and QA
Date: 28-Nov-2026

## Preflight and source
- Re-read current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry and C288 CCIL source-provenance report.
- Searched Library for exact file `Daily Interbank Forex Rates (USD vis-a-vis INR) (1).txt`; found one new Library item (uploaded 28-Nov-2026 10:54:40 UTC, 348,819 bytes). Materialized a read-only working copy for byte-level inspection. No Library mutation or duplicate upload.
- TXT content itself states Source: Reserve Bank Of India; Forex Rates (United States Dollars); Data available from August 2000; Figures in Rs. Its table header is Date, Interbank Open Rate, Interbank High Rate, Interbank Low Rate, Interbank Close Rate, RBI Reference Rate. This matches the report the user had opened on official RBI DBIE in prior screenshots. Source is treated as user-exported RBI DBIE report, with content/source header confirmed; raw file itself does not contain a signed checksum or embedded download metadata.
- SHA-256: `ac8cbec57bc8c87b2c4cacd5a02f68620e44672f488bd711fd0f81565ca6bf1c`; bytes 348,819; physical lines 6,340; header at line 10.

## Structural and coverage QA
- Parsed data rows: 6,330; malformed row field counts: 0; unparseable dates: 0; all rows contain exactly six tab-separated fields.
- Date span: 08-Aug-2000 through 31-Jul-2026; 6,330 unique dates; duplicate dates: 0; exact duplicate full records: 0.
- Rows are strictly reverse chronological (newest to oldest).
- Yearly counts: 2000 99; 2001 243; 2002 252; 2003 248; 2004 250; 2005 248; 2006 249; 2007 247; 2008 243; 2009 237; 2010 246; 2011 239; 2012 242; 2013 244; 2014 237; 2015 244; 2016 242; 2017 240; 2018 243; 2019 242; 2020 243; 2021 242; 2022 244; 2023 241; 2024 241; 2025 244; 2026 140 (Jan–Jul only).
- As of 28-Nov-2026, latest observation is 120 calendar days old; no data for Aug–Nov 2026. This file is a substantial historical extract but not current through the present date.
- 6,124 rows have all five rate fields present; 206 rows have at least one dash/missing rate. Per-field missing counts: Open 199; High 193; Low 192; Close 194; RBI Reference 49. Missingness patterns: 141 rows have all four OHLC fields missing but Reference Rate present; 49 rows have all five fields missing; remaining 16 rows have partial OHLC/reference missingness.
- No duplicate dates/records and no malformed six-column rows. Basic structure and chronology PASS; expected publication-session completeness has not been calendar-verified.

## Critical data-quality anomalies — do not auto-correct
- In 6,124 complete OHLC rows, the value in the column labelled `Interbank High Rate` is lower than the value in `Interbank Low Rate` in 6,017 rows; only 107 rows have High >= Low. This strongly suggests a systematic High/Low label/value inversion in the exported table, but this has NOT been independently confirmed against RBI documentation. Do not silently swap columns.
- 140 complete OHLC rows have Open or Close outside the numeric interval formed by the reported High and Low values.
- A single extreme outlier appears: 21-Mar-2016 Open Rate is `3,355.7300` (parsed as 3355.73), far outside the surrounding USD/INR series. Treat as likely source misprint requiring official correction evidence; do not replace or drop it silently.
- No negative/zero values among successfully parsed rate numbers; dash markers are missing data, not numeric zeros.
- All numeric fields parse after removing a thousands comma from the single outlier token; retain raw token exactly as supplied.

## Decision
- Raw TXT acquisition/readability: PASS.
- Six-column schema, 6,330 valid date rows, uniqueness, reverse chronology: PASS.
- Historical coverage 08-Aug-2000–31-Jul-2026: CAPTURED (partial relative to current date).
- Full current coverage through 28-Nov-2026: FAIL / NOT CAPTURED (Aug–Nov 2026 absent).
- Value semantics/High-Low ordering and extreme outlier: BLOCKED pending RBI table/metadata confirmation; no normalization or repair.
- Missingness: 206 affected rows; requires source-calendar and publication-status adjudication.
- This is the first substantive RBI DBIE interbank OHLC + reference-rate TXT extract found in Library; it materially advances the USD/INR work but does not yet qualify for clean production ingestion or close all GCR FX gates.

## Next actions
1. Preserve this TXT as immutable raw source; use hash above as intake fingerprint.
2. Compare exact date/value rows against official RBI Table 218/222/223 periods and/or an independently downloaded official RBI export, especially High/Low labels and 21-Mar-2016 outlier.
3. Seek official DBIE data dictionary / report definition for High and Low semantics and handling of dashes.
4. Obtain official DBIE/FBIL current segment for 01-Aug-2026 onward through current date; do not fill forward.
5. Only after adjudication create a separately versioned normalized derivative with explicit correction ledger; never overwrite raw source.
6. Keep CCIL FX-Clear spot transaction data as a separate dataset and do not blend it with RBI daily interbank series.

## GCR state and invariants
The TXT materially advances the official RBI daily USD/INR series but full/current coverage and data semantics remain unresolved. USD/INR data gate is PARTIAL / BLOCKED for clean ingestion. FPI and DII remain separate blockers; Macro-Geo P0 last artifact-backed 6/8; strict GCR hard gate BLOCKED; candidate_release_allowed=false; overall NOT_COMPUTABLE / NOT_CERTIFIED. Research spend ₹0. CORE-672 (56x12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.
