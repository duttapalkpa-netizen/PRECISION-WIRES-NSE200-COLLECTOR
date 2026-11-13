# CDSL FPI Daily — 13-Nov-2026 Cash and Derivatives QA

## Source identity and lag
- Official source: https://www.cdslindia.com/eservices/publications/fiidaily
- CDSL displayed reporting date: 13-NOV-2026.
- CDSL note states cash figures are compiled from custodian reports submitted on the reporting date and represent trades conducted on/up to previous trading day(s).
- Derivatives figures are compiled from NSE, BSE, MSEI, NCDEX and MCX reports submitted on the reporting date and represent previous trading day positions.
- Therefore report date must not be mistaken for same-day trade date; retain CDSL reporting date and source lag note.
- Rendered official HTML inspected; raw archive bytes not acquired; no raw SHA-256 claimed.

## Cash-market totals (INR crore)
| Category | Purchases | Sales | Net |
|---|---:|---:|---:|
| Equity incl. primary/others | 21,500.33 | 12,601.53 | 8,898.80 |
| Debt-General | 727.92 | 31.14 | 696.78 |
| Debt-VRR | 43.83 | 117.59 | -73.76 |
| Debt-FAR | 1,012.33 | 805.30 | 207.03 |
| Hybrid | 29.71 | 31.08 | -1.37 |
| Mutual Funds | 0.33 | 0.49 | -0.16 |
| AIF | 0.00 | 0.00 | 0.00 |
| **Total** | **23,314.45** | **13,587.13** | **9,727.32** |
- USD net investment displayed: USD 1,037.415 million.
- Displayed conversion rate: INR 93.765 per USD.

## Cash arithmetic QA
- PASS: category purchases sum to INR 23,314.45 crore.
- PASS: category sales sum to INR 13,587.13 crore.
- PASS: category net sums to INR 9,727.32 crore.
- PASS: total purchases minus sales = INR 9,727.32 crore.
- Category net values also reconcile to total: 8,898.80 + 696.78 - 73.76 + 207.03 - 1.37 - 0.16 + 0 = 9,727.32.
- USD cross-currency check not independently performed in this report.

## Derivatives end-of-day positions (as displayed)
Amounts INR crore; report date 13-Nov-2026.
| Product | Buy contracts | Buy amount | Sell contracts | Sell amount | End OI contracts | End OI amount |
|---|---:|---:|---:|---:|---:|---:|
| INDEX_FUTURES | 30,714 | 5,266.61 | 9,962 | 1,700.53 | 191,292 | 32,628.02 |
| INDEX_OPTIONS | 26,234,705 | 4,318,864.84 | 26,530,890 | 4,366,465.52 | 3,665,602 | 617,091.24 |
| STOCK_FUTURES | 293,579 | 20,578.05 | 303,617 | 20,856.12 | 6,128,144 | 413,220.87 |
| STOCK_OPTIONS | 290,131 | 21,336.77 | 314,597 | 22,945.20 | 1,523,150 | 106,096.42 |
| INTEREST_RATE_FUTURES | 0 | 0.00 | 0 | 0.00 | 3,800 | 73.47 |
| CURRENCY_FUTURES | 50,409 | 474.26 | 59,280 | 557.46 | 285,903 | 2.70 |
| CURRENCY_OPTIONS | 0 | 0.00 | 0 | 0.00 | 0 | 0.00 |
| COMMODITY_FUTURES | 35,069 | 1,121.31 | 33,480 | 1,005.39 | 77,705 | 2,011.00 |
| COMMODITY_OPTIONS | 1,141,066 | 31,237.70 | 1,135,485 | 30,555.20 | 426,257 | 13,957.82 |

## Adjacent-report OI delta: 12-Nov report to 13-Nov report
Delta = current displayed EOD OI minus previous report displayed EOD OI. This compares adjacent CDSL reporting dates; due to CDSL's previous-trading-day note, it is not same-calendar-day trading attribution.
| Product | Contract delta | OI amount delta (INR Cr) |
|---|---:|---:|
| INDEX_FUTURES | +6,338 | +1,278.95 |
| INDEX_OPTIONS | -652,376 | -103,757.67 |
| STOCK_FUTURES | +12,458 | +3,110.13 |
| STOCK_OPTIONS | +28,472 | +2,833.54 |
| INTEREST_RATE_FUTURES | 0 | -0.16 |
| CURRENCY_FUTURES | -9,753 | -0.08 |
| CURRENCY_OPTIONS | 0 | 0.00 |
| COMMODITY_FUTURES | +1,983 | +110.45 |
| COMMODITY_OPTIONS | +29,835 | +654.74 |

## Interpretation controls
- OI contract count and OI amount are distinct measures; they may not move proportionally.
- OI movement alone does not establish bullish/bearish positioning; no call/put or long/short breakdown is supplied in this table.
- Keep CDSL custodian-confirmed cash flow, CDSL derivatives positioning, and NSE provisional T-day exchange flows as distinct data products.
- Do not infer missing daily rows from monthly/fortnightly data.
- No synthetic data, no paid source, no spend, no external contact.
- Research-only; no production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics or Hard Gate changed. No PR/merge.
- This is rendered-page QA, not historical raw archive acquisition or completeness proof.
