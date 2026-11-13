# Corporate Events P0 — Official Filings vs RSS Freshness Cross-check
Date: 2026-11-14
Scope: compare currently exposed official NSE Corporate Filings page fields and snapshot with secondary RSS-reader status signals. No RSS payload bytes were available; this is not item-level feed validation.

## Official NSE Corporate Filings snapshot
Source: https://www.nseindia.com/companies-listing/corporate-filings-application
Search retrieval date: 2026-11-14
- Page summary displays 7 Corporate Announcements, 26 Corporate Actions and 535 Board Meetings.
- Latest Announcements table exposes columns Symbol, Subject, Broadcast Date. Five displayed examples:
  - YATRA — Investor Presentation — 13-Nov-2026
  - GICHSGFIN — Updates — 13-Nov-2026
  - TARSONS — Analysts/Institutional Investor Meet/Con. Call Update — 13-Nov-2026
  - ONIDA — Credit Rating- Revision — 13-Nov-2026
  - RUBYMILLS — Change in Management — 13-Nov-2026
- Separate Corporate Actions table uses Symbol, Purpose, Ex-Date; Board Meetings table uses Symbol, Purpose, Meeting Date. These are different event families and different date semantics.
- NSE disclaimer states disclosures are uploaded by the concerned company and displayed by the exchange without verification of adequacy, accuracy or veracity. The event pipeline must preserve issuer-submitted source text and not mark it independently verified by NSE.

## Secondary RSS reader signal
- Feeder listing A reports the NSE-hosted announcements feed as working, checked about 1 hour ago, with latest posts about 4 hours ago. It lists latest-post company names including Cantabil Retail India, W S Industries, CARE Ratings, ABH Healthcare, GP Eco Solutions and Marushika Technology.
- Feeder listing B reports the same feed as working, checked 5 minutes ago, latest posts about 15 minutes ago, with examples including Railtel, ACC, Star Health, Axis Max Life and UTI Mutual Fund.
- The two listings disagree materially on post rate (about 1,011/day vs about 1,427/day) and freshness timestamps. This demonstrates reader-specific caches/measurement windows or other unexplained differences; these metrics are not reliable coverage evidence.
- The RSS sample items do not overlap with the five latest rows rendered by the official filings page at retrieval time. Because the page exposes only a limited latest-row sample and the RSS item records/raw XML were unavailable, this is not evidence of missing events or feed incompleteness. No item-level reconciliation can be claimed.

## Reconciliation conclusion
1. Official NSE page independently confirms the field contract for announcement discovery: symbol, subject, broadcast date.
2. Corporate Actions and Board Meetings must remain separate; ex-date and meeting date are not announcement publication timestamps.
3. RSS reader "working" and high post-rate labels are secondary availability signals only; conflicting counts mean they must not be used for event volume, completeness or coverage denominators.
4. NSE's own disclaimer makes issuer-submitted disclosures not independently verified by the exchange; retain raw provenance and add a verification status that does not imply NSE endorsement.
5. The official page's summary count (7) is a live-page snapshot, not a historical count or a validated daily universe.

## Acceptance
| Criterion | Result |
|---|---|
| Official NSE announcement fields and sample rows captured | PASS (page snapshot) |
| Official distinction among announcements/actions/meetings | PASS |
| NSE disclaimer/issuer responsibility captured | PASS |
| Secondary RSS reader operational signals observed | PASS (secondary only) |
| RSS volume/freshness metrics consistent across readers | FAIL / CONFLICT |
| Raw RSS XML acquired | NOT ACQUIRED |
| Item-level GUID/symbol/title/pubDate cross-check | NOT RUN |
| Completeness/retention/missing-item rate | UNKNOWN |
| Corporate Events P0 | BLOCKED |

## Sources
- NSE Corporate Filings: https://www.nseindia.com/companies-listing/corporate-filings-application
- NSE RSS page: https://www.nseindia.com/static/rss-feed
- Feeder listing A: https://feeder.co/discover/aaf60f744d/nseindia-com-companies-listing-corporate-filings-announcements
- Feeder listing B: https://feeder.co/discover/c63e3e629e/nseindia-com-corporates-corporatehome-html-id-allannouncements

## Safety
No secondary RSS item promoted to official raw data, no synthetic event/timestamp, no paid service, no code/workflow changes, no PR merge or production integration. Hard Gate and protected invariants unchanged.
