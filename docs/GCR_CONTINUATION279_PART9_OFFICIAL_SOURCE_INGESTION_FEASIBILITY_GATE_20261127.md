# GCR Continuation 279 — Part-9 source-ingestion feasibility gate (27-Nov-2026)
Date: 2026-11-27 (Asia/Kolkata)

## 1. Preflight / duplicate prevention
Re-read current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, C278 report, Failure Lessons Register, Library Mother File (continuations 55–57 and source-route adjudication) and existing official-source report. C273 matrix QA, C274 schema fix, C278 regression execution, NSE raw archive QA, canonical panel rebuild and export Phases 4–6 were not repeated. No duplicate Library upload.

## 2. Part-9 objective
Resolve whether the two outstanding Macro-Geo P0 source groups can be admitted under the project's strict rules: official/free sources, zero spend, no credential bypass, no third-party proxy, no fabricated observations, and no redistribution contrary to publisher terms.

## 3. USD/INR — official route status
- RBI Reference Rate Archive page was freshly inspected: https://www.rbi.org.in/scripts/ReferenceRateArchive.aspx
- Page exposes currency selection including USD, From/To date inputs, and an Excel download control. This confirms an official interactive archive/export surface.
- The inspection did not capture the actual form submission request, response workbook bytes, schema, retrieval timestamp, or SHA-256. Therefore endpoint/export execution and raw capture remain NOT_VERIFIED.
- RBI's official explanation states FBIL assumed computation/publication of USD/INR and other reference rates from 10-Jul-2018, after which RBI discontinued its own publication. FBIL's public page shows recent reference-rate rows, but this task did not obtain an auditable historical raw export. IMF metadata describes the daily FBIL benchmark methodology (actual spot transactions in a 11:30–12:30 IST window, published around 13:30 on Mumbai business days); this is benchmark context, not an OHLC series.
- Classification boundary: FBIL/RBI reference rate is a daily benchmark and must not be relabelled interbank OHLC, DXY or carry. No third-party compiled CSV/dataset promoted.
- Status: official source identity CONFIRMED; export control DISCOVERED; request/schema/raw bytes NOT_CAPTURED; USD/INR remains BLOCKED / UNKNOWN.

## 4. FPI/DII — official route and terms boundary
- NSDL official FPI Investments listing confirms distinct routes for FPI Archive and DII Archive: https://pilot.fpi.nsdl.co.in/Reports/ReportsListing.aspx
- The same official page's terms/disclaimer state that proprietary rights in information remain with NSDL and reproduction, redistribution and transmission of information on the site are strictly prohibited.
- No permission or explicit license authorizing automated archival/reuse was found in the inspected page. No credential bypass, terms circumvention, or external contact was attempted.
- Therefore NSDL data must not be downloaded into the research archive or automatically ingested for this workflow unless applicable written terms/permission clearly authorize the intended use. This is a lawful-use gate, not a technical workaround task.
- Keep FPI investment data separate from provisional exchange FPI/FII-DII trading activity. NSE exchange data cannot be silently substituted for final depository FPI/DII flows. CDSL FPI investment data is not DII history.
- Status: NSDL routes DISCOVERED; reuse permission NOT_ESTABLISHED; raw archive NOT_CAPTURED; FPI/DII remains BLOCKED / UNKNOWN.

## 5. Research impact / accepted progress
- C278 isolated archive-contract regression remains PASS and closed.
- This C279 task yields a new source-governance decision and narrows the blocker: RBI archive export execution is the next technical capture task; NSDL FPI/DII is gated by reuse permission/terms, not simply a missing URL.
- No raw USD/INR or FPI/DII rows were added; Macro-Geo P0 remains 6/8 (last artifact-backed inventory); strict GCR hard gate BLOCKED; candidate_release_allowed=false; overall GCR NOT_COMPUTABLE / NOT_CERTIFIED.
- No claim of improved numerical coverage or GCR predictive performance.

## 6. Next actionable task
1. Use an auditable browser session to submit the RBI official USD date-range Excel form, capture the exact request/response, raw workbook, schema, date range, retrieval time, row-level QA and SHA-256. If the form cannot be submitted or export cannot be retrieved, retain BLOCKED.
2. For FPI/DII, do not ingest NSDL archive unless a clearly applicable reuse permission/terms basis is available without external contact or credential bypass. Otherwise mark this source path NOT_ADMISSIBLE for automated archival and investigate a distinct official source with compatible reuse terms; preserve separate FPI and DII definitions and the >=60 distinct dates / >=90 calendar days gate.
3. Any workflow execution must be separately bounded to <=10 minutes and audit-only. No NSE raw re-acquisition, IMF re-query, cohort rebuild, paid source, synthetic rows, production changes or merge.

## 7. Protected invariants
₹0 spend; official/free sources only; UNKNOWN is neither PASS nor FAIL; no guessed IDs/timestamps, interpolation, forward-fill, proxy promotion, or external contact. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged.
