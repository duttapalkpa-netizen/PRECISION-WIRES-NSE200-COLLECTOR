# GCR Continuation 299 — Malaysia (MYS) Q2-2026 BNM ↔ IMF publication-vintage and revision-cutoff audit
Date: 28-Nov-2026 (Asia/Kolkata)
Scope: fixed 63-country Q2-2026 cohort; MYS next after MNG's exact documented .px route remained inaccessible and was closed for repeat through the same reader.

## 1. Continuity preflight and duplicate rejection
- Re-read current GitHub Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, immutable 63-country matrix, MYS BNM/IMF dual-leg reconciliation, exact IMF row extraction, and IMF panel acquisition report.
- Rechecked Library Mother File / prior research context and Library search results for MYS Q2 publication-vintage work. The next open MYS dependency was explicitly the BNM-vs-IMF publication-vintage and revision-cutoff reconciliation.
- Skipped completed PASS work: fixed cohort, IMF raw row extraction and SHA-256, BNM Q3 Annex Table 3 national dual-leg capture, BNM daily/monthly FX raw capture, Q2 60-row daily FX mean, monthly cross-check, country-specific sign mapping, and the two independent numeric leg comparisons. No IMF re-query, no FX re-download, no repeated numeric arithmetic, no cohort rebuild.
- MNG was not repeated: its documented .px metadata URL variant already returned “URL not accessible” with no HTTP status/body; only a genuinely different supported GET-capable route could reopen it. MYS is the next executable pending-vintage task in the fixed cohort sequence.

## 2. New official DOSM revision-practice evidence
Official source: Department of Statistics Malaysia, Balance of Payments — Third Quarter 2026, Technical Notes, printed page 90.
URL: https://www.dosm.gov.my/uploads/release-content/file_20261118114552.pdf
Publication date: November 2026; Q3 release published 18-Nov-2026.

The technical notes explicitly state DOSM's release/revision practice:
- Preliminary data are released seven weeks after the reference quarter.
- Revision data for the previous year are published in the first quarter of the current year.
- Final data are published one year after the release of revised data.
- Revisions arise from recent reporting and updated information from data providers.
- Abbreviations distinguish p = preliminary, r = revised and f = final.

Interpretation boundary:
- This is an official DOSM BOP revision policy. It is valid evidence of DOSM's general release/revision cadence.
- It does not itself provide an observation-specific revision timestamp, nor prove that BNM's separately published Q2 portfolio-flow rows and the IMF Q2 observations share the same source-vintage cutoff.
- It does not identify a specific Q2-2026 revision event or establish that the current BNM Q2 values are final.
- The policy implies that 2026 observations can enter the “previous year” revision cycle in Q1-2027, and final data follow one year after the revised release. This is a general schedule implication, not a guaranteed date for the individual MYS portfolio rows.

## 3. Independent DOSM Q2 net corroboration — net only
- DOSM's official Q3-2026 BOP release dated 18-Nov-2026 reports Q2-2026 portfolio investment as a net outflow of RM35.2 billion.
- The same DOSM report's technical notes state the revision policy above.
- The DOSM Q3 report is an independent official national publication for the Q2 net figure; it does not expose the separate Q2 portfolio asset and liability legs in the inspected summary.
- This corroborates the Q2 net total only. It is not used to infer, back-solve or replace either gross leg.

Official release: https://www.dosm.gov.my/portal-main/release-content/quarterly-balance-of-payments-q32026

OpenDOSM's BOP balance dataset also says that the most recent eight quarters may be revised in future releases and is net-only (balance is credits less debits); its latest update is 18-Nov-2026:
https://open.dosm.gov.my/data-catalogue/bop_balance
This dataset is revision-window context only, not a substitute for portfolio A/L transaction legs.

## 4. Reuse of BNM Q3-2026 Annex Table 3 and prior accepted numeric work
Prior MYS report retained unchanged:
docs/GCR_MALAYSIA_MYS_Q2_2026_BNM_OFFICIAL_FX_AND_DUAL_LEG_RECONCILIATION_20261120.md

BNM Q3-2026 Annex Table 3 (published 18-Nov-2026), Q2-2026, BPM6, RM billion, marks Q2 as preliminary:
- Portfolio assets: -33.3 RMbn.
- Portfolio liabilities: -1.8 RMbn.
- Portfolio net: -35.2 RMbn.
- Displayed component sum is -35.1 RMbn; retain the existing 0.1 RMbn rounding REVIEW. Do not force the identity.
- Prior MYS reconciliation already passed each separate numeric leg at BNM's published display precision using the accepted BNM 1200-middle Q2 daily FX mean 4.0016916666666667 MYR/USD and the country-specific sign crosswalk. No calculation was repeated here.
- Prior asset residual: USD 7.240206m; prior liability residual: USD 3.795162m; both within the converted ±USD12.494716m half-unit bound from one-decimal RMbn display. These figures are carried forward from the prior report only.

Official BNM annex locator: https://www.bnm.gov.my/documents/20124/23688793/qb26q3_en_annex.pdf

## 5. IMF receipt timing and observation-vintage boundary
Reused existing archived IMF panel; no IMF query was made.
- Existing panel acquisition report: docs/GCR_IMF_BOP_EMDE_PANEL_PART2_20261119.md.
- Existing exact MYS raw-row extraction: docs/GCR_MALAYSIA_MYS_Q2_2026_IMF_RAW_ROW_EXTRACTION_20261120.md.
- IMF archive acquisition receipt date: 19-Nov-2026, UTC capture window 06:43–06:45.
- Existing IMF panel artifact 14505862034, ZIP SHA-256 1a1a184f3689e04ff75d4433b44904083a33e18bdc70f096c3e9919900ebeb4f.
- Existing raw MYS asset CSV SHA-256 677054017f5d3ae5fdd0403d7341588ebf43ad8b54124ae1b616bf323229326e.
- Existing raw MYS liability CSV SHA-256 713b7a3000712e2ffb07cd574d08d7e6f3c02a6b2573ce4b40d06e0458cd7bba.
- Existing Q2 rows: IMF.STA:BOP(21.0.0), indicator P_F, UNIT=USD, FREQUENCY=Q, TIME_PERIOD=2026-Q2; asset A_NFA_T raw OBS_VALUE 8328720912.826584, SCALE=6; liability L_NIL_T raw OBS_VALUE -453604929.8946682, SCALE=6. Raw values remain unchanged.

Temporal comparison:
- BNM Q3-2026 publication date: 18-Nov-2026.
- IMF panel transport receipt: 19-Nov-2026 06:43–06:45 UTC.
- This proves the archived IMF file was acquired after the BNM Q3 publication became public. It does not prove the IMF observation was compiled from, incorporated, or revised to the same BNM Q2 source vintage. The IMF row metadata/receipt does not contain a MYS Q2 observation-specific source-submission timestamp or matching revision ID.
- Therefore “IMF retrieved after BNM release” is a transport chronology fact only; it is not a same-vintage bridge.

## 6. Acceptance result
| Gate | Status |
|---|---|
| Current Ledger / Queue / Registry / fixed cohort preflight | PASS |
| Library Mother File / prior MYS report review | PASS |
| DOSM official Q3-2026 revision policy captured | PASS (policy evidence only) |
| DOSM Q2 portfolio net corroboration | PASS (net only; not dual-leg evidence) |
| BNM Q2 asset/liability values and preliminary label | PASS (carried forward) |
| Existing BNM Q2 FX capture and daily/monthly arithmetic | PASS (carried forward; not repeated) |
| Existing separate numeric asset comparison | PASS at published display rounding (carried forward) |
| Existing separate numeric liability comparison | PASS at published display rounding (carried forward) |
| IMF archived row hashes and exact attributes | PASS (carried forward) |
| BNM release date vs IMF transport receipt chronology | PASS (chronology only) |
| Observation-specific IMF Q2 source vintage / revision ID | NOT_CAPTURED |
| BNM↔IMF same-vintage identity | NOT_ESTABLISHED |
| MYS full national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 7. Exact next action
1. Keep MYS asset and liability numeric gates PASS, but keep vintage PENDING and FULL_PASS NO.
2. Reopen only if a distinct official BNM/DOSM observation-level revision record, archived BNM Q2 table snapshot, or IMF observation-specific source-submission/vintage metadata becomes available.
3. If no observation-specific bridge is publicly exposed, preserve NOT_ESTABLISHED and advance to the next eligible fixed-cohort country. Do not repeat BNM FX extraction, numeric arithmetic, or IMF retrieval.
4. Do not infer a 2026-Q2 final status from the general DOSM calendar; the current BNM values remain explicitly preliminary.

## 8. Protected invariants
₹0; official/free sources only. No IMF re-query, cohort rebuild, paid API, credentials, synthetic data, fabricated timestamp, inferred revision ID, unsupported FX/sign/scale conversion, net-to-leg back-solving, stock/flow substitution, tolerance widening or aggregate promotion. UNKNOWN is neither PASS nor FAIL. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged. No workflow dispatch, merge or production integration.

**Task result:** C299 adds an official DOSM revision-practice source and an independent Q2 net corroboration, while confirming that the MYS same-vintage bridge is still not established. Existing numeric PASS gates are preserved; MYS remains PARTIAL / NOT PASS and the 63-country aggregate remains NOT_AUTHORIZED.