# IMF BOP Public Quarterly Portfolio-Flow Pilot — 2026-11-19

## Decision
**Public observation access is PASS.** Anonymous GET requests to the official IMF SDMX 3.0 data endpoint returned country-level quarterly BOP observations without an API key, login, cookies or session credentials. The API Swagger UI sign-in requirement does not prevent direct public SDMX GET access.

This is a two-country pilot (Brazil and India), not an EMDE aggregate and not a trading signal.

## Official source and structure
- Dataset: IMF Balance of Payments (BOP), official dataset page: https://data.imf.org/en/datasets/IMF.STA%3ABOP
- Dataset API docs: https://data.imf.org/en/Resource-Pages/IMF-API
- Direct API base used: `https://api.imf.org/external/sdmx/3.0/`
- Dataflow: `IMF.STA:BOP(21.0.0)`
- DSD: `IMF.STA:DSD_BOP(24.0.0)`
- Dimension order: COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY.
- Codelists: `CL_BOP_COUNTRY(1.0.0)`, `CL_BOP_ACCOUNTING_ENTRY(3.3.0)`, `CL_BOP_INDICATOR(10.0.0)`, `CL_UNIT(2.13.0)`, `CL_FREQ(1.2.0)`.

## Flow-series definitions
- Indicator `P_F`: “Portfolio investment, Total financial assets/liabilities”.
- `A_NFA_T`: “Assets, Net acquisition of financial assets”.
- `L_NIL_T`: “Liabilities, Net incurrence of liabilities”.
- Unit code `USD`; frequency `Q`.
- These are financial-account transaction flows, not CPIS/PIP stock positions. The earlier `P_MV` position-indicator smoke test returned empty observations and was rejected for this flow panel.
- Source attribute `DERIVATION_TYPE=O` is “Reported official data” (official country-authority data reported to IMF without IMF staff modifications/adjustments).
- `SCALE`, `PRECISION`, and all other source attributes are retained exactly. No rescaling, currency conversion, forward-fill, imputation or synthetic rows.

## Exact series and coverage
| Country | Series | Periods | Rows | Latest period |
|---|---|---:|---:|---|
| Brazil (BRA) | A_NFA_T / P_F / USD / Q | 2015-Q1–2026-Q3 | 47 | 2026-Q3 |
| Brazil (BRA) | L_NIL_T / P_F / USD / Q | 2015-Q1–2026-Q3 | 47 | 2026-Q3 |
| India (IND) | A_NFA_T / P_F / USD / Q | 2015-Q1–2026-Q2 | 46 | 2026-Q2 |
| India (IND) | L_NIL_T / P_F / USD / Q | 2015-Q1–2026-Q2 | 46 | 2026-Q2 |
- Total panel: 186 non-empty observations.
- All four series are contiguous across their available quarterly windows.
- India 2026-Q3 is absent in this retrieval and remains absent; no forward-fill.

## Anonymous API query patterns
Example Brazil asset-flow request:
`https://api.imf.org/external/sdmx/3.0/data/dataflow/IMF.STA/BOP/21.0.0/BRA.A_NFA_T.P_F.USD.Q?c%5BTIME_PERIOD%5D=ge%3A2015-Q1&c%5BTIME_PERIOD%5D=le%3A2026-Q3&format=csvdata`

Exact query keys:
- `BRA.A_NFA_T.P_F.USD.Q`
- `BRA.L_NIL_T.P_F.USD.Q`
- `IND.A_NFA_T.P_F.USD.Q`
- `IND.L_NIL_T.P_F.USD.Q`

## Independent QA
- Workflow run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44473784679
- Artifact ID: `14505706180`
- Artifact ZIP SHA-256 (GitHub artifact digest): `cbb27d38d258a0ab539baa334100a94037e8446460926670ef66a50aa66d3287`
- Exact request status: 4/4 HTTP 200; CSV parse 4/4 PASS.
- Exact normalized panel: 186 rows, 186 unique keys, zero duplicates.
- Exact-to-broad raw comparison: 186/186 value matches; zero missing, zero value mismatches.
- Raw-to-normalized attribute comparison: zero mismatches.
- All four quarterly series contiguous.
- Normalized panel SHA-256: `8ef39ecdefc4dd042d6e7a74e84aaf95aa9c66162de36164667d2bc6ad74e778`.
- Per-series raw CSV SHA-256:
  - BRA A_NFA_T: `3feca530a6495a3877370ad21bbacece69de87f3ebb725af4cbc455e1f84183c`
  - BRA L_NIL_T: `2d6b4a22740fe4df16ab4b84e71f69fd6d2833e12c32d94fa0db7bee2925a254`
  - IND A_NFA_T: `c86388af35f1b83b0b9d2a451d35c3c78541ea03af1d9a9c826a12bb34f04a82`
  - IND L_NIL_T: `25d41406425a78d575273a7b3fc63cfb3ecc05cda3789c25787b5a610b5c138d`

## BOPSY 2025 metadata boundary
- Official BOPSY Explanatory Notes PDF SHA-256: `8bd7cf9dd16845b2c781b0c2349971c23952a68a7fbcf9d78f01d84c2da353d8`.
- 200 country reporting-coverage rows and 219 raw country-group membership labels extracted from the 31-page official PDF.
- BOPSY country-group aggregates can include WEO-derived estimates for nonreporting economies. Do not mix aggregate estimates with country-level reported observations without explicit provenance.
- Reporting currency and last reported year are coverage metadata, not observations.

## Rejected / not admitted
1. `P_MV` position indicator: returned empty observation payloads for the four requested country/accounting-entry keys; not used for flow panel.
2. BOPSY country-group aggregates: not substituted for quarterly country observations; annual and may contain estimates for nonreporting economies.
3. CPIS/PIP positions: not substituted for BOP transaction flows.
4. No country-group sum or net-flow scalar calculated in this pilot. Assets and liabilities remain separate until sign, unit-scale and group aggregation policy are formally frozen.
5. No stock or trade admission; this is research-only data acquisition and validation.

## Remaining work
1. Resolve `SCALE=6` presentation semantics from authoritative IMF metadata before any rescaling; keep raw values/attribute unchanged meanwhile.
2. Expand to a versioned EMDE country universe using a frozen membership edition and map names to IMF BOP country codes through the official codelist.
3. Acquire all EMDE country observations using exact validated keys; report country-by-country period coverage, derivation type, missingness and revisions.
4. Define net flow sign convention and FX conversion only after the source metadata and unit scale are resolved.
5. Add point-in-time vintage/revision handling and test no-lookahead.
6. Integrate the panel into GCR only after cross-country completeness and reconciliation pass; no production weights or stock-selection changes.

## Hard invariants
₹0 spend; official/free sources only; no synthetic data; no invented timestamps; no paid API; no selector/ranking/pressure-fade/CORE-672/Engine A–E changes. UNKNOWN is never PASS.
