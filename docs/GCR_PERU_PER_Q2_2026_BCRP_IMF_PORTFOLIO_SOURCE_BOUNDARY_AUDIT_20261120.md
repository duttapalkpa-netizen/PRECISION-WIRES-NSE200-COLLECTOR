# Peru (PER) Q2-2026 — BCRP official portfolio-source boundary audit
Date: 2026-11-20 (Asia/Kolkata)
Decision: PER selected from the fixed 63-country Q2-2026 dual-leg cohort after repository search found no dedicated PER Q2-2026 national portfolio-flow reconciliation report. Existing IMF raw rows were extracted, but no exact Q2-2026 BCRP national portfolio asset/liability transaction pair was independently retrieved from an accessible official BCRP publication in this bounded audit. PER national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## Continuity and duplicate rejection
- Re-fetched Master Continuity Ledger, GCR Priority Queue and fixed 63-country cohort before selection.
- PER is present in the fixed cohort. The cohort and IMF panel were reused; no rebuild or new IMF query.
- GitHub search for PER Q2-2026 portfolio source/reconciliation found no dedicated PER report. Prior country validations and completed IMF panel QA were not repeated.

## Existing IMF raw archive — exact Q2 rows
- Asset raw file: docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv
  - Git blob SHA: 15449e87c9057291a1f52f2f8cd9805df55f9fb8
  - Exact PER row: `dataflow,IMF.STA:BOP(21.0.0),R,PER,A_NFA_T,P_F,USD,Q,2026-Q2,1999155686.69433,6,6,,,,,,,,,,,,O,,,,true,,`
- Liability raw file: docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv
  - Git blob SHA: 15f379dc42e2760eb5f2384618e48f5ddc3177f1
  - Exact PER row: `dataflow,IMF.STA:BOP(21.0.0),R,PER,L_NIL_T,P_F,USD,Q,2026-Q2,1699664071.47559,6,6,,,,,,,,,,,,O,,,,,,`
- Both are USD, quarterly, 2026-Q2, SCALE=6, PRECISION=6, ACTION=R. Converted for display only: asset USDm 1,999.15568669433; liability USDm 1,699.66407147559. Preserve raw USD OBS_VALUE and scale; no inferred scaling beyond the recorded scale semantics.
- These are IMF observations only, not national validation.

## Official BCRP source boundary
1. BCRP “Indicadores Económicos — IV Trimestre 2025”: https://www.bcrp.gob.pe/docs/Estadisticas/indicadores-trimestrales.pdf
   - Official PDF currently exposes quarterly economic indicators through 2025-Q4, not Q2-2026. It includes a private-sector long-term capital flow table; the inspected official version is therefore stale for the requested Q2-2026 target.
2. BCRP statistical portal reference: https://www.bcrp.gob.pe/estadisticas.html
   - BCRP directs users to its statistics portal and historical statistical tables. No directly accessible Q2-2026 BCRP portfolio asset/liability transaction export was captured in this audit.
3. BCRP Note of Studies No. 59 / Macroeconomic Report — Second Quarter 2026:
   - Candidate official URL tested: https://www.bcrp.gob.pe/docs/Publicaciones/Notas-Estudios/2026/nota-de-estudios-59-2026.pdf
   - The web retrieval returned only an HTML iframe shell, not the official PDF contents. A third-party index exposes snippets attributed to the report, but those snippets are not accepted as official raw evidence and are not used for numeric admission.
   - The candidate report may contain sector-level balance-of-payments details, but portfolio-specific gross assets and liabilities, table/page, definitions, source vintage and raw file are NOT_INSPECTED. Do not infer or copy values from the third-party extract.
4. BCRP official historical quarterly indicator PDF: https://www.bcrp.gob.pe/docs/Estadisticas/indicadores-trimestrales.pdf
   - It contains private-sector financial account assets/liabilities and portfolio sub-lines, but latest available quarter in the inspected official PDF is 2025-Q4. It cannot validate PER 2026-Q2.
5. IMF Article IV staff report is not a substitute for the national primary source; its annual/projection BOP table is excluded from Q2-2026 transaction validation.

## Fail-closed acceptance
- Fixed cohort membership / IMF panel two-leg availability: PASS at panel level only (inherited cohort evidence).
- Existing IMF PER Q2-2026 exact raw row extraction: PASS.
- Official BCRP source family discovery: PASS.
- Official national Q2-2026 portfolio asset leg: NOT_EXTRACTED.
- Official national Q2-2026 portfolio liability leg: NOT_EXTRACTED.
- Official source bytes / retrieval receipt / SHA-256: NOT_CAPTURED.
- BCRP table-specific sign, BPM basis, portfolio component mapping and period/vintage alignment: NOT_ESTABLISHED.
- Numeric dual-leg comparison: NOT_DONE.
- PER national validation: PARTIAL / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## Next exact action
Obtain the official BCRP Note of Studies No. 59 (Q2-2026) PDF through a supported official download path or the BCRP statistics portal, archive exact raw bytes with retrieval metadata and SHA-256, then inspect the precise portfolio component table. Map national financial-account assets/liabilities separately to IMF A_NFA_T and L_NIL_T only after verifying BPM basis, sign convention, units, period, and publication vintage. If official PDF access remains unavailable, record BLOCKED and advance to the next eligible country; do not use third-party snippets or stocks as transaction flows.

## Invariants
No IMF re-query, no cohort rebuild, no third-party numeric admission, no IIP stock substitution, no netting, no FX inference, no synthetic/filled values, no aggregate admission, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.


## Continuation 54 addendum — official BCRPData series recovered (2026-11-20)

### Official portal and series identifiers
- BCRPData quarterly Financial Account page: https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/cuenta-financiera . It identifies private-sector financial-account series in USD million, quarterly from T1-2012 through T2-2026, last updated 20-Aug-2026; and separate public-sector financial-account series with the same period/update metadata. Official series page explicitly identifies the source sectors and series codes.
- Private-sector portfolio assets: series PN39278BQ, official result page https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/resultados/PN39278BQ/html ; T226 = 1,749 USDm.
- Private-sector portfolio liabilities: series PN39285BQ, official result page https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/resultados/PN39285BQ/html ; T226 = 279 USDm.
- Public-sector portfolio liabilities: series PN39404FQ, official result page https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/resultados/PN39404FQ/html ; T226 = 1,421 USDm.
- Public-sector series catalogue exposes a public-sector asset aggregate PN39402FQ but does not list a public-sector portfolio-asset subseries in the 25-series list. Therefore the complete national portfolio-asset leg remains unavailable from the inspected catalogue; do not substitute total public assets.

### Separate-leg comparison and scope control
- Liability leg: BCRP private + public sector portfolio liabilities = 279 + 1,421 = 1,700 USDm. Existing IMF raw PAK-equivalent PER L_NIL_T = 1,699.66407147559 USDm. Difference = +0.33592852441 USDm, within BCRP's whole-USDm published precision. This is a strong rounded numeric match, subject to definition and vintage checks.
- Asset leg: BCRP private-sector portfolio assets = 1,749 USDm only; IMF A_NFA_T = 1,999.15568669433 USDm. Difference against private-sector-only subtotal = -250.15568669433 USDm, but this is NOT a valid like-for-like discrepancy because the BCRP public-sector portfolio-asset component is not separately identified. Do not call it a failed full asset comparison and do not fill it with total public assets.
- No netting. Private and public sector liabilities are added only to reconstruct the national liability component, as separate non-overlapping sector series; they are not combined with asset series.

### Revised acceptance status
- BCRP official Q2-2026 source extraction: PASS for private assets, private liabilities and public liabilities; public portfolio-asset subcomponent NOT_AVAILABLE in inspected series catalogue.
- National liability leg: numeric comparison PASS at whole-USDm rounding (1,700 vs 1,699.664 USDm; residual +0.336 USDm).
- National asset leg: PARTIAL / NOT_DONE (private-sector component captured; full-sector portfolio-asset coverage not established).
- Full dual-leg national validation: PARTIAL / NOT PASS. Sign/definition crosswalk and same-vintage remain NOT_ESTABLISHED; BCRP series last updated 20-Aug-2026, while IMF raw observations only carry ACTION=R and no matching timestamp in the archived rows.
- BCRP series page provides official public values and series IDs but no raw API payload/bytes or retrieval receipt was archived in this bounded step; no raw-file SHA-256 is claimed.
- PER aggregate admission remains NOT_AUTHORIZED.

### Next exact action
- Inspect BCRPData API/developer documentation and the official public-sector asset series metadata to determine whether a portfolio-investment-specific public-sector asset flow series exists outside the 25-series list. Do not use public-sector total assets as a proxy. Then verify BCRP's BPM6 sign/sector definitions and any dated vintage history; if public-sector portfolio assets are not published, preserve the PER asset gate as UNKNOWN/PARTIAL and advance.


### Continuation 54 — BCRP API contract check
- Official BCRPData API developer guide: https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf . It documents GET series queries, up to 10 same-frequency series, output formats including JSON/CSV, and exact series-code/date-range URL structure (guide pp.2-5; updated 24-May-2022).
- Constructed one documented, single-period JSON GET for PN39278BQ-PN39285BQ-PN39404FQ, 2026-2/2026-2/ing. The web retrieval returned an internal access error; no raw API payload/receipt was acquired. Do not claim API download or raw-file hash. Previously inspected official HTML series pages remain the evidence for the three displayed values.
- API path remains an available documented retrieval contract but the exact endpoint access in this session is BLOCKED; do not repeatedly retry the same URL. Continue with HTML display evidence only, and keep the raw-byte archival gate open.


## Continuation 55 — BCRP public-asset catalogue closure and next-country handoff (2026-11-20)

### PER public-sector portfolio-asset series check
- Re-inspected the complete official BCRPData quarterly Financial Account catalogue: https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/cuenta-financiera . It lists 58 series: private sector 17, public sector 25, short-term capital 16. Public sector includes PN39402FQ aggregate Assets and PN39403FQ aggregate Liabilities, then detailed portfolio-liability series PN39404FQ onward; there is no public-sector portfolio-asset subseries in the full listed 25-series block.
- The public asset aggregate PN39402FQ is not portfolio-specific and is explicitly rejected as a substitute. Catalogue-based absence finding: PASS (within this official listed catalogue); all-source absence cannot be asserted.
- BCRPData API developer guide https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf documents GET/POST and CSV/JSON/XML/HTML formats, but prior exact API GET remained inaccessible. No raw API bytes or SHA-256 captured.
- PER status unchanged: BCRP source extraction 3 series PASS; liability numeric PASS (1,700 vs IMF 1,699.664 USDm, residual +0.336 within ±0.5); full asset coverage PARTIAL/NOT_DONE; sign/definition and same-vintage NOT_ESTABLISHED; full dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

### Next country selected: Nepal (NPL)
- Confirmed NPL is in the fixed 63-country cohort and found no dedicated NPL Q2-2026 national reconciliation report in the repo search performed in this continuation.
- NRB official External Sector page https://www.nrb.org.np/database-on-nepalese-economy/external-sector/ lists monthly Balance of Payments (BPM 6) and BPM 5 datasets, plus annual BPM6/BPM5 datasets. This is a viable official source family for calendar Q2 extraction from Apr–Jun 2026, subject to exact series/table availability and period alignment.
- Official BPM6 workbook link exposed by NRB page: https://www.nrb.org.np/contents/uploads/2026/09/Balance-of-Payments-BPM6.xlsx . Web retrieval refused XLSX MIME (400 unsupported content-type); workbook content not inspected. NRB July 2026 annual macro report is not accepted for quarterly portfolio legs. No use of central-bank balance-sheet investment stocks.
- NPL next exact action: retrieve the official NRB BPM6 workbook via an XLSX-capable route, inspect its period coverage and separate portfolio assets/liabilities rows for Apr–Jun 2026; verify monthly vs cumulative nature and units/signs. Reuse archived IMF exact rows only; no new IMF query. If the workbook has only net portfolio or no Q2 legs, keep NPL blocked/partial and move on.

### Evidence boundaries
- BCRP catalogue source: full official series list as inspected 20-Nov-2026; it establishes the listed catalogue's absence of a public portfolio-asset subseries, not universal absence from all NRB/BCRP data.
- NRB external-sector index and linked BPM6 XLSX are official source discovery only; XLSX contents NOT_INSPECTED, values NOT_EXTRACTED, no raw file hash claimed.
- No synthetic data, no stocks-as-flows, no netting, no inferred sign/scale, no cohort rebuild, no IMF re-query, no production changes.
