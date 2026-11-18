# গবেষণা যাচাই অব্যাহত 36 — Part-5: IMF SDMX Transactions Activity
Date: 2026-11-18

## Objective
Use the newly identified official IMF SDMX Transactions activity view to advance Brazil registration-history reconstruction without repeating archived RSS transaction downloads.

## Official evidence observed
Source: https://sdmxcentral.imf.org/activity/activity-log.html
- The page labels columns Transaction Time, Transaction Type and Action, and exposes a Download Transaction control.
- Search-indexed rendering exposed a bounded 18-row sample, each labelled Structure Submission, with Replace/Delete actions. Visible timestamps:
  - 2026-10-08T19:03:23Z
  - 2026-09-09T14:58:26Z, 14:58:09Z, 14:57:52Z, 14:57:34Z, 14:56:47Z, 14:56:17Z, 14:53:19Z, 14:52:28Z, 14:51:22Z
  - 2026-08-24T22:13:56Z
  - 2026-07-28T19:29:14Z
  - 2026-06-24T15:39:26Z (Delete)
  - 2026-06-22T22:13:42Z
  - 2026-05-15T15:40:43Z, 15:38:59Z, 15:38:04Z (Delete), 15:37:08Z
- The rendered text simultaneously says “Showing 1 to 2 of 100 entries”; this inconsistency means the 18-row sample is not considered complete and no exhaustive count/pagination claim is made.
- Static page extraction shows table headers and Download Transaction control but no row payload/IDs. It also exposes Login and confirmation/re-authentication dialogs. No credentials were used.
- The visible rows do not identify agency, dataflow, provider, Provision Agreement or Brazil URL. They are generic Structure Submission records and cannot be attributed to Brazil.
- FMR View Activity documentation states a transaction can represent a structure/group of structures/data registration; Download Transaction provides SDMX-XML and View Details can provide a CSV log. This is product capability documentation, not evidence that any visible row is Brazil-related. Source: https://fmrwiki.sdmx.io/12.5.0/user/fmr/ViewActivity/

## Reuse / non-duplication
- Did not repeat the archived 33 RSS transaction downloads or BCB XML retrieval.
- Did not invent a transaction ID, infer a Brazil match from timestamp alone, or call an undocumented endpoint.
- Available static extraction did not expose selectable row identifiers or downloadable transaction bytes.

## Acceptance matrix
| Item | Status |
|---|---|
| Official SDMX Transactions page located | PASS |
| Transaction Time / Type / Action schema confirmed | PASS |
| Bounded visible timestamp sample captured | PASS (sample only) |
| Brazil-specific transaction identified | NOT_DONE |
| Brazil transaction SDMX-XML / CSV log downloaded | NOT_DONE |
| Brazil Provision Agreement URN / chronology resolved | UNKNOWN |
| BOP6 vs BOP_BPM6 mismatch | CONFIRMED |
| Brazil admission / EM aggregation / market use | BLOCKED / NOT_AUTHORIZED |

## Next action
Use the official interactive SDMX Transactions GUI with an authorized session if required: select a transaction row, invoke Download Transaction or View Details, and inspect returned SDMX-XML/CSV for exact IMF:BR1, BCB URL, BOP6/BOP_BPM6 and Provision Agreement identifiers. Do not infer from timestamps. If login is required, the repository owner must perform the GUI action and provide the downloaded XML/CSV. Until then chronology stays UNKNOWN.

## Guardrails
₹0; free official sources only. No fabricated timestamps, guessed transaction IDs, undocumented endpoints or synthetic data. Brazil remains BLOCKED. Macro Overlay remains deferred until Brazil Reconstruction is evidence-backed closed. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is not PASS.
