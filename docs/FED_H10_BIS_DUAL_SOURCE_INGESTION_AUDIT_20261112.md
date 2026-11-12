# PRECISION-WIRES V11.3 — H.10 + BIS USD/INR Dual-Source Ingestion Audit
**Audit date:** 2026-11-12  
**Research branch:** \`research/fed-h10-raw-ingestion-v1\`  
**Pull request:** #31 — Draft / Open / Unmerged  
**Scope:** Research-only official-source ingestion and daily panel construction. No production integration.

## 1. Completion summary

| Work item | Status | Progress |
|---|---|---:|
| Federal Reserve H.10 collector exact-origin security hardening | PASS | 100% |
| Federal Reserve H.10 live raw ZIP retrieval and SHA-256 archive | PASS | 100% |
| H.10 XML + structure extraction for selected daily series | PASS | 100% |
| BIS WS_XRU daily USD/INR raw SDMX-CSV retrieval and SHA-256 archive | PASS | 100% |
| H.10/BIS side-by-side date join with explicit missingness | PASS | 100% |
| SDMX-ML v1.0 full XSD validation | UNKNOWN / dependency-blocked | 0% |
| H.10/BIS vintage and semantic divergence assessment | PENDING | 0% |
| Capital Rotation overlay research validation / production integration | NOT RUN / NOT AUTHORIZED | 0% |

Overall PRECISION-WIRES research progress remains at the last audited baseline of **36%**. This audit does not recompute the entire project denominator; unrelated research workstreams and acceptance gates were not re-audited in this task.

## 2. Federal Reserve H.10 raw source

- Official source: \`https://www.federalreserve.gov/datadownload/Output.aspx?filetype=zip&rel=h10\`
- Retrieval run: \`43236135160\` (raw-only first verified run)
- Final dual-source workflow run: \`43237270064\` (SUCCESS)
- Raw ZIP bytes: 2,087,377
- Raw ZIP SHA-256: \`1f9fd18709b09d082b29d01621f52672426eca108a4f74224fa8f190a5f801b2\`
- Archive members: \`H10_data.xml\`, \`H10_struct.xml\`, \`H10_H10.xsd\`, \`frb_common.xsd\`
- ZIP CRC test: PASS
- H.10 data message Prepared: \`2026-11-09T18:25:06\`
- Release contains 87 series.

### Selected daily series
| Series | Meaning | First | Last | Observations | A | ND |
|---|---|---|---|---:|---:|---:|
| \`JRXWTFB_N.B\` | Nominal Broad Dollar Index | 2006-01-02 | 2026-11-06 | 5,440 | 5,227 | 213 |
| \`JRXWTFN_N.B\` | Nominal Advanced Economies Dollar Index | 2006-01-02 | 2026-11-06 | 5,440 | 5,227 | 213 |
| \`JRXWTFO_N.B\` | Nominal Emerging Market Economies Dollar Index | 2006-01-02 | 2026-11-06 | 5,440 | 5,227 | 213 |
| \`RXI_N.B.IN\` | Fed daily USD/INR, INR per USD | 1973-01-02 | 2026-11-06 | 14,049 | 13,497 | 552 |

Frequency code \`9\` was resolved from the official H.10 structure codelist as **Business day**. All three dollar-index series share the same 5,440-date calendar. The Fed USD/INR series covers every date in that calendar.

H.10 panel SHA-256: \`a0296b24fb86a44cd29a9490bb16071812b76b63dc3cd9ad7ff47b2efdd0280a\`.

## 3. BIS official daily USD/INR source

- Official API: \`https://stats.bis.org/api/v2/data/dataflow/BIS/WS_XRU/1.0/D.IN.INR.A?format=csv\`
- Dataflow: \`BIS,WS_XRU,1.0\`
- Series: \`D.IN.INR.A\`
- Dimensions: \`FREQ=D\`, \`REF_AREA=IN\`, \`CURRENCY=INR\`, \`COLLECTION=A\`
- Quotation: Indian rupees per US dollar; daily average of observations through period.
- Retrieved: \`2026-11-12T14:27:09Z\`
- Raw CSV bytes: 1,938,201
- Raw CSV SHA-256: \`15d5ff6e43e34aef09d848c8270e69f5702d41015d3f43a4f2d904802f476ad4\`
- Observations: 13,985, from 1973-01-02 through 2026-11-10.
- Source status counts: A=13,640; M=345.
- Duplicate dates: 0; dates sorted ascending.
- Confidentiality attribute: F for all rows.

## 4. Dual-source panel reconciliation

- H.10 panel calendar: 5,440 dates, 2006-01-02 through 2026-11-06.
- BIS status on the H.10 calendar:
  - A = 5,337
  - M = 37
  - No BIS observation = 66
- Both H.10 and BIS USD/INR active: 5,154 date pairs.
- Mean absolute difference across active pairs: 0.0703131802483508 INR/USD.
- Median absolute difference: 0.04812300000000036 INR/USD.
- Maximum absolute difference: 1.1638869999999955 INR/USD.
- Joined panel SHA-256: \`4e9c20937fc59834945b01da794bfcff70c2b2ebf6b31777a9e0232df821bbb1\`.

**Policy:** H.10 and BIS values remain in separate columns. Differences are descriptive only. No source is promoted, no value is overwritten, and no imputation or forward-fill is performed. BIS status M and absent dates remain explicitly marked.

## 5. CI and artifacts

| Run ID | Scope | Result |
|---|---|---|
| \`43235938618\` | H.10 URL-origin security regression | PASS, 8 tests |
| \`43236135160\` | H.10 raw source archive | PASS |
| \`43236687557\` | H.10 extraction and panel tests | PASS, 11 tests |
| \`43236972966\` | H.10 + BIS raw source ingestion | PASS |
| \`43237270064\` | H.10 + BIS dual-source daily panel | PASS, 13 tests |

Final artifact:
- Artifact ID: \`13952877084\`
- Name: \`fed-h10-bis-usd-inr-evidence\`
- Artifact SHA-256: \`c10652ad56bc4a161fc3dce9f821967fbefa370d11eac068ee9f219584cef7a6\`
- Retention until: 2027-02-10
- Workflow duration: 24 seconds (within the 10-minute limit).

## 6. Security correction and failed-run handling

The original H.10 URL prefix check was replaced with parsed-origin validation: exact HTTPS hostname, permitted port, and no userinfo. Redirects are checked against the same exact origin. Lookalike hosts, HTTP redirects, and non-standard ports are rejected.

An intermediate implementation commit had a ZIP magic-byte escaping error and its CI run failed (\`43235885420\`). The byte literal was corrected, and the subsequent security suite passed 8/8. The failed run is retained as a diagnostic history item; it is not counted as PASS.

## 7. Explicit UNKNOWN / pending gates

Full XSD validation is **UNKNOWN**, not PASS or FAIL. The official H.10 archive contains \`H10_H10.xsd\` and \`frb_common.xsd\`, but the latter imports SDMX-ML v1.0 dependencies not present in the archive: \`SDMXMessage.xsd\`, \`SDMXCompactData.xsd\`, and \`SDMXCommon.xsd\`. The user's SDMX-ML 2.1 schema bundle is a different standard version and is not substituted.

Next steps:
1. Obtain and provenance-pin the matching SDMX-ML v1.0 dependency schemas from an authoritative source; validate the H.10 data and structure documents against the correct schema set.
2. Reconcile H.10 and BIS USD/INR observation semantics, collection time, vintage, and material differences; retain source-specific values.
3. Only after QA, evaluate the panel in the research-only Global Capital Rotation Overlay. No production integration without explicit authorization.

## 8. Production invariants

- Production selector unchanged.
- \`RANKING_SCORE\` unchanged.
- \`+1 PRESSURE_FADE\` unchanged.
- 672 diagnostics unchanged.
- No synthetic research observations, fabricated timestamps, source promotion, paid APIs, or spending.
- PR #31 remains Draft and Unmerged. No PR merge performed.
