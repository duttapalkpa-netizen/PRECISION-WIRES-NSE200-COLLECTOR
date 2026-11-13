# U.S. Treasury 2026 XML Retrieval Diagnostic — 2026-11-13

## Purpose
A narrow follow-on diagnostic to the existing Treasury source-contract record. This does not repeat source discovery and does not claim historical raw-data acquisition.

## Exact request attempted
Official Treasury endpoint documented by Treasury:
`https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026`

Treasury's own XML feed instructions document this endpoint structure, yearly retrieval, and the daily par yield curve availability from 1990. The endpoint contract is therefore official and documented.

## Retrieval observations
1. A browser retrieval attempt returned HTTP 400 with the message `Unsupported content-type: text/xml`. This is a limitation of the retrieval interface's supported content types; it is not evidence that Treasury returned a server-side error or that the endpoint is down.
2. A separate direct HTTPS retrieval attempt from the execution environment failed before an HTTP response with DNS resolution error: `Temporary failure in name resolution`.
3. No response body was received by either attempt. No XML bytes, record count, date range, or response headers were obtained.

## Evidence ledger
| Item | Status | Evidence |
|---|---|---|
| Official feed URL contract | PASS | Treasury XML feed documentation |
| 2026 year-specific request constructed exactly to documented pattern | PASS | URL recorded above |
| HTTP response received by execution environment | UNKNOWN | DNS failed before HTTP |
| Browser parser accepted XML response | FAIL (tool limitation only) | HTTP 400 Unsupported content-type text/xml |
| Raw XML body acquired | NOT ACQUIRED | No body returned |
| Raw byte count / SHA-256 | UNKNOWN | No bytes |
| 2026 record count / date coverage | UNKNOWN | No records inspected |
| XML schema / field validation | NOT STARTED | Requires raw XML |
| Daily market-session reconciliation | NOT STARTED | Requires parsed dates |

## Safe next action
Run the same documented URL from a network-enabled environment that supports XML responses, preserving response bytes unchanged. Capture retrieval timestamp (UTC and IST), status, content-type, byte count, and SHA-256 before parsing. Validate XML root/feed structure, entry count, dates, unique date keys, expected yield fields, null representation, and year boundary. Retain nulls as null; do not impute or infer. Compare any 2026 year-end/current-year completeness only against official Treasury publication schedule.

Do not silently switch to FRED, third-party mirrors, a different Treasury series, or CSV archives to claim this specific request succeeded. Such sources may be separately qualified if explicitly required.

## Gate decision
**RAW ACQUISITION BLOCKED / UNVERIFIED.** The official endpoint contract is confirmed, but raw XML bytes were not acquired. The two retrieval failures have different causes and neither proves Treasury-side unavailability.

## Invariants
₹0 spend; official free sources only; no synthetic rows or timestamps; UNKNOWN is neither PASS nor FAIL; no production selector, RANKING_SCORE, +1 PRESSURE_FADE, or CORE-672 changes; no PR merge. Research-only diagnostic.
