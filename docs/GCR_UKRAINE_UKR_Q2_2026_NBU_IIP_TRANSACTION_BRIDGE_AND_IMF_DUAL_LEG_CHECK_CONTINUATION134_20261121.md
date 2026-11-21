# Ukraine UKR Q2-2026 — NBU IIP transaction-column dual-leg bridge and archived IMF comparison
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 134

## Decision
Official NBU Q2-2026 IIP reconciliation provides separate portfolio transaction changes (not closing stocks): assets +USD 159m and liabilities +USD 34m. Exact archived IMF Q2 rows are +USD 159m and +USD 34m after the bounded country-specific OBS_VALUE/10^6 display comparison; both match exactly at NBU whole-USD-million precision. Transaction-column extraction and numerical dual-leg cross-check PASS. Same-vintage/revision equivalence and formal IIP-transaction-to-BOP table identity remain NOT_ESTABLISHED; UKR remains PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## 1. Continuity preflight and selection
- Re-fetched current Master Continuity Ledger, GCR Priority Queue, fixed 63-country cohort, TJK Continuation 113, TLS Continuation 117 and TZA Continuation 119. Prior PASS work excluded; no cohort rebuild.
- TJK NBT publication period remains ambiguous (archive link label says Q2, PDF filename says H1 and PDF bytes inaccessible); no standalone Q2 legs or same-vintage Q1 basis. Closed this route at BLOCKED/NOT_CAPTURED and advanced.
- TLS BCTL live series latest observation is Q1-2025 and export workbook is Q3-2025 vintage; H1-2026 is net-only. Closed current public routes as stale/NOT_AVAILABLE for Q2-2026 and advanced.
- TZA official BoT Table 6.1 contains Q2 portfolio investment only as net -USD 14.0m; assets and liabilities are not separate rows. No net-to-leg back-solving. The TZA report directs next to UKR; UKR is in the immutable cohort.
- No IMF query and no cohort rebuild.

## 2. Official NBU Q2-2026 source — transaction changes, not stocks
- Official National Bank of Ukraine Q2 IIP publication: https://roundtable.bank.gov.ua/files/ES/IIP_q.pdf
- Section 1.2: International Investment Position as of end-Q2 2026; unit USD million; document last updated 23-Sep-2026.
- Q2 table columns: opening position at 31-Mar-2026; changes due to transactions (8−4); exchange-rate/price/other changes; component revaluations; total changes; closing position at 30-Jun-2026.
- Portfolio investment — ASSETS row (PDF/text lines 329–330): opening stock 5,552; transaction changes +159; other change components separately itemized; closing stock 5,730 USDm.
- Portfolio investment — LIABILITIES row (PDF/text lines 449–450): opening stock 32,920; transaction changes +34; other change components separately itemized; closing stock 32,914 USDm.
- Use only the explicit changes-due-to-transactions column (+159, +34). Do not use opening/closing positions or total stock changes as flows. This is an IIP reconciliation transaction component, not a separate standalone BOP table row; formal identity to the published BOP financial-account series remains to be documented.

## 3. Existing archived IMF Q2-2026 exact rows — no re-query
- Asset file docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv; blob SHA 15449e87c9057291a1f52f2f8cd9805df55f9fb8. Exact UKR row: A_NFA_T, P_F, USD, Q, 2026-Q2, OBS_VALUE=159000000, SCALE=6, PRECISION=6, DERIVATION_TYPE=O, IFS_FLAG=true.
- Liability file docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv; blob SHA 15f379dc42e2760eb5f2384618e48f5ddc3177f1. Exact UKR row: L_NIL_T, P_F, USD, Q, 2026-Q2, OBS_VALUE=34000000, SCALE=6, PRECISION=6, DERIVATION_TYPE=O; IFS_FLAG blank.
- Both raw rows are Q2-2026, USD, quarterly, country UKR. Raw OBS_VALUE and SCALE preserved independently. No IMF query and no synthetic values.

## 4. Numeric comparison — country-specific bounded display check
- NBU IIP transaction column: assets +159 USDm; liabilities +34 USDm.
- Archived IMF raw OBS_VALUE/10^6 candidate display: assets 159 USDm; liabilities 34 USDm.
- Residuals: assets 0.000 USDm; liabilities 0.000 USDm at NBU whole-million display precision; arithmetic identity (assets minus liabilities) = +125 USDm in both representations.
- Both separate-leg numeric comparisons PASS at displayed precision.
- This is a UKR Q2-specific empirical cross-check only. Do not generalize /10^6 to other countries or alter archived OBS_VALUE/SCALE. No FX conversion is needed because both sources are in USD.

## 5. Vintage and definition boundaries
- NBU IIP Q2 publication last-updated 23-Sep-2026. NBU changes/revision PDF https://roundtable.bank.gov.ua/admin_uploads/article/Changes_ES.pdf last updated 23-Sep-2026 lists BOP revisions through Q1-2026, not Q2-2026. Absence of Q2 from that list is not proof of identical source vintage or no subsequent Q2 revision.
- NBU public BOP quarterly analytical PDF https://bank.gov.ua/files/ES/BOP_q.pdf states last update 18-Sep-2025 and carries data only through Q2-2025; it is stale and cannot serve as a Q2-2026 BOP table.
- Official NBU methodology says BOP is compiled quarterly and prior periods can be revised quarterly; monthly BOP estimates are adjusted after quarterly BOP release. This supports the need for a vintage gate, not a same-vintage PASS.
- Q2 period match PASS; USD unit match PASS; separate transaction legs PASS; numeric display cross-check PASS; explicit IIP transaction-column ↔ BOP P_F same-vintage/source-definition equivalence NOT_ESTABLISHED; Q2 revision/vintage bridge NOT_ESTABLISHED.
- UKR status PARTIAL / NOT PASS. Aggregate / production admission NOT_AUTHORIZED.

## 6. Exact next actions
1. Locate an official NBU Q2-2026 BOP analytical/standard presentation file or SDMX/API series from a distinct current data route, then confirm the same +159/+34 transaction legs and release vintage.
2. If current BOP series is not publicly retrievable, preserve the IIP transaction-column cross-check as a corroborating official flow component, but keep formal BOP equivalence open.
3. Obtain any Q2-specific revision notice after 23-Sep-2026 before asserting same-vintage alignment.
4. No generic IIP stock substitution, no net-to-leg inference, no arbitrary FX, no IMF re-query, no cohort rebuild.

## 7. Sources
- NBU Q2-2026 IIP: https://roundtable.bank.gov.ua/files/ES/IIP_q.pdf
- NBU BOP analytical series (stale; last update 18-Sep-2025): https://bank.gov.ua/files/ES/BOP_q.pdf
- NBU revision list (updated 23-Sep-2026): https://roundtable.bank.gov.ua/admin_uploads/article/Changes_ES.pdf
- NBU BOP methodology: https://bepsinua.bank.gov.ua/admin_uploads/article/BoP_methodological_notes_en.pdf
- IMF archived raw asset/liability files and blob SHAs are recorded above.

## 8. Protected invariants
₹0; official/free sources only. No synthetic data, no inferred sign/scale conversion, no stock-as-flow, no net-to-leg inference, no arbitrary FX, no annual-to-quarter proration, no cohort rebuild, no IMF re-query, no aggregate admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.