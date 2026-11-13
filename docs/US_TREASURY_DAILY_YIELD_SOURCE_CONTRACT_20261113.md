# US Treasury Daily Yield Curve Source Contract & Retrieval Gate — 2026-11-13

## Scope
Research-only source qualification for the Global Capital Rotation Overlay. This record does not modify the production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 × 12), Hard Gate, or any production workflow.

## Official source identity
- Publisher: U.S. Department of the Treasury.
- Daily view: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve
- XML feed documentation: https://home.treasury.gov/treasury-daily-interest-rate-xml-feed
- XML endpoint pattern: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=YYYY
- CSV archive index: https://home.treasury.gov/interest-rates-data-csv-archive/
- Archive listing identifies Daily Treasury Par Yield Curve Rates from 1990 and CSV files including 1990-2024 and decade segments.
- Official feed documentation states the XML endpoint supports a year query, month query, and all-years pagination. For all-years retrieval pagination is zero-based, begins at page=0, and returns up to 300 rows per page by default; increment until the entry collection is empty.

## Series semantics and known breaks
- Treasury describes par yields as interpolated constant-maturity yields derived from indicative bid-side quotations for recently auctioned Treasury securities, obtained by the Federal Reserve Bank of New York at or near 3:30 PM each business day. These are not transaction prices.
- Treasury changed its curve derivation method on 2021-12-06 from quasi-cubic Hermite spline (HS) to monotone convex spline (MC). The pre-change series remains official, but the methodology break must be represented in metadata and tested before cross-period factor use.
- The 1.5-month constant-maturity series began 2025-02-18; do not treat its earlier absence as missing-data failure.
- Treasury's current daily page exposed November 2026 observations through 2026-11-10 in the page snapshot reviewed for this audit. Do not infer publication completeness beyond the displayed records.

## Retrieval attempt and evidence boundary
- A direct XML retrieval was attempted from the documented official endpoint for year 2026 using the available execution environment.
- The request did not complete because the execution environment could not resolve home.treasury.gov (DNS/name-resolution failure). A separate container download attempt also failed.
- This is an execution-environment access failure only. It is NOT evidence of a Treasury server outage, endpoint rejection, or data unavailability.
- Browser-rendered official page content was discoverable, but no raw XML/CSV bytes were obtained in this work package.
- Consequently: raw archive acquisition = BLOCKED; raw SHA-256 = UNKNOWN; raw byte count = UNKNOWN; parsed row count = UNKNOWN; duplicate-date check = NOT RUN; date coverage reconciliation = NOT RUN; schema/type validation = NOT RUN.
- No HTML table transcription, synthetic records, inferred dates, or guessed response payload is accepted as raw data.

## Gate matrix
| Check | Status | Evidence / reason |
|---|---|---|
| Official publisher and series identity | PASS | Treasury interest-rate statistics and XML feed documentation |
| Documented endpoint and pagination contract | PASS | Official feed documentation |
| Historical availability start year | PASS | Official documentation states daily par yield curve available from 1990 |
| Methodology-break metadata captured | PASS | 2021-12-06 HS-to-MC change documented |
| Raw 2026 XML/CSV bytes acquired | BLOCKED | Execution environment DNS failure; no bytes received |
| Raw SHA-256 and immutable archive manifest | UNKNOWN | No raw bytes |
| XML schema/field validation | NOT RUN | No raw XML |
| Date uniqueness, coverage, and null semantics | NOT RUN | No raw XML |
| Historical factor/PIT suitability | UNKNOWN | Requires acquisition, date/time semantics review, and point-in-time validation |
| Factor efficacy / backtest acceptance | NOT RUN | Source qualification alone is not efficacy evidence |

## Exact next action
Retry the documented year-scoped XML request from a working network environment, preserve the exact response bytes and response metadata, calculate SHA-256 before parsing, then validate:
1. XML well-formedness and expected feed entry/property names;
2. unique observation date keys and chronological coverage;
3. explicit null/N/A semantics without filling values;
4. maturity columns and methodology-era flags;
5. reconciliation of the latest observation date against the official Treasury daily view;
6. immutable manifest with source URL, retrieval timestamp (actual only), HTTP metadata, byte count, SHA-256, parser version, and QA outcomes.

If the endpoint remains inaccessible, retain BLOCKED and use a user-supplied official export only after recording its provenance. Do not substitute FRED or a third-party mirror for the Treasury primary source without a separately approved source contract.

## Research spend and production safety
- Spend: ₹0.
- Paid APIs/services: none.
- External contact: none.
- Synthetic data: none.
- Production files or selector/ranking logic changed: no.
- Main branch modified or PR merged: no.
- Overall project progress: NOT CALCULABLE until the complete acceptance ledger and weights are reconciled.
