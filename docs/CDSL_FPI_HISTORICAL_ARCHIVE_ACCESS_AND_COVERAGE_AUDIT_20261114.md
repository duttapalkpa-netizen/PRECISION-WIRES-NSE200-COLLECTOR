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

