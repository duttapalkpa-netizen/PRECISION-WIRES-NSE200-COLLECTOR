# IMF Brazil public GUI cross-check — Part 14
Date: 2026-11-18 (Asia/Kolkata)
Workstream: PRECISION-WIRES V11.3 / গবেষণা যাচাই অব্যাহত 36

## Objective
Independently cross-check the Part-13 Brazil Provision Agreement evidence against the currently indexed official IMF SDMX Central public GUI pages, and determine whether those public page renderings expose revision history or transaction-level chronology without an authenticated interactive session.

## Official page evidence inspected
1. Provision Agreements page: https://sdmxcentral.imf.org/data/provisionAgreements.html
   - The current public page rendering identifies the page as “Provision Agreements”.
   - It exposes a Provision Agreement Details panel with References, Changelog, Export SDMX-ML 3.0, Export Excel, Compare and View Provision Agreement controls.
   - The page also exposes detail fields URN, URL, Revisions, Description, Annotations, Valid From and Valid To.
   - The static page extraction does not show a selected Brazil PA row or populated details for URN IMF:BR_BOP_BP6(1.0). The presence of the controls is evidence of UI capability, not evidence of Brazil's actual revision/changelog content.
2. Registrations page: https://sdmxcentral.imf.org/data/registrations.html
   - Current search-index rendering lists the row IMF:BOP6(1.0), provider IMF:BR1, and the exact BCB URL:
     https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml
   - The same rendered row shows Last Updated 2026-10-26T11:47:29.000Z.
   - This independently corroborates the current registration tuple already established in prior work. It does not provide the original registration event, transaction ID, action, initial creation date, or PA revision chronology.
   - The page's static extraction exposes Registration Details fields (Registration ID, Registered URL, Dataflow, Data Provider, Registration Type), but no historical row log or event payload in the extracted page.
3. Official SDMX Central User Guide and Web Services Guide remain the previously documented basis for the distinction between current registration state and registration event documents. No undocumented REST endpoint was inferred or queried in this part.

## Reconciliation
- Current registration row (IMF:BOP6(1.0), IMF:BR1, BCB URL, Last Updated): CONFIRMED by public page rendering; corroborates prior evidence.
- PA identity and explicit PA -> Dataflow BOP6 / Data Provider BR1 references: CONFIRMED by Part-13 raw XML evidence; this part does not repeat the large PA downloads.
- PA page has Changelog/Revisions/Compare/View controls: CONFIRMED as UI affordances.
- Actual selected Brazil PA revisions/changelog contents: NOT_OBSERVED.
- PA-to-BCB URL relation: NOT_ESTABLISHED by the PA XML examined in Part-13 or by this static page rendering.
- Brazil-specific historical registration rows and original transaction XML/CSV: NOT_DONE.
- Create/Replace/Delete/Re-Register chronology: UNKNOWN.
- BOP6 vs BOP_BPM6 payload mismatch: CONFIRMED / UNRESOLVED.
- Brazil/EM admission and market use: BLOCKED / NOT_AUTHORIZED.

## Access and evidence boundary
The web extraction is a static rendering. It does not execute the PA table selection, open Changelog/Compare/View for the target URN, or download a selected historical transaction. No login, credentials, or authenticated actions were attempted. Therefore it would be incorrect to claim that the selected Brazil PA's changelog was empty, inaccessible, or required login. The actual interaction outcome remains UNKNOWN.

## Exact next closure dependency
An authorized owner-side interactive session must select URN IMF:BR_BOP_BP6(1.0), export or capture its Revisions/Changelog/Compare/View details, and select the IMF:BR1 registration history row to export its dated transaction SDMX-XML/CSV. Preserve original download bytes, source URL, retrieval timestamp, and SHA-256. If the UI requires authentication or the export is not available to the owner, supply the official exported files; do not share credentials.

## Safety / scope
No parser changes, no workflow run, no full NSE collector, no RSS/BCB repeat download, no production integration, no PR merge, no macro weights, no Brazil/EM admission, and no spend. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 x 12), and Engines A-E remain unchanged. UNKNOWN is not PASS.

## Sources
- IMF Provision Agreements: https://sdmxcentral.imf.org/data/provisionAgreements.html
- IMF Registrations: https://sdmxcentral.imf.org/data/registrations.html
