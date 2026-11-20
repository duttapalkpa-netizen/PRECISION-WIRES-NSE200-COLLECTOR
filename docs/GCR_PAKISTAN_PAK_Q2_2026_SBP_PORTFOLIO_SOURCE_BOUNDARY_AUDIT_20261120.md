# Pakistan (PAK) Q2-2026 — SBP official portfolio-source boundary audit
Date: 2026-11-20 (Asia/Kolkata)
Decision: official SBP source catalogue and public releases inspected. A quarterly BPM6 BOP dataset is listed through June 2026, but the retrievable public table inspected here does not expose separate Q2-2026 portfolio asset/liability transaction legs. The separate “Core Set of Portfolio Investment Assets” source is a half-yearly position/stock dataset, last released 15-Jan-2026 and reporting end-June 2025; it is not a Q2-2026 transaction-flow substitute and has no corresponding liability leg in that source. PAK national validation PARTIAL/BLOCKED; no Q2 values admitted; sign mapping, same-vintage and numeric comparison NOT_ESTABLISHED/NOT_DONE; aggregate NOT_AUTHORIZED.

## Continuity / duplicate rejection
- PAK belongs to the fixed 63-country Q2-2026 synchronous dual-leg cohort. Repository search found no dedicated PAK Q2-2026 national portfolio-flow validation report. The existing IMF panel and cohort were reused as a roster only; no IMF re-query and no cohort rebuild.
- Prior completed IMF panel/receipt, 9,299-row QA, and other country reports were not repeated.

## Official SBP evidence
1. SBP Economic Data catalogue: https://www.sbp.org.pk/economic-data
   - Lists “Summary Balance of Payments as per BPM6 - Quarterly” as quarterly, with current catalogue result showing coverage through June 2026 / latest listing dated 17-Nov-2026.
   - Separately lists “Core Set of Portfolio Investment Assets data” as half-yearly, last updated 15-Jan-2026.
   - The catalogue listing establishes dataset existence/frequency only; it does not itself provide Q2 portfolio transaction values or asset/liability field definitions.
2. SBP EasyData dataset listing: https://easydata.sbp.org.pk/apex/f?p=10:210:8439371819372:
   - “Summary of Balance of Payments as per BPM6” is quarterly, Sep-2002 through Jun-2026, last release 18-Aug-2026.
   - This is a quarterly BOP dataset listing; in this session the EasyData report page timed out and no raw observation export, series metadata, response receipt or SHA-256 was obtained.
3. SBP Summary Balance of Payments as per BPM6 — September 2026:
   https://www.sbp.org.pk/assets/document/Balancepayment_BPM6.pdf
   - Public table is in million USD and includes Jul-Jun FY26 revised cumulative values, September FY26 monthly values, and Jul-Sep FY26/FY27 aggregates. Portfolio Investment is broken down into Portfolio Investment Abroad and Portfolio Investment in Pakistan, with equity/fund shares and debt securities. However, the inspected table does not provide an April-June 2026 quarterly column; Jul-Jun FY26 cumulative and Sep FY26 monthly values cannot isolate Q2 2026.
   - Footnote marks R as revised and P as provisional. Source note says data are collected from multiple sources; ITRS cash-basis data receive accrual adjustments and reinvested earnings are estimated. This is relevant vintage/accounting context, not an observation-specific Q2 revision history.
4. SBP “Pakistan-Core Set of Portfolio Investment Assets Data”:
   https://www.sbp.org.pk/ecodata/CPIS-Sdds-Assets-Data.pdf
   - Search-indexed official document is labelled End-June 2025, Million Rupees, and presents equity and debt securities held abroad by country plus grand totals. It is a position/stock snapshot, not Q2-2026 BOP transaction flows; it is not admitted to A_NFA_T and provides no liability leg.
5. SBP archive page:
   https://archive.sbp.org.pk/ecodata/index2.asp
   - Lists “Balance of Payment on Calendar Year Basis” quarterly with an Excel format and June-17-2026 update, but no inspected raw workbook or Q2 portfolio component observations were acquired. Do not assume that this archived calendar-year dataset is identical to the newer BPM6 quarterly series without inspecting the workbook metadata and definitions.

## Fail-closed acceptance boundary
- PAK fixed-cohort membership / IMF two-leg panel availability: PASS at panel level only (inherited from existing cohort evidence).
- Official SBP quarterly BPM6 BOP dataset discovery through Jun-2026: PASS (catalogue metadata only).
- Q2-2026 separate portfolio asset transaction value: NOT_EXTRACTED.
- Q2-2026 separate portfolio liability transaction value: NOT_EXTRACTED.
- Calendar-quarter vs fiscal-year mapping and exact reference-period definition: NOT_ESTABLISHED.
- CPIS half-yearly assets data: NOT_APPLICABLE to transaction-flow comparison (stock/position, end-June-2025).
- Sign mapping: NOT_ESTABLISHED.
- Same-vintage bridge to IMF Q2 panel: NOT_ESTABLISHED.
- Numeric dual-leg comparison: NOT_DONE.
- PAK national validation: PARTIAL/BLOCKED / NOT PASS.
- 63-country aggregate: NOT_AUTHORIZED.

## Next exact action
Use the official SBP quarterly BPM6 EasyData export or the documented archive workbook to retrieve the exact Q2-2026 portfolio asset and liability transaction rows with units, period labels, revision flags, source/vintage metadata and raw-byte hashes. First verify whether the reported quarter is calendar 2026-Q2 or a fiscal-year quarter. If the export is unavailable or only net/cumulative values are published, retain the blocker and move to the next eligible fixed-cohort member. Do not substitute CPIS stocks, monthly foreign-investment net inflows, FY cumulative totals, or broad financial-account totals.

## Invariants
No IMF re-query, no cohort rebuild, no synthetic values, no imputation/forward-fill, no stock-flow substitution, no inferred sign/vintage, no netting, no aggregate admission, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E and IPO-PLX V2 remain unchanged.


## Continuation 51 addendum — official quarterly table located; Q2-2026 component values extracted (2026-11-20)
- Fresh official SBP source review found a distinct quarterly calendar-year BPM6 PDF: https://www.sbp.org.pk/assets/document/BPM6_c.pdf . Its header explicitly labels quarterly columns Q1/Q2/Q3/Q4 for CY25, then Q1/Q2/Q3 for CY26; the CY26 Q2 column is marked revised (R). Units are million US dollars.
- In the CY26 Q2 (R) column, SBP publishes “Portfolio investment abroad” = -2 USD million and “Portfolio investment in Pakistan” = -243 USD million. The source separately identifies the portfolio asset-side and liability-side categories and disaggregates each into equity/fund shares and debt securities. This supersedes the earlier claim that no Q2-specific portfolio component values had been extracted.
- Exact column mapping was read from the table's two header rows: after CY25 Q1, Q2, Q3(R), Q4(R), and CY25(R), the next columns are CY26 Q1(R), CY26 Q2(R), CY26 Q3(P). Q2 values are therefore not derived from FY cumulative or monthly data.
- This is a source-value extraction PASS only. The PDF table does not, in the inspected excerpt, provide a detailed BPM6 sign/definition note linking the signed “abroad/in Pakistan” labels to IMF A_NFA_T and L_NIL_T. Do not automatically equate signs or treat -2/-243 as normalized IMF values. Exact IMF PAK Q2 row was not independently retrieved from the already archived panel in this bounded step; no comparison values copied or reconstructed.
- SBP marks CY26 Q2 as revised (R), but the exact revision release timestamp/history and IMF observation-vintage alignment remain NOT_ESTABLISHED. No raw PDF bytes/headers or SHA-256 were captured in this task; do not claim a raw hash.
- Updated PAK gates: official source discovery PASS; Q2-2026 portfolio asset/liability published values extracted PASS (source table precision USDm); sign/definition crosswalk NOT_ESTABLISHED; IMF exact-row reconciliation NOT_DONE; same-vintage NOT_ESTABLISHED; numeric dual-leg comparison NOT_DONE; PAK national validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next exact action: retrieve the archived IMF PAK Q2 exact A_NFA_T and L_NIL_T observation rows from the existing raw/panel archive (without re-querying IMF), inspect the SBP BPM6 table's official methodology/sign definitions and compare the two legs separately within SBP's USDm display precision. Then seek the SBP revision timestamp/vintage bridge. Do not net the two legs or infer a sign flip.
- New source: https://www.sbp.org.pk/assets/document/BPM6_c.pdf ; official search/open citation source page indexed 2026-11-20.
- No production changes, no cohort rebuild, no new IMF request, no synthetic values, no stock-flow substitution, no netting or aggregate admission. All protected V11.3 invariants remain unchanged.


## Continuation 52 — archived IMF dual-leg reconciliation and SBP BPM6 sign crosswalk (2026-11-20)

### Exact archived IMF rows (no new IMF query)
- Reused existing raw archive files; Git blob SHAs:
  - `docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`: `15449e87c9057291a1f52f2f8cd9805df55f9fb8`
  - `docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`: `15f379dc42e2760eb5f2384618e48f5ddc3177f1`
- Exact PAK Q2-2026 asset row: `dataflow,IMF.STA:BOP(21.0.0),R,PAK,A_NFA_T,P_F,USD,Q,2026-Q2,-2000000,6,6,,,,,,,,,,,,O,,,,true,,`
- Exact PAK Q2-2026 liability row: `dataflow,IMF.STA:BOP(21.0.0),R,PAK,L_NIL_T,P_F,USD,Q,2026-Q2,-243000000,6,6,,,,,,,,,,,,O,,,,,,`
- Both rows carry ACTION=R, UNIT=USD, FREQUENCY=Q, TIME_PERIOD=2026-Q2, SCALE=6, PRECISION=6.

### Official SBP methodology and dual-leg comparison
- SBP BPM6 revision notice (16-Aug-2013): https://www.sbp.org.pk/departments/stats/Notice/BPM6-Revision-16-Aug-13.pdf . It states that in the financial account increases in assets and liabilities are positive and decreases are negative; its comparison table separately identifies portfolio investment in Pakistan and portfolio investment abroad (PDF text lines 49-57 and 66).
- SBP FY23 BPM6 introduction: https://www.sbp.org.pk/publications/bop/BOPFY23/Intro.pdf . It states that the financial account presents net acquisition of financial assets (NAFA) and net incurrence of liabilities (NIL), with positive changes indicating increases and negative changes indicating decreases (PDF text lines 62-76).
- SBP CY26 Q2(R) table in https://www.sbp.org.pk/assets/document/BPM6_c.pdf publishes (USD million) Portfolio investment abroad = -2 and Portfolio investment in Pakistan = -243.
- Separate comparison: abroad/asset leg: SBP -2 USDm vs IMF A_NFA_T -2 USDm; difference 0 USDm. In-Pakistan/liability leg: SBP -243 USDm vs IMF L_NIL_T -243 USDm; difference 0 USDm. No netting.
- Result: exact dual-leg numeric agreement at SBP's published USDm precision. SBP's BPM6 methodology supports the sign interpretation (negative = decrease) and NAFA/NIL financial-account framework. This is a source-supported conceptual crosswalk, not proof the underlying raw transaction compilation is identical.

### Vintage and acceptance boundary
- SBP CY26 Q2 column is marked revised (R); IMF raw observation rows also carry ACTION=R. This is consistent revision-status metadata, not proof of same-vintage timing. Exact SBP revision timestamp, IMF extraction timestamp/vintage bridge, and revision-history identity remain NOT_ESTABLISHED.
- PAK gates: existing IMF row extraction PASS; SBP official BPM6 sign/framework source PASS; dual-leg numeric comparison 2/2 PASS at USDm display precision; national source/IMF conceptual mapping SUPPORTED; exact same-vintage NOT_ESTABLISHED; complete national validation PARTIAL (not PASS); aggregate admission NOT_AUTHORIZED.
- No SHA-256 for SBP PDF/raw downloaded bytes is claimed; only Git blob SHAs for archived IMF raw CSVs are recorded.
- No IMF re-query, no fixed cohort rebuild, no synthetic/filled values, no sign inversion, no netting, no production changes, no workflow run triggered.

### Next exact action
- Inspect the SBP Data Revision Policy and identify an official, dated revision/vintage history for the CY26 Q2(R) portfolio rows; compare it with IMF archived observation vintage metadata if available. If no observation-specific history is publicly exposed, retain same-vintage as UNKNOWN and move to the next unvalidated country rather than infer it.
