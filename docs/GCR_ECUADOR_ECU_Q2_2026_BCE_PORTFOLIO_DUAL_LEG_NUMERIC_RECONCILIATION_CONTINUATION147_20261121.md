# GCR — Ecuador (ECU) Q2-2026 BCE portfolio dual-leg numeric reconciliation
Date: 2026-11-21 (Asia/Kolkata)
Status: NATIONAL DUAL-LEG NUMERIC COMPARISON PASS (0.1 USDm publication precision); SAME-VINTAGE NOT_ESTABLISHED; full country acceptance PARTIAL.

## Progress Log / continuity preflight
- Reopened Master Priority Queue, Master Continuity Ledger and immutable 63-country Q2 dual-leg cohort. ECU is an eligible fixed-cohort member. Repository search did not find a dedicated ECU Q2-2026 national portfolio dual-leg reconciliation report. No IMF re-query or cohort rebuild.
- Selected ECU because the Central Bank of Ecuador (BCE) SDDS/NEDD official external-sector table publishes Q2/26 portfolio investment asset and liability transaction legs separately, in USD millions.

## Official national source and observations
- BCE SDDS/NEDD English page: https://contenido.bce.fin.ec/home1/estadisticas/dsbb/docs/hyperlink/HyperlinkENG.htm
- Page last updated 10-Nov-2026; states data correspond to IMF DSBB dissemination standards and, unless otherwise indicated, are final.
- External Sector / Balance of Payments Q2/26, unit USD millions:
  * Net acquisition of financial assets — Portfolio investment: -595.2
  * Net incurrence of liabilities — Portfolio investment: +1,000.3
- BCE press release dated 1-Oct-2026 independently states portfolio investment decreased by USD595.2m in Q2 and liabilities incurred were USD1,519.3m in total. This corroborates the asset leg and overall liability context; the NEDD table provides the exact portfolio liability subcomponent +1,000.3m.
- BCE page footnote says BOP/IIP data prepared and disseminated under IMF BPM6. Preserve source's own row labels and signs; no sign inversion.
- The same page separately presents Q2 IIP end-period positions/stocks. Those are not used in this flow comparison.

## Archived IMF raw panel — reused exact rows only
- Asset panel blob SHA: 15449e87c9057291a1f52f2f8cd9805df55f9fb8
- Liability panel blob SHA: 15f379dc42e2760eb5f2384618e48f5ddc3177f1
- ECU Q2-2026 A_NFA_T raw OBS_VALUE=-595164167.96001; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- ECU Q2-2026 L_NIL_T raw OBS_VALUE=1000348809; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- For comparison only, declared SCALE=6 converts raw USD values to USDm: assets -595.16416796001; liabilities +1,000.348809. No sign conversion or netting.

## Numeric reconciliation — rounded to national 0.1 USDm precision
| Leg | BCE Q2/26 (USDm) | Archived IMF raw / 1e6 (USDm) | Difference (BCE−IMF) | Result |
|---|---:|---:|---:|---|
| Portfolio asset net acquisition | -595.2 | -595.16416796001 | -0.03583203999 | PASS — same 0.1 rounding |
| Portfolio liability net incurrence | +1,000.3 | +1,000.348809 | -0.048809 | PASS — same 0.1 rounding |
- Each national leg independently rounds to the same 0.1 USDm as its archived IMF counterpart. This is numeric agreement at publication precision, not proof of identical data vintage.

## Vintage / raw evidence boundary
- BCE NEDD page last updated 10-Nov-2026; BCE press release carrying the Q2 result is dated 1-Oct-2026. Archived IMF panel snapshot is dated 19-Nov-2026.
- No exact BCE revision ledger / release payload timestamp for the two portfolio rows, nor IMF extraction-vintage metadata proving synchronized vintage, was captured. Same-vintage remains NOT_ESTABLISHED; do not infer from date proximity or rounded equality.
- The national table was read from the live official NEDD HTML page. A preserved raw national HTML/PDF file with SHA-256 and retrieval timestamp has not yet been committed to the evidence archive; national raw-file SHA256 NOT_CAPTURED.
- National currency/unit and BPM6 scope are explicit (USD million, Q2/26, BPM6). National row labels provide separate assets and liabilities; no inferred category or stock/flow substitution.

## Acceptance matrix
| Gate | Status |
|---|---|
| Fixed cohort membership / archived IMF Q2 both legs | PASS (roster only) |
| Official BCE Q2/26 BOP source | PASS |
| Separate portfolio asset / liability values | PASS |
| National unit, period and BPM6 scope | PASS |
| Archived IMF exact rows and blob provenance | PASS |
| Asset numeric comparison at 0.1 USDm | PASS |
| Liability numeric comparison at 0.1 USDm | PASS |
| Sign alignment (source-native row signs) | PASS at numeric match; no transform |
| National raw HTML/PDF SHA-256 archive | NOT_CAPTURED |
| Exact same-vintage bridge | NOT_ESTABLISHED |
| ECU dual-leg numeric gate | PASS at published precision; vintage-qualified PARTIAL |
| Aggregate admission | NOT_AUTHORIZED |

## Next exact actions
1. Preserve the exact BCE NEDD page / official Q2 bulletin file and response metadata with retrieval timestamp and SHA-256 in the evidence archive.
2. Obtain exact BCE Q2 release vintage/revision metadata and IMF series extraction-vintage evidence; keep same-vintage gate NOT_ESTABLISHED until matched.
3. Retain both separate-leg numeric PASS results; do not repeat extraction or promote aggregate eligibility.
4. Advance to next uncovered fixed-cohort member after this evidence package is recorded.

## Protected invariants
₹0; official/free sources only; no synthetic data; no IIP stock as BOP flow; no netting/back-solving; no sign inversion; no unapproved scale conversion; no IMF re-query; no cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Source references
- BCE official NEDD/SDDS: https://contenido.bce.fin.ec/home1/estadisticas/dsbb/docs/hyperlink/HyperlinkENG.htm
- BCE Q2-2026 press release (1-Oct-2026): https://www.bce.fin.ec/en/ecuador-recorded-a-current-account-surplus-of-usd-1425-million-in-the-second-quarter-of-2026/
- Q2 BOP detailed bulletin index: https://contenido.bce.fin.ec/documentos/Estadisticas/SectorExterno/BalanzaPagos/boletin96/indice.htm