# Serbia SRB — July 2026 Bulletin retrieval route exhaustion and next gate
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 111
Decision: **The official NBS July issue is confirmed in both Serbian and English archives, but all currently exposed routes resolve to an interactive archive form or a direct PDF that times out in the available retrieval channel. Search indexing exposes no Table 2.3 July header. No new numeric observation can be verified. The July-vintage month alignment remains NOT_VERIFIED; do not repeat the same failed URL fetch as if it were progress. The September-vintage May values remain the only exact May vintage captured.**

## 1. Continuity preflight
Re-fetched:
- Master Ledger blob SHA eeef11fd8bfd0ed321e5e5ba35ccf3a6c52f79c9
- GCR Priority Queue blob SHA 831c53b4843e9afcac1402a54d75184f98ea24fb
- Continuation 110 blob SHA 13eab75efb08b133c36fe8cd4dcfc989df7832f4
Excluded all PASS work: NBS sign/transaction FX methodology, IMF standards mapping, archived IMF rows, September-vintage May values and arithmetic.

## 2. Fresh official-source check (2026-11-21)
- Current NBS Serbian Statistical Bulletin archive shows September 2026 as the currently linked issue and archive calendar row 31-Aug-2026 | July 2026. It renders archive controls only as Select/Input/Show in extracted HTML.
- English NBS Bulletin archive similarly exposes Select/Input/Show, and its release calendar records 3-Sep-2026 | July 2026.
- Official Serbian news archive lists “Statistički bilten - jul 2026. godine” dated 31.08.2026; English archive lists “Statistical Bulletin - July 2026” dated 03/09/2026. These confirm issue identity/date only.
- Direct official July PDF URL was attempted again and returned HTTP/tool-side 400 timeout. Exact search for July PDF + Table 2.3 + 3,932 returned no indexed Table 2.3 header or month alignment.
- Official NBS BOP page continues to expose September 2026 monthly and detailed BPM6 workbooks, not a July monthly XLS direct link. No public July PDF alternate path or data API discovered in this pass.
- NBS web-service route remains account-gated per Continuation 106; no application/contact was made. No browser DOM execution or raw binary retrieval capability available in this pass.
- September 2026 PDF is fully indexed and its Table 2.3 header and May values are exact (Continuation 109).

## 3. Evidence status
- July issue identity/publication dates: PASS.
- July PDF/Table 2.3 header: NOT_CAPTURED.
- July Table 2.3 liability row with 3,932: text fragment captured in C107, month attribution NOT_VERIFIED.
- July-vintage May assets/liabilities/net: NOT_VERIFIED.
- September-vintage May assets -25, liabilities +3,932, net -3,957 EURm: PASS; arithmetic identity PASS (C109).
- July-to-September vintage revision: NOT_DONE.
- NBS raw PDF bytes/hash: NOT_CAPTURED.
- FX bridge and national scope/timing/valuation equivalence: NOT_ESTABLISHED.
- SRB PARTIAL / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 4. Next action — route change required
Do not repeat direct July PDF fetch or infer form parameters. To progress further, an actual browser with DOM inspection and download support is required to execute the official archive form's Show action and capture the generated file. If no such capability is available, pause this specific retrieval rather than falsely marking PASS; keep the July-vintage gate OPEN/BLOCKED. No authenticated web-service application or external contact without explicit user approval.

## 5. Official sources
- NBS Serbian Statistical Bulletin archive: https://nbs.rs/sr/drugi-nivo-navigacije/publikacije-i-istrazivanja/SB/index.html
- NBS English Statistical Bulletin archive: https://nbs.rs/en/drugi-nivo-navigacije/publikacije-i-istrazivanja/SB/
- NBS Serbian news archive: https://www.nbs.rs/sr/drugi-nivo-navigacije/pres/arhiva-vesti/arhiva-vesti-g/index.html
- NBS English news archive: https://www.nbs.rs/en/drugi-nivo-navigacije/pres/arhiva-vesti/arhiva-vesti-g/
- NBS July PDF (retrieval timed out): https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_07_26.pdf
- NBS September PDF: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_09_26.pdf

## 6. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
