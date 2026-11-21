# Sri Lanka LKA — Q2-2026 CBSL / Treasury BOP portfolio dual-leg reconciliation (Continuation 174)
Date: 2026-11-21 (Asia/Kolkata)
Decision: FIXED-COHORT MEMBERSHIP PASS; NO PRIOR DEDICATED LKA Q2-2026 NATIONAL DUAL-LEG RECONCILIATION FOUND IN SCOPED REPOSITORY SEARCH; OFFICIAL MINISTRY OF FINANCE TABLE 7 REPORTS SEPARATE Q2 PORTFOLIO ASSET AND LIABILITY LEGS, ATTRIBUTED TO CBSL AND PROVISIONAL; BOTH LEGS NUMERICALLY AGREE WITH ARCHIVED IMF RAW VALUES AFTER ROUNDING TO USD MILLION; SAME-VINTAGE REVISION METADATA AND ORIGINAL CBSL RAW EXPORT NOT_CAPTURED; LKA STRONG DUAL-LEG RECONCILIATION / PROVISIONAL, NOT FINAL SAME-VINTAGE PASS; AGGREGATE AUTHORIZATION NOT_GRANTED.

## 1. Continuity preflight and duplicate prevention
- Re-fetched Master Continuity Ledger (pre-task blob SHA `88f694a8af4793715810380c1e3bf0f4e921ce66`), GCR Master Priority Queue (`7d742565e7e2b099ffaf8a1c684a2ea1bc22025e`), Historical Task Registry (`938636639de375276fda97206e07c65a4ec500fd`), and immutable Q2-2026 cohort (blob SHA `31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`).
- Re-fetched LAO Continuation 173 report (blob SHA `645c762c92ad7c2e8fbb0246aec55606ab0fbe10`). LAO remains PARTIAL; its identical failed BOL links were not retried.
- Repository searches for `LKA Sri Lanka Q2-2026 portfolio assets liabilities` and `Sri Lanka CBSL BOP Q2 2026 dual leg` returned no prior dedicated LKA national dual-leg reconciliation report in scoped repository search.
- Exact immutable cohort row: `LKA,Sri Lanka,2026-Q2,A_NFA_T_PRESENT,L_NIL_T_PRESENT,BOTH_LEGS_PRESENT_IN_IMF_PANEL,NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING,NOT_AUTHORIZED`. No cohort rebuild and no IMF re-query.

## 2. National official source — Ministry of Finance report, Table 7
- Official source: Ministry of Finance, Planning and Economic Development, Sri Lanka, *Budget Economic and Fiscal Position Report – 2027*, issued 12-Nov-2026 under the Public Financial Management Act; official PDF: https://treasury.gov.lk/api/file/04b45c52-3ded-4621-86c7-b8c67455c9d8 .
- Table 7, “Balance of Payments – 2026”, page 102, unit USD million, gives separate rows for “Portfolio Investment: Assets” and “Portfolio Investment: Liabilities” for 2026 Q1 and Q2.
- Q2-2026 national published figures: Portfolio Investment Assets = +26 USD million; Portfolio Investment Liabilities = -351 USD million.
- Both are marked provisional by footnote (a). Table source line explicitly says “Source: Central Bank of Sri Lanka”. This is an official Ministry reproduction with explicit CBSL source attribution; the primary CBSL statistical tables page could not be opened in this retrieval session (HTTP 403), so the original CBSL workbook/raw bytes were not directly captured.
- Table 7 is BOP financial-account transaction data, not IIP stocks. It separates assets and liabilities and therefore satisfies the required national dual-leg shape at published rounded precision.

## 3. Archived IMF raw observation rows — reused, not re-queried
- Asset raw file: `docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`; Git blob SHA `15449e87c9057291a1f52f2f8cd9805df55f9fb8`.
- Exact LKA asset row: `dataflow,IMF.STA:BOP(21.0.0),R,LKA,A_NFA_T,P_F,USD,Q,2026-Q2,25676196.5415909,6,6,,,,,,,,,,,,O,,,,true,,`.
- Liability raw file: `docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`; Git blob SHA `15f379dc42e2760eb5f2384618e48f5ddc3177f1`.
- Exact LKA liability row: `dataflow,IMF.STA:BOP(21.0.0),R,LKA,L_NIL_T,P_F,USD,Q,2026-Q2,-350932889.850796,6,6,,,,,,,,,,,,O,,,,,,`.
- No fresh IMF request or data extraction was made.

## 4. Numeric reconciliation
| Leg | National Table 7 (USD mn, provisional, rounded) | Archived IMF raw (USD) | IMF converted to USD mn | Difference vs national rounded value |
|---|---:|---:|---:|---:|
| Portfolio investment assets | +26 | +25,676,196.5415909 | +25.6761965416 | -0.3238034584 |
| Portfolio investment liabilities | -351 | -350,932,889.850796 | -350.9328898508 | +0.0671101492 |
- At whole-USD-million rounding, IMF values reproduce the national published Q2 values: +25.676m → +26m; -350.933m → -351m.
- Both legs agree independently; no net-to-leg back-solving was used.
- National report marks Q2 values provisional. IMF raw observation revision/vintage date is not supplied in the extracted row; the two sources' exact revision cut-off equivalence is therefore NOT_ESTABLISHED.
- This is a strong independent two-leg numerical cross-check at the national report's stated precision, but not a final same-vintage raw-source hash validation.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| LKA fixed 63-country Q2 cohort membership | PASS |
| Prior dedicated LKA report absent in scoped repository search | PASS (scoped search only) |
| Official national report and Q2 Table 7 located | PASS |
| Explicit CBSL source attribution | PASS |
| Separate national portfolio asset and liability legs | PASS |
| Q2 national values and USD-million unit | PASS (provisional, rounded) |
| Archived IMF asset and liability rows | PASS (existing raw archive) |
| Asset numerical reconciliation at published rounding | PASS |
| Liability numerical reconciliation at published rounding | PASS |
| Same-vintage / revision cutoff bridge | NOT_ESTABLISHED |
| Original CBSL raw XLSX / raw bytes / SHA-256 | NOT_CAPTURED |
| Ministry PDF raw bytes / SHA-256 in local archive | NOT_CAPTURED |
| LKA validation classification | STRONG DUAL-LEG RECONCILIATION / PROVISIONAL; FINAL SAME-VINTAGE PASS PENDING |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 6. Rejected list
- Macro Lab series pages are secondary derived presentation and were not used as national evidence.
- IIP portfolio investment stocks are excluded; only BOP Table 7 transaction rows were used.
- Financial Account net (-668) and Portfolio Investment (Net) figures are not substituted for the two legs.
- No back-solving, annual/H1 substitutions, sign changes or FX conversion.
- Do not promote provisional values to final or claim exact revision-vintage equivalence.

## 7. Next exact action
1. Obtain the underlying CBSL Table 2.10 quarterly BPM6 statistical-table export and its metadata if an accessible official download route exists; capture exact URL, timestamp, content type, byte count and SHA-256.
2. Establish the release/revision date of the IMF Q2 rows and compare it to the 12-Nov-2026 national report vintage / underlying CBSL table vintage.
3. If source-vintage bridge is confirmed and primary CBSL raw source is captured, upgrade LKA to final national dual-leg PASS; otherwise retain provisional strong reconciliation.
4. Update aggregate only after the full cohort-wide acceptance criteria are met; current aggregate remains NOT_AUTHORIZED.

## 8. Protected invariants
No production code/configuration, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, weights, gates or alerts changed. No IMF re-query, cohort rebuild, paid API, synthetic data, fabricated timestamp, unsupported sign/scale/FX conversion, stock-as-flow substitution or acceptance relaxation. Research spend ₹0. UNKNOWN is never PASS.
