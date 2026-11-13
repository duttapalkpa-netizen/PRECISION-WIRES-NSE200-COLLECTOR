# Corporate Events P0 — Official Source Contract and Failure Diagnosis
Date: 2026-11-14
Scope: identify the next bounded, evidence-backed remediation for the only missing Macro-Geo P0 group. This is a source/contract audit, not a successful ingestion claim.

## Exact Run 210 failure evidence
From Run #210 artifact `12908992135` (run `40898379422`):
- `p0_repair_report.json`: `corporate_events.status=BLOCKED`, rows=0.
- Reason: "No valid official NSE rows with symbol, subject, publication timestamp and source URL".
- Attempted endpoint: `https://www.nseindia.com/api/corporate-announcements`.
- `p0_collection_manifest.json`: official NSE attempt timed out after 6 seconds (ReadTimeout).
- The 0-row outcome is therefore an acquisition/normalization failure; it is not evidence that no corporate events existed.

## Official NSE surface inspection
1. NSE Corporate Filings application: `https://www.nseindia.com/companies-listing/corporate-filings-application?id=allAnnouncements`
   - Official page separates Corporate Announcements, Corporate Actions, Board Meetings, Financial Results and other filing categories.
   - Its announcements table exposes Symbol, Subject and Broadcast Date. The corporate-actions table exposes Symbol, Purpose and Ex-Date.
   - The current official page rendered recent announcements dated 13-Nov-2026 and corporate actions with 13-Nov-2026 ex-dates. These are separate temporal fields and must not be conflated.
2. NSE Corporate Filings — Corporate Actions: `https://www.nseindia.com/companies-listing/corporate-filings-actions`
   - Official page exposes symbol, company, series, purpose, face value, ex-date, record date and book-closure dates.
3. NSE investor-relations Announcements page: `https://www.nseindia.com/static/investor-relations/announcements`
   - Official static listing exposes subject, announcement date, attachment and file size. It is a separate disclosure surface and not a substitute for the full market-wide filings feed.

## Required normalized event contract
Keep each source record raw and preserve the original source-specific time fields. A normalized row may be considered valid only when all required identity/provenance fields are directly observed:
- `source_exchange` = NSE
- `source_record_id` = original source ID if supplied; otherwise null (do not synthesize)
- `symbol` = exact exchange symbol, unchanged
- `company_name` = as published, if present
- `subject` = exact published subject/purpose
- `publication_timestamp` = exchange broadcast/announcement timestamp as published; if only a date exists, retain date precision and do not invent a time
- `event_or_effective_date` = separate field, e.g. ex-date, record date, meeting date; null if not present
- `source_url` = exact official page/API URL for the record; attachment URL separately if present
- `retrieved_at_utc`, `raw_payload_sha256`, `raw_payload_bytes`, `content_type`, HTTP status/final URL
- `event_type` = source category/purpose, not a guessed classification
- `isin` = only if explicitly supplied or joined through a dated official NSE security master with exact symbol+series identity and a documented join; otherwise UNKNOWN
- `series` = preserve when supplied; do not assume EQ for all records

## Acquisition and validation plan
1. Use the official NSE filings page's own data route as the discovery surface; capture actual request URL/query parameters from the live official page or browser network evidence before implementing. Do not guess endpoint parameters or invent pagination.
2. Retry the existing API route with bounded network timeout and retry/backoff (the prior six-second timeout is too short to establish endpoint unavailability). Keep each date window bounded and checkpointed; record every request, response status, final URL, MIME, byte count and raw SHA-256.
3. Acquire announcement rows and corporate-action rows as distinct source families. Do not merge ex-date into publication timestamp.
4. Parse to a raw immutable archive first; then normalize. Keep empty/malformed rows as rejected evidence with exact reason; do not silently drop them.
5. Validate symbol/series against the correct date-vintage official NSE security master. Preserve unmatched rows as UNKNOWN rather than dropping them.
6. Deduplicate only with a documented source-native ID; absent that, use a transparent composite key while retaining duplicate source rows and collision audit.
7. Produce coverage by requested date, returned date, symbol, source family and category; explicitly list no-data dates and failed requests.
8. Feed only accepted rows to the existing P0 group contract after independent QA. No selector or score changes.

## Acceptance gate
| Criterion | Current status |
|---|---|
| Official NSE filing surfaces identified | PASS |
| Source fields and temporal semantics mapped | PASS |
| Prior timeout and 0-row failure tied to exact Run 210 evidence | PASS |
| Live API request shape/pagination verified from official network capture | UNKNOWN / NOT YET VERIFIED |
| Raw official payload archived with byte count, MIME and SHA-256 | NOT ACQUIRED |
| Symbol/series/ISIN date-vintage validation | NOT RUN |
| Duplicate, timestamp and coverage QA | NOT RUN |
| Corporate Events P0 group | BLOCKED |

## Safety / scope
No paid API or service, third-party scraper, fabricated timestamp, synthetic event, guessed API query, source promotion, code change, workflow run, PR merge or production integration. NSE public filing pages are the source of record; any undocumented endpoint must be treated as an implementation detail until its live request shape and returned fields are captured. Hard Gate remains BLOCKED.

## Sources inspected
- NSE Corporate Filings application: https://www.nseindia.com/companies-listing/corporate-filings-application?id=allAnnouncements
- NSE Corporate Filings — Corporate Actions: https://www.nseindia.com/companies-listing/corporate-filings-actions
- NSE investor-relations Announcements: https://www.nseindia.com/static/investor-relations/announcements
