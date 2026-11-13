# Corporate Events P0 — RSS Operational Signal and Acquisition Readiness
Date: 2026-11-14

## New independent availability evidence
The NSE official RSS directory confirms that Announcements is a first-party Corporate Information feed and explains that users should open its RSS icon to obtain the actual subscription URL. It also warns that third-party reader/provider delays are outside NSE's control.
- Official NSE RSS page: https://www.nseindia.com/static/rss-feed

Two independent Feeder directory entries currently describe the NSE-hosted announcements RSS feed as working and show recent items:
- https://feeder.co/discover/aaf60f744d/nseindia-com-companies-listing-corporate-filings-announcements
- https://feeder.co/discover/c63e3e629e/nseindia-com-corporates-corporatehome-html-id-allannouncements
Both point to the same NSE-hosted XML path, with minor host alias differences (nsearchives.nseindia.com vs archives.nseindia.com). This is secondary availability evidence only. It does not establish NSE's HTTP status, exact response headers, completeness, or retention.
- A recent technical article published 3 days before this audit independently describes the same NSE RSS path and reports a sample of 548 items retrieved on 10-Nov-2026. This is a non-official reproduction; it is not adopted as source evidence or used for data values: https://dev.to/datadaemon/is-there-an-nse-india-api-for-corporate-announcements-corporate-actions-and-bulk-deals-json-2d48

## Direct acquisition attempt
- URL attempted: https://nsearchives.nseindia.com/content/RSS/Online_announcements.xml
- Request headers included a browser-like User-Agent and Accept for RSS/XML.
- Timeout: 15 seconds.
- Result: DNS resolution failure (`Temporary failure in name resolution`) in the current execution environment.
- No HTTP response, raw bytes, MIME, byte count, final URL, or SHA-256 were received.
- Web page reader independently refuses the endpoint because it returns/declares `application/xml`; it does not expose the XML payload. This is not a transport-level HTTP status.

## Host alias policy
- The official NSE RSS page is the source of authority.
- `nsearchives.nseindia.com` is the host identified by the RSS directory and earlier technical reproduction.
- `archives.nseindia.com` appears as an alias in another directory. Do not silently treat these hosts as identical or redirect-equivalent. If acquired, capture the final URL and redirect chain and preserve original requested URL.

## Operational readiness conclusion
| Test | Result |
|---|---|
| Official NSE Announcements RSS category | PASS |
| NSE-hosted XML path independently corroborated | PASS |
| Independent reader currently reports recent feed activity | SECONDARY SIGNAL ONLY |
| Direct DNS/network retrieval from this runtime | BLOCKED |
| HTTP status, redirects, MIME headers, raw bytes, SHA-256 | UNKNOWN |
| XML validity, GUID uniqueness, pubDate timezone | NOT RUN |
| Retention, missing-item rate, completeness | UNKNOWN |
| Corporate Events P0 ingestion | BLOCKED |

## Next action when network path is available
Perform a single bounded GET to the exact NSE-hosted URL with 15-second timeout; record status, redirect chain, MIME, actual bytes and SHA-256; validate XML; preserve every item. Then acquire one overlapping daily NSE filings table and reconcile GUID/link/symbol/title/pubDate. No historical completeness claim from RSS alone.

## Safety
No third-party feed content is used as authoritative event data; no synthetic rows or timestamps, no endpoint parameters guessed, no paid service, code change, workflow run, PR merge or production integration. Hard Gate and protected invariants remain unchanged.
