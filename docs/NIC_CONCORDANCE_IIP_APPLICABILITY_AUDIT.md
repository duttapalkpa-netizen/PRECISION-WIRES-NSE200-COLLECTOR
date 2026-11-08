# NIC-2025 ↔ NIC-2008 Concordance: IIP Mapping Applicability Audit

Status: OFFICIAL SOURCE FOUND; IIP AGGREGATION NOT YET APPROVED
Recorded: 2026-11-09
Scope: Determine whether MoSPI's official NIC concordance can safely be used to translate IIP industry groups. Research-only; no production integration.

## Official source located

MoSPI, National Industrial Classification 2025, official PDF:
https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf

The official publication's contents identify "Concordance between 4-digit industry classes of NIC-2025 and NIC-2008" on printed pages 232–238. The table heading explicitly says:
- (p) denotes part
- + denotes aggregation of classes

The source table is at PDF extracted lines 15753 onward (web source reference: https://www.mospi.gov.in/uploads/publications_reports/publications_reports1763457214315_c3e5d4f3-8e25-4775-85e3-ad42d571652f_NIC_2025_Final.pdf).
MoSPI also states NIC-2025 has 87 divisions, 258 groups, 463 classes and 1,887 subclasses; NIC-2008 had 88 divisions, 238 groups, 403 classes and 1,304 subclasses. The revised classification has structural changes, not just code renaming.

## Source examples proving partial / aggregation complexity

Examples transcribed from the official concordance:
- NIC-2025 0113 ← NIC-2008 0113 + 0128(part)
- NIC-2025 0330 ← NIC-2008 0311(part) + 0312(part) + 0321(part) + 0322(part)
- NIC-2025 1512 ← NIC-2008 1512 + 2220(part)
- NIC-2025 1811 ← NIC-2008 1811 + 1313(part)
- NIC-2025 2611 and 2619 ← NIC-2008 2610(part)
- NIC-2025 3511, 3512 and 3513 each ← NIC-2008 3510(part)
- NIC-2025 3530 ← NIC-2008 3530 + 1104(part)
- NIC-2025 3540 ← NIC-2008 3510(part) + 3520(part)
- NIC-2025 3101 and 3102 each ← NIC-2008 3100(part)

These are direct evidence that a simple prefix substitution or one-to-one code rename would be invalid. A NIC-2025 4-digit class may draw on only part of one NIC-2008 class, multiple old classes, or portions of several classes. Reverse mappings may also split one old class among multiple new classes.

## IIP relevance and safe-use decision

1. The old IIP manufacturing table is based on NIC-2008 two-digit industry groups; the current 2022-23 IIP uses NIC-2025 industry groups.
2. The MoSPI concordance is at 4-digit class level, not an IIP-specific 2-digit index-weight concordance.
3. Do not roll up the concordance to 2-digit by simply truncating codes or counting classes. Such an operation ignores partial mappings and does not preserve IIP item-group coverage or weights.
4. Even a mathematically valid activity-class mapping would not itself provide a statistical bridge between IIP indices: IIP basket, item-group coverage, weights and deflator changed. Never infer index-level conversion or historical growth from NIC concordance.
5. For any future division-level crosswalk, aggregate only after parsing every official 4-digit row, preserving the exact source expression and partial flags; test both forward and reverse coverage. A division can be called one-to-one only if every constituent class is fully mapped, no partial marker occurs, the reverse mapping is unique, and the IIP scope itself is unchanged. Otherwise label it MANY_TO_MANY, PARTIAL or UNKNOWN.
6. An IIP sector/industry bridge additionally requires MoSPI's official IIP-specific correspondence or explicit item-group/weight mapping. NIC concordance alone is insufficient.

## Validation contract for a future machine-readable extraction

Required fields:
- nic2025_class_4d
- nic2008_source_expression
- nic2008_class_codes (parsed tokens, retaining original expression)
- has_partial_marker
- has_aggregation_operator
- source_pdf_url
- source_printed_page
- source_line_or_table_locator
- extraction_status
- reviewer_status

Required tests:
- every source row is retained exactly once;
- no code is silently dropped or padded incorrectly;
- all '+' aggregation components are retained;
- every '(p)' flag is preserved and parsed as partial, not treated as a complete code;
- duplicate NIC-2025 class rows are rejected unless the official source explicitly provides them;
- forward and reverse mapping multiplicities are calculated independently;
- no 2-digit mapping is promoted to PASS unless the completeness and uniqueness conditions above are met;
- no IIP index values or weights are generated from the NIC concordance.

## Completion and remaining work

Completed in this task:
- official MoSPI concordance located and opened;
- official granularity and page range confirmed;
- representative partial and aggregation cases verified;
- unsafe prefix-mapping assumption explicitly rejected;
- IIP-specific limitations and machine-extraction QA contract documented.

Not completed:
- full 4-digit table extraction to CSV/JSON;
- independent row-count reconciliation against all seven printed pages;
- complete forward/reverse multiplicity report;
- official IIP-specific 2-digit item-group/weight correspondence;
- any production integration.

Current status: official source discovery and applicability audit PASS; machine-readable extraction and IIP roll-up remain UNKNOWN / BLOCKED. No data invented, no CI rerun, no production changes, no PR merge.
