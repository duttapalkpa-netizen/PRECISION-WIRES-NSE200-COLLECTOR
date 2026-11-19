# BCEAO BEN/BFA/SEN 2024 national BOP source archive and structure screen — 2026-11-19

## Decision
**Raw source acquisition PASS (3/3). Numerical gross-leg extraction: PARTIAL / UNKNOWN by country. Aggregate IMF A_NFA_T and L_NIL_T mapping remains BLOCKED.** These are source-screening results, not panel repair.

## Archive receipt
- Focused workflow run: `44495561543`, SUCCESS.
- Artifact ID: `14514373729`; name `bceao-ben-bfa-sen-bop-2024-raw`; ZIP size 17,363,969 bytes; artifact digest SHA-256 `6a670ead73df28b6766aef0c0e5004f795867903dc9bdb3ad59b248c0921518d`; expires 2027-02-17.
- Script commit `d0329a779aa002f516ce973bffb3011b889b491a`; workflow commit `1939e57aad83c5cddd9cd6ba088fdfcb801c4bd2`; production collector pre-guard commit `afa8fbcf080ad2f6e5daa6af192013f2a9f2f3d7`; trigger commit `b972bc997bc8a757384c03b2eb2eb836b4ab4d99`.
- All three original PDF files were downloaded with HTTP 200 / application/pdf and independently re-hashed after artifact download.

| Country | PDF bytes | Raw SHA-256 | PDF pages |
|---|---:|---|---:|
| BEN | 5,606,445 | `15af93618aafee0446eef191ab9e208dcc1c807e3507eadf306c1ce6dbc92193` | 78 |
| BFA | 6,707,349 | `6a4b7149d5abb13d4aac7600cc13a7c0b157cb1d6aa06f8fed41e2b12e33a8ba` | 91 |
| SEN | 6,055,592 | `ee8e7794d2ad85f337d6c1536edcda973f3f7f322cb3b131e332fdb38a133395` | 66 |

## Initial structure screen
### Benin (BEN)
- The report's financial-account table gives only net category balances; 2024 net direct investment inflow is FCFA 232,015.8 million; portfolio net inflow FCFA 130,102.7 million.
- The report separately shows portfolio investment positions (not transactions): non-resident holdings of Beninese securities (liabilities stock) FCFA 209,811.7 million at end-2024 and residents' foreign-security holdings (assets stock) FCFA 79,709.0 million. These are stocks, not net transaction legs and must not be substituted into IMF P_F transaction observations.
- Numerical gross transaction asset/liability split for total financial account not found in the initial text extraction; detailed page-image review remains NOT_DONE.

### Burkina Faso (BFA)
- The report gives total net financial-account capital inflows FCFA 777.8 billion and net FDI outflow FCFA 157.2 billion.
- It explicitly reports a 2024 decrease in net liabilities on inward FDI of FCFA 122.6 billion (debt instruments -83.0; equity -43.4). This is a liability-side FDI component only; the matching outward-asset transaction amount and total gross financial-account legs were not established in the initial text extraction.
- Do not infer the missing asset leg by subtracting from net FDI or net financial-account values without a complete source-defined bridge.

### Senegal (SEN)
- The report's financial-account narrative and summary provide net external financing / net category information; the initial searchable text did not expose a numerical aggregate split into net acquisition of financial assets and net incurrence of liabilities.
- Mark gross-leg extraction UNKNOWN pending inspection of the full table/page images and any detailed annex. No negative conclusion is inferred from missing searchable text.

## Cross-source conclusion
- The 2024 Côte d'Ivoire report already provides both sides for the direct-investment component only (assets 138.1; liabilities 1,892.8 FCFA bn; net = -1,754.7), but not total financial-account gross legs.
- Across CIV/BEN/BFA/SEN, only CIV has a fully explicit numeric FDI asset and liability pair captured so far. BFA has a liability-side FDI component. BEN exposes portfolio stocks (not flows). SEN remains UNKNOWN at this stage.
- None of these partial observations can be promoted to total IMF A_NFA_T or L_NIL_T. They are annual, country-specific, and may differ in vintage, coverage and BCEAO analytical scope.

## Next action
1. Page-image/OCR audit the BFA and SEN financial-account tables and detailed annexes; check whether numerical gross asset and liability columns exist beyond searchable text.
2. Retrieve and screen 2024 detailed reports for GNB, MLI and TGO; keep NER on 2023 vintage separately.
3. For each country, construct a source-defined bridge across direct, portfolio, derivatives, other investment and reserve assets. No leg is inferred from net values.
4. Only after both aggregate legs, period, scale, currency, BPM basis and vintage reconcile may a country-period enter the alternate panel. Quarterly interpolation and aggregate admission remain prohibited.