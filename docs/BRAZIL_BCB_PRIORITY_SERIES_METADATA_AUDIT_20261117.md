# Brazil BCB Priority-Series Metadata Audit — 2026-11-17

## Scope
Complete the official dataset-metadata gate for the seven priority SGS series already selected in the hierarchy map. This is metadata/source identity work only; it is not raw observation capture or accounting acceptance.

## Verified priority series
| SGS | Official dataset title | Organization | Frequency | Unit | Coverage start | Official dataset page |
|---|---|---|---|---|---|---|
| 22905 | Portfolio investment - monthly - net | BCB/Depec | Monthly | Million US dollars | 1995-01-01 | https://opendata.bcb.gov.br/dataset/22905-portfolio-investment---monthly---net |
| 22906 | Portfolio investment - Net acquisition of financial assets - monthly - net | BCB/Depec | Monthly | Million US dollars | 1995-01-01 | https://opendata.bcb.gov.br/dataset/22906-portfolio-investment---net-acquisition-of-financial-assets---monthly---net |
| 22907 | Portfolio investment - Net acquisition of financial assets - monthly - inflows | BCB/Depec | Monthly | Million US dollars | 1995-01-01 | https://opendata.bcb.gov.br/dataset/22907-portfolio-investment---net-acquisition-of-financial-assets---monthly---inflows |
| 22908 | Portfolio investment - Net acquisition of financial assets - monthly - outflows | BCB/Depec | Monthly | Million US dollars | 1995-01-01 | https://opendata.bcb.gov.br/dataset/22908-portfolio-investment---net-acquisition-of-financial-assets---monthly---outflows |
| 22924 | Portfolio investment - Net incurrence of liabilities - monthly - net | BCB/Depec | Monthly | Million US dollars | 1995-01-01 | https://opendata.bcb.gov.br/dataset/22924-portfolio-investment---net-incurrence-of-liabilities---monthly---net |
| 22925 | Portfolio investment - Net incurrence of liabilities - monthly - inflows | BCB/Depec | Monthly | Million US dollars | 1995-01-01 | https://opendata.bcb.gov.br/dataset/22925-portfolio-investment---net-incurrence-of-liabilities---monthly---inflows |
| 22926 | Portfolio investment - Net incurrence of liabilities - monthly - outflows | BCB/Depec | Monthly | Million US dollars | 1995-01-01 | https://opendata.bcb.gov.br/dataset/22926-portfolio-investment---net-incurrence-of-liabilities---monthly---outflows |

## Evidence boundary
- 22905–22908 were previously inspected in the earlier BCB SGS crosswalk/hierarchy work; their metadata is reused, not re-fetched as a new observation test.
- 22924 and 22925 were newly confirmed from their official BCB dataset pages in this audit. 22926 is retained from the prior verified pilot and independently visible on its official BCB dataset page.
- The official BCB pages expose JSON and CSV resources through the BCData/SGS service. This audit does not claim that the raw payload bytes were retrieved.
- Metadata describes monthly frequency and USD-million units. It does not by itself establish the accounting sign convention, exact perimeter equivalence, component arithmetic, or revision/vintage behavior.
- BCB dataset pages refer to the Balance of Payments historical-series methodological notes. The methodology page was previously found to be JavaScript-dependent/unreadable in the available retrieval path; exact sign treatment remains unresolved.

## Acceptance
| Gate | Result |
|---|---|
| Seven priority SGS identities mapped | PASS |
| Official dataset page for each priority series | PASS |
| Frequency/unit/coverage metadata for seven priority series | PASS |
| Raw CSV/JSON byte capture | NOT_DONE |
| HTTP response metadata, byte lengths and SHA-256 | NOT_DONE |
| Complete date-level observations | NOT_DONE |
| BOP sign convention and net/component identities | UNKNOWN / NOT_DONE |
| Country-period QA | NOT_DONE |
| Brazil pilot | NOT_ACCEPTED |
| EM-wide panel | NOT_DONE |
| Production integration | NOT_AUTHORIZED |

## Next action
Use a byte-capable GitHub Actions runner or user-supplied raw exports to acquire the seven official CSV payloads. Archive the exact response bytes, URL, retrieval timestamp, HTTP status/headers, byte length and SHA-256. Only after raw capture should date-level joins and candidate identities be tested. Keep net series distinct from receipts/outflows until the official BOP sign convention is documented.

## Invariants
Research-only; ₹0; official free sources only. No synthetic/forward-filled values, invented timestamps or hashes. UNKNOWN never PASS. Do not change Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate, collector workflows, or production integration.
