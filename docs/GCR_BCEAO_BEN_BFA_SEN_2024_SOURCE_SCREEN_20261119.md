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
- Correction after opening the separate official Ministry of Economy and Finance/BCEAO PDF: Table 15 explicitly provides 2024 non-monetary-sector net acquisition of assets 342.6, net incurrence of liabilities 1,120.4, and balance -777.8 FCFA bn.
- Category rows: direct investment 34.6 / -122.6 / +157.2; portfolio -3.7 / 246.1 / -249.8; derivatives 0 / 0 / 0; other investment 311.7 / 996.9 / -685.1. The other-investment category row differs by 0.1 from asset-minus-liability; published category and total values preserved. Total asset-minus-liability = -777.8 exactly.
- Crucial scope limitation: Annex 1 explicitly says BCEAO analytical optic excludes central bank and other deposit-taking institutions' portfolio, derivatives and other-investment operations; monetary-sector operations are separately recorded in net external assets/liabilities. Thus Table 15 is not whole-country IMF gross A_NFA_T/L_NIL_T. It is a scoped non-monetary-sector benchmark only.

### Senegal (SEN)
- Page 27 (PDF page 44), Table 16, reports only the financial-account net balance and net category balances: total -2,139.9; direct investment -1,963.1; portfolio -395.9; derivatives 0.0; other investment +219.2 FCFA bn.
- The displayed table has one 2024 column per category, not separate asset and liability columns. Gross asset/liability split is NOT_DISCLOSED in this summary table; detailed annex/underlying source remains to be checked.

## Cross-source conclusion
- The 2024 Côte d'Ivoire report already provides both sides for the direct-investment component only (assets 138.1; liabilities 1,892.8 FCFA bn; net = -1,754.7), but not total financial-account gross legs.
- Across CIV/BEN/BFA/SEN, only CIV has a fully explicit numeric FDI asset and liability pair captured so far. BFA has a liability-side FDI component. BEN exposes portfolio stocks (not flows). SEN remains UNKNOWN at this stage.
- None of these partial observations can be promoted to total IMF A_NFA_T or L_NIL_T. They are annual, country-specific, and may differ in vintage, coverage and BCEAO analytical scope.

## Next action
1. Page-image/OCR audit the BFA and SEN financial-account tables and detailed annexes; check whether numerical gross asset and liability columns exist beyond searchable text.
2. Retrieve and screen 2024 detailed reports for GNB, MLI and TGO; keep NER on 2023 vintage separately.
3. For each country, construct a source-defined bridge across direct, portfolio, derivatives, other investment and reserve assets. No leg is inferred from net values.
4. Only after both aggregate legs, period, scale, currency, BPM basis and vintage reconcile may a country-period enter the alternate panel. Quarterly interpolation and aggregate admission remain prohibited.

## Correction log — page-image and full-source review
- The first text-only screening understated BFA evidence. The separate official ministry-hosted PDF was opened and Table 15 read in its indexed table structure; BFA has gross legs for the BCEAO non-monetary-sector optic, but not whole-country IMF coverage.
- SEN page image was inspected: it confirms Table 16 is net-only. BEN page 30 Table 14 is also net-only.
