# PRECISION-WIRES V11.3 — IIP native source discovery note
Date: 2026-11-07
Continuation: গবেষণা যাচাই অব্যাহত 18

## Purpose
Continue the unresolved April 2026 IIP native MoSPI source recovery without repeating the already completed PIB crosswalk.

## New official-source findings
1. MoSPI/e-Sankhyiki catalogue and IIP macro-indicator pages are the official entry points:
   - https://esankhyiki.mospi.gov.in/catalogue-main/catalogue
   - https://esankhyiki.mospi.gov.in/macroindicators?product=iip
2. The official e-Sankhyiki IIP API tab is discoverable at:
   - https://esankhyiki.mospi.gov.in/macroindicators?product=iip&tab=api
   - It advertises GET /api/iip/getIIPData.
   - The linked OpenAPI file is /layout/swagger_user_iip.yaml, but this retrieval attempt returned an unsupported application/octet-stream content-type; no parameter schema was verified.
3. PIB release PRID=2278961, posted 2026-06-29, explicitly says MoSPI revised the entire IIP 2022-23 series using Output PPI, superseding the earlier WPI-based series released 2026-06-01. It also says updated source-agency data from April 2022 onward were incorporated. Therefore, the 2026-06-01 April 2026 PIB crosswalk is supplemental historical evidence only and must not be treated as the current PPI-based series.
   Official URL: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2278961&lang=1&reg=3
4. Official MoSPI catalogue search surfaced the current IIP monthly dataset family and table IDs through August 2026, including IIPMFY26018AUG (monthly NIC-2 digit and sectoral), IIPMFY26020AUG (monthly use-based), and IIPMFY26017AUG / IIPMFY26019AUG (annual tables). This confirms that the current catalogue is active, but does not by itself identify the exact April 2026 PPI-based XLSX URL.
5. Official PIB's 2026-06-01 release points to detailed data in e-Sankhyiki and contains the initial April 2026 new-series statements. It is not the superseding PPI vintage.
6. The catalogue and macroindicator pages are client-rendered and returned no readable page lines in the browser inspection. Exact April 2026 PPI workbook filename/download URL remains unverified.

## Important source-quality distinction
- Official PIB evidence establishes that the PPI-based IIP series supersedes the initial WPI-based series.
- The 36-row PIB crosswalk already committed in continuation 18 remains supplemental evidence for the original 2026-06-01 publication only. Do not overwrite it or silently relabel it as PPI-based.
- Do not infer workbook names, table IDs, file paths, query parameters, or API responses.
- Do not use third-party code or documentation as a substitute for official MoSPI source evidence. Any third-party API clues are navigation hints only.

## Status after this discovery
- Native MoSPI April 2026 PPI-based XLSX provenance: UNRESOLVED.
- Official e-Sankhyiki IIP API route discovered; endpoint parameter schema and response not yet verified.
- No dataset was downloaded or parsed in this step.
- IIP audit remains BLOCKED_WITH_GAPS; Hard Gate remains BLOCKED.
- Previously completed PIB crosswalk, its QA, and continuation-18 checkpoint remain unchanged.

## Next bounded task
Use the official portal's API metadata/OpenAPI route to obtain verified filter definitions and query the April 2026 monthly record only if the official schema confirms the exact parameters and base-year coverage. Otherwise continue targeted catalogue lookup. Preserve the result as a distinct PPI-based evidence artifact; never substitute the June 1 PIB crosswalk.
