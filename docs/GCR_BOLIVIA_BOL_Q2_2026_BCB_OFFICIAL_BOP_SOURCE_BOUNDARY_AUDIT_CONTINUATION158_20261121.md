# GCR Bolivia (BOL) Q2-2026 BCB official BOP source-boundary audit — Continuation 158
Date: 2026-11-21

## Preflight and selection
- Re-fetched the current Master Continuity Ledger (blob SHA b0fdab2c12a2a1259b483777f844cb888ffc11b6), GCR Priority Queue (blob SHA c8ceebb5d45598c262953a9024503b567e1398ce) and the immutable 63-country Q2-2026 both-legs cohort (blob SHA 31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8).
- BOL is a fixed-cohort member; archived IMF asset and liability Q2 rows both exist. Repository search found no prior dedicated BOL Q2-2026 national dual-leg audit. No IMF re-query and no cohort rebuild.
- The immediately preceding BLZ (Continuation 157) remains PARTIAL because its official workbook byte fetch failed. This task selected BOL because BCB has an explicitly Q2-2026 page and two direct Q2 XLSX links, a materially more specific source route than a generic annual/H1 report.

## Official national source findings
- Banco Central de Bolivia (BCB), official “Avance de Cifras del Reporte de Balanza de Pagos (VI MANUAL)” page:
  https://www.bcb.gob.bo/?q=pub_avance-cifras-rbpiv
  It explicitly labels “RESUMEN DE CIFRAS DE BALANZA DE PAGOS SEGUNDO TRIMESTRE - GESTIÓN 2026” and lists separate links for “Balanza de Pagos” and “Series de tiempo: Balanza de Pagos”.
- Direct BOP workbook: https://www.bcb.gob.bo/webdocs/publicacionesbcb/1.%20BOP_T2%202026.xlsx
  Web retrieval returned HTTP 400 unsupported XLSX MIME. A separate direct byte-download attempt also failed. No workbook bytes, sheets, Q2 row values, retrieval receipt or SHA-256 captured.
- Direct time-series workbook: https://www.bcb.gob.bo/webdocs/publicacionesbcb/4.%20Serie_BOP_T2%202026.xlsx
  Web retrieval returned HTTP 400 unsupported XLSX MIME. No bytes, series IDs, Q2 values, receipt or SHA-256 captured.
- BCB's general publication page currently lists the full “Reporte ... PRIMER SEMESTRE 2026” dated 30-Sep-2026, not a separate full Q2 narrative report. That H1 publication is contextual only and cannot replace the explicit Q2 workbook.
- BCB's official VI Manual page identifies the Q2 publication under “VI MANUAL”; a separate Q2-specific detailed methodology/sign convention and revision-vintage bridge was not captured. A 2025 report confirms BCB uses BPM6, but that is not accepted as Q2-2026 vintage proof.
- Official Q2-2026 Q2 locator is PASS; actual dual-leg national values and raw bytes remain NOT_CAPTURED. No national-vs-IMF numerical comparison is admitted.

## Archived IMF panel rows (reused, not re-queried)
- BOL A_NFA_T, P_F, USD, Q, 2026-Q2: OBS_VALUE=-154107393.924487; SCALE=6.
- BOL L_NIL_T, P_F, USD, Q, 2026-Q2: OBS_VALUE=974071938.904098; SCALE=6.
- Existing raw panel Git blob SHAs unchanged: asset 15449e87c9057291a1f52f2f8cd9805df55f9fb8; liability 15f379dc42e2760eb5f2384618e48f5ddc3177f1. These are Git blob SHAs, not national raw-file SHA-256.
- Preserve exact OBS_VALUE and SCALE separately; no scale conversion, sign transformation, netting or inferred leg mapping.

## Acceptance decision
| Gate | Status |
|---|---|
| Immutable cohort membership and both IMF rows present | PASS |
| Official BCB Q2-2026 BOP workbook locator | PASS |
| Official Q2-2026 time-series workbook locator | PASS |
| National XLSX bytes/sheets/dual-leg layout and exact values | NOT_CAPTURED |
| National Q2-specific item mapping, BPM equivalence, sign/unit/scale | NOT_ESTABLISHED |
| National revision/publication vintage and receipt timestamp | NOT_CAPTURED |
| Numerical comparison | NOT_DONE |
| BOL country validation | PARTIAL / NOT PASS |
| 63-country aggregate authorization | NOT_AUTHORIZED |

## Next bounded action
Use a genuinely supported official BCB raw-byte/export route for the two already identified Q2 XLSX files (not the same web MIME retry); preserve both original files, retrieval timestamp and SHA-256; inspect exact Q2 asset and liability series/rows, units, sign convention and vintage. If no supported route is available, retain BOL PARTIAL and advance to the next unreviewed fixed-cohort member. Do not substitute H1/annual data, IIP stocks, net flow or unrelated BOP categories.

₹0 spent. No synthetic data. No production selector/scoring/CORE-672/engine changes. UNKNOWN never PASS.
