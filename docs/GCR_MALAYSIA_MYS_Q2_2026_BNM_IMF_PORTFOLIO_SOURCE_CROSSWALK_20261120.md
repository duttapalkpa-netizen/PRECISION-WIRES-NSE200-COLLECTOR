# Malaysia MYS Q2-2026 BNM–IMF portfolio source crosswalk
Date: 2026-11-20 (Asia/Kolkata)
Decision: national source extraction PASS; national sign convention documented; IMF row-level comparison NOT_DONE; full dual-leg validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## Continuity preflight and selection
- Re-fetched Master Continuity Ledger, GCR Master Priority Queue, 63-country Q2-2026 synchronous dual-leg cohort, IMF 154-member panel report, and prior POL/TUR/CHN source-gate reports.
- PASS items and previously blocked routes were excluded from repeat work. BGD XLS/XML/Open Data routes remain exhausted; POL NBP XLSX and TUR TCMB ZIP remain blocked on previously failed retrieval paths.
- MYS is explicitly in the fixed 63-country Q2-2026 cohort. Existing IMF coverage QA records both A_NFA_T and L_NIL_T present through 2026-Q2 (46/47 quarters each; 2026-Q3 is the sole missing tail). No cohort rebuild was performed.
- Existing panel raw file is committed as `docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv`, but GitHub text fetch returned empty content for this large file. No MYS exact IMF numeric value was extracted in this task; no new IMF query is claimed.

## Official national source
- Bank Negara Malaysia, Quarterly Bulletin 3Q 2026, Annex Table 3: Balance of Payments.
- Official PDF: https://www.bnm.gov.my/documents/20124/23688793/qb26q3_en_annex.pdf
- Publication date: 18 November 2026 (DOSM Q3 BOP release date, whose source tables feed BNM bulletin); source table identifies 2026 Q2 as preliminary (`p`).
- Source basis: BPM6; unit RM billion; source: Department of Statistics Malaysia.
- Table 3 Q2 2026 portfolio investment:
  - Net portfolio investment: -35.2 RMbn
  - Asset: -33.3 RMbn
  - Liabilities: -1.8 RMbn
- Source sign notes: asset negative denotes outflows due to acquisition of assets abroad by residents; liability positive denotes inflows due to incurrence of foreign liabilities. Thus the national table explicitly documents separate asset and liability directions.
- Arithmetic diagnostic: asset + liabilities = -33.3 + (-1.8) = -35.1 RMbn, versus published portfolio net -35.2 RMbn. Difference 0.1 RMbn is within one-decimal table rounding; the source explicitly warns figures may not add due to rounding. Do not force an exact equality from rounded display values.
- The official DOSM Q2 release (14-Aug-2026) independently states Q2 portfolio investment net outflow RM35.2bn; Q3 bulletin is the later source that exposes the separate legs and labels Q2 preliminary. DOSM Q3 release date 18-Nov-2026. Q2 original release PDF: https://www.dosm.gov.my/site/downloadrelease?id=quarterly-balance-of-payments-q22026&lang=English
- The OpenDOSM dashboard confirms BOP net figures are assets less liabilities for its balance dashboard, but this aggregate net convention is not by itself sufficient to assign the IMF series signs; keep the table's explicit transaction sign notes as the national source evidence.

## Acceptance matrix
- MYS membership in fixed 63-country Q2 both-leg cohort: PASS (existing archived coverage QA).
- National source Q2-2026 portfolio asset row: PASS (source extraction; RM -33.3bn, preliminary).
- National source Q2-2026 portfolio liability row: PASS (source extraction; RM -1.8bn, preliminary).
- National source portfolio net row: PASS (RM -35.2bn, preliminary).
- Display arithmetic: REVIEW / rounding difference 0.1 RMbn; source permits rounding.
- National sign convention: PASS as a source-description capture; asset negative=outflow; liability positive=inflow.
- FX conversion / RM-to-USD: NOT_DONE; no FX applied.
- IMF MYS exact Q2 values and raw row hashes in this task: NOT_DONE; large archived panel file was not text-readable through GitHub fetch. No new IMF query or synthetic value used.
- Exact IMF↔BNM scale/sign/period/vintage reconciliation: NOT_DONE.
- MYS full national dual-leg validation: PARTIAL / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## Next exact action
Use a supported way to extract the two MYS Q2 rows from the already archived IMF 9,299-row normalized panel (without re-querying IMF); then obtain an official same-period RM/USD conversion basis only if necessary, and compare both legs with the BNM preliminary Q3-bulletin vintage. If the archived panel cannot be materialized, document the access limitation and do not substitute a fresh or guessed value.

## Protected invariants
No aggregation, netting, imputation, forward-fill, synthetic observations, silent sign flip, FX conversion, or production integration. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Source references
- BNM Q3 2026 Quarterly Bulletin Annex Table 3, PDF lines 281–505: https://www.bnm.gov.my/documents/20124/23688793/qb26q3_en_annex.pdf
- DOSM Q2 2026 release date and portfolio net: https://www.dosm.gov.my/site/downloadrelease?id=quarterly-balance-of-payments-q22026&lang=English
- DOSM Q3 2026 release date: https://www.dosm.gov.my/portal-main/release-content/quarterly-balance-of-payments-q32026
- OpenDOSM BOP methodology / net display: https://open.dosm.gov.my/dashboard/balance-of-payments
- Existing cohort report: docs/GCR_2026Q2_SYNCHRONOUS_DUAL_LEG_COVERAGE_COHORT_CONTINUATION40_PART5_20261119.md
