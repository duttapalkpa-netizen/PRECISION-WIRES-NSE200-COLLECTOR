# IIP policy-stage candidate accounting reconciliation — 2026-11-07

## Reconciled population
The Batch 001 audit note explicitly defines the original policy-stage-aligned candidate universe as 693 transitions, with 9 certified and 684 remaining after Batch 001. It separately records 431 historical-panel/out-of-window transitions, for 1,124 total observed differences.

The existing Batch 001-005 ledgers were read independently and grouped by exact observation period + previous vintage ID + current vintage ID + NIC code. They contain 54 rows and 54 unique transition keys, distributed as:

| Batch | Observation period | Vintage transition | Rows |
|---|---|---|---:|
| 001 | 2023-04 | IIPMFY23049APR Quick → IIPMFY23054MAY First Revision | 9 |
| 002 | 2023-04 | IIPMFY23049APR Quick → IIPMFY23054MAY First Revision | 6 |
| 003 | 2023-04 | IIPMFY23049APR Quick → IIPMFY23054MAY First Revision | 5 |
| 004 | 2023-05 | IIPMFY23054MAY Quick → IIPMFY23058JUN First Revision | 14 |
| 005 | 2023-06 | IIPMFY23058JUN Quick → IIPMFY23062JUL First Revision | 20 |
| **Total** | | **3 distinct vintage-period pairs** | **54** |

April 2023's 20 rows are corroborated by Batch 003 README: Batch 001 (9) + Batch 002 (6) + Batch 003 (5) complete the 20 candidate-cell pair. Batch 004 README describes 14/14 policy-stage candidate transitions for May 2023. Batch 005 README describes 20 policy-stage candidate transitions for June 2023.

## Updated accounting
The 684 remaining count was the position immediately after Batch 001's 9 certified rows, not a timeless remaining count. Batches 002-005 add 45 additional distinct rows within the policy-stage candidate universe. Therefore:

- Original policy-stage-aligned candidate universe: 693
- Current certified rows across Batches 001-005: 54
- Current remaining policy-stage candidates: 639 (= 693 - 54)
- Historical-panel/out-of-window unresolved: 431
- Total observed differences: 1,124 (= 693 + 431 = 54 + 639 + 431)

This accounting is supported by unique transition keys, exact vintage pair grouping, and batch-specific scope notes. It does not assert that all 54 rows have been re-fetched/revalidated against source workbooks in this run; it carries forward the bounded batch certifications as recorded in their individual audit files.

## Provenance caveat
Legacy CSV SHA-256 mismatches for Batches 001, 003, 004, and 005 remain quarantined. The structural row and population accounting does not clear those hash mismatches. Do not update legacy hash declarations until original bytes or a defensible immutable artifact derivation chain is recovered.

## Gate and invariants
- IIP source audit: BLOCKED_WITH_PROVENANCE_GAPS.
- Overall Hard Gate: BLOCKED.
- No unsupported PASS promotion, no synthetic rows, no extrapolation.
- Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 unchanged.
- Research spend ₹0.
