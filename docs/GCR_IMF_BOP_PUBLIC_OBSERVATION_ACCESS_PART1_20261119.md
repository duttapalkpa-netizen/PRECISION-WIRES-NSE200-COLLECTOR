# IMF BOP Public Observation Access — Brazil/India Pilot (2026-11-19)

## Outcome

<badge>PASS — public observation extraction and independent reconciliation</badge>

The IMF SDMX 3.0 BOP observation endpoint was accessed without an API key, login, session cookie, or paid service. The official BOP dataset is published at annual and quarterly frequency; IMF's API page documents SDMX 2.1 and SDMX 3.0 access. The API documentation's Swagger explorer requires a beta portal account, but that is not a prerequisite for the tested public SDMX 3.0 metadata and observation URLs.

- Dataset: `IMF.STA:BOP`
- Dataflow: `IMF.STA:BOP(21.0.0)`
- DSD: `IMF.STA:DSD_BOP(24.0.0)`
- DSD SHA-256: `1541c0e65af5801acb86767a183a124537aa4b6a04d2a4e528c23d73d4b2019b`
- Dimension order: `COUNTRY.BOP_ACCOUNTING_ENTRY.INDICATOR.UNIT.FREQUENCY`

## Exact series and codes

The current codelists confirm:
- `P_F`: Portfolio investment, Total financial assets/liabilities.
- `A_NFA_T`: Assets, Net acquisition of financial assets.
- `L_NIL_T`: Liabilities, Net incurrence of liabilities.
- `USD`: US dollar.
- `Q`: Quarterly.

The first trial indicator `P_MV` returned HTTP 200 but no observations for the tested Brazil/India keys. It was rejected for this panel. Broad country-level observations revealed `P_F` as the populated portfolio-total indicator; exact-key extraction then succeeded. Assets and liabilities are kept separate.

## Extracted panel

| Country | Accounting entry | Observations | Coverage |
|---|---|---:|---|
| Brazil | A_NFA_T — assets | 47 | 2015-Q1 to 2026-Q3 |
| Brazil | L_NIL_T — liabilities | 47 | 2015-Q1 to 2026-Q3 |
| India | A_NFA_T — assets | 46 | 2015-Q1 to 2026-Q2 |
| India | L_NIL_T — liabilities | 46 | 2015-Q1 to 2026-Q2 |
| **Total** | **4 exact series** | **186** | **2015-Q1 to 2026-Q3** |

India's 2026-Q3 observations were not returned; they remain missing. No forward-fill or synthetic row was inserted.

## Independent validation

GitHub Actions run [44472944620](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44472944620), artifact ID `14504732476`.

- 4/4 exact requests HTTP 200; 4/4 CSV parse PASS.
- 186 non-empty observations; 186 unique series-period keys; 0 duplicates.
- Exact-key values versus broad raw country capture: 186/186 exact matches.
- Raw source rows versus normalized panel attributes: 186/186 exact matches, including all 32 source columns.
- 0 missing or mismatched values; all observed quarters contiguous within each series.
- Artifact ZIP: 7,784,894 bytes; SHA-256 `2e00a175837e1ad5e98346b114c4ec5a9d55ddf38833938711e9a3106a331d6c`.
- Normalized panel SHA-256 `8ef39ecdefc4dd042d6e7a74e84aaf95aa9c66162de36164667d2bc6ad74e778`.

## Durable evidence files

Compressed raw series and normalized panel are committed under `docs/evidence/`:
- `IMF_BOP_PORTFOLIO_PILOT_BRA_IND_2015Q1_2026Q3.csv.gz`
- `IMF_BOP_PORTFOLIO_RAW_BRA_A_NFA_T_P_F_USD_Q.csv.gz`
- `IMF_BOP_PORTFOLIO_RAW_BRA_L_NIL_T_P_F_USD_Q.csv.gz`
- `IMF_BOP_PORTFOLIO_RAW_IND_A_NFA_T_P_F_USD_Q.csv.gz`
- `IMF_BOP_PORTFOLIO_RAW_IND_L_NIL_T_P_F_USD_Q.csv.gz`

The machine-readable validation summary is `docs/evidence/IMF_BOP_PORTFOLIO_PILOT_BRA_IND_2015Q1_2026Q3.json`.

## Interpretation limits — not yet a production factor

- `SCALE=6` and `PRECISION=6` are preserved as returned. No scale or currency transformation is applied until the scale semantics are independently resolved.
- This is quarterly BOP portfolio transaction data, not daily FPI/FII flow data. It cannot replace SEBI FPI/FPI-DII daily flow sources.
- Brazil and India are a pilot pair, not an approved Emerging Markets universe. No EM aggregation, weighting, ranking, or country-membership assumptions are introduced.
- BOP_AGG is a separate annual group-aggregate dataset. IMF notes that non-reporting-economy estimates may be incorporated in its group totals; it must be assessed as a separate product, not silently substituted for country observations.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, or Engines A–E changes. No trading admission is authorized.

## Next exact tasks

1. Resolve IMF `SCALE` semantics and verify unit/scale treatment from official metadata.
2. Define and version the EM country membership set, with effective dates and exclusions.
3. Probe BOP_AGG annual group aggregates as a separately labelled comparison series; preserve its estimates methodology.
4. Expand exact-key quarterly extraction only after the country universe and factor definitions are approved.
5. Keep BOP transaction flows distinct from IIP/CPIS positions and daily FPI flows.
