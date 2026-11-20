# Serbia SRB Q2-2026 — NBS BPM6 sign, transaction-FX methodology and revision route
Date: 2026-11-20 (Asia/Kolkata)
Continuation: Research verification 44 / Continuation 103
Decision: **Official NBS BPM6 sign convention and transaction-currency conversion methodology PASS; exact cross-currency numerical bridge remains NOT_ESTABLISHED; newer September 2026 monthly BOP dataset exists but its XLS byte route is inaccessible through current retrieval bridge; May-2026 revision check NOT_DONE; SRB PARTIAL / NOT PASS; aggregate NOT_AUTHORIZED.**

## 1. Continuity preflight / PASS work excluded
- Re-fetched Master Ledger (blob SHA bd4259ad6176cbbcd0d481c12c012efff63f7493), GCR Priority Queue (blob SHA 250e3cce04832837cf942b6cd285c62db825b7a2), SRB Continuation 102 (blob SHA 874f1908814137b67c0d4032752b73dd3a29e207), and SRB Continuation 101 (blob SHA ca0eb8844ab9d14a378f4278506f363fdf776c65).
- Excluded completed work: immutable cohort membership, NBS monthly Q2 extraction/arithmetic, exact archived IMF SRB dual rows. No IMF query or cohort rebuild.

## 2. New official NBS BPM6 methodology evidence
Official NBS Explanatory Notes, “Balance of Payments of the Republic of Serbia (BPM6)”, PDF `II-EOI-PB-e.pdf`, pp. 2–3 (PDF page labels 2–3; web lines 62–111), establish:
- NBS compiles BOP under IMF BPM6 and disseminates monthly and annual data in EUR million and USD million.
- Original-currency transactions are recalculated into reporting currency using the official NBS middle exchange rate **on the transaction date**.
- BPM6 financial-account items use the assets-liabilities approach.
- An increase in assets/liabilities is shown positive; a decrease is shown negative.
- Net is calculated as assets minus liabilities.
- Portfolio investment includes equity securities with less than 10% ownership and debt securities; NBS says compilation uses ITRS through banks and NBS plus the Central Securities Depository and Clearing House.
- This resolves the NBS-side sign convention and confirms the conversion is transaction-date-based, not quarter-end or generic period-average FX.

## 3. What this resolves — and what it does not
- NBS sign presentation: PASS (asset/liability increases positive; decreases negative; net=assets−liabilities).
- NBS reporting currency conversion method: PASS (official middle rate on each transaction date).
- Direct numerical conversion of published Q2 EURm aggregates into IMF USDm: NOT_ESTABLISHED. Transaction-level underlying source-currency amounts and transaction dates are not present in the monthly aggregate table; applying one monthly/quarterly FX rate would not reproduce the official method.
- IMF A_NFA_T / L_NIL_T sign/concept equivalence to NBS portfolio asset/liability rows: plausible mapping but not independently established by this NBS note alone; keep NOT_ESTABLISHED pending exact IMF metadata/definition bridge.
- Same-vintage alignment: NOT_ESTABLISHED.

## 4. Newer official vintage / route check
- NBS official Balance of Payments page now lists “Balance of payments - monthly, September 2026 (BPM6)” and a separate “details (BPM6)” XLS dataset. Page also records “Balance of payments developments in September 2026” dated 18-Nov-2026.
- This is a potentially useful later data vintage for checking whether May-2026 +3,932 EURm liability was revised.
- Exact XLS locators exposed by the official page:
  - `https://www.nbs.rs/export/sites/NBS_site/documents-eng/statistika/ino_ekonomski_odnosi/platni_bilans/balance_of_payments_26.xls`
  - `https://www.nbs.rs/export/sites/NBS_site/documents-eng/statistika/ino_ekonomski_odnosi/platni_bilans/balance_of_payments_detailed_26.xls`
- Current retrieval bridge rejects the XLS content-type (HTTP/tool-side 400 unsupported content-type); raw workbook bytes, sheet names, values, byte count and SHA-256 were not captured. Do not claim revision confirmation from the page listing alone.
- The NBS explanatory-notes PDF was inspected through official web text; raw PDF bytes and SHA-256 not captured in this continuation.

## 5. Updated gate matrix
- NBS BPM6 official sign convention: PASS.
- NBS transaction FX methodology: PASS.
- Latest September 2026 monthly BOP dataset locator identified: PASS.
- Later-vintage May-2026 portfolio liability value: NOT_CAPTURED / NOT_DONE.
- Raw NBS XLS/PDF bytes and SHA-256: NOT_CAPTURED.
- Exact IMF SRB rows: CAPTURED in Continuation 102.
- IMF-to-NBS exact definition/sign bridge: NOT_ESTABLISHED.
- Transaction-level FX bridge to compare USD and EUR: NOT_ESTABLISHED.
- Same-vintage dual-leg comparison: NOT_DONE.
- SRB: PARTIAL / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 6. Next exact actions
1. Obtain the official September 2026 BOP XLS and detailed XLS through a supported byte-preserving route (or official NBS downloadable data series route); record bytes, size, SHA-256, retrieval timestamp and workbook sheets before parsing.
2. Check May-2026 portfolio asset/liability rows against the September 2026 vintage and record revisions without overwriting prior vintage.
3. Retrieve authoritative IMF indicator metadata for A_NFA_T and L_NIL_T and prove the mapping to NBS portfolio assets/liabilities.
4. Do not convert NBS quarterly EUR totals with an arbitrary monthly average or quarter-end FX rate. A comparable USD figure requires transaction-date weighted source data or an officially published USD series with a documented same-vintage bridge.

## 7. Official sources
- NBS Explanatory Notes (BPM6): https://www.nbs.rs/export/sites/NBS_site/documents-eng/statistika/mo/II-EOI-PB-e.pdf
- NBS Balance of Payments page: https://www.nbs.rs/en/drugi-nivo-navigacije/statistika/platni_bilans/index.html
- NBS September 2026 Statistical Bulletin: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_09_26.pdf

## 8. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX-rate substitution, no sign flip, no net-to-leg inference, no stock-as-flow, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
