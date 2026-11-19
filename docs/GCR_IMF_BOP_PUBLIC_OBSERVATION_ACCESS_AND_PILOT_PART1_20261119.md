# GCR — IMF BOP Public Observation Access and Brazil/India Pilot (Part 1)
Date: 2026-11-19 (Asia/Kolkata)
Status: public observation route CONFIRMED; bounded two-country panel PASS; EMDE aggregate NOT_DONE.

## 1. Executive result
The earlier assumption that IMF BOP observations were blocked behind the beta portal was too broad. The IMF Data API's Swagger explorer asks users to sign in, but the IMF's public SDMX 3.0 data endpoint was independently reached without API key, cookies or credentials. Public BOP observations were downloaded as CSV.
- Dataset/dataflow: `IMF.STA:BOP(21.0.0)`
- Data structure: `IMF.STA:DSD_BOP(24.0.0)`
- Dimensions (in order): COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY; TIME_PERIOD is the time dimension.
- Official dataset landing page: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- API data route tested: `https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0/{key}?...`
- API docs still state SDMX 2.1/3.0 and beta portal sign-in for Swagger exploration. That sign-in note does not prevent the tested public GET observation endpoint from returning CSV without credentials.

## 2. Raw acquisition and independent reconciliation
Workflow: [44472944620](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44472944620)
Artifact: 14504732476, `imf-bop-public-route-probe-44472944620.zip`, size 7,784,894 bytes, SHA-256 `2e00a175837e1ad5e98346b114c4ec5a9d55ddf38833938711e9a3106a331d6c`.
- Official IMF dataset/API/metadata page responses: HTTP 200.
- Official IMF BOP dataflow structure endpoint: HTTP 200, XML parse PASS, 5 dimensions.
- Official IMF DSD_BOP structure endpoint: HTTP 200, XML parse PASS.
- Exact BOP codelists and concept scheme: all 7 requested responses HTTP 200 and XML parse PASS.
- Broad country diagnostics: Brazil quarterly all-key query 103,927 rows; India quarterly all-key query 62,842 rows (62,337 nonempty); Brazil annual all-key query 25,501 rows; raw response bytes and SHA-256 retained in artifact.
- The first exact-key probe tried `P_MV` (Portfolio investment, Market value): four requests returned HTTP 200 CSV, but zero nonempty observations. This is an empty-series diagnostic, not a data PASS; do not use P_MV as a BOP flow indicator in this extraction.
- Broad response inspection identified `P_F` (Portfolio investment, Total financial assets/liabilities) as the indicator with observations. Exact series were then captured for assets and liabilities.

## 3. Exact pilot panel
Key dimensions: COUNTRY × BOP_ACCOUNTING_ENTRY × INDICATOR × UNIT × FREQUENCY.
- Country codes: BRA (Brazil), IND (India)
- Accounting entries: `A_NFA_T` = Assets, Net acquisition of financial assets; `L_NIL_T` = Liabilities, Net incurrence of liabilities
- Indicator: `P_F` = Portfolio investment, Total financial assets/liabilities
- Unit code: USD; frequency: Q
- Period request: 2015-Q1 through 2026-Q3
- Four exact CSV requests all HTTP 200 and parsed.
- Brazil: 47 quarterly observations in each entry, 2015-Q1 through 2026-Q3.
- India: 46 quarterly observations in each entry, 2015-Q1 through 2026-Q2. 2026-Q3 not present; no forward fill.
- Total normalized rows: 186; unique series-period keys: 186; duplicates: 0.
- No synthetic rows, no forward fill, no currency conversion, no rescaling; all source attributes including `SCALE`, `PRECISION`, `DERIVATION_TYPE`, `IFS_FLAG`, `STATUS` were preserved as delivered.
- Raw-to-normalized attribute matches: 186/186.
- Exact-query vs independent broad-query value matches: 186/186.
- Missing-from-broad: 0; value mismatches: 0; period sequences contiguous within each country/entry.
- Independent validator status: PASS.
- Normalized panel SHA-256: `8ef39ecdefc4dd042d6e7a74e84aaf95aa9c66162de36164667d2bc6ad74e778`.
- Exact CSV SHA-256:
  - BRA A_NFA_T: `3feca530a6495a3877370ad21bbacece69de87f3ebb725af4cbc455e1f84183c`
  - BRA L_NIL_T: `2d6b4a22740fe4df16ab4b84e71f69fd6d2833e12c32d94fa0db7bee2925a254`
  - IND A_NFA_T: `c86388af35f1b83b0b9d2a451d35c3c78541ea03af1d9a9c826a12bb34f04a82`
  - IND L_NIL_T: `25d41406425a78d575273a7b3fc63cfb3ecc05cda3789c25787b5a610b5c138d`

## 4. Public BOP DSD V2.6.0 metadata archive — separate structure
The official SDMx Global Registry publishes BOP DSD V2.6.0 without authentication. It was captured separately, both SDMX-ML 2.1 and 3.0.
Workflow: [44473409770](https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44473409770)
Artifact: 14505177819, `imf-bop-dsd-v260-public-metadata-44473409770.zip`, size 237,674 bytes, ZIP SHA-256 `ba2ce640bb3a4c1cf614341103facec5b9b9aea820100fe7e28a3447993576fe`.
- SDMX 2.1 XML: 1,081,882 bytes; SHA-256 `642fa30fa3ee76be08bf2cdcebdef452e38a421355dd3516fe4666d9cce7b122`; XML parse PASS.
- SDMX 3.0 XML: 1,076,119 bytes; SHA-256 `5296c0fa950d19dea53a5a477a98915bcb14b1cecb673fbac9a0dcc87ebb11a2`; XML parse PASS.
- 23 codelists, 1 concept scheme, 3 dataflows captured in each format.
- DSD `IMF:BOP(2.6.0)` has 17 dimensions plus TIME_PERIOD, including REF_AREA, COUNTERPART_AREA, REF_SECTOR, COUNTERPART_SECTOR, FLOW_STOCK_ENTRY, ACCOUNTING_ENTRY, INT_ACC_ITEM, FUNCTIONAL_CAT, INSTR_ASSET, MATURITY, UNIT_MEASURE, CURRENCY_DENOM, VALUATION, COMP_METHOD and TYPE_ENTITY.
- This Global Registry BOP DSD V2.6.0 is NOT assumed to be the same as the IMF Data Portal's `IMF.STA:DSD_BOP(24.0.0)` used by dataflow `IMF.STA:BOP(21.0.0)`. Their identifiers, dimensions, codelists and versioning are distinct. No silent crosswalk or alias has been applied.
- The older IMF pilot BOP dissemination page contains regional files but is last updated 2013-01-09 and reports only 75 series per country. It is stale and explicitly rejected for current panel ingestion.

## 5. Semantics and guardrails
- `P_F` separates portfolio investment financial assets from liabilities through the accounting-entry dimension. These are financial-account transactions, not CPIS/PIP positions.
- ECB's BPM6 explainer describes financial account entries as net acquisition of financial assets and net incurrence of liabilities; net lending/borrowing is assets minus liabilities. This report does not yet calculate a signed "net inflow" factor or combine the two entries; sign conventions and source attributes must be validated first.
- `SCALE=6` was preserved as the dataflow's SCALE attribute. It was not interpreted as a multiplier or applied as a power of ten. The separate BOP DSD V2.6.0 uses a distinct `UNIT_MULT` attribute. Do not transfer semantics between the two DSDs without an explicit concept crosswalk.
- `IFS_FLAG`, `DERIVATION_TYPE` and `STATUS` are retained exactly. Blank attributes remain blank.
- This is a two-country pilot, not an EMDE aggregate, no FII/DII proxy, no investment recommendation, no predictive score and no production input.

## 6. Next actions
1. Retrieve October 2026 WEO Entire Dataset workbook and extract the exact 154-economy Emerging Market and Developing Economies membership edition. Match names to BOP country codes with an explicit unmapped/ambiguous list.
2. Expand the exact `P_F` assets/liabilities quarterly panel to all WEO EMDE members with a date-coverage matrix; do not fill gaps.
3. Validate source attributes and units/scale semantics before any cross-country sum. Determine whether dataflow country-group aggregates are already supplied and compare only after composition/method is known.
4. Define EMDE panel completeness threshold and membership-vintage handling before aggregate calculations.
5. Only then calculate net-flow candidate measures and align to global rates/FX/risk/market benchmarks.

## Sources
- IMF BOP dataset: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- IMF API documentation: https://data.imf.org/en/Resource-Pages/IMF-API
- SDMx BOP DSD V2.6.0 / public registry: https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/
- IMF WEO October 2026 groups workbook: https://data.imf.org/-/media/iData/External-Storage/Documents/0FA3DC49A04D446E9D69DBEB29979E1C/en/WEOOct2026all.xlsx
- BPM6 financial account description: https://www.ecb.europa.eu/press/pubbydate/2023/html/ecb.bopiipbook202310~d2c47838a5.en.html
- IMF copyright and data use: https://www.imf.org/en/About/copyright-and-terms

## Decision
IMF BOP public observation route: PASS (tested exact endpoint).
Brazil/India 186-row quarterly pilot panel: PASS (bounded).
Official BOP DSD V2.6.0 metadata archive: PASS (separate from IMF portal DSD).
EMDE membership mapping: NOT_DONE.
EMDE complete panel/aggregate: NOT_DONE.
GCR formula/sector transmission/backtest: NOT_DONE.
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or Engines A-E changed. ₹0; no paid API, credentials, synthetic observations or guessed keys.
