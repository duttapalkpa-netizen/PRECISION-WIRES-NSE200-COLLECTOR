# IMF BOP_AGG raw-data acquisition attempt — 2026-11-17

Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch: research/global-capital-rotation-overlay-v1
Parent PR: #20 (OPEN / UNMERGED; research-only)
Scope: one bounded attempt to acquire the official BOP_AGG payload after the source/methodology checkpoint. This is a blocker record, not a data-ingestion PASS.

## Attempt and observed result
- Official dataset landing page: https://data.imf.org/Datasets/BOP_AGG
- Page identifies BOP_AGG as annual, released each November, BPM6, and states that world/country-group aggregates combine reported data with estimates for nonreporting economies.
- The page's rendered text exposes VIEW DATA and DOWNLOAD controls but the text extraction does not expose a concrete download URL or downloadable file reference. No raw bytes were obtained through this route.
- Official API link from the dataset page: https://portal.api.imf.org/apis
- Following the API link redirected to the IMF API developer portal sign-in page. Anonymous data API access was therefore not demonstrated in this attempt.
- A third-party redistributor/mirror surfaced in discovery, but it is not an IMF-hosted endpoint. It is excluded from the official-only ingestion path and no mirror data was downloaded or admitted.

## Status
| Check | State |
|---|---|
| Official dataset identity and methodology | PASS (prior checkpoint; reconfirmed on landing page) |
| Official page download control visible | PASS |
| Direct official download URL exposed by text extraction | NOT_EXPOSED |
| Official raw workbook/API response acquired | NOT_DONE |
| Raw byte count / retrieval timestamp / SHA-256 | NOT_DONE |
| Financial Account > Portfolio Investment transaction series mapping | UNKNOWN |
| Units, sign convention, geography, release vintage QA | UNKNOWN |
| Value admitted to em_portfolio_flow_usd_bn | NO |
| Overlay gate / overall completion percentage advanced | NO |

## Fail-closed handling
- Do not substitute IIP positions for BOP transactions.
- Do not treat the IMF EMDE grouping as MSCI EM.
- Do not use third-party mirrors as official-source evidence.
- Do not infer a series, unit, sign, release vintage, or observation from the landing page.
- Keep this annual aggregate as a potential strategic context input only; it is not a daily swing signal.
- No production code, selector, ranking, CORE-672, Engines A-E, or PR merge changed.

## Next acceptable acquisition route
Use the official IMF portal's interactive DOWNLOAD control in a real browser session, capture the actual resulting file and final IMF-hosted URL, or obtain documented anonymous API access from IMF's own portal. Preserve exact downloaded bytes, UTC retrieval timestamp, byte count, SHA-256, request/export metadata, and release vintage before parsing. If access requires credentials, stop and leave this source NOT_DONE rather than bypassing authentication.

## Evidence links
- Official dataset page: https://data.imf.org/Datasets/BOP_AGG
- Official API portal: https://portal.api.imf.org/apis
- Official IMF explanatory notes: https://data.imf.org/-/media/Explanatory-Notes-November-2025-BOPSY.pdf
