# NSE 200-Session Archive — Semantic Date & Timestamp Alignment Audit
**Date:** 2026-11-23  
**Scope:** Run #398 artifact; audit-only, no production changes.

## Executive result
- GitHub Actions run ID: `45027842316`; overall job `prospective-audit` was **CANCELLED** at the Macro-Geo P0 collection step. Earlier acquisition, manifest/hash, security-master and label-test steps completed successfully.
- Artifact ID: `14757294944`; branch head: `7360870b768a6ed746451afa96ea918a3bffae07`; ZIP SHA-256: `212a84103f2a9f47681865c7e165fe0247001b02d9563a5cef578636fb0b1898`. Local SHA-256 independently matches the GitHub artifact digest.
- Byte-level acquisition integrity: **200/200** raw CSVs match retained bytes, manifest byte counts and SHA-256 values.
- Semantic session coverage: **NOT ACCEPTED**. The manifest has 200 unique requested dates, but only **188 unique DATE1 trading dates** occur in the retained CSV contents. Twelve requested dates are NSE capital-market holidays and their files are exact byte-for-byte duplicates of the prior trading session.
- Therefore the artifact's `data/qa/qa_report.json` values `sessions=200` and `processed_dates=200` count requested file/date slots, not 200 distinct exchange sessions. The 200-session claim is false until corrected.
- The latest 20-Nov-2026 file itself is correctly dated and usable for the 20-Nov close/volume snapshot after the 12 holiday duplicates are removed from the time series.

## Reproducible checks
1. Opened `data/raw/acquisition_manifest.json` from the retained ZIP.
2. Recomputed SHA-256 and byte count for every manifest file: 200/200 matched `source_sha256`, `retained_sha256`, `source_bytes`, and `retained_bytes`.
3. Parsed each CSV's internal `DATE1`; compared it with `manifest.entries[].trade_date`.
4. Compared content hashes across requested dates. All twelve mismatched files are byte-identical to the prior valid session file.
5. Compared the twelve mismatched dates with the official NSE 2026 equity trading-holiday calendar (Circular NSE/CMTR/71775, 12-Dec-2025).

| Requested date in manifest | Internal CSV DATE1 | Result |
|---|---|---|
| 2026-03-03 | 2026-03-02 | Holi holiday; duplicate of 02-Mar |
| 2026-03-26 | 2026-03-25 | Ram Navami holiday; duplicate of 25-Mar |
| 2026-03-31 | 2026-03-30 | Mahavir Jayanti holiday; duplicate of 30-Mar |
| 2026-04-03 | 2026-04-02 | Good Friday holiday; duplicate of 02-Apr |
| 2026-04-14 | 2026-04-13 | Ambedkar Jayanti holiday; duplicate of 13-Apr |
| 2026-05-01 | 2026-04-30 | Maharashtra Day holiday; duplicate of 30-Apr |
| 2026-05-28 | 2026-05-27 | Bakri Id holiday; duplicate of 27-May |
| 2026-06-26 | 2026-06-25 | Muharram holiday; duplicate of 25-Jun |
| 2026-09-14 | 2026-09-11 | Ganesh Chaturthi holiday; duplicate of 11-Sep |
| 2026-10-02 | 2026-10-01 | Gandhi Jayanti holiday; duplicate of 01-Oct |
| 2026-10-20 | 2026-10-19 | Dussehra holiday; duplicate of 19-Oct |
| 2026-11-10 | 2026-11-09 | Diwali-Balipratipada holiday; duplicate of 09-Nov |

**Counts:** requested dates 200; manifest entries 200; byte/hash-valid files 200; internal unique DATE1 dates 188; date mismatches 12; duplicate-hash groups across requested dates 12.

## Point-in-time timestamp representation issue
The same artifact's quarterly-results calendar contains source raw field `an_dt` without an explicit timezone. Example: WELSPUNLIV raw `an_dt` is `21-Nov-2026 19:13:50`, while the normalized `BROADCAST_AT` and `PUBLICATION_TIMESTAMP` are serialized as `2026-11-21T19:13:50+00:00`. NSE's quote page displays the broadcast as `21-Nov-2026 19:13:50` without a UTC marker. The +00:00 suffix must not be treated as verified UTC until the source timezone contract is documented; it may be an unconverted India-local wall-clock value. The same concern applies to APLAPOLLO, TATASTEEL and HMAAGRO records. Preserve raw source text and set timezone semantics to **UNKNOWN** pending validation. Do not use these normalized fields for vintage-aligned macro/news joins.

## Impact on research
- The raw 20-Nov file is valid: manifest trade date and internal DATE1 both equal 2026-11-20; source URL is `https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_20112026.csv`; retrieved at `2026-11-22T14:00:42.495300+00:00`; raw file SHA-256 `ec8f1f246ad97ec2b4b57fd06a81084257d45c82b51af5072edbf586a9faaaa3`.
- However, the 200-session history is only 188 distinct exchange dates. Any backtest/indicator/label pipeline using the 200 requested slots without semantic de-duplication may compress or duplicate session windows.
- Run #398 `walk_forward_metrics.json` reports target metrics for +5/+10/+15/+20, but no row-level predictions are retained to remove holiday-duplicate cutoffs and recompute them. Those figures are **PROVISIONAL / NOT ACCEPTED**; accepted target hit rates remain UNKNOWN until a corrected unique-session rerun. +2% is absent from that metrics file.
- The artifact reports winner-probability mean 0.086886 versus non-winner mean 0.087184 inside the tested Top-30 cohort; the ranking signal does not show positive separation in this run. Treat as a diagnostic warning, not a production conclusion, until the date spine is corrected.

## New immutable lessons
### PW-LSN-20261123-001 — Holiday dates counted as trading sessions
- **Confirmed root cause:** session generation admitted 12 official NSE holidays into the 200-date request list; NSE returned the previous session's identical file for each.
- **Why missed:** the validator checked URL/retrieval/bytes/hash and request count, but not internal `DATE1 == trade_date`, official holiday membership, or distinct observed session count.
- **Research question:** does an official-holiday-aware session spine produce exactly 200 distinct observed exchange dates with every raw file's DATE1 matching its manifest date?
- **Bounded test:** network-free test over the existing ZIP: validate every entry's internal DATE1, holiday exclusion, unique-date count and duplicate-hash/date collisions. Then extend backfill by 12 earlier valid trading sessions; do not redownload the 188 valid existing dates.
- **Validation:** compare the next 10 newly acquired files with official NSE session dates; no synthetic sessions; require independent byte/hash and date-semantic checks.
- **Status:** ROOT CAUSE VERIFIED; CORRECTION/200-SESSION ACCEPTANCE OPEN; no production change.

### PW-LSN-20261123-002 — NSE filing timezone label not proven
- **Confirmed discrepancy:** raw `an_dt` has no timezone, but normalized timestamp fields append `+00:00`; NSE display uses the same wall-clock text without UTC designation.
- **Root-cause status:** timestamp serialization mismatch VERIFIED; whether raw source time is always IST or another timezone remains NOT VERIFIED.
- **Research question:** what timezone does the NSE announcements API contract assign to `an_dt` / `sort_date`, and does the normalizer convert or merely append UTC?
- **Bounded test:** compare raw API source text, official NSE page display, source server documentation and independently observed timezone semantics for 5 filings; assert conversion, not relabeling.
- **Carry-forward:** preserve raw time string, do not use normalized +00:00 for point-in-time joins, and keep GCR/news timestamp alignment UNKNOWN until validated.
- **Status:** DISCREPANCY VERIFIED; SOURCE TIMEZONE CONTRACT OPEN; no code/production change.

## Official source
- NSE 2026 equity trading-holiday page: https://www.nseindia.com/resources/exchange-communication-holidays
- NSE Circular NSE/CMTR/71775 (12-Dec-2025): https://nsearchives.nseindia.com/content/circulars/CMTR71775.pdf
- Raw 20-Nov bhavdata: https://nsearchives.nseindia.com/products/content/sec_bhavdata_full_20112026.csv
- Run #398: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/45027842316

## Decision / next actions
1. Rebuild the session spine using the official NSE holiday calendar; retain 188 valid existing dates and add 12 earlier valid dates to reach 200 unique trading sessions.
2. Add a date-semantic QA gate: every CSV internal DATE1 must equal its manifest trade_date; no holiday dates; distinct observed dates must equal requested session count.
3. Add a timestamp-contract regression test before admitting quarterly-results/news timestamps to point-in-time joins.
4. Rerun the corrected-label walk-forward audit only after the session spine is fixed; no historical performance rate or best-three list is accepted before then.
5. Keep Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2 unchanged.
