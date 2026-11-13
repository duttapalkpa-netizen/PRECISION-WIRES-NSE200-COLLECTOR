# NSE Official XBRL Catalog — Event Taxonomy Crosswalk and RSS Scope Rules
Date: 2026-11-14

## Official sources revalidated
1. General Announcement XBRL page:
   https://www.nseindia.com/companies-listing/corporate-filings-announcements-xbrl
   Current web snapshot: 1–20 of 958; fields SYMBOL, COMPANY NAME, Event/Subject, DETAILS, ATTACHMENT, TYPE OF SUBMISSION, BROADCAST DATE/TIME. Page notice says the affected event has moved to Para B effective 20-Jun-2026.
   Evidence: `turn649111search0`.
2. Official NSE XBRL Filing Information catalog:
   https://www.nseindia.com/static/companies-listing/xbrl-information
   NSE describes XBRL as structured compliance filings submitted through NEAPS and provides taxonomy / instance-document downloads. Catalog includes distinct filing templates such as Regulation 30 event categories, Regulation 29 prior intimation, Regulation 33 results, Regulation 44 voting results, shareholding, investor complaints, credit rating, default history and Para B.
   Evidence: `turn649111search1`.
3. Trading Window XBRL route:
   https://www.nseindia.com/companies-listing/corporate-filings-announcements-xbrl-trading-window-disclosure
   Current rendered snapshot: 390 records / 20 pages; subject Closure of Trading Window.
   Evidence: `turn649111search4`.
4. General Corporate Filings page:
   https://www.nseindia.com/companies-listing/corporate-filings-application
   Fresh page snapshot shows 9 Corporate Announcements, 14 Corporate Actions, 420 Board Meetings and 5 latest-announcement rows dated 12-Nov-2026. Another indexed snapshot showed 7/26/535 and latest rows dated 13-Nov-2026. This demonstrates counts are time-sensitive page snapshots and must be time-stamped; they are not fixed totals or RSS coverage denominators.
   Evidence: `turn649111search2`, `turn649111search3`.

## Taxonomy and scope conclusions
- Do not equate RSS Announcements with XBRL filings catalog. NSE XBRL is a structured compliance filing mechanism; the catalog describes templates and taxonomies, not an exhaustive public event feed.
- The Regulation 30 / Para A / Para B taxonomy is event-specific and versioned. Preserve the source's original event label, filing type, and effective-date context. For the announced 20-Jun-2026 migration, query Para B for affected event types after the effective date; do not relabel historical records.
- Trading Window is a specialized filing subset. Its page count (390) is not additive to general announcements without stable filing identity and duplicate checks.
- General Corporate Filings page has distinct announcement, corporate action, board meeting, financial results and shareholding tables. Their date fields mean different things (Broadcast Date vs Ex-Date vs Meeting Date vs Period Ended / As-on Date); keep separate event families and date semantics.
- The two general page snapshots report different counts (9/14/420 and 7/26/535), so counts are volatile. Never use them as static coverage denominator.
- Fresh samples shown by XBRL pages are late October; general page sample dates are 12–13 Nov. No 13 RSS item exact row/attachment match is claimed in this audit.

## Acceptance
| Check | Result |
|---|---|
| Official XBRL catalog and structured filing description | VERIFIED |
| Para B migration/effective date | VERIFIED |
| Trading Window as specialized route | VERIFIED |
| General filings event-family/date semantics | VERIFIED |
| Current page counts time-variant | VERIFIED |
| CSV bytes / exact export request | NOT CAPTURED |
| Cross-route stable identity / duplicate audit | NOT RUN |
| RSS 13-item exact reconciliation | NOT RUN |
| Corporate Events P0 | BLOCKED |

## Next action
Obtain CSV exports only through the official page's own UI for the exact RSS publication window, preserving route, category, original label, source symbol, source link/attachment, broadcast timestamp, and raw bytes/hash. Reconcile duplicates only by source-native stable ID or exact attachment URL; do not infer identity from company/date/subject alone.

No code/workflow/production change, no paid service, no PR/merge, no synthetic rows/timestamps. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and CORE-672 unchanged.
