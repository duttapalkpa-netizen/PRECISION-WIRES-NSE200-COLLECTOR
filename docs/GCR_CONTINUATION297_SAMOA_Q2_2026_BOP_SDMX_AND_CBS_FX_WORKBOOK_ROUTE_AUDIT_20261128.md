# GCR Continuation 297 — Samoa Q2-2026 BOP machine-readable source and FX-table route audit
Date: 28-Nov-2026 (Asia/Kolkata)
Scope: WSM / Samoa; immutable 2026-Q2 63-country cohort; official source-route and methodology-boundary audit only.

## 1. Mandatory continuity preflight and PASS work skipped
- Re-read current GitHub Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, immutable 63-country matrix, C296 report, and Library Mother File `PRECISION_WIRES_V11_3_MOTHER_FILE_CONTINUATION_1_53_20261122.md`.
- Library search also rechecked the RBI DBIE TXT and the prior official FX-source register. RBI DBIE is India USD/INR and is unrelated to Samoa's Tala conversion; it was not used or merged.
- Reused C295 Table B-1 values and C296 monthly FX observations. No repeated PDF text extraction, IMF re-query, cohort rebuild, repeated A/L arithmetic, or matrix edit.
- WSM baseline remains DATA_CAPTURED / ASSET_REVIEW / LIABILITY_REVIEW / VINTAGE_UNKNOWN / FULL_PASS=NO.

## 2. New official SBS NSDP route — source discovery PASS
Samoa Bureau of Statistics National Summary Data Page states that linked datasets correspond to IMF DSBB data and exposes separate actions for Balance of Payments:
- Browse Data
- Download in SDMX
- DSBB Metadata
Official page: https://www.sbs.gov.ws/nsdp-2/

The linked official SDMX data-message URL is:
https://www.sbs.gov.ws/images/sbs-documents/SDMX/CBS/BOP_samoa.xml

The official browser retrieval rejected the XML MIME type (application/xml); direct raw-file download through the available capture route also failed. This is a retrieval-surface limitation, not evidence that the CBS/SBS source is unavailable. No XML bytes, schema, row count, period coverage or hash are claimed. Status: SOURCE_ROUTE_CONFIRMED / RAW_PAYLOAD_NOT_CAPTURED.

The NSDP's Balance of Payments DSBB metadata link resolves to the IMF Samoa BOP metadata category:
https://dsbb.imf.org/e-gdds/dqaf-base/country/WSM/category/BOP00
The current rendered page exposed the DSBB shell but not the BOP metadata body; no conversion convention can be inferred from the inaccessible body. Status: METADATA_LOCATOR_CONFIRMED / METHODOLOGY_TEXT_NOT_CAPTURED.

## 3. New official CBS machine-readable workbook locators
CBS official “B - External Trade and Payments” page, last updated 29-Oct-2026, lists B1 Balance of Payments and B11 Foreign Currency per Tala:
https://cbs.gov.ws/external-trade-and-payments

Exact official download targets exposed by the page:
- B1 Balance of Payments: https://cbs.gov.ws/media/B1-Balance-of-Payments-9.xlsx
- B11 Foreign Currency per Tala: https://cbs.gov.ws/media/B11--Foreign-Currency-per-Tala-5.xlsx

Both links were confirmed as first-party CBS workbook links. The browser retrieval layer rejected the Excel MIME type; direct raw-file downloads also failed. Therefore no workbook bytes, sheet names, row counts, date coverage, formulas, or SHA-256 are claimed. Status for both: OFFICIAL_LOCATOR_CONFIRMED / RAW_PAYLOAD_NOT_CAPTURED.

The B11 label indicates foreign-currency-per-Tala midrates. It must not be inverted or treated as a transaction-weighted BOP conversion series without inspecting the workbook's exact date and rate semantics. It is distinct from the monthly-average USD/TALA reports and from the public daily indicative rates.

## 4. FX methodology boundary — no conversion rule established
- CBS Exchange Rate Developments is explicitly a monthly report describing currency movements against Tala during the month; the April 2026 PDF reports USD/TALA 2.7244 under “Tala per foreign currencies (month average)”. Official index: https://cbs.gov.ws/exchange-rates-development
- C296 already captured Apr/May/Jun monthly-average USD/TALA values and computed a calendar-day-weighted proxy. That proxy remains NOT_ACCEPTED for BOP conversion and is not repeated here.
- CBS Daily Exchange Rates explicitly says the rates are indicative only and not for market use. It is not an accepted BOP conversion source.
- CBS Samoa Customs Rates are a separate customs-purpose table; not an accepted BOP conversion source.
- IMF Samoa 2026 Article IV publication reports fiscal-year period-average market rates (e.g. 2025/26 2.75 Tala/USD), but this is annual/fiscal-year level and does not establish a Q2-2026 portfolio transaction conversion rule.
- Samoa BOP DSBB metadata body was not retrieved. Therefore transaction-date, monthly-average, quarterly-average, and other conversion methods remain unadjudicated. Do not borrow another country's DSBB methodology.

## 5. Acceptance result
| Gate | Result |
|---|---|
| SBS NSDP official BOP locator | PASS — first-party NSDP |
| Official BOP SDMX target URL | SOURCE_ROUTE_CONFIRMED |
| BOP SDMX raw XML / schema / coverage / hash | NOT_CAPTURED |
| IMF DSBB Samoa BOP metadata locator | PASS — body not rendered |
| DSBB conversion-method statement | NOT_CAPTURED / NOT_ESTABLISHED |
| CBS B1 BOP workbook locator | PASS — first-party XLSX |
| CBS B1 raw workbook / hash | NOT_CAPTURED |
| CBS B11 FX workbook locator | PASS — first-party XLSX |
| CBS B11 raw workbook / hash | NOT_CAPTURED |
| Daily indicative/customs rates | REJECTED for BOP conversion |
| C296 monthly-average weighted proxy | NOT_ACCEPTED; not repeated |
| Official Q2 transaction FX convention | NOT_ESTABLISHED |
| CBS observation-specific revision/vintage | UNKNOWN |
| Matching archived IMF vintage | UNKNOWN |
| WSM ASSET / LIABILITY / VINTAGE / FULL gates | REVIEW / REVIEW / UNKNOWN / NO |
| Aggregate admission | NOT_AUTHORIZED |

## 6. Exact next action
1. Capture the two first-party CBS XLSX files and SBS BOP SDMX XML as original bytes using a supported browser/download session; retain exact URL, byte count, MIME type, SHA-256 and file metadata. No manual retyping or third-party mirror.
2. Inspect B1 workbook notes and the DSBB BOP metadata body for the explicit conversion method, recording basis, valuation and revision policy. Inspect B11 workbook only to determine its exact rate direction, period and observation semantics.
3. If the CBS method is transaction-date, monthly, or quarterly, follow only that documented convention and use the appropriate matching official rate series; do not construct an ad hoc calendar-day weighting.
4. Inspect BOP source data and metadata for the Q2 portfolio asset and liability legs separately and for revision markers; then compare with already archived IMF observations/vintage only if the conversion basis and vintage match are demonstrable. No IMF re-query.
5. If raw official file capture remains blocked, retain NOT_CAPTURED and do not promote WSM; proceed to the next eligible country only after recording the blocker and priority rationale.

## 7. Invariants
₹0; official/free sources only; immutable 63-country cohort; no paid API/license, no external contact, no mirror/proxy admission, no synthetic values, no inferred timestamps, no silent FX conversion, no netting or stock/flow substitution. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL.

**Task result:** Three additional official machine-readable locators are now verified (SBS BOP SDMX XML, CBS B1 BOP XLSX, CBS B11 FX XLSX), and the IMF DSBB BOP metadata locator is confirmed. Actual payload bytes and Samoa's BOP conversion convention remain unavailable; WSM gates are unchanged and aggregate remains NOT_AUTHORIZED.
