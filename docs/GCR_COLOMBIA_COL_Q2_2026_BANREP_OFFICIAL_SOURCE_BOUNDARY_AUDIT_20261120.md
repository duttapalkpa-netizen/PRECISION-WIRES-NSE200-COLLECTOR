# Colombia (COL) Q2-2026 — Banco de la República official-source boundary audit
Date: 2026-11-20 (Asia/Kolkata)
Decision: official Q2 report and SDDS page inspected; direct Q2 portfolio transaction legs NOT_EXTRACTED; national numeric validation NOT_DONE; same-vintage NOT_ESTABLISHED; aggregate NOT_AUTHORIZED.

## Continuity and duplicate rejection
- Reused the fixed 63-country 2026-Q2 dual-leg cohort. Its existing coverage matrix records COL with 46 observations in each of A_NFA_T and L_NIL_T, both ending 2026-Q2. This is panel availability only, not numeric admission.
- Repository search found no prior COL national-source report or COL Q2-2026 portfolio-flow reconciliation. No cohort rebuild, IMF re-query, or panel reconstruction was performed.
- Existing IMF normalized panel and exact-key receipt were not modified. No raw COL IMF observation values were transcribed or asserted in this source-boundary task.

## Official Banco de la República evidence
1. Banco de la República Q2-2026 Balance of Payments and International Investment Position report:
   https://banrep.gov.co/es/publicaciones-investigaciones/informe-balanza-pagos/segundo-trimestre-2026
   Publication date: 2026-09-01. The official report states Q2 financial-account net capital inflows of USD 3,719m and says these include net liquidation of external assets (USD 6,149m), derivative gains paid by nonresidents (USD 804m), partially offset by decreases in external liabilities (USD 2,683m), plus reserve-asset transactions (USD 550m). It describes net liquidation of portfolio instruments as a partial offset, but does not publish Q2 portfolio asset and liability transaction legs separately in the inspected report text/PDF.
2. Exact official report PDF rendering:
   https://banrep.gov.co/es/print/pdf/node/66270
   Inspected PDF pages 0–4. Page 1 lines 22–32 and page 3 lines 44–53 contain the financial-account summary and the BPM6 sign explanation. The report says financial-account presentation uses the same sign as the current account. This is a general financial-account presentation note; it is not a sufficient portfolio-component-specific crosswalk for A_NFA_T/L_NIL_T.
3. Banco de la República SDDS economic/financial data page:
   https://www.banrep.gov.co/economia/dsbb/imfcolom.htm
   Page states last updated 2026-11-13. Its Q2/26 portfolio rows under International Investment Position show ASSET STOCKS: portfolio investment USD 125,046.1m (equity 72,701.1; debt instruments 52,344.9) and LIABILITY STOCKS: USD 118,800.9m (equity 7,692.1; debt instruments 111,108.8). These are end-period IIP positions, NOT Q2 BOP transaction flows. They are explicitly excluded from comparison to IMF A_NFA_T/L_NIL_T.
   The same page defines (p) provisional and (r) revised in its footnotes; no observation-specific vintage/revision timestamp for the Q2 portfolio-flow legs was identified.
4. BanRep's statistics portal link from the report resolves to a series page for current-account/financial-account statistics but the web reader timed out. No values, export, or raw bytes were obtained from that route in this task.

## Source boundary / fail-closed decision
- Q2 portfolio transaction legs (net acquisition of financial assets and net incurrence of liabilities): NOT_EXTRACTED.
- Q2 financial-account aggregate: USD 3,719m, but it includes reserves and derivatives and is not a portfolio-only net flow; do not use as proxy.
- Q2 portfolio IIP stocks: available, but wrong measurement type for a flow reconciliation; explicitly NOT_ADMITTED.
- National sign mapping: general BPM6 financial-account presentation note located, but portfolio-row direction mapping remains NOT_ESTABLISHED.
- Same-vintage bridge to the existing IMF Q2 panel: NOT_ESTABLISHED.
- No numeric residual, tolerance, dual-leg PASS, or aggregate authorization is claimed.

## Next exact action
Use the official BanRep statistics portal's underlying public series/export metadata (not the IIP stock rows) to identify the two Q2-2026 portfolio transaction series, their exact labels, units, signs, source update/revision metadata and raw export route. If the public export remains inaccessible or does not expose separate legs, preserve COL as BLOCKED / NOT PASS and move to the next eligible cohort member. Do not re-query IMF or rebuild the cohort.

## Invariants
No paid sources, no fabricated values/timestamps, no stock-flow substitution, no inferred sign flip, no netting, no forward-fill, no aggregate. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
