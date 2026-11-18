# Brazil Reconstruction — BCB September 2026 Official Release Freshness Reconciliation (Part 26)
Date: 2026-11-18
Status: OFFICIAL BULLETIN COVERAGE PASS / SGS API RESPONSE CONFLICT OPEN / IMF REGISTRATION RECONSTRUCTION BLOCKED

## Why this part exists
Part-25 recorded that the directly opened full-series SGS JSON responses for 22701 and 22707 appeared to end at February 2026. A later official BCB press release, published October 26, 2026, proves that BCB had already published September 2026 external-sector statistics. Therefore the Part-25 broad "BCB data is stale" interpretation is superseded. The narrower finding is a retrieval/response-coverage discrepancy that must be reconciled.

## Official primary source
BCB, "External Sector Statistics", Press Release dated October 26, 2026:
https://www.bcb.gov.br/content/statistics/externalsectorstatistics_prev/202610_External_sector_statistics_text.pdf

The document explicitly reports:
- Reference month September 2026.
- Current-account deficit for September 2026: USD 5.1 billion; September 2025 comparator: USD 8.8 billion.
- Current-account deficit over the 12 months through September 2026: USD 60.0 billion, 2.33% of GDP; through August 2026: USD 63.7 billion, 2.50% of GDP; through September 2025: USD 78.4 billion, 3.57% of GDP.
- Balance-of-goods surplus in September 2026: USD 6.9 billion; September 2025 comparator: USD 2.5 billion.
- September 2026 goods exports USD 34.6 billion (+12.9% YoY); goods imports USD 27.7 billion (-1.7% YoY).
- Services deficit USD 5.2 billion; primary income deficit USD 7.2 billion.
- Direct investment liabilities net inflows in September 2026 USD 11.3 billion; 12-month through September USD 88.3 billion (3.43% GDP).
- Domestic-market portfolio investment net outflows USD 2.1 billion in September 2026; 12-month net inflows USD 5.1 billion.
- International reserves USD 362.8 billion in September 2026.
The PDF is an official BCB press release. Do not overstate approximate chart values as exact monthly observations; use the explicit narrative values above for exact claims.

## Reconciliation against Part-25
- Part-25's observation that the web-opened SGS JSON response ended at 2026-02 remains a description of that response as observed then; it is not evidence that BCB's underlying source was stale.
- The official October 26 BCB release confirms coverage through September 2026 for the external-sector statistical publication.
- Therefore the prior conclusion "reject these series because BCB's source is stale through February" is withdrawn/superseded.
- New status: OFFICIAL BCB EXTERNAL-SECTOR RELEASE COVERAGE THROUGH 2026-09 = PASS.
- The discrepancy between the SGS API response visible in the earlier audit and the newer official bulletin is OPEN. A date-filtered API request could not be read through the available web retrieval interface; no successful API refresh is claimed.
- Do not copy bulletin headline numbers into the SGS raw series as if they were API rows. Keep press-release observations and SGS raw API observations as separate evidence objects until exact series extraction is validated.

## Current-use boundary
As of 2026-11-18, the latest BCB external-sector bulletin located in this audit is dated 2026-10-26 and covers reference month September 2026. This is a one-month reporting lag, not a February-to-November stale series. The bulletin is appropriate as the latest located official monthly release; confirm the next scheduled BCB publication before treating it as the latest available after its release date.

## What remains not done
- Exact date-filtered SGS 22701/22707 API response for March-September 2026: NOT_DONE (web retrieval interface did not expose response).
- Raw PDF byte archive, byte count and SHA-256: NOT_DONE.
- Raw JSON byte archive and SHA-256: NOT_DONE.
- Reconcile monthly exact values in PDF tables against SGS rows: PARTIAL (explicit September current-account and goods balances found; not full monthly table).
- BCB historical BPM6 ZIP acquisition/inspection: NOT_DONE.
- Exact NSDP SDMX Balance of Payments link target: NOT_DONE.
- IMF registration events and PA changelog: NOT_DONE / UNKNOWN.
- BOP6 vs BOP_BPM6 mismatch: CONFIRMED / UNRESOLVED.
- Brazil Reconstruction: INCOMPLETE / BLOCKED.

## Implications for Macro-Geo
- Use September 2026 official BCB bulletin as the latest located monthly external-sector evidence, with source publication date 2026-10-26 and reference month 2026-09.
- Preserve the distinction between current-account balance, goods balance, services, primary income, FDI liabilities and portfolio flows.
- Do not treat these as the complete financial-account/BoP table or as IMF registration history.
- No forward-fill, synthetic rows, or inferred timestamps.

## Next action
Obtain the original BCB PDF and date-filtered SGS JSON through a normal browser/local authorized network, archive exact bytes and SHA-256, and reconcile the September 2026 values against the corresponding SGS series. Then continue historical BPM6 ZIP inspection and, separately, seek authorized IMF Brazil registration/PA history.

## Guardrails
₹0 spend; official/free sources only. No paid APIs, synthetic historical data, guessed timestamps, automatic Dataflow renaming, production integration, PR merge or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
