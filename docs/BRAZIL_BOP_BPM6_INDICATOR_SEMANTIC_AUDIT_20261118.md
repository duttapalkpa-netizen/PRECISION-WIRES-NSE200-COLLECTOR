# Brazil BOP_BPM6 Indicator Semantic Audit — 2026-11-18

Checkpoint: Chapter 35, Part-1  
Branch: `research/global-capital-rotation-overlay-v1`  
Scope: research-only inspection of the Part-7 Brazil BCB SDMX-ML payload. No production integration.

## 1. Recovered artifact and independent byte checks

- Workflow Run ID: `44256602275` (reported successful in Part-7 evidence).
- Artifact ID: `14405348744`.
- Downloaded artifact: `part7_brazil_bop_raw_capture.zip`.
- ZIP size in this runtime: 832,358 bytes.
- Independently computed ZIP SHA-256: `608906789259365455bb02844a5fc11486c0e24ac62dd2fde6d9e44bbba40c24`.
- ZIP members: `capture_manifest.json`, `response.xml`.
- Manifest source URL: `https://www.bcb.gov.br/content/statistics/sddsdocuments/4%20External%20Sector/Ext%201%20IMF%20SDMX%20BOP%20BPM6.xml`.
- Manifest HTTP status: 200; Content-Type: text/xml; raw response byte length: 4,840,062; retrieved at `2026-11-18T07:09:07.318958+00:00` UTC; Last-Modified: `2026-10-26T11:44:11Z`.
- Manifest raw XML SHA-256: `3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c`.
- Independent XML parse: PASS.

## 2. Independently parsed structure facts

The XML is a StructureSpecificData message with dataflow reference `IMF:BOP_BPM6(1.0)`. Its 237 Series elements expose exactly these series-level attributes:

| Attribute | Observed value |
|---|---|
| DATA_DOMAIN | BOP6 (237/237) |
| REF_AREA | BR (237/237) |
| COUNTERPART_AREA | W1 (237/237) |
| FREQ | M (237/237) |
| UNIT_MULT | 6 (237/237) |
| TIME_FORMAT | P1M (237/237) |
| INDICATOR | 237 distinct codes |

Observed observations: 89,097. Each observation contains only `TIME_PERIOD` and `OBS_VALUE`; 237 distinct series keys; 0 duplicate series keys; period range 1995-01 to 2026-09. No series-level `UNIT_MEASURE`, explicit sign field, or observation-level `OBS_STATUS` / `CONF_STATUS` attribute was present in this payload.

The source is Brazil's BCB national SDMX dissemination payload. It is not an IMF global country panel and cannot be treated as an India series or a global EM aggregate.

## 3. Critical data-structure finding

Do **not** apply the 17-dimension global BOP DSD crosswalk directly to this payload as if all 17 dimensions appeared as XML attributes. This is the IMF BOP collection/compact design: the collection representation uses a single `INDICATOR` dimension to encode a combination of the more detailed global BOP concepts. The IMF SDMX Central Web Services Guide's BOP_BPM6 example identifies the dataflow as `IMF:BOP_BPM6(1.0)` and the collection data structure as `IMF:ECOFIN_DSD(1.0)`. The SDMX FMR representation-map explanation also documents the collapse of the global-use BOP dimensions into the collection `INDICATOR` dimension.

Therefore the correct next semantic work is:
1. Retrieve and archive the exact `IMF:ECOFIN_DSD(1.0)` used by the collection dataflow.
2. Retrieve the exact `CL_INDICATOR` codelist referenced by that DSD, including agency/version.
3. Retrieve the official representation/structure map that maps global BOP dimensions to each `INDICATOR` code, if published.
4. Compare the live dataflow's actual DSD reference and the Brazil payload's full header against those artefacts; the guide example alone is not proof of the live dataflow linkage.
5. Build a code-level semantic table for all 237 indicators; preserve unmapped codes as UNKNOWN.

Official references:
- IMF SDMX Central Web Services Guide: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- SDMX FMR representation-map explanation: https://fmrwiki.sdmx.io/12.5.0/information-model/SDMX-maintainables/RepresentationMap/
- IMF BOP Introductory Notes (November 2024), Annex I/II: https://data.imf.org/-/media/iData/External-Storage/Documents/D7E2CE23AF2340EFA7932CF6CD7DD11A/en/BOP-Introductory-Notes-as-of-November-2024.pdf
- IMF BOP dataset: https://data.imf.org/en/datasets/IMF.STA%3ABOP

## 4. Bounded semantic cross-check — not a 237-code mapping

The IMF November-2024 BOP Introductory Notes explicitly label the following standard-presentation codes:
- `BFP_BP6_USD`: Portfolio investment (functional category total).
- `BFPA_BP6_USD`: Net acquisition of financial assets under portfolio investment.
- `BFPAE_BP6_USD`: Equity and investment fund shares under portfolio-investment assets.
- `BFPAD_BP6_USD`: Debt securities under portfolio-investment assets.

The captured Brazil payload contains exact codes `BFP_BP6_USD`, `BFPA_BP6_USD`, and `BFPAD_BP6_USD`. These exact matches are a bounded cross-check against the IMF published code labels, not proof that all other similarly prefixed Brazil codes have the same meaning. The exact code `BFPAE_BP6_USD` was not observed; codes such as `BFPAEEO_BP6_USD` and `BFPAEIS_BP6_USD` must not be silently substituted for it.

The IMF source defines financial-account entries as net acquisition of financial assets and net incurrence of liabilities; increases in assets and increases in liabilities are positive, decreases negative. A positive asset acquisition is not automatically a capital inflow to Brazil. Keep asset and liability sides separate.

## 5. Explicitly not accepted

- No full 237-code semantic map has been produced.
- No live `ECOFIN_DSD`, `CL_INDICATOR`, representation map, or live dataflow-reference payload has been downloaded and archived in this checkpoint.
- No units beyond the observed `UNIT_MULT=6` have been accepted; `UNIT_MEASURE` is absent from the payload.
- No liability sign or net-flow transformation has been accepted from code prefixes alone.
- No aggregation, USD conversion, EM membership, or global-flow inference has been performed.
- No Brazil series has been admitted as an India/global-EM trading signal.

## 6. Status

| Gate | State |
|---|---|
| Part-7 artifact download and independent ZIP hash | PASS |
| Raw XML manifest SHA / HTTP / byte metadata | PASS (manifest evidence) |
| Independent XML parsing and 237/89,097 counts | PASS |
| Collection-vs-global DSD distinction identified | PASS (standards cross-check; live linkage pending) |
| Exact live dataflow-to-DSD reference | UNKNOWN |
| Exact `ECOFIN_DSD` and `CL_INDICATOR` capture | NOT_DONE |
| 237-code semantic mapping | NOT_DONE |
| Unit/sign/quality metadata acceptance | UNKNOWN |
| Portfolio-investment-only extraction | PARTIAL / NOT_ACCEPTED |
| India or global EM panel admission | NOT_AUTHORIZED |

Protected invariants unchanged: Production Selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 (56×12), Engines A–E. No merge or production integration.


## 7. Screenshot-vs-raw-byte discrepancy
The Chapter 34 Part-7 screenshot visually reports the raw XML size as 4,840,052 bytes. The downloaded artifact's `capture_manifest.json` reports 4,840,062 bytes, and the ZIP member's independently inspected uncompressed size is also 4,840,062 bytes; the independently computed raw XML SHA-256 matches the manifest. Record the screenshot value as a 10-byte display/evidence discrepancy, not as the accepted raw byte count. Accepted byte count for the downloaded artifact is 4,840,062; preserve the screenshot discrepancy for audit traceability.


## 8. Chapter 35 Part-2 — authoritative collection-DSD correction and workflow repair (2026-11-18)

### Standards evidence
The IMF SDMX Central Web Services Guide (last updated May 2025) explicitly shows the `IMF:BOP_BPM6(1.0)` dataflow example using `IMF:ECOFIN_DSD(1.0)` and describes ECOFIN as the six-dimension dissemination DSD. The IMF SDDS Plus Technical Implementation Guide specifies the six dimensions and identifies `INDICATOR` as a mixed dimension encoding economic concept, statistical adjustment and unit of measure. It identifies the associated codelist as IMF `CL_INDICATOR`. Sources and relevant guide locations:
- IMF SDMX Central Web Services Guide, PDF pages/lines 0–4 and its BOP_BPM6/ECOFIN example: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralWebServicesGuide.pdf
- IMF SDDS Plus Technical Implementation Guide, Section III, paragraphs 16–21 and Table 1: https://dsbb.imf.org/content/pdfs/SDDS%20Plus%20Technical%20Implementation%20Guide.pdf
- Live IMF SDMX Central DSD catalogue lists IMF:ECOFIN_DSD latest version 1.0: https://sdmxcentral.imf.org/data/datastructure.html

### Corrected interpretation
The prior workflow's assertion that `BOP_BPM6` must reference the global-use `IMF:BOP(2.6.0)` DSD was over-specific and contradicted by the official IMF collection/dissemination example. The global-use BOP DSD remains a separate standard and should not be confused with the ECOFIN collection DSD used by this BOP_BPM6 example. The prior generic BOP DSD capture remains useful as a separate metadata artefact; it is not the collection DSD for this six-dimension indicator encoding.

### Brazil payload recheck
Independent local re-read of the exact Part-7 XML confirms the dataflow Header reference is `IMF:BOP_BPM6(1.0)`; the dataset's `Structure` element exposes a local structure identifier `IMF_BOP_BPM6_1_0` and an ObsLevelDim namespace. It does not itself name the DSD maintainable reference. The payload still has 237 distinct `INDICATOR` values and 89,097 observations. A code-family inventory found nine codes beginning `BFP` / `BFPL`:
- `BFP_BP6_USD`, `BFPA_BP6_USD`, `BFPAD_BP6_USD`, `BFPAEEO_BP6_USD`, `BFPAEIS_BP6_USD`, `BFPL_BP6_USD`, `BFPLD_BP6_USD`, `BFPLEEO_BP6_USD`, `BFPLEIS_BP6_USD`.
This is a lexical candidate list only. Do not map these codes to specific instruments or directions from prefixes alone. The published standard-presentation code labels previously checked remain bounded evidence only.

### GitHub workflow repair
Updated `.github/workflows/imf_bop_dsd_acquisition.yml` on `research/global-capital-rotation-overlay-v1`:
- Dataflow QA now expects exactly `IMF:ECOFIN_DSD:1.0`, not `IMF:BOP:2.6.0`.
- Added an explicit raw acquisition request for the version-pinned ECOFIN DSD with `references=children`.
- Added XML parsing/inventory for DSD components, the INDICATOR dimension and the referenced `CL_INDICATOR` codelist, including all captured code IDs and labels.
- Added exact byte count and SHA-256 output for the captured ECOFIN metadata.
- Workflow still retains the separately version-pinned global BOP DSD request and the dataflow/constraint acquisitions.
- First workflow edit commit: `70b640f8d010d6145819ed5ec15cea1e49e364b9`.
- Shell-escaping correction commit: `83fd95e67c6f73f6f7405dd1f0758e92153c38da`.
- Final workflow blob SHA: `226daa294d329b501b19312eb94cec290f17e160`.
- Final workflow file re-fetched and inspected; corrected expected reference and new ECOFIN/CL_INDICATOR step are present.

### Runtime limitation and exact status
- A direct runtime GET attempt from the current container failed at DNS resolution (`curl: (6) Could not resolve host: sdmxcentral.imf.org`); it returned no HTTP response. This is an execution-environment failure, not evidence that the IMF endpoint is down.
- The available GitHub connector in this session has no workflow-dispatch action. The updated workflow is committed but has NOT been run. No new ECOFIN DSD bytes, metadata response headers, codelist rows, byte count or SHA-256 are claimed.
- The official guide is standards evidence for the six-dimension ECOFIN structure and the CL_INDICATOR association. It is not a substitute for the required version-pinned live XML acquisition.

### Gate state after Part-2
| Gate | State |
|---|---|
| IMF standard confirms ECOFIN dissemination DSD and CL_INDICATOR association | PASS (official documentation) |
| Brazil payload confirms BOP_BPM6 dataflow and 237 indicator codes | PASS (captured XML) |
| Existing workflow corrected to test ECOFIN_DSD 1.0 and acquire CL_INDICATOR | PASS (committed and re-fetched; static verification) |
| Live dataflow-to-ECOFIN_DSD reference | UNKNOWN pending workflow run |
| Raw ECOFIN_DSD and CL_INDICATOR capture + hashes | NOT_DONE |
| 237-code semantic mapping | NOT_DONE |
| Brazil portfolio investment subset accepted | NOT_ACCEPTED |
| India / global EM flow admission | NOT_AUTHORIZED |

No production integration or protected-selector change.
