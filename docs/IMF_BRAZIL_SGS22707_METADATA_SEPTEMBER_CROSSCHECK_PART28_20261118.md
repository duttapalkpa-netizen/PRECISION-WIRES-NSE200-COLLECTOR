# Brazil Reconstruction — SGS 22707 Official Metadata and September Coverage Check (Part 28)
Date: 2026-11-18
Status: METADATA PASS / SEPTEMBER VALUE CROSS-CHECK PARTIAL / PRIMARY SGS PAGE LATEST-VALUE NOT_VERIFIED

## Objective
Continue Part-27 by closing the specific gap: official SGS 22707 latest-observation metadata and September 2026 value. Preserve the distinction between official primary evidence and secondary corroboration.

## Official BCB evidence inspected
1. BCB Open Data Portal dataset 22707:
   https://dadosabertos.bcb.gov.br/dataset/22707-balanca-comercial---balanco-de-pagamentos---mensal---saldo
   Official metadata confirms:
   - monthly time series;
   - unit: million US dollars;
   - SGS code 22707;
   - source: BCB Department of Statistics;
   - source database: SGS;
   - expected timeliness: up to four weeks after reference period;
   - series begins 01-01-1995;
   - metadata last updated 8 September 2026.
   This is official definition/metadata evidence, not a live last-observation field.
2. Official BCB public SGS metadata page for 22707 was found:
   https://www3.bcb.gov.br/sgspub/consultarmetadados/consultarMetadadosSeries.do?hdOidSerieSelecionada=22707&method=consultarMetadadosSeriesInternet
   Search-indexed page confirms series 22707 exists in the public SGS module. The embedded Basic data/Metadata iframe did not expose a last-observation field in the accessible page capture.
3. The direct public SGS value/chart URL for 22707 was attempted, but the browser retrieval layer returned an inaccessible/internal-error page. No raw official series response was obtained in this part.

## September 2026 corroboration — secondary, not promoted to primary
A third-party charting page that attributes its series to BCB SGS 22707 reports:
- latest observation: September 2026;
- value: USD 6,869 million;
- coverage: Jan-1995 through Sep-2026;
- stored/collected series timestamp 11 Nov 2026.
Source: https://econograma.com.br/escuro/graficos/balanca-comercial-bp/
This is secondary corroboration only. It is directionally consistent with BCB's official 26 Oct 2026 external-sector bulletin, which reports September goods balance of approximately USD 6.9 billion. Do not use the third-party exact 6,869 value as an official BCB raw observation until the primary SGS CSV/JSON is captured.
The third-party page itself warns that the series concept is BPM6 balance-of-payments goods balance and differs from MDIC customs trade balance. Preserve this definition boundary.

## What is established / not established
- Official BCB dataset identity and metadata for 22707: PASS.
- Official BCB metadata says normal timeliness up to four weeks: PASS.
- BCB official September bulletin reports September 2026 goods balance USD 6.9bn: PASS (bulletin-level, rounded).
- Secondary mirror reports exact SGS 22707 September value USD 6,869m: corroboration only.
- Official SGS 22707 latest-observation field: NOT_VERIFIED.
- Exact official SGS 22707 September JSON/CSV record: NOT_DONE.
- Raw response bytes, headers, byte count and SHA-256: NOT_DONE.
- Value-level official reconciliation: PARTIAL, not PASS.
- SGS 22701 official latest observation remains September 2026 (Part-27).
- BCB historical BPM6 ZIP acquisition/inspection: NOT_DONE.
- NSDP exact SDMX Data URL extraction: NOT_DONE.
- IMF registration history and PA changelog: NOT_DONE / UNKNOWN.
- IMF registry Dataflow BOP6 vs captured BCB XML Dataflow BOP_BPM6: CONFIRMED / UNRESOLVED.
- Brazil Reconstruction: INCOMPLETE / BLOCKED.

## Next action
Obtain official BCB SGS 22707 CSV/JSON through the Open Data Portal resource download or local browser. Preserve the exact bytes, retrieval time, source URL, HTTP headers, byte count and SHA-256. Compare September 2026 value against the official BCB October bulletin and record any revisions. Do not substitute the third-party 6,869m mirror for primary data.

## Guardrails
₹0 spend; official/free sources only. No paid APIs, synthetic rows, guessed timestamps, third-party promotion to primary, automatic Dataflow renaming, production integration, PR merge or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
