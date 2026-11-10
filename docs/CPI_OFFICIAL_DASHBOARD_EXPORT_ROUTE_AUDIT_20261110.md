# CPI Official Dashboard Export Route Audit — 2026-11-10

## Scope
Determine whether the public MoSPI CPI product dashboard's visible XLSX download can be accepted as the CPI 2024 back-series artifact, and prevent a false-positive data-ingestion claim.

## Evidence
1. MoSPI CPI product dashboard:
   https://www.mospi.gov.in/themes/product/9--
   Search-indexed official page shows a dashboard with separate "Chart download PDF • 3.9 MB" and "Data download XLSX • 396 KB" controls.
   The accessible rendered page did not expose the XLSX target URL, workbook bytes, sheet names, reference-period coverage, series identifier, or data vintage.
2. MoSPI NMDS, section 3.5:
   https://mospi.gov.in/sites/default/files/CPI/National_Metadata_Structure_for_CPI.pdf
   Explicitly states CPI 2024=100 back-series January 2013–December 2024 is available on e-Sankhyiki.
3. MoSPI/PIB answer dated 29 July 2026:
   https://www.pib.gov.in/PressReleasePage.aspx?PRID=2291051&lang=1&reg=1
   Explicitly confirms All-India General indices and inflation for Rural, Urban and Combined, January 2013–December 2024, are available on e-Sankhyiki.
4. e-Sankhyiki CPI catalogue:
   https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI
   Accessible catalogue result exposes only 1–10 of 495 records and current monthly tables, including CPIMCY26004AUG (August 2026 All India Combined General level index and inflation). This is a current-month table, not evidence of the back-series dataset ID.
5. e-Sankhyiki FAQ:
   Search result confirms catalogue datasets are downloadable in Excel and product-page filtered Macro Indicator datasets in CSV; registration is not required. This describes platform capabilities, not the contents of this particular XLSX.

## Decision
- Official existence of CPI 2024 back-series and its scope: PASS.
- Official product dashboard exposes an XLSX download control: PASS (page-level evidence only).
- XLSX download target and bytes retrieved: UNKNOWN / NOT RETRIEVED.
- XLSX identified as the January 2013–December 2024 back-series: UNKNOWN.
- Do NOT accept the 396 KB dashboard XLSX as the back-series without inspecting workbook metadata and contents.
- Do NOT substitute current-month table CPIMCY26004AUG for the back-series.
- A third-party mirror for Combined General index was discovered but excluded from ingestion and acceptance because this project requires free official primary-source artifacts only; it is not evidence of the Rural/Urban/Combined official workbook.

## Next action
From the official e-Sankhyiki CPI Macro Indicator UI, select the Back Series dataset (not current CPI monthly table), export the filtered dataset as CSV, and preserve raw bytes, exact source page/table identifier, selection parameters, retrieval timestamp, byte size and SHA-256. Alternatively use the official catalogue's matching Back-Series Excel statement after locating its table ID. If the browser route does not expose it, request a user-provided official export; do not infer the download URL.

## Controls
No observation request made, no raw CPI rows ingested, no hash invented, no paid service, no external contact. No changes to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or Hard Gate. UNKNOWN remains neither PASS nor FAIL. This route audit does not increase CPI ingestion, Milestone 6, overlay, or overall V11.3 progress.
