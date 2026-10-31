# MoSPI API Contract & Release Metadata Audit — 2026-10-31

## Status
- Official portal documentation cross-check: PARTIAL PASS.
- CPI/IIP release-calendar metadata cross-check: PASS for the entries below.
- Authenticated live API smoke test: BLOCKED — repository credential availability has not been verified; no token was provided to the workflow.
- Actual JSON response schema / typed VALUE mapping: NOT VERIFIED.
- macro_indicators promotion: PROHIBITED; retain UNKNOWN/PARTIAL/BLOCKED as currently recorded.

## Critical IIP endpoint discrepancy
The official e-Sankhyiki IIP API page currently renders the endpoint as:
`GET /api/iip/getIIPData` (capital IIP in the operation name).

The community-maintained `nso-india/esankhyiki-mcp` mirror currently maps IIP to:
`GET /api/iip/getIipData` (mixed-case Iip).

These strings are not interchangeable assumptions. The official swagger asset could not be retrieved as readable text in this audit, and the live API response was not obtained. Therefore:
1. Treat the official portal's rendered path as the current primary documentation observation.
2. Treat the mirror path as secondary evidence only.
3. Do not hard-code either path into production until the official OpenAPI document and a minimal authenticated request confirm the exact route.
4. Capture the final URL, HTTP status, content type, sanitized response keys, response shape, request parameters and observation timestamp in a run artifact.

Official portal: https://esankhyiki.mospi.gov.in/macroindicators?product=iip&tab=api
Official API host documented by MoSPI: https://api.mospi.gov.in/
Secondary mirror: https://github.com/nso-india/esankhyiki-mcp

## Verified release metadata (calendar vs observed publication)
| Indicator | Reference period / release | Calendar date | Observed official publication | Audit interpretation |
|---|---|---:|---:|---|
| CPI | September 2026 | 12 Oct 2026 | MoSPI Latest Releases lists September CPI press release dated 12-10-2026 | RELEASED_AT can be populated from the press-release publication date; preserve source timezone/time only if the document provides it |
| IIP | September 2026 | 28 Oct 2026 | MoSPI Quick Links lists September 2026 IIP quick estimates dated 28 Oct 2026 | RELEASED_AT date corroborated; extract exact publication timestamp from the linked press note before storing a time |
| GDP | Q1 FY 2026-27 | 31 Aug 2026 | Advance Release Calendar lists Q1 FY27 quarterly GDP estimates on 31 Aug 2026 | Calendar date verified; retrieve the exact press release to verify actual publication and any revisions |
| GDP | Q2 FY 2026-27 | 30 Nov 2026 | Future scheduled date in 2026-27 Advance Release Calendar | SCHEDULED_AT only; must not be represented as RELEASED_AT |

Calendar caveat: MoSPI states release dates can change in exigencies and releases may move to the next working day on holidays. Store scheduled and observed timestamps separately.

## Seven-field feasibility
- DATE: derive only from the API's source reference-period field, after schema inspection.
- INDICATOR: use source-native indicator/category codes plus metadata name; do not infer from row text alone.
- VALUE: NOT VERIFIED until actual response schema and type/range checks pass.
- RELEASED_AT: CPI/IIP release dates above can be populated from official publication metadata at date precision; time-of-day remains unknown unless press note metadata proves it.
- SOURCE: MoSPI.
- SOURCE_URL: exact API/catalogue/press-release URL per observation.
- OBSERVED_AT_UTC: collector timestamp generated at retrieval time; never substitute for RELEASED_AT.

## Live-test prerequisite
A secret named `MOSPI_API_TOKEN` must be configured in GitHub Actions only if the official endpoint's current auth requirement is confirmed to require bearer auth. Never paste the token into chat, source files, artifacts, command output or logs. If the official endpoint supports public access, use the public access path instead; do not impose a token requirement based solely on an old/mirror OpenAPI copy.

## Next execution gate
Run one small request for a single IIP month after official path/auth confirmation, then inspect actual JSON keys and data types. In parallel, obtain CPI and GDP press-note URLs and exact publication timestamps. Validate non-empty rows, period parsing, indicator metadata join, numeric VALUE, duplicate key, pagination and revision/vintage. Attach sanitized raw response, schema report, QA output, run ID and SHA-256. Only then may the source status be reconsidered.

## Safety invariants
No changes to the production selector, RANKING_SCORE, +1 PRESSURE_FADE, 672 diagnostics, collector backbone or 200-session dataset. This audit is research evidence only; it does not promote macro_indicators or unblock V11.3.
