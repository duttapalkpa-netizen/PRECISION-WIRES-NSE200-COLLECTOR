# Serbia SRB Q2-2026 — NBS July Bulletin prior-vintage cross-check (Continuation 107)
Date: 2026-11-20 (Asia/Kolkata)
Decision: **A previously uninspected official NBS July 2026 Statistical Bulletin PDF was located and its Table 2.3 rows extracted through web PDF text. This provides an independent publication vintage candidate for the anomalous +3,932 EURm portfolio-liability value. The available extracted lines include the value, but the PDF table header/month alignment could not be re-opened because subsequent PDF page fetch/screenshot calls timed out. Therefore exact attribution of +3,932 to May in this July vintage remains NOT_VERIFIED; no cross-vintage PASS is claimed.**

## 1. Continuity preflight
Re-fetched:
- Master Ledger blob SHA 761c100c418e2c7c003df0e46952deeebac34bba
- GCR Priority Queue blob SHA dbec3cfe50a6c13022252c0cf687d15620884368
- Continuation 106 blob SHA e5994fc9b1318aaa5b4cc4c4db8aaa1f91106b30
Excluded all PASS work: NBS sign/transaction-date FX method, IMF standards code semantics, exact IMF rows and NBS Q2 arithmetic.

## 2. New official vintage candidate
- Official NBS Statistical Bulletin — July 2026:
  https://www.nbs.rs/export/sites/NBS_site/documents-eng/publikacije/sb/sb_07_26.pdf
- PDF metadata/text confirms title “Statistical Bulletin — July 2026”, 156 pages. Contents identify Table 2.3 “Balance of Payments of the Republic of Serbia (BPM6)” on printed page 105.
- PDF text extraction for Table 2.3 returned:
  - Line 7410: 3.2.A Assets: 3, 28, 6, 30, -47, 21, 29, 73, 77, 121, -53, 24, 35, 62, 153, 78, 134, 945
  - Line 7411: 3.2.B Liabilities: 682, -63, -43, 97, 1,553, 1,697, 1,912, 442, -212, -796, -880, -889, 224, 1,686, 1,709, 66, 1,019, 1,373
  - Another Table 2.3 extracted block:
    - Line 7474: 3.2.A Assets: 39, -84, 233, -410, 79, 65, 149, -32, -28, -68, 91
    - Line 7475: 3.2.B Liabilities: 103, -93, -94, -6, -72, -23, -82, -19, -82, 3,932, -79, 199
- The July bulletin PDF table page (printed page 105; PDF page index 104) was located. Reopening the table header lines and screenshot later timed out; hence month-to-column alignment for the 3,932 value is not established in this continuation.
- September 2026 bulletin Table 2.3 independently prints May 2026 portfolio liabilities +3,932 EURm and May net -3,957 EURm, with May assets -25 EURm (already recorded in Continuation 101/102). July PDF is a potential earlier-vintage comparison, but exact matching month in July vintage must be header-verified before claiming consistency.
- This is a newly found official PDF source, not the XLS route. Raw PDF bytes/byte count/SHA-256 were not captured; web PDF text extraction only.

## 3. Updated gate matrix
- July 2026 NBS Statistical Bulletin PDF located: PASS.
- Table 2.3 portfolio asset/liability text rows extracted: PASS (text extraction only).
- July-vintage month header alignment for +3,932: NOT_VERIFIED (header fetch timed out).
- May 2026 +3,932 cross-vintage consistency: NOT_DONE.
- September 2026 May values: remain +assets -25 / liabilities +3,932 / net -3,957 EURm (existing C101/C102 evidence).
- XLS raw bytes/sheets/hash: NOT_CAPTURED.
- USD/EUR transaction-weighted bridge: NOT_ESTABLISHED.
- National coverage/timing/valuation equivalence: NOT_ESTABLISHED.
- SRB PARTIAL / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 4. Next exact actions
1. Re-open July 2026 Bulletin Table 2.3 printed page 105 using a stable PDF text or page-image route and capture the year/month header row.
2. Verify whether +3,932 in July vintage corresponds exactly to May 2026; if yes, compare its associated assets/net rows with September vintage and record revision status.
3. Preserve July and September vintages separately; do not overwrite either.
4. Continue NBS XLS raw capture only via byte-preserving route; do not infer FX or compare USD/EUR without official bridge.

## 5. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.
