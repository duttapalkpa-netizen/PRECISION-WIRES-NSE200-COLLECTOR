# Brazil Reconstruction — BCB NSDP and BPM6 Historical Source Crosswalk (Part 24)
Date: 2026-11-18
Status: SOURCE DISCOVERY PASS / RAW BYTE INGESTION NOT_DONE / RECONSTRUCTION BLOCKED

## Scope
Follow-up to the user's instruction to use the official Banco Central do Brasil (BCB) website as the next source hub. This part records only what was directly verified from BCB-published pages and IMF's current public registration listing. It does not claim the historical ZIP payloads were downloaded or parsed.

## Official BCB source discoveries
1. BCB National Summary Data Page (NSDP), English:
   https://www.bcb.gov.br/en/statistics/nsdp
   The page explicitly lists "Balance of Payments" under External Sector, National Presentation BCB, SDMX Data "SDMX-ML", with a separate Metadata link. It also lists International Investment Position, External Debt, International Reserves and Foreign Currency Liquidity, and related categories as SDMX-ML.
   Web evidence: https://www.bcb.gov.br/en/statistics/nsdp (search result captured 2026-11-18).
2. BCB Historical Series of the Balance of Payments — BPM6:
   https://www.bcb.gov.br/ingles/economic/seriehist_i_bpm6.asp?frame=1
   The page describes downloadable historical series under BPM6 and exposes three archive links:
   - Monthly: https://www.bcb.gov.br/ftp/notaecon/balpaym.zip (listed as ZIP 2.7 Mb)
   - Quarterly: https://www.bcb.gov.br/ftp/notaecon/balpayq.zip (listed as ZIP 1.0 Mb)
   - Annual: https://www.bcb.gov.br/ftp/notaecon/balpaya.zip (listed as ZIP 280 Kb)
   The page was readable, but binary download attempts through this environment failed. Therefore no ZIP contents, raw-byte sizes, SHA-256 hashes, internal file names, dataflow IDs, or observation coverage are asserted in this report.
3. BCB official External Sector Statistics explanatory note (February 2026):
   https://www.bcb.gov.br/content/estatisticas/notas_metodologicas/balanco_pagamentos/bpm6/Nota%20Explicativa%20-%20Indicadores%20do%20Setor%20Externo.pdf
   It states that BCB compiles and disseminates external-sector statistics according to BPM6 and EDS 2013; it documents selected indicator calculation methods. This is methodology evidence, not a registry transaction log.
4. BCB Open Data Portal current-account dataset:
   https://dadosabertos.bcb.gov.br/dataset/22701-transacoes-correntes---mensal---saldo
   Metadata describes a monthly time series in USD millions, source BCB Department of Statistics, derived from SGS. Reported timeliness is up to four weeks after the reference period. This can be a separate cross-check series, not a replacement for the full SDMX registration payload.
5. BCB Open Data Portal balance-on-goods dataset:
   https://dadosabertos.bcb.gov.br/dataset/22707-balanca-comercial---balanco-de-pagamentos---mensal---saldo
   Dataset metadata identifies monthly series, USD millions, BCB Department of Statistics, and the BPM6 external-sector classification. It notes adjustments to trade data (including electricity purchases not recorded in Siscomex, fictitious operations, and international postal shipments). Treat it as a distinct published series with its own definition.

## Registration mismatch cross-check
The current IMF SDMX Central public Registrations table still lists:
- Dataflow IMF:BOP6(1.0)
- Provider IMF:BR1 (Central Bank of Brazil)
- BCB SDMX XML URL
- Last Updated 2026-10-26T11:47:29.000Z
Source: https://sdmxcentral.imf.org/data/registrations.html
Previously archived inspection of the BCB registration XML payload found Dataflow IMF:BOP_BPM6(1.0). The two identifiers remain different. BCB's NSDP statement that Balance of Payments is disseminated as SDMX-ML confirms the category and format, but does not resolve which Dataflow identifier is authoritative for the IMF registration. Do not infer equivalence from BPM6 wording or a shared DSD.

## Attempted retrieval and limitations
- BCB historical BPM6 page successfully exposed the three archive URLs above.
- Browser binary retrieval failed for all three ZIPs in this environment; a direct container download attempt for the monthly ZIP also failed.
- BCB NSDP page search-index content is available, but direct page opening returns a JavaScript-required shell; the exact underlying Balance of Payments SDMX-ML target URL was not extracted in this session.
- No ZIP or new BCB XML raw bytes were obtained; no new SHA-256 hashes were generated. Existing previously captured BCB XML hash remains prior evidence and is not recalculated here.
- No official registration-history events, PA changelog rows, action timestamps, or IMF correction notice were found in these BCB source pages.

## Acceptance update
- BCB NSDP source discovery: PASS (page content indexed; Balance of Payments explicitly SDMX-ML).
- BCB BPM6 historical archive link discovery: PASS (monthly, quarterly, annual URLs visible).
- Historical ZIP byte acquisition and inspection: NOT_DONE (environment download failure).
- BCB NSDP exact SDMX link target extraction: NOT_DONE.
- IMF current registration row: PASS (current-state only).
- BOP6 vs BOP_BPM6 mismatch: CONFIRMED / UNRESOLVED.
- Brazil historical registration chronology and PA changelog: NOT_DONE / UNKNOWN.
- Brazil Reconstruction: INCOMPLETE / BLOCKED.

## Next action
Use an ordinary browser or an authorized local network to download the three official BCB ZIP files, preserve original bytes, record retrieval time/source URL/byte count/SHA-256, inspect archive contents without modifying them, and compare the monthly/quarterly/annual series identities and coverage. Separately extract the exact SDMX-ML URL from the NSDP Balance of Payments row. These data-source checks can validate BCB data consistency but cannot substitute for IMF's historical registration transaction/PA history.

## Guardrails
₹0 spend; official/free sources only. No synthetic history, guessed timestamps, automatic Dataflow renaming, paid APIs, production integration, PR merge, or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
