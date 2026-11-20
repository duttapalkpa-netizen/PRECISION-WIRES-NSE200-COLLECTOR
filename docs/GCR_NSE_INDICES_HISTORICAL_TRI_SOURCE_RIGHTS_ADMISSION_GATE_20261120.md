# GCR NSE Indices Historical TRI — Source Rights & Admission Gate
Date: 2026-11-20
Research continuation 42 — bounded rights/availability review
Status: **RIGHTS NOT CLEARED / NOT ADMITTED**

## 1. Continuity and duplicate rejection
Before this task, the Master Continuity Ledger and prior reports were inspected.
- BSE sector TRI rights gate is already complete: `docs/GCR_BSE_SECTOR_TRI_SOURCE_RIGHTS_ADMISSION_GATE_20261120.md`. It found BSE terms prohibit historical database creation and derived data absent express written consent. Do not repeat.
- Existing NSE TRI route discovery is already recorded in `docs/GCR_NSE_HISTORICAL_INDEX_VIX_SAMPLE_INTEGRITY_REVIEW_CONTINUATION42_PART6_20261119.md` and related GCR reports. It identifies the official NSE/NSE Indices historical reports route. Do not repeat route discovery or mistake it for an accepted dataset.
- GCR requires total-return series, not price-only series, with aligned close/timezone, publication timestamp and vintage. No source admission follows merely from a public URL.

## 2. Official primary-source evidence inspected
1. NSE Indices Historical Data: https://www.niftyindices.com/reports/historical-data
   - Page presents a distinct “Total returns Index Values” selection and a result schema with “Total Returns Index” and “Net Total Return Index” columns.
   - It offers index-type/sub-index/index/date-range selection and CSV format.
   - This establishes a public-facing retrieval interface and the existence of TRI/NTR output fields. It does **not** itself state a reuse licence, permission to retain a long-term database, or permission for derived analytical datasets.
2. NSE Indices Products & Services: https://www.nse.in/static/nse-indices/products-services
   - States use of NSE Indices data, names or indices requires a licence or subscription.
   - States licensing is mandatory for tracking index performance and use of index names; data subscription for index values/constituents is a paid service.
3. NSE Indices Index Data Subscription: https://www.nse.in/static/nse-indices/index-data-subscription
   - Describes ongoing and historical index data products and identifies quantitative research/performance attribution among applications.
   - Directs users to contact NSE Indices for licensing opportunities and asserts proprietary rights in index names, trademarks, copyrights, compilation, composition and changes.
4. NSE Data Sharing & Usage Policy: https://www.nseindia.in/static/market-data/nse-data-policy
   - The policy governs NSE/NSE Data market-data products and says use, handling, transmission and dissemination are governed by a Relevant Agreement.
   - It expressly includes historical data in the definition of Market Data, restricts redistribution except as agreed, and routes research requests through NSE Economic Policy Research Department with case-specific documentation and confidentiality declarations.
   - Scope caution: this policy is published for NSE/NSE Data market-data products; it is not treated here as a substitute for a specific NSE Indices licence or a definitive legal interpretation of every public niftyindices.com TRI response.
5. BSE comparison remains separately documented in the BSE gate; no BSE data or terms are imported as an NSE rule.

## 3. Acceptance decision
**NSE TRI is NOT ADMITTED to the GCR historical research database or derived sector-transmission panel under the evidence currently available.**
Reason: a public TRI/NTR interface is visible, but the same provider's official commercial/licensing pages state that use of index data/names/indices requires licence or subscription. No official page inspected grants this user an explicit free licence to archive daily TRI/NTR observations, build a historical database, calculate derived returns/sector factors, or retain/publish derived datasets. The user’s no-paid-source constraint does not create such permission.

This is a rights/permission gate result, not a claim that the TRI values are technically unavailable, nor a legal opinion. A public interface and CSV button do not override licensing statements. No endpoint scraping, hidden API probing, automated download, database build or data ingestion was performed.

## 4. Acceptance matrix
| Gate | Status | Evidence / reason |
|---|---|---|
| Official NSE Indices provider identified | PASS | Official NSE Indices pages |
| Public historical TRI/NTR interface identified | PASS | Historical Data page exposes TRI/NTR fields and CSV interface |
| Exact TRI vs NTR distinction visible | PASS | Separate result headings |
| Public interface proves free reuse licence | NOT_ESTABLISHED | No reuse grant found on page |
| Explicit permission for persistent historical database | UNKNOWN / NOT_ESTABLISHED | No affirmative grant found |
| Permission for derived returns/sector-transmission analytics | UNKNOWN / NOT_ESTABLISHED | Licensing required; scope not granted |
| Unrestricted free historical TRI download | NOT_ESTABLISHED | Interface exists; provider states index data subscription is paid/licensed |
| Daily historical TRI acquired and hash-verified | NOT_DONE | No download attempted |
| Exact sector index universe, identifiers, start dates and currency validated | NOT_DONE | No dataset admission |
| GCR sector-return panel admission | BLOCKED | Rights and dataset acceptance gate not closed |

## 5. Required evidence to reopen
Only reopen if an official source supplies one of:
- an explicit public licence covering internal research storage, persistent database creation, derived calculations/analytics, retention, and any intended disclosure; or
- a provider-issued written permission/agreement covering those exact purposes and the applicable index universe, term, geography and users; or
- a clearly scoped official open-data licence attached to the exact TRI resource.

If permission is obtained, preserve the exact terms version/date, resource/index IDs, TRI vs NTR definition, currency, launch/first-value/base dates, daily coverage, publication and retrieval timestamps, timezone/close convention, vintage/revision treatment, schema/parser version, raw bytes, SHA-256, immutable path, and QA. Keep PR, TRI and NTR separate.

## 6. GCR impact and next action
- NSE TRI factor remains **UNKNOWN / EXCLUDED** from GCR scoring and sector-transmission calculations.
- BSE sector TRI remains **RIGHTS BLOCKED / NOT ADMITTED** under its separate report.
- Do not substitute price-return index for TRI, infer dividend-adjusted returns, or use an unlicensed mirror/third-party scraper.
- Next highest-value work should move to a distinct unfinished GCR input with official free-use evidence, rather than repeating either TRI route discovery or rights checks. The exact next task must be selected only after ledger preflight; likely candidates include the still-open raw IMF BOP DSD/codelist/dataflow capture or a remaining CDSL/NSDL raw archive parsing gap, but do not assume those are not completed without checking the latest reports.

## 7. Protected invariants
No production code, selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, IPO-PLX V2, model weights, or trade gates changed. No paid API, synthetic data, fabricated timestamp, or access-control bypass. UNKNOWN is never PASS.
