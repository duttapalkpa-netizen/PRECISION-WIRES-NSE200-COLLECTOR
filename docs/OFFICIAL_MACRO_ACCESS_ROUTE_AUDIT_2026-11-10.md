# Official Macro Data Access Route Audit — 2026-11-10
Branch: research/global-capital-rotation-overlay-v1
Purpose: Incremental access-policy/route evidence for Milestone 6. This is not a data-ingestion run.

## Evidence reviewed

### IMF SDMX Central vs IMF Data Portal
- Official IMF SDMX Central REST entry point is documented as `https://sdmxcentral.imf.org/sdmx/v2/`.
- Official SDMX Central page exposes structure/dataflow navigation and documents web services for querying structures and data. Public-facing documentation is visible without sign-in.
- IMF Data API page states SDMX 2.1 and 3.0 APIs are available, but the Swagger explorer requires a beta portal account.
- Therefore:
  - SDMX Central public structure metadata route: SOURCE/ROUTE DOCUMENTED.
  - IMF Data Portal observation endpoint and BOP dataflow key: UNKNOWN until a public documented data query is identified and a real response is retrieved.
  - No login bypass, credential guessing, or account circumvention attempted.
  - Existing IMF BOP DSD V2.6.0 XML/XSD validation remains valid and is not repeated here.
- Important: a dataflow named `BPM6_BOP_Q` under agency `ESTAT` is Eurostat, not proof of an IMF BOP dissemination dataflow. Do not promote it.

### RBI DBIE/CIMS transition
- RBI's official Reporting Portals page (last updated 2026-11-09) lists CIMS DRM at `https://sankalan.rbi.org.in` and CIMS Common Login at `https://cims.rbi.org.in`.
- The same official page says existing XBRL, DBIE and SAARC portals will be discontinued once the complete CIMS project goes live.
- Consequence: do not hard-code legacy DBIE as a permanent route. Treat CIMS as a candidate portal, not an open observation API.
- CIMS access requirements and downloadable public macro series are not established by the portal listing alone. No login-only route was bypassed.
- RBI public reporting portal page is an official source register, not a validated observation payload.

### MoSPI / eSankhyiki
- Official eSankhyiki catalogue reports more than 4,700 datasets and lists CPI, IIP and National Accounts dataset families.
- Official eSankhyiki IIP API page exposes an OpenAPI/Swagger description for `GET /api/iip/getIIPData`; the page notes its Swagger UI preview returns only the first 10 records.
- MoSPI FAQ describes aggregated National Accounts, CPI and IIP at NIC 2-digit level as Category A Open Access, free without registration. It distinguishes registered-access microdata (free for non-commercial use, priced for commercial use) and restricted data requiring authorization.
- Consequence: use public aggregated datasets/API only; do not assume item-level or unit-level microdata is open. API route documentation is not proof of a complete historical download.
- IIP API operation parameters, pagination, date coverage, rate limits, terms and full response schema still need direct inspection before ingestion. CPI/GDP routes need their own series-level checks.

## Gate decisions

| Source / route | Official route evidence | Public/free status | Observation retrieval | Gate |
|---|---|---|---|---|
| IMF SDMX Central structure service | Documented | Public documentation visible; exact data query not yet tested | No BOP observations | PARTIAL / UNKNOWN |
| IMF Data Portal API explorer | Official API page confirms SDMX 2.1/3.0; Swagger sign-in stated | API access terms/anonymous query not established | No BOP observations | UNKNOWN / BLOCKED pending authorized route |
| RBI legacy DBIE | Official transition warning | Long-term route not reliable | No fresh observations in this audit | DEPRECATE AS PERMANENT ROUTE |
| RBI CIMS portals | Officially listed | Public data access not established by listing | No observations | UNKNOWN |
| MoSPI eSankhyiki catalogue | Official catalogue | Aggregated public catalogue documented | Dataset inventory only | SOURCE VERIFIED |
| MoSPI IIP API docs | Official OpenAPI/Swagger page | Public docs visible; operational terms and pagination not yet validated | No complete raw response archived | ROUTE DOCUMENTED / OBSERVATION UNKNOWN |
| MoSPI aggregated CPI/NAS/IIP | Official FAQ says Category A free/no registration | Free public aggregated data | No new raw observations ingested in this audit | SOURCE POLICY VERIFIED |

## Reproducibility / safety
- No synthetic observations, invented timestamps, guessed dataflow IDs or inferred API parameters.
- No paid sources, paid services, external contact, credentials, or authorization bypass.
- No raw observation was downloaded in this audit; therefore no observation SHA-256, row count, parser QA or vintage PASS is claimed.
- The previous matrix and prior PASS artifacts remain unchanged.
- No production code, selector, ranking score, pressure-fade, CORE-672, engines, or hard gate was modified.

## Progress accounting
- This audit task: 100% complete as a source-policy/route evidence addendum; not a data-ingestion task.
- Milestone 6: retain 20% design/source mapping; raw observation ingestion remains 0%.
- Overlay: retain 62.5% (5/8); no milestone promotion.
- Overall PRECISION-WIRES V11.3: NOT_CALCULABLE pending reconciled acceptance denominator and gates.

## Next non-duplicate action
Inspect the public OpenAPI schema and authorized query requirements for MoSPI IIP; identify the official CPI/NAS public dataset download route; separately test IMF SDMX Central documented public structure/data endpoints without authentication bypass. For RBI, verify whether CIMS has a public statistical-data dissemination route; if not, retain UNKNOWN and use any still-valid official RBI public statistical publication/archive. Store raw response bytes and hashes before parsing.
