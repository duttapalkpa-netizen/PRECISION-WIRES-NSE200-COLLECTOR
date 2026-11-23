# CDSL Official FPI Archive Retry — Continuation 62 (2026-11-23)

## Scope
Bounded retry of the official CDSL historical FPI archive after Continuation 61. No raw data ingestion, collector modification, workflow dispatch, or production change.

## Preflight / accepted work skipped
- Reused the current Master Continuity Ledger at main head `cc3e7c5c5e5051bafafa6dcdc39444dfc4e9d8c9` and the Continuation 61 evidence report.
- Skipped CDSL Continuation 77 arithmetic QA, Continuation 78 static-snapshot/freshness audit, Continuation 61 archive retry, NSE provisional CSV boundary audits (Continuations 59/60), and accepted NSE archive/QA work.
- Preserved the rule that NSE provisional exchange trading activity cannot substitute for final depository FPI.

## Fresh official-source observations
1. CDSL FPI landing page: https://www.cdslindia.com/Publications/ForeignPortInvestor.html
   - Page reports last updated 18-Nov-2026.
   - Its linked “Daily Trends in FII/FPI Investments (New Format)” list still begins at 04-Apr-2025.
   - The page separately lists fortnightly sector-wise reports through 15-Nov-2026; these are not daily FPI flows.
2. CDSL current daily confirmed-flow page: https://www.cdslindia.com/eservices/publications/fiidaily
   - Current rendered page reports 20-NOV-2026.
   - It provides category/route-level gross purchases, gross sales, net investment in INR crore, net investment in USD million and conversion rate.
   - The page says figures are compiled from custodian reports submitted to depositories and relate to trades on and up to previous trading day(s). It distinguishes these confirmed figures from provisional exchange trading-member data.
   - This is a current daily snapshot, not historical archive coverage.
3. CDSL archive route: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
   - Fresh re-open on 23-Nov-2026 returned “Error Occurred” / “Internal Error Occurred Please try after some time”, TicketNumber 439701.
   - This reproduces the same failure ticket recorded in Continuation 61. The route is not currently reproducible.
   - No raw archive response, complete date list, row count, export schema, response bytes or SHA-256 captured.
4. CDSL legacy archive link: https://www.cdslindia.com/Publications/FIITrends.aspx
   - It renders only an Archive form with a date input and a page-last-updated date of 20-May-2020; no downloadable export URL/schema was exposed in the rendered response. It is not evidence of a working current daily archive.
5. SEBI official FPI curation directory: https://www.sebi.gov.in/curation/fpi.html
   - Confirms CDSL routes for daily latest data, current month and archive; the archive link points to FIITrends.aspx. This confirms route identity, not successful historical retrieval.

## Result / acceptance
- CDSL current confirmed daily snapshot: DISCOVERED (20-Nov-2026).
- CDSL historical archive route ArchiveDataAfter2009.aspx: BLOCKED / INTERMITTENT; same internal-error ticket 439701 reproduced.
- Legacy FIITrends.aspx: interactive legacy date form; export endpoint/schema NOT VERIFIED.
- >=60 distinct daily observations spanning >=90 calendar days: NOT VERIFIED.
- Raw archive bytes, complete row-level QA and SHA-256: NOT CAPTURED.
- Final FPI historical ingestion: BLOCKED / UNKNOWN. Macro-Geo P0 remains 6/8; strict Hard Gate BLOCKED; candidate_release_allowed=false.
- No collector mapping, fixture, source-coverage code, workflow run, or production rule changed.

## Exact next action
Do not retry repeatedly while CDSL returns ticket 439701. Resume only when an approved auditable browser/session can retrieve the archive consistently and capture full raw response bytes, request metadata, all distinct reporting dates, schema, terms/usage boundary and SHA-256. Admit nothing until >=60 distinct valid dates spanning >=90 calendar days are independently verified. Keep NSE provisional activity separate; CDSL FPI is not DII.

## Invariants
₹0; official/free sources only; no synthetic data, fabricated timestamps, guessed endpoints, scraping or reverse engineering; UNKNOWN never PASS; H+3 minimum 50 fully matured observations per State; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2.0 unchanged; no merge or production integration.
