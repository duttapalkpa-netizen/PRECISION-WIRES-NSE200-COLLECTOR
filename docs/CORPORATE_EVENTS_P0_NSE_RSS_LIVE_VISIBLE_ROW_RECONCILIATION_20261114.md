# Corporate Events P0 — Official NSE Live Visible-Row Reconciliation & Endpoint Discovery Boundary
Date: 2026-11-14
Branch: `research/corporate-events-rss-collector-v1-20261114`

## Evidence inspected
1. Official NSE Corporate Filings page: https://www.nseindia.com/companies-listing/corporate-filings-application
   - Web retrieval reference: `turn460765view0`, retrieved 2026-11-14.
   - Page displayed 9 Corporate Announcements; Latest Announcements table exposed five rows with Symbol, Subject, Broadcast Date.
   - Five visible rows:
     - RELIGARE — Analyst/Investor Meet Para A-XBRL — 14-Nov-2026
     - FUSIONCX — Dividend — 14-Nov-2026
     - RELIGARE — Analysts/Institutional Investor Meet/Con. Call Update — 14-Nov-2026
     - FUSIONCX — Record Date — 14-Nov-2026
     - RELIGARE — Monitoring Agency Report — 14-Nov-2026
   - Clicking the official page's RELIGARE and FUSIONCX symbol links resolved to NSE quote pages whose canonical paths identify Religare Enterprises Limited and Fusion CX Limited, respectively (web refs `turn967599view0`, `turn967599view1`).
2. Existing RSS raw snapshots (two previously verified artifacts):
   - Run 43489286657 raw XML SHA-256: `21de2c9b2d1f39cad81600cdca22556e813d2854eeee28d5082c913ec95aa1a4`.
   - Run 43490004265 raw XML SHA-256: `ee92888d16048899cffe4da9f57a6c246a7d4db2e133822e223e0674722bdaf0`.
   - Both contain 13 byte-identical parsed records; JSONL SHA-256 `b918f872cabca6b6d053e4f5eeb12850e1086233d27e2dbb8f79ffdc902a6511`.

## Bounded row-level findings
- RELIGARE: all three RSS items are represented in the five visible official rows by exact subject-family matches:
  1. Analyst/Investor Meet Para A-XBRL
  2. Analysts/Institutional Investor Meet/Con. Call Updates (NSE table truncates final text)
  3. Monitoring Agency Report
  Company identity is corroborated by the official NSE symbol link to Religare Enterprises Limited.
- FUSIONCX: two of three RSS items are represented in the five visible rows:
  1. Dividend
  2. Record Date
  The third RSS item is Outcome of Board Meeting; it is not in the five-row visible slice, despite the page summary showing 9 Corporate Announcements. This is NOT a missing-event conclusion; the full 9-row set was not exposed in the retrieved text.
- These are issuer/symbol/subject matches, not exact RSS-link-to-filing-attachment matches. The official page sample does not expose attachment URLs or precise filing timestamps for these rows.
- RSS pubDate values retain original timezone-naive strings; official page Broadcast Date is date-only. No timestamp normalization or equality assertion made.

## Official endpoint discovery boundary
- The official NSE page itself and its linked company quote pages are verified official sources.
- A third-party article published 2026-11-10 describes an apparent GET endpoint `/api/corporate-announcements` and parameters `index`, `from_date`, `to_date`, optional `symbol`. This is an unverified third-party report, not an NSE API specification. It is recorded only as a lead, not an approved source contract.
- The official page's rendered text does not disclose the underlying request URL, headers, parameter schema, pagination, retention or rate limits. No guessed endpoint request was made; no undocumented endpoint is promoted into collector.
- Next acceptance step: capture the request/response directly from the official page's own network activity or obtain an NSE-published specification, then validate exact schema and date/pagination semantics before any collector change.

## Decision
| Check | Result |
|---|---|
| RSS two-snapshot replay | PASS (prior Appendix 26) |
| Official page five-row visible sample | PASS |
| RELIGARE 3/3 subject-level visible matches | PASS |
| FUSIONCX 2/3 subject-level visible matches | PASS; 3rd not in visible slice |
| All 13 RSS items reconciled against complete official rows | UNKNOWN / NOT COMPLETE |
| Exact attachment URL equality | NOT RUN |
| Official JSON endpoint contract | NOT VERIFIED |
| Corporate Events P0 | BLOCKED |

No code/workflow changes, no symbol guessing, no synthetic data, no paid service, no PR/merge, no production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 remain unchanged.
