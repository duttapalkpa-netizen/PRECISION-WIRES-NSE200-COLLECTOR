# BCB SGS 22942 Source-Level Compilation Provenance Investigation — 2026-11-18

## Objective
Determine whether official BCB documentation identifies the underlying reporting systems and records used to compile SGS 22942 (portfolio investment liabilities — debt securities issued in the domestic market — monthly — net), without repeating the prior series-vintage and revision-policy audits.

## New official evidence

### 1. BCB BPM6 methodological note (November 2014)
Official source: https://www.bcb.gov.br/content/statistics/methodologicalnotes_docs/BPM6/nm1bpm6i.pdf

The note states:
- The major source of Brazilian BOP statistics is financial transactions recorded in the BCB Exchange System (Sistema Câmbio); the BOP is mainly compiled from individual transaction microdata (ITRS).
- Other monthly BOP compilation sources include MDIC trade data, COSIF, BCB international reserves, RDE foreign-capital modules, CBE, Censo and supplementary questionnaires from public/private institutions.
- It classifies portfolio investment liabilities as a BPM6 financial-account component, but does not name SGS 22942 or map a specific source system to that series.

Evidence location: official PDF lines 32–41 and 48–55 (web audit references turn489488view2 / turn658616view0 context).

### 2. BCB Banking Report 2020 — non-resident portfolio flows
Official source: https://www.bcb.gov.br/content/publications/bankingreport/2020/BAR_2020.pdf

The report's portfolio-investment box states that the data sources for portfolio investment flows are Sistema Câmbio, portfolio-investment series SGS 22924, trade-balance series SGS 11047 and financial-balance series SGS 11050. It separately states that stock data sources are CBLC and Selic databases; B3 data were used for non-resident equity purchases.
This is direct evidence about a broader non-resident domestic-market portfolio-flow measure, not an explicit input lineage declaration for SGS 22942. SGS 22924 is a broader portfolio-liabilities series and must not be silently substituted for the debt-only domestic-market series.

Evidence location: official PDF lines 7626–7647 (turn658616view0).

### 3. BCB Banking Report 2021 — securities statistics data sources
Official source: https://www.bcb.gov.br/content/publications/bankingreport/2021/BAR_2021.pdf

The report says securities statistics compiled by issuers use domestic issuance liability positions registered in custody central systems B3 and Selic, or BCB database calculations for certain bank deposit certificates not registered at B3 but captured in bank balance sheets. For international issuance it identifies RDE-ROF. This section describes securities positions/statistics by issuer and holder, not the monthly transaction-flow construction of SGS 22942.
Therefore B3/Selic and bank balance-sheet inputs are relevant institutional securities-statistics lineage, but their direct use in SGS 22942 monthly net flow is NOT_PROVEN.

Evidence location: official PDF lines 3010–3024 (turn658616view1).

### 4. SGS 22942 official catalogue
Official source: https://opendata.bcb.gov.br/dataset/22942-portfolio-investment---debt-securities----issued-in-the-domestic-market---monthly---net

The catalogue identifies BCB/Depec as publisher/maintainer, monthly frequency, USD million, and the series concept. It does not disclose the primary reporting institution, input records, transaction-level fields, or a series-specific compilation formula.

## Provenance decision matrix

| Lineage element | Status | Reason |
|---|---|---|
| Statistical compiler / publisher (BCB/Depec) | PASS | Explicit SGS catalogue metadata |
| BPM6 financial-account classification | PASS | BCB methodology note |
| General BOP transaction source system (Sistema Câmbio / ITRS) | PASS at BOP-wide level | Explicit BCB methodology note |
| Broader domestic non-resident portfolio flow source list (Sistema Câmbio, SGS 22924, SGS 11047, SGS 11050) | PASS at broader-measure level | Explicit BCB Banking Report 2020 |
| Domestic securities-position source systems (B3, Selic, selected bank balance-sheet data) | PASS at positions-statistics level | Explicit BCB Banking Report 2021 |
| Direct mapping of those inputs to SGS 22942 monthly flow | UNKNOWN | No inspected official source explicitly maps the inputs to SGS 22942 |
| SGS 22942 transaction-level reporting entities and records | UNKNOWN | Not disclosed in inspected official materials |
| SGS 22942 monthly net-flow calculation / sign formula | UNKNOWN | Not disclosed in inspected official materials |
| Source-vintage/revision linkage to Feb-2026 +USD 203.70779636m discrepancy | UNKNOWN | No series-specific revision record or original March vintage established |

## Interpretation boundary
1. Do not equate BOP-wide Sistema Câmbio microdata with proof that every SGS 22942 instrument-level observation is compiled exclusively or directly from Sistema Câmbio.
2. Do not equate B3/Selic securities positions with monthly transactions or net flow.
3. Do not treat SGS 22924 as a component identity or replacement for SGS 22942.
4. The 2020 report is useful evidence of broader portfolio-flow compilation, but its scope and series references do not identify SGS 22942.
5. No causal explanation for the February-2026 difference is established.

## Final disposition
- General BCB BOP compilation lineage: PARTIAL (official sources identified).
- SGS 22942-specific underlying source mapping: UNKNOWN / NOT_PROVEN.
- February-2026 revision cause/date: UNKNOWN / NOT_PROVEN.
- Original March-2026 Table 10 workbook vintage: NOT_PROVEN.
- SGS 22942 Feb-2026 reconciliation: BLOCKED.
- Brazil pilot acceptance: NOT_ACCEPTED.
- Production integration: NOT_AUTHORIZED.

## Next action
Do not repeat the generic BOP methodology search or securities-position source review. The only meaningful next evidence would be an official BCB series-specific technical note, internal-public compilation description, metadata attachment, or immutable contemporaneous revision/source record explicitly linking SGS 22942 to transaction inputs. If none is publicly available, preserve the limitation and keep the series out of pilot admission.

## Protected invariants
Research-only; ₹0 spend; official/free sources only; no synthetic values, fabricated timestamps, guessed source mappings, raw archive overwrites or unsupported attribution. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate and production workflows unchanged.
