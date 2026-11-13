# CDSL Daily FPI 11-Nov-2026 — FX and Subtotal Cross-Check

## Scope and source
- Official CDSL daily report: https://www.cdslindia.com/eservices/publications/fiidaily
- Reporting date: 11-NOV-2026.
- Displayed INR/USD conversion rate: 1 USD = INR 93.8579.
- This validates rendered-table arithmetic only; no raw archive bytes or SHA-256 are claimed.

## USD category reconciliation (USD million)
| Category | USD net |
|---|---:|
| Equity (including primary/others) | 741.4773 |
| Debt-General | 31.4614 |
| Debt-VRR | 14.5486 |
| Debt-FAR | -125.1338 |
| Hybrid | -1.3552 |
| Mutual Funds | 6.2136 |
| AIF | 0.0000 |
| Component sum | 667.2119 |
| CDSL displayed total | 667.2120 |
| Difference | -0.0001 |

Result: PASS at displayed precision; 0.0001 USD million difference is consistent with category rounding to four decimals.

## Cross-currency total check
- CDSL displayed USD total: 667.212 million.
- CDSL displayed conversion rate: INR 93.8579 per USD.
- Implied INR crore = 667.212 × 93.8579 ÷ 10 = INR 6,262.31171748 crore.
- CDSL displayed INR total: INR 6,262.31 crore.
- Difference before rounding: INR 0.00171748 crore; rounded to two decimals, implied value is INR 6,262.31 crore.
- Result: PASS at displayed precision.

## Mutual Fund internal subtotal check (INR crore)
- Equity schemes: purchases 4.05, sales 4.53, net -0.48.
- Debt schemes: purchases 60.00, sales 0.00, net 60.00.
- Hybrid schemes: purchases 0.01, sales 0.00, net 0.01.
- Solution-oriented: purchases 0.00, sales 0.00, net 0.00.
- Other schemes: purchases 1.05, sales 2.26, net -1.21.
- Sum purchases = 65.11; sum sales = 6.79; sum net = 58.32.
- CDSL Mutual Funds subtotal = purchases 65.11, sales 6.79, net 58.32.
- Result: PASS.

## Interpretation controls
- USD component discrepancy is a rounding residual, not a data error; preserve displayed source precision and do not force-adjust a category.
- Conversion check is performed only on displayed aggregate USD total and displayed rate; it is not an independent FX reconstruction for every underlying transaction.
- CDSL confirmed custodian/depository daily data remains distinct from NSE provisional T-day data.
- This is a supplemental QA to the 11-Nov daily extraction; do not count it as new historical dates or archive coverage.
- Research-only; no production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics, or Hard Gate changed. No spend, no paid source, no external contact, no PR/merge.
