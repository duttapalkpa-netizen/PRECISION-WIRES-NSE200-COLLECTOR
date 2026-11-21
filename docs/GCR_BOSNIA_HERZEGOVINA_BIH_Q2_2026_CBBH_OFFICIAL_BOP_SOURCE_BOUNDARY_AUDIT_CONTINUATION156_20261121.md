# GCR Q2-2026 — Bosnia and Herzegovina (BIH) CBBH official BOP source-boundary audit
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 156
Status: FIXED-COHORT / IMF ROW PRESENCE PASS; OFFICIAL CBBH QUARTERLY BOP SERIES / BPM6 / KM UNIT CONFIRMED; Q2-2026 NATIONAL PORTFOLIO DUAL-LEG VALUES NOT_CAPTURED; BIH PARTIAL / NOT PASS.

## 1. Continuity preflight and duplicate rejection
- Re-fetched current Master Continuity Ledger, GCR Master Priority Queue and immutable 63-country Q2-2026 cohort. BIH is a fixed-cohort member with both A_NFA_T and L_NIL_T rows present in the existing IMF raw panels.
- Repository searches for BIH / Bosnia and Herzegovina Q2-2026 national portfolio dual-leg reports found no dedicated prior country report.
- BGD Bangladesh is not selected: existing report and queue document prior Bangladesh Bank net-only Q2/FY26 Q4 publication, annual PI survey route and NSDP/XML/XLS access boundary; BGD remains BLOCKED / NOT PASS. No repeat.
- No IMF re-query, cohort rebuild, panel rebuild, or re-extraction of previously PASS work.

## 2. Official CBBH Q2-2026 release boundary
- CBBH Advanced Release Calendar identifies “Balance of payments of BH” as quarterly and sets Q2/2026 publication deadline “until 30.09.2026”; IIP is separately quarterly with the same Q2 deadline.
- Official calendar: https://www.cbbh.ba/content/read/29?lang=en
- The current public Quarterly Bulletins archive lists Bulletin 1 2026 and Bulletin 2 2026. The accessible Bulletin 2 2026 (data deadline 18-Aug-2026) contains BOP Table T15 through Q1 2026 only; it is not the Q2 release.
- Official archive: https://www.cbbh.ba/content/archive/35
- Bulletin 2 2026 PDF: https://www.cbbh.ba/content/DownloadAttachment/?id=b75e4e59-9365-49db-94d2-9441be5fff59&langTag=en
- T15 (p.72; PDF text lines 3955–4018) is in KM million and contains separate “Portfolio investment”, “Net acquisition of financial assets” and “Net incurrence of liabilities” rows. The latest quarter in that table is Q1 2026; its portfolio line is -101 KMm, asset net acquisition -101 KMm and liability net incurrence 0 KMm. These are Q1 values only and are not used as Q2 evidence.
- T15 note explicitly states CBBH BOP is compiled under BPM6 and quarterly data for the current year are regularly revised; the current year and four previous years may be revised.
- This confirms official concept layout, unit, methodology and revision boundary for the publication series, but does not supply Q2 2026 transaction legs.

## 3. Official Statistics Portal route — execution boundary
- CBBH’s official Statistics web portal page links “Web portal access” and an application user guide:
  https://www.cbbh.ba/content/read/915
- CBBH official portal user guide (2020):
  https://www.cbbh.ba/data/dokumenti/pdf/panorama_necto_manual_en.pdf
  - States the portal can be accessed by anonymous (unregistered) users; registration is only needed for saving customized workboards in a private directory.
  - Workboards/reports are arranged by language and statistics area; filters allow selection of periods/members.
  - Portal exports support PDF, Excel, Image and Email.
- IMF e-GDDS BOP metadata independently describes CBBH as the sole official BOP compiler; BOP is quarterly, presented in KM million, disseminated in the CBBH Quarterly Bulletin and statistical portal. It documents current-year quarterly revisions and additional four-year revisions when annual surveys become available.
  https://dsbb.imf.org/egdds/dqaf-base/country/BIH/category/BOP00
- The dynamic Panorama Necto portal target listed in the metadata was not accessible through the current browser route:
  http://statistics.cbbh.ba/Panorama/novaview/SimpleLogin_bs_html.aspx
  The exact portal workboard, selected Q2-2026 series, data table, raw export bytes, retrieval timestamp and SHA-256 were not captured. This is a tool-access / execution boundary, not evidence that the data do not exist.
- Next actionable route: use the documented anonymous portal UI, locate BOP financial-account table/workboard, filter 2026-Q2, export the exact Q2 table to Excel/PDF, preserve original bytes and hash, then inspect portfolio asset and liability rows separately. If the portal requires unsupported interactive desktop/browser steps, record NOT_EXECUTED and advance rather than guessing.

## 4. Existing archived IMF Q2-2026 rows reused — no query
From the existing raw IMF panel CSVs:
- Asset file `docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv`, Git blob SHA `15449e87c9057291a1f52f2f8cd9805df55f9fb8`.
  - Exact row: COUNTRY=BIH; ENTRY=A_NFA_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=61489941.04204912; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG=true.
- Liability file `docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv`, Git blob SHA `15f379dc42e2760eb5f2384618e48f5ddc3177f1`.
  - Exact row: COUNTRY=BIH; ENTRY=L_NIL_T; INDICATOR=P_F; UNIT=USD; FREQUENCY=Q; PERIOD=2026-Q2; OBS_VALUE=1324417089.731674; SCALE=6; PRECISION=6; DERIVATION_TYPE=O; IFS_FLAG blank.
- Preserve raw OBS_VALUE and SCALE exactly. Git blob identifiers are not SHA-256 digests. No scale conversion, sign adjustment or numeric comparison admitted.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| BIH membership in immutable 63-country Q2-2026 cohort | PASS |
| Archived IMF A_NFA_T / L_NIL_T rows present | PASS |
| Official CBBH quarterly BOP series / publication route | PASS |
| Official Q2-2026 BOP release due date (30-Sep-2026) | PASS (calendar only) |
| CBBH BOP BPM6 statement / KM million unit | PASS (series metadata / T15) |
| Separate portfolio asset/liability table structure | PASS (T15 historical/Q1 table) |
| Q2-2026 national portfolio dual-leg values | NOT_CAPTURED |
| Panorama Necto Q2-2026 workboard/export execution | NOT_EXECUTED |
| National raw bytes / receipt timestamp / SHA-256 | NOT_CAPTURED |
| Q2 observation-level revision vintage | NOT_ESTABLISHED |
| National sign / item / scale bridge to IMF rows | NOT_ESTABLISHED |
| Separate-leg numeric comparison | NOT_DONE |
| BIH full national dual-leg validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## 6. Rejected substitutes
- Q1-2026 portfolio values (-101 KMm assets; 0 KMm liabilities) are not Q2 and cannot be substituted.
- Q2-2026 IIP positions are stocks, not BOP transactions.
- IMF Article IV projections/estimates are not national raw-source observations and cannot replace the CBBH Q2 export.
- BIS cross-border banking positions are stocks and different coverage, not portfolio transaction flows.
- Do not infer one leg from portfolio net, financial-account totals or other subaccounts.

## 7. Next bounded action
- First attempt the documented anonymous CBBH Panorama Necto portal route for exact Q2-2026 BOP export. Preserve raw file bytes, retrieval time, SHA-256, table labels, unit, sign conventions and revision note.
- If the portal cannot be operated in this session, mark execution NOT_EXECUTED, retain BIH PARTIAL / NOT PASS, and advance to the next eligible fixed-cohort member. Do not retry the same inaccessible portal endpoint or treat deadline/calendar as proof of captured values.
- No aggregate admission until country-level dual-leg criteria and the cohort-wide acceptance gates pass.

## 8. Protected invariants
₹0; free official sources only. No synthetic values, fabricated timestamps, IMF re-query, cohort rebuild, inferred sign/scale, stock-as-flow, net-to-leg back-solving, annual-to-quarter allocation, aggregate admission or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
