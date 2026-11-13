# Corporate Events P0 — Official NSE RSS Channel Evaluation
Date: 2026-11-14
Scope: evaluate an additional first-party NSE disclosure channel after the Run 210 JSON endpoint timed out. This is a source-discovery and contract audit only; no raw feed bytes were obtained.

## Official source evidence
- NSE RSS page: https://www.nseindia.com/static/rss-feed (legacy route https://www.nseindia.com/rss-feed redirects here).
- The page explicitly describes RSS as a way to receive fresh NSE updates and states subscribers have immediate access to latest material posted on NSE (subject to reader/provider delays).
- The official page enumerates distinct Corporate Information feeds: Announcements, Annual Reports, Board Meetings, BRSR, Corporate Actions, Corporate Governance, Buyback/Redemption, Financial Results, Integrated Filing-Financials, Insider Trading, Investor Complaints, Offer Documents, Related Party Transactions, Regulation 29, Regulation 31, Reason for Encumbrance, Secretarial Compliance, Share Transfers, Shareholding Pattern, Deviation & Variation, Unitholding Patterns and Voting Results.
- NSE Corporate Filings application independently displays separate latest tables for Corporate Announcements (Symbol, Subject, Broadcast Date), Corporate Actions (Symbol, Purpose, Ex-Date) and Board Meetings (Symbol, Purpose, Meeting Date). It currently displays announcement and action records dated 13-Nov-2026.
- NSE investor-relations Announcements page separately publishes subject, announcement date, attachment and file size.

## What this establishes
1. RSS is a first-party NSE publication/distribution channel, not a third-party substitute.
2. Announcements and Corporate Actions are distinct feeds and must remain separate source families.
3. RSS is suitable as a potential low-latency discovery/ingestion fallback or cross-check; it is not yet proven to provide full market-wide historical coverage, all required fields, stable IDs, ISIN, or attachment/source URL metadata.
4. The current web-rendered NSE RSS page exposes feed icons as image links but the exact XML feed target could not be resolved from the page text extraction. No feed URL is guessed.
5. The page states "immediate" access, but downstream reader/provider delays may occur; store the observed publication timestamp and retrieval timestamp separately.

## Required validation before production ingestion
- Capture exact XML feed href from the official page's HTML or browser network panel; retain the original URL and retrieval evidence.
- Download raw XML with a bounded request; record HTTP status, final URL, MIME, bytes, retrieved_at_utc and SHA-256.
- Inspect RSS version, channel metadata, item GUID, pubDate/timezone, title/description, link and enclosure fields. Do not assume any element exists before observing it.
- Test overlapping refreshes and feed retention across several consecutive dates; quantify duplicates, missing items and oldest retained item.
- Cross-check feed items against the official Corporate Filings application for the same dates; keep announcement publication time distinct from corporate action ex-date/record date and board meeting date.
- Preserve raw XML items and rejected/ambiguous items. Do not deduplicate without source GUID or a documented collision-safe key.
- Validate symbol/series against the correct dated official NSE Security Master; ISIN remains UNKNOWN unless explicitly supplied or joined under a documented date-vintage key.
- Only after raw and coverage QA, map eligible announcement items into Corporate Events P0; RSS absence must not be interpreted as no event.

## Acceptance
| Criterion | Result |
|---|---|
| Official NSE RSS page identified | PASS |
| First-party feed families enumerated | PASS |
| Announcements/actions/board meetings semantically separated | PASS |
| Exact feed XML URL captured | UNKNOWN / NOT RESOLVED |
| Raw XML acquired and hashed | NOT ACQUIRED |
| GUID/timezone/schema/retention verified | NOT RUN |
| Historical completeness / date coverage | UNKNOWN |
| Corporate Events P0 | BLOCKED |

## Sources
- NSE RSS Feeds: https://www.nseindia.com/static/rss-feed
- NSE Corporate Filings application: https://www.nseindia.com/companies-listing/corporate-filings-application
- NSE Investor Relations Announcements: https://www.nseindia.com/static/investor-relations/announcements

## Safety
No paid data, paid API, external contact, third-party data vendor, guessed feed URL, synthetic event, source promotion, code/workflow change, PR merge or production integration. Existing Hard Gate and all protected invariants remain unchanged.
