# Corporate Events P0 — NSE Announcements RSS Feed URL Resolution
Date: 2026-11-14
Scope: resolve the first-party NSE announcements RSS feed URL using official NSE page evidence plus independent directory corroboration; test retrieval without treating a parser/network limitation as a feed QA pass.

## Feed URL resolution
- Official NSE RSS page: https://www.nseindia.com/static/rss-feed
- The official page explicitly lists the Announcements feed under Corporate Information and instructs users to click the RSS icon to open the feed in a browser or reader.
- Independent feed directory Feeder's NSE feed listing identifies the announcements feed URL as:
  `https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml`
- The same listing enumerates related NSE-hosted feeds:
  - Corporate Actions: `https://nsearchives.nseindia.com/content/RSS/Corporate_action.xml`
  - Board Meetings: `https://nsearchives.nseindia.com/content/RSS/Board_Meetings.xml`
  - Financial Results: `https://nsearchives.nseindia.com/content/RSS/Financial_Results.xml`
- The directory also describes the announcements feed as National Stock Exchange announcements. This is corroboration for locating a URL, not proof of completeness or a substitute for the official NSE publication page.
- URL has the NSE archive host `nsearchives.nseindia.com`; no query parameters were guessed.

## Retrieval test and limitation
- Direct open of the exact XML URL returned an unsupported-content-type error because the response is `application/xml`; the web page reader does not render raw XML. This is not a 404 and is consistent with an XML feed endpoint, but the HTTP status, final URL, raw byte count, MIME header and payload digest were not exposed by that reader.
- A direct raw download attempt from the execution environment failed at DNS resolution (`Temporary failure in name resolution`). No file bytes were received.
- Therefore the feed URL is RESOLVED as a candidate NSE-hosted endpoint with independent directory corroboration; raw feed acquisition is NOT ACQUIRED. Do not claim feed health, valid XML, item count, GUID/pubDate schema, timezone, retention or historical completeness.

## Next bounded acquisition
- Retry from a network-enabled environment that can reach the NSE archive host, with a 10–15 second timeout and one bounded retry; capture status, final URL, Content-Type, Content-Length/actual bytes, retrieved_at_utc and SHA-256.
- Preserve the exact raw XML before parsing. Parse only after validating XML well-formedness and RSS/Atom version.
- Inspect channel metadata and item GUID, title, link, pubDate/timezone, description and enclosure without assuming all fields exist.
- Cross-check at least two overlapping publication dates against the official NSE Corporate Filings announcement table; retain duplicates and report source-native GUID collisions.
- Treat feed retention as a rolling snapshot unless measured historical coverage proves otherwise.

## Acceptance
| Criterion | Result |
|---|---|
| Official NSE RSS announcements category verified | PASS |
| NSE-hosted feed URL identified with independent corroboration | PASS (URL resolution only) |
| XML endpoint responds in a format incompatible with HTML reader | OBSERVED; not HTTP-status verification |
| Raw XML bytes acquired | NOT ACQUIRED |
| HTTP status/final URL/MIME/bytes/SHA-256 | UNKNOWN |
| XML parse, GUID, pubDate/timezone, retention | NOT RUN |
| Coverage cross-check vs NSE filings | NOT RUN |
| Corporate Events P0 | BLOCKED |

## Sources
- Official NSE RSS page: https://www.nseindia.com/static/rss-feed
- Independent NSE feed directory (URL corroboration only): https://feeder.co/discover/c63e3e629e/nseindia-com-corporates-corporatehome-html-id-allannouncements
- NSE-hosted announcements XML candidate: https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml

## Safety
No synthetic rows/timestamps, guessed query parameters, paid data/API, third-party event data, source promotion, code/workflow change, PR merge or production integration. Hard Gate and protected invariants unchanged.
