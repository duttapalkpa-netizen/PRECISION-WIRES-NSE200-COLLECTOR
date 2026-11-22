# Macro-Geo Official Source Route Adjudication — 2026-11-22

## Purpose
Record the official-source route discovery for the two missing Macro-Geo P0 groups (USD/INR and FPI/DII). This is a source-discovery and schema-boundary note, not raw-data acceptance. No production selector, ranking, pressure-fade, CORE-672, engine or IPO code is changed.

## Preflight / prior PASS work skipped
- Re-read Mother File Continuation 55, current Master Continuity Ledger and failure lessons.
- Skipped verified Run #398 200-session NSE raw archive, acquisition QA/provenance, canonical panel rebuild, archive schema regression and FPI/DII inventory fail-closed regression.
- Latest confirmed Macro-Geo run remains #45050554515; artifact #14765264055; ZIP SHA-256 `972db66a147c7b67b3a81e24bbfb98eae8a3b23c4f046dea9650e195f7b67703`. Strict hard gate BLOCKED; candidate_release_allowed=false.

## Finding A — USD/INR reference rate
1. RBI Reference Rate Archive is an official RBI page with currency selector (USD/GBP/EUR/JPY etc.), from/to date inputs and an Excel export control:
   https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx
2. RBI explicitly records that FBIL took over computation/publication of USD/INR and other major-currency reference rates from 10 July 2018; RBI discontinued its own publication from that date:
   https://www.rbi.org.in/Scripts/BS_DisplayReferenceRate.aspx
   https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=44393
3. RBI archive page is an interactive form. Rendered-page inspection identifies the Excel control but does not expose a verified export request URL, parameter schema or downloadable raw workbook. The icon target resolves to a GIF, not the export endpoint.
4. FBIL official homepage:
   https://www.fbil.org.in/
   Current page is a client-rendered shell with no extractable data lines in this inspection. No verified historical download/API endpoint or raw file was captured.
5. Semantic boundary: FBIL USD/INR reference rate is a benchmark, not interbank OHLC. Do not map it to OHLC, DXY, or cross-currency carry. Store benchmark name, observation date, published rate, units, publication/retrieval timestamp and raw source bytes/hash separately.

**Status:** official source identity DISCOVERED; historical export endpoint NOT VERIFIED; raw observations NOT CAPTURED; coverage UNKNOWN/BLOCKED. Do not mark P0 available.

## Finding B — NSDL official FPI and DII routes are distinct
NSDL's FPI Investments navigation exposes:
- FPI Latest: https://pilot.fpi.nsdl.co.in/Reports/Latest.aspx
- FPI Archive: https://pilot.fpi.nsdl.co.in/Reports/Archive.aspx
- DII Latest report route: https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=L
- DII Archive route: https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=A

The NSDL navigation explicitly lists separate Archive (FPI Investments) and Archive DII links. The archive screen shows a date input and Export to Excel control. The DII archive route is a date-driven report; a date-free request displayed “No Data Found”. The DII latest route returned a report for 16-Apr-2026 in this web inspection, with a conversion rate and category/instrument/route-level gross purchases, gross sales and net investment. This demonstrates a separate DII report route, not historical completeness.

Official source page:
https://pilot.fpi.nsdl.co.in/Reports/ReportsListing.aspx

**Important limitation:** the current NSDL report pages are dynamically rendered. This inspection did not recover the export POST/GET request, raw workbook, complete date range, or a >=60-date/90-day daily archive. NSDL's page footer reports a legacy 05-Oct-2020 update stamp; treat UI freshness and archive availability as requiring direct download verification.

**Status:** FPI archive route DISCOVERED; DII archive route DISCOVERED; daily export endpoint/schema and raw data NOT VERIFIED; historical coverage UNKNOWN/BLOCKED. Keep FPI and DII as separate series, preserving their definitions and units.

## Finding C — CDSL and NSE classification
- CDSL official FPI page provides Daily Trends in FII/FPI Investments and an Archive navigation:
  https://www.cdslindia.com/Publications/ForeignPortInvestor.html
- CDSL daily trend page reports FPI gross purchases, gross sales, net investment, USD million and conversion rate; it describes FPI investment activity including stock-exchange and primary-market/other activity. This is not DII history:
  https://www.cdslindia.com/eservices/publications/fiidaily
- CDSL archive route was identified but direct open returned an internal server error during this inspection. No raw archive file was downloaded.
- NSE official FII/FPI & DII page provides downloadable CSV tables for NSE-exclusive and combined NSE/BSE/MSEI trading activity. NSE explicitly says the FII/FPI data are provisional and subject to custodial confirmation, and directs users to NSDL/CDSL for final FPI data:
  https://www.nseindia.com/reports/fii-dii
- Therefore maintain separate fields/series for (a) final depository FPI investment flow, (b) final NSDL DII report if archive is retrievable, and (c) provisional exchange FII/FPI-DII trading activity. Never merge or substitute these without an explicit definition-level decision.

## Required ingestion acceptance contract
For each series independently:
1. Capture exact official raw URL and request parameters; retain raw bytes immutable.
2. Record retrieval timestamp (UTC and IST), report/observation date, publisher/revision date if supplied, HTTP status, content type, byte count and SHA-256.
3. Verify schema, units, category, sign convention, gross purchase/sale/net arithmetic, date uniqueness and source identity.
4. Require at least 60 distinct valid daily dates spanning at least 90 calendar days for each required daily flow series. If the official archive cannot supply this, report BLOCKED/UNKNOWN; do not fill from monthly totals or proxies.
5. Keep FPI investment flows separate from exchange trading activity; keep DII as its own category/report.
6. Only after raw-file acceptance should collector mapping and source-coverage code be changed. Add a bounded fixture test before enabling ingestion.
7. Rerun source coverage/event study/strict hard gate only after both missing P0 groups are actually satisfied. Release requires hard_gate_report status PASS, blockers [], candidate_release_allowed=true.

## Exact next action
Use an auditable browser/session inspection (no credential bypass) to submit RBI date-range Excel export and NSDL FPI/DII date/archive forms; capture actual request URLs, raw response bytes and schemas. If the official endpoints are inaccessible or the NSDL redistribution terms restrict automated archival, retain BLOCKED and document the limitation. No third-party mirror, paid API, synthetic data, inferred timestamps or production changes.

## Constraints
₹0; official/free sources only; no paid APIs; no fabricated timestamps or synthetic rows; UNKNOWN never PASS; H+3 State threshold >=50 fully matured observations; no production selector/ranking/pressure-fade/CORE-672/Engines A–E/IPO-PLX changes; no merge or production integration.
