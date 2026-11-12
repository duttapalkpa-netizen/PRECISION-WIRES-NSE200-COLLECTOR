# NIC Concordance Evidence and Two-Digit Mapping Safety — IIP Research
Date: 2026-11-05
Branch: fix/iip-41-vintage-audit-clean

## Official primary source located
MoSPI, National Industrial Classification 2025 (NIC-2025), final PDF:
https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf
Publication metadata: NIC-2025, dated 07 November 2025 in the publication front matter.
Concordance section: printed pages 232–238; PDF extracted lines 15745 onward.
Table title: Concordance between 4-digit industry classes of NIC-2025 and NIC-2008.
Table note: (p) denotes part; + denotes aggregation of classes.

## What this source proves
- An official NIC-2025 ↔ NIC-2008 concordance exists at the 4-digit industry-class level.
- The concordance contains partial mappings and aggregated mappings; it is not a universal one-to-one crosswalk.
- NIC-2025 uses a five-level hierarchy including 2-digit Division, 3-digit Group, 4-digit Class and 6-digit national Sub-Class.
- The new IIP series disseminates manufacturing at NIC-2025 2-digit level, while the Batch 014 March-2024 legacy crosswalk is NIC-2008 2-digit, base 2011-12.

## Critical analytical limitation
The official NIC concordance is at 4-digit class level, whereas the current Batch 014 candidate ledger is at 2-digit NIC division level. The presence of a 4-digit concordance does NOT, by itself, certify a one-to-one 2-digit mapping. A correct roll-up requires all child classes, partial markers, aggregation operators and code coverage to be resolved, with no double counting or unassigned class hidden.

MoSPI's new-IIP release provides linking factors only at General and sectoral levels and explicitly cautions that lower-level linking may not be reliable because the item basket changes significantly. It also says the water supply/sewerage/waste-management sector is new and has no old-series linking factor. Therefore:
- Do not use NIC 4-digit concordance as an index-level linking factor.
- Do not convert 2011-12/NIC-2008 NIC-2 index levels into 2022-23/NIC-2025 NIC-2 levels using code-prefix matching.
- Do not assume same 2-digit code means identical industrial coverage between classifications.
- Any analytical 2-digit bridge must be separately constructed from the official 4-digit concordance and full child-code universe, with explicit partial/aggregation handling, and independently reviewed. Even then it is a classification concordance, not an index-level linking factor.

## Research-layer implementation requirements
1. Retain original NIC system and code as immutable source fields.
2. Store concordance rows at their native 4-digit granularity, with `nic2025_code`, `nic2008_reference`, `mapping_operator`, `partial_flag`, and source page/row.
3. Parse plus signs as aggregation relationships, not text decoration; parse `(p)` as partial correspondence, not full equivalence.
4. Build any 2-digit roll-up only as a derived research view with coverage counts, unmatched codes, partial mappings and many-to-many flags exposed.
5. Require complete child-class coverage and independent QA before a 2-digit derived mapping can be marked PASS.
6. Keep index series separate by base year, deflator vintage, classification system, release ID and estimate stage.
7. UNKNOWN remains neither PASS nor FAIL; no synthetic concordance rows or inferred mappings.

## Batch 014 implications
- Existing March-2024 two-sided PIB crosswalk remains valid for the legacy 2011-12 / NIC-2008 cohort only.
- It does not certify values in the 2022-23 / NIC-2025 back-series.
- The official 4-digit concordance is now located and its semantic markers are verified from the published document, but a full machine-readable extraction and 2-digit roll-up audit have not yet been completed.
- No candidate ledger rows are overwritten or reclassified.

## Status
OFFICIAL_NIC2025_PUBLICATION: LOCATED
OFFICIAL_4DIGIT_NIC2025_TO_NIC2008_CONCORDANCE: VERIFIED_IN_SOURCE
PARTIAL_AND_AGGREGATION_MARKERS: VERIFIED
FULL_MACHINE_READABLE_CONCORDANCE_EXTRACTION: PENDING
NIC2_ROLLUP_COVERAGE_AUDIT: PENDING
NEW_SERIES_MAR2024_CELL_RECONCILIATION: PENDING
RAW_PDF_BINARY_SHA256: PENDING
BATCH014_FULL_PROVENANCE: BLOCKED
MASTER_HARD_GATE: BLOCKED

## Production invariants
No changes to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, or V11.3(A/B/C/D/E) logic. No historical PASS evidence deleted or rewritten. No synthetic rows, fabricated timestamps, unsupported source promotion, or hard-gate relaxation.