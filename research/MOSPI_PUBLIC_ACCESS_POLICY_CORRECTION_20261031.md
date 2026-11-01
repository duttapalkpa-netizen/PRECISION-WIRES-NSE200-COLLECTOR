# MoSPI Public Access Correction — 2026-10-31

## Decision
Do not ask the user for an API token for MoSPI Category A aggregate/open-access statistics. MoSPI's current FAQ explicitly classifies aggregated CPI and IIP at NIC 2-digit level and National Accounts publications as Category A Open Access, free of cost and available without registration. e-Sankhyiki FAQ also states registration is not required and the Macro Indicators module provides CSV downloads.

Official evidence:
- MoSPI data dissemination FAQ: https://mospi.gov.in/faq
- e-Sankhyiki public access and download FAQ: https://esankhyiki.mospi.gov.in/
- Official IIP Macro Indicators/API page: https://esankhyiki.mospi.gov.in/macroindicators?product=iip&tab=api
- PIB description of e-Sankhyiki download and API modules: https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2029708&lang=2&reg=48

## Important boundary
Open access to the published aggregate dataset does not prove that every API route is unauthenticated. The portal supports CSV downloads; use the public download route first for Category A data. Do not infer API authentication from a Swagger Authorize button, and do not require a bearer token unless the official endpoint returns an authentication challenge or its current official contract explicitly requires it.

Category B item-level IIP/CPI and unit-level microdata are a separate registered-access category. They are not required for the current aggregate macro_indicators task and must not be fetched or treated as open access.

## Collector implementation requirements
1. Discover the public CSV download URL through the official e-Sankhyiki product page and selected filters; record the exact final URL.
2. Fetch a bounded aggregate IIP/CPI/GDP extract with no credentials.
3. Store raw response bytes, response content type, final URL, retrieval timestamp UTC and SHA-256.
4. Parse schema from the actual file; do not assume column names.
5. Normalize source reference period to DATE, source indicator code/name to INDICATOR, numeric observation to VALUE, and preserve UNIT/FREQUENCY/BASE_YEAR/GEOGRAPHY where present.
6. Populate RELEASED_AT only from an official release notice/calendar; if only a date is verified, store date precision and leave time null.
7. Run non-empty, schema, type, duplicate-key, unit, frequency, period, revision and provenance QA.
8. Keep macro_indicators unpromoted until an artifact proves all gates.

## Current validation status
- Public access policy for aggregate Category A data: VERIFIED from official MoSPI FAQ.
- Public CSV facility: VERIFIED from official e-Sankhyiki FAQ.
- Exact selected IIP CSV download URL and response schema: NOT YET CAPTURED.
- Unauthenticated live download smoke test: NOT YET RUN.
- Domain QA and factor coverage promotion: NOT APPROVED.

No production selector, RANKING_SCORE, +1 PRESSURE_FADE, 672 diagnostics, collector backbone or 200-session dataset changes are authorized by this correction.
