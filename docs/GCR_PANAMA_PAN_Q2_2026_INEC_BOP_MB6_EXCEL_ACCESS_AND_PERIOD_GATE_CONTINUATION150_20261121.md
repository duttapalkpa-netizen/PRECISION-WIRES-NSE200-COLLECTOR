# GCR — Panama (PAN) Q2-2026 INEC BOP MBP6 Excel access and period gate
Date: 2026-11-21 (Asia/Kolkata)
Status: PARTIAL / NOT PASS; Q2 national portfolio-only legs NOT_CAPTURED; aggregate NOT_AUTHORIZED.

## Progress Log / continuity preflight
- Reopened Master Priority Queue, Master Continuity Ledger and immutable 63-country Q2 dual-leg cohort. PAN is a fixed-cohort member; no dedicated PAN Q2-2026 national portfolio dual-leg report found in repository inventory. No IMF re-query or cohort rebuild.
- Official INEC publication page lists BOP release 'Años 2024-25 y primer semestre 2026', dated 25-Sep-2026, and MBP6 Table 1 Excel workbook. This is H1 cumulative, not Q2-only.

## Official source and retrieval result
- INEC publication page: https://www.inec.gob.pa/Publicaciones/Default3.aspx?ID_CATEGORIA=4&ID_PUBLICACION=1428&ID_SUBCATEGORIA=24
- Page explicitly states data cover January–June 2026 and uses IMF BPM6 tables from 2015 onward; the BOP combines public and private sector transactions.
- Exact MBP6 normalized BOP Table 1 Excel URL exposed by page: https://www.inec.gob.pa/archivos/P0774740120260925095521Cuadro%201.%20Componentes%20Normalizados%20-%20MBP6.xlsx
- Attempted direct retrieval via the official page link failed: 400 Unsupported content-type application/vnd.openxmlformats-officedocument.spreadsheetml.sheet. Workbook bytes/sheets/cells and SHA-256 were not captured.
- Official page lists prior quarterly BOP publication 'Años 2023-25, por trimestre' dated 27-Mar-2026 and first-quarter 2026 release dated 26-Jun-2026. It does not show a Q2-only 2026 publication in the current publication index; latest 2026 release is explicitly first semester. Therefore Q2 national-only source route not established from current index.
- Do not use H1 figures as Q2, subtract Q1 unless exact same-vintage Q1 and H1 portfolio-only legs are available, or use IIP positions as flow.

## Archived IMF raw panel — reused exact rows only
- Asset panel blob SHA: 15449e87c9057291a1f52f2f8cd9805df55f9fb8
- Liability panel blob SHA: 15f379dc42e2760eb5f2384618e48f5ddc3177f1
- PAN Q2-2026 A_NFA_T raw row: dataflow,IMF.STA:BOP(21.0.0),R,PAN,A_NFA_T,P_F,USD,Q,2026-Q2,3328699298.09,6,6,,,,,,,,,,,,O,,,,true,,
- PAN Q2-2026 L_NIL_T raw row: dataflow,IMF.STA:BOP(21.0.0),R,PAN,L_NIL_T,P_F,USD,Q,2026-Q2,450738775.03,6,6,,,,,,,,,,,,O,,,,,,
- Raw values and attributes retained exactly. No scale/sign conversion, netting, H1-to-Q2 derivation, or IMF re-query.

## Acceptance matrix
| Gate | Status |
|---|---|
| Fixed cohort membership / archived IMF Q2 both legs | PASS (roster only) |
| Official INEC MBP6 BOP H1 2026 publication | PASS |
| Official Q2-only 2026 BOP publication located | NOT_CAPTURED / NOT_ESTABLISHED |
| Exact official Excel bytes / SHA-256 | NOT_CAPTURED (unsupported XLSX MIME) |
| National Q2 portfolio asset leg | NOT_CAPTURED |
| National Q2 portfolio liability leg | NOT_CAPTURED |
| H1 portfolio-only data as substitute for Q2 | PROHIBITED |
| National Q2 sign/scale/vintage bridge | NOT_ESTABLISHED |
| Numeric comparison | NOT_DONE |
| PAN full validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## Next exact actions
1. Wait for or locate an official INEC Q2-only 2026 BPM6 BOP release or underlying quarterly dataset; verify release period and row granularity.
2. Recover official MBP6 Excel through a supported spreadsheet/browser route or owner-side save; preserve original bytes, retrieval timestamp, URL and SHA-256.
3. Extract Q2 portfolio assets and liabilities separately; verify whether H1 and Q1 releases are same vintage before considering any subtraction.
4. If no Q2-only release exists, retain PAN PARTIAL and advance to next eligible cohort member; do not fabricate quarterly legs.

## Protected invariants
₹0; official/free sources only; no synthetic data; no H1 as Q2; no Q1/H1 differencing without same-vintage proof; no IIP stock as BOP flow; no netting/back-solving; no unapproved sign/scale conversion; no IMF re-query; no cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Source references
- INEC BOP H1 2026 publication: https://www.inec.gob.pa/Publicaciones/Default3.aspx?ID_CATEGORIA=4&ID_PUBLICACION=1428&ID_SUBCATEGORIA=24
- Exact official MBP6 Table 1 XLSX: https://www.inec.gob.pa/archivos/P0774740120260925095521Cuadro%201.%20Componentes%20Normalizados%20-%20MBP6.xlsx
- INEC BOP publication index: https://www.inec.gob.pa/publicaciones/Default2.aspx?ID_CATEGORIA=4&ID_SUBCATEGORIA=24