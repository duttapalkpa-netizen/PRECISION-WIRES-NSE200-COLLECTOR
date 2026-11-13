# CDSL 31-Oct-2026 Fortnightly Report — Official Link Resolution and FX Display Check — 2026-11-13

## What is new in this task
Resolved the exact official CDSL archive link for the 31-Oct-2026 fortnightly sector-wise report by following the live archive index link (not by guessing a filename or URL). Opened the linked report and checked its visible structure, period labels, grand totals, and displayed FX conversion metadata.

## Source chain
1. Official CDSL FPI landing/index page: https://www.cdslindia.com/Publications/ForeignPortInvestor.html
   - Page header/footer metadata: last updated 05-Nov-2026.
   - Link text “October 31, 2026” is link id 170 in the retrieved page.
2. Exact linked report URL:
   https://www.cdslindia.com/publications/FII/FortnightlySecWisePages/Oct%2031%202026.html
3. Retrieved report title: “CDSL : Fortnightly Sector-wise FII Investment data”.
4. The opened report contains 24 sector/category rows plus Grand Total, with AUC at 15-Oct and 31-Oct and net-investment columns for 01–15 Oct and 16–31 Oct.

## Grand Total values as displayed (₹ crore and USD million)
| Measure | INR Cr | USD Mn |
|---|---:|---:|
| AUC as on 15-Oct-2026 | 7,346,751 | 772,781 |
| Net investment 01–15 Oct 2026 | -45,828 | -4,821 |
| Net investment 16–31 Oct 2026 | +21,354 | +2,243 |
| AUC as on 31-Oct-2026 | 7,284,170 | 764,749 |

## FX metadata
The report states period-end RBI reference rates:
- AUC as on 15-Oct-2026 and net investment 01–15 Oct: 95.0691 INR/USD.
- AUC as on 31-Oct-2026 and net investment 16–31 Oct: 95.2492 INR/USD.
It explicitly says the fortnightly report uses end-of-period RBI reference rates for INR-to-USD conversion, unlike the daily series which uses the daily RBI reference rate.

Independent rough conversion check using displayed rounded INR grand totals:
- 7,346,751 × 10 / 95.0691 = 772,780.11 USD Mn vs displayed 772,781 (difference +0.89).
- -45,828 × 10 / 95.0691 = -4,819.80 USD Mn vs displayed -4,821 (difference -1.20).
- 21,354 × 10 / 95.2492 = 2,241.91 USD Mn vs displayed 2,243 (difference +1.09).
- 7,284,170 × 10 / 95.2492 = 764,748.68 USD Mn vs displayed 764,749 (difference +0.32).

These are approximate comparisons against rounded displayed INR totals and a single published rate. They are NOT proof of error: underlying unrounded amounts and row-level conversion/rounding may explain the small differences. Do not force-adjust displayed figures or treat the rounded aggregate conversion as exact.

## Data interpretation safeguards
- This report is fortnightly sector-wise data, not a daily FPI aggregate.
- The 31-Oct report's period-end FX methodology is not interchangeable with CDSL daily RBI-rate conversion.
- Do not use this report to impute missing daily observations, including the unresolved 12-Nov cash record.
- This is a browser-retrieved HTML report, not an acquired raw downloadable archive binary. No MIME/byte count/raw SHA-256 or file schema validation is claimed.
- The exact official link is now resolved and reproducible from the CDSL index; this resolves link discovery, not raw-file acquisition.

## Acceptance ledger
| Check | Result |
|---|---|
| Official landing page archive entry located | PASS |
| Exact 31-Oct-2026 destination link followed | PASS |
| Report opened and date/period headings observed | PASS |
| 24 categories plus Grand Total structure observed | PASS |
| Grand Total INR/USD figures transcribed | PASS |
| Report-specific FX method/rates recorded | PASS |
| Approximate FX comparison completed | PASS (rounding differences disclosed; no forced adjustment) |
| Raw archive binary acquired | NOT ACQUIRED |
| Raw bytes/MIME/SHA-256/schema QA | NOT STARTED |
| Daily factor acceptance | NOT AFFECTED / BLOCKED independently |

## Invariants
₹0 spend; free official sources only; no paid APIs/feeds or external contact; no synthetic rows/timestamps; UNKNOWN is neither PASS nor FAIL; Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and 56×12 CORE-672 unchanged; research-only; no PR merge.
