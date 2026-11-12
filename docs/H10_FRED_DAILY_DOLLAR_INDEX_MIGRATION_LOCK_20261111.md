# H.10 to FRED migration and daily dollar index source lock
Date: 2026-11-11
Scope: source migration/identity audit. No production change. No observations ingested.

## Why this audit was necessary
The previous audit treated the Federal Reserve DDP "Build Your Package" route as the intended full-history acquisition path. The Federal Reserve's H.10 page now states that during the week of 2026-11-09 the Build Your Package feature is being removed ahead of DDP retirement, and directs users to FRED for expanded download options. The preformatted DDP CSV packages are explicitly "Last 10 Obs" and must not be mistaken for full-history data.

Official evidence:
- Federal Reserve H.10 release / migration notice: https://www.federalreserve.gov/Releases/H10/
- Federal Reserve DDP Choose page: https://www.federalreserve.gov/datadownload/Choose.aspx?rel=H10
- Federal Reserve DDP Build page (removal notice): https://www.federalreserve.gov/datadownload/Build.aspx?rel=H10
- Federal Reserve H.10 feed (includes migration notice and historical corrections): https://www.federalreserve.gov/feeds/h10.html

## Locked FRED daily series identifiers
| Purpose | FRED ID | Official series label | Source | Frequency | Unit | Verified date range |
|---|---|---|---|---|---|---|
| Broad USD pressure | DTWEXBGS | Nominal Broad U.S. Dollar Index | Board of Governors / H.10 via FRED | Daily | Index Jan 2006=100 | 2006-01-02 to 2026-11-06 |
| Advanced economy USD pressure | DTWEXAFEGS | Nominal Advanced Foreign Economies U.S. Dollar Index | Board of Governors / H.10 via FRED | Daily | Index Jan 2006=100 | Daily series; exact latest table date to be captured at raw download |
| Emerging market USD pressure | DTWEXEMEGS | Nominal Emerging Market Economies U.S. Dollar Index | Board of Governors / H.10 via FRED | Daily | Index Jan 2006=100 | 2006-01-02 to 2026-11-06 |

Official FRED pages:
- Broad: https://fred.stlouisfed.org/data/DTWEXBGS
- Advanced: https://fred.stlouisfed.org/series/DTWEXAFEGS
- Emerging: https://fred.stlouisfed.org/data/DTWEXEMEGS

The FRED daily rates category confirms all three current daily indexes share the 2006-01-02 start date and update weekly after the H.10 release. The Federal Reserve releases daily rates/indexes for the previous business week on Mondays (normally 4:15 p.m. ET). Do not treat the weekly release cadence as weekly observations: the series observations are daily business-day values.

## Corrected interpretation / prior audit clarification
- DDP "Last 10 Obs" packages are previews, not full-history files.
- The DDP custom Build route is in retirement/removal; do not build a new collector dependency on it.
- Use the FRED-hosted Board of Governors series pages/data tables as the public download route, with the FRED series IDs above. FRED is the distribution interface; the underlying source remains Board of Governors H.10.
- DTWEXBGS is not ICE DXY. Do not label it DXY.
- Keep broad, AFE and EME indices separate. They are not capital flows.
- FRED states observations can be revised; preserve retrieval/vintage snapshots rather than overwriting.

## Acquisition protocol for the next ingestion run
For each series independently:
1. Retrieve the full table/export, not a chart preview or last-10-observation package.
2. Save untouched raw bytes.
3. Record exact download URL and all date/export parameters, retrieval UTC, last observation date, file size, media type, row count and SHA-256.
4. Parse DATE and VALUE only after raw hash capture; preserve original rows and any missing-value markers.
5. QA unique dates, monotonic date ordering, valid numeric values, start/end dates, missing values, and overlap consistency across the three series.
6. Keep a separate source_vintage_id for each retrieval; FRED values are subject to revision.
7. No forward fill and no synthetic calendar rows.

## Gate status
- DDP retirement/migration issue identified: PASS.
- FRED source identity for Broad/AFE/EME: PASS.
- Full raw daily export downloaded in this audit: NO.
- SHA-256 / raw-byte manifest: NOT DONE.
- Row-level QA: NOT DONE.
- India USD/INR alignment: NOT DONE.
- Global capital flow measurement: NOT ESTABLISHED.
- Overlay Milestone 6 actual observation ingestion: remains 0%.
- Overlay overall milestone progress: remains 62.5% (5/8); no increase is warranted by source migration alone.

## Project invariants
Research-only. ₹0 spend. Public official sources only. No paid API or credentialed endpoint. No synthetic observations, fabricated timestamps, forward-fill, or unsupported source promotion. No changes to Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 x 12), Engines A-E, or Hard Gate. No production integration without explicit approval.
