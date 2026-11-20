# Serbia SRB Q2-2026 — NBS alternate data-route and next-vintage gate
Date: 2026-11-20 (Asia/Kolkata)
Continuation: 105
Decision: **Alternative official NBS publication route audited. No separate public CSV/HTML monthly BOP dataset or documented USD series located in the inspected official NBS pages. Current September 2026 monthly and detailed BOP data remain XLS-only; web retrieval rejects XLS content-type. The next scheduled Statistical Bulletin release is 3-Dec-2026 for October 2026 data, so it is a future vintage candidate, not available evidence today. May revision and USD bridge remain NOT_DONE.**

## 1. Continuity preflight
Re-fetched:
- Master Ledger blob SHA 554fa175e22b21db928da579a05ffc63d267fda0
- GCR Priority Queue blob SHA ca9822d94a496ec27b5665d2c223c548b800a7fa
- Continuation 104 blob SHA fd1253e3c6f9b2681a825a756c4a88252f83ee80
Excluded all PASS work: NBS BPM6 sign/transaction-date FX methodology, IMF A/L and portfolio semantics, exact IMF rows and NBS Q2 aggregation.

## 2. Alternate NBS official route audit
- Official NBS BOP page lists only September 2026 monthly BPM6 and detailed BPM6 workbooks plus historical 2007–2025 workbooks; no CSV or HTML monthly BOP table link is exposed in the page text.
- Direct clicks on the official monthly and detailed XLS links fail with HTTP/tool-side 400 unsupported content type application/vnd.ms-excel. No workbook bytes, workbook sheets, values, byte count or SHA-256 captured.
- NBS Statistical Bulletin page links to September 2026 bulletin and a generic “Data series in XLS format” page; that link resolves to general Statistics landing page, not a directly exposed CSV/HTML BOP series. No separate official USD-denominated BOP flow dataset was located in the inspected NBS pages/search results.
- The Statistical Bulletin page release calendar explicitly lists 3-Dec-2026 for October 2026 data. This is a future scheduled release, not evidence of a current later vintage.
- NBS official statistics landing page reports “Balance of payments, Republic of Serbia” dated 18-Nov-2026, but its visible index does not expose a downloadable alternative series or separate USD legs.
- IMF BPM6 and NBS method sources previously captured remain unchanged. No FX rate or net-to-leg inference used.

## 3. Gate matrix
- NBS official XLS locator: PASS (identified).
- XLS byte-preserving retrieval: BLOCKED by unsupported content type.
- Alternate official CSV/HTML monthly BOP flow route: NOT_FOUND in inspected public pages (not proof none exists behind interactive archive).
- Official NBS USD separate asset/liability series: NOT_FOUND in inspected public pages.
- Next NBS monthly bulletin vintage (October 2026, scheduled 3-Dec-2026): FUTURE / NOT_YET_AVAILABLE.
- May 2026 revised separate portfolio legs: NOT_CAPTURED / NOT_DONE.
- Transaction-weighted USD/EUR bridge: NOT_ESTABLISHED.
- National scope/timing/valuation equivalence: NOT_ESTABLISHED.
- SRB PARTIAL / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 4. Next exact actions
1. Inspect NBS archive form's underlying official data endpoint / browser-export path using an approved byte-preserving route; if XLS cannot be parsed, preserve original workbook bytes and use a local XLS parser.
2. Re-check official NBS BOP page and October-2026 Statistical Bulletin after scheduled 3-Dec-2026 release; capture separate May monthly asset and liability revisions as a distinct vintage.
3. Do not assume the NBS statistics landing page or bulletin XLS series is USD; verify workbook labels and units before use.
4. Keep comparison blocked until transaction FX or official same-currency series and national coverage/timing/valuation equivalence are documented.

## 5. Official sources
- NBS Balance of Payments page: https://www.nbs.rs/en/drugi-nivo-navigacije/statistika/platni_bilans/index.html
- NBS Statistical Bulletin page: https://nbs.rs/en/drugi-nivo-navigacije/publikacije-i-istrazivanja/SB/
- NBS Statistics landing page: https://nbs.rs/en/drugi-nivo-navigacije/statistika/index.html

## 6. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
