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


## 8. Follow-up verification (2026-11-15)

A fresh inspection of the official IMF Documents catalogue and BOP dataset page reconfirmed the October 2025 document metadata and publication date (14 May 2026), but neither page extraction exposed the PDF download target or body. The official IMF SDMX Central REST Web Service page and its Web Services Guide confirm that structure queries can be generated through the UI and that the service supports Dataflow and Provision Agreement queries. The registry overview currently exposes only a paginated sample of dataflows; it does not establish the absence of an IMF.STA BOP dataflow. Direct retrieval of the guessed `IMF.STA/BOP/21.0.0` path remains inaccessible through this web retrieval channel. Consequently no negative inference is permitted.

Sources:
- IMF Documents catalogue: https://data.imf.org/en/Documents
- IMF BOP dataset: https://data.imf.org/Datasets/BOP
- IMF SDMX Central REST Web Service: https://sdmxcentral.imf.org/webservice/schema.html
- IMF SDMX Central Web Services Guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- SDMX Central Dataflow overview: https://sdmxcentral.imf.org/data/overview.html

Status remains unchanged: October 2025 PDF table NOT_RETRIEVED; exact IMF.STA Dataflow / Provision Agreement / Provider constraints UNKNOWN; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.


## 9. SDMX API contract validation and exact query specification (2026-11-15)

The official IMF SDMX Central Web Services Guide (last updated May 2025) was inspected. It confirms:
- REST entry point: `https://sdmxcentral.imf.org/sdmx/v2/`.
- Supported structure resources include `dataflow`, `provisionagreement`, `dataproviderscheme`, `contentconstraint`, `actualconstraint`, `allowedconstraint`, and `attachmentconstraint`.
- The query path has agencyID, structureID, version and optional itemID; the guide's references parameter supports `all`, `children`, `parents`, etc.
- A Dataflow or Provision Agreement can carry constraints; the registry's own landing page explains that constraints can restrict allowable content beyond the DSD.
- The SDMX Central Web Service UI allows the query URL to be generated from Structure Type, Agency, ID and Version selectors and downloaded. This is the preferred reproducible manual retrieval route if direct API retrieval is inaccessible.

Exact query template prepared from the documented contract (not evidence that the response exists):
`https://sdmxcentral.imf.org/sdmx/v2/structure/dataflow/IMF.STA/BOP/21.0.0?references=all&format=sdmx-2.1`

Follow-up structure query templates, to be populated only from actual returned references:
`.../structure/provisionagreement/{agency}/{id}/{version}?references=all&format=sdmx-2.1`
`.../structure/contentconstraint/{agency}/{id}/{version}?format=sdmx-2.1`
`.../structure/actualconstraint/{agency}/{id}/{version}?format=sdmx-2.1`
`.../structure/attachmentconstraint/{agency}/{id}/{version}?format=sdmx-2.1`

Direct web retrieval attempts against the exact Dataflow URL, broad IMF Dataflow listing, ContentConstraint listing and ProvisionAgreement listing returned inaccessible through this web retrieval interface. These errors do not establish HTTP status at the origin and do not prove the structures are absent. No response body, artefact ID, provider, or constraint was fabricated.

The IMF SDMX Central registry currently visibly lists IMF:BOP6_CONSTRAINT attached to BOP6[1.0] and IMF:BOP_BP6_CONSTRAINT attached to BOP_BPM6[1.0]. These remain distinct from the target IMF.STA:BOP(21.0.0) flow unless an actual reference establishes a relationship.

Official sources:
- https://sdmxcentral.imf.org/webservice/schema.html
- https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf (May 2025 guide; resources and references parameters)
- https://sdmxcentral.imf.org/ (registry description of Dataflow and Provision Agreement constraints)
- https://sdmxcentral.imf.org/data/constraints.html
- https://sdmxcentral.imf.org/data/overview.html

Status: API contract and reproducible query specification PASS; actual target Dataflow response NOT_RETRIEVED; target Provision Agreement/Provider/Constraint UNKNOWN; six-country eligibility UNKNOWN; quarterly coverage NOT PASS; EMDE aggregation BLOCKED.
