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
