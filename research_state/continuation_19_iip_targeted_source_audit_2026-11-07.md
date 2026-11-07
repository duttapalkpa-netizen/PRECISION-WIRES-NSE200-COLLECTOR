# PRECISION-WIRES V11.3 — Continuation 19 targeted IIP source audit
Date: 2026-11-07
Page: গবেষণা যাচাই অব্যাহত 19

## Scope and no-repeat control
This is a targeted continuation of the unresolved April 2026 IIP native-source recovery. The continuation-18 PIB crosswalk, crosswalk QA, and source-discovery note were not recreated or modified.

## New verified official evidence
1. The official e-Sankhyiki IIP API page exposes the endpoint label GET /api/iip/getIIPData and links the OpenAPI document at ../../layout/swagger_user_iip.yaml. Browser retrieval of the YAML fails with HTTP/tool content-type limitation (application/octet-stream). Therefore the parameter schema, response fields, and valid monthly filters remain UNVERIFIED. Official API page: https://esankhyiki.mospi.gov.in/macroindicators?product=iip&tab=api
2. The official e-Sankhyiki catalogue currently indexes 4,784 entries and its latest IIP catalogue page shows August 2026 tables:
   - IIPMFY26020AUG: monthly use-based classification
   - IIPMFY26017AUG: annual NIC-2 digit/sectoral indices
   - IIPMFY26019AUG: annual use-based indices
   - IIPMFY26018AUG: monthly NIC-2 digit and sectoral indices
   Source: https://esankhyiki.mospi.gov.in/catalogue-main/catalogue
3. Exact official catalogue search for April 2026 table IDs did not return an indexed matching result. The existing legacy record IIPMFY26002APR remains HTTP 404 according to the previously committed audit. Do not infer a replacement ID from the August naming pattern.
4. Official MoSPI portal FAQ states that the IIP dissemination contains monthly indices and growth rates at sectoral, NIC 2-digit and use-based levels; item-group production and indices are provided through the micro-data catalogue to registered users. This distinction matters: the public catalogue workbook and restricted microdata should not be conflated. Source: https://mospi.gov.in/faq
5. Official PIB release 2278961 (29 June 2026) supersedes the 1 June WPI-based 2022-23 series with the Output-PPI-based series and says updated source-agency data from April 2022 onward were incorporated. Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3
6. Official e-Sankhyiki home page describes the current IIP base year as 2022-23 and says portal Macro Indicators datasets can be downloaded as CSV, while Catalogue datasets are downloadable as Excel. Source: https://esankhyiki.mospi.gov.in/

## Outcome
- Native April 2026 PPI-based MoSPI workbook: NOT RECOVERED.
- API schema/filters: NOT VERIFIED.
- Catalogue confirms a current monthly/annual table family, but does not identify the April 2026 PPI-based table ID or download URL from available indexed content.
- No guessed API parameters, URLs, table IDs, or data values were used.
- No data was downloaded, parsed, or promoted into the research dataset.
- IIP audit remains BLOCKED_WITH_GAPS; Hard Gate remains BLOCKED.

## Next bounded action
Continue through official e-Sankhyiki's user-facing metadata/table workflow to identify the April 2026 row and its current PPI-based table metadata. If the portal exposes only API data/CSV, record that as a distinct official source format; do not assert an XLSX exists unless the catalogue itself exposes it. Use exact filter values only after official metadata/API schema is readable. Capture the raw response, retrieval timestamp, URL, response headers/content type, row count, and SHA-256 before parsing.

## Progress accounting
- Official API route discovery: complete (endpoint path only).
- API schema and monthly filter verification: 0%.
- April 2026 current PPI native workbook/source recovery: 0%.
- IIP monthly ingestion count remains 39/41 = 95.1%; this is period ingestion coverage only, not audit completion.
- No defensible new overall research percentage calculated. Last recorded overall baseline remains 36%, not re-certified.
- Production selector, RANKING_SCORE, +1 PRESSURE_FADE, and CORE-672 remain untouched.
