# GNB 2024 — IMF BOP series-key and reporting-period audit
Date: 2026-11-19
Continuation: 60

## Decision
**GNB national-source reporting periodicity: annual publication documented. Exact IMF BOP dataflow series availability for GNB: NOT_VERIFIED in this audit. Gross-leg admission: BLOCKED.**
Do not claim that a quarterly IMF series exists or does not exist until the exact public API key query is captured and archived. Do not map annual BCEAO net Financial Account values to quarterly IMF A_NFA_T / L_NIL_T.

## Exact panel mapping already established in the repository
The current historical GCR panel was built from:
- Dataflow: IMF.STA:BOP(21.0.0)
- DSD: IMF.STA:DSD_BOP(24.0.0)
- Dimension order: COUNTRY, BOP_ACCOUNTING_ENTRY, INDICATOR, UNIT, FREQUENCY
- Exact pilot codes: A_NFA_T = Assets, Net acquisition of financial assets; L_NIL_T = Liabilities, Net incurrence of liabilities; P_F = Portfolio investment, Total financial assets/liabilities; USD; Q.
- The exact key pattern in the existing capture scripts is COUNTRY.ENTRY.INDICATOR.UNIT.FREQUENCY (e.g. BRA.A_NFA_T.P_F.USD.Q).
- The 2026-11-19 IMF BOP coverage QA says GNB is among 40/154 G200 members with no observations for either P_F entry in the captured panel. This is a panel result, not proof that every current IMF dataflow/version lacks GNB series.

Repository evidence:
- `docs/GCR_IMF_BOP_PORTFOLIO_FLOW_PILOT_20261119.md`
- `docs/GCR_IMF_BOP_EMDE_COVERAGE_QA_PART3_20261119.md`
- `scripts/research/capture_imf_bop_portfolio_panel.py`

## Official IMF source evidence
1. IMF BOP dataset page describes the dataset as Annual and Quarterly, and announces the BOP/IIP Metadata Dashboard released 18 Nov 2026:
   https://data.imf.org/en/datasets/IMF.STA%3ABOP
2. IMF BOP Metadata Dashboard landing page:
   https://data.imf.org/en/dashboards/bop%20metadata%20dashboard
   The dashboard's GNB country-level detail could not be rendered through the available browser extraction in this audit; no GNB dashboard fields are asserted.
3. IMF e-GDDS metadata for Guinea-Bissau states that BOP aggregates appear annually in a brochure entitled "Balance of Payments of Guinea-Bissau":
   https://dsbb.imf.org/egdds/dqaf-base/country/GNB/category/AAC00
4. IMF Country Report 25/167 (July 2025), Annex III / Data Issues, states that final annual BOP data are produced only 10–12 months after year-end; it also records the launch of the National Summary Data Page in June 2024 and continuing efforts to populate it. This is evidence of annual national publication/timeliness, not proof that the IMF cannot disseminate quarterly estimates:
   https://www.imf.org/-/media/files/publications/cr/2025/english/1gnbea2025001-print-pdf.pdf
5. IMF Country Report 22/196 notes weak BOP data, substantial unrecorded trade and inconsistencies between financial-account transactions and IIP positions; it describes the ITRS implementation as expected to improve source data and periodicity from annual to quarterly:
   https://www.imf.org/-/media/files/publications/cr/2022/english/1gnbea2022002.pdf
6. IMF SDMX Central currently lists the IMF BOP DSD as version 2.6.0. The SDMx-BOP standards page states BOP package v2.6.0 was published December 2025:
   https://sdmxcentral.imf.org/data/datastructure.html
   https://sdmx.org/sdmx-data-structure-definitions-for-balance-of-payments-sdmx-bop/
   This is a newer registry structure version than the legacy 24.0.0 DSD used by the captured historical panel. No automatic remapping of the legacy panel is authorized without an explicit code/structure crosswalk.

## Exact verification status
| Test | Result |
|---|---|
| Legacy IMF dataflow/DSD and dimension order from existing pilot | PASS |
| Legacy A_NFA_T / L_NIL_T / P_F semantics from existing pilot | PASS |
| GNB absent in the captured 154-member P_F panel | PASS (panel scope only) |
| GNB national BOP public brochure periodicity | Annual documented |
| Current IMF BOP dashboard GNB metadata detail | NOT_RETRIEVED |
| Exact GNB API requests for both gross-leg series, all indicators/units | NOT_RUN / NOT_VERIFIED |
| Current DSD v2.6.0 to legacy DSD 24.0.0 crosswalk | NOT_DONE |
| GNB 2024 quarterly gross asset/liability observations | NOT_VERIFIED |
| Production/backtest admission | BLOCKED |

## Next bounded action
Run one focused, read-only API capture against the current IMF BOP dataflow/DSD and the exact legacy dataflow key pattern for GNB:
- `GNB.A_NFA_T.P_F.USD.Q`
- `GNB.L_NIL_T.P_F.USD.Q`
- query a narrow window first (2024-Q1 to 2024-Q4), then broad query only if response indicates a valid series.
Archive raw response bytes, HTTP status, headers, retrieval UTC, byte counts, SHA-256, exact URL/key, and series/observation attributes. Query current DSD v2.6.0 separately and preserve its codelist/code mapping. A 404/empty response is not proof of universal absence; record only exact endpoint and version scope.
If GNB has no quarterly observations, retain UNKNOWN/BLOCKED and do not interpolate the annual BCEAO value.

## Constraints
No net-to-gross inference, no stock-to-flow conversion, no annual-to-quarterly interpolation, no forward fill, no fabricated timestamps, no FX or scale conversion without independent source reconciliation. Preserve Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged. ₹0 research spend. UNKNOWN is never PASS.
