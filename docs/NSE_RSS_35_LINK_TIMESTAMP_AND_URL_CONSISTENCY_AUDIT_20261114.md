# NSE RSS 35-link timestamp and URL consistency audit — 2026-11-14

## Exact input
- Inventory: `NSE_RSS_35_linked_attachment_inventory_20261114.csv`
- 35 rows; 15,648 bytes; SHA-256 `ba60e2859990be59f5f1a573ffccb4dfab6f498e5042d3bb5ab5ec8c4ad066ef`.
- The inventory derives from the 190-record RSS snapshot captured in run `43558025207`, artifact `14098814399`; parsed source member SHA-256 `fa17c0c89ebc10321821aa54fe5f5eaf7c488ddbd2e3a4d32ac0aa2e49c9b60d`.

## URL and row-integrity checks
- 35/35 records have non-empty issuer title, pubDate, description, URL and filename.
- 35/35 URLs use HTTPS and exact host `nsearchives.nseindia.com`.
- 35/35 URL path basenames exactly equal the preserved filename field.
- 35/35 URLs are unique; no query string or fragment present.
- File extension counts: 33 PDF, 2 XML.
- These checks validate string-level provenance and internal consistency only. They do not prove the URLs resolve or that attachments are valid.

## Filename timestamp vs RSS pubDate
- Parsed timestamp candidates from all 35 filenames using the observed filename conventions: 33 ordinary 14-digit timestamps and 2 XBRL/XML timestamps with millisecond suffixes.
- All 35 timestamps parsed successfully under their respective filename formats.
- RSS pubDate is later than the filename timestamp for all 35 records.
- Difference range: 1–470 seconds (maximum 7 minutes 50 seconds); no negative differences and none exceed 1 hour.
- This is a consistency check, not proof that the filename timestamp has a formally documented meaning or that pubDate is an exchange broadcast timestamp. Preserve both raw values separately; do not overwrite or infer timezone precision beyond the source strings.
- The two XML names use document identifiers `REG30_PARA_B_27796_WebXMLFile_20261114_093607605.xml` and `SAIIM_2677_WebXMLFile_20261114_003557058.xml`; the 9-digit suffix is retained as supplied and not interpreted as a standard timestamp field beyond the leading date/time.

## Machine-readable output
- `NSE_RSS_35_link_timestamp_consistency_20261114.csv`
- 35 rows; 6,598 bytes.
- SHA-256 `e6fa614d2602de4f7849271847c76aec30b3b8fae2f6905c2fa476a013903332`.
- Includes raw pubDate/filename, parsed candidate timestamp, difference in seconds, parse status, URL scheme/host, path-filename match and query/fragment flags.

## Retrieval/content-validation boundary
A direct retrieval attempt through the web retrieval path for two PDFs and one XML URL returned inaccessible/internal errors. This does not establish that the links are broken. No attachment bytes, HTTP status, redirect, MIME response header, byte count, PDF text, XML parse, or per-attachment SHA-256 were acquired. Attachment-content validation remains 0% / NOT VALIDATED.

## Status
- 35-row structural and string-integrity checks: 100%.
- URL host/scheme/path checks: 100%.
- Filename timestamp parsing and pubDate consistency: 100%.
- Live attachment retrieval and content validation: 0%.
- Official issuer-symbol mapping: 0% / UNKNOWN.
- Event-to-price join and matured H+1/H+3/H+5 study: 0% / BLOCKED.
- No code, source data, selector, ranking, diagnostics, workflow or production behavior changed; no PR/merge.
- Overall project: NOT CALCULABLE; Hard Gate BLOCKED.

## Official context
NSE's public corporate-filings pages expose corporate announcements and XBRL announcement sections, and NSE's circular guidance describes machine-readable/searchable corporate announcement filings. These pages provide context for the disclosure channel, not a substitute for fetching the exact archived attachment bytes:
- https://www.nseindia.com/companies-listing/corporate-filings-application
- https://www.nseindia.com/companies-listing/corporate-filings-announcements-xbrl-trading-window-disclosure
- https://nsearchives.nseindia.com/content/equities/NSE_Circular_17012018.pdf
