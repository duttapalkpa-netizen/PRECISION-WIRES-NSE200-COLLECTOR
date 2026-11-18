# Brazil Reconstruction — Official IMF Registration Timestamp Semantics and Evidence Gate (Part 23)
Date: 2026-11-18
Status: RESEARCH-ONLY / INCOMPLETE / BLOCKED

## New authoritative evidence
1. The live official IMF SDMX Central Registrations table currently lists:
   - Dataflow: IMF:BOP6(1.0)
   - Data Provider: IMF:BR1
   - URL: https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml
   - Last Updated: 2026-10-26T11:47:29.000Z
   Source: https://sdmxcentral.imf.org/data/registrations.html
2. The IMF SDMX Central Web Services API Guide (last updated May 2025), section 7.2, explicitly states that selecting an existing registration and using "Re-Register" updates the "Last Updated" timestamp. Therefore the current listing timestamp is NOT evidence of the original create time and cannot be used as the event timestamp for Brazil chronology.
   Source: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
3. The same guide, section 7.1, describes the registration endpoint as private, with access for admin/agency/data provider associated with the Provision Agreement. Section 7.2 says registration via the UI requires login. The guide's documented REST interface is for submitting registration requests, not a public unauthenticated historical audit-log retrieval endpoint. No public official read API for Brazil's complete PA/registration history has been established in this audit.
4. The official guide's section 7.3 identifies the SDMX registration message as containing the action, Provision Agreement, Dataflow, provider and SimpleDataSource URL. The actual Brazil event package must retain those exact fields from original IMF records; they cannot be reconstructed from the current listing alone.
5. Official IMF SDMX Central public RSS documentation describes notifications for transactions and links to underlying SDMX documents. Prior audit already retrieved and checked a bounded 33-item window with no Brazil marker; this bounded negative result does not establish full historical absence.

## Reconfirmed mismatch
- Registration table: IMF:BOP6(1.0) for IMF:BR1.
- Previously byte-captured BCB XML payload: IMF:BOP_BPM6(1.0).
- The IDs differ. Same DSD is not an equivalence proof. No automatic normalization is allowed.
- Current registration row is current-state evidence only. It does not identify the original registration date or whether a later Replace/Re-Register operation changed the current state.

## Acceptance decision
Brazil Reconstruction remains INCOMPLETE / BLOCKED.
- Current registry row identity: PASS (current state only).
- Current BCB payload identity: PASS (prior archived capture).
- Dataflow mismatch: CONFIRMED / UNRESOLVED.
- Last Updated interpreted as original registration time: REJECTED.
- Brazil-specific historical registration event records: NOT_DONE.
- PA historical revision/changelog: NOT_DONE.
- Create/Replace/Delete/Re-Register chronology: UNKNOWN.
- Event-to-current-state reconciliation: BLOCKED.
- Parser offline unit suite: PASS (16/16 in GitHub Actions Run #21).
- Formal offline XSD validation and complete XSD byte archive/hash manifest: NOT_DONE.

## Exact external evidence dependency
The next required evidence is an official IMF SDMX Central export or capture of the Brazil-specific Data Registrations / Activity / Registration Details and exact Provision Agreement history, containing for every relevant event:
- original event XML or official CSV export;
- transaction date/time and action exactly as displayed;
- Dataflow URN, Data Provider URN, Provision Agreement URN and Data URL;
- event/registration identifier where supplied;
- PA revision/changelog rows and their dates;
- retrieval source and raw-file SHA-256.

The public registration page and current BCB payload cannot supply these historical rows. The user/repository owner must sign in to the official IMF SDMX Central interface (if authorized) and export the Brazil-filtered history/PA details, or obtain the same primary export from the authorized provider. Do not request or share passwords. No undocumented endpoint, guessed transaction ID, RSS ordering, or Last Updated timestamp may substitute.

## Work that remains independently actionable
- Complete official SDMX-ML 2.1 XSD dependency closure, byte archive, SHA-256 manifest and offline XSD validation once raw schema files can be captured reproducibly.
- Do not mark Brazil Reconstruction complete until the primary historical event and PA records are reconciled and the Dataflow mismatch is resolved by authoritative evidence.

## Guardrails
₹0 spend; official/free sources only. No synthetic historical records, inferred timestamps, paid APIs, production integration, PR merge or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
