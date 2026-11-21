# Poland (POL) Q2-2026 — NBP official quarterly release dual-leg capture
Date: 2026-11-21
Chapter: গবেষণা যাচাই অব্যাহত 47
Part: 11
Continuation sequence: 163
Decision: OFFICIAL Q2 RELEASE NOW IDENTIFIED AND BOTH PORTFOLIO LEGS CAPTURED FROM APPENDIX 1; RAW PDF BYTES/SHA-256 NOT_CAPTURED; USD/PLN TRANSACTION CONVERSION AND SAME-VINTAGE BRIDGE NOT_ESTABLISHED; POL PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight
- Re-fetched the current Master Continuity Ledger and GCR Priority Queue, plus the prior exact POL report.
- Prior POL report's quarantine concerned a different NBP PDF, bopa_en.pdf, whose front matter said March 2026 despite later quarter columns. That warning remains valid for that file only.
- A genuinely distinct, correctly titled official NBP quarterly release was identified: https://static.nbp.pl/dane/bilans-platniczy/bop_kw_en.pdf — “Balance of Payments in Q2 of 2026”, Warsaw, 30 September 2026.
- Existing IMF exact-key receipt/raw CSVs reused; no new IMF query and no cohort rebuild.

## 2. National Q2 dual-leg observations captured
Official NBP PDF Appendix 1, page 11 (PDF page 10), table unit “mn PLN”, Q2 2026 column:
- Portfolio investment — assets: **24,144 mn PLN**.
  - Equity securities: 9,616 mn PLN.
  - Debt securities: 14,528 mn PLN.
- Portfolio investment — liabilities: **70,910 mn PLN**.
  - Equity securities: 969 mn PLN.
  - Debt securities: 69,941 mn PLN.
- Arithmetic checks: 9,616 + 14,528 = 24,144; 969 + 69,941 = 70,910. These are source-table component sums, not inferred from a net total.
- The report narrative independently describes Q2 resident portfolio investment abroad as PLN 24.1bn and foreign portfolio inflows into Polish securities as PLN 70.9bn.
- Official release is explicitly Q2 2026 and dated 30-Sep-2026; quarterly compilation is based on monthly/quarterly reporting by Polish entities, official statistics and administrative sources.

## 3. Existing IMF exact values retained (no re-query)
From the prior immutable receipt:
- A_NFA_T = +USD 6,602m; SCALE=6; raw CSV SHA-256 19ba3d8918245d7abe73125d76c08e27f9970817cc1a46b8753763352e5a2e21 (4,891 bytes).
- L_NIL_T = +USD 19,391m; SCALE=6; raw CSV SHA-256 365bac8801d0951f3d69f863628e844c6da07b0e69651880614c815b859c769b (4,726 bytes).
- Exact values are not compared directly to PLN observations. No ad-hoc USD/PLN conversion or implied FX rate is used.

## 4. Retrieval and vintage boundary
- The Q2 PDF itself was accessible as a PDF through the official NBP static site and its contents were extracted by the web PDF reader. It provides a stable exact source URL and publication date.
- Separate raw-byte download attempt failed in the current container transfer route. Therefore byte count, HTTP headers, retrieval receipt and SHA-256 of the NBP PDF are NOT_CAPTURED. Do not substitute the Git blob SHA or the web reader text for raw PDF SHA-256.
- The NBP release date 30-Sep-2026 is known. The existing IMF raw-panel capture/archive is dated 19-Nov-2026; same-vintage/revision equivalence with the NBP September publication is NOT_ESTABLISHED.
- NBP Q2 report's detailed appendix is in PLN millions. A supported exact transaction-level USD/PLN conversion methodology or matched USD presentation for these exact portfolio legs has not yet been captured. No cross-currency residual/tolerance comparison is performed.

## 5. Acceptance matrix
| Gate | Result |
|---|---|
| Fixed cohort / existing IMF dual-leg rows | PASS (reused) |
| Official NBP Q2-2026 quarterly release and date | PASS |
| Q2 portfolio asset national value | PASS — 24,144 mn PLN |
| Q2 portfolio liability national value | PASS — 70,910 mn PLN |
| Equity/debt component arithmetic | PASS |
| Official NBP PDF raw bytes / SHA-256 | NOT_CAPTURED |
| Exact USD/PLN transaction conversion bridge | NOT_ESTABLISHED |
| Same-vintage/revision alignment | NOT_ESTABLISHED |
| Cross-currency numeric comparison | NOT_DONE |
| POL national validation | PARTIAL / NOT PASS |
| Cross-country aggregate | NOT_AUTHORIZED |

## 6. Decision and next bounded action
- The earlier “no Q2 national dual-leg values” blocker is closed: the correctly titled NBP Q2 release Appendix 1 contains both exact portfolio flow legs in PLN million.
- Next: obtain the official NBP Q2 PDF bytes via a genuinely supported transfer route and archive SHA-256; inspect the NBP methodology/metadata for the exact transaction FX conversion convention or locate a matched-vintage official USD presentation for these same two legs. Then establish the vintage bridge to the existing IMF receipt. Do not infer an FX rate from the two totals.
- If no valid conversion/vintage bridge is found, retain POL PARTIAL and proceed to the next country without downgrading the captured national observations.
- ₹0; official sources only. No synthetic data, fabricated timestamps, stock-as-flow, net-to-leg inference, ad-hoc currency conversion, IMF re-query, cohort rebuild or production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
