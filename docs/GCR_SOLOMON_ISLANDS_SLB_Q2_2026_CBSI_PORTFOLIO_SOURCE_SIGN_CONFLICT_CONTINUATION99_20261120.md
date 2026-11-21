# Solomon Islands SLB Q2-2026 — CBSI portfolio dual-leg source gate and sign-conflict audit
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44, Part-4 / Continuation 99
Decision: **SLB fixed-cohort membership PASS; official CBSI BPM6 quarterly BOP source PASS; Q2-2026 table reports portfolio financial-asset transactions SBD 38m and liability dash (general note defines dash as nil); narrative says portfolio investment deficit SBD 38m, creating unresolved sign/presentation conflict; exact IMF rows and SBD/USD transaction bridge NOT_CAPTURED; SLB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight / PASS work excluded
- Re-fetched current Master Continuity Ledger (blob SHA `1194f809a00a214913a5535969d3f80111e5fd1e`), GCR Master Priority Queue (blob SHA `15501663d5fbb531e220c5cc2546400477e550b2`), Rwanda Continuation 98 (blob SHA `001cc1fc2d6f698566206a7e746871d9eba1ee90`), and immutable 63-country Q2-2026 both-leg cohort (blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`).
- Reused existing Saudi Arabia (SAU) reconciliation and source-vintage follow-up: numeric two-leg check had already passed at displayed rounding, but exact same-vintage identity remains unresolved; did not repeat SAU.
- SLB (Solomon Islands) is the next fixed-cohort member after RWA and is present with both IMF A_NFA_T and L_NIL_T entries.
- Repository searches for SLB / Solomon Islands Q2-2026 national portfolio reconciliation found no dedicated prior country report. No cohort rebuild and no new IMF request.

## 2. Official CBSI source and BPM6 basis
- Central Bank of Solomon Islands (CBSI) official Balance of Payments page states the quarterly and annual BOP series covers current, capital and financial accounts and is based on BPM6. It states latest BOP statistics are 2026-Q2.
- CBSI Quarterly Review, June 2026, Chapter IV and Statistical Annex Table 1.17, “Capital Account and Financial Account”, reports annual and quarterly data, unit SBD million, quarterly columns through 2026-Q2, source CBSI.
- The publication general note says “-” means nil and warns that data are subject to periodic revision as updated information becomes available.
- Official page and PDF are cited below. Web text extraction exposed the table content. A direct container download attempt failed; no original PDF bytes, response headers, retrieval receipt, byte count or SHA-256 are claimed.

## 3. Q2-2026 national portfolio transaction table
CBSI Quarterly Review June 2026, Table 1.17 (SBD million), column 2026-Q2:
- Financial Assets total: 540.
- Portfolio investment under Financial Assets: +38.
- Financial Liabilities total: 539.
- Portfolio investment under Financial Liabilities: “-”, which the report's general note defines as nil.
- Other relevant rows: net lending (+)/borrowing (-) from Financial Account = +2.
- This is transaction/financial-account table, not the IIP stock table. Do not use Table 1.14's portfolio IIP asset position of SBD 373m as a transaction flow.

## 4. Material internal sign/presentation conflict — not resolved
- Chapter IV narrative says: “portfolio investment recorded a wider deficit of $38 million” in Q2-2026, compared with deficit of $1 million in Q1-2026.
- Table 1.17 instead displays portfolio financial assets +38 and portfolio financial liabilities nil for Q2-2026.
- The report does not, in the extracted table/narrative context, explain whether the narrative “deficit” refers to a reverse sign convention, net balance, transaction direction or an editorial inconsistency.
- Do not silently choose a sign, flip +38 to -38, or assign a zero liability to IMF L_NIL_T without confirming the CBSI methodology and table semantics. The nil symbol is clear as published, but the crosswalk to IMF's “net incurrence of liabilities” remains unestablished.
- Table 1.17 aggregate financial assets 540 and liabilities 539 with net lending +2 is not a sufficient algebraic proof of portfolio leg sign; other financial-account items and rounding contribute. No inference from aggregate identity is permitted.

## 5. Gate matrix
| Gate | Status |
|---|---|
| SLB in immutable 63-country Q2-2026 both-leg cohort | PASS |
| No prior dedicated SLB Q2 country report found | PASS |
| Official CBSI quarterly BOP source / BPM6 | PASS |
| Latest source period Q2-2026 | PASS |
| Table 1.17 quarterly frequency and SBD million unit | PASS |
| Q2 portfolio financial-asset row | PUBLISHED: +38 SBDm |
| Q2 portfolio financial-liability row | PUBLISHED: nil (“-”) |
| Narrative sign/presentation agreement | BLOCKED / CONFLICT |
| CBSI methodology definition of sign for this table | NOT_ESTABLISHED |
| Exact IMF A_NFA_T and L_NIL_T row values from archived raw panel | NOT_CAPTURED (large panel GitHub fetch returned empty content; no re-query) |
| SBD-to-USD transaction conversion basis | NOT_ESTABLISHED |
| Same-vintage comparison | NOT_DONE |
| SLB national validation | PARTIAL / NOT PASS |
| Aggregate / production admission | NOT_AUTHORIZED |

## 6. Next exact action
1. Locate CBSI official methodology/metadata notes for Table 1.17 and portfolio transaction sign convention; specifically resolve narrative “deficit 38” versus Table 1.17 asset +38/liability nil.
2. Retrieve exact archived IMF SLB 2026-Q2 A_NFA_T and L_NIL_T rows from existing raw/panel evidence without a new IMF query. The committed large panel `docs/evidence/imf_bop_emde_20261119/emde_portfolio_flows.csv` has blob SHA `2a8db2878cac6323bbad74ffa4035dc70e5e6b98`; GitHub text fetch returned zero characters, so the exact rows are not currently exposed by that route.
3. Establish official transaction-period SBD/USD conversion method and source vintage before any currency comparison. Do not use a quarter-end IIP exchange rate or infer conversion.
4. Archive the original CBSI PDF bytes and SHA-256 through a supported direct route before treating this as a fully reproducible numeric source capture.
5. Only after sign, period, units, currency and vintage are established, compare the two legs independently within published precision. Otherwise preserve PARTIAL / NOT PASS and advance within fixed cohort.

## 7. Official evidence
- CBSI Balance of Payments statistics page (BPM6; latest 2026-Q2): https://www.cbsi.com.sb/data-statistics/economic-statistics/balance-payments
- CBSI Quarterly Review — June 2026 (Chapter IV; Table 1.17, pp. 12 and 44; source PDF): https://www.cbsi.com.sb/sites/default/files/2026-10/June%202026%20Qarterly%20Report%20final.pdf
- CBSI Quarterly Reviews index: https://www.cbsi.com.sb/publications/major-reports/quarterly-reviews
- Solomon Islands National Statistics Office BOP page (states CBSI is compiler/disseminator): https://statistics.gov.sb/balance-of-payments/

## 8. Protected invariants
No cohort rebuild, no IMF re-query, no net-to-leg inference, no sign flip, no IIP-stock-as-flow, no inferred FX, no netting, no synthetic data, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 remain unchanged. UNKNOWN is never PASS. Research spend ₹0.


## Continuation 132 — CBSI sign semantics and archived IMF raw rows extracted (2026-11-21)

### Fresh continuity preflight
- Re-fetched current Master Continuity Ledger, GCR Priority Queue, immutable 63-country cohort, Batch-1 report and this SLB Continuation 99 report. SLV Continuation 131 is recorded; SLB is the next unresolved batch item. No PASS work repeated.
- Reused existing IMF archive only; no IMF query, no cohort rebuild.

### CBSI Q2-2026 table and narrative sign reconciliation
- Re-opened official CBSI Quarterly Review June 2026 PDF. Table 1.17 (pp.43–44; PDF extracted lines 2814–2865) labels the table Capital and Financial Account, SBD million, annually and quarterly. Q2-2026: financial assets 540; portfolio investment asset subcomponent +38; financial liabilities 539; portfolio investment liability dash, which the report general note defines as nil. Table says BPM6 statistics; source CBSI.
- Chapter IV lines 772–775 says financial account net surplus +27 and portfolio investment deficit 38, versus deficit 1 in Q1. This is not necessarily a sign contradiction: under BPM6, +38 net acquisition of assets and zero liability contributes +38 to net lending (assets minus liabilities), equivalently -38 when described from a net-inflow/deficit perspective (liabilities minus asset acquisition). This is a conceptual reconciliation, not an explicit CBSI definition of the word deficit.
- IMF BPM6 Compilation Guide and BPM6 crosscutting chapter state positive financial-account values indicate increases in assets/liabilities, negative values indicate decreases, and net lending/borrowing equals net acquisition of assets minus net incurrence of liabilities. CBSI BOP page says its quarterly/annual series is BPM6-based. Do not flip the published +38 asset row.
- Historical CBSI Quarterly Review June 2015 Table 1.17 note explicitly says negative financial-account subcomponents signify a reduction or withdrawal. Consistent with positive = increase, but historical corroboration only.

### Exact IMF rows retrieved from existing archived raw CSVs
- GitHub fetch_file successfully returned complete archived raw CSVs (the earlier normalized-panel fetch was empty; the separate raw leg files are accessible).
- Asset file docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv; blob SHA 15449e87c9057291a1f52f2f8cd9805df55f9fb8; 4,728 lines including header. Exact SLB row: COUNTRY=SLB, ENTRY=A_NFA_T, INDICATOR=P_F, UNIT=USD, FREQUENCY=Q, PERIOD=2026-Q2, OBS_VALUE=4675384.136569459, SCALE=6, PRECISION=6, DERIVATION_TYPE=O, IFS_FLAG=true.
- Liability file docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv; blob SHA 15f379dc42e2760eb5f2384618e48f5ddc3177f1; 4,663 lines including header. Exact SLB row: COUNTRY=SLB, ENTRY=L_NIL_T, INDICATOR=P_F, UNIT=USD, FREQUENCY=Q, PERIOD=2026-Q2, OBS_VALUE=0, SCALE=6, PRECISION=6, DERIVATION_TYPE=O; IFS_FLAG blank.
- Both rows are from the existing IMF archive vintage captured 2026-11-19. Raw OBS_VALUE and SCALE preserved independently.

### Conditional numeric plausibility check — not a conversion PASS
- CBSI Q2 table: +38 SBDm assets, nil liabilities. The same report's exchange-rate section reports Q2 quarterly average SBD/USD at 8.08.
- Diagnostic only: if this quarterly average is used provisionally, 38 / 8.08 = 4.702970297 USDm. IMF asset OBS_VALUE / 1,000,000 = 4.675384137 USDm under the bounded display convention previously empirically checked in pilot countries; difference = -0.027586160 USDm. CBSI whole-SBDm rounding bound ±0.5/8.08 = ±0.061881188 USDm, so the candidate asset values are arithmetically consistent within that bound.
- IMF liability raw OBS_VALUE is exactly zero; CBSI liability table displays nil. This is a displayed-zero match, subject to source definition/vintage.
- Critical: the panel research record prohibits universal SCALE conversion; /1e6 has been empirically reconciled for Brazil and India, not SLB. CBSI publishes 8.08 as Q2 quarterly-average FX but does not explicitly state this is the rate used to convert BOP transaction flows. Thus the above is a bounded plausibility check only, not an admitted official FX crosswalk or numeric PASS.

### Remaining blockers and status
- Apparent narrative/table sign conflict: conceptually reconciled by distinguishing asset acquisition/BPM6 net lending from narrative net-outflow/deficit perspective; no sign flip. Exact CBSI definition of narrative deficit remains NOT_EXPLICIT.
- Exact IMF Q2 asset/liability raw rows: RETRIEVED; row identity PASS.
- Same Q2 period: PASS.
- CBSI national values: +38 SBDm assets; liability nil; original PDF bytes/SHA-256 NOT_CAPTURED (browser PDF text only; container byte download failed).
- IMF OBS_VALUE/SCALE preserved; SLB-specific conversion of OBS_VALUE/SCALE to USDm NOT_YET_VALIDATED.
- Official CBSI BOP transaction-period FX conversion method NOT_ESTABLISHED. Quarterly average 8.08 is published context only.
- Asset comparison CONDITIONAL / REVIEW; liability displayed numeric zero matches archived IMF zero but definition/vintage bridge remains REVIEW; full SLB validation PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.
- Next exact action: seek CBSI technical metadata explicitly stating transaction FX conversion method and official definition of portfolio deficit; if unavailable, retain REVIEW and advance beyond fixed batch to next eligible cohort country after preflight. Do not re-query IMF or infer FX.

### Official evidence
- CBSI BOP statistics page: https://www.cbsi.com.sb/data-statistics/economic-statistics/balance-payments
- CBSI Quarterly Review June 2026 PDF: https://www.cbsi.com.sb/sites/default/files/2026-10/June%202026%20Qarterly%20Report%20final.pdf
- CBSI Quarterly Review June 2015: https://www.cbsi.com.sb/wp-content/uploads/2016/06/QR-JUN2015.pdf
- IMF BPM6 Compilation Guide: https://www.imf.org/external/pubs/ft/bop/2011/pdf/guide.pdf
- IMF BPM6 Crosscutting Issues, Chapter 8: https://www.elibrary.imf.org/display/book/9781484312759/ch008.xml

No IMF re-query, no cohort rebuild, no net-to-leg inference, no sign flip, no stock-as-flow, no inferred FX, no synthetic data, no production changes. ₹0; UNKNOWN is never PASS.
