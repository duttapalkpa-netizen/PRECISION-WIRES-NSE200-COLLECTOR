# FII/DII Runtime Context Artifact Availability Audit

Date: 2026-11-16  
Scope: read-only artifact/provenance inspection; no data acquisition or code change  
Repository: `duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR`

## Objective

Determine whether the already-known archived workflow evidence contains the actual `data/context/market_context.json` required to validate the FII/DII collector-to-diagnostic schema contract. This is not a repeat of the source-schema audit or CORE-672 duplication audit.

## Exact source inspection

- `collector/context_data.py`, blob SHA `f38e17979774d1439eea79e4dc7728ba92a790d1`, on branch `research/nse-raw-manifest-retention-20261115`.
- `.github/workflows/nse_collector.yml`, blob SHA `96a714e7e74aa9d09b43f74facc758f358fd3124`, on branch `research/nse-raw-manifest-retention-20261115`.
- The workflow runs `python collector/context_data.py` and its upload-artifact step includes `data/context/` in the artifact path list.
- The collector writes `data/context/market_context.json` with `generated_at`, `sources.fii_dii`, `fii_dii[]`, and `fii_dii_coverage` when the NSE request succeeds. This describes the expected workflow output, not proof that any particular run produced it.

## Artifact inspected

- Existing artifact ID: `14175433267`
- Artifact name: `v11-3-cutoff-safe-replay-36`
- Associated known Run #36 / run ID: `43749155334`
- Downloaded file: `run36-context-check.zip`
- ZIP size: 25,817,040 bytes
- Independently recomputed ZIP SHA-256: `da4243672222fc764214bc8dcc9ef2afe3fbf661724c95f3c09d6581a3bca6e1` (matches the previously recorded artifact hash)
- ZIP entries: 13
- Relevant entries found: `data/qa/raw_archive_manifest.json`, `outputs/backtest/v11_3_historical_signals/v11_3_historical_signal_manifest.json`
- No entry under `data/context/`; no `market_context.json`; no FII/DII context payload.

## Finding and scope boundary

**PASS — artifact integrity check:** downloaded ZIP hash matches the already recorded SHA-256.

**NOT_PRESENT — context payload in this specific artifact:** the Run #36 replay artifact does not contain `data/context/market_context.json`.

This finding is strictly limited to artifact ID `14175433267`. It does NOT establish that no other workflow run or artifact contains a context payload. The artifact inspected is a cutoff-safe replay artifact; do not generalize its missing context directory to all collector runs.

## Consequence

- Real archived FII/DII context remains NOT_VERIFIED.
- No row-level runtime assertion can be made about the collector's actual output from this artifact.
- Do not generate a synthetic market context or claim the collector output was runtime-validated.
- Keep aggregation period, sign/units, missing-side behavior and freshness policy BLOCKED until policy is approved and an actual context artifact is located.
- No adapter or regression implementation is authorized by this audit.

## Progress

- Exact collector/workflow source reinspection: 100%.
- Existing Run #36 artifact download and SHA-256 verification: 100%.
- ZIP inventory and context-file presence check: 100%.
- Actual archived context retrieval across all workflow runs: NOT_COMPLETE (not claimed).
- Real FII/DII runtime schema validation: 0% / NOT_VERIFIED.
- Aggregation policy: BLOCKED.
- Adapter implementation and regression execution: 0% / NOT_STARTED.

## Scope protection

No production code, workflow, dataset, selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672 definitions, engines A–E, default branch, or PR state changed. No CI run was dispatched, no PR was merged, no paid API or spend was used.

## Next action

Search the relevant collector workflow runs' artifact inventories (not the replay artifact already inspected), download only a run artifact that advertises the context output, verify its archive SHA-256, and inspect `data/context/market_context.json` without altering it. If no such artifact is available, record the retention gap and design a separate, bounded research-only artifact-retention test; do not rerun the full 60-minute collector workflow.
