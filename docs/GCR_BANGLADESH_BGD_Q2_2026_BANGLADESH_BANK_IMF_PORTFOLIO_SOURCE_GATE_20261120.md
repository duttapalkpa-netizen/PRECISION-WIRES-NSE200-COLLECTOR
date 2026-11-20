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
