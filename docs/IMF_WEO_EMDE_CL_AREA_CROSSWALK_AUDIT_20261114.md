# IMF WEO EMDE to IMF CL_AREA Crosswalk Audit

Audit date: 2026-11-14 (Asia/Kolkata)
Scope: research branch only; free official IMF sources; no observation extraction or EM aggregation.

## Outcome

**PASS — 154/154 mapped, 0 UNKNOWN, 0 ambiguous.**

- Classification authority: IMF World Economic Outlook, April 2026 Database Appendix.
- Membership denominator: 154 Emerging and Developing Economies (EMDE).
- Mapping authority: IMF SDMX Central CL_AREA, version 2.0.0.
- Exact normalized matches plus explicit reviewed label aliases: 154.
- Unique mapped IMF area codes: 154; duplicate code assignments: none.
- Ambiguous mappings: none.
- West Bank and Gaza → IMF CL_AREA code PS (current label: Palestine, State of), using an explicit official IMF legacy-code crosswalk.
- India: WEO India → IMF area IN, exact normalized match.
- This does not establish BOP observation availability. No flow panel or EM aggregate was calculated.

## Official source captures

### WEO April 2026 Database Appendix
- URL: https://data.imf.org/-/media/iData/External%20Storage/Documents/4AA1F4D0624C46E98F95988F1F83E770/en/April%202026%20WEO%20Database%20Appendix
- HTTP 200; Content-Type application/pdf; 523,673 bytes.
- SHA-256: b8a538c3158bf0553a3ae45d4797cd5648cbea684eb4be848a52c1d64d994395

### IMF CL_AREA 2.0.0
- URL: https://sdmxcentral.imf.org/sdmx/v2/structure/codelist/IMF/CL_AREA/2.0.0/?format=sdmx-2.1&detail=full
- HTTP 200; Content-Type application/xml;charset=UTF-8; 186,255 bytes.
- English code labels parsed: 931.
- SHA-256: e66ec5af93108d35f5a20c7899fe43edf1f337af694d043e9d3a2f3a6a02fc9d

## Newly resolved explicit label aliases

| WEO label | IMF CL_AREA label | Code |
|---|---|---|
| Cabo Verde | Cape Verde | CV |
| Eswatini | Kingdom of Eswatini | SZ |
| Lao P.D.R. | Lao People's Democratic Republic | LA |
| St. Kitts and Nevis | Saint Kitts and Nevis | KN |
| St. Lucia | Saint Lucia | LC |
| St. Vincent and the Grenadines | Saint Vincent and the Grenadines | VC |
| Vietnam | Viet Nam | VN |

These are explicit label equivalences, not fuzzy matches. West Bank and Gaza is not mapped to Palestine, State of or Gaza and Jericho without authoritative equivalence.

### West Bank and Gaza territorial-label evidence
- IMF CPIS Data Template (official IMF source): https://data.imf.org/-/media/iData/External-Storage/Documents/00DA1FBD843040C89781AF28C926168F/en/CDIS-Data-Template.pdf
- The IMF template lists area code PS as “West Bank and Gaza Strip”. The current IMF CL_AREA 2.0.0 codelist lists PS as “Palestine, State of”.
- The crosswalk therefore uses the stable IMF area code PS, with the historical label equivalence retained in each affected member row's review_note. It does not map to the distinct CL_AREA code XG (“Gaza and Jericho”).
- This is an IMF area-code continuity crosswalk, not a geopolitical/legal-status assertion.

## Workflow and artifact evidence

- Workflow: IMF WEO EMDE membership to IMF area-code crosswalk
- Final Run ID: 43599993875; conclusion SUCCESS; all six workflow steps completed.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/43599993875
- Workflow commit: f74a39dfbe6184e77fd804a0948a6b3fe662cb6b
- Artifact ID: 14115508523
- Artifact ZIP SHA-256: 50a627f4ecc10a0b762ffa382f155b5a986e73eaa3f008ff8c15103be634ce68
- Artifact includes raw WEO PDF, raw IMF CL_AREA XML, membership CSV, and full JSON crosswalk. Artifact was downloaded again and its ZIP and individual source hashes verified.

## Failure analysis and corrections retained

Earlier diagnostic runs remain preserved:
1. Run 43598079002 failed because an HTML table id=e1 was assumed; the IMF appendix resource was a PDF.
2. Run 43598148417 failed because the PDF parser dependency was not installed.
3. Run 43598156963 failed because stale HTML parser code remained and referenced weo_raw before acquisition.
4. Run 43598218778 completed as an integrity audit: 146 mapped, 8 unmapped, no ambiguous names.
5. Run 43599970390 completed with 153 mapped but temporarily included an unverified West Bank and Gaza alias.
6. Run 43599993875 removed that unverified alias and retained one UNKNOWN (153/154).
7. Final Run 43600131132 added the official IMF CPIS area-code evidence for PS, then achieved 154/154 unique mappings with zero unknown and zero ambiguous names.

Corrective lessons: inspect source media type before selecting a parser; pin dependencies; sequence acquisition, parsing, validation and artifact upload; remove duplicate alias keys; use explicit aliases only; retain territorial ambiguity as UNKNOWN. Workflow SUCCESS means the audit executed successfully, not that all mapping gates passed.

## Remaining gates

| Gate | Status |
|---|---|
| WEO April 2026 membership capture and 154-row integrity | PASS |
| IMF CL_AREA 2.0.0 capture and XML parsing | PASS |
| 153 unique area-code mappings | PASS |
| West Bank and Gaza → IMF area code PS, supported by official IMF CPIS template | PASS |
| Complete 154/154 crosswalk | PASS |
| BOP reporter/dataflow availability by economy | NOT DONE |
| India BOP observation extraction and reconciliation | NOT DONE |
| EM aggregation | BLOCKED |

## Production invariants

No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostic, engine, or hard-gate logic was changed. No synthetic observation, timestamp, mapping, or EM flow value was created. No paid API or service was used.
