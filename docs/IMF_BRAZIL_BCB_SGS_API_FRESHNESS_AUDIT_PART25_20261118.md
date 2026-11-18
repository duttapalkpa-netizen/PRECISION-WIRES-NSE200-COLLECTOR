# Brazil Reconstruction — BCB SGS API Historical Series Retrieval and Freshness Audit (Part 25)
Date: 2026-11-18
Status: PUBLIC API READ PASS / SERIES FRESHNESS WARNING / IMF RECONSTRUCTION BLOCKED

## Purpose
Advance the BCB source crosswalk by directly reading the official BCB BCData/SGS JSON endpoints for two separate monthly BPM6 indicators: current-account balance (SGS 22701) and balance-on-goods balance (SGS 22707). These are corroborative statistical series, not the complete BOP SDMX message or IMF registration-history evidence.

## Exact official API endpoints queried
- Current account, monthly balance:
  https://api.bcb.gov.br/dados/serie/bcdata.sgs.22701/dados?formato=json
- Balance on goods, monthly balance:
  https://api.bcb.gov.br/dados/serie/bcdata.sgs.22707/dados?formato=json

## Directly observed endpoint response facts
Both endpoints returned JSON arrays with monthly observations beginning 01/01/1995 and the latest visible observation dated 01/02/2026. The observed date range is therefore 1995-01 through 2026-02. Do not infer the archive ZIP's coverage from these separate SGS series.

### Latest observations (unit: USD million)
| Reference month | SGS 22701 current-account balance | SGS 22707 balance-on-goods |
|---|---:|---:|
| 2026-01 | -8,886.3 | 2,990.7 |
| 2026-02 | -5,613.8 | 3,507.5 |

### Prior-month context
- SGS 22701 current account: 2025-12 = -3,670.0; 2026-01 = -8,886.3; 2026-02 = -5,613.8.
- SGS 22707 balance on goods: 2025-12 = 8,505.4; 2026-01 = 2,990.7; 2026-02 = 3,507.5.

The series are different statistical concepts. Do not add, subtract, or treat them as interchangeable without the complete component definition and accounting context.

## Critical freshness finding
At the 2026-11-18 audit date, the latest visible observation in both full-series API responses is February 2026. That is materially older than the audit date. The Open Data Portal metadata for these monthly series describes normal timeliness as up to four weeks after the reference period. This discrepancy is a FRESHNESS WARNING requiring investigation; it is not proof of a BCB outage or data error. Until a new API response or official publication schedule is checked, these series must be rejected for current/near-real-time macro decisions and marked STALE/UNKNOWN for current period use.

## Source definitions retained
- SGS 22701 is the monthly current-account balance, USD millions. BCB portal definition aggregates balance on goods, services, primary income and secondary income. Source organization BCB/Dstat; base source SGS.
- SGS 22707 is the monthly balance-on-goods balance, USD millions. Portal definition says it is based on trade statistics adjusted by BCB for broader coverage, including electricity purchases not in Siscomex, fictitious operations and international postal shipments. Keep as a distinct series.

## Evidence limits
- These are public JSON endpoint observations inspected through official BCB API URLs.
- No raw response file was downloaded into the working container; direct binary/container download was unavailable. Therefore no raw-byte SHA-256, response byte count, HTTP headers, or complete local parse artifact is claimed.
- Web response exposed the full JSON array in the page view; this report records only the verified first/latest boundaries and selected latest rows, not a byte-exact archived dataset.
- No official BCB historical ZIP bytes were acquired in this part.
- No exact NSDP Balance of Payments SDMX URL target was extracted.
- No IMF registration event, action timestamp, or PA changelog evidence was obtained.

## Acceptance update
- SGS 22701 endpoint JSON read: PASS (public response observed).
- SGS 22707 endpoint JSON read: PASS (public response observed).
- Latest visible common reference month: 2026-02.
- Currentness for 2026-11-18: STALE / WARNING; do not use as current macro input.
- Full raw response archive and SHA-256: NOT_DONE.
- BCB monthly/quarterly/annual BPM6 ZIP acquisition: NOT_DONE.
- IMF BOP6 vs BOP_BPM6 mismatch: CONFIRMED / UNRESOLVED.
- IMF Brazil registration chronology / PA history: NOT_DONE / UNKNOWN.
- Brazil Reconstruction: INCOMPLETE / BLOCKED.

## Next action
Find and validate a newer official BCB publication/series endpoint or document the official update cadence and last release date for SGS 22701 and 22707. In parallel, acquire BCB BPM6 ZIP bytes through a working network path and extract the exact NSDP SDMX link. Do not forward-fill, infer missing months, or promote February 2026 values as current November 2026 data.

## Guardrails
₹0 spend; official/free sources only. No synthetic history, guessed timestamps, automatic Dataflow renaming, paid APIs, production integration, PR merge, or trading admission. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN is not PASS.
