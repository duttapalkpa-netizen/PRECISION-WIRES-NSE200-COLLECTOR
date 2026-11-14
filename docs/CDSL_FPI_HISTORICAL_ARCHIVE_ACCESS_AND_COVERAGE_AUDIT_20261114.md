# CDSL FPI historical archive access and coverage audit — 2026-11-14

## Objective
Bounded audit of the official CDSL historical FPI archive surface, its date coverage, and whether raw historical bytes can be safely acquired and hashed using the currently available research tooling.

## Official source evidence
- Official CDSL archive URL: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
- Search-indexed official page snapshot retrieved 2026-11-14 states "Daily Trends in FII / FPI Investments upto 13-Nov-2026" and displays daily rows beginning 02-Nov-2026 in the visible extracted content, plus cumulative totals since November 1992. It states data is compiled from custodian reports submitted to depositories on 13-Nov-2026 and constitutes trades conducted on and up to previous trading day(s).
- Official CDSL daily page: https://www.cdslindia.com/eservices/publications/fiidaily; indexed snapshot reports 12-NOV-2026 with Equity Stock Exchange net +14,678.72 crore, Primary & Others +15.00, subtotal +14,693.72; Debt-General +445.65; Debt-VRR -173.22; Debt-FAR +1,022.81.
- CDSL archive page's indexed snapshot is not a byte-preserved CSV/Excel acquisition. It is a dynamic HTML view / search extraction and cannot serve as a historical raw archive artifact.

## Retrieval attempt and integrity outcome
- Opened official archive URL using available web retrieval on 2026-11-14. The page returned "Error Occurred.. Internal Error Occurred Please try after some time" (ticket 604935); no HTML data table or download link could be extracted in that open attempt.
- No direct-download URL, query parameters, file name, content-type, byte count, response body or HTTP status for a downloadable archive file were exposed by the evidence available in this task.
- Consequently: raw archive bytes NOT ACQUIRED; SHA-256 NOT COMPUTED; no manifest created. This is an explicit access limitation, not a zero-row result and not proof the official archive is empty.
- No guessed endpoint, fabricated CSV, reconstructed history, or copied search-result text was promoted into a raw data file.

## Coverage and methodology decision
- CDSL archive page claims cumulative totals since November 1992, but the indexed extracted daily table visible in this retrieval begins 02-Nov-2026; full daily row coverage and pagination/download contract remain UNKNOWN.
- Preserve CDSL reporting date separately from underlying trade date; the source explicitly describes previous trading day(s), not a guaranteed one-to-one date mapping.
- Preserve route/asset class separately: Equity, Debt-General, Debt-VRR, Debt-FAR, Hybrid, MF and AIF. Do not sum subtotals with components.
- CDSL custodian-submitted figures and NSE provisional trade-member figures remain separate source series. Same-day matching must be based on explicit source date semantics, not assumed T+1.
- Any date without verified raw row and publication availability remains UNKNOWN; no synthetic values or timestamps.

## Outcome
- Official archive surface existence and indexed latest date: VERIFIED.
- Latest daily CDSL arithmetic (12-Nov-2026): previously PASS in FPI/DII source semantics report.
- Full historical daily archive coverage: UNKNOWN.
- Raw historical archive acquisition / manifest / SHA-256: NOT ACQUIRED / NOT COMPUTED.
- Same-date NSE provisional vs CDSL custodian reconciliation: NOT RUN.
- Rolling FPI/DII-to-sector impact study: NOT RUN.
- Hard Gate remains BLOCKED. No production selector/ranking/CORE-672 changes, no paid services, no PR/merge.


## Alternate official route discovered: SEBI source catalog and NSDL archive UI

- SEBI's official FPI curation page explicitly lists NSDL and CDSL as parallel official sources for latest daily, current-month and archive FPI trends; it also lists yearly/monthly, fortnightly sector-wise, AUC, trade-wise and ODI/PN data routes. Source: https://www.sebi.gov.in/curation/fpi.html
- NSDL's official FPI portal report listing exposes separate FPI Archive and DII Archive links. Source: https://pilot.fpi.nsdl.co.in/Reports/ReportsListing.aspx
- Followed official NSDL FPI Archive link. The archive UI exposes a To Date field, View Report, Export to Excel and Print controls: https://pilot.fpi.nsdl.co.in/Reports/Archive.aspx . The page's static extraction does not expose a selected date, returned data rows, exported workbook bytes or request parameters; therefore no data file/hash is claimed.
- Followed official NSDL DII Archive link. It resolves to a date-entry report form, but static extraction currently shows Please Select Date / No Data Found before any date selection: https://pilot.fpi.nsdl.co.in/Users/DIIGenerateReport.aspx?Rep=A . This is not evidence that historical DII data is empty.
- CDSL remains the direct custodian source whose archive page is intermittently returning internal error. The SEBI-listed NSDL route provides an independent official path to attempt dated export without guessing a CDSL endpoint.
- Operational next step: use NSDL archive UI to choose each exact date in the required research window and Export to Excel; preserve original workbook bytes, response metadata, retrieval time and SHA-256. Do not infer dates from reporting date or use UI-exported files as if available before their actual publication timestamp.
- Status update: alternate official archive UI identified and export affordance verified; raw workbook acquisition and historical coverage remain NOT ACQUIRED / NOT VERIFIED.


## Official CDSL archive indexed snapshot re-check — 2026-11-14

### Newly surfaced dated record and arithmetic checks
- Official CDSL archive indexed snapshot now exposes a daily trends table headed “upto 13-Nov-2026”; its extracted first daily row is reporting date 02-Nov-2026. The page states the data is compiled from custodian reports submitted on 13-Nov-2026 and represents trades on and up to previous trading day(s). Do not infer that the extracted first row is the only row in the underlying archive or that the archive starts on 02-Nov; full pagination/coverage is not established. Source: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx (web evidence turn593944search2).
- 02-Nov-2026 Equity Stock Exchange gross purchases ₹21,334.02 crore less gross sales ₹17,015.12 crore = net ₹4,318.90 crore; Primary & Others net ₹138.90 crore; Equity subtotal ₹4,457.80 crore. Arithmetic PASS.
- 02-Nov-2026 Debt Stock Exchange net ₹585.95−₹1,108.13 = −₹522.18 crore; Primary & Others net −₹26.15 crore; Debt subtotal −₹548.33 crore. Arithmetic PASS.
- 02-Nov-2026 Debt-VRR subtotal net −₹238.70 crore; Debt-FAR subtotal net −₹275.99 crore; Hybrid stock-exchange net −₹9.98 crore. Preserve routes/categories; do not collapse into equity.
- The same page separately displays FPI derivative activity “upto 13-Nov-2026”, including 13-Nov-2026 INDEX_FUTURES buy amount ₹5,266.61 crore, sell amount ₹1,700.53 crore and end-date open interest ₹32,628.02 crore. This is a separate derivatives table/date semantics and must not be joined as if it were the 02-Nov cash-equity record.
- CDSL notes confirmed custodian FPI cash data can represent trades on and up to previous trading day(s); exchange provisional data is T-day trading-member PAN based. The two series remain distinct in source finality and as-of availability.

### Coverage / acquisition conclusion
- New achievement: an actual dated archive row and independent buy-minus-sell arithmetic are now visible in the official indexed archive extraction; this upgrades evidence from “archive UI only” to “at least one dated record visible”.
- Still NOT acquired: original downloadable archive/workbook bytes, response headers/content type, byte count, exact export URL, complete row set, raw SHA-256 manifest and reproducible pagination/export contract. Do not hash search-result text as if it were the source file.
- Full daily historical coverage, aligned NSE provisional-vs-CDSL custodian panel, DII historical export and rolling impact study remain UNKNOWN / NOT RUN. Hard Gate remains BLOCKED.
- Official route inventory is now explicit: SEBI lists NSDL and CDSL parallel daily/monthly/archive FPI routes (https://www.sebi.gov.in/curation/fpi.html; web evidence turn593944search0); CDSL's portal lists archive, fortnightly sector-wise, derivatives and trade-wise equity/debt datasets (web evidence turn593944search1, turn593944search6). These are acquisition leads, not proof of downloaded historical files.



## CDSL archive 2026 YTD aggregation and archive inventory audit — 2026-11-14

### Official CDSL indexed archive values
- The official archive page provides an explicit “Total for 2026” aggregation in addition to dated daily rows and cumulative totals since November 1992. As at the page's 13-Nov-2026 compilation, 2026 equity gross purchases ₹3,596,322.95 crore, gross sales ₹3,807,178.21 crore, net −₹210,855.26 crore; primary/other net +₹69,275.84 crore; equity subtotal net −₹141,579.42 crore. Arithmetic check: −210,855.26 + 69,275.84 = −141,579.42 crore. Source https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx (web evidence turn479037search0).
- 2026 Debt subtotal net +₹57,469.39 crore; Debt-VRR −₹18,196.58 crore; Debt-FAR +₹29,960.14 crore; Hybrid −₹6,715.12 crore; Mutual Fund subtotal +₹10,641.48 crore; AIF −₹3.46 crore. These remain distinct categories/routes.
- 2026 total net across displayed categories −₹137,699.41 crore. Do not describe this as equity-only flow; the total includes multiple instrument categories.
- CDSL archive also shows cumulative totals since Nov-1992 to 13-Nov-2026: Equity +₹628,696.11 crore; Debt +₹424,720.10 crore; Hybrid −₹6,836.15 crore; Debt-VRR −₹18,196.58 crore; Debt-FAR +₹29,960.14 crore; MF +₹10,641.48 crore; AIF −₹3.46 crore. Cumulative is not an investable flow window.
- CDSL's official FPI landing page exposes archive, calendar-year, financial-year, quarterly, fortnightly sector-wise, AUC, derivative, trade-wise equity/debt and ODI/PN categories. The landing page lists fortnightly sector snapshots through 15-Oct-2026 and states derivative data daily since 01-Dec-2010. Source https://www.cdslindia.com/Publications/ForeignPortInvestor.html (web evidence turn479037search2).
- Daily CDSL page shows 12-Nov-2026 equity subtotal +₹14,693.72 crore, Debt-General +₹445.65 crore, Debt-VRR −₹173.22 crore and Debt-FAR +₹1,022.81 crore; derivative tables separately dated 12-Nov. Source https://www.cdslindia.com/eservices/publications/fiidaily (web evidence turn479037search1).

### Interpretation and control
- A strongly positive single-day custodian equity observation (12-Nov) can coexist with negative 2026 YTD equity subtotal. These answer different horizons; do not let one day override the YTD regime or vice versa.
- The 2026 YTD equity subtotal is a better horizon context feature than the all-category total, but still requires a dated historical panel and as-of publication controls before backtest use.
- Do not treat CDSL archive's 2026 YTD aggregate as daily history. It cannot satisfy the raw daily archive manifest or 200+ session coverage.
- Official indexed page data is visible, but original downloadable bytes, complete daily rows, response metadata and raw SHA-256 are still NOT ACQUIRED. No search-result text was hashed.
- Scoped 2026 YTD arithmetic and archive-category inventory: DOCUMENTED / arithmetic PASS. Daily raw archive acquisition, DII historical export, exact coverage calendar, same-date NSE provisional reconciliation and rolling FPI impact study remain NOT ACQUIRED / NOT RUN. Hard Gate remains BLOCKED.


## CDSL fortnightly sector-wise FPI report — latest listed 15-Oct-2026 — ingestion audit

- Official CDSL archive inventory lists fortnightly sector-wise FPI snapshots through 15-Oct-2026; latest listed report link is 15-Oct-2026, followed by 30-Sep and 15-Sep 2026. This is the latest available dated sector snapshot visible in the source inventory, not a November update. Source https://www.cdslindia.com/Publications/ForeignPortInvestor.html (web evidence turn849696search0).
- Opened official report https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/October%2015,%202026.html . It exposes sector-level AUC as at 30-Sep-2026, net investment for 16–30 Sep and 01–15 Oct, and AUC as at 15-Oct, across Equity, Debt General, Debt VRR, Debt-FAR, Hybrid, Mutual Funds and AIF, with INR crore and USD million columns. Source web evidence turn849696search1.
- Visible row check: Automobile and Auto Components equity AUC was ₹4,98,295 crore at 30-Sep; net equity investment −₹3,542 crore for 16–30 Sep and −₹6,533 crore for 01–15 Oct; equity AUC ₹4,77,593 crore at 15-Oct. This is a sector example only; no claim that all sector rows or all report totals have been reconciled.
- The report provides a direct bridge from fortnightly sector flow to sector AUC. For Auto & Auto Components, arithmetic AUC bridge cannot be validated from this visible excerpt alone because the displayed AUC changes may include valuation/FX effects and source may have additional components; do not equate AUC delta with net flow.
- Scope improvement: verified the exact official report and the available sector/time/category dimensions; captured a concrete sector row and its two fortnightly equity net-flow observations. This is materially better than merely recording that the link exists.
- Still not acquired: original downloaded workbook/HTML bytes as an immutable local artifact, response headers/byte count, raw SHA-256 manifest, complete machine-readable sector panel, all-row arithmetic/reconciliation, and a multi-period sector flow history joined to NSE sector returns with as-of timestamps.
- No sector flow is promoted into scanner features or ranking. Historical sector panel and rolling predictive test remain NOT RUN; Macro-Geo P0 / Hard Gate remain BLOCKED. No synthetic observations, no inferred company mapping, no paid API, no production changes or PR/merge.


## CDSL 15-Oct-2026 fortnightly sector panel — full 22-sector table and total-flow audit

- Opened the complete official report text through the Grand Total and notes (web evidence turn633522view0 lines 3–63; continuation turn915067view0 lines 25–63). It contains 22 BSE Common Industry Classification sectors plus an Others bucket. It is not a direct 1:1 list of NSE sector indices.
- Grand Total Equity net investment: −₹21,745 crore for 16–30 Sep 2026 and −₹47,955 crore for 01–15 Oct 2026. Combined two-fortnight equity net flow = −₹69,700 crore (derived sum; arithmetic check).
- Sector equity net flows, 16–30 Sep / 01–15 Oct (₹ crore): Automobile & Auto Components −3,542 / −6,533; Capital Goods −1,353 / −3,886; Chemicals −133 / +41; Construction +381 / −1,224; Construction Materials −847 / −564; Consumer Durables −1,508 / −586; Consumer Services +1,911 / −1,931; Diversified +115 / +43; FMCG −972 / −8,172; Financial Services −6,943 / −8,634; Forest Materials +6 / −50; Healthcare +3 / −5,497; Information Technology −38 / +2,599; Media, Entertainment & Publication +31 / +252; Metals & Mining −2,322 / −3,693; Oil, Gas & Consumable Fuels −4,469 / −3,680; Power −570 / −1,732; Realty +19 / −578; Services +1,397 / +262; Telecommunication −2,423 / −3,928; Textiles +636 / −59; Utilities −33 / −34. Others bucket is reported separately and must not be reallocated to listed sectors.
- This panel shows material sector dispersion: Financial Services, FMCG, Auto, Telecom, Metals and Oil/Gas had notable equity outflows over the two windows; IT shifted from −₹38 crore to +₹2,599 crore; Consumer Services shifted from +₹1,911 crore to −₹1,931 crore. These are source-reported flows, not evidence of subsequent share-price performance or causality.
- Classification/coverage caveats from CDSL: BSE common industry classification used for ~4,800 issuers in 22 sectors; FPI investments outside those issuers are in “Others”. CDSL says Debt VRR included from 30-Apr-2020; Debt-FAR, MF and AIF AUC from 31-Aug-2024; net investment in those categories from 15-Sep-2024.
- INR→USD for fortnightly net investment uses period-end RBI reference rate (95.9832 for 30-Sep, 95.0691 for 15-Oct), not the daily RBI reference rate used on CDSL daily pages. Preserve currency-conversion methodology as a separate field; do not compare USD columns across daily and fortnightly products without normalization.
- No complete raw file download, response metadata, byte count or SHA-256 manifest is yet captured. Table text was extracted from official web report; do not represent it as immutable original-file acquisition.
- Full sector panel transcription and arithmetic cross-check of grand-total equity windows: DOCUMENTED. Full all-category/all-sector arithmetic reconciliation, mapping to NSE sector indices, issuer constituents, daily/fortnightly historical panel, event-time joins and rolling predictive test remain NOT RUN. No production feature/ranking changes; Hard Gate remains BLOCKED.
