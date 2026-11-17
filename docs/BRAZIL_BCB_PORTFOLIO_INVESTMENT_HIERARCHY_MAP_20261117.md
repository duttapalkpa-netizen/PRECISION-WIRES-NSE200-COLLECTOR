# Brazil BCB Portfolio Investment Hierarchy Map — 2026-11-17

## Objective
Build a taxonomy map from the official Banco Central do Brasil Open Data Portal topic catalogue and exact SGS dataset pages. This corrects the earlier narrow pilot framing: SGS 22905 is the top-level monthly portfolio-investment net series; 22906 is the asset-side net series; 22907/22908 are asset-side receipt/expense components; 22924 is liability-side net; 22925/22926 are liability-side receipt/expense components. These are different accounting levels and must not be treated as interchangeable.

## Official top-level hierarchy (BCB topic catalogue)
Official topic catalogue: https://dadosabertos.bcb.gov.br/pages/temas

| SGS code | Official Portuguese catalogue label | English catalogue interpretation | Hierarchy |
|---|---|---|---|
| 22905 | Investimentos em carteira - líquido | Portfolio investment - monthly - net | Total portfolio investment |
| 22906 | Investimentos em carteira - ativos - líquido | Portfolio investment assets - net | Assets |
| 22907 | Investimentos em carteira - ativos - receita | Portfolio investment assets - receipts/inflows | Assets |
| 22908 | Investimentos em carteira - ativos - despesa | Portfolio investment assets - expenses/outflows | Assets |
| 22909–22911 | Ações - ativos: líquido / venda / aquisição | Equity assets: net / sale / acquisition | Assets → equity |
| 22912–22914 | Fundos de investimento - ativos: líquido / venda / aquisição | Investment fund assets: net / sale / acquisition | Assets → fund shares |
| 22915–22917 | Títulos de dívida - ativos: líquido / venda / aquisição | Debt securities assets: net / sale / acquisition | Assets → debt |
| 22918–22920 | Títulos de dívida - ativos - curto prazo: líquido / venda / aquisição | Short-term debt securities assets | Assets → debt → short-term |
| 22921–22923 | Títulos de dívida - ativos - longo prazo: líquido / venda / aquisição | Long-term debt securities assets | Assets → debt → long-term |
| 22924 | Investimentos em carteira - passivos - líquido | Portfolio investment liabilities - net | Liabilities |
| 22925 | Investimentos em carteira - passivos - receita | Portfolio investment liabilities - receipts/inflows | Liabilities |
| 22926 | Investimentos em carteira - passivos - despesa | Portfolio investment liabilities - expenses/outflows | Liabilities |
| 22927–22929 | Ações - passivos: líquido / ingresso / saída | Equity liabilities: net / inflow / outflow | Liabilities → equity |
| 22930–22932 | Ações - no país: líquido / ingresso / saída | Domestic-market equity liabilities | Liabilities → equity → domestic |
| 22933–22935 | Ações - no exterior: líquido / ingresso / saída | Foreign-market equity liabilities | Liabilities → equity → abroad |
| 22936–22938 | Fundos de investimento - passivos: líquido / ingresso / saída | Investment-fund liabilities | Liabilities → fund shares |
| 22939–22941 | Títulos de dívida - passivos: líquido / ingresso / saída | Debt-security liabilities | Liabilities → debt |
| 22942–22944 | Títulos de dívida - passivos - curto prazo: líquido / ingresso / saída | Short-term debt-security liabilities | Liabilities → debt → short-term |
| 22945–22947 | Títulos de dívida - passivos - longo prazo: líquido / ingresso / saída | Long-term debt-security liabilities | Liabilities → debt → long-term |

The numeric ranges above are grouped by the topic catalogue's explicit consecutive code labels; exact English names for the child series are working translations of the Portuguese catalogue terms, not independent English metadata claims.

## Directly opened official dataset metadata
- 22905: https://opendata.bcb.gov.br/dataset/22905-portfolio-investment---monthly---net
  - BCB/Depec; monthly; USD million; coverage from 1995-01-01; ODbL.
- 22906: https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net
  - BCB/Depec; monthly; USD million; coverage from 1995-01-01; ODbL.
- 22907: https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows
  - BCB/Depec; monthly; USD million; coverage from 1995-01-01; ODbL.
- 22908: https://opendata.bcb.gov.br/dataset/22908-portfolio-investment---net-acquisition-of-financial-assets---monthly---outflows
  - BCB/Depec; monthly; USD million; coverage from 1995-01-01; ODbL.
- 22926: https://opendata.bcb.gov.br/dataset/22926-portfolio-investment---net-incurrence-of-liabilities---monthly---outflows
  - Previously verified in the prior pilot; monthly; USD million; coverage from 1995-01-01; ODbL.

The BCB topic catalogue also lists liability net (22924), liability receipts (22925), and instrument-level liability series (22927 onward). The exact English resource metadata and payloads for these child series have not all been independently opened in this audit.

## Important semantic correction
The Portuguese catalogue uses:
- receita = receipts / inflows
- despesa = expenses / outflows
- aquisição = acquisition
- venda = sale
- ingresso = inflow / entry
- saída = outflow / exit

Therefore 22907/22908 should be understood as asset-side receipt/expense series, not as equity-market foreign investor net flows. Similarly 22925/22926 are liability-side receipt/expense series. Do not assume signs from English labels alone; confirm BCB time-series methodology and compare net/receipt/expense observations only after raw payload capture.

## Research implications
1. 22905 is the most direct top-level aggregate series for total portfolio investment net.
2. 22906 and 22924 are separate asset and liability net series; do not simply add/subtract them without BOP sign convention.
3. 22907/22908 and 22925/22926 are components, not substitutes for the aggregate net series.
4. The equity/fund/debt breakdown (22909 onward) offers a much more useful route to distinguish risk-on equity allocation from debt-security flows, but instrument-level payloads and accounting identities are not yet verified.
5. Domestic versus foreign market split appears for equity liabilities (22930–22935). Do not treat domestic-market equity liability flows as total portfolio flows.
6. All listed series are monthly macro context, not 1–3 day trading triggers.

## QA and acceptance status
| Gate | Status |
|---|---|
| Official topic hierarchy located | PASS |
| Top-level total series 22905 identified | PASS |
| Asset/liability net and component code families mapped | PASS (catalogue labels) |
| Instrument-level equity/fund/debt hierarchy mapped | PASS (catalogue labels) |
| Exact child dataset English metadata and resource endpoints | PARTIAL |
| Exact BOP sign and series arithmetic | UNKNOWN / NOT_DONE |
| Raw payloads and immutable SHA-256 manifests | NOT_DONE |
| Country-period observation QA | NOT_DONE |
| Brazil pilot acceptance | NOT_ACCEPTED |
| EM-wide panel | NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## Next bounded action
Prioritize exact raw capture and identity reconciliation for 22905, 22906, 22924, 22907, 22908, 22925 and 22926 over attempting every child series. Once the aggregates reconcile, add the smallest instrument split needed for equity-vs-debt allocation. Obtain the exact BCB methodological note and verify accounting signs before calculation. Preserve all raw observations, source vintages and response manifests.

## Hard invariants
Research-only. No synthetic data, guessed values, timestamps, or hashes. ₹0 spend. UNKNOWN never PASS. Do not alter Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate or production workflows.
