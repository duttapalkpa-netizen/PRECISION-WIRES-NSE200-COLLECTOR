# Peru (PER) Q2-2026 — BCRP official portfolio-source boundary audit
Date: 2026-11-20 (Asia/Kolkata)
Decision: PER selected from the fixed 63-country Q2-2026 dual-leg cohort after repository search found no dedicated PER Q2-2026 national portfolio-flow reconciliation report. Existing IMF raw rows were extracted, but no exact Q2-2026 BCRP national portfolio asset/liability transaction pair was independently retrieved from an accessible official BCRP publication in this bounded audit. PER national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## Continuity and duplicate rejection
- Re-fetched Master Continuity Ledger, GCR Priority Queue and fixed 63-country cohort before selection.
- PER is present in the fixed cohort. The cohort and IMF panel were reused; no rebuild or new IMF query.
- GitHub search for PER Q2-2026 portfolio source/reconciliation found no dedicated PER report. Prior country validations and completed IMF panel QA were not repeated.

## Existing IMF raw archive — exact Q2 rows
- Asset raw file: docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv
  - Git blob SHA: 15449e87c9057291a1f52f2f8cd9805df55f9fb8
  - Exact PER row: `dataflow,IMF.STA:BOP(21.0.0),R,PER,A_NFA_T,P_F,USD,Q,2026-Q2,1999155686.69433,6,6,,,,,,,,,,,,O,,,,true,,`
- Liability raw file: docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv
  - Git blob SHA: 15f379dc42e2760eb5f2384618e48f5ddc3177f1
  - Exact PER row: `dataflow,IMF.STA:BOP(21.0.0),R,PER,L_NIL_T,P_F,USD,Q,2026-Q2,1699664071.47559,6,6,,,,,,,,,,,,O,,,,,,`
- Both are USD, quarterly, 2026-Q2, SCALE=6, PRECISION=6, ACTION=R. Converted for display only: asset USDm 1,999.15568669433; liability USDm 1,699.66407147559. Preserve raw USD OBS_VALUE and scale; no inferred scaling beyond the recorded scale semantics.
- These are IMF observations only, not national validation.

## Official BCRP source boundary
1. BCRP “Indicadores Económicos — IV Trimestre 2025”: https://www.bcrp.gob.pe/docs/Estadisticas/indicadores-trimestrales.pdf
   - Official PDF currently exposes quarterly economic indicators through 2025-Q4, not Q2-2026. It includes a private-sector long-term capital flow table; the inspected official version is therefore stale for the requested Q2-2026 target.
2. BCRP statistical portal reference: https://www.bcrp.gob.pe/estadisticas.html
   - BCRP directs users to its statistics portal and historical statistical tables. No directly accessible Q2-2026 BCRP portfolio asset/liability transaction export was captured in this audit.
3. BCRP Note of Studies No. 59 / Macroeconomic Report — Second Quarter 2026:
   - Candidate official URL tested: https://www.bcrp.gob.pe/docs/Publicaciones/Notas-Estudios/2026/nota-de-estudios-59-2026.pdf
   - The web retrieval returned only an HTML iframe shell, not the official PDF contents. A third-party index exposes snippets attributed to the report, but those snippets are not accepted as official raw evidence and are not used for numeric admission.
   - The candidate report may contain sector-level balance-of-payments details, but portfolio-specific gross assets and liabilities, table/page, definitions, source vintage and raw file are NOT_INSPECTED. Do not infer or copy values from the third-party extract.
4. BCRP official historical quarterly indicator PDF: https://www.bcrp.gob.pe/docs/Estadisticas/indicadores-trimestrales.pdf
   - It contains private-sector financial account assets/liabilities and portfolio sub-lines, but latest available quarter in the inspected official PDF is 2025-Q4. It cannot validate PER 2026-Q2.
5. IMF Article IV staff report is not a substitute for the national primary source; its annual/projection BOP table is excluded from Q2-2026 transaction validation.

## Fail-closed acceptance
- Fixed cohort membership / IMF panel two-leg availability: PASS at panel level only (inherited cohort evidence).
- Existing IMF PER Q2-2026 exact raw row extraction: PASS.
- Official BCRP source family discovery: PASS.
- Official national Q2-2026 portfolio asset leg: NOT_EXTRACTED.
- Official national Q2-2026 portfolio liability leg: NOT_EXTRACTED.
- Official source bytes / retrieval receipt / SHA-256: NOT_CAPTURED.
- BCRP table-specific sign, BPM basis, portfolio component mapping and period/vintage alignment: NOT_ESTABLISHED.
- Numeric dual-leg comparison: NOT_DONE.
- PER national validation: PARTIAL / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## Next exact action
Obtain the official BCRP Note of Studies No. 59 (Q2-2026) PDF through a supported official download path or the BCRP statistics portal, archive exact raw bytes with retrieval metadata and SHA-256, then inspect the precise portfolio component table. Map national financial-account assets/liabilities separately to IMF A_NFA_T and L_NIL_T only after verifying BPM basis, sign convention, units, period, and publication vintage. If official PDF access remains unavailable, record BLOCKED and advance to the next eligible country; do not use third-party snippets or stocks as transaction flows.

## Invariants
No IMF re-query, no cohort rebuild, no third-party numeric admission, no IIP stock substitution, no netting, no FX inference, no synthetic/filled values, no aggregate admission, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS.
