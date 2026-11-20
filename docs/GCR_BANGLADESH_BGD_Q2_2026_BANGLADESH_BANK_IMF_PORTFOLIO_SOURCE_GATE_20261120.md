# Bangladesh (BGD) Q2 2026 Bangladesh Bank–IMF Portfolio Source Gate
Date: 2026-11-20
Status: BLOCKED / NOT PASS — national publication exposes portfolio net balance only; no national dual-leg component split validated.

## Preflight and selection
- Preflighted current Master Continuity Ledger, GCR priority queue, ARG detail report, MEX detail report and IMF BOP panel report. Completed PASS work excluded.
- ARG's exact public revision closure remains unavailable: INDEC page lists the live BOP SDMX-ML archive, but the XML endpoint is served as text/xml which the browser reader rejects; the official Datos Argentina quarterly CSV resource link timed out. No evidence that these endpoints contain a historical vintage/change log. Do not repeatedly retry the same failed routes.
- Advanced to BGD from the existing 12-country exact-key IMF receipt. No new IMF GET, sample rebuild, or cohort rebuild.

## Existing immutable IMF receipt
- Workflow run 44474458684; artifact 14505009889; ZIP SHA-256 588101c0deff3b4310984dae5eabcac64fc8288f4416854b7676b4b6ff6b4cd7.
- BGD A_NFA_T raw CSV: 4,976 bytes; SHA-256 67b7d5a7460fa096a85471b597fe7be5893576e5bbf01a0481acf40bee043106.
- BGD L_NIL_T raw CSV: 5,045 bytes; SHA-256 de54a736d8cb3975c62a3fe762354921057555dbda830df7f5b8aacf609aafe0.
- Exact Q2 2026 IMF values: A_NFA_T = USD 0; L_NIL_T = USD -113,334,678.0510731 (-113.3346780510731 USDm).
- Both observations identify IMF.STA:BOP(21.0.0), P_F, USD, quarterly, period 2026-Q2. The zero asset observation is a reported numeric zero, not missing; retain it as zero only for this source receipt, with no imputation.

## Official national source
- Bangladesh Bank Quarterly, Vol. XXIII, No. 4, Table V.1 “Balance of Payments”, unit million USD:
  https://www.bb.org.bd/pub/quaterly/bbquarterly/bangladesh%20bank%20quarterly%2C%20%20vol%20xxiii%2C%20no%204.pdf
- Table includes FY26 Q4 portfolio investment (net) = -109 USDm. Fiscal-year quarter alignment: Bangladesh FY26 Q4 corresponds Apr–Jun 2026 (calendar Q2 2026); however this is the aggregate portfolio balance only.
- Table V.1 does not disclose portfolio asset net acquisition and liability net incurrence as separate component rows. It therefore cannot independently validate both IMF legs or establish their signs/concepts. Do not derive the missing legs from the IMF values.
- The table is not by itself a dated vintage comparison for the Q2 observation; its title/edition is Vol XXIII No.4. Exact release date and revision status of the Q2 portfolio row were not established in the captured source.
- Bangladesh Bank Quarterly earlier Vol XXII No.4 also publishes portfolio investment as a net total, confirming that this publication family is not a dual-leg source in the retrieved tables:
  https://www.bb.org.bd/pub/quaterly/bbquarterly/bangladesh%20bank%20quarterly%2C%20%20vol.%20xxii%2C%20no.%204_09112025.pdf

## Acceptance matrix
- Existing IMF exact-key receipt and raw hashes: PASS.
- Bangladesh Bank official Q2-period portfolio net row: PASS (aggregate only).
- Calendar Q2 ↔ FY26 Q4 period alignment: PASS (period mapping).
- National asset net acquisition: NOT_AVAILABLE in retrieved table.
- National liability net incurrence: NOT_AVAILABLE in retrieved table.
- Country-specific sign/concept bridge for two IMF legs: NOT_ESTABLISHED.
- Same-vintage bridge: NOT_ESTABLISHED.
- BGD full national dual-leg validation: BLOCKED / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## Exact next action
Find a Bangladesh Bank official detailed BOP table or SDDS/metadata series that separately reports portfolio investment financial assets and liabilities for FY26 Q4, including source publication/vintage date and sign convention. Do not use the portfolio net total to back-solve either leg. If no such official breakdown is published, preserve BGD BLOCKED and move beyond the fixed 12-country sample only with an authorized cohort expansion.

## Protected invariants
No cross-country aggregation, netting, imputation, forward-fill, synthetic observations, inferred split of net total, silent sign transform, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.


## 2026-11-20 — Bangladesh NSDP machine-readable BOP source route audit
- Official Bangladesh Bank NSDP page explicitly lists Balance of Payments with three separate actions: Browse Data, Download in SDMX, and DSBB Metadata. This establishes a designated official machine-readable national BOP publication route beyond the quarterly PDF table.
- Exact official links exposed by the page:
  - NSDP landing page: https://www.bb.org.bd/econdata/nsdp/nsdp_bb.php
  - BOP Browse Data: https://www.bb.org.bd/econdata/nsdp/browsefile/bpm6_bgd.xls
  - BOP SDMX download: https://www.bb.org.bd/econdata/nsdp/xml/bgd/bop6_bgd.xml
  - BOP Alternate Presentation SDMX: https://www.bb.org.bd/econdata/nsdp/xml/bgd/bopanltcl_bgd.xml
  - IMF DSBB BOP metadata: https://dsbb.imf.org/e-gdds/dqaf-base/country/BGD/category/BOP00
- Retrieval boundary: web reader rejects the XLS MIME and XML MIME (400 unsupported content-type); direct container download of BOP6 XML also failed. The BOP Alternate Presentation XML likewise was not parsed. No raw bytes, retrieval timestamp, content length, HTTP headers, hash, SDMX observation values, dimensions, or revision attributes were captured. Do not describe the SDMX route as successfully downloaded or inspected.
- The official NSDP page confirms that BOP data are offered in SDMX, but does not itself prove that the XML includes separate portfolio asset and liability flows, or that it contains historical vintage metadata. Therefore BGD remains BLOCKED / NOT PASS; national asset/liability legs and same-vintage bridge remain NOT_ESTABLISHED; aggregate NOT_AUTHORIZED.
- This is a material source-route discovery and bounded technical access test, not a numerical validation. No repeated retries of the same MIME-blocked URLs are authorized without a supported byte-preserving retrieval mechanism.
- Sources: Bangladesh Bank NSDP page, lines 2–19 and 34–35; official BOP Browse and SDMX endpoints linked from that page. IMF DSBB BOP metadata link is listed by Bangladesh Bank.
- Next exact action: use a supported transfer route to capture the official `bop6_bgd.xml` or `bpm6_bgd.xls` bytes and hash; inspect structure/series keys first, then only if both portfolio asset/liability legs exist, extract FY26 Q4 values, units, sign conventions and vintage attributes. Do not back-solve the net-only PDF total.


## 2026-11-20 — Bangladesh Bank annual BPM6 component/sign crosswalk (historical only)
- Inspected the official Bangladesh Bank publication `Balance of Payments & International Investment Position of Bangladesh — Annual 2024–25`: https://www.bb.org.bd/pub/annual/bop/bop%2024-25.pdf (PDF title page identifies Annual 2024–25; statistical tables are in Chapter Four).
- Table 11, “Bangladesh financial account transactions”, unit million BDT, separately reports portfolio investment (net), assets and liabilities for each quarter of FY2024–25. Portfolio rows:
  - FY25 Q1 (Jul–Sep): net -607; assets 0; liabilities +607.
  - FY25 Q2 (Oct–Dec): net +6,889; assets 0; liabilities -6,889.
  - FY25 Q3 (Jan–Mar): net +6,487; assets 0; liabilities -6,487.
  - FY25 Q4 (Apr–Jun): net +3,996; assets 0; liabilities -3,996.
  - FY25 full year: net +16,765; assets 0; liabilities -16,765.
- Identity across these rows: portfolio net = asset net acquisition − liability net incurrence. Example FY25 Q4: 0 − (−3,996) = +3,996. The table therefore exposes a country-specific historical component mapping; it is not the target FY26 Q4 observation.
- Bangladesh Bank methodology (section 1.1) states a credit entry records a decrease in foreign financial asset holdings or increase in foreign financial liabilities; debit records an increase in foreign financial assets or decrease in foreign financial liabilities; net positions deduct debits from credits. In the financial-account table's directional asset/liability presentation, the separate component rows are consistent with A_NFA_T and L_NIL_T signed directions, and portfolio balance is assets minus liabilities. This is a historical sign/concept crosswalk only; no FY26-Q4 sign assumption is applied until the current-period detailed source is captured.
- Critical limitation: the annual publication ends at FY2024–25. It does not provide FY2025–26 Q4 / calendar 2026-Q2 values, a dated Q2-2026 vintage, or a revision bridge. The NSDP XML/XLS raw files remain uninspected due MIME/transfer restrictions. No Q2 2026 numerical comparison is made.
- Updated acceptance: historical Bangladesh portfolio component/sign crosswalk PASS for FY2024–25; current Q2 2026 national asset and liability observations NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; BGD full dual-leg validation remains BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Sources: official PDF title and contents pages; methodology lines 266–272; Table 11 lines 2872–2903; portfolio-liability description and figures lines 3129–3145. Browser source references: turn738669view1, turn391275view1, turn391275view2, turn391275view0.
- Next exact action: obtain FY2025–26 annual BOP statistical table or Q4 FY26 quarterly detailed table from Bangladesh Bank with separate portfolio asset/liability rows, units, publication date and revision status. Do not substitute FY25 values for FY26 Q4.


## 2026-11-20 — Q4 FY26 quarterly net-only recheck and IMF sign-identity exception
- Re-opened the official Bangladesh Bank Quarterly, April–June 2026, Volume XXIII No.4, Table V.1 (PDF pp.74–75). The table labels FY26 Q1–Q4 as provisional (`P=Provisional`) and reports portfolio investment net: FY26 Q1 -45, Q2 -59, Q3 -10, Q4 -109 USDm; FY26 annual -223 USDm. The target calendar 2026-Q2 corresponds to FY26 Q4 (Apr–Jun), and its national net-only value remains -109 USDm. This source is the direct official quarterly publication, not a separate-leg table.
- Reused the pre-existing IMF exact-key sample (run 44474458684, artifact 14505009889; no new IMF retrieval). Existing Q2 values: A_NFA_T = 0 USD; L_NIL_T = -113,334,678.0510731 USD = -113.3346780510731 USDm.
- Diagnostic only: applying the historical Bangladesh Bank Table 11 identity `portfolio net = assets − liabilities` mechanically to IMF legs gives +113.334678 USDm, while the official FY26 Q4 national net-only row is -109 USDm. Absolute difference is 222.334678 USDm and signs oppose. This is a material sign/concept/source-vintage exception, NOT a validated national dual-leg comparison. It may reflect a distinct presentation/sign convention or unreconciled source/vintage; do not silently flip either IMF leg or use this net value to back-solve.
- Quarterly table says FY26 values provisional; no exact publication timestamp or historical revision bridge captured in the table. Annual data HTML also exposes 2025-26P aggregate annual BOP data but not the missing portfolio legs.
- Updated acceptance: official FY26 Q4 national portfolio net-only value PASS; national two legs NOT_AVAILABLE; historical FY25 component/sign crosswalk PASS only for FY25; cross-vintage/net identity check REVIEW / FAIL_DIAGNOSTIC; same-vintage NOT_ESTABLISHED; BGD dual-leg validation BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Sources: official Bangladesh Bank Quarterly PDF title/date lines 0–4; Table V.1 lines 3997–4042; provisional status lines 4058–4059; official annual BOP page https://www.bb.org.bd/en/index.php/econdata/bop_yearly/1. Web references: turn144302view0, turn797000view0, turn269023search0.
- Next exact action: inspect the Bangladesh Bank official FY26 quarterly BOP detailed SDMX/XLS or a dated revision/vintage source that exposes separate portfolio asset and liability legs; prioritize resolving the opposite-sign net identity. Until then keep BGD blocked and aggregate unauthorized.


## 2026-11-20 — Primary PDF reinspection: FY26 portfolio series, period labels and publication provenance
- Re-opened the exact official Bangladesh Bank Quarterly PDF (April–June 2026, Vol XXIII No.4): https://www.bb.org.bd/pub/quaterly/bbquarterly/bangladesh%20bank%20quarterly%2C%20%20vol%20xxiii%2C%20no%204.pdf. Official publication index lists this edition as published 2026-11-15: https://www.bb.org.bd/en/index.php/publication/recent_publications/annual/feidportal/.
- Re-read Table V.1 directly (PDF printed page 74; web extraction lines 3997–4042). It labels columns FY25R, FY26P, FY25 Q2/Q3/Q4, FY26P Q1/Q2/Q3/Q4; unit million USD. Portfolio investment row is FY25 -138, FY26 -223, FY25 Q2 -57, Q3 -53, Q4 -33, FY26 Q1 -45, Q2 -59, Q3 -10, Q4 -109. Therefore calendar 2026-Q2 = Bangladesh FY26 Q4 = -109 USDm; FY26 annual provisional = -223 USDm. Source note at lines 4058–4059 defines P=Provisional and R=Revised.
- This primary PDF table reports only the portfolio net row. It does not expose separate portfolio assets and liabilities. Other rows in the same table do separately split DMBs and NBDCs (lines 4031–4033) and reserve assets (4037–4039), confirming that those are distinct subcomponents and must not be misidentified as portfolio investment legs.
- Publication provenance cross-check: Bangladesh Bank recent-publications index records the April–June 2026 Bangladesh Bank Quarterly entry on 2026-11-15. The PDF title confirms period and Volume XXIII No.4. No document revision timestamp or earlier-vintage snapshot is stated in the extracted table; Q4 FY26 remains provisional.
- IMF sample remains the same previously archived receipt; no new IMF query. The prior +113.334678 USDm calculation remains only a conditional diagnostic under a historical FY25 identity, not a proven FY26 mapping. Because the FY26 primary PDF supplies no portfolio legs or explicit sign bridge, the opposite-sign diagnostic is retained as REVIEW / FAIL_DIAGNOSTIC, not a validated reconciliation.
- Acceptance unchanged: national FY26 Q4 net-only row PASS; national portfolio legs NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; BGD dual-leg BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Web evidence: PDF title/edition lines 0–4; Table V.1 lines 3997–4042; P/R legend lines 4058–4059; publication index turn152279search1. Detailed PDF ref turn720212view0 / parent turn315186view0.
- Next exact action: pursue a supported official Bangladesh Bank NSDP/BPM6 dataset capture that exposes the two portfolio legs; the quarterly PDF is conclusively net-only for this item, so do not re-parse it or use its DMB/NBDC rows as portfolio legs.


## 2026-11-20 — Bangladesh Bank portfolio survey publication-scope audit (alternative source ruled out for Q2 flow)
- Inspected Bangladesh Bank Statistics Department's official Survey Forms page: https://www.bb.org.bd/aboutus/dept/stat/surveyforms.php. It defines portfolio investment asset-side holdings as resident-owned securities issued by non-residents, and liability-side holdings as resident-issued securities owned by non-residents. Custodian banks and domestic end-investors report the relevant holdings. The page explicitly states PI survey data are reported on a calendar-year basis.
- Inspected the official `Foreign Direct Investment and External Debt — July–December 2025` publication, Chapter III, Portfolio Investment. It states annual PI data span 2010–2025; methodology says compilation through NITA for BoP/IIP, PI-1 returns from authorized dealer bank branches within 15 days following the reference month, and coverage includes inflows, outflows, purchase, sale and stock. Published chapter tables, however, present annual 2023–2025 stock position, 2025 capital-market transactions and NITA flows, plus end-December stock positions in Bangladesh and abroad; they do not publish a quarterly FY26 Q4 asset/liability transaction pair.
- This resolves a source-route ambiguity: the survey's asset/liability definitions are useful for conceptual mapping, but the publicly available PI survey publication is annual/calendar-year and stock/transaction summary oriented. It cannot be used as a substitute for missing FY26 Q4 BPM6 BOP legs. Do not treat end-Dec 2025 stock changes, NITA inflow/outflow, purchases/sales or 2025 survey totals as Q2 2026 asset/liability flows.
- Official Bangladesh Bank annual BOP webpage separately confirms FY2025–26P portfolio investment net = -223 USDm, consistent with quarterly Vol XXIII No.4 FY26P annual row; it still reports only portfolio net, while its DMB/NBDC assets/liabilities are a different functional category and not portfolio legs.
- NSDP BOP SDMX route remains designated on official NSDP page; direct XML/XLS byte capture still NOT_DONE. Alternate Presentation browse route rejected by site; alternate XML remains MIME-blocked. No repeated attempts.
- Acceptance: survey asset/liability definitions PASS (concept only); annual publication scope PASS; FY26 Q2 separate national PI legs NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; BGD full dual-leg validation BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Sources: Bangladesh Bank Survey Forms page (portfolio definition and calendar-year frequency); official July–December 2025 FDI/External Debt report Chapter III, Table 1 and methodology, PDF pp.17–20; annual BOP page 2025–26P net PI -223. Web refs: turn614019view0, turn105604view0, turn503512view1, turn503512view0. No source provides Q2 2026 national dual-leg values.
- Next exact action: pursue only an official NSDP/BPM6 SDMX or XLS raw-byte capture route that can reveal the FY26 Q4 portfolio asset/liability observations and vintage attributes. If a supported byte-preserving route remains unavailable, keep BGD blocked and advance to next eligible country; do not reuse the annual PI survey publication for quarterly flow validation.


## 2026-11-20 — Bangladesh Bank open-data / monthly BOP alternate-route boundary audit
- Reopened Bangladesh Bank Open Data Initiative page: https://www.bb.org.bd/en/index.php/econdata/index. It states the Monthly Economic Trends Excel is free, monthly updated and includes detailed BOP indicators; a historical Excel dataset extends to 1972 and is yearly updated. Direct click on the official workbook `https://www.bb.org.bd/pub/monthly/econtrds/statisticaltable.xlsx` was rejected by the browser reader as unsupported XLSX MIME; a direct byte-preserving container download also failed. Historical workbook `https://www.bb.org.bd/econdata/time_series_data1972-2024.xlsx` was likewise rejected by reader. No workbook bytes, retrieval headers, content length or hash were captured.
- Reopened official Bangladesh Bank BOP monthly page: https://www.bb.org.bd/en/index.php/econdata/bop. Its current displayed table covers FY2025-26R July-Sep, FY2026-27R July-Aug and FY2026-27P July-Sep. Portfolio investment is shown only as `net` (-45, -54, -69 USDm respectively); DMB/NBDC and reserve categories have separate assets/liabilities but are distinct functional categories. These are not FY2026-Q2 portfolio legs. Do not misclassify or back-solve.
- Official BOP monthly PDF search result likewise shows PI net only; it does not offer portfolio asset/liability legs. Official IIP time-series workbook/PDF is position/stock data, not quarterly transaction flows, and cannot be used as a substitute.
- This is a bounded alternative-route audit, not a dual-leg validation. Open Data Excel route discovery PASS; byte capture NOT_DONE. Monthly BOP public table scope PASS (PI net-only); FY26 Q4 separate national PI legs NOT_AVAILABLE; same-vintage NOT_ESTABLISHED; BGD dual-leg BLOCKED / NOT PASS; aggregate NOT_AUTHORIZED.
- Sources: Bangladesh Bank Open Data page lines 101–104 and BOP category lines 189–195; official monthly BOP table lines 109–169; monthly BOP search result; official IIP series search result. Web refs: turn963386view0, turn590064view2, turn898847search25, turn898847search24. XLSX MIME rejection: turn590064view0 and turn590064view1; direct container download of statisticaltable.xlsx failed. No raw file content/hash claimed.
- Next exact action: no further retries of the same XLSX or MIME-blocked NSDP links. If no newly supported byte-preserving route becomes available, close BGD source-access attempts as BLOCKED and advance to the next country in the existing 63-country dual-leg cohort using already archived IMF observations and a different national-source route.
