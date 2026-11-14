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
