# GCR — Nigeria IMF BOP scale/sign independent validation
Date: 2026-11-19
Decision: **6/6 quarter-entry comparisons PASS; fifth country in the cross-country sample.**

## Progress Log
### Completed
- Captured the official Central Bank of Nigeria (CBN) Q2 2026 BOP Highlights PDF anonymously, HTTP 200.
- Extracted Table 2, Financial Accounts, printed page 6 (PDF page index 6).
- Compared the two portfolio investment financial-account legs for Q2 2025, Q1 2026 and Q2 2026 against independent public IMF SDMX 3.0 observations.
- IMF assets and liabilities queries both HTTP 200; 5 quarterly observations returned per leg, 3 matched quarters selected.
- All six comparisons PASS within ±US$5 million, the maximum rounding tolerance implied by CBN publication to US$0.01 billion.
- Raw IMF CSVs, CBN PDF, extracted PDF text, comparison CSV and summary JSON are retained in the workflow artifact.

### Rejected / limits
- No universal scale/sign generalization to all 154 WEO G200 EMDE members from this one additional country.
- No net-flow aggregate, EMDE total, FX conversion, rescaling of raw observations, forward-fill or synthetic rows.
- CBN values are rounded to US$0.01 billion; do not overstate precision beyond ±US$5 million.
- Q2 2025 is marked provisional and Q1 2026 revised in the CBN footnotes; Q2 2026 is described as provisional in the release narrative. Preserve this source vintage status.
- This is an external national-source cross-check, not an IMF query-shape self-match.

## Sources
- CBN official PDF: https://www.cbn.gov.ng/Out/2026/STD/Q2%202026%20BOP%20Highlights_%20revised.pdf
- IMF public dataflow: `IMF.STA:BOP(21.0.0)`; indicator `P_F`; entries `A_NFA_T` and `L_NIL_T`; country `NGA`; quarterly; unit `USD`.
- IMF asset CSV SHA-256: `4e7ea3a3f3e171e7b72895ff1b0ad32ee4e8cbba69cf48d2bc2f63f7d2419f24`.
- IMF liability CSV SHA-256: `c6e5bec075e950aa6731380b78c0293a15f38fc7c69a725574971ce115584c45`.
- CBN PDF: 2,206,494 bytes; SHA-256 `b77c0066385cac4bb3bcbe150321c8da28da7d76c91b78423808a31deaea4cf9`.

## Calculation
`IMF USD million (derived) = raw OBS_VALUE / 1,000,000`
`CBN USD million = published USD billion × 1,000`
PASS if absolute residual ≤ US$5 million. Raw IMF observations are never overwritten.

| Period | Entry | CBN USD bn | IMF raw OBS_VALUE | IMF derived USD m | CBN USD m | Residual USD m | Result |
|---|---|---:|---:|---:|---:|---:|---|
| 2025-Q2 | Assets | -0.66 | -661,884,851.605964 | -661.884852 | -660 | -1.884852 | PASS |
| 2026-Q1 | Assets | 0.26 | 261,042,097.262066 | 261.042097 | 260 | 1.042097 | PASS |
| 2026-Q2 | Assets | 0.70 | 703,015,513.296694 | 703.015513 | 700 | 3.015513 | PASS |
| 2025-Q2 | Liabilities | 5.28 | 5,283,292,152.805870 | 5,283.292153 | 5,280 | 3.292153 | PASS |
| 2026-Q1 | Liabilities | 6.03 | 6,025,245,356.212000 | 6,025.245356 | 6,030 | -4.754644 | PASS |
| 2026-Q2 | Liabilities | 7.09 | 7,088,922,653.053650 | 7,088.922653 | 7,090 | -1.077347 | PASS |

## Reproducibility
- GitHub Actions run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44485137974
- Artifact ID: `14510920161`; ZIP 2,056,239 bytes; SHA-256 `bf80b403e072c8eae39f4ec32de77b55d776ef77b7ff4a88e157e3023da7febf`; 90-day retention.
- Durable raw CSVs, comparison and manifest are committed under `docs/evidence/gcr_nigeria_bop_20261119/`.

## Decision boundary
Nigeria adds six PASS comparisons to the four-country sample previously reported as 118/118. Combined tested sample: **124/124 PASS across Brazil, India, Mexico, Chile (older aligned vintage) and Nigeria**. This does not validate the other 149 EMDE members, resolve all vintage revisions, or authorize an aggregate. Keep all 154-member coverage gaps explicit. No production factor/backtest admission.
