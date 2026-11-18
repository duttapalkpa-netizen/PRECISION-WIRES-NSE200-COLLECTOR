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



## 9. Chapter 35 Part-3 — fail-closed IMF indicator code-list gate (2026-11-18)

### Official IMF validation rule added
The IMF SDMX Central User Guide (last updated May 2025), Section 2.2, lines 181–196, documents two ECOFIN-specific checks:
- An indicator absent from IMF:CL_INDICATOR fails when it also does not begin with the reporting country's three-letter ISO code.
- An indicator absent from CL_INDICATOR but beginning with that three-letter country code is a warning (country-specific indicator), not a standard IMF codelist match.
The same guide describes Valid Representation as checking reported dimension values against the DSD representation. Official source: https://dsbb.imf.org/content/pdfs/IMFSDMXCentralUserGuide.pdf (Section 2.2, pp. 5–6).

### New reusable QA implementation
Added `qa/audit_brazil_bop_indicator_codes.py`:
- Validates the exact `IMF:ECOFIN_DSD:1.0` structure.
- Requires exactly one `INDICATOR` dimension whose representation references `IMF:CL_INDICATOR:1.0`.
- Validates the codelist agency, ID, version, non-empty code inventory and duplicate IDs.
- Parses Brazil's actual StructureSpecificData header namespace for `Dataflow=IMF:BOP_BPM6(1.0)`; this parser shape is based on the recovered BCB payload, which does not emit a separate Dataflow element.
- Requires all series to have `REF_AREA=BR` and a non-empty `INDICATOR`.
- Classifies each observed code as official CL_INDICATOR match, Brazil ISO3-prefixed country-specific warning, or fail/quarantine.
- Keeps country-specific warning codes semantically UNKNOWN when no official IMF label exists. Official codelist matches also require further economic semantic review.
- Explicitly blocks portfolio-flow, global EM aggregate and trading-signal admission. Code-list compliance alone cannot establish transaction direction, unit, sign, observation quality or vintage.

Added `tests/test_brazil_bop_indicator_codes.py` with four regression cases: official-vs-country-specific distinction; unlisted non-country-prefixed code fail-closed; wrong codelist identity; wrong dataflow identity. These tests are wired into the GitHub Actions workflow. No workflow execution is claimed yet.

### Actual prior Brazil payload parser check
The previously archived Part-7 BCB XML was re-read locally. Exact observed values remain: dataflow `IMF:BOP_BPM6(1.0)`, REF_AREA `BR`, 237 Series, 237 unique INDICATOR codes, 89,097 observations. The nine BFP/BFPL-prefixed codes remain lexical candidates only; they are not semantically classified from prefixes. This is a re-parse of the existing archived bytes, not a new upstream capture.

### Workflow integration
Updated `.github/workflows/imf_bop_dsd_acquisition.yml`:
- Added repository checkout.
- Added the unit-test step for the new QA gate.
- Extended the job timeout to 8 minutes (within the project's under-10-minute run constraint).
- Retains version-pinned ECOFIN DSD + referenced codelist acquisition.
- Acquires the current official BCB Brazil BOP XML as a paired payload, recording request URL, response headers, transfer metadata, request-start and completion timestamps, raw byte count and SHA-256.
- Runs the code-list audit against the captured BCB XML and the ECOFIN DSD/codelist response; output is retained in the workflow artifact.
- Final workflow commit: `9a17d6fd0144708ffee152d4af233945dfee98bf`.
- Final workflow blob SHA: `c5caacbe917d16d108f74bc28047aa60ff89c5e0`.
- QA script commit: `1924fc0c1290435ed9db5a76168bf0b2b6f95e66`; fetched blob SHA: `b2dbb6b9a63b02c57293f316fc5218fe743161fa`.
- Test commit: `0516defffc320cb26c5acc98745c9d3fb265330c`; fetched blob SHA: `42f8e83fc9ed13f9683a9bfab698fbd98b9809e9`.
- Static re-fetch verification: checkout, test step, 8-minute timeout, BCB URL, audit invocation, ECOFIN request and CL_INDICATOR checks all present.

### Runtime status and guardrails
The GitHub workflow has not been dispatched in this session. Therefore the newly added committed tests have not yet been executed by GitHub Actions, and no live ECOFIN codelist or paired current BCB payload has been acquired by this workflow. The previous Part-7 artifact remains the only raw Brazil capture currently evidenced. No 237-code crosswalk is claimed complete. No code is admitted to the Brazil portfolio-flow panel, global EM aggregate or trading signal.

| Gate | State |
|---|---|
| IMF ECOFIN country-specific indicator validation rule documented | PASS (official IMF guide) |
| New fail-closed code-list audit implementation committed | PASS (static re-fetch) |
| Four regression tests committed and wired into workflow | PASS (static re-fetch; runtime NOT_DONE) |
| Existing Brazil raw XML re-parse: 237 series / 89,097 observations | PASS (archived payload) |
| Live ECOFIN DSD/CL_INDICATOR capture | NOT_DONE |
| Actual 237-code vs official codelist comparison | NOT_DONE |
| Economic semantic classification of portfolio codes | NOT_DONE |
| Brazil flow panel / global EM aggregate / trading signal admission | NOT_AUTHORIZED |

No production integration or protected selector changes.


### Artifact retention path correction — 2026-11-18
Final workflow review caught that the artifact upload initially included only `evidence/imf_bop_dsd/`, omitting the paired BCB payload and code-audit report. Corrected the upload-artifact path to include both `evidence/imf_bop_dsd/` and `evidence/brazil_bop/`. Correction commit: `9b793dfc10476dcd83d272e8a36275c8bd978b2b`; workflow blob SHA: `affcbdf7166a4dc1bdbbb104c2877975631109e1`. Re-fetch verification still pending final audit closeout. This correction ensures the actual Brazil payload, manifest, checksums and indicator audit JSON are retained with the IMF metadata artifact.



### Part-4 — independent IMF registry listing and regression expansion (2026-11-18)
- Independently checked the IMF SDMX Central registry listing surfaced by its official catalogue: IMF `ECOFIN_DSD` latest version `1.0`; IMF `CL_INDICATOR` label `Economic Indicator`, version `1.0`. This corroborates the version-pinned IDs in the workflow, but is catalogue-page evidence only, not a raw XML acquisition or code-list payload. Sources: https://sdmxcentral.imf.org/data/datastructure.html and https://sdmxcentral.imf.org/items/codelist.html.
- Expanded `tests/test_brazil_bop_indicator_codes.py` with three further fail-closed cases: wrong REF_AREA; non-matching country ISO3 prefix (IND_ code while the reporting REF_AREA is BR / ISO3 BRA); duplicate CL_INDICATOR code ID. Total committed regression cases: seven. Commit: `1f8b07b7111a218880e247997e4cc8f010d8c7fd`; final test blob to be re-fetched for exact verification.
- The code remains deliberately conservative: an official codelist match is `LABEL_AVAILABLE_REVIEW_REQUIRED`; a Brazil-specific code not in the IMF codelist is `UNKNOWN_NO_IMF_LABEL`; a code neither listed nor correctly BRA_-prefixed is `UNKNOWN_QUARANTINE`. No semantic portfolio classification is implied.
- Live XML retrieval, workflow dispatch, execution of the seven tests, 237-code codelist comparison and economic semantic mapping remain NOT_DONE. Do not treat catalogue listings as substitutes for raw SDMX XML, checksums or workflow artifacts.



## 10. Chapter 35 Part-5 — full 237-code historical crosswalk and portfolio split (2026-11-18)

### Exact source artefacts re-opened and independently parsed
1. IMF official metadata acquisition Run `44095286184`, Artifact `14333192531`, created 2026-11-17. Manifest reports successful HTTP 200 capture of the `IMF:BOP_BPM6(1.0)` dataflow, its referenced `IMF:ECOFIN_DSD(1.0)`, and the BOP constraint. Raw metadata facts:
   - Dataflow XML: 22,078 bytes; SHA-256 `74a8f3a58ff3e0bc6e6681c4143cd042cc642edee06f8080e86c29dc3b64e919`.
   - Constraint XML: 18,675 bytes; SHA-256 `aa6c002fb3a2498420ed8796621664b492c18f58d75918d5c1bf8737fc917656`.
   - Referenced ECOFIN DSD + child codelists XML: 42,707,649 bytes; SHA-256 `81f4bf8bf43d466f94f8a429f8c8c40eccffe480845018421a1c384aae97d045`.
   - The referenced DSD contains exactly one `IMF:CL_INDICATOR(1.0)` with 113,644 unique code IDs.
2. Brazil BCB raw capture Run `44256602275`, Artifact `14405348744`. Re-downloaded ZIP and independently extracted `response.xml`: 4,840,062 bytes; SHA-256 `3e736c45d67fe64ac8c0cb3396718addab21a1ef43d09666ae8dd8ccaba3f52c`.
3. Parsed Brazil XML Header `Structure/@namespace` explicitly identifies `Dataflow=IMF:BOP_BPM6(1.0)`; all 237 series have `REF_AREA=BR`, `DATA_DOMAIN=BOP6`, `COUNTERPART_AREA=W1`, `FREQ=M`, `UNIT_MULT=6`, `TIME_FORMAT=P1M`.

### Exact code-list join result
- Brazil unique indicator codes: 237.
- Exact matches against the official IMF `CL_INDICATOR(1.0)`: 237 / 237.
- Unmatched: 0.
- Duplicate Brazil series keys: 0.
- Observations: 89,097; monthly coverage 1995-01 through 2026-09 (381 distinct months).
- Series observation-count distribution: 217 series × 381 observations; 16 × 345; 2 × 249; 2 × 201.
- Rule-based domain counts from the exact official English labels: Current Account 146; Financial Account 79; Capital Account 9; Other BOP 3. Classification is label-based and reviewable, not a model-generated inference.

### Portfolio investment — critical separation
The exact official labels identify 18 portfolio-related indicators, but only 9 are Financial Account portfolio-investment transaction series. A separate 9 are Current Account portfolio-investment income; they are not portfolio capital-flow transactions and must not be mixed into the capital-flow panel.

**Financial Account — Portfolio investment (9 codes):**
- `BFP_BP6_USD` — Portfolio investment total (side not split in the label).
- `BFPA_BP6_USD` — Net acquisition of financial assets total.
- `BFPAD_BP6_USD` — Assets: debt securities.
- `BFPAEEO_BP6_USD` — Assets: equity securities other than investment fund shares.
- `BFPAEIS_BP6_USD` — Assets: investment fund shares or units.
- `BFPL_BP6_USD` — Net incurrence of liabilities total.
- `BFPLD_BP6_USD` — Liabilities: debt securities.
- `BFPLEEO_BP6_USD` — Liabilities: equity securities other than investment fund shares.
- `BFPLEIS_BP6_USD` — Liabilities: investment fund shares or units.

Each of these nine series has 381 monthly observations from 1995-01 to 2026-09.

**Portfolio investment income — Current Account (9 separate codes):**
`BIPIPED_BP6_USD`, `BIPIPI_BP6_USD`, `BIPIP_BP6_USD`, `BMIPIPED_BP6_USD`, `BMIPIPI_BP6_USD`, `BMIPIP_BP6_USD`, `BXIPIPED_BP6_USD`, `BXIPIPI_BP6_USD`, `BXIPIP_BP6_USD`.
These describe investment-income receipts/payments or balances in the current account, not acquisition/incurrence of portfolio financial assets/liabilities.

### Unit, sign, quality and aggregation gates
- Series metadata contains `UNIT_MULT=6`; the official IMF code labels specify US Dollars. The payload does not expose a separate `UNIT_MEASURE` attribute. Raw values have not been rescaled; do not multiply/convert until the exact scale convention is independently checked against the DSD representation and source documentation.
- Observation elements expose only `TIME_PERIOD` and `OBS_VALUE`; no observation-level `OBS_STATUS` or `CONF_STATUS` attributes are present in this captured Brazil XML. Quality status is therefore `UNKNOWN`, not PASS.
- IMF BPM6 sign convention: increases in financial assets and liabilities are positive; decreases are negative. Financial-account balance/net lending (+)/net borrowing (-) is calculated as net acquisition of financial assets minus net incurrence of liabilities. Official sources: https://data.imf.org/-/media/iData/External-Storage/Documents/73FBCD5B6CDE4D289C60B9B0CAA40622/en/2-bpm6.pdf (paragraph 3.31); https://data.imf.org/-/media/iData/External-Storage/Documents/FB1F86C7158646DDB554D0882F1F2A3B/en/3-BPM6-com-guide.pdf (paragraphs 8.102–8.104, Tables 8.9–8.10).
- For Brazil, positive net acquisition of external assets means an increase in residents' external assets; positive net incurrence of liabilities means an increase in liabilities to non-residents. Do not treat either series alone as net inflow. Do not sum the portfolio total `BFP`, assets total `BFPA`, liabilities total `BFPL` and their component series together; that would double-count hierarchy levels. No net series has been computed.

### Dataflow registration discrepancy retained as an open provenance issue
The Brazil XML Header identifies `IMF:BOP_BPM6(1.0)`, and the captured official IMF dataflow metadata confirms that this dataflow references `IMF:ECOFIN_DSD(1.0)`. Separately, the current IMF SDMX Central Registrations page lists the BCB Brazil URL under `IMF:BOP6(1.0)`. These catalogue registration and payload-header identifiers conflict. Do not silently rewrite the raw header or claim the registration discrepancy resolved. Record it as `REGISTRATION_CATALOGUE_VS_PAYLOAD_HEADER_CONFLICT`; obtain a current BCB registration confirmation or matching IMF registration metadata before production admission.

### Reproducible implementation and current run
- Added `qa/build_brazil_bop_indicator_crosswalk.py` (commit `2b355b9ea5db9b4e934454fe877b18a17d6a6036`) to join the actual Brazil XML against official CL_INDICATOR, emit every matched label, per-series observations/periods, label-based domain/portfolio separation, and fail closed on unmatched codes or unexpected dataflow/area.
- Added `tests/test_brazil_bop_indicator_crosswalk.py` (commit `94e48d826ca1cce865fc0eab8143b6d30e008fd1`) covering portfolio financial-account vs income separation, absent quality remaining UNKNOWN, unmatched-code failure, wrong dataflow and wrong REF_AREA.
- Local independent execution against the two recovered source XML files: `PASS_CODELIST_CROSSWALK_ONLY`; output 237/237 exact matches, 89,097 observations, 9 financial-account portfolio series and 9 separate portfolio-income series. Local JSON output SHA-256 `637c64cffdc37e250704e6ac560d5167cdefec1e7e417b33c999644c7fbfcf1f` (238,180 bytes). This local file hash is not a GitHub artifact hash.
- Updated workflow to execute both indicator test files, capture current BCB + IMF metadata, build `evidence/brazil_bop/indicator_semantic_crosswalk.json`, hash it, and upload the full evidence directories. Push trigger is limited to the research branch and relevant workflow/QA/test paths. Commit `7584d5a1292356741716ce4540d4e0a693ed948d`.
- Workflow Run `44270663838` started on 2026-11-18 08:51:57 UTC from that commit. At the last check it was `in_progress`; the initial unit-test step and prior metadata validation steps were successful, and the ECOFIN DSD/codelist acquisition step was still running. Final runtime result/artifact must be recorded after completion.

### Acceptance status
| Gate | State |
|---|---|
| Official dataflow -> ECOFIN_DSD link (archived metadata) | PASS |
| Official CL_INDICATOR version 1.0 / 113,644 codes | PASS |
| Historical Brazil 237/237 exact code matches | PASS (recovered immutable artifacts) |
| 9 financial-account portfolio codes separated from 9 portfolio-income codes | PASS (official labels) |
| 9 portfolio FA series coverage 1995-01 to 2026-09 | PASS (captured observations) |
| Unit rescaling / observation quality | UNKNOWN |
| BCB registration vs payload dataflow identity discrepancy | OPEN / UNKNOWN |
| Current live paired capture and GitHub run 44270663838 | IN_PROGRESS at audit cut-off |
| Brazil portfolio flow panel admission | NOT_AUTHORIZED |
| Global EM aggregate / trading-signal admission | NOT_AUTHORIZED |

No production integration or protected selector changes.



### Additional value-level QA — explicit missing tokens (2026-11-18)
A separate value scan of all 89,097 captured observations found 88,764 numeric finite values and 333 literal `...` values. All 333 occur in only two series: `BFDLERV_BP6_USD` (132) and `BFOR_BP6_USD` (201). These tokens are not zero and their reason is not specified in the payload; retain them as missing/unknown. No duplicate TIME_PERIOD values were found within any of the 237 series. No OBS_VALUE attributes were absent. The 333 tokens reinforce that observation quality remains UNKNOWN because OBS_STATUS/CONF_STATUS are not present.

Updated `qa/build_brazil_bop_indicator_crosswalk.py` to count numeric observations and explicit `...` tokens, fail on unrecognized nonnumeric values, missing OBS_VALUE, non-finite values, and duplicate periods; never impute missing markers as zero. Commit `2275348648ac97efeb0a72358dbae54528e8769b`; blob SHA `1a1828c0b2e5fb7c918b8a348265844971ed54ff`.

Expanded crosswalk regression tests for explicit missing-token accounting, unexpected nonnumeric values, and duplicate periods. Commit `c7210113190afef7627e71212f043e0afe521b02`; blob SHA `a3e6f9a9110a52be2a12c1620ae9d3227bed6513`. The push-triggered workflows are running on commits `2275348648ac97efeb0a72358dbae54528e8769b` (Run `44270990383`) and `c7210113190afef7627e71212f043e0afe521b02` (Run `44271011602`). Their final conclusions are pending.
