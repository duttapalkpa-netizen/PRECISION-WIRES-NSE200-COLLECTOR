# BCB SGS 22942 — Revision Policy Applicability & Attribution Boundary
Date: 2026-11-18
Scope: determine what BCB's official revision policy can and cannot establish about February-2026 SGS 22942 (domestic-market portfolio debt securities, USD million).

## Executive decision
BCB's published revision policy confirms that external-sector statistics may undergo ordinary short-term revisions and that these can incorporate new information, revised estimates, corrections to submitted data or compilation, and data-quality validation. It also provides for ordinary annual revisions and extraordinary revisions. This makes a later change to an observation procedurally possible, but does not identify which mechanism changed February-2026 SGS 22942 or when it changed.

**Attribution remains UNKNOWN / NOT_PROVEN.** The policy is a general framework, not a series-specific revision log.

## Official policy evidence
Source: BCB, *Política de revisão das estatísticas econômicas oficiais compiladas pelo DSTAT*, 3rd edition, June 2023:
https://www.bcb.gov.br/content/estatisticas/Documents/notas_metodologicas/Politica_de_Revisoes_de_Estatisticas.pdf

- Lines 125–133 define revisions as changes to initially published values and list possible reasons: source/compilation error correction, missing information becoming available, higher-frequency/lagged data, consistency across sources, new sources, estimate improvement, regulatory changes, and methodology improvements.
- Lines 159–170 state statistics are generally revised at their publication periodicity; annual, methodological and extraordinary revisions may also occur. Minor routine monthly revisions need not receive detailed explanation; other revisions are described in accompanying release text.
- Lines 182–218 state short-term ordinary revisions arise from routine compilation and commonly include new information unavailable at initial release, revised estimates, correction of reported or compilation errors, and quality validation. Minor/routine incorporations may not be detailed.
- Lines 220–250 describe annual revisions after definitive reference-year information and validated data become available.
- Lines 258–275 describe methodological and extraordinary revisions; extraordinary revisions arise from error or extraordinary data availability and are to be disclosed in the release accompanying the statistic.
- Table lines 432–437 show the policy's Balanço de Pagamentos schedule as monthly publication, short-term revisions monthly (up to 1 month lag), annual revision up to 23 months, with annual revision months July and November in the 2023 policy edition. This policy edition must not be assumed to override the 4th-edition September-2026 schedule without checking the later policy text.

## Official September-2026 BCB review disclosure
Source: BCB external-sector statistics press note, 28-Sep-2026:
https://bcb.gov.br/estatisticas/estatisticassetorexterno

The note states the 4th edition (September 2026) unified ordinary annual revision of balance of payments and IIP in September, covering definitive 2025 statistics and revisions of current-year 2026 estimates. It lists sources and impacts:
- Censo: direct-investment earnings and associated current-account/financial-account entries; some portfolio-investment reclassification linked to fund ownership.
- CBE: overseas account movements, export receipts/use of funds, direct-investment earnings and external asset positions.
- SCE-IED/SCE-Crédito: foreign-capital declarations, intercompany debt amortization, and external-debt disbursement/interest/principal paid via overseas accounts.
- Extraordinary 2023 and 2025 revisions for international corporate restructurings, with no effective financial cash flow.

Crucially, the published explanation does not identify SGS 22942, February-2026 domestic debt securities liabilities, or a USD 203.70779636m change. The listed 2026 revisions described in section 3.3 concern January–July balance-of-payments current-account estimates, direct-investment profits and related reinvested earnings; they do not attribute the SGS 22942 observation.

## Series definition
BCB Open Data catalog:
https://opendata.bcb.gov.br/dataset/22942-portfolio-investment---debt-securities----issued-in-the-domestic-market---monthly---net
- Series 22942: Portfolio investment — Debt securities — issued in the domestic market — monthly — net.
- Unit: million US dollars; monthly frequency; source BCB/Department of Economics.
- The catalog's metadata update timestamp is not a revision log or observation vintage.

## Quantitative evidence already verified (do not rerun)
- March-labelled captured Table 10 row 24, February 2026: USD 2,579.492203640002m.
- Contemporaneous 27-Mar-2026 BCB release rounded debt securities to USD 2.6bn.
- 17-Nov archive and live SGS API: February 2026 = USD 2,783.2m.
- Difference (live/current SGS minus captured March-labelled Table 10) = +USD 203.707796359998m.
- 15 SGS series live-vs-archive audit: 5,715/5,715 exact matches, zero changed observations; collector integrity PASS.
- Captured March-labelled workbook's HTTP Last-Modified is 18-Oct-2026, so it is not proven to be the original March release vintage.

## Attribution decision matrix
| Candidate explanation | Policy permits generally? | Series-specific evidence for 22942 Feb-2026? | Decision |
|---|---|---|---|
| Routine monthly new information | Yes | None located | UNKNOWN |
| Revised estimate | Yes | None located | UNKNOWN |
| Correction to source submission or compilation | Yes | None located | UNKNOWN |
| Quality-validation correction | Yes | None located | UNKNOWN |
| September-2026 annual review sources | Yes, annual review occurred | Published named impacts do not identify this series/month | NOT_ATTRIBUTED |
| Extraordinary revision | Yes, if error/new data | No 22942-specific disclosure located | NOT_PROVEN |
| Methodological/classification change | Yes, policy category exists | No series-specific methodology notice located | NOT_PROVEN |

## Acceptance status
- General revision-policy applicability: PASS.
- Official September-2026 review scope inspected: PASS.
- Series-specific attribution to 22942 Feb-2026: UNKNOWN / NOT_PROVEN.
- Exact original March XLSX vintage: NOT_PROVEN.
- Exact revision date: UNKNOWN.
- Brazil pilot: NOT_ACCEPTED.
- Production integration: NOT_AUTHORIZED.

## Next action
Do not repeat the live API comparison, accounting identity checks, or general policy search. The remaining high-value evidence is a series-specific BCB source/compilation record or exact original March-2026 Table 10 XLSX (or official pre-18-Oct-2026 version history). If unavailable, keep the observation excluded from Brazil pilot acceptance.

## Invariants
₹0; official/free sources only; no synthetic values or invented timestamps; no raw archive overwrite. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, hard gates and production workflows unchanged.
