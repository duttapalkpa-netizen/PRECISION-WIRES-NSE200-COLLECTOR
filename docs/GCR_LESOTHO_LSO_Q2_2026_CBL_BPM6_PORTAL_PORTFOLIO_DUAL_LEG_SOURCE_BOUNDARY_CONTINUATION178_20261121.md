# Lesotho (LSO) Q2-2026 — CBL BPM6 portal portfolio dual-leg source boundary (Continuation 178)
Date: 2026-11-21 (Asia/Kolkata)
Decision: FIXED-COHORT MEMBERSHIP PASS; OFFICIAL CBL STATISTICAL RESEARCH PORTAL IDENTIFIED AND INSPECTED; ITS BALANCE OF PAYMENTS 6 CATALOGUE EXPOSES A SINGLE AGGREGATE PORTFOLIO INVESTMENT SERIES (BPI_BPM6_XDC, MILLION MALOTI), NOT SEPARATE PORTFOLIO ASSET AND LIABILITY TRANSACTION SERIES; CBL QUARTERLY REVIEW TABLES INSPECTED IN THE AVAILABLE REPORT FAMILY ALSO PRESENT PORTFOLIO INVESTMENT NET ONLY; Q2-2026 NATIONAL DUAL LEGS NOT_CAPTURED; LSO PARTIAL / NOT PASS; AGGREGATE NOT_AUTHORIZED.

## 1. Continuity preflight and duplicate prevention
- Re-fetched Master Continuity Ledger (blob SHA `e563bf9c885099573e61edf68fb0fdc0c43db8fe`), GCR Master Priority Queue (`2ab318107262559252ac262c5d3da576da1fe7f9`), Historical Task Registry (`5eb66a9b0ddcd78cccf83a0e756feb76501ae887`) and immutable cohort (`31f5bfe5adb59f4c1a139b6d8c54b5ad9fb672c8`).
- Re-opened LKA C174–C177; no repeated Treasury extraction, Table 2.10 HTML route, or stale SDDS BOP.xlsx click/download.
- An initial candidate ALB was rejected after complete report-history retrieval revealed C139–C141 and the same Main-data/interactive export route was already bounded and closed. No ALB route was retried.
- Repository searches for `LSO`, `Lesotho`, Q2-2026 BOP and portfolio assets/liabilities returned no dedicated LSO country validation report.
- Exact immutable cohort row: `LSO,Lesotho,2026-Q2,A_NFA_T_PRESENT,L_NIL_T_PRESENT,BOTH_LEGS_PRESENT_IN_IMF_PANEL,NATIONAL_SOURCE_VINTAGE_VALIDATION_PENDING,NOT_AUTHORIZED`.
- No cohort rebuild and no IMF re-query.

## 2. New official source route inspected
- Central Bank of Lesotho official Statistical Research Portal: https://statisticalwebportal.azurewebsites.net/
- Portal instructions identify it as a data-download portal: select data items, frequency, date range, then Download.
- Its category is explicitly titled “Balance of Payments 6”; source is identified as Central Bank of Lesotho.
- The visible BPM6 BOP catalogue includes:
  - `BFA_BPM6_XDC` — Financial account
  - `BNFA_BPM6_XDC` — Net lending (+) / net borrowing (-) (balance from financial account)
  - `BDI_BPM6_XDC` — Direct investment
  - `BPI_BPM6_XDC` — Portfolio investment
  - `BFD_BPM6_XDC` — Financial derivatives
  - `BOI_BPM6_XDC` — Other investment
  - `BRA_BPM6_XDC` — Reserve assets
- Every listed BOP series is denominated in Million Maloti. The BOP6 catalogue does not list separate portfolio investment assets and liabilities series or equity/debt children. The only portfolio item exposed in this category is the aggregate `BPI_BPM6_XDC` series.
- The portal page's full visible BOP6 category was inspected; “assets” and “liabilities” matches elsewhere on the page belong to government finance / balance-sheet categories, not BOP portfolio transaction legs. They are not eligible substitutes.
- This is a concrete official source-family boundary, not proof that CBL has no detailed unpublished/other-format data. The portal's net-only portfolio series cannot independently validate IMF A_NFA_T and L_NIL_T.

## 3. Cross-check against CBL published quarterly report family
- Official CBL Quarterly Economic Review, September 2025: https://centralbank.org.ls/wp-content/uploads/QIII-2025-Quarterly-Economic-Review-1.pdf
- Table 19, “Financial Account Balance (Million Maloti)”, reports a single “Portfolio Investments net” row; it does not expose separate asset and liability rows in the table.
- The report table covers 2024 Q3 through 2025 Q3, so it does not provide Q2-2026 observations. It corroborates the report-family net-only presentation boundary only; it is not Q2-2026 evidence.
- CBL FAQ explains that the BOP is a period-based statement and that a quarterly survey is conducted by CBL; resulting data are published in CBL quarterly and annual reports. This supports the BOP flow distinction, but does not provide missing Q2-2026 portfolio legs.

## 4. Rejected substitutes and duplicate routes
- Rejected `BPI_BPM6_XDC` as a dual-leg substitute: it is one aggregate portfolio investment series, not separate asset and liability transaction observations.
- Rejected CBL Quarterly Economic Review “Portfolio Investments net” as a dual-leg substitute for the same reason.
- Rejected government finance foreign financial assets/liabilities catalogue items: they are government finance balance-sheet aggregates, not BOP portfolio investment flows.
- Rejected annual, H1, IIP stock, or IMF-only values as national dual-leg validation.
- No net-to-leg back-solving, sign flip, currency conversion, or fabricated observation was performed.
- The portal page was inspected for its published catalogue; no unsupported hidden API endpoint was guessed. No machine-readable export bytes or Q2 data rows were captured.

## 5. Acceptance matrix
| Gate | Status |
|---|---|
| LSO fixed 63-country cohort membership | PASS |
| No prior dedicated LSO report in scoped repository search | PASS |
| Official CBL Statistical Research Portal identified | PASS |
| Official BPM6 BOP6 catalogue and Million Maloti unit | PASS |
| Portfolio series identity `BPI_BPM6_XDC` | PASS |
| Separate Q2-2026 portfolio asset and liability series in inspected BOP6 catalogue | NOT_EXPOSED |
| CBL quarterly report-family table separate dual-leg publication | NOT_EXPOSED in inspected report |
| Exact Q2-2026 national asset observation | NOT_CAPTURED |
| Exact Q2-2026 national liability observation | NOT_CAPTURED |
| Raw national dual-leg export / bytes / SHA-256 | NOT_CAPTURED |
| National sign/scale/vintage bridge | NOT_ESTABLISHED |
| Numeric IMF dual-leg comparison | NOT_DONE |
| Full LSO national validation | PARTIAL / NOT PASS |
| 63-country aggregate admission | NOT_AUTHORIZED |

## 6. Next exact action
1. Do not re-query IMF or rebuild the cohort.
2. Do not repeat the same CBL portal catalogue inspection or substitute the net-only BPI series.
3. Reopen LSO only if a distinct official CBL Q2-2026 BOP detailed report, documented export/API, or a supported portal download payload is located that explicitly exposes portfolio assets and liabilities separately.
4. Otherwise move to the next fixed-cohort member after a complete repository report-history and duplicate-route preflight.

## 7. Protected invariants
₹0; free official sources only. No synthetic data, fabricated values/timestamps, IIP stocks as BOP flows, net-to-leg back-solving, unsupported FX/sign/scale transformation, repeated IMF request, or cohort rebuild. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS.
