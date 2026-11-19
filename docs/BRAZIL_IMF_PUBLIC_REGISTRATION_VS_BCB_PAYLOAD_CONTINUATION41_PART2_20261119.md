# Brazil — IMF public registration vs BCB payload Dataflow identity
Date: 2026-11-19
Continuation: 41, Part-2
Scope: read-only cross-check of the current public IMF SDMX Central registration listing against the already archived and independently reparsed BCB payload. No authenticated registry action or new payload GET.

## Progress log
- Reused Part-3 public structure artifact and Part-4 independent raw-byte/XML reparse; no duplicate capture.
- New check: current public IMF SDMX Central registration listing surfaced the exact BCB URL under Dataflow IMF:BOP6(1.0), Data Provider IMF:BR1, last updated 2026-10-26T11:47:29Z.
- Existing Part-4 raw BCB XML at that same registered URL independently declares Dataflow IMF:BOP_BPM6(1.0) in schema/header/structure reference; raw-byte SHA-256 3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c, original retrieval 2026-11-18T12:11:07.589328Z, 4,840,062 bytes.
- Existing Brazil PA IMF:BR_BOP_BP6(1.0) references Dataflow IMF:BOP6(1.0), Provider IMF:BR1.

## New public cross-check
IMF SDMX Central public Registrations listing (https://sdmxcentral.imf.org/data/registrations.html) currently indexes:
- Dataflow: IMF:BOP6(1.0)
- Data Provider: IMF:BR1 (Central Bank of Brazil)
- Registered URL: https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml
- Last updated: 2026-10-26T11:47:29Z

The listing is public read-only evidence; it does not expose the PA's historical changelog or prove that a cross-Dataflow submission is permitted. The IMF SDMX Central page itself distinguishes public registration listing from authenticated registry actions (login/confirmation controls).

## Reconciliation
The same exact BCB URL is represented in three relevant places:
1. Brazil PA IMF:BR_BOP_BP6(1.0) → StructureUsage Dataflow IMF:BOP6(1.0), Provider IMF:BR1 (archived raw PA structure).
2. Current public registration listing → IMF:BOP6(1.0), IMF:BR1, same BCB URL.
3. Raw XML served by that URL → payload Dataflow IMF:BOP_BPM6(1.0), structureRef IMF_BOP_BPM6_1_0 (Part-4 independent reparse).

Therefore the PA and public registration listing agree with each other, while the current bytes served from the registered URL declare a different Dataflow. This is stronger evidence of a live registration/payload identity inconsistency; it is NOT evidence that BOP6 and BOP_BPM6 are aliases. Shared ECOFIN_DSD and DATA_DOMAIN=BOP6 do not establish equivalence.

## Acceptance
- Exact public registration tuple (BOP6 / BR1 / BCB URL): CONFIRMED from public listing.
- Exact current PA tuple (BOP6 / BR1): CONFIRMED from archived PA structure.
- Exact payload tuple (BOP_BPM6 / BCB XML): CONFIRMED from Part-4 raw reparse.
- PA/registration vs payload identity consistency: FAIL / MISMATCH CONFIRMED.
- Brazil-specific crosswalk or authorized exception: NOT_PROVEN.
- Historical PA revision/change chronology: UNKNOWN / BLOCKED.
- Brazil Reconstruction: BLOCKED pending IMF/BCB owner-side correction or documented authorized mapping and history evidence.

## Exact next actions
1. Preserve this as a reproducible discrepancy; do not rewrite the PA, change Dataflow IDs, infer an alias, or transform payload data.
2. Obtain an authorized owner-side export of the exact Brazil PA history/Changelog and registration details, or an official IMF/BCB written correction/exception identifying the intended Dataflow for the registered URL.
3. After an owner-side correction, retrieve the new public payload and repeat the raw-byte digest + XML header/structureRef comparison; require the PA, registration listing and payload Dataflow to agree before marking Brazil PASS.

## Sources
- IMF SDMX Central public registrations: https://sdmxcentral.imf.org/data/registrations.html
- IMF SDDS Brazil BOP metadata (BPM6 concepts and public source context): https://dsbb.imf.org/sdds/dqaf-base/country/BRA/category/BOP00
- BCB payload URL: https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml
- Prior raw verification report: docs/BRAZIL_BCB_RAW_PAYLOAD_HEADER_REPARSE_CONTINUATION40_PART4_20261119.md

## Invariants
₹0; public official evidence only; no credentials, no authenticated writes, no synthetic data, no inferred alias, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is never PASS.
