# GCR India FPI — CDSL Daily Archive Raw Freshness & Arithmetic QA (Continuation 229)
**Date:** 25-Nov-2026 (Asia/Kolkata)  
**Scope:** Re-validate one already-retained official CDSL archive capture; no new source request, no production ingestion.  
**Decision:** RAW ARTIFACT / PARSER / DISPLAYED ARITHMETIC PASS; ARCHIVE FRESHNESS AND COMPLETENESS NOT PASS.

## 1. Mandatory preflight and no-repeat selection
- Re-fetched current Master Continuity & Acceptance Ledger, GCR Master Priority Queue, and 63-country Historical Task Registry.
- Reopened controlling CDSL freshness reports C39 and C68, CDSL 15-Nov sector arithmetic C74, NSDL Archive form contract C76, and CDSL daily 18-Nov full-table QA C77.
- Reused prior PASS evidence: CDSL sector 192/192 row-subtotal arithmetic, CDSL daily 18-Nov 17/17 route arithmetic + 7/7 category arithmetic, NSDL raw landing/form contract, and existing artifact integrity. None was repeated.
- Selected the still-unfinished GCR India flow-lineage subtask: parse the retained CDSL daily archive HTML, record its exact vintage and reporting semantics, and perform scoped arithmetic QA.

## 2. Exact retained source and byte integrity
- Existing GitHub Actions run: 44519322726; artifact ID: 14527092174; artifact name: `gcr-india-fpi-raw-pages-3`.
- Downloaded the retained artifact for this scoped inspection; compressed ZIP: 196,057 bytes.
- Independently recomputed ZIP SHA-256: `83048ea0bc712b6a453270f8fb5c3c6755b579857ff2ad9eb7d53c8ba1778fbd` — exact match to the previously accepted digest.
- ZIP contains 10 members; uncompressed member total 1,067,099 bytes. Existing `manifest.json` is 12,012 bytes, SHA-256 `06dce2306392d6931016894bece5758b0d21eea50a399a0aaf4a2430d334cc18`.
- CDSL archive member: `cdsl_daily_archive.html`, 73,784 bytes, SHA-256 `aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df`.
- Capture manifest records GET, HTTP 200, final URL unchanged, retrieval UTC `2026-11-19T11:57:09.076562+00:00`, Content-Type `text/html; charset=utf-8`, byte count 73,784. Requested URL: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx.

## 3. Freshness and semantic boundary — material finding
- The captured page title is “Archive Data”; its visible heading says “Daily Trends in FII / FPI Investments upto 02-Mar-2026”. The cash table's reporting date is 02-03-2026. The separate derivatives table is also dated 02-MAR-2026.
- Thus this particular HTTP-200 archive response, captured on 19-Nov-2026, exposes a 02-Mar-2026 observation — approximately 262 days before capture. This is a source-response freshness observation, not a claim that CDSL has no later records elsewhere.
- This differs from C39's 30-Sep-2026 rendered archive observation and C68's 31-Oct-2026 rendered archive observation for the same URL. The earlier C39 audit also recorded materially different HTTP-200 bodies across captures. Preserve all three source-specific snapshots; do not overwrite or infer which body is canonical.
- The archive cash table contains daily, “Total for March”, “Total for 2026”, and cumulative-since-November-1992 blocks. In this capture the March block contains only the 02-Mar observation; it is not a complete month.
- Source note: confirmed investment data are based on custodian/depository reports submitted on the reporting date and represent trades on/up to previous trading day(s). Separate note distinguishes exchange-member provisional T-day figures from custodian-confirmed data.
- Conversion note: daily RBI reference rate prevailing on trading day; if bank holiday, immediately preceding working-day rate. Preserve the supplied INR/USD values and rate; do not recompute with a different FX series.
- Cash investment and derivatives remain separate dimensions. Do not merge them.

## 4. Independent arithmetic QA on the retained HTML
- Parsed both source tables without modifying the retained raw HTML.
- Cash table: 25 numeric rows in each of the daily, “Total for March”, and “Total for 2026” blocks; gross purchases − gross sales = net investment passed 25/25 in each block (75/75 total).
- Cumulative-since-November-1992 block: gross purchases − gross sales = net investment passed 8/8 rows.
- Seven category subtotals (Equity, Debt, Debt-VRR, Debt-FAR, Hybrid, MF, AIF) sum to the published INR total exactly in each block:
  - Daily / 02-Mar: purchases 42,832.45; sales 47,426.42; net −4,593.97 INR crore.
  - March-to-date (one observed day only): same displayed totals; not a complete monthly series.
  - 2026 YTD as of 02-Mar: purchases 783,815.70; sales 779,845.47; net +3,970.23 INR crore.
- Displayed USD subtotal sums: daily and March-to-date category sums are −505.08 USDm versus published −505.09 USDm (−0.01 USDm displayed-rounding residual); 2026 YTD subtotal sum matches published +426.88 USDm. Preserve published totals; do not adjust components.
- This arithmetic PASS validates internal identities at displayed precision only. It does not validate freshness, archive completeness, provider reconciliation, or investment returns.

## 5. Reconciliation to existing GCR evidence
- C77's CDSL daily eServices table for 18-Nov-2026 remains the more recent captured CDSL daily observation; its separate 17/17 route and 7/7 category arithmetic and grand-total identity were already accepted. Not repeated here.
- C74's CDSL fortnightly sector report dated 15-Nov-2026 remains a separate period-flow/stock panel; its 192/192 sector-row subtotal arithmetic remains accepted. AUC is stock; fortnightly net investment is flow. No daily interpolation.
- NSDL Latest in the same raw capture is headed 19-Nov-2026 and has different provisional-T-day vs custodian-prior-day semantics. It is not a matched-date comparison with CDSL's 18-Nov table.
- C76 documents the NSDL Archive ASP.NET form contract, but no postback was executed and no archive rows were returned. Captured ViewState must not be replayed; a fresh interactive browser action is required.
- No NSDL/CDSL matched-date, same-scope, status-qualified reconciliation is established. NSE exchange-member provisional daily data must remain distinct from custodian/depository-confirmed data.

## 6. Acceptance matrix
| Gate | Status |
|---|---|
| Existing artifact ZIP digest reverified | PASS |
| CDSL archive raw member size/hash | PASS |
| Capture URL/status/UTC/headers/byte count | PASS |
| Cash table period/schema extraction | PASS |
| Daily / March / YTD purchase-sale-net arithmetic | PASS (75/75) |
| Cumulative block arithmetic | PASS (8/8) |
| INR category subtotal to published total | PASS (3/3 blocks) |
| Displayed USD subtotal | REVIEW (−0.01 USDm daily and March residual) |
| CDSL archive freshness | NOT PASS / CONFLICTING SNAPSHOTS |
| CDSL archive completeness | UNKNOWN / BLOCKED |
| NSDL Archive postback output | NOT_DONE |
| Matched-date NSDL/CDSL reconciliation | NOT_DONE |
| Sector TRI mapping / synchronized India-global panel | BLOCKED / NOT_DONE |
| Relative-attraction formula / event study / rolling OOS | NOT_DONE / NOT_AUTHORIZED |
| Production / weights / trading admission | NOT_AUTHORIZED |

## 7. Next exact action and stop rule
- CDSL raw archive parsing and arithmetic subtask is complete. Do not repeat this artifact/hash or the arithmetic checks.
- Next dependency is a fresh-state NSDL Archive interactive public date selection and one View Report postback, followed by response byte/header/UTC/hash capture and schema/status/date inspection. Existing C76 form contract is sufficient; do not replay stale ViewState or guess a POST body.
- If a supported interactive browser is unavailable, keep NSDL archive NOT_DONE and do not fabricate matched-date results. Do not substitute the stale 02-Mar CDSL archive response or 18-Nov CDSL daily page for an NSDL matched-date output.
- After a valid NSDL response exists, compare only same reporting/trade date, same asset scope and same confirmed/provisional status. Otherwise provider variance remains NOT_COMPUTABLE.

## 8. Protected invariants
₹0; official/free sources only; no synthetic/interpolated rows, no AUC/flow mixing, no daily/fortnightly conflation, no inferred date matching, no guessed sign/FX conversion, no external contact. No IMF re-query/cohort rebuild, no macro weights or aggregate admission. Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.
