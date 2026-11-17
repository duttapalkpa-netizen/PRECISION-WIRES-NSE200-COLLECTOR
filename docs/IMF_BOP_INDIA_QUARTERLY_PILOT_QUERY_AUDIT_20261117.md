# Chapter 34 — India Quarterly BOP Pilot: Query-Contract Audit
Date: 2026-11-17 (Asia/Kolkata)
Branch: `research/ch34-india-bop-pilot-query-audit-20261117`
Base: `acbac5fcf12bb403ca4545578989cddde5b2418a`
Scope: research-only; bounded metadata/query audit. No observations acquired in this checkpoint.

## 1. Previously accepted evidence — reused, not repeated
- IMF BOP metadata acquisition: PASS, Run `44095286184`.
- Crosswalk QA: PASS, Run `44096119287`.
- Four raw XML response bodies and HTTP provenance are archived in `evidence/imf_bop_dsd/20261117T134325Z/`.
- Raw manifest SHA-256: `e029afe097cb5267113663eb0a40b0c1990290c9ff8c1bf1c0469a080d6331fb`.
- Actual dataflow reference is `IMF:BOP_BPM6:1.0 -> IMF:ECOFIN_DSD:1.0`; it is not `IMF:BOP:2.6.0`. Do not collapse these DSDs.
- Constraint: `DATA_DOMAIN=BOP6`, `COUNTERPART_AREA=W1`; 98 allowed indicators.
- Portfolio candidates permitted by the captured constraint include `BFPA_BP6_USD` (net acquisition of financial assets) and `BFPL_BP6_USD` (net incurrence of liabilities). `BFP_BP6_USD` is not permitted by that constraint.

## 2. New finding: exact ECOFIN_DSD dimension order
Parsed directly from the archived `IMF:ECOFIN_DSD:1.0` XML (raw response SHA-256 above):
1. `DATA_DOMAIN` — position 1
2. `REF_AREA` — position 2
3. `INDICATOR` — position 3
4. `COUNTERPART_AREA` — position 4
5. `FREQ` — position 5
6. `TIME_PERIOD` — position 6 (time dimension)

The first five dimensions form the series key; `TIME_PERIOD` is the observation time dimension. Therefore any SDMX 2.1 key must follow this order, not the legacy IMF BOP DSD order and not an assumed country-first key. This finding establishes the dimension order only; it does not establish the public observation endpoint or prove a successful query.

## 3. Attributes that must be retained
- `UNIT_MULT`: mandatory; preserve the source multiplier exactly.
- `OBS_STATUS`: conditional observation attribute; preserve exact code and resolve through the referenced IMF codelist.
- `COMMENT`: conditional attribute; retain if supplied.
- `BASE_PER`: conditional series attribute; retain if supplied.
- `TIME_FORMAT`: conditional series attribute; retain if supplied.
- `OBS_VALUE`: primary measure.
- No standalone actual/estimate dimension is established by the inspected component excerpt. Actual/estimate status must not be inferred from a label; inspect all returned attributes/annotations and the portal's official metadata before assigning it.

## 4. Bounded India pilot request contract — not yet executed
Target series:
- `BOP6.IN.<BFPA_BP6_USD>.W1.Q` — key template only; do not execute until the captured `CL_REF_AREA` confirms the India code and the official data API endpoint/SDMX version and key syntax are established.
- `BOP6.IN.<BFPL_BP6_USD>.W1.Q` — same restriction.

The literal `IN` above is a provisional ISO-style candidate, not an accepted IMF codelist value. Replace it only with the exact `CL_REF_AREA` value from the archived ECOFIN DSD codelist. No query URL is authored in this checkpoint because the IMF Data Portal documents SDMX 2.1/3.0 APIs but directs users to a Swagger explorer requiring beta-portal sign-in; the SDMX Central service verified here is a structure service, not proof of an anonymous observation endpoint.

Before execution, establish and archive:
1. Official observation API base URL, SDMX version, request path/key syntax, and whether public GET access works without credentials.
2. Exact India `REF_AREA` code and `FREQ=Q` code from the referenced codelists.
3. One bounded request for the two allowed USD indicators, quarterly frequency, world counterpart `W1`, and a limited period range.
4. Untouched response bytes, request and final URL, HTTP status, Content-Type, retrieval UTC, byte length, SHA-256, and response metadata.
5. Returned `UNIT_MULT`, `OBS_STATUS`, `COMMENT`, `BASE_PER`, `TIME_FORMAT`, all available vintage/revision attributes, and exact periods/values.
6. Independent reconciliation of the two directions and source units; never treat BFPL as equity-only FPI or as gross inflows.

## 5. Status — Chapter 34 work-package only
| Work package | Progress | Status |
|---|---:|---|
| Prior IMF structure capture | 100% | PASS — reused |
| Portfolio semantic candidate crosswalk | 100% | PASS — reused |
| ECOFIN_DSD exact dimension order | 100% | PASS — newly audited |
| India REF_AREA codelist value confirmation | 0% | NOT_DONE |
| Public observation endpoint/query contract | 0% | UNKNOWN / NOT_DONE |
| India quarterly BFPA/BFPL observation pilot | 0% | NOT_DONE |
| Actual/estimate, reporter coverage and vintage/PIT gate | 0% | NOT_DONE |
| EM aggregation eligibility | 0% | NOT_DONE |

## 6. Rejected / excluded
- Reusing `IMF:BOP:2.6.0` key order for the BOP_BPM6 dataflow.
- Guessing the India area code or a public observation URL.
- Using `BFP_BP6_USD`, which is not allowed by the captured constraint.
- Combining assets and liabilities into one net-flow figure.
- Treating metadata acquisition or a successful structure query as observation access.
- Treating quarterly BOP as a 1–3 day trigger.

## 7. Hard invariants
₹0 spend; official/free sources only; no credentials, paid APIs, synthetic observations, fabricated timestamps, forward-fill or inferred country eligibility. UNKNOWN remains UNKNOWN. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate, parser admission and production workflows remain untouched. No PR merge or production integration.

## 8. Source references
- IMF API page: https://data.imf.org/en/Resource-Pages/IMF-API (SDMX 2.1/3.0; Swagger beta-account sign-in note).
- IMF SDMX Central Web Services Guide (May 2025): https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf (structure service scope and ECOFIN DSD examples).
- Canonical prior capture commit: `bd2a7d123b949f4ffcc426608a36de706a8fd658`.
- Canonical prior crosswalk QA commit: `62e0e4132b9567bc4e8cd6ff82a7e3e9d8536dfc`.
- Prior Chapter 34 ledger commit: `acbac5fcf12bb403ca4545578989cddde5b2418a`.
