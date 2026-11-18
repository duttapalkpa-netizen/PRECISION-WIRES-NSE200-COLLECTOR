# গবেষণা যাচাই অব্যাহত 36 — Part-13: IMF Brazil Provision Agreement evidence reconciliation
Date: 2026-11-18 (Asia/Kolkata)
Source artifact: Library upload `imf_pa_research(1).zip` (5,628,154 bytes)
ZIP SHA-256: `8cb2ed4bd96c0b1c4d3f24d0530771a5868f55bba256213404d5acf22a3f2b45`
Manifest SHA-256: `0954644ea442a76e380cfc3e8ee2d95503fd9b05da088c853f17fd4c320aa903`

## Executive decision
**Major evidence gap closed: the Brazil Balance of Payments Provision Agreement identity is now CONFIRMED. Overall Brazil Reconstruction remains INCOMPLETE / BLOCKED.**
The supplied archive contains three successful HTTP 200 IMF structure responses. All three independently include the same Brazil PA identity and references:
- Provision Agreement: `urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)`
- PA ID/version: `IMF:BR_BOP_BP6(1.0)`
- Name: `Brazil Balance of Payments`
- StructureUsage/Dataflow reference: `IMF:BOP6(1.0)`
- DataProvider reference: `IMF:DATA_PROVIDERS(1.0).BR1` (provider agency IMF, parent DATA_PROVIDERS version 1.0, id BR1)
This directly confirms that the IMF registry's Brazil BOP Provision Agreement joins provider IMF:BR1 to dataflow IMF:BOP6(1.0). It does not establish a historical event chronology.

## Archive integrity and endpoint results
The ZIP contains exactly four entries:
| Entry | Bytes | SHA-256 |
|---|---:|---|
| `legacy_all.xml` | 53,443,157 | `75b7a55f5daafb0ce566593542f76874f202eeae6b4f09cb572f5372ef44be85` |
| `v2_imf_all.xml` | 52,420,642 | `9c8e9c9157da0e3ce33ca23db5afbc25e2517e02f481c8688d3ad0ed7f13ff0e` |
| `v2_all_agencies.xml` | 592,196 | `85b951126342dc1e5be7b104e676b519b1e9d1a857fa78a4d91b2a3e35637453` |
| `manifest.json` | 1,383,003 | `0954644ea442a76e380cfc3e8ee2d95503fd9b05da088c853f17fd4c320aa903` |

Manifest records:
1. Legacy REST `https://sdmxcentral.imf.org/ws/public/sdmxapi/rest/provisionagreement/all/all/latest?references=all`: HTTP 200, `application/xml;charset=UTF-8`, 53,443,157 bytes.
2. SDMX v2 IMF scope `https://sdmxcentral.imf.org/sdmx/v2/structure/provisionagreement/IMF/all/latest?references=all&format=fusion-json`: HTTP 200, `application/xml;charset=UTF-8`, 52,420,642 bytes.
3. SDMX v2 all-agencies scope `https://sdmxcentral.imf.org/sdmx/v2/structure/provisionagreement/*/*/*?format=fusion-json`: HTTP 200, `application/xml;charset=UTF-8`, 592,196 bytes.

Important format observation: despite the `format=fusion-json` query parameter, the two v2 responses recorded by the uploader are XML, not JSON. We parsed them as XML, consistent with their actual Content-Type and bytes; no JSON parsing assumption was used.

ProvisionAgreement counts by response: legacy 1,003; v2 IMF 992; v2 all-agencies 1,004. The three response sets all contain the exact target PA. The legacy and v2 IMF datasets each expose 27 ProvisionAgreements linked to provider IMF:BR1; the all-agencies file contains the target record as well. Counts differ by endpoint scope/response content; no claim is made that the 3 response payloads are byte-identical.

## Exact target ProvisionAgreement payload
The target object in all three XML responses has:
- `ProvisionAgreement` attributes: agencyID=`IMF`, id=`BR_BOP_BP6`, version=`1.0`, isFinal=`false`.
- English Name: `Brazil Balance of Payments`.
- `StructureUsage/Ref`: package=`datastructure`, agencyID=`IMF`, id=`BOP6`, version=`1.0`, class=`Dataflow`.
- `DataProvider/Ref`: maintainableParentID=`DATA_PROVIDERS`, package=`base`, maintainableParentVersion=`1.0`, agencyID=`IMF`, id=`BR1`, class=`DataProvider`.

This is a direct structural join: PA -> IMF:BOP6(1.0) and PA -> IMF:BR1. The PA does not contain the BCB SimpleDataSource URL, registration action/timestamp, transaction ID, or dated revision/changelog in the extracted object.

## Other Brazil PA inventory (provider IMF:BR1)
The legacy response contains 27 PAs linked to BR1:
| PA ID | Dataflow | Name |
|---|---|---|
| BR_BOP_BP6 | BOP6 | Brazil Balance of Payments |
| BR_CBS | CBS | Brazil Central Bank Survey |
| BR_CGD | CGD | Brazil Central Government Debt |
| BR_CGO | CGO | Brazil Central Government Operations |
| BR_CPI | CPI | Brazil Consumer Price Index |
| BR_DCS | DCS | Brazil Depositary Corporations Survey |
| BR_DSE | DSE | Brazil Debt Securities |
| BR_EMP | EMP | Brazil Employment |
| BR_EXD_BP6 | EXD_BPM6 | Brazil external Debt |
| BR_EXR | EXR | Brazil Exchange Rates |
| BR_FSI | FSI | Brazil Financial Soundness Indicators |
| BR_FSI_2 | FSI | Brazil Financial Soundness Indicators monthly |
| BR_GGD | GGD | Brazil General Government Debt |
| BR_GGO | GGO | Brazil General Government Operations |
| BR_IIP_BP6 | IIP6 | Brazil International Investment Position |
| BR_ILV2 | ILV2 | Brazil International Reserves and Foreign Currency Liquidity |
| BR_IND | IND | Brazil Industrial Production |
| BR_INR | INR | Brazil Interest Rates |
| BR_MET | MET | Brazil Merchandise Trade |
| BR_NAG | NAG | Brazil National Accounts |
| BR_OFS | OFS | Other Financial Corporations Survey |
| BR_POP | POP | Brazil Population |
| BR_PPI | PPI | Brazil Producer Price Index |
| BR_SBS | SBS | Brazil Sectoral Stocks of Financial assets and Liabilities |
| BR_SPI | SPI | Brazil Share Prices Index |
| BR_UEM | UEM | Brazil Unemployment |
| BR_WOE | WOE | Brazil wages and earnings |

Note: PA identifier suffixes such as `BP6` are labels, not a substitute for reading the explicit Dataflow Ref. For the target PA the explicit Dataflow Ref is `BOP6`. For `BR_EXD_BP6`, the explicit Dataflow Ref is `EXD_BPM6`.

## Reconciliation with the previously established BCB mismatch
Previously archived current registration row:
- Provider `IMF:BR1`
- Dataflow `IMF:BOP6(1.0)`
- Data URL: BCB BPM6 XML
- Last Updated: `2026-10-26T11:47:29.000Z`

Previously archived BCB payload declares `IMF:BOP_BPM6(1.0)`.
New Part-13 finding: the authoritative current PA object confirms that `IMF:BR1` is provisioned for `IMF:BOP6(1.0)`, consistent with the current registry row. It does **not** explain why the registered BCB payload declares `IMF:BOP_BPM6(1.0)`. Therefore:
- Registry row ↔ PA Dataflow identity: **CONFIRMED CONSISTENT** (`BOP6`).
- PA ↔ Provider identity: **CONFIRMED** (`BR1`).
- Registry/PA BOP6 ↔ BCB payload BOP_BPM6: **MISMATCH REMAINS CONFIRMED / UNRESOLVED**.
- Do not treat BOP6 and BOP_BPM6 as interchangeable; same DSD does not establish identifier equivalence.

## Acceptance matrix update
| Requirement | Status |
|---|---|
| Official PA endpoint retrieval (3 responses) | PASS (manifest HTTP 200) |
| Raw ZIP integrity/hash | PASS (ZIP hash recorded) |
| Target Brazil BOP PA exact URN | PASS |
| PA -> Data Provider IMF:BR1 reference | PASS |
| PA -> Dataflow IMF:BOP6(1.0) reference | PASS |
| Cross-response target PA presence | PASS (3/3) |
| Brazil provider's other PA inventory | PASS (27 in legacy and v2 IMF responses) |
| PA changelog/revision history | NOT_DONE / not present in extracted PA object |
| PA-to-BCB URL link | NOT_ESTABLISHED by this PA response |
| Actual registration event rows | NOT_DONE |
| Create/Replace/Delete/Re-Register chronology | UNKNOWN |
| Event-to-current-registration row reconciliation | PARTIAL / BLOCKED |
| BOP6 vs BOP_BPM6 payload mismatch resolution | BLOCKED |
| Brazil/EM admission or market use | BLOCKED / NOT_AUTHORIZED |

## Exact next work
1. Use exact PA URN `IMF:BR_BOP_BP6(1.0)` to inspect the official PA detail page / compare / revisions / changelog and export any available revision records.
2. Retrieve exact Data Registration detail row for provider `IMF:BR1`, Dataflow `IMF:BOP6(1.0)`, and the BCB URL; capture the PA URN attached to the row if shown.
3. Obtain the original registration transaction SDMX-XML/CSV to determine the event action and timestamp; do not infer from PA version or Last Updated.
4. Reconcile whether the payload Dataflow BOP_BPM6 is a stale/mislabelled URL, a later replacement, or an IMF registration error. Only authoritative transaction evidence or IMF clarification can decide.

## Guardrails
- ZIP and all three raw XML files are user-provided official endpoint captures; source retrieval timestamps per HTTP response are not included in the manifest. Do not invent them. Library upload timestamp is not substituted for HTTP retrieval time.
- No synthetic data, guessed event IDs, undocumented endpoints, or fabricated chronology.
- ₹0 spend; official/free sources only.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. No production integration, PR merge, macro weights or trading admission. UNKNOWN is not PASS.
- Overall Brazil Reconstruction remains **INCOMPLETE / BLOCKED**, despite PA identity/reference closure.
