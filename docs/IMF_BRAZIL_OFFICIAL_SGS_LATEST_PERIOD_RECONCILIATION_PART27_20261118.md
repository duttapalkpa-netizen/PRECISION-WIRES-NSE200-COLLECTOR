# Brazil Reconstruction — Official SGS Latest-Period Reconciliation (Part 27)
Date: 2026-11-18
Status: OFFICIAL SGS CURRENT-PERIOD METADATA PASS / VALUE-LEVEL API RECONCILIATION PARTIAL / IMF RECONSTRUCTION BLOCKED

## Objective
Resolve the Part-25 apparent February-2026 API cutoff using BCB's own public SGS Time Series Management System and the October 2026 BCB external-sector bulletin. No third-party API or derived data is promoted to official evidence.

## Official BCB SGS verification
1. Official SGS public series page for code 22701:
   https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?hdOidSeriesSelecionadas=22701&method=consultarGraficoPorId
   Search-indexed page explicitly identifies:
   - Code 22701
   - Current account - monthly - net
   - Unit US$ million
   - Periodicity monthly
   - Start 01/01/1995
   - Last value set/2026 (September 2026)
   - Page timestamp: Public user 17/11/2026 19:27
   This is direct BCB SGS metadata, and supersedes the Part-25 conclusion that the series was stale through February 2026.
2. Official BCB Open Data Portal dataset for 22701 confirms it is monthly current-account net, USD million, and comprises goods, services, primary income and secondary income. It links to the SGS JSON/CSV resources.
3. Official BCB Open Data Portal dataset for 22707 confirms it is monthly Balance on Goods, USD million, BPM6, and reports normal timeliness up to four weeks after the reference period. It also links to SGS JSON/CSV resources.
4. Official BCB October 26, 2026 External Sector Statistics release:
   https://www.bcb.gov.br/content/statistics/externalsectorstatistics_prev/202610_External_sector_statistics_text.pdf
   It reports September 2026:
   - Current-account deficit USD 5.1 billion (versus USD 8.8 billion Sep-2025).
   - Balance-of-goods surplus USD 6.9 billion (versus USD 2.5 billion Sep-2025).
   - Goods exports USD 34.6 billion; imports USD 27.7 billion.
   - 12-month current-account deficit USD 60.0 billion / 2.33% GDP through Sep-2026.
   The release provides the value-level primary cross-check for September. Do not confuse the September monthly current-account flow with the 12-month rolling deficit.

## Corrected Part-25 conclusion
- Part-25's full-series JSON view appeared to end at February 2026. That observation remains a historical description of the specific response seen then.
- The official BCB SGS page for 22701 now explicitly says Last value = set/2026. Therefore the prior broad STALE conclusion is superseded and must not be used as the current series status.
- Correct status for 22701: official SGS latest-period metadata PASS through Sep-2026.
- For 22707, the official September BCB release reports the Sep-2026 goods balance +USD 6.9bn, and the official portal confirms 22707 is the monthly BPM6 goods-balance series. However, this audit did not retrieve the 22707 SGS series page's own Last value field. Therefore official bulletin coverage through Sep-2026 is PASS, while SGS page latest-period metadata for 22707 remains NOT_VERIFIED.
- A full value-level reconciliation of the raw SGS JSON for 22701/22707 against the September release remains PARTIAL. The date-filtered JSON response and raw bytes were not captured in this session. No raw SHA-256 is claimed.
- Do not use third-party mirrored API values to override BCB's official September release. Any value discrepancy between a mirror and BCB is a separate provenance/revision investigation.

## Updated acceptance
- SGS 22701 official page latest period: PASS, Sep-2026.
- SGS 22707 official series page latest period: NOT_VERIFIED; official bulletin reference-month coverage Sep-2026: PASS.
- BCB September 2026 bulletin: PASS.
- Exact date-filtered SGS JSON values for Sep-2026: NOT_DONE.
- Raw SGS JSON bytes, response headers, byte count, SHA-256: NOT_DONE.
- Part-25 broad stale-series conclusion: SUPERSEDED.
- Historical BPM6 ZIP byte acquisition/inspection: NOT_DONE.
- NSDP exact SDMX Data URL extraction: NOT_DONE.
- IMF historical registration events and PA changelog: NOT_DONE / UNKNOWN.
- IMF listing Dataflow BOP6 vs captured BCB XML Dataflow BOP_BPM6: CONFIRMED / UNRESOLVED.
- Brazil Reconstruction: INCOMPLETE / BLOCKED.

## Next action
Capture official SGS page/CSV/JSON data for 22701 and 22707 through the BCB interface with explicit date range through 2026-09, preserve raw bytes and SHA-256, and compare exact September observations with the October bulletin. Keep the 22701 and 22707 series definitions separate.

## Guardrails
₹0 spend; official/free sources only. No third-party mirrored data promoted as primary evidence, no synthetic rows, no guessed timestamps, no automatic Dataflow renaming, no production integration, no PR merge or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
