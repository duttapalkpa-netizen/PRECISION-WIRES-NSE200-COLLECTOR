# GCR Q2-2026 — Chile (CHL) BCCh BDE monthly dual-leg and vintage audit
Date: 2026-11-21
Chapter: গবেষণা যাচাই অব্যাহত 47
Part: 8
Continuation sequence: 160
Status: OFFICIAL Q2 RELEASE + MONTHLY DUAL-LEG BDE OBSERVATIONS CAPTURED; PROVISIONAL MONTHLY-SUM COMPARISON PLAUSIBLE; RAW-BYTE SHA-256 / SAME-VINTAGE RECONCILIATION PENDING; CHL PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity and selection
- Re-fetched current Master Continuity Ledger, GCR Priority Queue and immutable 63-country Q2-2026 both-leg cohort. CHL is a fixed-cohort member with both archived IMF rows present.
- Search found no prior dedicated CHL Q2 national dual-leg audit. Existing Chile reports cover source/vintage access and revision context; those were not repeated. Brazil is skipped: its BCB monthly portfolio series capture and PA/Dataflow identity issue are already documented, and the priority queue explicitly says not to repeat exhausted public endpoint probes.
- BLR Part-7 continuation was followed up through the exact official NBRB publication route: https://www.nbrb.by/publications/balpay lists only “January–June 2026” as the latest current-year bulletin. The exact official PDF https://www.nbrb.by/publications/balpay/balpay2026_2.pdf timed out in web retrieval and failed direct byte download. It is H1, not an isolated Q2 transaction table. No Q2 national dual-leg values or raw bytes were obtained. BLR remains PARTIAL; no unsupported URL guesses or H1-to-Q2 inference.
- No IMF re-query, cohort rebuild, paid source or production-code modification.

## 2. Official Chile Q2 release — flow versus stock boundary
- Banco Central de Chile official Q2-2026 BOP publication: https://www.bcentral.cl/documents/33528/8574503/Balanza%2Bde%2BPagos%2BSegundo%2BTrimestre%2B2026.pdf/7509dfd7-2fd8-66ef-b29b-948a77cdc9fb?t=1793642226985
- The report is explicitly “Resultados al segundo trimestre de 2026”. Table 1 reports Q2 portfolio investment net = USD 299m, but not both legs in that summary row. Narrative says liabilities increased USD 5,398m; this is not used to back-solve the missing asset leg.
- Table 2 reports portfolio-investment net transaction contribution of -USD 299m to net IIP position change; this is not itself a pair of gross asset/liability legs. IIP positions are stocks and excluded as flow substitutes.
- The same official publication's revision table explicitly shows Q1 2026 revised from prior vintage and a Q2 current value, so revision vintage matters.

## 3. Official BDE monthly flow series — independent dual legs
Official BCCh BDE “Canasta” source:
https://si3.bcentral.cl/siete/ES/Siete/Canasta?idCanasta=T7KXJ2131
The indexed official table exposes both portfolio-investment transaction legs in USD million, monthly, with Jan–Aug 2026 observations:
- Portfolio investment assets, total financial account: Jan 1,999.12; Feb 3,273.94; Mar 1,359.52; Apr 1,643.45; May 932.56; Jun 2,522.90.
- Portfolio investment liabilities, total financial account: Jan 4,660.60; Feb 395.26; Mar 439.32; Apr 3,224.69; May 2,501.14; Jun -328.32.
- Quarterly Q2 arithmetic from the three explicit monthly flow observations (Apr+May+Jun; no interpolation):
  - Assets: 1,643.45 + 932.56 + 2,522.90 = USD 5,098.91m.
  - Liabilities: 3,224.69 + 2,501.14 - 328.32 = USD 5,397.51m.
  - Difference liabilities minus assets = USD 298.60m, which rounds to the Q2 report's published net portfolio investment USD 299m. This is a consistency check, not a gross-leg inference: both legs were independently observed in the BDE table.
- Official BDE series search identifies monthly total portfolio asset series F068.G2.FLU.Z.0.S.A.Z.T.Z.Z.6.0.M and total portfolio liability series F068.G2.FLU.Z.0.S.P.Z.T.Z.Z.6.0.M; both monthly from Jan-2003 and sourced to Banco Central de Chile.
- Official methodology describes portfolio assets as resident Chilean investment in securities issued by non-residents and includes equity and debt instruments. The BDE metadata identifies USD million, monthly frequency, BPM6 and source BCCh.
- BDE indexed basket/page was captured, but downloadable raw response bytes, retrieval receipt and SHA-256 were not captured in this turn. The monthly values must therefore be treated as source-page observations, not as an immutable byte archive.

## 4. Reused archived IMF raw rows — no re-query
- Asset raw CSV docs/evidence/imf_bop_emde_20261119/raw/EMDE_A_NFA_T_P_F_ALL_UNITS_Q.csv, blob SHA 15449e87c9057291a1f52f2f8cd9805df55f9fb8: CHL A_NFA_T / P_F / USD / Q / 2026-Q2, OBS_VALUE=5098898918.11, SCALE=6.
- Liability raw CSV docs/evidence/imf_bop_emde_20261119/raw/EMDE_L_NIL_T_P_F_ALL_UNITS_Q.csv, blob SHA 15f379dc42e2760eb5f2384618e48f5ddc3177f1: CHL L_NIL_T / P_F / USD / Q / 2026-Q2, OBS_VALUE=5397501758.8, SCALE=6.
- For a diagnostic only, OBS_VALUE / 1,000,000 gives USD 5,098.89891811m asset and USD 5,397.5017588m liability. Differences from BDE monthly sums are +0.01108189m and +0.0082412m respectively. This near-match is consistent with rounding, but not admitted as PASS because same-vintage alignment, raw source bytes/hash, and exact revision cut-off have not yet been verified.
- SCALE is retained separately; no global/unapproved conversion rule is inferred. No numeric production crosswalk is authorized.

## 5. Acceptance matrix
| Gate | Result |
|---|---|
| Immutable 63-country cohort membership | PASS |
| Archived IMF Q2 asset/liability rows | PASS |
| Official BCCh Q2-2026 BOP release | PASS |
| Official BDE monthly asset and liability series labels/units | PASS |
| Q2 asset and liability values from three monthly observations | PASS — source-page capture |
| Q2 arithmetic and net consistency check | PASS — diagnostic only |
| Same-vintage alignment / release-revision timestamp | NOT_ESTABLISHED |
| BDE raw bytes, retrieval receipt, SHA-256 | NOT_CAPTURED |
| Exact source-to-IMF accounting/sign bridge | PARTIAL |
| Numeric validation admission | NOT_AUTHORIZED |
| CHL national validation | PARTIAL / NOT PASS |
| Cross-country aggregate | NOT_AUTHORIZED |

## 6. Decision and next bounded action
- This is a meaningful new source discovery: Chile's official BDE monthly flow series exposes both Q2 portfolio legs independently and their quarterly sums reconcile to the published net row to rounding. Do not upgrade to PASS yet.
- Next: capture the official BDE series observations via a supported documented export/API route as raw bytes; preserve response URL, retrieval timestamp, series codes, source update/vintage metadata, file bytes and SHA-256. Then compare with the same-vintage Q2 release/IMF panel, explicitly reconcile the BCCh sign convention to IMF A_NFA_T/L_NIL_T and apply rounding bounds only after source definitions align.
- If raw export is inaccessible, retain CHL PARTIAL and move to the next eligible cohort member. No net-to-leg back-solving, no IIP stock substitution, no annual/H1-to-quarter allocation, no unsupported sign/scale conversion.
- ₹0 spend. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
