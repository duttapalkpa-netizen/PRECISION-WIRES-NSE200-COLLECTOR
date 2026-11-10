# CPI Back-Series Availability and Retrieval Route Reconciliation — 2026-11-10

## Purpose
Reconcile the prior unresolved CPI 2024=100 back-series acquisition path using the newly located official MoSPI National Metadata Structure (NMDS), CPI 2024 first press release, FAQ and e-Sankhyiki API/catalogue pages.

## New official evidence
1. MoSPI National Metadata Structure for CPI:
   https://mospi.gov.in/sites/default/files/CPI/National_Metadata_Structure_for_CPI.pdf
   - Section 3.5 explicitly states that CPI data on back series from January 2013 to December 2024 with base year 2024=100 is available on the e-Sankhyiki portal.
   - It distinguishes this from the old CPI 2012 series, which remains available through the CPI warehouse.
2. MoSPI first CPI 2024 press release, 12 February 2026:
   https://mospi.gov.in/uploads/latestReleases/latest_release_1770891893893_6b458c0a-c327-4fef-a554-41131ea67273_Press_Relase_of_CPI_for_Jan26.pdf
   - Pages 9–10 state that the released back-series comprises All-India General indices for Rural, Urban and Combined, January 2013–December 2024, and annual inflation January 2014–December 2024.
   - Published general-level linking factors: Rural 0.5222, Urban 0.5320, Combined 0.5267.
   - Formula uses the ratio of 2025 annual geometric-average new-series to old-series CPI.
   - Direct linking is restricted to General Index level because CPI 2024 adopts COICOP-2018 while CPI 2012 uses a different classification.
3. MoSPI CPI 2024 FAQ:
   https://mospi.gov.in/uploads/documents/documents/1770891066052-Annexure_V.pdf
   - FAQ Q35–Q36 confirms the e-Sankhyiki access route and the same back-series publication scope.
4. e-Sankhyiki CPI API documentation:
   https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api
   - Endpoint GET /api/cpi/getCPIData; API 2.0.0 / OpenAPI 3.0; paginated JSON envelope; optional bearer token; per-IP rate limiting.
   - The page advertises relative schema document ../../layout/swagger_user_cpi.yaml.
5. e-Sankhyiki CPI catalogue:
   https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI
   - Current catalogue view exposes dated 2024-base tables (e.g. All India Combined General table CPIMCY26004AUG for August 2026), but the accessible first page did not expose the 2013–2024 back-series table ID or download URL.

## Retrieval attempt
- Resolved candidate schema URL: https://esankhyiki.mospi.gov.in/layout/swagger_user_cpi.yaml
- The retrieval tool returned an access/retrieval error. This is not evidence the official file does not exist.
- No guessed API request was sent; no query parameters were fabricated.
- No workbook/CSV bytes were retrieved in this pass.

## Gate status
- Official existence and e-Sankhyiki availability of CPI 2024 back-series: PASS (NMDS).
- Back-series period and sector scope: PASS (NMDS, FAQ and press release).
- General-level linking formula/factors/scope: PASS (press release).
- Exact e-Sankhyiki catalogue table ID / file URL: UNKNOWN.
- OpenAPI YAML contents and exact request schema: UNKNOWN / retrieval blocked.
- Raw observations, monthly completeness, revision vintage and SHA-256: UNKNOWN / NOT RETRIEVED.
- Independent recomputation of linking factors: BLOCKED pending unrounded 2025 series inputs.

## Safe next action
Use the e-Sankhyiki CPI product UI and its authorized table/download workflow to locate the specifically described CPI 2024 back-series table (2013-01 through 2024-12), then save the original XLSX/CSV and record its source table ID, URL, retrieval timestamp, byte size and SHA-256. If the table UI or download route is inaccessible, obtain an official user export. Only after raw-file verification should parsing and completeness checks begin.

## Invariants and progress accounting
No synthetic observations, guessed source IDs, guessed query parameters, fabricated timestamps or hashes. UNKNOWN is neither PASS nor FAIL. No paid API/service, no external contact, no production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E or Hard Gate changes. This route reconciliation is not observation ingestion and does not increase CPI ingestion, Milestone 6, overlay or overall V11.3 progress.
