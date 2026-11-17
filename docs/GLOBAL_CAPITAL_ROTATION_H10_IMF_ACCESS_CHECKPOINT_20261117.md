# Global Capital Rotation — official H.10 release XML route and IMF API access checkpoint
Date: 2026-11-17
Branch: research/global-capital-rotation-overlay-v1

## Scope
Bounded follow-up to the existing CDSL/H.10 and IMF BOP_AGG acquisition blockers. No source observations were downloaded or admitted.

## Federal Reserve H.10 — additional official route identified
- Official H.10 release landing page: https://www.federalreserve.gov/releases/h10/
- The release landing page explicitly lists an XML download link beside RSS, Data Download and FRED.
- Exact XML/ZIP URL resolved from that official link: https://www.federalreserve.gov/releases/h10/data/FRB_h10_xml.zip
- The browser fetch attempted the exact URL but rejected its binary `application/x-zip-compressed` content type. Therefore the route is VERIFIED_OFFICIAL / PINNED, but raw ZIP acquisition is NOT_DONE.
- This release-page XML route is distinct from the older DDP Output.aspx URL. Fed FAQ says the release landing-page XML will remain available after Build Your Package retirement; the XML is overwritten on each update and reflects the current/latest vintage, not an archived point-in-time vintage.
- Do not claim byte count, raw ZIP SHA-256, XML parse, series coverage, or point-in-time vintage capture. No H.10 indicator or gate advanced.
- H.10 broad dollar index remains distinct from ICE DXY. Do not splice the H.10 Jan-1997-base preview with FRED DTWEXBGS Jan-2006-base history without crosswalk and overlap QA.

## IMF — public API route distinction
- Official IMF API page states datasets are available through SDMX 2.1 and SDMX 3.0 APIs, but directs users to a Swagger page requiring a beta portal account sign-in.
- The BOP_AGG dataset page confirms annual BPM6 World/Country Group Aggregates and states that group aggregates combine reported data with estimates for nonreporting economies.
- A legacy IMF SDMX Central web-services guide (2019) documents a public GET endpoint at https://sdmxcentral.imf.org/ws/public/sdmxapi/rest for structures and data. However, no successful live response or BOP_AGG-to-legacy-dataflow mapping was demonstrated in this attempt. Do not assume BOP_AGG exists on that legacy service.
- Result: modern IMF API access for this dataset remains ACCESS_NOT_DEMONSTRATED anonymously; legacy public SDMX Central route is DOCUMENTED_BUT_UNVERIFIED for BOP_AGG. No IMF observations acquired; raw bytes, SHA-256, transaction series mapping, units/sign/vintage QA remain NOT_DONE/UNKNOWN.
- No third-party mirror, synthetic data, or inferred endpoint used.

## Acceptance status
- H.10 official landing-page XML route: PASS (route discovery only).
- H.10 raw ZIP acquisition and parsing: NOT_DONE.
- IMF modern API anonymous access: NOT_DEMONSTRATED.
- IMF legacy public SDMX Central BOP_AGG availability: UNKNOWN / NOT_VERIFIED.
- IMF raw observations and series mapping: NOT_DONE / UNKNOWN.
- Synchronized macro panel, relative-attraction calculation, event study and predictive validation: NOT_DONE.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A-E and Hard Gate: unchanged.
- PR #20: do not merge; remains open/draft/unmerged unless explicitly authorized.
