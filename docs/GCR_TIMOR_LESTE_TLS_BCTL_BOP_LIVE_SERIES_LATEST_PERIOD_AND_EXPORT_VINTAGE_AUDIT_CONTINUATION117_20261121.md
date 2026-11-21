# Timor-Leste TLS — BCTL live BOP series latest-period and export-vintage audit (Continuation 117)
Date: 2026-11-21 (Asia/Kolkata)
Decision: **The public BCTL “Balance of Payments (Thousand USD)” live series exposes quarterly observations only through Jan–Mar 2025 (Q1 2025). Its “Export Excel” link resolves to a workbook explicitly named BoP_2025Q3.xlsx, i.e. Q3 2025 vintage, not Q2 2026. The chart's three numeric fields are not labelled in extracted source and cannot be identified as portfolio assets/liabilities. Thus the route does not provide verified Q2 2026 dual legs. The exact XLSX download failed; workbook contents and hash not captured. TLS remains NOT_VALIDATED / NOT PASS.**

## 1. Continuity preflight
Re-fetched current:
- Master Ledger blob SHA d5c6ff4eaae89d0a57cb480ed0f149a28767fa6e
- GCR Priority Queue blob SHA ffc0cefec854638081117e1904253891690f21d0
- TLS C116 report blob SHA 282807d8df8ffe3c91e96c14aa2f66f5f7234d69
C116 and C115 completed checks were not repeated.

## 2. Live BOP series — exact latest period exposed
- Official BCTL route: https://bancocentral.tl/en/portfolio/balanceofpayments/categoria_id/297/ano_id
- Page title and chart unit: “Balance of Payments (Thousand USD)”.
- Extracted series contains quarterly labels:
  Jan-Mar-2020, Apr-June-2020, Jul-Sep-2020, Oct-Dec-2020; then 2021–2024 quarters; and final observation “Jan - Mar-2025”.
- The final visible row is index 20, Q1 2025. No Q2 2025, Q3 2025, Q4 2025 or 2026 row is exposed in the page's extracted JSON.
- Each row exposes three numeric keys y, y2, y3, but the accessible HTML does not expose their legend/category labels. Do not assign these values to portfolio investment assets/liabilities or use them as dual legs.
- The chart page's year selector lists 2020–2025, but the exposed current JSON still ends Q1 2025.

## 3. Excel export endpoint — vintage identified, bytes unavailable
- The “Export Excel” control (link 194 on the official page) resolves to:
  https://bancocentral.tl/uploads/portfolio/ficheiros/1764122263_8744_BoP_2025Q3.xlsx
- Filename explicitly identifies workbook as BoP_2025Q3.xlsx.
- Web click redirected to BCTL home rather than exposing workbook content; direct container download failed. No XLSX bytes, size, sheets, values or SHA-256 captured.
- Therefore file name is evidence of Q3-2025 workbook vintage only; not evidence of Q2-2026 data.
- The older BCTL quarterly release schedule page lists Q1 2025, Q2 2025, Q3 2025 and Q4 2025 release dates; the separate live chart/export route still does not show a 2026 observation.

## 4. Methodology support / source boundaries
Official BCTL BOP metadata PDF:
https://www.bancocentral.tl/uploads/documentos/documento_1741650203_4205.pdf
- BCTL says BOP is broadly consistent with BPM6 (PDF text lines 46–50).
- BOP is quarterly and published within two months of reference period (lines 125–131).
- Unit of account is USD; all data are presented in USD (lines 133–138).
- Portfolio investment asset transactions are derived from Petroleum Fund balance sheet and commercial bank balance sheets (lines 243–246).
- Portfolio asset transactions are valued at market value including accrued coupon; market revaluations not arising from transactions are excluded (lines 147–151 and 345–347).
- These methodology notes do not provide current Q2 2026 values or separate asset/liability legs.
- BCTL H1 2026 Mid-Year Review portfolio investment = -USD 524.9m remains H1 aggregate only, not Q2 dual legs.

## 5. Gate matrix
- Official BCTL live BOP page: PASS.
- Series unit (chart): Thousand USD.
- Latest exposed chart period: Q1 2025.
- Three chart numeric keys labels: NOT_CAPTURED.
- Excel filename vintage: Q3 2025.
- XLSX bytes/workbook sheets/hash: NOT_CAPTURED.
- Q2 2026 portfolio assets: NOT_CAPTURED.
- Q2 2026 portfolio liabilities: NOT_CAPTURED.
- Q2 period/sign/vintage alignment: NOT_ESTABLISHED.
- Archived IMF comparison: NOT_DONE; no IMF query.
- TLS NOT_VALIDATED / NOT PASS; aggregate / production admission NOT_AUTHORIZED.

## 6. Rejected interpretations
- Do not treat page metadata/crawl date or Excel file timestamp as observation period.
- Do not treat Q3-2025 workbook filename as Q2-2026 evidence.
- Do not guess the y/y2/y3 legend from numerical patterns.
- Do not infer portfolio legs from net H1 portfolio component.
- Do not substitute IIP stocks or Petroleum Fund position/market valuation for BOP transactions.
- No H1-Q1 subtraction without same-vintage Q1 separate dual legs.

## 7. Next exact action
1. Actual browser/Computer Use is needed to save the exact BoP_2025Q3.xlsx export and inspect workbook sheets, legends and historical period headers. Do not retry the same direct download channel.
2. If workbook confirms only Q3 2025 latest, mark BCTL public chart/export vintage stale and advance to next eligible cohort country.
3. If a separate Q2 2026 official BOP release appears, capture raw bytes, source URL, UTC retrieval time, byte count and SHA-256 before parsing; verify portfolio assets and liabilities separately.
4. Do not query IMF again or rebuild cohort.

## 8. Sources
- BCTL live BOP series: https://bancocentral.tl/en/portfolio/balanceofpayments/categoria_id/297/ano_id
- Exact export URL (download failed): https://bancocentral.tl/uploads/portfolio/ficheiros/1764122263_8744_BoP_2025Q3.xlsx
- BCTL BOP methodology: https://www.bancocentral.tl/uploads/documentos/documento_1741650203_4205.pdf
- BCTL quarterly BOP/IIP release page: https://www.bancocentral.tl/publication/quert_bop_iip_sts/
- BCTL H1 2026 Mid-Year Economic Review: https://www.bancocentral.tl/publication/krep/download/594/

## 9. Protected invariants
No IMF re-query, no cohort rebuild, no synthetic data, no generic FX conversion, no sign flip, no net-to-leg inference, no stock-as-flow, no annual-to-quarter proration or cross-vintage H1-Q1 subtraction, no production changes. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged. UNKNOWN is never PASS. Research spend ₹0.


## Continuation 133 — BCTL public route closed as stale for Q2-2026 (2026-11-21)
- Rechecked current Ledger/Queue/cohort and TLS Continuation 117. Official live BCTL chart ends Q1-2025; export workbook name BoP_2025Q3.xlsx; H1-2026 mid-year review has only net portfolio component -USD524.9m, not separate Q2 legs. The previously inspected “Aug 2026” archive PDF contains observations only through 2016.
- No new official standalone Q2-2026 separate portfolio asset/liability table was found in the current BCTL public route evidence. Do not use H1 net, old Q3-2025 workbook, IIP stocks, or Petroleum Fund valuations as Q2 dual legs.
- TLS national Q2 dual legs NOT_CAPTURED; public route stale / Q2 NOT_AVAILABLE in inspected sources; TLS NOT_VALIDATED / NOT PASS. Advance to next fixed-cohort member. No IMF query/cohort rebuild; ₹0; UNKNOWN never PASS.
