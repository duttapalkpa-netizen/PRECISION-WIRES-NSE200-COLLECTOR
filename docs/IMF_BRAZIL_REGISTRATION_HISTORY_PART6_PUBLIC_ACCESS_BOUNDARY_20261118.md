# গবেষণা যাচাই অব্যাহত 36 — Part-6: IMF SDMX public transaction access boundary
Date: 2026-11-18

## Objective
Resolve the next narrow question after Part-5: can the IMF SDMX Central transaction history and its Download Transaction / View Details controls provide Brazil-specific transaction evidence without an authenticated interactive session?

## New official-source checks
1. Official SDMX Transactions page: https://sdmxcentral.imf.org/activity/activity-log.html
   - Search-indexed page currently labels the view "Showing all transactions for the selected period" and displays date controls from 2025-07-06 to 2026-11-18.
   - It still exposes only the Transaction Time / Transaction Type / Action columns and a Download Transaction control in the rendered extract. The previously observed bounded 18-row sample is not a complete transaction listing: the same rendering says "Showing 1 to 2 of 100 entries". No row-specific transaction payload or Brazil identifier is exposed in the public extract.
2. Official IMF SDMX Central login page: https://sdmxcentral.imf.org/login.html
   - The page exposes username/password authentication and a login failure state. This confirms that an authenticated UI exists; it does not prove that every activity-log row or download requires login. No credentials were entered or tested.
3. Official IMF SDMX Central Web Services Guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
   - The guide explicitly says there is no official REST API for data-processing services such as validation, conversion or registration; FMR has a separate entry point. Therefore the standard structure REST API must not be misrepresented as a historical registration-event API.
4. Official IMF SDMX Central User Guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralUserGuide.pdf
   - The RSS feed is updated when a transaction occurs. The guide says transactions include structure additions/modifications/deletions and data registrations/deletions, and each RSS item links to an underlying SDMX RegistryInterface document containing a SubmitStructureRequest or SubmitRegistrationRequest.
   - This documents the RSS event model and explains why registration-specific evidence must be sought in the actual linked transaction document, not inferred from a generic timestamp or a structure-submission label.
5. Official search/export UI: https://sdmxcentral.imf.org/search.html
   - It explicitly warns that neither Data Registrations nor Metadata Sets may be downloaded through generic structure export. Do not use that export as a substitute for registration history.
6. Official Data Registrations activity view: https://sdmxcentral.imf.org/activity/data-log.html
   - It exposes provider/dataflow/provision-agreement breakdown modes and registration detail fields, but current public text extraction has no event rows. No Brazil event is evidenced.

## Findings and interpretation
- A public search/rendering route exposes transaction timestamps and generic action labels, but not row IDs, Brazil identifiers, or downloadable row content.
- The existence of a login page does not establish that all public history is private; the precise unresolved boundary is row selection/download behavior in an authenticated interactive session.
- Standard SDMX structure REST endpoints are not an official substitute for FMR registration-processing/history operations.
- The RSS feed is the documented public event-notification path. Previously archived 33 transaction records remain the bounded evidence set; they were not downloaded again in this step. The prior bounded result found no Brazil/IMF:BR1/BCB URL/BOP_BPM6 match within that sample only. No claim is made about events outside the sampled window.
- Generic structure export is explicitly unsuitable for Data Registrations.

## Acceptance matrix
| Item | Status |
|---|---|
| Official SDMX Transactions page and visible columns | PASS |
| Public page exposes Brazil-specific transaction detail | NOT_DONE |
| Anonymous row-level Download Transaction / View Details behavior | UNKNOWN (interactive behavior not verified) |
| Official REST registration-history API documented | NO — guide says no official REST API for registration processing |
| RSS event-document mechanism documented | PASS |
| Generic structure export as registration-history substitute | REJECTED |
| Brazil-specific transaction XML/CSV | NOT_DONE |
| Brazil historical chronology | UNKNOWN |
| BOP6 vs BOP_BPM6 mismatch | CONFIRMED |
| Brazil admission / EM aggregation / market use | BLOCKED / NOT_AUTHORIZED |

## Exact next action
Owner-side, authorized interactive check only: open the official SDMX Transactions page, select a dated row, test Download Transaction and View Details, and save the returned SDMX-XML/CSV. Inspect the actual payload for IMF:BR1, the BCB URL, BOP6/BOP_BPM6 and Provision Agreement URNs. If access requires login, the repository owner supplies only the exported file; never share credentials. If no Brazil row appears in the selected transaction window, record the exact filter/window and keep chronology UNKNOWN. Do not infer from timestamp alone.

## Reuse and guardrails
- No repeat RSS 33-item download, BCB XML download, or generic structure export.
- No guessed transaction IDs, undocumented endpoints, fabricated timestamps, synthetic data, or claims of exhaustive history.
- ₹0, official/free sources only. No production integration, PR merge, Brazil/EM admission or macro overlay weighting.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
