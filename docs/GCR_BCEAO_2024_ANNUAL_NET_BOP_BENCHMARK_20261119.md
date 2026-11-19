# BCEAO 2024 annual BOP benchmark extraction — GCR (2026-11-19)

## Decision
**Annual net benchmark extraction: PARTIAL PASS (8/8 country rows captured); IMF A_NFA_T/L_NIL_T reconciliation: BLOCKED.** The official BCEAO Annual Report 2024 Annexes A23–A27 contain separate national Balance of Payments tables for all eight UEMOA members. The extracted 2024 (*) financial-account total and component balances are annual net figures in billions of FCFA. The asterisk denotes estimate in the source tables. This is useful source evidence but it does not separately disclose net acquisition of financial assets and net incurrence of liabilities.

## Source
- Official BCEAO-hosted annual report PDF: https://cofeb.bceao.int/sites/default/files/2025-07/Rapport_Annuel_2024_BCEAO_INTERACTIF_compressed.pdf
- The PDF contents index identifies Balance of Payments in Annexes A23–A27; country tables appear in the extracted text at PDF lines 8431 and 8520.
- Table headings: 2022, 2023, 2024 (*); unit: billions of FCFA.
- The source footnotes mark 2024 (*) as an estimate.
- Publicly indexed PDF text was inspected. The original PDF bytes have NOT yet been archived to this repository; no raw-byte SHA-256 is claimed.

## 2024 country observations (FCFA billion; estimated)
| Code | Country | Financial-account net balance | Direct investment net | Portfolio investment net | Derivatives net | Other investment net | Sum components | Residual (reported minus sum) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| BEN | Benin | -674.7 | -292.7 | -245.1 | 0.0 | -136.9 | -674.7 | 0.0 |
| BFA | Burkina Faso | -793.6 | -27.8 | -281.2 | 0.0 | -484.5 | -793.5 | -0.1 |
| CIV | Côte d'Ivoire | -4,085.3 | -1,964.0 | -895.1 | -3.1 | -1,223.0 | -4,085.2 | -0.1 |
| GNB | Guinea-Bissau | -55.3 | -15.9 | -59.8 | 0.0 | 20.4 | -55.3 | 0.0 |
| MLI | Mali | -1,089.0 | -492.3 | -262.3 | 0.0 | -334.4 | -1,089.0 | 0.0 |
| NER | Niger | -309.8 | -311.8 | -67.1 | 0.0 | 69.1 | -309.8 | 0.0 |
| SEN | Senegal | -2,665.0 | -1,193.5 | -708.9 | 0.0 | -762.6 | -2,665.0 | 0.0 |
| TGO | Togo | 71.7 | -95.3 | 56.6 | 0.0 | 110.3 | 71.6 | +0.1 |

## QA
- Eight countries have a source-reported financial-account net balance and four named component net balances.
- Component-sum residuals: 5/8 exactly zero at one decimal; 3/8 differ by 0.1 FCFA billion (BFA -0.1, CIV -0.1, TGO +0.1). This is consistent with one-decimal component presentation/rounding, but do not overwrite reported totals.
- All 8 are 2024 estimates, not final actual observations.
- The dataset explicitly marks both IMF leg mappings NOT_SEPARATELY_DISCLOSED.
- The annual total or its components must NOT be mapped directly to A_NFA_T or L_NIL_T. No sign conversion or inferred gross legs is authorized.
- Annual data cannot fill missing quarterly observations. No interpolation, forward-fill, currency conversion, proxy aggregation, or production/backtest admission.

## Next source requirement
For each country, acquire the detailed national BOP table or underlying compilation dataset with separate asset and liability transactions (or detailed BPM6 functional-category asset/liability columns). Then validate annual 2024 vintage against the IMF quarterly series and source revisions. Keep 2024 estimates separate from final releases.

## Status
- Official PDF text source verified: PASS.
- Eight-country annual net extraction: PARTIAL PASS.
- Arithmetic cross-check: 5 exact, 3 rounding residuals of 0.1 FCFA bn.
- Raw PDF byte archive/hash: NOT_DONE.
- IMF A_NFA_T and L_NIL_T leg mapping: BLOCKED.
- Quarterly repair / EMDE aggregate admission: BLOCKED / NOT_AUTHORIZED.
- Spend ₹0; UNKNOWN is not PASS.
