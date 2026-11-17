# India institutional-flow + Fed H.10 uploaded-file byte audit — 2026-11-17

Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Branch: research/global-capital-rotation-overlay-v1
Parent PR #20 remains OPEN / UNMERGED / DRAFT.
Scope: byte-level and arithmetic QA of existing Library CSV files supplied in prior project work. This is not independent source-download provenance verification.

## 1. NSE FII/FPI + DII CSVs

Two distinct uploaded CSV files were materialized and hashed:

| File | Bytes | SHA-256 |
|---|---:|---|
| `fii-dii-combined-latest.csv` | 218 | `2697546fa012f4c08449b37a3eb7d0f8298f296c25fd8ce4b7ca134c37999eb2` |
| `fii-dii-nse-latest.csv` | 218 | `b733444b5a846abb672226bc96448bc0baea2da0ad15fe810207fbe93aad7f18` |

Both contain two category rows dated 13-Nov-2026. Gross buy minus gross sell reconciles exactly to reported net:
- Combined NSE+BSE+MSEI: DII 11,745.95 - 13,999.53 = -2,253.58; FII/FPI 18,339.57 - 12,603.02 = +5,736.55 (INR crore).
- NSE-only: DII 10,561.32 - 12,532.05 = -1,970.73; FII/FPI 17,376.50 - 12,122.52 = +5,253.98 (INR crore).

Both copies of each file found in Library were byte-identical (same SHA-256); they are duplicate copies, not additional observations. Keep combined and NSE-only as separate scopes. The common date and category arithmetic are QA PASS for these supplied files only.

## 2. Fed H.10 recent slice

File: `FRB_H10(1).csv`
- Bytes: 813
- SHA-256: `c47d0f4b10e2cc5f541f91113d9c4d34bd9dfc72845b2313a99e68437ea7dad1`
- Series IDs: JRXWTFB_N.B (Nominal Broad Dollar Index), JRXWTFN_N.B (Advanced Foreign Economies), JRXWTFO_N.B (Emerging Market Economies).
- Unit metadata: Index, January 1997 = 100; multiplier 1.
- Ten daily observations, 2026-10-26 through 2026-11-06.
- Endpoint-to-endpoint change over this 9-interval slice: broad +0.227048%; advanced +0.254686%; emerging-market economies +0.200138%.

This is a short 10-observation slice, NOT a 20-session signal and NOT ICE DXY. The H.10 observation values and file structure can be parsed; do not populate `dxy_change_pct_20d`. The broad series belongs only in `fed_broad_usd_change_pct_20d` after a full valid 20-interval history is available.

## 3. Provenance and acceptance boundary

The files were found in the user's Library and exact bytes were hashed in the working environment. Their original official download URLs, source response headers, retrieval timestamps, and immutable source-download manifests are not embedded in the CSVs and were not independently recovered in this audit. Therefore:
- Supplied-file byte integrity: PASS.
- Gross/net arithmetic for both NSE CSV snapshots: PASS.
- H.10 schema/series/unit identification and 10-row slice calculation: PASS (bounded).
- Official raw-download provenance: NOT_VERIFIED.
- Historical panel / synchronized daily panel: NOT_DONE.
- 20-session Fed broad USD return: NOT_DONE.
- IMF BOP_AGG raw acquisition: NOT_DONE.
- Relative-attraction calculation and validation: NOT_DONE.

Do not infer that the user-supplied CSV bytes prove the original source retrieval route. Preserve the separate provisional status and distinct NSE scopes. No missing dates are filled, no duplicate copies are counted twice, no synthetic observations are introduced.

## 4. Next action

Acquire official raw source files with exact final URL, retrieved_at, response status, byte count, SHA-256, and schema/vintage metadata. Extend Fed H.10 broad USD history to at least 21 valid observations for a 20-interval calculation. Acquire CDSL daily raw bytes and IMF transaction observations; then construct the synchronized panel. No production changes, selector/ranking/CORE-672/Engines A-E changes, or PR merge.
