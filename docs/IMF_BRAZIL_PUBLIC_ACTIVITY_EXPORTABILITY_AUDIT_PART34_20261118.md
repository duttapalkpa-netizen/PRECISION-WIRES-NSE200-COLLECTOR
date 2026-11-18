# IMF Brazil — Public activity UI and transaction exportability audit (Part-34)
Date: 2026-11-18

## Purpose
Test whether IMF SDMX Central's public Data Registrations history and SDMX Transactions pages provide a directly extractable BR1 chronology in the available public web representation, without authenticated write actions or assumptions.

## Fresh official public-page observations

### A. Data Registrations history
URL: https://sdmxcentral.imf.org/activity/data-log.html
The current public page identifies itself as "Data Registrations" and says it shows historical activity for provision agreements. It exposes four breakdown modes:
- Breakdown By Provision Agreement
- Breakdown By Dataflow
- Breakdown By Data Provider
- Show All Data Registrations

The detail table fields are Date, Data URL, Action, Data Store and Series. The selected Registration Details panel exposes Data URL, Provision URN, Dataflow URN, Data Provider URN and User.

However, the web-rendered snapshot currently contains an empty Agency/Id/Version selection table and "No data available in table" (0 rows). The page is interactive/dynamically populated; the extracted HTML snapshot does not provide the filtered BR1 rows, event dates, PA URN or download payload. This is an extraction limitation, not evidence that no registrations/events exist.

### B. SDMX Transactions
URL: https://sdmxcentral.imf.org/activity/activity-log.html
The public page exposes a selected date range, Transaction Time, Transaction Type, Action and a "Download Transaction" control. Current extracted page snapshot:
- selected period: 2025-07-06 through 2026-11-18
- table reports 100 entries, with visible latest sample events on 2026-10-08 and 2026-09-09, all shown as Structure Submission / Replace.
- Search-engine extracted table sample also contains older Structure Submission Replace/Delete rows.
- No BR1, Brazil, BOP6 or BOP_BPM6 event was exposed in the returned snapshot.
The page is bounded/paginated and interactive. No conclusion about absence of Brazil events is permitted. No transaction download bytes were returned.

### C. Public Provision Agreement listing
URL: https://sdmxcentral.imf.org/data/provisionAgreements.html
The public listing exposes agency/id/name/version and a detail panel with URN, URL, Revisions, Description, Annotations, Valid From and Valid To; it also provides References, Changelog, Export SDMX-ML 3.0, Export Excel, Compare and View Provision Agreement controls.
The extracted first page is sorted to ESTAT and early IMF rows (e.g. Austria, Belgium, Bulgaria); it does not surface the Brazil PA in the returned first-page sample. No specific Brazil PA URN or revisions were obtained from this extraction.

### D. Current registration cross-check
URL: https://sdmxcentral.imf.org/data/registrations.html
The fresh public listing again shows:
- Dataflow `IMF:BOP6(1.0)`
- Data Provider `IMF:BR1`
- BCB source URL `https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml`
- Last Updated `2026-10-26T11:47:29.000Z`

The same listing contains many providers on `IMF:BOP6(1.0)` and many other providers on `IMF:BOP_BPM6(1.0)`. The registry therefore treats these as distinct Dataflow identifiers in the current registration list; this does not establish equivalence/aliasing or explain the BR1 XML's prior BOP_BPM6 declaration.

## Decision
- Public Data Registrations history interface existence and exposed fields: PASS.
- Public SDMX Transactions interface and download control existence: PASS.
- Public Provision Agreement detail/changelog controls existence: PASS.
- BR1 filtered history rows / transaction export bytes captured: NOT_DONE.
- Brazil PA URN and changelog captured: NOT_DONE.
- Chronology: BLOCKED / NOT_DONE.
- Current BR1 registry row as IMF:BOP6(1.0): OBSERVED.
- Prior BCB XML as IMF:BOP_BPM6(1.0): prior byte-captured project evidence.
- Dataflow equivalence or explicit alias: NOT_PROVEN; mismatch remains CONFIRMED / UNRESOLVED.

## Exact next action requiring interactive UI access
In an ordinary browser session, open Data Registrations history, select "Breakdown By Data Provider", select Agency IMF and Provider BR1, then export/capture all returned rows and registration details. Separately use SDMX Transactions with a date range covering the available full history and download transaction records; filter downloaded records by BR1, BCB source URL, Brazil PA URN, and either Dataflow URN. In Provision Agreements, locate the Brazil PA and capture its URN, revisions, Valid From/To, references and changelog. Archive original downloads and hashes. If UI requires login for the necessary history, record the access boundary; do not attempt write actions or use credentials not supplied by the user.

## Guardrails
No event timestamps inferred from Last Updated. No missing event inferred from empty static extraction. No registration mutation, POST, external contact, credentials, paid APIs, production integration or merge. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
