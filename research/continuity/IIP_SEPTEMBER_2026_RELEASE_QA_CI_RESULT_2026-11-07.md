# September 2026 IIP release metrics QA — executed result 2026-11-07

## CI execution
- Workflow: IIP September 2026 Release Metrics QA
- Run ID: 42400271361
- Commit: fe9f87a37bb110a5202729c721a8713a671b6392
- Result: GitHub Actions SUCCESS; both Python validators completed and artifact uploaded.
- Run URL: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/42400271361
- Artifact ID: 13584194796
- Artifact name: iip-2026-09-release-metrics-qa-1
- ZIP SHA-256: 6a97828061391dece1825a1b26c1daea65ad1705c6edef92468e5510cf54956b

## Independently downloaded and inspected artifact
- Artifact ZIP downloaded from GitHub and SHA-256 independently recomputed; matches GitHub artifact digest.
- Release metrics QA JSON SHA-256: 33a55d1e6eccd10dd361c02783a901ca0e3e90729c2f5f8b6a5cd849024d1bd1
- NIC-2 Statement II-A QA JSON SHA-256: 5e22145ecd4e96f7881a427a1cd556b2ca9f689350dad83e31fbef23573493c0

## Exact QA outcomes
### Release-level metrics
- Status: PASS_TRANSCRIPTION_AND_STRUCTURE_QA
- 19 rows; 19 unique metric keys; zero errors.
- Source CSV SHA-256: 79ff77d60d6ad3e776a5aa68fedec3a4891269c5b196a2c4f50b558b30d39540.
- Derived 17/23 positive manufacturing group breadth = 73.913%; explicitly derived, not a separately published MoSPI metric.

### Complete NIC-2 manufacturing Statement II-A
- Status: PASS_TRANSCRIPTION_STRUCTURE_AND_ARITHMETIC_QA
- 23 rows; 23 unique codes; complete NIC-2025 code coverage 10–32.
- Source CSV SHA-256: 102bef6c87b95c1478686935d9a6f5fcacda90dce07ea48f36d09e340fc29b7f.
- Monthly YoY and cumulative growth arithmetic validators: zero errors.
- Positive/negative/zero groups: 17/6/0.
- Displayed weights sum 76.065 vs official manufacturing weight 76.062; +0.003 rounding difference, within configured ±0.005 tolerance. Published values were not adjusted.

## Trigger hardening
Workflow was changed from manual-only dispatch to also run on bounded pushes affecting only the two September 2026 source CSVs, their two validators, or the workflow itself. Existing 5-minute job timeout and artifact upload on always() are retained. No main-branch automation was enabled; branch remains fix/iip-41-vintage-audit-clean.

## Certification boundary
This is CI transcription/schema/arithmetic QA for the 28-Oct-2026 PIB release ledger and the 23-row NIC-2025 manufacturing Statement II-A. It is NOT raw PIB PDF binary SHA-256 certification, not independent extraction from raw PDF bytes in this run, not a full April-2023-onward IIP monthly panel, and not source workbook provenance certification. PDF raw hash remains NOT_ACQUIRED. No predictive factor or production score was added/changed.

## Gate and invariants
- September 2026 ledger QA: PASS at stated scope.
- Raw PDF binary provenance: PENDING.
- Full historical new-series panel and revision vintage panel: PENDING.
- IIP full audit and master Hard Gate: BLOCKED.
- Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and A/B/C/D/E production logic unchanged.
- Research spend ₹0.
