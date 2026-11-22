# Macro-Geo Official Export and Terms Boundary — Continuation 57 (23-Nov-2026)

## Preflight and prior PASS work skipped
- Re-read Mother File Continuation 56, current GitHub Master Continuity Ledger, and `docs/MACRO_GEO_OFFICIAL_SOURCE_ROUTE_ADJUDICATION_20261122.md`.
- Skipped accepted NSE 200-session acquisition/provenance/QA, canonical panel, archive schema regression, FPI/DII fail-closed test, and Run #45050554515 artifact/source-coverage acceptance. No data re-download or repeat audit.
- Current P0 acceptance remains 6/8, Hard Gate BLOCKED, `candidate_release_allowed=false`.

## RBI / FBIL USD-INR route reinspection
1. RBI Reference Rate Archive remains an official interactive form with currency choice, from/to date inputs and an Excel control. The web-rendered form exposes no action URL or export request metadata; the Excel icon click resolves only to a GIF. No request was submitted and no raw workbook was obtained. Source: https://www.rbi.org.in/Scripts/ReferenceRateArchive.aspx
2. RBI page notes FBIL assumed computation/publication of USD/INR and other major currency reference rates from 10-Jul-2018; RBI's own archive should not be assumed to contain the post-takeover benchmark history. Source: https://www.rbi.org.in/Scripts/BS_DisplayReferenceRate.aspx
3. FBIL public page currently renders an INR/1 USD daily rate table, but search-rendered entries visible in this inspection were 05-Nov-2026 and 06-Nov-2026; page's client-rendered structure does not expose a verified historical export endpoint, full daily archive or raw bytes. Source: https://www.fbil.org.in/
4. FBIL methodology says USD/INR benchmark is based on actual spot transactions in an electronic-platform window, normally 11:30–12:30 Mumbai time. It is a benchmark and must not be represented as interbank OHLC, DXY or cross-currency carry. Source: https://www.fbil.org.in/uploads/Methodology_Document_on_Reference_Rate_Dated_11th_June2018_Version1_6db1a143aa.pdf

**Status:** source identity CONFIRMED; recent public rate table DISCOVERED; full historical export URL/schema NOT VERIFIED; raw daily archive NOT CAPTURED; USD/INR P0 remains BLOCKED/UNKNOWN.

## NSDL FPI / DII: official routes and terms boundary
1. SEBI's official FPI curation page confirms NSDL and CDSL latest, current-month and archive links for FPI investments: https://www.sebi.gov.in/curation/fpi.html
2. NSDL official navigation lists distinct FPI archive and DII archive routes. FPI archive page renders date input and Export to Excel control; DII archive route requires a date and returns “No Data Found” when no date is supplied.
3. The NSDL archive page's own Terms & Conditions / disclaimer states that proprietary rights in the information remain with NSDL and “reproduction, redistribution and transmission” of website information are prohibited. It also prohibits reverse engineering of NSDL software. Source: https://pilot.fpi.nsdl.co.in/Reports/Archive.aspx (Terms lines are visible on page).
4. Therefore no automated scraper, reverse-engineering of ASP.NET postback, bulk archival, or copying of NSDL data into GitHub should be attempted under this project without explicit permission/licence. A public page's visibility does not imply redistribution rights. The report route can be documented as discovered, but raw data capture/storage is NOT AUTHORIZED on the evidence presently available.
5. NSDL DII latest report describes provisional exchange trading-member data versus custodian-confirmed DII trades and warns that Mutual Funds/AIFs can appear in both investor and investment categories; totals cannot simply be summed. Source: https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=L
6. NSDL DII archive date form shows no data without date. No daily raw workbook or historical coverage was captured.

**Status:** FPI and DII route DISCOVERED; NSDL raw data archival NOT AUTHORIZED absent permission/terms clarification; series remain BLOCKED/UNKNOWN. No scraper implementation.

## CDSL FPI and NSE provisional alternative
1. CDSL official FPI page lists daily/current-month/archive navigation and shows page last updated 18-Nov-2026: https://www.cdslindia.com/Publications/ForeignPortInvestor.html
2. Its visible daily trends section enumerates dates only through 04-Apr-2025 in the extracted page. Daily and monthly CDSL data routes redirected to an internal error in this inspection; archive route opens an interactive form with 1999–present / 1992–1998 choice and date input, but no raw export URL or workbook was exposed.
3. CDSL daily FPI series is investment activity, not DII history. It cannot be substituted for DII.
4. NSE official FII/FPI & DII page exposes downloadable CSV tables for NSE-only and combined NSE/BSE/MSEI capital-market trading activity. It explicitly labels FII/FPI data provisional and subject to custodian confirmation, and directs users to NSDL/CDSL for final FPI data: https://www.nseindia.com/reports/fii-dii
5. NSE's historical reports page has a historical FII/FPI & DII landing route but the rendered page only links to the report; no date-bounded archive download was surfaced in this inspection: https://betanseapi.nseindia.com/static/all-reports/historical-equities-fii-fpi-dii-trading-activity

**Potential fallback:** if its actual public CSV download and terms are verified, NSE provisional exchange activity may be admitted only as a separately named provisional trading-activity series, never as final FPI investment flows. It does not close the final depository FPI gate.

## Decision and exact next actions
- Do not change collector mapping or source coverage code: no acceptable raw daily files were captured and NSDL terms restrict reproduction/redistribution.
- Keep USD/INR, final FPI and DII P0 groups BLOCKED/UNKNOWN. Do not lower the >=60 distinct dates / >=90 calendar-day rule.
- Next best compliant path:
  1. Inspect FBIL for a public historical daily download/archive link and terms, or a public documented API; if none, keep blocked.
  2. Obtain written permission/licence for NSDL FPI/DII data archival or use an official source whose terms expressly permit machine retrieval and internal archival. No reverse engineering or bulk capture.
  3. Inspect NSE CSV endpoint and terms; if usable, store as provisional exchange activity in a separate table, not final FPI/DII. Verify >=60 dates and >=90 days before any coverage claim.
  4. Revisit CDSL daily/archive when official page is functioning and confirm terms before capture.
  5. Only after permitted raw capture, write collector mapping and fixture tests; then rerun source coverage, event study and hard gate.
- No synthetic/proxy substitution, no paid API, no credentials bypass, no production changes. ₹0; UNKNOWN never PASS; H+3 threshold >=50 matured observations; production selector/ranking/pressure-fade/CORE-672/Engines A–E/IPO-PLX unchanged.
