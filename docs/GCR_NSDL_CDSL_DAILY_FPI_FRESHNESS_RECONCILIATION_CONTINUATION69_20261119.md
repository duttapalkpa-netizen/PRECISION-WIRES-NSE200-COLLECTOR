# GCR NSDL/CDSL Freshness Reconciliation + Brazil Next-Gate — Continuation 69
Date: 2026-11-19 (Asia/Kolkata)
Research-only. No production changes or factor admission.

## Decision
The highest-value next action was official daily FPI source freshness verification. This pass found an important source-rendering discrepancy: SEBI confirms the official NSDL Latest/Monthly/Archive/Fortnightly routes, but direct fetch of the three NSDL report endpoints returned HTTP 502 in this environment. CDSL's archive search-index snapshot says daily investment through 18-Nov-2026, while a direct open of the same official archive page renders a heading through 31-Oct-2026 and October rows. These two views conflict; neither is sufficient to certify current daily data until raw HTML/response bytes and source headers are captured independently.
No daily flow series is promoted in this pass.

## Official source-route verification
SEBI official curation directory:
https://www.sebi.gov.in/curation/fpi.html
It explicitly lists:
- NSDL Latest: https://www.fpi.nsdl.co.in/web/Reports/Latest.aspx
- NSDL Current Month: https://www.fpi.nsdl.co.in/web/Reports/Monthly.aspx
- NSDL Archive: https://www.fpi.nsdl.co.in/web/Reports/Archive.aspx
- NSDL fortnightly sector selector: https://www.fpi.nsdl.co.in/web/Reports/FPI_Fortnightly_Selection.aspx
- CDSL corresponding daily/monthly/archive and fortnightly sector pages.
This is route-discovery PASS, not data-capture PASS.

## NSDL direct endpoint access results
Direct web fetches attempted for:
1. Latest.aspx
2. Archive.aspx
3. FPI_Fortnightly_Selection.aspx
All three returned HTTP 502 Bad Gateway in this retrieval environment. This does not establish NSDL service outage or data absence. Do not interpret 502 as no observations. A GitHub Actions runner or other direct HTTP client may be able to retrieve the public ASP.NET pages; preserve exact request/response and form state if used.
A public third-party scraper's README documents that NSDL daily FPI archive pages are ASP.NET postback pages and that FPI archive queries are month-scoped while DII daily queries require one request per trading day. This is implementation discovery only, not accepted source evidence or code to vendor blindly. Third-party repo: https://github.com/BAC-Brindco/nsdl-fpi.

## CDSL archive discrepancy
Official page:
https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
- Search-indexed snapshot (crawled today) states “Daily Trends in FII/FPI Investments upto 18-Nov-2026” and derivatives through 18-Nov-2026.
- Direct open snapshot of the same URL renders “Daily Trends in FII/FPI Investments upto 31-Oct-2026” and October daily rows.
- The two source representations are inconsistent in the retrieved evidence. Search snippets may be fresher than direct page extraction, but without exact raw bytes, retrieval time, headers and HTML hash the 18-Nov heading is NOT independently captured.
- Earlier Continuation 68 conclusion that daily investment freshness was only through 31-Oct is now qualified: it reflects direct page rendering, not necessarily current server state. Conversely the 18-Nov search-index text is not yet raw evidence. Status: freshness CONFLICT / UNKNOWN pending raw capture.
- Derivatives latest date 18-Nov cannot be used as proof of cash investment table latest date.

## Data interpretation contract retained
- Keep Equity, Debt, Debt-VRR, Debt-FAR, Hybrid, MF and AIF separate.
- Keep Stock Exchange vs Primary Market & Others separate.
- Preserve gross purchases, gross sales, net INR crore, net USD million, and source-provided RBI conversion rate; do not silently re-convert.
- Preserve reporting date separately from underlying trade date and retrieval timestamp.
- AUC is a stock/position; period net investment is a flow.
- NSDL/CDSL depository-confirmed flows and NSE provisional exchange flows are separate series; reconcile only matched date/scope/asset class, and preserve revision status.
- Do not daily-interpolate fortnightly sector allocations.

## Brazil status — no repeated probes
- Completed: exact Brazil Registration URN 40-event lifecycle and transaction index cross-check, documented in `docs/IMF_BRAZIL_REGISTRATION_HISTORY_PART7_20261119.md`.
- Remaining: PA transaction ID 2 / dated Changelog payload. Previously tested documented fusion-json and sdmx-json both returned HTTP 500; do not repeat.
- Remaining: PA reference Dataflow `IMF:BOP6(1.0)` vs BCB payload `IMF:BOP_BPM6(1.0)` identity mismatch, compatibility counts 234/237 vs 27/237. No rewrite or alias.
- Next Brazil evidence path remains official interactive PA details UI: select exact `IMF:BR_BOP_BP6(1.0)`, inspect Changelog/Revisions/Compare/Export and download actual returned rows. If access is owner-authenticated, record as external dependency; no credentials requested and no guessed endpoint.

## Acceptance state
- SEBI official NSDL/CDSL route directory: PASS.
- NSDL report endpoint direct retrieval in this environment: BLOCKED (HTTP 502); data absence NOT inferred.
- CDSL current daily investment freshness: CONFLICT / UNKNOWN (search-index snapshot through 18-Nov vs direct rendered page through 31-Oct).
- Raw daily FPI immutable capture, schema parser, date coverage, SHA-256 and NSE/depository reconciliation: NOT_DONE.
- Brazil Registration lifecycle: PASS (completed).
- Brazil PA tx2/Changelog: BLOCKED.
- Brazil BOP6/BOP_BPM6 identity reconciliation: BLOCKED.
- GCR/Brazil production admission: NOT_AUTHORIZED.

## Exact next steps
1. Use a short GitHub Actions direct-HTTP capture of the four NSDL official pages (Latest, Monthly, Archive, Fortnightly selector) and CDSL archive/sector page. Preserve response status, headers, retrieval UTC, raw HTML bytes, SHA-256 and any ASP.NET form fields. Do not parse until raw bytes are secured.
2. If NSDL archive is a postback workflow, inspect actual page form names, hidden ViewState/EventValidation and available date controls from captured HTML; submit only documented public form state, one month/request for FPI and one trading date/request for DII as needed. Never infer dates or fabricate rows.
3. Parse into source-specific normalized tables only after schema is observed; keep raw source row, source URL, report date, retrieval timestamp, asset class, route, gross/net and currency.
4. Reconcile same-date NSDL/CDSL depository-confirmed vs NSE provisional data, retaining differences/revisions.
5. Brazil: owner-side UI/export of PA changelog; if unavailable without owner interaction, keep BLOCKED and continue other independently closable GCR factors.
No paid API, no external contact, no production selector/score/pressure-fade/CORE-672/engine changes. UNKNOWN is not PASS.
