# GCR Continuation 303 — CCIL FX-Clear USD/INR SPOT CSV window, duplicate and field-semantics audit
Date: 28-Nov-2026 (Asia/Kolkata)

## 1. Preflight / duplicate prevention
- Re-read current Master Continuity Ledger, GCR Priority Queue, Registry, fixed 63-country matrix, C288 and Library Mother File 1–53.
- C288's five original Library CSVs were materialized read-only into the working container; no Library upload, overwrite, rename or deletion. All five raw SHA-256 values were independently recomputed and match C288.
- No RBI DBIE/FBIL file was merged; no OHLC generated; no data row removed or repaired.

## 2. Official source semantics (new documentary boundary)
- Official CCIL FX-Clear page identifies SPOT, C-SPOT and R-SPOT separately; says the source is FX Clear hosted at Clearcorp, spot rates are in Rupees, and the Individual Trade Details CSV date range is limited to 182 days / six months: https://www.ccilindia.com/en/fx-clear .
- The five uploaded CSVs' source identity and selected product/pair/segment are supported by the user's 28-Nov screenshot recorded in C288: CCIL > FX-Clear > USD/INR > SPOT > Individual Trade Details. CSV header itself remains only Trade Date, Quantity, Trade Price, Trade Timestamp.
- CCIL's Forex Settlement Regulations define a Spot trade by settlement value date as the second business day after trade date. This is settlement-tenor semantics, not a CSV quantity-unit definition: https://www.ccilindia.com/documents/43866/11572213/Forex%2BSettlement%2BRegulation_effective%2BJuly%2B2024.pdf/2193ab06-3817-9b08-5019-5eb2d91247a9?t=1721302780758 .
- CCIL's 2022 Reference Rate Spot notification says matched trade details are displayed with matched spread, trade quantity and trade timestamp, and R-Spot final trade price is derived by adjusting the FBIL reference rate with the spread. This is specifically Reference Rate Spot; it is not proof that the ordinary SPOT CSV has the same price semantics. Keep SPOT and R-SPOT separate: https://www.ccilindia.com/documents/d/ccil/notificationtomembersfbilreferencerateonfxclear07oct2022-pdf .
- No public field dictionary located that explicitly defines the CSV Quantity unit/scale, Trade Price precision/side/status treatment, cancellation/reversal inclusion, or stable trade identifier. Do not infer Quantity units from the dashboard aggregate label “Volume (USD in Mio)”.

## 3. Five-file date-window and raw-integrity audit
Each file's inclusive calendar span is <=182 days, so none violates the portal's stated maximum. This does not prove the date-range inputs actually used or complete expected-session coverage.

| File | Rows | Date span | Inclusive days | Unique dates | Exact duplicate extra rows | Non-positive prices |
|---|---:|---|---:|---:|---:|---:|
| (2).csv | 158,152 | 2025-01-01–2025-04-30 | 120 | 76 | 4,626 | 801 |
| (3).csv | 180,488 | 2025-05-02–2025-10-01 | 153 | 101 | 34,324 | 322 |
| (4).csv | 79,455 | 2025-10-01–2025-12-31 | 92 | 61 | 13,586 | 0 |
| (1).csv | 132,236 | 2026-01-01–2026-06-18 | 169 | 82 | 56,308 | 0 |
| base .csv | 110,231 | 2026-06-29–2026-11-27 | 152 | 12 | 103,627 | 0 |

- Combined rows 660,562; unique captured dates 331; overall observed endpoints 2025-01-01 to 2026-11-27.
- Cross-file overlap: 2025-10-01 appears in (3) and (4), with 1,048 common exact tuples. This is an export-boundary overlap; do not count twice pending an approved transaction identity/dedup policy.
- The five windows are individually under 182 days, but date ranges leave unobserved calendar intervals: 2025-05-01, 2026-06-19–28, and other gaps inside windows. 2026 later coverage is sparse: May 5 distinct dates, Jun 3, Jul 7, Aug 1, Sep 1, Oct 0, Nov 1. No official holiday/session calendar was applied; gaps are not classified as missed trading sessions.
- Recomputed raw SHA-256 (matches C288):
  - (2) e0f97ee7167fb2ea072b35169db9ace57cc0b61339e99304f0d8d3237a76a340
  - (3) 764b33036a304a1dea55756eb4403e4af9b1272facbea93d8308287d1d4eb9c5
  - (4) 1324770bd32559d9728e455e67e1a84ef5fdcf7748b157ac99366e3375c87413
  - (1) 077306322d2ab2691209b600affadc103e0cfb1dbb718bb0e344ccbac3a5b86d
  - base 47694e2455cf5cfa74fd2bb1a5f9906bc8f79ee764e26f0391ce87b74ace2e9f

## 4. Duplicate and invalid-price diagnostics
- Exact tuple key tested: (Trade Date, Quantity, Trade Price, Trade Timestamp). Combined exact duplicate extra rows: 213,519; distinct exact tuples: 447,043; duplicated tuple groups: 58,415.
- Maximum identical tuple multiplicity is 240 in the base file; the 2026-01–06 file has a maximum multiplicity of 119. This is strong repeated-row evidence, but without a unique trade ID it does not prove which copies are export duplication versus legitimate identical trades.
- Non-positive Trade Price: 1,123 rows, all in 2025 files; 404 negative and 719 zero. File (2): 269 negative / 532 zero; file (3): 135 negative / 187 zero. No such rows in the three 2025-10 onward files.
- Quantity is positive in all rows (minimum 0.01 in first file; 500,000 in later three files); no quantity unit/scale can be accepted from numeric shape alone.
- All five files have zero null fields and all Trade Timestamp strings match HH:MM:SS shape. This is structural QA only, not trade validity or timestamp timezone proof.

## 5. Decisions / acceptance gates
| Check | Status |
|---|---|
| CCIL FX-Clear USD/INR SPOT source family | SOURCE_CONFIRMED (user screenshot + official page) |
| 182-day max-window compliance | PASS for observed file spans only |
| Raw byte integrity / SHA-256 | PASS; C288 hashes independently reproduced |
| Header/null/time-string structure | PASS, limited |
| Full date/session coverage | NOT_ESTABLISHED |
| Quantity unit and field semantics | NOT_ESTABLISHED |
| Trade identity / duplicate policy | BLOCKED |
| 1,123 non-positive price disposition | BLOCKED |
| Cancellation/reversal/status inclusion | NOT_ESTABLISHED |
| Licensing/reuse permission | NOT_ESTABLISHED |
| Daily OHLC eligibility / GCR ingestion | NOT_ADMITTED |

## 6. Next admissible action
- Request from user/authorized operator only the original export metadata or official CCIL documentation for Quantity unit, Trade Price semantics, status/cancellation inclusion, and whether repeated tuples are intentionally repeated in CSV export. No personal/member details, fee or paid access.
- If metadata remains unavailable, retain raw files and quarantine duplicate/non-positive rows; do not silently deduplicate, delete, winsorize, convert or calculate OHLC.
- To prove coverage, preserve each exact From/To date request and reconcile against official CCIL trading/session calendar. 182 days is only a maximum allowed query range, not a completeness guarantee.

## 7. Protected invariants
₹0; no paid access, external contact, terms bypass, raw-file mutation, Library duplication, synthetic data, timestamp inference, RBI/FBIL substitution, or production integration. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.
