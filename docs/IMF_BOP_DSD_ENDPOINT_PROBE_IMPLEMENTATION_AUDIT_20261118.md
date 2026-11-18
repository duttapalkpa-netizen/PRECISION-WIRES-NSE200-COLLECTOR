# IMF BOP DSD Official Endpoint Probe — Implementation Status (2026-11-18)

## Objective
Resolve the existing IMF BOP DSD V2.6.0 raw-XML retrieval blocker without guessing a source route or treating a candidate URL as verified.

## Official-source findings
- IMF SDMX Central's official catalogue lists agency IMF, DSD ID BOP, version 2.6.0: https://sdmxcentral.imf.org/data/datastructure.html
- Its official web-service page documents the public structure-service entry point: https://sdmxcentral.imf.org/webservice/structure.html
- The repository extraction specification already documented a current structure route and a legacy route candidate. The current route was not accessible through the web retrieval layer; this is not an HTTP response and does not prove endpoint failure.
- No XML payload bytes, HTTP status, Content-Type, final URL, byte length, SHA-256, or parsed DSD component list were obtained during this implementation step.

## Bounded probe implementation
Added a small Python 3.12 script to test two exact candidate paths on the official host only:
1. Current documented structure path: `/sdmx/v2/structure/datastructure/IMF/BOP/2.6.0/`
2. Legacy public service path already recorded as a candidate in the repository's IMF extraction spec: `/ws/public/sdmxapi/rest/datastructure/IMF/BOP/2.6.0/`

For each route, the script records UTC retrieval time, HTTP status, final URL, Content-Type, byte length, SHA-256 and XML parse result; raw response bytes are retained when an HTTP response is received. The script is route-discovery only and downloads no BOP observations.

Files:
- `scripts/research/probe_imf_bop_dsd_endpoints.py` — commit `45850a0d04d4548d056f21bc22a2c1734eeb8d59`
- `.github/workflows/imf-bop-dsd-endpoint-probe.yml` — commit `7029fe9fbe00e8855c12c7629b84dd435677c6e6`
- Workflow timeout: 5 minutes; artifact retention: 90 days; workflow_dispatch plus active research-branch push trigger.

## Runtime status
- Script/workflow authored: PASS (source files committed).
- GitHub Actions check-run evidence for commits `45850a0d04d4548d056f21bc22a2c1734eeb8d59` and `7029fe9fbe00e8855c12c7629b84dd435677c6e6`: no check-run surfaced in the connected GitHub interface at audit time.
- Endpoint execution: NOT_VERIFIED / NOT_RUN from available run evidence.
- Raw XML response: NOT_RETRIEVED.
- DSD XML parsing/codelist mapping: UNKNOWN.
- BOP observation download, country panel and EM aggregation: NOT_DONE.

Do not claim this endpoint probe succeeded. Do not infer a failure status from the absence of a surfaced run record. Next unblocker is to obtain a real Actions run for workflow `IMF BOP DSD Official Endpoint Probe` and inspect its artifact/logs. If the workflow has not run, use repository Actions UI to run the workflow manually; no alternate guessed endpoints or third-party mirrors are accepted.

## Decision
IMF BOP DSD route remains UNKNOWN until the exact response is captured and validated. No country observations or EM aggregate were created. IMF BOP is annual/quarterly context, not a daily market trigger.

## Invariants
₹0 spend; official/free sources only; no synthetic values/timestamps, no guessed dimensions/signs/units; all unverified states remain UNKNOWN. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate and production workflows unchanged. No production integration.
