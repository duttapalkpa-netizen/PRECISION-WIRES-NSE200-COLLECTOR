# Malaysia MYS Q2-2026 — archived IMF exact-row extraction
Date: 2026-11-20 (Asia/Kolkata)

Decision: **IMF raw-row extraction PASS; national-source numeric comparison NOT_DONE; MYS full dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## Continuity and duplicate rejection
- Reopened the current GCR priority queue and Malaysia national-source crosswalk.
- Reused the existing IMF EMDE panel artifact; no new IMF request, no cohort rebuild, and no repeated BNM source extraction.
- MYS remains in the fixed 63-country Q2-2026 both-leg cohort. The existing coverage matrix records both A_NFA_T and L_NIL_T through 2026-Q2.

## Archived artifact integrity
- Workflow: 44474218174.
- Artifact: 14505862034.
- ZIP size: 5,997,777 bytes.
- ZIP SHA-256: `1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f`.
- Normalized panel: `emde_portfolio_flows.csv`, 1,849,027 bytes.
- Normalized panel SHA-256: `e8a44abbc8455fef44cc1e4677018ae4b9634d1c04f65bf6fc6dad133cfce62a`.
- Raw asset CSV SHA-256: `677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e`.
- Raw liability CSV SHA-256: `713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba`.
- All three CSV files were read from the downloaded ZIP; archive hash matches the previously recorded acquisition receipt.

## Exact Malaysia rows extracted
Both rows are from IMF.STA:BOP(21.0.0), indicator P_F, UNIT=USD, FREQUENCY=Q, TIME_PERIOD=2026-Q2.

| Field | Asset row | Liability row |
|---|---:|---:|
| COUNTRY | MYS | MYS |
| BOP_ACCOUNTING_ENTRY | A_NFA_T | L_NIL_T |
| OBS_VALUE (raw, unchanged) | 8328720912.826584 | -453604929.8946682 |
| SCALE | 6 | 6 |
| PRECISION | 6 | 6 |
| DERIVATION_TYPE | O | O |
| IFS_FLAG | true | blank |
| SOURCE_FILE | EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv | EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv |

No raw value was multiplied/divided by 10^6, rescaled, converted, netted or overwritten. The prior country-specific scale/sign pilots do not authorize a universal transformation.

## National-source comparison boundary
Reused the existing national source capture:
- BNM Quarterly Bulletin Q3 2026, Annex Table 3, BPM6, RM billion, Q2 preliminary.
- Portfolio net: -35.2 RMbn.
- Assets: -33.3 RMbn.
- Liabilities: -1.8 RMbn.
- Published display arithmetic: -33.3 + (-1.8) = -35.1 RMbn; 0.1 RMbn difference is retained as source rounding review, not forced to zero.
- National source sign-note capture remains as documented in the existing Malaysia crosswalk; do not infer or silently apply a sign transformation.

Official BNM exchange-rate averages reproduced in DOSM Monthly Statistical Bulletin June 2026, Table 8.8 (source: BNM), RM per USD:
- April 2026: 3.9784
- May 2026: 3.9526
- June 2026: 4.0778
The publication labels these rates “Average for Period”. These are monthly averages, not an explicitly published Q2 daily-weighted average. No quarterly FX rate has been manufactured by taking an unweighted mean of the three monthly observations. Exact FX aggregation convention and national-vintage alignment must be established before any official USD comparison.

## Acceptance matrix
| Gate | Status |
|---|---|
| Fixed 63-country Q2 cohort membership | PASS (reused) |
| Archived panel ZIP SHA-256 | PASS |
| Normalized panel SHA-256 | PASS |
| Exact MYS Q2 asset row extracted | PASS |
| Exact MYS Q2 liability row extracted | PASS |
| Raw source attributes preserved | PASS |
| National BNM Q2 component/sign-note capture | PASS (reused) |
| Quarterly FX convention / exact rate | NOT_DONE |
| Country-specific numeric scale/sign crosswalk | NOT_DONE |
| Same-vintage national ↔ IMF alignment | NOT_ESTABLISHED |
| MYS full dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate | NOT_AUTHORIZED |

## Next exact action
1. Establish the correct Q2 2026 RM/USD period-average method from official BNM daily observations or an official quarterly average; preserve the exact source dates and calculation convention.
2. Resolve BNM's asset/liability sign notes against IMF A_NFA_T and L_NIL_T separately; do not infer a shared sign transform.
3. Convert only after the rate convention and sign crosswalk are evidenced; compare each leg independently with source-display rounding bounds.
4. Preserve the BNM preliminary vintage and IMF retrieval vintage separately. Same-vintage identity must not be claimed without evidence.
5. If the exact vintage bridge is unavailable, keep MYS PARTIAL and proceed to the next eligible country in the existing fixed cohort.

## Protected invariants
No production code, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, or trade gates changed. No paid API, synthetic data, fabricated timestamp, silent conversion, netting, imputation, or aggregate authorization. UNKNOWN is never PASS.

## Source references
- Existing national crosswalk: `docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_IMF_PORTFOLIO_SOURCE_CROSSWALK_20261120.md`.
- IMF panel acquisition report: `docs/GCR_IMF_BOP_EMDE_PANEL_PART2_20261119.md`.
- DOSM Monthly Statistical Bulletin June 2026, Table 8.8 (official BNM sourced exchange rates): https://www.dosm.gov.my/uploads/release-content/file_20260826081723.pdf
- BNM exchange-rate display: https://www.bnm.gov.my/exchange-rates
