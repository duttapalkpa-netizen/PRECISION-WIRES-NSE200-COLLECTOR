# Côte d'Ivoire 2024 BOP — partial gross FDI-leg extraction (GCR)

## Decision
**Source-byte archive PASS. Direct-investment gross-leg extraction PARTIAL PASS. Total IMF A_NFA_T / L_NIL_T reconciliation BLOCKED.** The official national 2024 report gives the gross FDI asset-side and liability-side flows separately, but does not provide an aggregate gross financial-account asset and liability total in the extracted account tables. Portfolio and other investment are published as net balances. Do not promote the FDI-only legs into the aggregate IMF P_F entries.

## Official source and archive
- BCEAO official report PDF: https://www.bceao.int/sites/default/files/2026-09/Balance_des_Paiements_et_Position_Ext%C3%A9rieure_Globale_2024-C%C3%B4te_d-Ivoire.pdf
- Publication page: https://www.bceao.int/fr/publications/balance-des-paiements-et-position-exterieure-globale-de-la-cote-divoire-2024
- PDF title: *Rapport de la balance des paiements de la Côte d'Ivoire au titre de l'année 2024*.
- PDF pages: 63; relevant printed pages 24–25 (PDF pages 27–28).
- Workflow run: 44495255971, SUCCESS.
- Artifact ID: 14515150693; artifact name `bceao-cote-divoire-bop-2024-raw`; ZIP size 1,851,216 bytes; artifact digest SHA-256 `6ad9941564fbed0c144e6d65e7065acbef5c6511df19fb7cd5c59ce5f9659baa`; retention through 2027-02-17.
- Raw PDF HTTP 200, application/pdf, retrieved UTC `2026-11-19T09:18:58.398586+00:00`, 3,596,808 bytes, SHA-256 `99aee45e2f75464e85b9b319c9acd93bfd706779119e8c6bfac8db0f5a1a2f28`, magic `%PDF-1.7`.
- Script commit `20b3637ecc7169558df15456e5cd204d45f7dbb0`; workflow commit `247b88e5c06bd6f91eaa2eca8f0c0c8a86991a2c`; collector paths-ignore guard commit `f82444e347be43490c643dd7894066020f572ce6`; trigger commit `ac0b8977db9fc48a735793d14e64c206d15ff673`.

## Extracted 2024 source values (FCFA billion)
The report's Table 13 gives:
- Direct investment net balance: -1,754.7.
- Portfolio investment net: -1,055.5.
- Financial derivatives net: +0.1.
- Other investment net: -1,233.0.
- Total financial account net balance: -4,043.1.

The narrative on printed pages 24–25 explicitly states:
- Net acquisition of financial assets (outward direct investment): 138.1.
- Net incurrence of liabilities (inward direct investment): 1,892.8.
- Arithmetic: 138.1 - 1,892.8 = -1,754.7; exact match to reported direct-investment net balance.
- Inward direct-investment liabilities: debt instruments 1,176.9, reinvested earnings 426.3 and equity other than reinvested earnings 289.6; sum 1,892.8.
- Outward asset acquisitions: equity/fund shares 92.7 and debt instruments 45.4; sum 138.1.

## Scope and blockers
- This is a **direct-investment component only**, not the whole financial account.
- The report publishes portfolio, derivatives and other investment as net positions only; it also notes the BCEAO presentation excludes banking-system flows for certain categories (portfolio, derivatives, other investment and reserve assets).
- Therefore the 138.1 and 1,892.8 cannot be used as IMF total A_NFA_T and L_NIL_T.
- No full gross asset/liability reconciliation to IMF quarterly series has been made; no annual-to-quarterly expansion, sign inference, FX conversion or synthetic data.
- The report does not mark the 2024 row as estimated in the inspected table; estimate_flag=NOT_INDICATED, not assumed final/provisional.
- This extraction is a source-level partial benchmark and must remain outside the production GCR aggregate and backtests.

## QA
- Direct-investment component arithmetic: 138.1 - 1,892.8 = -1,754.7, exact PASS.
- Liability subcomponents: 1,176.9 + 426.3 + 289.6 = 1,892.8, exact PASS.
- Asset subcomponents: 92.7 + 45.4 = 138.1, exact PASS.
- Total financial account net arithmetic: -1,754.7 - 1,055.5 + 0.1 - 1,233.0 = -4,043.1, exact PASS.
- IMF aggregate asset/liability mapping: BLOCKED / NOT_MAPPED.

## Next action
Acquire detailed 2024 reports for the other seven UEMOA zero-data members and test whether they publish separate gross asset/liability flows for direct investment only or for all functional categories. In parallel, identify a source that separately publishes portfolio, derivatives and other-investment asset/liability transactions. No aggregate promotion until all categories and coverage reconcile.