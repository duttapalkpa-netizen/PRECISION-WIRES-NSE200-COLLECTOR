# IIP 2022-23 official data access route audit

Audit date: 2026-11-08
Scope: locate a lawful, zero-cost official source for same-base-year IIP data needed to cross-check the April 2026 NIC-2025 first-release ledger.

## Findings

1. The MoSPI e-Sankhyiki portal identifies the current IIP series as base year 2022-23 and describes its Macro Indicators / Data Catalogue as open access. Its portal FAQ states that registration is not required for e-Sankhyiki browsing and downloads, and that Macro Indicators datasets can be downloaded as CSV after applying filters.
   - Portal: https://esankhyiki.mospi.gov.in/
   - IIP macro-indicator route: https://esankhyiki.mospi.gov.in/macroindicators?product=iip
   - Evidence checked: portal home/FAQ, 2026-11-08.

2. The MoSPI Microdata Portal separately lists study DDI-IND-NSO-IIP-2022-23, titled "Index of Industrial Production (IIP) with Base Year 2022-23". Its metadata states reference period 2022-23=100, NIC 2-digit manufacturing coverage 10-32, and use of Output PPI as deflator in the new series.
   - Catalogue: https://microdata.gov.in/nada/index.php/catalog/299
   - Get Microdata: https://microdata.gov.in/nada/index.php/catalog/299/get-microdata
   - The Get Microdata page explicitly requires login and offers free account registration. This is registered access; it is not an anonymous public download.

3. MoSPI FAQ distinguishes open-access aggregated IIP at NIC 2-digit level from registered-access item-level IIP data. Do not conflate the microdata login requirement with the open e-Sankhyiki aggregate download route.

## Audit decision

- The next preferred route is the public e-Sankhyiki IIP Macro Indicators CSV export, filtered to April 2026 and NIC 10-32, with the source's own base-year/classification/vintage metadata retained.
- If the required same-base-year series is not exposed in that public export, the alternative is the free Microdata Portal account route, requiring the account holder to log in and download the study data.
- No credentials were used, no authentication was bypassed, and no paid service or external contact was used.
- No data rows were downloaded or independently cross-checked in this audit. Therefore this note does not resolve the pending same-base-year cross-check, does not alter the 23-row ledger, and does not change any gate.
- Keep `LATER_VINTAGE_SOURCE_CROSSCHECK_PENDING` and `RAW_PDF_SHA256_PENDING` unchanged until the actual source file is obtained, hashed, parsed, and matched with explicit base-year/classification/vintage provenance.
- Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, and all 672 diagnostics remain untouched.
