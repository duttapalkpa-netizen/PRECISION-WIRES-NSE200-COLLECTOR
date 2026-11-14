# IMF October 2025 BPM6 reporting document — retrieval and evidence-status audit

Audit date: 2026-11-15
Target document: "Economies Reporting on BPM6 Basis October 2025"
IMF publication date: 14 May 2026
Dataset association: Balance of Payments (BOP), International Investment Position (IIP)
Security classification: Public or Unrestricted
Content type: Manual
Format: PDF

## 1. What is verified

The official IMF Documents catalogue and the official IMF BOP dataset page both list the target document with the exact title, publication date, dataset association, public/unrestricted classification and PDF format.

Official catalogue:
`https://data.imf.org/en/Documents`

Official BOP dataset page:
`https://data.imf.org/Datasets/BOP`

Search-result metadata exposes the catalogue item identifier `1792656603400855000`.

## 2. What is not verified

The PDF binary and its complete country table were not retrievable through the available public page extraction in this audit. The catalogue landing page exposed the document metadata but not a direct PDF link or the document body. Therefore:
- no country row was read from the October 2025 table;
- no absence/presence conclusion is made for CAF, ERI, GNQ, SOM, TCD or TKM in this edition;
- no BPM6 BOP start date is assigned to any of the six;
- the April 2025 table result remains historical evidence only and is not silently carried forward.

This is an evidence-access limitation, not a failed country eligibility test.

## 3. Exact SDMX artefact limitation

The public IMF SDMX Central Structure Web Service page confirms the registry REST entry point:
`https://sdmxcentral.imf.org/sdmx/v2/`
and that the service can query Dataflows, Data Structures, Provision Agreements and related structural artefacts.

The public Reporting Constraints page lists `IMF:BOP6_CONSTRAINT` attached to `BOP6[1.0]` and `IMF:BOP_BP6_CONSTRAINT` attached to `BOP_BPM6[1.0]`. It does not establish that either applies to `IMF.STA:BOP(21.0.0)` / `IMF.STA:DSD_BOP(24.0.0)`.

A guessed REST path for the IMF.STA BOP dataflow returned inaccessible through the page retrieval interface; it is not treated as proof that the artefact is absent. No Provision Agreement or Data Provider identity was identified and no provider-level constraint was resolved.

## 4. Evidence table

| Question | Evidence status |
|---|---|
| October 2025 BPM6 document exists in official IMF catalogue | VERIFIED |
| Publication date is 14 May 2026 | VERIFIED |
| Document is public/unrestricted PDF | VERIFIED |
| PDF body retrieved and inspected | NOT_RETRIEVED |
| Six country rows checked in October 2025 table | NOT_DONE |
| Exact IMF.STA:BOP dataflow constraint identified | UNKNOWN |
| Applicable Provision Agreement identified | UNKNOWN |
| Applicable Data Provider identified | UNKNOWN |
| Provider-level constraint resolved | UNKNOWN |
| Six-country formal eligibility | UNKNOWN |

## 5. Next retrieval procedure

Use the official IMF catalogue item's identifier `1792656603400855000` to obtain the PDF's actual download/content URL from the IMF document metadata or browser download action; then preserve the downloaded PDF and SHA-256, inspect all pages including continuation pages, and transcribe only the BOP start-date column for the six exact country codes. In parallel, use the SDMX Central REST structure service UI to select Structure Type = Dataflow, Agency = IMF.STA (if present), Structure ID = BOP, Version = 21.0.0; retrieve its references, then follow only actual returned Provision Agreement and Data Provider references. Do not guess artefact IDs or reuse BOP6 constraints.

## 6. Gate decision

- Official catalogue metadata verification: PASS.
- October 2025 table content review: NOT_RETRIEVED.
- Exact dataflow / provision / provider constraint resolution: UNKNOWN.
- Six-country formal eligibility: UNKNOWN.
- Quarterly coverage acceptance: NOT PASS.
- EMDE aggregation: BLOCKED.

## 7. Protected invariants

₹0 spend; official public sources only; no credentials, paid API, external contact, synthetic data, aggregation, annual-to-quarterly conversion, PR merge or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, engines A–E and Hard Gate unchanged.
