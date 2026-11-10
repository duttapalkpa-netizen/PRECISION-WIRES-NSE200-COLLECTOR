# M6 Official WPI Source Feasibility & Series Boundary Audit — 2026-11-11

## Outcome

**PASS — official source and series coverage identified.**
**PARTIAL — monthly file download links and raw observation payload have not yet been captured.**
**NO INGESTION CLAIMED.**

## Primary official source

Office of the Economic Adviser (OEA), DPIIT, Ministry of Commerce & Industry:
- Current WPI/PPI index-file catalogue (base 2022-23): https://eaindustry.nic.in/download_data_2223.asp
- Historical WPI index-file catalogue (base 2011-12): https://www.eaindustry.nic.in/download_data_1112.asp
- WPI press-release archive: https://eaindustry.nic.in/wpi_press_release_archive.asp
- OEA homepage: https://eaindustry.nic.in/

## Verified coverage and release rules

Official current catalogue states:
- WPI (base 2022-23): monthly index files from April 2023 onwards.
- OPPI (base 2022-23): monthly index files from April 2023 onwards.
- Trial IPPI: March 2026 onwards, experimental and manufacturing-only.
- Service PPI: quarterly from Q1 FY 2023-24 onwards.
- Latest two months for WPI, OPPI and Trial IPPI are provisional; determine exact provisional months from the monthly press release.
- Latest quarter for Service PPI is provisional.

Official historical catalogue states:
- WPI (base 2011-12): monthly index files from April 2012 onwards.
- Historical catalogue also provides annual average monthly indices by calendar year (2013 onwards) and financial year (2012-13 onwards).

## Series-boundary controls

- Base 2011-12 and base 2022-23 are distinct index series and must not be concatenated as if they shared one base.
- April 2023 is the first month shown for the 2022-23 series; the older 2011-12 series remains separately available from April 2012.
- Do not splice or backcast the two series without a documented official linking factor or an explicit rebasing methodology.
- Preserve the published reference month, release/publication date, provisional/final status, series base, index type, and source file identity separately.
- WPI is a goods-price index; it does not cover services (as described in OEA WPI FAQ).
- WPI manual states provisional indices are released about two weeks after reference month and finalized after around eight weeks/two months. For current operational status, the specific OEA monthly press release controls.

## Retrieval attempt

Search-indexed official catalogue was accessible and its coverage notes were captured. Direct open of the download catalogue returned a gateway 502 from the retrieval interface. This is not an HTTP status observed from an underlying WPI file endpoint and does not establish that the OEA site is down.

No exact monthly workbook/CSV URL, download timestamp, raw bytes, or SHA-256 was obtained in this task. No observations were downloaded or ingested.

## M6 source-register decision

- Official owner/source: VERIFIED (OEA, DPIIT, Government of India).
- Monthly WPI availability: VERIFIED for both base series.
- Current base and coverage start: VERIFIED (2022-23, April 2023 onwards).
- Historical base and coverage start: VERIFIED (2011-12, April 2012 onwards).
- Provisional/final policy: VERIFIED at catalogue/manual level; exact month status must be read from each release.
- Exact direct download URL: UNKNOWN.
- Observation payload / SHA-256: NOT_CAPTURED.
- Macro-Geo factor admission: BLOCKED pending retrieval, schema QA, release-vintage checks and series-boundary treatment.

## Next action

Obtain the direct official monthly index file link from the OEA catalogue using a normal browser session or a directly exposed page link. Download one small, latest finalized month first; record exact URL, UTC retrieval time, file size, SHA-256, sheet/column schema, reference month and release vintage. Reconcile it against the matching official press release before expanding the historical panel.

## Safety / invariants

₹0 spend; free official source only; no paid feeds, no login circumvention, no synthetic data, no fabricated timestamps, no silent series splice. No production integration. Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 and Engines A–E unchanged.
