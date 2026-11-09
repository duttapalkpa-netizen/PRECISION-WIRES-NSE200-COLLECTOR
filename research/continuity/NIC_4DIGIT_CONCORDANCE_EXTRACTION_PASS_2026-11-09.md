# NIC-2025 ↔ NIC-2008 4-Digit Concordance — Extraction PASS and Independent Reconciliation
Date: 2026-11-09
Scope: Research-only official-source extraction; no production integration.

## Result
- Official NIC-2025 PDF concordance printed pages 232–238: 463 rows extracted.
- NIC-2025 keys: 463 unique; duplicates: 0.
- Partial mapping rows: 184.
- Aggregation rows: 62.
- Reverse source-code one-to-many mappings: 123.
- Known source sentinels: 10/10 PASS, including the 4772 split expression.
- Independent QA: PASS; errors: 0.

## GitHub execution evidence
- Branch: `research/nic-concordance-463-extraction-hardening`
- Head commit: `a0d5b8db5b2863f57c1b2fd4220d5cbdb1937795`
- Workflow: Official NIC Concordance Source Acquisition and Extraction
- GitHub Actions Run ID: `42564242920`
- Run status: completed / success
- Run duration: 46 seconds (2026-11-09 04:53:38Z to 04:54:24Z)
- Artifact ID: `13651160498`
- Artifact name: `official-nic-concordance-audit-7`
- Artifact size: 4,791,962 bytes
- Artifact ZIP SHA-256: `2f5a3c73dea21e81cfbceec673ccf83737a650434fb2fa8fe037276fe380e618`

## Source binary SHA-256
- NIC-2025 final PDF (5,143,225 bytes): `66bc2babc1e915b670b21a66d556c2933b97f72d9590a50cc535c5e9239fe709`
- NIC-2025 XLSX (213,156 bytes): `ad3b8f24a40de5650c9fa8d06a36940c6e3c5d159d4f82d6c5cb3740d4e324c0`
- NIC-2008 XLSX (77,938 bytes): `7dad3bc665da03df3da73e54b25eb0d08b58ea781204537afe9278a3407c9dba`
- Extracted CSV SHA-256: `0169b5668db57ac5155992947026a71815cff2964d4a31fa8e302203912ac8fa`

## Independent reconciliation
- PDF-extracted NIC-2025 class set equals the official NIC-2025 workbook Class column: 463/463.
- All 419 distinct NIC-2008 source components referenced by the concordance exist in the official NIC-2008 workbook.
- Raw source-cell expression vs canonical expression and parsed component reconstruction checked.
- All '+' aggregation operators and '(p)' partial markers retained.
- Source printed page, table index, row index and raw continuation fragments retained.
- 4772 expression reconstructed only because the preceding source cell ended with '+' and the next table's first blank-code row supplied 4799(p). Both source fragments are retained.
- Ten sentinel mappings all match: 1512, 1811, 2611, 2619, 3101, 3102, 3511, 3512, 3513, 4772.
- Independent QA JSON reports `PASS`, zero errors.

## Defects found and corrected during this execution
1. Prior PDF endpoint returned HTTP 404. Replaced it with the current official MoSPI publication URL; PDF download and binary hash now PASS.
2. Plain text line parsing returned zero rows because PDF table columns are exposed as separate text lines. Replaced it with PyMuPDF table-cell extraction across the seven printed pages.
3. Header cells were split as `NIC2025\nCode` / `NIC2008Code`. Added whitespace-normalized header recognition and regression coverage.
4. NIC-2025 4772 mapping ends with a '+' in one table and continues as 4799(p) in the next table. Added fail-closed continuation handling; orphan or unresolved fragments are rejected.
5. Workbook inventory incorrectly iterated cell values as row objects and raised TypeError. Corrected it to materialize rows; acquisition manifest now requires both workbook inventories plus all three source downloads to PASS.

## Output files in artifact
- `raw/nic2025_pdf.pdf`
- `raw/nic2025_xlsx.xlsx`
- `raw/nic2008_xlsx.xlsx`
- `nic_source_sha256_and_workbook_inventory.json`
- `concordance/nic2025_to_nic2008_4digit_concordance.csv`
- `concordance/nic_concordance_extraction_audit.json`
- `concordance/nic_concordance_independent_qa.json`

## Boundary / unresolved research gate
- This PASS certifies the 4-digit NIC activity-class concordance extraction and its code-set/source validation only.
- NIC-2 manufacturing roll-up is NOT CERTIFIED.
- IIP-specific item-group/weight correspondence remains UNKNOWN / BLOCKED.
- Do not truncate codes to 2 digits, infer IIP weights, create index conversion factors, or promote this concordance to production.
- The manufacturing mapping safety decision remains: no automatic 2-digit IIP mapping from NIC concordance alone.
- No production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 diagnostics or V11.3 engines were changed.

## Protected project constraints
56 Steps × 12 Filters = 672 diagnostics remain unchanged. UNKNOWN is neither PASS nor FAIL. No synthetic rows, fabricated timestamps, unsupported source promotion, paid API, spend, or Hard Gate relaxation. Step 6 remains gated by Step 5 final-paper acceptance.
