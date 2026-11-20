# Serbia SRB Q2-2026 — July bulletin header recovery and vintage gate
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 108
Decision: **The prior-vintage header recovery attempt was not successful: official July 2026 PDF direct open and binary download both timed out/failed, and indexed search did not return the July Table 2.3 header. Official NBS publication records independently confirm the July 2026 bulletin was released 3-Sep-2026, but this release date does not prove the month-column alignment of the extracted 3,932. No cross-vintage PASS is claimed.**

## 1. Continuity preflight
Re-fetched:
- Master Ledger blob SHA 698a63e3efe4d1a77aa60f097e38d7f594e62a6f
- GCR Priority Queue blob SHA 7c6bc3b48199d8523c040edb9513a58c48afba83
- Continuation 107 blob SHA d7c063d63b2b8a19ff94c6b4fd31a82de98e7729
No completed PASS work repeated.

## 2. Exact recovery attempts and findings
- Direct official PDF: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_07_26.pdf — web open returned timeout; binary download also failed. No raw PDF bytes or SHA-256 captured.
- Search for exact July PDF + Table 2.3 portfolio asset/liability header returned no indexed result.
- Official NBS Statistical Bulletin index independently confirms the July 2026 bulletin entry and publication schedule 3-Sep-2026. This establishes publication date only, not the table's month header.
- Official NBS news archive independently lists “Statistical Bulletin - July 2026” dated 03/09/2026.
- Prior Continuation 107 extracted Table 2.3 rows and a 3,932 liability value from the July PDF text, but could not recover the header row. The sequence appears to include monthly observations; without the header, no specific month attribution can be made. Do not assume May.
- September 2026 NBS bulletin already establishes May asset -25, liability +3,932, net -3,957 EURm. This remains same-vintage evidence only for May values; no July-vintage revision conclusion.

## 3. Gate matrix
- July bulletin exists / publication date 03-Sep-2026: PASS.
- July Table 2.3 text rows extracted in Continuation 107: PASS (text extraction only).
- July table month header / column mapping: NOT_VERIFIED.
- July-vintage May liability 3,932: NOT_VERIFIED.
- July vs September May revision: NOT_DONE.
- July PDF raw bytes/hash: NOT_CAPTURED.
- NBS September PDF May value: CAPTURED in prior C101/C102 evidence.
- USD/EUR transaction-weighted bridge: NOT_ESTABLISHED.
- SRB PARTIAL / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 4. Next exact action
1. Obtain July 2026 PDF through an actual browser download or alternate official NBS-hosted path that preserves PDF bytes; then inspect printed page 105 and record the complete Table 2.3 header and row.
2. If inaccessible, request the official monthly BOP dataset from NBS archive through its actual UI only if a browser-capable environment is available; do not guess form parameters or use authenticated web service without explicit authorization.
3. Only after month alignment, compare May 2026 July-vintage asset/liability/net values with September 2026 vintage, recording revision deltas separately.
4. Keep FX and national-coverage gates unchanged.

## 5. Official sources
- NBS Statistical Bulletin index: https://nbs.rs/en/drugi-nivo-navigacije/publikacije-i-istrazivanja/SB/
- NBS News archive (July Bulletin release 03-Sep-2026): https://www.nbs.rs/en/drugi-nivo-navigacije/pres/arhiva-vesti/arhiva-vesti-g/
- NBS July 2026 Bulletin PDF: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_07_26.pdf
- NBS September 2026 Bulletin PDF: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_09_26.pdf

## 6. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
