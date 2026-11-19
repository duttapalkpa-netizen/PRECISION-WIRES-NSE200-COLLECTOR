# Burkina Faso 2024 gross asset/liability source extraction — scoped partial result

## Decision
**2024 non-monetary-sector gross asset/liability extraction PASS; whole-country IMF A_NFA_T/L_NIL_T mapping BLOCKED.** The official Ministry of Economy and Finance/BCEAO annual report Table 15 explicitly separates net acquisition of financial assets from net incurrence of liabilities for the BCEAO analytical optic. The same report explicitly states that this optic excludes central bank and other deposit-taking institution portfolio, derivatives and other-investment operations. Therefore this table is not the complete whole-economy IMF BOP financial account.

## Official source
- PDF: https://www.finances.gov.bf/fileadmin/user_upload/storage/fichiers/Rapport_BdP_2024_au_10-12-2025_TS_AG_13h00__2_.pdf
- Publication: annual 2024 report, November 2025; MBP6 basis.
- Table 15, printed page 36 (PDF lines 1521–1582 in official indexed extraction).
- Table columns explicitly: 2023 and 2024, each with net acquisition of financial assets, net incurrence of liabilities, and balance.

## 2024 values (FCFA billion)
| Category | Assets | Liabilities | Balance | Check |
|---|---:|---:|---:|---|
| Direct investment | 34.6 | -122.6 | +157.2 | exact |
| Portfolio investment | -3.7 | 246.1 | -249.8 | exact |
| Financial derivatives | 0.0 | 0.0 | 0.0 | exact |
| Other investment | 311.7 | 996.9 | -685.1 | 311.7−996.9 = −685.2; published balance differs by +0.1 |
| TOTAL | 342.6 | 1,120.4 | -777.8 | exact |

## Scope restriction
The report's Annex 1 states that the BCEAO analytical optic excludes the central bank and other deposit-taking institutions' portfolio investment, financial derivatives and other investment from the financial account; these monetary-sector operations are instead recorded in net external assets/liabilities and form part of the overall BOP balance. The table is therefore a non-monetary sector scope, not full national gross legs. Do not map the 342.6 and 1,120.4 totals to whole-country IMF A_NFA_T/L_NIL_T.

## QA and admission
- Row checks: direct, portfolio and derivatives exact; other investment rounding residual +0.1; total exact.
- Component assets sum = 342.6 exact.
- Component liabilities sum = 1,120.4 exact.
- Published category balances sum = -777.7 versus published total -777.8 (0.1 rounding residual). Preserve source totals.
- Full-country gross asset/liability mapping: BLOCKED due excluded monetary-sector scope and unresolved table-vs-IMF reconciliation.
- Annual 2024 only; no quarterly imputation, no FX conversion, no production/backtest admission.

## Next action
Obtain the monetary-sector asset/liability transaction flows excluded by the BCEAO analytical optic and reconcile them to IMF's whole-economy financial account. Then compare the full country total with the IMF vintage, scale, sign convention and quarter/year bridge.