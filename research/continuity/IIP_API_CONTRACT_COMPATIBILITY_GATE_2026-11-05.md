# IIP API Contract Compatibility Gate — 2026-11-05

## Newly verified portal/API fact
The current official e-Sankhyiki IIP API page identifies API version 1.0.0, OpenAPI 3.0, operation `GET /api/iip/getIIPData`, and links its specification at `../../layout/swagger_user_iip.yaml`. Official portal page: https://esankhyiki.mospi.gov.in/macroindicators?product=iip&tab=api

## Why the previous contract audit needed a stricter gate
A separately inspected public GitHub mirror of the IIP Swagger contract described a different operation spelling/path (`/api/iip/getIipData`), legacy base-year enums (2011-12, 2004-05, 1993-94), and bearer authentication. That mirror is not the official source of truth and must not be used to configure calls to the current 2022-23 series.

## Script correction
`pipeline/audit_official_iip_api_contract.py` now:
- downloads the current official Swagger URL only;
- hashes and retains the exact raw YAML bytes;
- inventories IIP operations, parameter names/enums/defaults and declared security;
- requires an explicitly declared `getIIPData` operation AND an explicit `2022-23` base-year parameter before it returns `CONTRACT_COMPATIBLE_REVIEW_REQUIRED`;
- otherwise returns `BLOCKED_LEGACY_OR_INCOMPLETE_CONTRACT` and exits non-zero;
- never calls the data API and never assumes the token is optional.

## Official data series facts
- New IIP base 2022-23 detailed tables from April 2023 onwards are published on e-Sankhyiki: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2267531&lang=1&reg=3
- The current portal identifies the 2022-23 IIP series as the current series and gives the IIP macroindicator page: https://esankhyiki.mospi.gov.in/macroindicators?product=iip
- The PIB report release says linking factors are at General and sectoral levels; do not derive lower-level linking factors from NIC concordance.
- A later PIB release states the Output-PPI-based IIP release supersedes the earlier WPI-based 2022-23 series. The revision vintage must therefore be captured and kept distinct in the data model: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3

## Execution status
OFFICIAL_PORTAL_API_PAGE: VERIFIED
API_OPERATION_LABEL: GET /api/iip/getIIPData (portal-rendered documentation)
OFFICIAL_SWAGGER_RAW_BYTES_AND_SHA256: PENDING
OFFICIAL_SWAGGER_2022_23_PARAMETER_COMPATIBILITY: PENDING
DATA_API_CALL: NOT MADE
NEW_SERIES_DATA_INGESTION: PENDING
REVISION_VINTAGE_CAPTURE: REQUIRED
MASTER_HARD_GATE: BLOCKED

## Immediate next step
Run Actions > Official e-Sankhyiki IIP API Contract Audit on branch `fix/iip-41-vintage-audit-clean`. Review the raw Swagger and JSON. If the official contract does not explicitly expose 2022-23, do not call the legacy endpoint: use the portal's downloadable detailed IIP tables and record their exact metadata, vintage, source URL and raw-byte SHA-256 instead.

## Invariants
No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 or A/B/C/D/E logic changed. No synthetic observations, fabricated release times, unsupported source promotion, or Hard Gate relaxation.