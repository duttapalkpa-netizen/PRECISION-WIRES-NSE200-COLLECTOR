# Bounded Macro-Geo P0 raw-data acquisition & dated event sample — 2026-11-02

Status: `ACQUISITION_ATTEMPTED_RAW_BINARY_FETCH_BLOCKED_EVENT_SAMPLE_PARTIAL`. This is a fail-closed evidence report. It does not claim a successful raw-data download, SHA-256 of unavailable files, repeated-download drift result, or vintage revision PASS.

## Fixed bounded window
2025-10-01 through 2025-10-10 inclusive (calendar days; official trading days only for index/VIX series). Two attempts were made for the NSE daily all-indices CSV:
- https://nsearchives.nseindia.com/content/indices/ind_close_all_01102025.csv
- https://nsearchives.nseindia.com/content/indices/ind_close_all_02102025.csv

The web retrieval service rejected CSV as unsupported content type for the first URL and could not access the second. A direct file download attempt also failed. No raw bytes were obtained; therefore SHA-256 is `NOT_COMPUTED`, repeated-download drift is `NOT_TESTED`, and no data row is promoted.

## P0 group collection status

| Group | Official source / bounded target | Raw download | SHA-256 | Repeated-download drift | Vintage comparison | Status |
|---|---|---|---|---|---|---|
| benchmark_index | NSE all-indices daily CSV, 01–10 Oct 2025 | BLOCKED (CSV endpoint inaccessible in this runtime) | NOT_COMPUTED | NOT_TESTED | No archived file pair | UNKNOWN |
| sector_indices | Nifty Indices historical-data portal; same 01–10 Oct 2025 window | UI exposes index/date filters, but no selected CSV bytes returned in this run | NOT_COMPUTED | NOT_TESTED | No archived file pair | UNKNOWN |
| volatility | NSE India VIX historical data; same window | UI exposed historical CSV download control but no CSV bytes returned | NOT_COMPUTED | NOT_TESTED | No archived file pair | UNKNOWN |
| geopolitical_events | Official PIB + MEA dated release pages | HTML/text release metadata captured in ledger; raw source-file bytes not archived locally in this run | NOT_COMPUTED for raw files | NOT_TESTED | No independently archived duplicate copies | PARTIAL_SAMPLE_ONLY |

## Dated geopolitical-event / official-release sample

The sample records publication time separately from event date. These are dated government releases and sample rows, not a complete geopolitical event universe. Event occurrence time is UNKNOWN unless stated in the source.

| Publisher | Release ID / identifier | Published time/date | Subject | Evidence URL |
|---|---|---|---|---|
| PIB / Ministry of Finance | PRID 2175552 | 06 Oct 2025 7:50 PM | Fourth Kautilya Economic Conclave concluded | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2175552&lang=2&reg=3 |
| PIB / Ministry of External Affairs | PRID 2174721 | 04 Oct 2025 12:29 PM | Passport Mobile Seva Kendra at Symbiosis International University Pune | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2174721&lang=2&reg=3 |
| PIB / Ministry of External Affairs | PRID 2177448 | 10 Oct 2025 5:58 PM | Passport Mobile Seva Camp at FTII Pune | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2177448&lang=2&reg=48 |
| PIB / Ministry of External Affairs | PRID 2174482 | 03 Oct 2025 12:46 PM | Global Mobility Conclave on Overseas Recruitment | https://www.pib.gov.in/PressReleasePage.aspx?PRID=2174482&lang=2&reg=3 |
| MEA | Advanced-search result: Swachhata Hi Seva Campaign | Published 10 Oct 2025 (time not supplied in search result) | Campaign 17 Sep–02 Oct 2025; MEA offices/missions/RPOs | https://www.mea.gov.in/advanced-search-list.htm |
| MEA | Advanced-search result: 15th India-Australia JWG on Counter Terrorism | Published 30 Oct 2025 (outside fixed sample window; retained as control only) | Bilateral counter-terrorism working group, held 29–30 Oct | https://www.mea.gov.in/advanced-search-list.htm |

Note: the MEA 30-Oct row is explicitly outside the 01–10 Oct collection window and is included only as a control example of dated MEA metadata, not as a sample-window event. The 10-Oct MEA campaign entry has date-only publication precision in the search result. A specific MEA canonical detail URL was not resolved for the indexed entry, so it is not treated as a fully captured source document.

## Official endpoints and source semantics
- NSE All Reports / Historical Index Data: https://www.nseindia.com/all-reports
- NSE India VIX historical data: https://www.nseindia.com/reports-indices-historical-vix
- Nifty Indices historical data: https://www.niftyindices.com/reports/historical-data
- PIB All Releases: https://www.pib.gov.in/AllRel.aspx?lang=1&reg=3
- MEA Advanced Search: https://www.mea.gov.in/advanced-search-list.htm

NSE historical data portals present CSV download controls. The portal UI's existence does not establish a successful download or a raw file hash. PIB pages supply Posted On date/time. MEA indexed results supply Published On date, but may omit time and direct document URL. Neither publisher's publication time should be conflated with event occurrence time.

## SHA-256 and repeated-download test policy
For unavailable files, SHA-256 is explicitly `NOT_COMPUTED`; no placeholder digest is permitted. Drift testing requires at least two successful independent retrievals of the same canonical URL and byte-level hashes, with retrieval timestamps retained. Revision testing requires two real, independently dated vintages or archive captures; a single current page cannot prove absence of revisions.

## Final decision
- benchmark_index: UNKNOWN / acquisition blocked.
- sector_indices: UNKNOWN / raw selected CSV not acquired.
- volatility: UNKNOWN / raw selected CSV not acquired.
- geopolitical_events: PARTIAL dated release sample; not complete event universe; raw-byte archive/hash not completed.
- repeated-download drift: NOT_TESTED for all groups.
- vintage-to-vintage revision ledger: NOT CREATED because no qualifying independent archived file pair was acquired.
- Factor Registry promotion: NOT AUTHORIZED.
- Hard Gate: BLOCKED.
- Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, 672 diagnostics: unchanged.
- Research spend: ₹0; no external contact; no merge/deployment.

## Next executable remediation
Run the bounded collector from the repository's GitHub Actions runner (which can reach official CSV endpoints if NSE allows it), with session warm-up, one request/second, two separate retrievals per URL, raw response preservation, HTTP status/content-type validation, SHA-256, and a fail-closed artifact manifest. For PIB/MEA, crawl the exact date filters and store each canonical HTML/PDF response with source-stated publication precision, retrieval time and SHA-256. Only compare vintages when archive capture timestamps or dated source releases are independently established.
