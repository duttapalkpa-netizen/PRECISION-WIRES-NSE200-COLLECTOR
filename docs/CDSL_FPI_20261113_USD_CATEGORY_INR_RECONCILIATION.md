# CDSL FPI Daily 13-Nov-2026 — USD Category and INR Conversion Reconciliation

## Official source and scope
- Official CDSL daily report: https://www.cdslindia.com/eservices/publications/fiidaily
- Displayed report date: 13-NOV-2026.
- Source rendered HTML lines include cash category subtotals, USD million values, conversion rate and methodology note.
- CDSL states its daily conversion uses RBI reference rate prevailing on the trading day (or preceding working day if a bank holiday); aggregate discrepancies can arise from rounding.
- This is a rendered-page arithmetic reconciliation, not raw archive acquisition.

## USD net investment category reconciliation (USD million)
| Category | CDSL subtotal USD Mn |
|---|---:|
| Equity | 949.0535 |
| Debt-General | 74.3113 |
| Debt-VRR | -7.8665 |
| Debt-FAR | 22.0797 |
| Hybrid | -0.1461 |
| Mutual Funds | -0.0171 |
| AIF | 0.0000 |
| **Component sum** | **1,037.4148** |
| **CDSL displayed total** | **1,037.4150** |
| **Difference** | **-0.0002** |

Result: PASS at displayed precision. Residual 0.0002 USD million is consistent with category values rounded to four decimals. Preserve the source values; do not force-adjust a category.

## INR-to-USD aggregate conversion check
- Displayed USD net total: 1,037.415 million.
- Displayed conversion rate: INR 93.765 per USD.
- Implied INR crore = 1,037.415 × 93.765 ÷ 10 = INR 9,727.3217475 crore.
- CDSL displayed INR net total: INR 9,727.32 crore.
- Implied total rounded to two decimals: INR 9,727.32 crore.
- Result: PASS at displayed precision.

## Equity subtotal USD detail check
- Stock Exchange USD net: 947.4825.
- Primary market & others USD net: 1.5709.
- Sum of displayed components: 949.0534.
- CDSL Equity subtotal: 949.0535.
- Difference: -0.0001 USD million, consistent with component-level rounding.

## INR category and gross reconciliation
- Purchases: INR 23,314.45 crore.
- Sales: INR 13,587.13 crore.
- Net: INR 9,727.32 crore.
- Purchases minus sales equals net exactly at displayed precision.
- Category net INR subtotals sum exactly to INR 9,727.32 crore.

## QA disposition
- PASS: USD category subtotal sum agrees with displayed USD total within 0.0002 USD million rounding residual.
- PASS: aggregate USD-to-INR conversion rounds to the displayed INR total.
- PASS: Equity Stock Exchange plus Primary & Others subtotal agrees within 0.0001 USD million rounding residual.
- PASS: gross INR purchases less sales and category INR net totals reconcile exactly.
- Do not label tiny displayed precision residuals as errors or rewrite source values.
- CDSL confirmed custodian-reported series remains separate from exchange provisional T-day FII/FPI data.
- Report date is the custodian reporting date; underlying trades are on/up to previous trading day(s), per CDSL note.
- No synthetic data, no paid source, no spend, no external contact.
- Research-only; production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics and Hard Gate unchanged; no PR/merge.
- Raw daily archive bytes were not downloaded; no SHA-256 or historical completeness claim.
