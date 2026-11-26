# GCR Continuation 263 — Serbia SRB Q2-2026 NBS September 2026 Bulletin Table 2.3 dual-leg capture
Date: 2026-11-26
Scope: research-only national-source capture for the immutable 63-country Q2-2026 cohort.

## 1. Preflight and duplicate prevention
- Re-fetched the current Master Continuity Ledger, GCR Priority Queue, Historical Task Registry and 63-country matrix; searched the Library Mother File and prior conversation records.
- Reused the fixed cohort and archived IMF raw files. No IMF re-query, cohort rebuild, workflow dispatch, or production change.
- Skipped completed/closed work: C262 Samoa dual-leg capture; C259 Montenegro attachment annotation boundary; C260 Cabo Verde duplicate XLS route closure; C261 Georgia future Q3 publication trigger.
- MNG C234/C235 route-contract and .px-suffix tests were reviewed. The exact metadata route had already been attempted and closed in C235; no repeated API call is claimed as new evidence.
- SRB C233 July bulletin route fingerprint was not repeated. A distinct official September 2026 Statistical Bulletin PDF is now directly accessible, giving a new source issue and an internally headed monthly table.

## 2. New official source
- National Bank of Serbia, Statistical Bulletin — September 2026:
  https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_09_26.pdf
- Table 2.3, “Balance of Payments of the Republic of Serbia (BPM6)”, printed page 105 / PDF page corresponding to the Table 2.3 section.
- Unit: million euros; preliminary data.
- The table header explicitly pairs 2025 and 2026 for each month January–August. For 2026 Q2 the relevant month columns are April, May and June.
- Table note: presentation is as far as possible in line with IMF BPM6; data are subject to correction in line with changes in official data sources; table data were available until 17-Sep-2026.
- Official bulletin index also lists September 2026 as the latest statistical bulletin and its release date as 4-Nov-2026.

## 3. Q2-2026 portfolio legs captured from monthly flows
Table 2.3 rows:
- 3.2.A Portfolio investment assets (2026 monthly values): April +149, May −25, June +124 EUR million.
- 3.2.B Portfolio investment liabilities (2026 monthly values): April −19, May +3,932, June +199 EUR million.
- 3.2 Portfolio investment, net (= asset − liabilities): April +168, May −3,957, June −75 EUR million.

Quarterly arithmetic from the three monthly flow observations:
- Assets: 149 − 25 + 124 = **+248 EUR million**.
- Liabilities: −19 + 3,932 + 199 = **+4,112 EUR million**.
- Net: 168 − 3,957 − 75 = **−3,864 EUR million**.
- Internal identity: 248 − 4,112 = −3,864; the monthly row values also reconcile month-by-month (149 − (−19)=168; −25−3,932=−3,957; 124−199=−75).

These are transaction-flow legs, not IIP stocks. The unusually large May 2026 liability value (+3,932 EURm) is retained exactly as published; it is not smoothed, dropped, or interpreted as error. The table's preliminary status and correction note remain attached to the evidence.

## 4. Existing IMF rows reused without query
Source files:
- Asset: `docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`; Git blob SHA `15449e87c9057291a1f52f2f8cd9805df55f9fb8`.
  - SRB, A_NFA_T, P_F, USD, Q, 2026-Q2; OBS_VALUE=288993091.8400176; SCALE=6; PRECISION=6; DERIVATION_TYPE=O.
- Liability: `docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`; Git blob SHA `15f379dc42e2760eb5f2384618e48f5ddc3177f1`.
  - SRB, L_NIL_T, P_F, USD, Q, 2026-Q2; OBS_VALUE=4782903852.31975; SCALE=6; PRECISION=6; DERIVATION_TYPE=O.
- Raw IMF values and metadata are preserved exactly. No conversion from EUR to USD, numeric residual, or same-vintage match is asserted. No new IMF query was made.

## 5. Acceptance boundary
- Official source identity / Table 2.3 / BPM6 label / monthly 2026 Q2 asset and liability rows: CAPTURED.
- Quarterly aggregation and internal arithmetic: PASS as a deterministic sum/identity of the published monthly values.
- National-vs-IMF numeric comparison: REVIEW, because the national table is EUR million while IMF raw rows are USD and no transaction-consistent FX conversion was applied.
- Same-vintage/revision bridge: PENDING. The national table is preliminary and based on data available until 17-Sep-2026; the archived IMF extract is dated 19-Nov-2026. These dates do not prove same-vintage.
- Raw PDF bytes, byte count, local SHA-256 and retrieval receipt: NOT_CAPTURED in this task; do not fabricate.
- SRB remains DATA_CAPTURED / PARTIAL / NOT PASS; asset REVIEW; liability REVIEW; vintage PENDING; full_pass NO; aggregate NOT_AUTHORIZED.

## 6. Next action
Only pursue a documented NBS transaction-period EUR/USD conversion methodology and observation-specific revision/vintage bridge. If these cannot be established, retain REVIEW/PENDING and move to the next eligible fixed-cohort country. Do not repeat C233 July PDF/XLS route, do not infer vintage from issue date, and do not substitute an IIP stock or a net-only summary.

## 7. Invariants
₹0 research spend; official/free sources only; no synthetic rows, fabricated timestamps, unsupported conversion or proxy substitution; UNKNOWN is neither PASS nor FAIL; no IMF re-query/cohort rebuild; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2.0 unchanged; no merge, workflow dispatch or production integration without explicit approval.
