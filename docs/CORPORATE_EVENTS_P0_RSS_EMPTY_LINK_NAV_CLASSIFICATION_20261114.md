# NSE RSS empty-link cohort classification — 2026-11-14

## Scope and input provenance
- Input: official NSE RSS acquisition artifact from workflow run 43558025207, artifact ID 14098814399.
- Artifact ZIP SHA-256: `ca0649032c67fd4519bce66d2dd6cd61805efbd2f9f7f0612fa88b05cedec517`.
- Raw XML SHA-256: `b76717de6777404a56ded5cae962c922f199b32534364800a96ef059918a9990`.
- JSONL SHA-256: `fa17c0c89ebc10321821aa54fe5f5eaf7c488ddbd2e3a4d32ac0aa2e49c9b60d`.
- This is a re-analysis of the already acquired immutable artifact; no new fetch or synthetic data.

## Deterministic cohort result
- Total RSS items: 190; non-empty-link cohort: 35; empty-link cohort: 155.
- All 155 empty-link records have the exact source subject suffix `SUBJECT: Declaration of NAV`.
- All 155 source-native publication date strings are `14-Nov-2026 07:00:00`.
- Their titles identify mutual funds / ETFs / fund schemes, and descriptions identify Asset Management Companies and NAV values/dates.
- Therefore, the 155 empty-link records are classifiable as a NAV disclosure cohort, not as 155 missing equity-company announcement attachments.
- The cohort is retained as 155 source records; no rows are deleted, merged, or assigned fabricated URLs.

## Symbol and identity handling
- Some descriptions contain token-like prefixes (for example ETF/fund scheme codes). They are NOT promoted to NSE-listed equity symbols or issuer identifiers.
- No official dated General Announcements CSV row export, issuer-master join, or fund-scheme master evidence was captured in this task. Hence symbol mapping, scheme identifiers, and attachment identity remain UNKNOWN.
- NAV valuation date inside the description is not substituted for RSS publication timestamp. Publication timestamp remains source-native and timezone-naive.

## Official source boundary
- NSE's official RSS page documents separate feeds including Announcements, Board Meetings, Corporate Actions and other corporate information, and notes possible reader/provider refresh delays: https://www.nseindia.com/static/rss-feed
- NSE's official General Announcements page presents a separate announcement panel with Symbol, Subject and Broadcast Date; latest indexed rows are a five-row live sample, not a complete date-window export: https://www.nseindia.com/companies-listing/corporate-filings-application?id=allAnnouncements
- The indexed page currently shows five latest announcements dated 14-Nov-2026 (RELIGARE, FUSIONCX, KOTHARIPET, SENCO), which are not sufficient to validate or invalidate the 155 NAV records.
- No exact CSV request URL, downloaded CSV bytes/hash, pagination contract, or 155-row official filing reconciliation is claimed.

## Decision
- Empty-link NAV cohort classification: PASS (155/155, source-text rule).
- Equity issuer/symbol mapping: UNKNOWN.
- General Announcements exact row reconciliation: NOT RUN.
- RSS source completeness / historical coverage: UNKNOWN.
- Corporate Events P0 remains BLOCKED pending official export capture, stable identity rules across event families, and coverage/replay validation.
- No code, workflow, production selector, ranking, or CORE-672 changes; no paid services, external contact, PR/merge, synthetic values, or guessed URLs.
