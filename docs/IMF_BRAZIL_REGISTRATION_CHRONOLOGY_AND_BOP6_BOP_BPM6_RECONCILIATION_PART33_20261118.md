# IMF Brazil — Registration chronology and BOP6/BOP_BPM6 reconciliation (Part-33)
Date: 2026-11-18

## Executive decision
This audit narrows the apparent mismatch but does NOT fully resolve either acceptance blocker. Do not mark Brazil registration chronology PASS and do not equate the two Dataflow IDs.

## 1. Critical semantic clarification: Dataflow ID is not DATA_DOMAIN
The IMF SDMX Central Web Services Guide (last updated May 2025) contains a worked BOP example in which:
- Dataflow = `IMF:BOP_BPM6(1.0)`
- DataStructure = `IMF:ECOFIN_DSD(1.0)`
- DATA_DOMAIN = `BOP6`

The guide shows this combination in its workbook example (PDF lines 220-249). It separately shows DATA_DOMAIN=BOP6 as a dimension value (lines 169-180 and 294-315). Therefore the string BOP6 can legitimately appear as a dimension/domain code while the Dataflow ID is BOP_BPM6. A parser or reconciliation routine MUST NOT compare a DATA_DOMAIN value with a Dataflow URN as if they were the same field.

Source: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf

## 2. What the current IMF registry evidence says
The current IMF SDMX Central public Registrations page lists the Brazil provider row:
- Dataflow: `IMF:BOP6(1.0)`
- Data Provider: `IMF:BR1`
- URL: `https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml`
- Last Updated: `2026-10-26T11:47:29.000Z`

Source: https://sdmxcentral.imf.org/data/registrations.html

The previously byte-captured BCB XML in this project declared Dataflow `IMF:BOP_BPM6(1.0)`. The IMF constraints listing separately enumerates constraints targeting `BOP6[1.0]` and `BOP_BPM6[1.0]`, which is evidence these are distinct registry Dataflow identifiers, not interchangeable strings:
https://sdmxcentral.imf.org/data/constraints.html

Thus:
- Confusion between DATA_DOMAIN=BOP6 and Dataflow BOP_BPM6 is RESOLVED as a semantic false-positive risk.
- The actual registry Dataflow BOP6 vs BCB XML Dataflow BOP_BPM6 discrepancy remains CONFIRMED / UNRESOLVED pending the exact live BCB XML bytes and registry structure crosswalk. Same DSD, shared dimensions, or similar labels do not establish alias/equivalence.
- No Dataflow renaming, remapping, or registration mutation is authorized by this audit.

## 3. Official registration-history surface found
The public IMF SDMX Central interface exposes:
- SDMX Transactions: https://sdmxcentral.imf.org/activity/activity-log.html
- Data Registrations history: https://sdmxcentral.imf.org/activity/data-log.html

The data-log page explicitly offers breakdown by Provision Agreement, Dataflow, Data Provider, and Show All Data Registrations. Its detail panel exposes Date, Data URL, Action, Data Store, Series, Provision URN, Dataflow URN, Data Provider URN and User.

The transaction log page exposes a selected date period, Transaction Time, Transaction Type, Action and Download Transaction. The currently indexed snapshot shows a bounded table (100 entries) and the sample rows surfaced are Structure Submission events, not a complete BR1 registration history. The public page's extracted snapshot did not return Brazil registration rows. Therefore no Brazil chronology is inferred from this absence.

## 4. Access limitation and official service contract
The IMF SDMX Central Web Services Guide specifies the registration service endpoint:
`https://sdmxcentral.imf.org/ws/secure/sdmxapi/rest`
Access: Private (admin / agency / data provider for the Provision Agreement), POST; authenticated submission. This is a write/registration endpoint, not a public history-export endpoint. Do not send POST requests or attempt changes.

The public history UI exists, but the current available web extraction did not expose the interactive filter results or downloadable transaction payload. No exact Brazil registration event timestamps, action sequence, PA URN history, or registration ID history were captured.

Official source: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf (section 7.1, lines 1276-1297 and section 7.3-7.5).

## 5. Required evidence to close both blockers
A. Registration chronology:
- Export the IMF SDMX Central Data Registrations history filtered to provider `IMF:BR1` and/or the Brazil PA, plus the relevant SDMX Transactions download covering the full available history.
- Preserve each row's event time, action, Dataflow URN, Provider URN, Provision Agreement URN, Data URL, Registration ID, transaction/event ID and user if exposed.
- Obtain the exact Brazil PA detail/revisions or official change log. Record time zone and export retrieval time separately.
- Compare earliest create/insert, subsequent replace/re-register, delete/recreate, and current state. Do not treat current Last Updated as original creation time.

B. Dataflow discrepancy:
- Capture the exact current BCB XML response bytes from the registered URL, including HTTP status, response headers, retrieval timestamp and SHA-256.
- Inspect the Dataflow URN in the XML header/structure and any explicit Dataflow reference/alias annotations.
- Retrieve official IMF structures for both `IMF:BOP6(1.0)` and `IMF:BOP_BPM6(1.0)`; compare DSD URN, constraints, annotations, valid-from/to and version lifecycle.
- Only close as resolved if an official crosswalk/alias/revision record proves equivalence OR if BCB/IMF registry records establish a corrected registration and the live XML matches it. Otherwise retain a confirmed discrepancy.

## 6. Status
- DATA_DOMAIN=BOP6 versus Dataflow=BOP_BPM6 semantic distinction: PASS (documented in IMF guide).
- Registry current BR1 row observed as Dataflow IMF:BOP6(1.0): PASS (public registry snapshot).
- BCB XML previously observed as Dataflow IMF:BOP_BPM6(1.0): PASS as prior byte-captured project evidence; current response bytes not recaptured in this audit.
- BOP6 and BOP_BPM6 as equivalent Dataflow IDs: NOT_PROVEN; discrepancy remains CONFIRMED / UNRESOLVED.
- Brazil registration/PA chronology: BLOCKED / NOT_DONE.
- Full registration-history export and transaction event reconciliation: NOT_DONE.
- No production integration, registration mutation, paid API, external contact, or credentials requested.
- Brazil Reconstruction remains INCOMPLETE / BLOCKED. UNKNOWN is not PASS.

## Guardrails
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. No merge without explicit approval. No synthetic data or guessed timestamps.
