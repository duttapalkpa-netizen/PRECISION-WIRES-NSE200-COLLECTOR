# CDSL Official FPI Archive Recheck — Continuation 61 (2026-11-23)

## Scope
Recheck the official CDSL daily FPI archive after the prior Continuation 78 static-snapshot audit. This is a bounded route-availability and freshness check only. It does not repeat prior CDSL arithmetic/schema work, does not ingest data, and does not use NSE provisional trading activity as a substitute for final depository FPI.

## Preflight / completed work skipped
- Re-read the current Master Continuity Ledger and the latest Mother File continuity record available in Library.
- Skipped CDSL Continuation 77 daily-table arithmetic QA and Continuation 78 static-snapshot/freshness audit; those are already recorded.
- Skipped the NSE provisional CSV scope/usage-boundary audit (Continuations 59/60); its classification remains separate from final FPI.
- No workflow dispatch, collector change, production integration, or raw-data acquisition was performed.

## Current official CDSL observations
1. CDSL FPI landing page: https://www.cdslindia.com/Publications/ForeignPortInvestor.html
   - Current rendered page reports last updated 18-Nov-2026.
   - Its “Daily Trends in FII/FPI Investments (New Format)” linked daily list still begins at 04-Apr-2025 and proceeds backwards; this list does not expose daily links for the latest November 2026 dates.
   - It separately lists fortnightly sector-wise reports through 15-Nov-2026. These are fortnightly sector reports, not daily flow observations.
2. CDSL current daily page: https://www.cdslindia.com/eservices/publications/fiidaily
   - Current indexed/rendered daily table is dated 20-Nov-2026.
   - It reports confirmed custodian/depository submissions, with category, route, gross purchases, gross sales, net investment, USD million and conversion rate. The page states these represent trades on and up to previous trading day(s).
   - This is a current daily snapshot, not proof of a retrievable historical archive or >=60 distinct dates spanning >=90 calendar days.
3. CDSL archive route: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
   - One live web retrieval returned a page heading “Daily Trends in FII / FPI Investment & Derivatives upto 23-Nov-2026”; the visible first daily record began 02-11-2026.
   - Subsequent requests to the same official URL returned “Internal Error Occurred Please try after some time” (ticket 439701). Thus the first rendered response was not reproducibly re-opened or fully validated.
   - No raw response bytes, complete row count, date-range controls, export schema, or SHA-256 were captured in this check. Do not infer full historical coverage from the heading or HTTP success alone.

## Source boundary
- CDSL confirmed FPI investment data remain distinct from NSE exchange provisional FII/FPI-DII trading activity.
- NSE's provisional exchange data cannot replace final depository FPI. NSDL remains a separate official candidate but prior terms review found archival/reproduction restrictions; no NSDL scraping or reverse engineering is authorized absent explicit permission.
- CDSL FPI series is not DII history.

## Result / acceptance
- CDSL current daily confirmed-flow page: CURRENT SNAPSHOT DISCOVERED.
- CDSL landing page daily-link list: stale relative to current daily page (latest linked date shown 04-Apr-2025).
- CDSL archive route: INTERMITTENT / NOT REPRODUCIBLE in this check.
- Archive completeness, >=60 distinct daily dates / >=90 calendar days, raw bytes, row-level QA and SHA-256: NOT VERIFIED.
- Final FPI historical ingestion: BLOCKED / UNKNOWN. Macro-Geo P0 remains 6/8; strict Hard Gate remains BLOCKED; candidate_release_allowed=false.
- No collector/fixture changes, no source-coverage rerun, no event-study or hard-gate rerun, no production changes.

## Exact next action
Use an approved, auditable browser/session to retry the official CDSL archive only when the route responds consistently; capture the complete raw response, exact URL/request metadata, all distinct reporting dates, schema, byte count and SHA-256. Stop if the official route remains unstable. Admit no data until terms/permission and the >=60-date / >=90-day gate are satisfied. Keep NSE provisional exchange activity separate.

## Invariants
₹0; official/free sources only; no paid APIs, scraping, reverse engineering, guessed endpoints, synthetic data, fabricated timestamps, or proxy substitution; UNKNOWN never PASS; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2.0 unchanged; no merge or production integration.
