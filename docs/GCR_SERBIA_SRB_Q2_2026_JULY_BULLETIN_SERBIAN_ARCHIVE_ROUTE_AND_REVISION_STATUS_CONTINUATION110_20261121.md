# Serbia SRB Q2-2026 — July Bulletin Serbian archive route and revision status
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 110
Decision: **A second official-language route was checked. NBS Serbian news archive independently confirms the July Bulletin was published 31-Aug-2026 (English archive says 03-Sep-2026; likely separate site publication dates). The Serbian Statistical Bulletin archive is still an interactive form with no exposed issue-specific PDF href in extracted text. Direct July PDF open still times out. No new July-vintage May observations or revision comparison can be certified. The exact September-vintage May legs remain verified.**

## 1. Continuity preflight
Re-fetched:
- Master Ledger blob SHA 856d68b455fd5f80cf5d19aae5fb82717f447ef2
- GCR Priority Queue blob SHA 6460923fd2db5f709708b3c6d1e1b74f202d6a36
- Continuation 109 blob SHA e3217fd96e3fbc3dd1593e787029e3cafd929100
Skipped PASS work: NBS methodology, IMF standards mapping, archived IMF rows, September-vintage exact May values and arithmetic.

## 2. Official Serbian archive route inspected
- Official NBS Serbian Statistical Bulletin page: https://nbs.rs/sr/drugi-nivo-navigacije/publikacije-i-istrazivanja/SB/index.html
- It confirms July issue in archive calendar: 31-Aug-2026 | Jul 2026.
- Official Serbian NBS news archive: https://nbs.rs/sr/drugi-nivo-navigacije/pres/arhiva-vesti/arhiva-vesti-g/index.html
- It lists “Statistički bilten - jul 2026. godine” dated 31.08.2026. English NBS news archive lists “Statistical Bulletin - July 2026” dated 03/09/2026. Both establish an official July issue but not Table 2.3's month header.
- Serbian Statistical Bulletin page's archive text exposes only an interactive Select/Input form; no July-specific PDF URL or result link is exposed in the extracted page.
- Direct English July PDF URL https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_07_26.pdf again returned timeout on open. No binary bytes, page image, or header recovered.
- No month alignment was inferred from extracted row order. The 3,932 value in July extraction remains unattributed to a month.

## 3. September-vintage May values — retained, not reworked
From Continuation 109 official September 2026 Bulletin Table 2.3:
- May 2026 portfolio assets: -25 EURm
- May 2026 portfolio liabilities: +3,932 EURm
- May 2026 net: -3,957 EURm
- Identity: -25 - 3,932 = -3,957.
These remain PASS for September-vintage only. No July-vintage comparison implied.

## 4. Updated gate matrix
- September-vintage May month header and three values: PASS.
- July issue existence / publication dates: PASS.
- July Table 2.3 extracted row containing 3,932: CAPTURED in Continuation 107 (text only).
- July Table 2.3 month header / 3,932 column mapping: NOT_VERIFIED.
- July-to-September May revision comparison: NOT_DONE.
- July raw PDF bytes/hash: NOT_CAPTURED.
- USD/EUR transaction-weighted bridge: NOT_ESTABLISHED.
- National scope/timing/valuation equivalence: NOT_ESTABLISHED.
- SRB PARTIAL / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 5. Next exact action
1. Inspect Serbian archive form with a browser capable of reading DOM and executing the Show action; record the exact generated July PDF URL and response headers.
2. Capture PDF bytes before parsing; inspect Table 2.3 header and corresponding May asset/liability/net values.
3. Compare July-vintage May values against September values and record revisions separately.
4. If the form requires authentication, stop; do not submit application/contact NBS without explicit user approval.

## 6. Official sources
- NBS Serbian Statistical Bulletin archive: https://nbs.rs/sr/drugi-nivo-navigacije/publikacije-i-istrazivanja/SB/index.html
- NBS Serbian news archive: https://nbs.rs/sr/drugi-nivo-navigacije/pres/arhiva-vesti/arhiva-vesti-g/index.html
- NBS English news archive: https://www.nbs.rs/en/drugi-nivo-navigacije/pres/arhiva-vesti/arhiva-vesti-g/
- NBS July 2026 Bulletin PDF candidate: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_07_26.pdf

## 7. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
