# NSE Corporate Filing XBRL — Category Route Inventory & Coverage Boundary Audit
Date: 2026-11-14

## Official page evidence
Fresh official NSE search retrievals on 2026-11-14 show that the XBRL filing surface is not a single undifferentiated page:
1. General Announcement XBRL:
   https://www.nseindia.com/companies-listing/corporate-filings-announcements-xbrl
   Current rendered view: 1–20 of 958 records, 48 pages. Fields include SYMBOL, COMPANY NAME, Event/Subject, DETAILS, ATTACHMENT, TYPE OF SUBMISSION, BROADCAST DATE/TIME.
2. Trading Window Disclosure route:
   https://www.nseindia.com/companies-listing/corporate-filings-announcements-xbrl-trading-window-disclosure
   Current rendered view: 1–20 of 390 records, 20 pages; category subject shown as Closure of Trading Window.
3. Loss of Share route:
   https://www.nseindia.com/companies-listing/corporate-filings-announcements-xbrl-loss-share
   Current rendered view: 1–8 of 8 records, 1 page; subject shown as Loss of share certificates.
4. NSE XBRL Filing Information:
   https://www.nseindia.com/static/companies-listing/xbrl-information
   The official index lists Regulation 30 - Para B of Part A of Schedule III of SEBI LODR 2015 and downloadable files, alongside other filing forms.

Evidence refs: `turn937329search0`, `turn937329search1`, `turn937329search3`, `turn937329search8`.

## Findings and safeguards
- The visible NSE website uses multiple category-specific filing routes. A single general XBRL page count (958) is not a total across all category routes, nor a coverage denominator for general RSS.
- The Trading Window route is a specialized subset and must not be double-counted as an independent set unless record-level identities are reconciled.
- Loss of Share is another specialized subject route. Keep its records in the same announcement event family only when source-native identity and semantics support it; do not merge by date or company name alone.
- The XBRL information page is a filing-form/catalog reference, not an announcement event feed. Its downloadable regulatory templates should not be counted as event records.
- Main page's Para A→Para B effective-20-Jun-2026 note requires a versioned taxonomy map. Category routes and dropdown options need to be captured independently; do not infer all event categories from the page title.
- These retrieved page samples are dated 27–30 Oct 2026, not the 13–14 Nov RSS window. No RSS item-level match is claimed.

## Acceptance
| Check | Result |
|---|---|
| General Announcement XBRL route | VERIFIED |
| Trading Window specialized route | VERIFIED |
| Loss of Share specialized route | VERIFIED |
| Official XBRL form catalog | VERIFIED |
| Cross-route record identity / duplicate reconciliation | NOT RUN |
| Complete category route inventory | UNKNOWN |
| 13 RSS items reconciled across routes | NOT RUN |
| Date-window CSV response bytes/hash | NOT CAPTURED |
| Corporate Events P0 | BLOCKED |

## Next action
Build a source-grounded route inventory from official NSE page links only, then capture date-filtered CSV exports from each relevant route for 13–14 Nov 2026. Preserve route/category as a first-class field, compare stable source identifiers/attachment URLs, and deduplicate only on exact source-native identity. Do not add speculative endpoints or merge specialized subsets into general feed totals.

No code/workflow/production changes, no paid services, no PR/merge, no synthetic data. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.
