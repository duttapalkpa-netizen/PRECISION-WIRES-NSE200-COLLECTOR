# GCR — Costa Rica (CRI) Q2-2026 SECMCA/BCCR portfolio dual-leg numeric reconciliation
Date: 2026-11-21 (Asia/Kolkata)
Status: NUMERIC DUAL-LEG COMPARISON PASS at 0.1 USDm display precision; primary-source raw-file capture and same-vintage bridge NOT_ESTABLISHED; full country acceptance PARTIAL.

## Progress Log / continuity preflight
- Reopened Master Priority Queue, Master Continuity Ledger and immutable 63-country Q2 dual-leg cohort. CRI is a cohort member; repository search showed no dedicated CRI Q2-2026 portfolio dual-leg reconciliation report. No IMF re-query or cohort rebuild.
- Selected CRI after official SECMCA ESEA quarterly analytical BOP table was found with separate Q2/2026 portfolio assets and liabilities. It gives an unusually clean independent dual-leg comparison opportunity.

## Official regional statistical source — Q2-2026
- SECMCA ESEA, Balanza de pagos — Presentación Analítica, Costa Rica, USD millions; page labels columns Trimestre I - 2026 and Trimestre II - 2026. Q2 values are the second-quarter column, not cumulative H1.
- Source URL: https://www.secmca.org/esea-chart//?chartid=467&cid=0&epID=0&parent=Balanza+de+pagos&scid=0&son=Presentaci%C3%B3n+Anal%C3%ADtica&subject=BALANZA_DE_PAGOS
- Q2-2026 portfolio investment assets: +1,275.5 USDm.
- Q2-2026 portfolio investment liabilities: +1,167.5 USDm.
- Table further disaggregates assets into equity/investment fund shares 998.7 and debt securities 276.7; liabilities into equity/investment fund shares 16.0 and debt securities 1,151.5. These sum to the respective displayed portfolio totals.
- SECMCA page describes BOP as transactions between residents and non-residents over a period and states USD million units. This is a flow table, not IIP stock. BCCR NEDD page independently shows Q2/26 and states the NEDD data follow IMF DSBB standards and are final unless otherwise indicated; however its visible summary only exposes aggregate financial account, not portfolio-only flow rows.
- Evidence boundary: the detailed Q2 portfolio legs are directly visible in the official regional SECMCA statistical portal. The linked export controls are rendered as client-side actions and the page does not expose the raw downloadable payload/underlying BCCR series ID in the retrieved text. Do not claim a captured BCCR primary workbook or national raw-file SHA-256.

## Archived IMF raw panel — reused exact rows only
- Asset panel blob SHA: 15449e87c9057291a1f52f2f8cd9805df55f9fb8
- Liability panel blob SHA: 15f379dc42e2760eb5f2384618e48f5ddc3177f1
- CRI Q2-2026 A_NFA_T raw OBS_VALUE=1275459662.03478; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- CRI Q2-2026 L_NIL_T raw OBS_VALUE=1167506330.15469; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- Declared SCALE=6 display conversion only: assets +1,275.45966203478 USDm; liabilities +1,167.50633015469 USDm. No sign inversion, netting or residual calculation.

## Numeric reconciliation — rounded to published 0.1 USDm
| Leg | SECMCA Q2-2026 (USDm) | Archived IMF raw / 1e6 (USDm) | Difference (SECMCA−IMF) | Result |
|---|---:|---:|---:|---|
| Portfolio asset net acquisition | +1,275.5 | +1,275.45966203478 | +0.04033796522 | PASS — same 0.1 rounding |
| Portfolio liability net incurrence | +1,167.5 | +1,167.50633015469 | -0.00633015469 | PASS — same 0.1 rounding |
- Both independent legs match at the regional portal's displayed precision. This establishes numerical agreement only, not identical national-source vintage or primary-source raw-file provenance.

## Vintage / provenance boundary
- BCCR NEDD page says it is updated daily, reflects IMF DSBB dissemination standards and data are final unless otherwise indicated. Its Q2/26 summary shows financial-account total -USD2,474.6m but does not separately display portfolio flows; it separately shows Q2 IIP portfolio positions (stocks), which are excluded.
- SECMCA ESEA Q2 table was retrieved 21-Nov-2026; archived IMF raw panel archive date is 19-Nov-2026. The regional portal page does not expose a row-specific release timestamp/revision vintage or the underlying BCCR primary series IDs in the visible retrieved output. Same-vintage NOT_ESTABLISHED.
- National BCCR original export/raw bytes, source URL for a direct primary data file, retrieval timestamp and SHA-256 NOT_CAPTURED. SECMCA table source attribution / primary-series mapping needs exact metadata or export capture.

## Acceptance matrix
| Gate | Status |
|---|---|
| Fixed cohort membership / archived IMF Q2 both legs | PASS (roster only) |
| SECMCA Q2/2026 analytical BOP table | PASS |
| Separate portfolio asset and liability legs | PASS |
| Period (quarter II, not H1) and unit USDm | PASS |
| Flow vs IIP stock distinction | PASS |
| Archived IMF exact rows / blob provenance | PASS |
| Asset numeric comparison at 0.1 USDm | PASS |
| Liability numeric comparison at 0.1 USDm | PASS |
| Direct BCCR raw source / export SHA-256 | NOT_CAPTURED |
| Exact same-vintage bridge | NOT_ESTABLISHED |
| CRI numeric dual-leg gate | PASS at portal precision; provenance/vintage qualified PARTIAL |
| Aggregate admission | NOT_AUTHORIZED |

## Next exact actions
1. Use SECMCA ESEA export (CSV/XLS/JSON) through supported direct download and preserve original bytes, retrieval timestamp, URL and SHA-256; inspect its source metadata and BCCR series IDs.
2. Obtain corresponding BCCR primary Q2-2026 portfolio asset/liability flow rows and revision/vintage metadata; verify exact source-native signs and mapping.
3. Keep numeric match PASS at 0.1 USDm; do not promote same-vintage or aggregate status until provenance is captured.
4. Advance to the next uncovered fixed-cohort member without repeating this numeric extraction.

## Protected invariants
₹0; official/free sources only; no synthetic data; no IIP stock as BOP flow; no H1 as Q2; no netting/back-solving; no unapproved sign/scale conversion; no IMF re-query; no cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Source references
- SECMCA ESEA Costa Rica analytical BOP Q1/Q2-2026: https://www.secmca.org/esea-chart//?chartid=467&cid=0&epID=0&parent=Balanza+de+pagos&scid=0&son=Presentaci%C3%B3n+Anal%C3%ADtica&subject=BALANZA_DE_PAGOS
- BCCR NEDD/SDDS Costa Rica: https://gee.bccr.fi.cr/indicadoreseconomicos/Documentos/NEDD/PAG_NAC_ING.htm