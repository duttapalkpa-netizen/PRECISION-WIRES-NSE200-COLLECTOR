# GCR — Dominican Republic (DOM) Q2-2026 BCRD quarterly BOP source gate
Date: 2026-11-21 (Asia/Kolkata)
Status: PARTIAL / NOT PASS; exact Q2 national portfolio legs NOT_CAPTURED; aggregate NOT_AUTHORIZED.

## Progress Log / continuity preflight
- Reopened Master Priority Queue, Master Continuity Ledger and immutable 63-country Q2 dual-leg cohort. DOM is a fixed-cohort member; repository inventory had no dedicated DOM Q2-2026 national portfolio dual-leg validation report. No IMF re-query or cohort rebuild.
- BCRD official Sector Externo page confirms quarterly BOP dataset coverage 2010–2026 and exposes a direct XLSX link for quarterly BPM6 data. Attempted retrieval of the linked workbook failed through browser fetch with unsupported content type application/octet-stream; direct download also failed. Exact workbook bytes, sheets, cells and SHA-256 not captured.

## Official BCRD evidence — distinguish H1 from Q2
- BCRD Informe de la Economía Dominicana, Enero-Junio 2026, issued September 2026, pages 41–42 and Anexo 3 pages 80–81, publishes H1 cumulative portfolio flow separately: assets +305.2 USDm; liabilities +2,366.5 USDm. These are January–June cumulative values, NOT Q2-only observations.
- The same H1 table reports portfolio net balance -2,061.3 USDm, but that net balance is not a substitute for separate Q2 legs.
- BCRD later Informe preliminar Enero-Septiembre 2026 publishes 9-month cumulative portfolio values: assets +136.3 USDm; liabilities +2,473.9 USDm. These are January–September cumulative values, NOT Q2-only observations. Do not subtract H1 to infer Q3 and do not treat them as Q2.
- BCRD official Sector Externo page identifies quarterly BOP dataset 2010–2026. Exact official XLSX: https://cdn.bancentral.gov.do/documents/estadisticas/sector-externo/documents/bpagos_trim_6.xlsx. The linked workbook fetch failed with 400 Unsupported content-type: application/octet-stream; direct container download failed. Therefore the Q2 rows are not inspectable in this task.
- BCRD's H1 table states that negative values reflect Dominican Republic net borrowing from the rest of the world and positive values net lending; this is account-level sign note. No sign conversion applied to any data.

## Archived IMF raw panel — reused exact rows only
- Asset panel blob SHA: 15449e87c9057291a1f52f2f8cd9805df55f9fb8
- Liability panel blob SHA: 15f379dc42e2760eb5f2384618e48f5ddc3177f1
- DOM Q2-2026 A_NFA_T raw OBS_VALUE=340200000; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- DOM Q2-2026 L_NIL_T raw OBS_VALUE=-184000000; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- Raw values/attributes retained. No conversion, sign transform, netting, H1-to-Q2 inference or IMF re-query.

## Acceptance matrix
| Gate | Status |
|---|---|
| Fixed cohort membership / archived IMF Q2 both-leg availability | PASS (roster only) |
| Official BCRD quarterly BOP dataset route | PASS |
| Official Q2 national portfolio asset leg | NOT_CAPTURED (XLSX inaccessible) |
| Official Q2 national portfolio liability leg | NOT_CAPTURED (XLSX inaccessible) |
| H1 2026 separate portfolio legs | CAPTURED, but wrong period for Q2 |
| 9M 2026 separate portfolio legs | CAPTURED, but wrong period for Q2 |
| National Q2 sign/scale/vintage bridge | NOT_ESTABLISHED |
| Separate-leg numeric comparison | NOT_DONE |
| DOM full national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## Next exact actions
1. Recover exact BCRD quarterly workbook using a supported spreadsheet/browser route or owner-side save of the exact XLSX URL; preserve original bytes, retrieval UTC, response metadata and SHA-256.
2. Inspect the workbook for Q2-2026 portfolio investment assets and liabilities separately; confirm quarter-only columns and national sign convention.
3. Compare each national Q2 leg against the archived IMF raw row and establish same-vintage/revision bridge. Do not use H1 or 9M cumulative rows as Q2.
4. If workbook remains inaccessible, retain DOM PARTIAL and advance to next eligible cohort member. Do not repeat the same unsupported XLSX fetch.

## Protected invariants
₹0; official/free sources only; no synthetic data; no H1/9M as Q2; no net-balance substitution; no IIP stock as BOP flow; no residual/back-solving; no unapproved sign/scale conversion; no IMF re-query; no cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Source references
- BCRD official Sector Externo page: https://www.bancentral.gov.do/a/CustomView/2532-sector-externo
- BCRD Q2 2026 H1 report (Sept 2026): https://cdn.bancentral.gov.do/documents/publicaciones-economicas/informe-de-la-economia-dominicana/documents/infeco_definitivo2026-06.pdf
- BCRD Jan-Sep 2026 preliminary report: https://cdn.bancentral.gov.do/documents/publicaciones-economicas/resultados-preliminares-de-la-economia-dominicana/documents/infeco_preliminar2026-09.pdf
- Exact BCRD quarterly BPM6 XLSX: https://cdn.bancentral.gov.do/documents/estadisticas/sector-externo/documents/bpagos_trim_6.xlsx