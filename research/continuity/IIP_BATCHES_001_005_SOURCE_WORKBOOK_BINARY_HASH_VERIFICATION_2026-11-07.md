# IIP Batch 001-005 original workbook binary hash verification — 2026-11-07

## Purpose
Resolve the highest-impact source-provenance uncertainty that can be settled from the retained immutable IIP ingestion artifact. This report verifies original XLSX workbook payload bytes, not the separate revision-ledger CSV hash declarations.

## Immutable source artifact
- GitHub Actions Run: 41640521553
- Artifact ID: 13232127900
- Artifact name: iip-41-vintage-ingestion-revision-audit
- Artifact ZIP SHA-256: e59d98dfe75e1c298b7a46d7304b44ce152d6a3363103238bfd1c466911a141c
- The artifact was downloaded from GitHub Actions and the raw XLSX members were read directly from the ZIP; hashes below are SHA-256 over the exact uncompressed XLSX member bytes.

## Exact workbook payload hashes
| Vintage ID | Original workbook | Bytes | Independently computed SHA-256 |
|---|---|---:|---|
| IIPMFY23049APR | IndicesIIP2011-12Monthly_annual_apr23_NIC2d_sectoralmonthly.xlsx | 63,571 | 7cff38f066509e007c980a4267fd1753aa1fcae560438ad3df424d78d49ec30e |
| IIPMFY23054MAY | IndicesIIP2011-12Monthly_annual_may23_NIC2d_sectoralmonthly.xlsx | 64,111 | 6530370f75fa24997f98b760f336b70533a058e1a0a0f464bf1c26a10985425a |
| IIPMFY23058JUN | IndicesIIP2011-12Monthly_annual_jun23_NIC2d_sectoralmonthly.xlsx | 64,381 | 326629f652ef7a6161ac60516b094a20f2f2b84e81fab278fdc9ea17377b263e |
| IIPMFY23062JUL | IndicesIIP2011-12Monthly_annual_jul23_NIC2d_sectoralmonthly.xlsx | 64,416 | ea5119cb6f76b2640289dcc98e71bfe1ac1786fc02f92f0e7cd57900fde3f26c |

## Batch mapping supported by existing ledgers and batch notes
- Batch 001 (April 2023): APR → MAY; both workbook hashes match the source artifact.
- Batch 002 (April 2023): APR → MAY; both workbook hashes match the source artifact.
- Batch 003 (April 2023): APR → MAY; both workbook hashes match the source artifact.
- Batch 004 (May 2023): MAY → JUN; both workbook hashes match the source artifact.
- Batch 005 (June 2023): JUN → JUL; both workbook hashes match the source artifact.

The four workbook hashes above are repeated in the corresponding batch CSV source columns and the batch-specific README/summary evidence. They match the exact original XLSX bytes in Run 41640521553's preserved artifact. This establishes workbook binary identity for these four vintages and supports the source workbook hash fields for batches 001-005.

## What this does and does not resolve
**Resolved:** Original XLSX payload SHA-256 for all four source vintages used by Batches 001-005.

**Not resolved:** The separate legacy CSV hash drift recorded for ledger files Batches 001, 003, 004, and 005. Those hashes refer to ledger CSV payloads, not XLSX workbooks. They remain quarantined and must not be overwritten.

**Not newly recertified:** This hash manifest does not independently repeat every source-cell value comparison. Existing batch-specific source crosswalks remain the evidence for their bounded cells. No additional candidate is promoted by this manifest.

## Gate and invariants
- Batch 001-005 source workbook binary hash verification: PASS for the four distinct workbook vintages.
- Legacy ledger CSV hash provenance: unresolved for 001,003,004,005.
- IIP full source audit: BLOCKED_WITH_PROVENANCE_GAPS.
- Master Hard Gate: BLOCKED.
- No synthetic rows, no invented timestamps, no unsupported PASS, no hash overwrite.
- Production selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and A/B/C/D/E production logic unchanged.
- Research spend ₹0.
