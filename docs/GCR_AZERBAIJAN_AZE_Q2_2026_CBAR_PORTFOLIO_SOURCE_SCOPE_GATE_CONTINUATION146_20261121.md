# GCR — Azerbaijan (AZE) Q2-2026 CBAR portfolio source scope gate
Date: 2026-11-21 (Asia/Kolkata)
Status: PARTIAL / NOT PASS; Q2 national portfolio-only dual legs NOT_CAPTURED; aggregate NOT_AUTHORIZED.

## Progress Log / continuity preflight
- Reopened Master Priority Queue, Master Continuity Ledger and immutable 63-country Q2 dual-leg cohort. AZE is an eligible fixed-cohort member; repository inventory/search showed no dedicated AZE Q2-2026 national portfolio-only dual-leg validation report. No IMF re-query or cohort rebuild.
- Selected Azerbaijan as a material oil-exporting EMDE; official Central Bank of Azerbaijan (CBAR) September 2026 Statistical Bulletin contains Q2-2026 BOP table 1.4.

## Official source scope finding
- CBAR Statistical Bulletin 09/2026, table 1.4, USD million, QII 2026 column: https://uploads.cbar.az/assets/34f2e92e50d556d098dd5b36f.pdf
- The table provides separate top-level financial-account net acquisition of financial assets and net incurrence of liabilities, but the breakdown under both is grouped as 'portfolio and other investments'. It does not expose portfolio investment as a separate Q2-2026 category. The combined values cannot be used as portfolio-only values.
- The same bulletin's quarterly series table is a Q2 observation; it must not be conflated with H1 (six-month) briefing figures.
- CBAR's 15-Sep-2026 briefing, reported by APA, gives H1 2026 net foreign financial asset/liability portfolio component estimates (assets -USD0.3bn, liabilities -USD2.0bn). These are six-month cumulative figures, not Q2-only flows; they cannot be substituted for Q2 or differenced without the corresponding Q1 same-vintage portfolio-only legs.
- Official bulletin table 1.4 Q2 2026 current account USD3,074m and financial-account top-level data are contextual only; not portfolio-only evidence. Do not infer portfolio legs from account residuals.

## Archived IMF exact rows — reused only
- Asset panel blob SHA: 15449e87c9057291a1f52f2f8cd9805df55f9fb8
- Liability panel blob SHA: 15f379dc42e2760eb5f2384618e48f5ddc3177f1
- AZE Q2-2026 A_NFA_T: OBS_VALUE=-333337000; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- AZE Q2-2026 L_NIL_T: OBS_VALUE=-8044000.0000001; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- Raw rows retained as-is. No conversion, sign inversion, netting, residual inference or IMF re-query.

## Acceptance matrix
| Gate | Status |
|---|---|
| Fixed cohort membership / archived IMF Q2 both-leg availability | PASS (roster only) |
| Official CBAR Q2-2026 BOP table identified | PASS |
| National Q2 portfolio-only asset leg | NOT_CAPTURED |
| National Q2 portfolio-only liability leg | NOT_CAPTURED |
| Portfolio and other combined Q2 rows | CAPTURED but NOT PORTFOLIO-ONLY |
| H1 portfolio components | CAPTURED by reported briefing, but wrong period for Q2 |
| National sign/scale/vintage bridge for Q2 portfolio-only series | NOT_ESTABLISHED |
| Separate-leg numerical comparison | NOT_DONE |
| AZE full national validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## Next exact actions
1. Obtain CBAR's underlying detailed Q2-2026 BOP dataset / Excel or table annex with portfolio investment separated from other investment for both assets and liabilities.
2. Preserve original file bytes, URL, publication/retrieval timestamp and SHA-256; inspect Q1 and Q2 rows only if the source explicitly provides period-specific standalone flows and a matching vintage.
3. Compare the two Q2 portfolio legs separately against archived IMF exact rows; establish national sign, scale, definition and same-vintage before any PASS.
4. If CBAR does not publish a Q2 portfolio-only split, retain PARTIAL and advance to next uncovered cohort member. Do not derive it from H1 minus Q1 unless both exact standalone portfolio legs and same-vintage evidence are available.

## Protected invariants
₹0; official/free sources only; no synthetic data; no combined portfolio+other as portfolio-only; no H1 as Q2; no IIP stock as BOP flow; no residual/back-solving; no unapproved sign/scale conversion; no IMF re-query; no cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Source references
- CBAR Statistical Bulletin 09/2026, Table 1.4: https://uploads.cbar.az/assets/34f2e92e50d556d098dd5b36f.pdf
- CBAR H1 2026 portfolio briefing coverage: https://en.apa.az/finance/azerbaijans-net-foreign-financial-assets-and-liabilities-increase-524364
- CBAR official portal: https://www.cbar.az/