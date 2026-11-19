# Brazil Portfolio Assets — Monthly Gross-Flow Identity Audit
Date: 2026-11-19 (Asia/Kolkata)
Continuation: Research verification 41, Part-1
Decision: **381/381 monthly identity checks PASS under the empirically selected convention: 22906 = 22908 - 22907.** This closes the BCB asset-side arithmetic integrity gate only; Brazil IMF PA identity and GCR aggregate gates remain open.

## Progress Log
### Completed / reused
- Reused Part-1 liabilities identity (SGS 22924 = 22925 - 22926): 381/381 PASS. No repeat.
- Reused the existing 22906 raw capture; artifact raw hash matches previous archive.
- Official BCB metadata confirms:
  - 22906: portfolio investment, net acquisition of financial assets, monthly, net.
  - 22907: same measure, monthly, inflows.
  - 22908: same measure, monthly, outflows.
  - All are BCB/DEPEC series, million USD, monthly, coverage from 1995-01.
- Because the assets-side sign convention was not assumed, both possible decompositions were tested against the net series for every matched month.

## Method and decision rule
Two candidate formulas were tested independently:
1. `22906 = 22908 - 22907` (outflows minus inflows)
2. `22906 = 22907 - 22908` (inflows minus outflows)

All three raw public SGS JSON responses were archived byte-for-byte with URL, final URL, retrieval UTC, response headers, status, byte count and SHA-256. Month keys were parsed as YYYY-MM and exact-joined. No interpolation or synthetic rows. A monthly check passes only if all three values are present, all three values are reported to one decimal place, and the absolute residual is <= USD 0.15 million.

## GitHub Actions evidence
- Workflow: `.github/workflows/bcb_asset_flow_identity.yml`
- Script: `scripts/research/validate_bcb_asset_flow_identity.py`
- Run ID: `44539091458`; SUCCESS. URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44539091458
- Artifact ID: `14535754997`; name `bcb-asset-identity-44539091458`; 16,611 bytes.
- ZIP SHA-256 (independently recomputed; equals GitHub artifact digest): `8849f91e5a28d3c7e90a3df1cdcdb46c1fc66bb22ce54af8ea20ebbeca05761b`.
- Artifact contains raw JSON for 22906, 22907, 22908, a manifest and monthly identity CSV.

## Raw source integrity
| SGS | Meaning | Bytes | SHA-256 |
|---|---|---:|---|
| 22906 | Net acquisition of financial assets | 14,594 | `110477090f5ff3e9f4e4d2ce235082d837020603b13795dbc2bde20769a3db30` |
| 22907 | Asset inflows | 14,567 | `920aea58c2a7f90106cfeef25b29b077e66d0f65efa73237ba82be34b8885c7a` |
| 22908 | Asset outflows | 14,593 | `7ef8ee458ceae80914183c49334409f175891e0d30d280ad1d513e684c6dc73e` |

All three returned HTTP 200 and contain 381 valid monthly observations from 1995-01 to 2026-09. The 22906 raw hash matches the previous archived response.

## Results
- Common matched months: 381/381.
- Candidate 1, `22906 = 22908 - 22907`: **381 PASS / 0 REVIEW**, max absolute residual USD 0.1 million.
- Candidate 2, `22906 = 22907 - 22908`: **0 PASS / 381 REVIEW**, max absolute residual USD 17,048.8 million.
- Selected convention: **net acquisition of assets = outflows minus inflows** for these BCB SGS series.
- Example 1995-01: 55.0 - 44.2 = 10.8 million USD, matching net 10.8.
- Example 2026-09: 5,955.2 - 2,685.9 = 3,269.3 million USD, matching net 3,269.3.

## Combined Brazil BCB accounting gate
- Assets: `22906 = 22908 - 22907`, 381/381 PASS.
- Liabilities: `22924 = 22925 - 22926`, 381/381 PASS (prior Part-1).
- Combined monthly gross-to-net checks: 762/762 PASS across two independent accounting legs.
- These are BCB internal source consistency checks. They are not independent country cross-source comparisons and must not be counted as 762 IMF-to-BCB validations.

## Acceptance matrix
| Gate | Status |
|---|---|
| Official metadata for 22906/22907/22908 | PASS |
| Three raw SGS downloads HTTP 200 | PASS |
| 381 valid rows per series | PASS |
| Exact month-key join / no missing months | PASS |
| Outflows-minus-inflows identity | PASS (381/381) |
| Opposite sign candidate rejected by evidence | PASS (0/381) |
| Artifact ZIP and raw hashes independently verified | PASS |
| BCB liabilities identity | Previously PASS (381/381) |
| Brazil IMF Data Portal scale/sign benchmark | Previously PASS (94/94 quarterly checks) |
| BCB registered XML BOP_BPM6 vs Brazil PA BOP6 | BLOCKED / unresolved |
| Brazil PA revision chronology | NOT_DONE |
| GCR 154-member coverage/vintage/BPM gate | BLOCKED / partial |
| EMDE aggregate / production admission | NOT_AUTHORIZED |

## Limitations and next actions
- This verifies only the BCB SGS assets gross-to-net arithmetic for the captured vintage. It does not establish IMF registration identity or PA chronology.
- Do not add gross inflows/outflows as independent capital attraction signals on top of net flows; they are components of the net identity and would double count.
- Next Brazil closure dependency remains official owner-side PA revision/changelog and BR1 registration detail, not another public SGS download.
- Next GCR closure work: raw historical Chile BDE vintage archive and country-vintage alignment; retain 40 no-data countries, 83 empty country-entry cells and 13 interior-gap series as missing.
- No aggregate or production score until all country coverage, vintage, BPM and semantics gates pass.

## Invariants
₹0; official free sources only; no synthetic values, inferred timestamps or fabricated hashes; UNKNOWN is not PASS. No production integration, macro weights, selector/ranking/pressure-fade/CORE-672/Engines A-E changes.
