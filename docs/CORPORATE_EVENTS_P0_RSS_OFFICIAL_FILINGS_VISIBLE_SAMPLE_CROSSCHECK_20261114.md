# Corporate Events P0 — RSS to Official Filings Cross-check (Visible NSE Page Sample)
Date: 2026-11-14
Evidence inputs: immutable RSS artifacts from runs 43489286657 and 43490004265; official NSE Corporate Filings page snapshot retrieved 2026-11-14.

## Official page contract and visible snapshot
Official page: https://www.nseindia.com/companies-listing/corporate-filings-application
The NSE page shows 7 Corporate Announcements and a latest-announcements sample with fields Symbol, Subject, Broadcast Date. Five visible rows:
- YATRA — Investor Presentation — 13-Nov-2026
- GICHSGFIN — Updates — 13-Nov-2026
- TARSONS — Analysts/Institutional Investor Meet/Con. Call Update — 13-Nov-2026
- ONIDA — Credit Rating- Revision — 13-Nov-2026
- RUBYMILLS — Change in Management — 13-Nov-2026
The same page keeps Corporate Actions (Purpose, Ex-Date) and Board Meetings (Purpose, Meeting Date) in separate tables. These dates must not be treated as announcement publication timestamps.

## RSS snapshot input
Two independently retrieved raw RSS artifacts were previously verified:
- Run #1 43489286657, raw XML SHA-256 `21de2c9b2d1f39cad81600cdca22556e813d2854eeee28d5082c913ec95aa1a4`.
- Run #2 43490004265, raw XML SHA-256 `ee92888d16048899cffe4da9f57a6c246a7d4db2e133822e223e0674722bdaf0`.
Both contain the same 13 parsed items. RSS fields contain issuer/company title, link, free-text description (including subject label), original pubDate string. No GUID and no explicit symbol/ISIN fields.

## Visible-sample comparison
The 13 RSS company titles are:
1. Religare Enterprises Limited (3 items)
2. Fusion CX Limited (3 items)
3. Kothari Petrochemicals Limited (2 items)
4. Viaz Tyres Limited (1 item)
5. Transteel Seating Technologies Limited (2 items)
6. Optivalue Tek Consulting Limited (1 item)
7. Senco Gold Limited (1 item)

None of these seven issuer names exactly matches the five company symbols/names visible in the official page's latest-announcements sample. This is a non-overlap against a five-row visible sample only. It is NOT a failed event match: the official page summary says 7 announcements and the visible page sample is limited; it does not expose all 13 corresponding rows in this retrieved rendering. RSS publication times are 14-Nov 00:00–00:35 without timezone suffix, while official page rows show Broadcast Date only (13-Nov). Date-only page values and timezone-naive RSS strings cannot safely be equated or ordered.

## Matchability and constraints
- Exact symbol-level matching: NOT POSSIBLE from RSS fields alone; no symbol/ISIN/GUID present.
- Subject-level matching: RSS description contains a subject label after `|SUBJECT:`, but the official sample has no rows for these issuers, so no exact pairwise validation can be made.
- Link-level matching: official page sample does not expose attachment links for the five rows in the search-rendered snapshot; no exact URL pair exists in this evidence.
- No symbol was inferred from attachment filename prefixes or issuer names.
- Do not compare RSS items to Corporate Actions or Board Meetings tables; their semantics differ.
- NSE's disclaimer says company-uploaded disclosures are displayed without the Exchange verifying adequacy, accuracy or veracity. Treat issuer source content as submitted disclosure, not exchange-certified truth.

## Decision
| Check | Result |
|---|---|
| RSS 13-item replay equality | PASS (prior audit) |
| Official page schema observed | PASS |
| Announcement/action/meeting date semantics kept separate | PASS |
| Name-level overlap with five visible official rows | 0/5 — LIMITED SAMPLE ONLY |
| Full 13-item official announcement reconciliation | NOT POSSIBLE FROM VISIBLE SAMPLE |
| Exact symbol/ISIN mapping | UNKNOWN |
| Exact attachment URL cross-check | NOT RUN |
| Corporate Events P0 | BLOCKED |

## Next required evidence
Obtain the complete official NSE announcement rows for the exact RSS publication window using an official page-linked request captured from the page's own browser/network behavior, or a direct official NSE source with documented request shape. Do not adopt query parameters from third-party articles as official contract. Preserve exact requested URL, final URL, response bytes/hash and source schema. Then join only on source-provided symbol/attachment URL or exact dated official master evidence.

No code/workflow change, no synthetic values, no guessed symbol, no paid source, no PR/merge, no production integration. Protected selector/ranking/CORE-672 invariants unchanged.
