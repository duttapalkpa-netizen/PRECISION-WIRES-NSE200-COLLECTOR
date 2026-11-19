# GCR — IMF BOPS registry DSD-version and provider evidence audit
Date: 2026-11-19 (Asia/Kolkata)
Workstream: Global Capital Rotation & Relative-Attraction Overlay
Stage: Observation only
Status: REGISTRY METADATA REFINED; INDIA RAW DATA ROUTE STILL NOT VERIFIED

## 1. Purpose
Use the current IMF SDMX Central public registry pages to refine the prior candidate mapping and avoid two earlier errors: treating a visible first-page result as the complete registry, and treating national SDDS+ registrations as the IMF global BOP observation dataset.

## 2. Current official registry evidence
### 2.1 Data Structure Definition (DSD) catalogue
Official page: https://sdmxcentral.imf.org/data/datastructure.html
The current indexed catalogue explicitly lists:
- Agency: IMF
- ID: BOP
- Name: Balance of Payments and International Investment Position
- Latest Version: 2.6.0
It also lists older IMF:BOP versions from 1.1 through 2.5.0, plus IMF:ECOFIN_DSD 1.0 and a UAE-specific BOP DSD. The current catalogue output therefore confirms BOP 2.6.0 as the listed latest version, but the detail panel did not expose its component payload or dataflow links in the browser text view.

The DSD page's visible detail interface identifies fields that need inspection: Dataflows, Data Providers, Period, Dimensions, Measures, Dataset Attributes, Series Attributes, Observation Attributes and Group Attributes. The static text rendering does not populate their values.

### 2.2 Registrations catalogue
Official page: https://sdmxcentral.imf.org/data/registrations.html
The current indexed output shows national SDDS+ registrations, including:
- IMF:BOP6(1.0), provider IMF:BR1, registered BCB URL, last updated 2026-10-26T11:47:29Z.
- IMF:BOP6(1.0), provider IMF:CL2, registered Chilean central-bank URL, last updated 2026-10-07T12:01:02Z.
- IMF:BOP_BPM6(1.0), provider IMF:AT2, registered OeNB URL, last updated 2026-09-30T09:23:34Z.
- IMF:BOP_BPM6(1.0), provider IMF:JP4, registered Japanese Ministry of Finance URL, last updated 2026-10-08T00:48:39Z.
- IMF:BOP_GBPM6 registrations for multiple national providers, with differing versions (1.0 through 2.0 and later).
These entries establish national provider XML registration routes. They are not the global IMF STA BOP dissemination dataset, and a national XML may use a related but distinct structure version/payload.

No India-specific BOP registration was visible in the search output. The page is a dynamic/paginated catalogue and no validated exhaustive query or complete export was obtained. Therefore India registration presence/absence remains UNKNOWN; do not report “India has no registration”.

### 2.3 Reporting Constraints
Official page: https://sdmxcentral.imf.org/data/constraints.html
The public indexed listing explicitly shows:
- IMF:BOP6_CONSTRAINT → Dataflow BOP6[1.0]
- IMF:BOP_BP6_CONSTRAINT → Dataflow BOP_BPM6[1.0]
- IMF:BOP5_CONSTRAINT → Dataflow BOP5_COLLECTION[1.0]
These are registry identities only. The page's static opened rendering shows the constraint table as a dynamic selection interface and does not render selected cube-region values or codelist members. Do not infer allowable countries, frequencies, counterpart areas or items from the constraint IDs alone.

## 3. Direct structure endpoint test
Attempted browser retrieval of:
- https://sdmxcentral.imf.org/sdmx/v2/dataflow/IMF/BOP6/1.0?references=all
- https://sdmxcentral.imf.org/sdmx/v2/dataflow/IMF/BOP_BPM6/1.0?references=all
- https://sdmxcentral.imf.org/sdmx/v2/datastructure/IMF/BOP/2.6.0?references=all
All three returned an internal/accessibility error in the research browser. This is a tool retrieval failure, not an HTTP status from the IMF server and not proof that the API is down or authentication-gated. No API response bytes or HTTP headers were captured.

## 4. Consequence for India quarterly BOP series
The evidence currently supports only:
- IMF registry contains a current BOP DSD catalogue entry (latest listed 2.6.0).
- IMF registry contains BPM6-family national dataflow registrations and two legacy IMF BPM6 dataflow/constraint candidates.
- National registrations exist for Brazil, Chile, Austria, Japan and other countries.
It does not support:
- exact global STA BOP dataflow-to-DSD relationship;
- India-specific dataflow or provider registration;
- India REF_AREA code in the relevant DSD;
- current quarterly frequency key or dimension order;
- gross inflow, gross FPI, net capital flow item codes;
- unit multipliers, sign conventions, status/revision flags;
- public access to India observations or reproduction of RBI paper's source vintage.

## 5. Acceptance matrix
| Gate | Status | Evidence |
|---|---|---|
| IMF:BOP latest listed DSD version | PASS (catalogue listing) | Current catalogue shows 2.6.0 |
| DSD component/dimension payload | NOT_DONE | Dynamic detail values not rendered |
| BOP6 and BOP_BPM6 constraint target IDs | PASS (registry identity only) | Indexed constraint listing |
| Constraint cube-region members | NOT_DONE | Dynamic values not rendered |
| National BPM6 registration examples | PASS | Current registration listing |
| Exhaustive India registration lookup | UNKNOWN | No validated complete query/export |
| Global STA BOP dataflow relationship | UNKNOWN | No dataflow-to-DSD payload |
| India item codes / units / signs | NOT_DONE | No DSD/codelist payload |
| IMF India quarterly observations | NOT_ACQUIRED | No data query |
| Independent sudden-stop replication | NOT_DONE | Raw validated series absent |

## 6. Decisions and invariants
- National SDDS+ registrations must not be conflated with IMF global BOP dataset.
- Do not equate BOP6, BOP_BPM6, BOP_GBPM6 or BOP DSD merely because names are similar.
- Do not infer India absence from an incomplete visible listing.
- Browser internal errors are recorded as tool-access failures, not server HTTP failures.
- Observation remains OPEN; Planning/Organizing remain NOT_STARTED.
- ₹0 spend; official/free sources only; no guessed codes, units, signs, keys or transformations.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E and IPO-PLX V2 unchanged.
- UNKNOWN is never PASS. GCR NOT COMPLETE; aggregate/production admission NOT_AUTHORIZED.

## 7. Next highest-value action
Use the official IMF SDMX Central interactive Data Structure / Dataflow / Registration pages to export the current IMF:BOP 2.6.0 DSD and BOP6/BOP_BPM6 dataflow structures (including references and codelists), if the public UI permits export without login. If export requires login or cannot expose the component payload, stop and document that boundary; do not infer a query key. In parallel, a separate RBI Table 42 national-source route can be mapped only as a clearly distinct cross-check.
