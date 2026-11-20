# Serbia SRB Q2-2026 — September-vintage exact month-header verification and July-vintage limit
Date: 2026-11-21 (Asia/Kolkata)
Continuation: 109
Decision: **A stronger official NBS PDF text source is now fully opened at Table 2.3 and its complete month header recovered. It independently verifies the September-2026 vintage's 2026 May portfolio assets -25 EURm, liabilities +3,932 EURm, net -3,957 EURm. Arithmetic identity holds exactly (-25 - 3,932 = -3,957). This closes the month-column ambiguity for September vintage only. It does not establish the July-2026 bulletin's column alignment or prove whether the May value was revised between July and September vintages.**

## 1. Continuity preflight
Re-fetched:
- Master Ledger blob SHA ccdda277aa8ee8cfa91a8d98c459e1dd24980509
- GCR Priority Queue blob SHA 545794c9590ebf5649b2d01a8dda0ad391e4a34a
- Continuation 108 blob SHA bac151f983b989d7bf5dae0d981b8bcbc6ab4d7d
Skipped all PASS work: NBS methodology, IMF semantics, archived IMF rows, cohort membership, and Q2 monthly aggregation.

## 2. New exact official evidence — September 2026 vintage
Official NBS Statistical Bulletin — September 2026, Table 2.3:
- Opened full PDF text and located Table 2.3 at extracted lines 8102–8184 (printed page 105).
- Header at lines 8110–8111 explicitly pairs month/year columns: 2025 Jan, 2026 Jan, 2025 Feb, 2026 Feb, 2025 Mar, 2026 Mar, 2025 Apr, 2026 Apr, 2025 May, 2026 May, 2025 Jun, 2026 Jun, 2025 Jul, 2026 Jul, 2025 Aug, 2026 Aug.
- 2026 May is therefore the 10th data column after ITEM in the table.
- Table rows:
  - 3.2 Portfolio investment, net: 2026 May = -3,957 EURm (line 8145).
  - 3.2.A Assets: 2026 May = -25 EURm (line 8146).
  - 3.2.B Liabilities: 2026 May = +3,932 EURm (line 8147).
- Arithmetic: -25 - 3,932 = -3,957 EURm, exact.
- NBS notes at lines 8178–8180 state BPM6 basis, data available until 17-Sep-2026 and subject to correction as official source data change. Thus this is a September 2026 publication vintage.
- This is official extracted PDF text; raw PDF bytes, byte count and SHA-256 were not captured.

## 3. July-vintage cross-check boundary
- July 2026 Bulletin PDF remains inaccessible through the current web PDF fetch route (timeout); no raw bytes or complete header captured.
- Continuation 107 previously extracted a Table 2.3 liability row containing 3,932 but no header. The July row's month attribution remains NOT_VERIFIED.
- Therefore September May value is now exact and internally reconciled, but July-to-September revision status remains NOT_DONE. Do not label this a cross-vintage confirmation.

## 4. Updated gate matrix
- September 2026 Table 2.3 month header: PASS.
- September-vintage May 2026 assets -25 EURm: PASS.
- September-vintage May 2026 liabilities +3,932 EURm: PASS.
- September-vintage May net -3,957 EURm: PASS.
- Arithmetic identity: PASS.
- July-vintage header / month mapping: NOT_VERIFIED.
- July-to-September revision comparison: NOT_DONE.
- NBS raw PDF bytes/hash: NOT_CAPTURED.
- USD/EUR transaction-weighted bridge: NOT_ESTABLISHED.
- National scope/timing/valuation equivalence: NOT_ESTABLISHED.
- SRB PARTIAL / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 5. Next exact action
1. Recover July 2026 Bulletin PDF through a real browser or alternate official byte-preserving route and inspect Table 2.3's complete month header.
2. If the July row is verified as May, compare July-vintage asset/liability/net separately against September values and record revisions. Do not infer month based only on row order.
3. Capture original PDF bytes, HTTP headers/status, timestamp, byte count and SHA-256 before parsing if retrieval succeeds.
4. Keep FX and national coverage gates unchanged; no cross-currency numeric comparison yet.

## 6. Official source
- NBS Statistical Bulletin — September 2026, Table 2.3, printed p.105: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_09_26.pdf
- NBS July 2026 Bulletin candidate: https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_07_26.pdf

## 7. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
