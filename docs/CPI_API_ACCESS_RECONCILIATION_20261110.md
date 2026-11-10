# MoSPI CPI API Access Reconciliation
Audit date: 2026-11-10 (Asia/Kolkata)
Repository scope: PRECISION-WIRES V11.3 research-only overlay
Branch: research/global-capital-rotation-overlay-v1

## Purpose
Establish whether India CPI is a lawful, free official macro-data candidate without confusing the current eSankhyiki API with the older MoSPI API platform.

## Verified official evidence
1. Current eSankhyiki CPI API documentation identifies OpenAPI 3.0.0, endpoint GET /api/cpi/getCPIData, and CPI base years 2010, 2012 and 2024.
2. The current eSankhyiki page describes paginated JSON responses with a statusCode flag and human-readable msg; bearer token is optional, guest requests are served, and requests are rate-limited per IP.
3. Current CPI catalogue results expose monthly 2024-base datasets, including July 2026 and August 2026 provisional releases, with table IDs and release dates. CPI is monthly and its vintage/provisional status must be retained.
4. The older MoSPI CPI API User Manual describes a different API platform (api.mospi.gov.in), signup/login, a 15-minute token, and a 10-record unauthenticated limit. It documents older endpoints /api/getCPIIndex and /api/getItemIndex.
5. These are distinct API generations/platforms. The older manual must not be applied to the current eSankhyiki endpoint; equally, the current page's guest-access statement must not be generalized to the legacy API.

## Gate decision
- Official current API route and advertised guest-access policy: VERIFIED at documentation level.
- Exact query parameter names/types, pagination cursor/page rules, schema field meanings, rate-limit thresholds, and full-history completeness: UNKNOWN until authoritative OpenAPI YAML or API metadata is retrieved and inspected.
- Raw CPI observations ingested and SHA-256 manifested in this task: NO.
- No API calls or credentials were attempted in this audit.
- CPI variable gate: SOURCE/API-DOCUMENTATION VERIFIED; OBSERVATION INGESTION NOT COMPLETE; production use BLOCKED pending schema, series selection, raw-response capture, and QA.

## Required acceptance tests before ingestion
1. Retrieve the official OpenAPI YAML/metadata from the exact link published on the current eSankhyiki CPI page; record HTTP status, content type, retrieval timestamp and SHA-256.
2. Parse schema and enumerate every required/optional parameter, response envelope, pagination mechanism, base-year selector and series dimension.
3. Use only documented public guest access and respect rate limits. Do not register, authenticate, or bypass access controls unless separately authorized and necessary under published terms.
4. Retrieve one narrowly scoped aggregate CPI sample only after schema validation; preserve raw bytes before parsing.
5. Validate returned rows against the matching catalogue workbook/table for same reference period, base year, geography, rural/urban/combined level and provisional/final vintage.
6. Report row counts, duplicate keys, missing periods, nulls, unit consistency and SHA-256. Do not combine 2012-base and 2024-base observations without an official linking method.

## Sources
- Current eSankhyiki CPI API documentation: https://esankhyiki.mospi.gov.in/macroindicators?product=cpi&tab=api
- Current eSankhyiki CPI catalogue: https://esankhyiki.mospi.gov.in/catalogue-main/catalogue?product=CPI
- Older MoSPI CPI API manual: https://api.mospi.gov.in/API/CPI%20API%20User%20Manual.pdf

## Project safety and progress
- Research-only. No changes to production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E, or Hard Gate.
- No paid API/feed, no synthetic observations, no unverified historical backfill.
- This source-access reconciliation is complete; it is not a data-ingestion pass.
- Milestone 6 remains 20% design/source mapping; observation ingestion remains 0% for this CPI work item.
- Overlay remains 62.5% (5/8); overall V11.3 remains NOT_CALCULABLE.
