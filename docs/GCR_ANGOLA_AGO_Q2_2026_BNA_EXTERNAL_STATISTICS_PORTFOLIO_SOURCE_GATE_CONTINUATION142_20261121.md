# GCR — Angola (AGO) Q2-2026 BNA external statistics / portfolio source gate
Date: 2026-11-21 (Asia/Kolkata)
Status: PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.

## Progress log and selection
- Reopened Master Continuity Ledger, Master Priority Queue and immutable 63-country cohort before selecting the next country after ALB. AGO is explicitly in the fixed cohort; repository inventory had no dedicated AGO Q2-2026 national portfolio dual-leg validation report. No IMF re-query and no cohort rebuild.
- Chosen as a high-priority oil-exporting EMDE market with a BNA Q2 external-statistics release publicly referenced in September 2026. The source gate is not a full numeric validation.

## National source evidence
- BNA official site exposes Statistics > External Statistics, annual data and a “Balance of Payments and International Investment Position Report” publication family. The current browser-readable official portal route is a JavaScript application with no extractable page text or downloadable report bytes in this retrieval channel.
- BNA Q2-2026 External Statistics Information Note was publicly announced 4-Sep-2026. Contemporary reports quoting the BNA note report Q2 current-account surplus about USD2.07–2.08bn and capital-and-financial-account deficit USD2,516.6m; these are account-level aggregates, not portfolio asset/liability legs. They also state that the deficit was driven mainly by medium/long-term capital (public external debt), positive FDI balance and other capital (trade credits/advances and deposits). These secondary reports establish existence and broad context of the BNA release, not the exact national portfolio series values.
- An Angola banking-sector economic report reproduces BNA external-indicator tables and provides Q2-2026 context, but it does not provide Q2 portfolio investment asset and liability legs separately. It is not substituted for the primary BNA workbook.
- IMF GDDS metadata for Angola says BNA's external-sector statistics dissemination includes annual BOP/IIP statistics and that quarterly bulletin distribution has historically been by mailing list; its metadata also records plans to improve quarterly BOP/IIP dissemination. This is a plausible access boundary, not proof that the Q2 note lacks detailed rows.

## Existing archived IMF rows — reused only
Raw panel blobs unchanged:
- Asset panel blob SHA: 15449e87c9057291a1f52f2f8cd9805df55f9fb8
- Liability panel blob SHA: 15f379dc42e2760eb5f2384618e48f5ddc3177f1
- AGO Q2-2026 A_NFA_T: OBS_VALUE=23014088.470948; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- AGO Q2-2026 L_NIL_T: OBS_VALUE=1500000000; UNIT=USD; SCALE=6; FREQ=Q; DERIVATION_TYPE=O.
- Values and attributes preserved exactly as archived. No normalization, sign conversion, FX conversion, netting or IMF re-query performed.

## Acceptance matrix
| Gate | Status |
|---|---|
| Fixed-cohort membership / Q2 both-leg IMF panel availability | PASS (roster only) |
| BNA Q2-2026 external-statistics release existence | PASS (release announcement / contemporaneous reporting) |
| Official BNA publication family identified | PASS |
| Exact BNA Q2 portfolio asset and liability values | NOT_CAPTURED |
| Official national raw workbook / bytes / SHA-256 | NOT_CAPTURED |
| National portfolio taxonomy and sign convention | NOT_ESTABLISHED |
| Exact FX/scale bridge to IMF USD rows | NOT_ESTABLISHED |
| Same-vintage/revision bridge | NOT_ESTABLISHED |
| Separate-leg numerical reconciliation | NOT_DONE |
| AGO full validation | PARTIAL / NOT PASS |
| Aggregate admission | NOT_AUTHORIZED |

## Next exact actions
1. Seek the Q2-2026 BNA External Statistics Information Note attachment or the detailed BOP/IIP report through a supported official download route or the BNA quarterly-bulletin distribution channel; preserve original bytes, response metadata, retrieval UTC and SHA-256.
2. Extract portfolio investment assets and liabilities separately, including equity/debt children where published; verify national sign convention and avoid using the capital-and-financial-account net deficit as a proxy.
3. Establish currency and scale using BNA's Q2 methodology/source notes before comparing with the archived IMF USD rows; verify same-vintage/revision status.
4. If official attachment is not accessible, retain AGO PARTIAL and advance to the next eligible member. Do not repeatedly retry the JavaScript portal page or infer portfolio legs from net aggregates.

## Protected invariants
₹0; free official sources only; no synthetic values/timestamps; no account-net to dual-leg back-solving; no IIP stock as BOP flow; no unapproved sign/FX/scale transforms; no IMF re-query; no cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.

## Source references
- BNA official portal / External Statistics and BOP-IIP publication family: https://www.bna.ao/#/pt/estatisticas/estatisticas-externas/dados-anuais
- BNA Q2 external statistics note announcement reported 4-Sep-2026: https://abanc.ao/?p=1944
- Q2 current-account and capital/financial-account summary citing BNA: https://abanc.ao/?p=1950
- BFA Q4-2026 economic report (secondary reproduction of BNA external indicators): https://www.bfa.ao/media/9125/economic-report-q4-2026.pdf
- IMF GDDS Angola metadata: https://dsbb.imf.org/e-gdds/dqaf-base/country/AGO/category/AAC00
