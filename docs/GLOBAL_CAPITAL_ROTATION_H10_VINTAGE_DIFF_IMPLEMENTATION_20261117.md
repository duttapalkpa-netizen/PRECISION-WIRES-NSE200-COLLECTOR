# H.10 Vintage Diff Implementation — 2026-11-17
Status: IMPLEMENTED IN RESEARCH BRANCH; TEST EXECUTION / CI INTEGRATION NOT YET VERIFIED; NO REAL VINTAGE PAIR

## Why this task
The Federal Reserve DDP FAQ states release XML files are overwritten as the release updates and prior-date XML versions are not available from that location:
https://www.federalreserve.gov/data/ddp-retirement-frequently-asked-questions.htm
The H.10 feed records the 2026-08-12 correction to the 2026-08-10 release, affecting August 3 values for all currencies and dollar indexes:
https://www.federalreserve.gov/feeds/h10.html
Those notices establish a correction event, not the old and new row values.

## Files committed
1. scripts/h10_vintage_diff.py
   - Exact target Board series: JRXWTFB_N.B.
   - Accepts two normalized CSV snapshots and two JSON provenance manifests.
   - Requires source URL, source publication timestamp, retrieval timestamp, raw byte length/hash, normalized CSV hash, exact series ID and vintage label.
   - Verifies normalized CSV SHA-256 before parsing.
   - Enforces timezone-aware timestamps, exact series ID, chronological unique dates, finite numeric A values and ND missing semantics.
   - Never downloads or fabricates a snapshot.
   - Emits deterministic row-level CSV classifications: unchanged, changed, added, removed, missing/status-changed; numeric absolute and relative deltas only for valid numeric pairs.
   - Summary explicitly states computed diff is not proof of official correction without independently established provenance.

2. qa/test_h10_vintage_diff.py
   - Five tests authored: all row classifications and ND preservation; unsorted/duplicate date rejection; normalized CSV hash mismatch; naive publication timestamp rejection; invalid ND value rejection.
   - Fixture timestamps/values are synthetic test fixtures only and are not historical observations. They must never be used as project data or evidence of the 2026-08 correction.

## Run locally
```bash
python -m unittest qa.test_h10_vintage_diff -v
python scripts/h10_vintage_diff.py --old-csv old.csv --old-manifest old.json --new-csv new.csv --new-manifest new.json --output revision_diff.csv --summary revision_diff_summary.json
```
CSV columns: date, series_id, value, status.
The two manifests must follow the required fields documented in the script docstring.

## Acceptance boundary
- Code and test files were written to branch research/taxonomy-crosswalk-contract-20261117 and re-fetched from GitHub to verify exact contents and blob IDs.
- The test suite has NOT been executed in GitHub Actions or locally in this task. Do not claim test PASS.
- No CI workflow was changed or dispatched.
- No authentic pre-correction / post-correction H.10 vintage pair was acquired.
- No row-level official correction diff was computed.
- The raw source archive SHA/byte length are provenance assertions supplied in the manifest; this tool does not independently reopen the raw archive. Independent raw archive verification remains a prerequisite upstream.

## Progress
| Item | State | Completion |
|---|---|---:|
| Diff utility committed and re-fetched | PASS | 100% |
| Five regression tests authored | PASS (authored only) | 100% |
| Test execution | NOT_DONE | 0% |
| CI wiring / run | NOT_DONE | 0% |
| Authentic pre/post vintages | NOT_DONE | 0% |
| Official row-level correction quantification | NOT_DONE | 0% |

## Invariants
Research-only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A-E unchanged. UNKNOWN never PASS. No synthetic observations, fabricated timestamps/hashes, paid APIs or spend; ₹0.

## CI execution and defect correction (2026-11-17)
- Dedicated workflow: .github/workflows/h10-vintage-diff-tests.yml; bounded timeout 3 minutes; offline only; no FRED/network retrieval.
- Workflow commit: f72eb31651baa9560e67680e2f6374d6d26119bc.
- First run #1 / ID 44066401613: FAILURE. Compilation passed; 4/5 tests passed. One assertion exposed Decimal formatting difference: computed relative delta "0.500" vs expected "0.5".
- Correction commit 4dbdc894461ff918545c03dce89894e5226c4af0 normalized Decimal formatting. Follow-up review caught a potential trailing-zero truncation edge case for integer percentages; corrected safely using Decimal.normalize().
- Final code commit: 81b56220028c9e680f9cb2146f1693b615775c3c.
- Final run #3 / ID 44066531312: SUCCESS; job 133981513053 SUCCESS; compile step SUCCESS; all five regression tests SUCCESS; test runtime 0.021 seconds.
- Tests: all row classes and ND preservation; chronology/uniqueness; hash mismatch; timezone-aware timestamp; invalid ND sentinel.
- No real vintage files were used. Synthetic fixtures are isolated unit-test inputs only; no historical correction inference.
- Final workflow URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44066531312

## Updated acceptance state
| Item | State | Completion |
|---|---|---:|
| Diff utility committed and re-fetched | PASS | 100% |
| Five regression tests | PASS | 100% |
| Dedicated offline CI workflow | PASS | 100% |
| Final GitHub Actions execution | PASS | 100% |
| Authentic pre/post vintages | NOT_DONE | 0% |
| Official row-level correction quantification | NOT_DONE | 0% |
| Production integration | BLOCKED / NOT_AUTHORIZED | 0% |

The offline implementation and regression gate are complete. Historical revision evidence is not complete until authentic, independently provenance-verified snapshots are available.
