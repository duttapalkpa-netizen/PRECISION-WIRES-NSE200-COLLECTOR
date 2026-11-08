# IIP Manufacturing NIC Crosswalk — Division-Level Safety Decision

Status: RESEARCH AUDIT COMPLETE; AUTOMATIC 2-DIGIT MAPPING NOT APPROVED
Recorded: 2026-11-09
Source: MoSPI NIC-2025 official concordance, printed pages 232–234 (PDF source lines 15228–15475).
Official PDF: https://www.mospi.gov.in/sites/default/files/main_menu/national_industrial_classification/NIC_2025Final_18112025.pdf

## Objective

Determine whether MoSPI's official 4-digit NIC-2025 ↔ NIC-2008 concordance can be safely collapsed to the 2-digit manufacturing divisions used in the legacy IIP manufacturing table.

## Source facts directly checked

MoSPI's table states that it links 4-digit industry classes; `(p)` means part and `+` means aggregation of classes. The source table spans printed pages 232–238. This audit checked the manufacturing-range rows visible on printed pages 233–234 and nearby boundary rows.

Representative manufacturing examples transcribed from the official table:
| NIC-2025 class | NIC-2008 source expression | Structural signal |
|---|---|---|
| 1103 | 1103(p) | PART |
| 1104 | 1103(p) | PART; one old class feeds multiple new classes |
| 1105 | 1104 | EXACT_CLASS_CODE |
| 1313 | 1313(p) | PART |
| 1512 | 1512 + 2220(p) | AGGREGATION + PART; crosses old divisions |
| 1811 | 1811 + 1313(p) | AGGREGATION + PART; crosses old divisions |
| 2029 | 2011(p) + 2029 | AGGREGATION + PART |
| 2393 | 2393 + 2392(p) | AGGREGATION + PART |
| 2520 | 2520 + 3030(p) | AGGREGATION + PART; crosses old divisions |
| 2611 | 2610(p) | PART |
| 2619 | 2610(p) | PART; split old class |
| 2750 | 2750(p) + 2815(p) | PART + cross-division aggregation |
| 2815 | 2815(p) | PART |
| 3030 | 3030(p) | PART |
| 3101 | 3100(p) | PART |
| 3102 | 3100(p) | PART; split old class |
| 3511 | 3510(p) | PART |
| 3512 | 3510(p) | PART |
| 3513 | 3510(p) | PART; split old class |
| 3530 | 3530 + 1104(p) | AGGREGATION + PART; crosses old divisions |
| 3540 | 3510(p) + 3520(p) | PART + aggregation |

The rows above are examples, not the complete 463-row concordance. The complete table is not represented as extracted in this artifact.

## IIP applicability decision

**No direct 2-digit IIP manufacturing mapping is approved from the NIC concordance alone.**

Reasons:
1. The official concordance is at 4-digit class level; legacy IIP tables are at 2-digit industry-group level.
2. Multiple new classes can draw on portions of one old class (e.g. 2610(p) → 2611 and 2619; 3100(p) → 3101 and 3102; 3510(p) → 3511/3512/3513).
3. Some new classes aggregate portions of old classes across divisions (e.g. 1512, 1811, 2520, 2750, 3530).
4. A 2-digit roll-up by code prefix or row counts would ignore partial scope and cannot preserve IIP basket/weights.
5. NIC concordance is an activity-classification correspondence, not an IIP item-group/weight concordance. Even a complete NIC class mapping would not by itself create an index-level bridge.

## Safe machine-readable schema

For future complete extraction, each source row must retain:
- `nic2025_class_4d`
- `nic2008_expression_raw` (verbatim, including spaces, plus signs and (p))
- `nic2008_components` (parsed array; each component has code and partial boolean)
- `has_partial`
- `has_aggregation`
- `source_printed_page`
- `source_pdf_url`
- `source_line_start`
- `source_line_end`
- `extraction_status`

Do not silently repair line wraps. The source extraction includes a table split across pages where the NIC-2025 code 4772's NIC-2008 expression continues in the next table block as 4799(p). A parser must support continuation rows with a blank NIC-2025 code and append the continuation to the prior row only when page/table sequence and column structure confirm it. Preserve both raw fragments and reconstructed expression.

## Required automated QA before full CSV acceptance

- Exact 463 NIC-2025 class rows, reconciled against MoSPI's published 463-class structure count (the count alone is not proof of concordance row completeness).
- Unique non-empty NIC-2025 4-digit keys; reject accidental duplicates.
- Every source row's raw expression retained verbatim.
- Every parsed component is a four-digit NIC-2008 code; leading zeroes preserved as strings.
- Every `(p)` flag retained; no partial converted to full.
- Every '+' component retained; no aggregation silently dropped.
- Blank-code continuation fragments are attached only with deterministic source context; otherwise fail closed.
- Forward and reverse mapping multiplicities computed independently.
- Any missing/ambiguous row is UNKNOWN, not imputed.
- No 2-digit mapping marked PASS unless all constituent classes and scopes are complete and IIP-specific coverage/weight correspondence is separately evidenced.
- No index-level conversion, rebasing factor, or synthetic weights generated.

## Outcome

- Official source and manufacturing-range concordance examples: PASS.
- Unsafe direct 2-digit roll-up rejected: PASS.
- Complete 463-row machine-readable extraction: NOT COMPLETED.
- IIP-specific item-group/weight bridge: UNKNOWN / BLOCKED.
- Production use: NOT APPROVED.

This task closes the IIP-specific mapping safety decision. It does not claim the complete NIC concordance extraction, does not clear the IIP 41-vintage gate or project Hard Gate, and does not alter any protected V11.3 invariant.
