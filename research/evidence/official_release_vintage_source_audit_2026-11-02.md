# Official Release / Vintage Evidence Audit — 2026-11-02

Status: research-only evidence register. This document does not promote any source to AVAILABLE and does not alter production logic, the selector, RANKING_SCORE, +1 PRESSURE_FADE, or the 672 diagnostic signals.

## Findings and fail-closed classifications

| Domain | Official evidence located | What it proves | What it does not prove | Required status |
|---|---|---|---|---|
| RBI DBIE Report 217 / Table 180 | https://systemhealth.rbi.org.in/Scripts/PublicationsView.aspx_id%3D22654%281%29.html | A published Table 180 page is dated 2024-09-13 and contains month-end SGL transaction yields by tenor. | No per-observation publication timestamp; a page date or DBIE loaded_at is not an observation-level RELEASED_AT. This monthly SGL curve is not the daily FBIL 10Y par-yield benchmark. | PARTIAL / RELEASE_AT_UNKNOWN |
| CGA monthly accounts | https://cga.nic.in/Content/Print/Advance-Release-Calendar.aspx ; https://cga.nic.in/Page/Monthly-Accounts-Review.aspx ; https://cga.nic.in/MonthDashboardReport/Published/list.aspx | Calendar describes expected dissemination on the last day of the month following the reference month (March by 31 May); CGA dashboard provides monthly account data and warns that data are subject to update/correction/revision. | Calendar date is scheduled, not actual publication timestamp. Current dashboard update is not a historical vintage record. | PARTIAL / HISTORICAL_VINTAGE_UNVERIFIED |
| GDP | https://esankhyiki.mospi.gov.in/catalogue-main/catalogue | Official e-Sankhyiki catalogue provides released statement datasets and release metadata. | Catalogue access alone does not establish a complete continuous historical GDP series or a complete release-vintage history. New-base back-series availability must be checked by statement and period. | PARTIAL / SERIES_COMPLETENESS_TO_VERIFY |
| CPI | https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI ; https://www.mospi.gov.in/uploads/latestreleasesfiles/1770893247472-Press%20Relase%20of%20CPI%20for%20Jan26.pdf | Catalogue provides reference period, release date, table ID and provisional/final labels. MoSPI Jan-2026 CPI release FAQ describes CPI 2024 access and back-series for Jan-2013 to Dec-2024. | CPI 2012 and CPI 2024 observations must not be silently concatenated; base/methodology and linked back-series provenance must remain explicit. | PARTIAL / SERIES_BREAK_PRESERVED |
| WPI | https://eaindustry.nic.in/wpi_press_release_archive.asp ; https://eaindustry.nic.in/download_data_2223.asp ; https://eaindustry.nic.in/press_release/press_release_202606.pdf | OEA archive has monthly press releases; item-wise index files are available from Apr-2023 for base 2022-23; latest two months are provisional. A June-2026 release contains an embargo time and states March-2026 final / May-2026 provisional. | Monthly item files and press releases do not, by themselves, provide item-level revision deltas or a complete vintage-by-vintage history for every item. | PARTIAL / ITEM_REVISION_HISTORY_UNVERIFIED |

## Ingestion rules

1. Preserve source URL, retrieval timestamp, source publication date/time precision, reference period, table/report identifier, base year, release status, and file SHA-256 independently.
2. Never synthesize a timestamp from a calendar date, file modified time, HTTP crawl time, DBIE loaded_at, or current page last-updated value.
3. For RBI Table 180, retain observation RELEASED_AT as null/UNKNOWN unless an authoritative per-observation release record is found. Do not map it to daily FBIL 10Y yield.
4. For CGA, store scheduled release date separately from observed actual publication timestamp. Keep historical vintage as unverified until archived dated files or trustworthy publication logs establish versions.
5. For GDP/CPI, ingest every officially released statement/table and record base, frequency, reference period, release date, release status and table ID. Do not interpolate missing historical periods or collapse different base series.
6. For WPI, archive every monthly item file and release PDF as a distinct vintage; compute item-level revision deltas only by comparing files for the same item/reference period across archived vintages. If an earlier vintage is absent, mark revision history UNKNOWN.
7. All source gaps remain UNKNOWN, not FAIL and not PASS. No source is promoted to AVAILABLE based solely on this document.

## Required next collection tasks

- RBI: obtain dated original DBIE release notices or immutable archived report versions for each observation period; verify whether publication time is actually available at observation granularity.
- CGA: recover dated historical monthly report files and their first-publication evidence; compare file versions by reference month.
- GDP/CPI: enumerate and download all e-Sankhyiki statements/series, reconcile overlapping base periods, and build release-vintage keys without fabricating continuity.
- WPI: collect each monthly item-level workbook/CSV and corresponding press release for every available month; produce per-item revision ledger with explicit missing-vintage flags.
- Rebuild one immutable snapshot only after manifests and source QA are complete; then audit all 35 factor groups on that exact snapshot and run regression/hard-gate checks.

## Guardrails

Research-only. No production changes, no deployment, no merge. Maintain ₹0 spend and use public official sources only. Hard Gate remains BLOCKED until all required P0 evidence and matured validation windows pass.
