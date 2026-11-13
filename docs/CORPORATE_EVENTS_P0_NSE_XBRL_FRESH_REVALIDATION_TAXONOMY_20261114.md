# NSE Announcement XBRL — Fresh Revalidation and Taxonomy Migration Check
Date: 2026-11-14

## Official-source revalidation
Official page: https://www.nseindia.com/companies-listing/corporate-filings-announcements-xbrl
Fresh web retrieval reference: `turn423980search0` (retrieved/crawled within the current research session).

Observed page controls and state:
- Announcement Type, Company, Events / Subject, From, To; GO; Download (.csv).
- Current rendered count: 1–20 of 958 records; 48 pages.
- Fields: SYMBOL, COMPANY NAME, Event / Subject, DETAILS, ATTACHMENT, TYPE OF SUBMISSION, BROADCAST DATE/TIME.
- Expanded broadcast details include Exchange Dissemination Time and Time Taken.
- Page note: "The said event has been merged with Para B and hence the data will be available under Para B drop down effective 20-Jun-2026." This is a source-published taxonomy transition notice.

## Research implications
1. Treat Announcement Type / event taxonomy as time-versioned. For dates on/after 20-Jun-2026, the affected event must be searched under Para B, not assumed to remain under its former Para A category. Preserve source wording and the effective date; do not silently rewrite historical records.
2. The page's 958-record count and 48-page count are a current UI snapshot, not a historical coverage guarantee or an RSS denominator.
3. CSV download affordance is visible, but this audit did not obtain the CSV response bytes, exact request URL, headers, pagination behavior, or date filter execution. No export acquisition or row-level RSS match is claimed.
4. Sample rows remain from 27–29 Oct 2026, not the 13–14 Nov RSS capture window. A separate date-filtered export is still required for overlap analysis.
5. Announcement XBRL remains a subset; do not assume full coverage of general announcement RSS or other filing families.

## Acceptance
| Check | Result |
|---|---|
| Official page reachable in fresh retrieval | PASS |
| 958 / 48 current UI count observed | PASS (snapshot only) |
| Column and timestamp fields observed | PASS |
| Para A → Para B migration notice/effective date recorded | PASS |
| Date-window CSV bytes/hash | NOT CAPTURED |
| Exact export request contract | UNKNOWN |
| 13 RSS item reconciliation via XBRL | NOT RUN |
| General announcement completeness | UNKNOWN |
| Corporate Events P0 | BLOCKED |

## Safe next step
Use a browser session on the official NSE page to set a bounded From/To range overlapping 13–14 Nov 2026, execute GO, and invoke its own CSV Download control. Capture the exact browser network request/response and downloaded CSV bytes; record request/final URL, response status/content-type, retrieval time, byte count, SHA-256, headers where available, row count and original fields. Only then reconcile RSS records. Do not guess API routes or parameters.

No code/workflow/production change; no paid service, no PR/merge, no synthetic data. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.
