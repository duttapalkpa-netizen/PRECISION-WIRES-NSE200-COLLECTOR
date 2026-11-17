# BCB Instrument-Level Net SGS — Permanent Raw Archive
Status: PASS — RAW CSVs COMMITTED AND RE-FETCHED WITH SHA-256 VERIFICATION
Source capture Run #1 / ID 44077406268; artifact ID 14326096168.
Artifact ZIP SHA-256: `37dcb1d5f4ad2938741953a1b8aad0cea3030a34c4e83d565379f2dd43fa0090`.
Eight instrument-net series raw CSVs passed initial manifest/hash inspection.

The archive workflow downloads the existing artifact (no BCB source re-fetch), verifies each raw file against its manifest, commits the original CSV bytes under `data/raw/bcb/instrument_net_capture_20261117/` with `*.csv -text`, and re-fetches each committed Git blob to verify SHA-256.

Targeted 5-minute workflow. Do not claim permanent archival until runtime commit and post-commit re-fetch pass.


## Verified runtime result
- Archive workflow Run #1 / ID `44077573395`: SUCCESS.
- Source capture artifact ID `14326096168`; no BCB source re-fetch during archival.
- Permanent archive commit: `527a8d41c434609c980eb3181d491eac4fa6e822`.
- Durable path: `data/raw/bcb/instrument_net_capture_20261117/`.
- Committed contents: `.gitattributes`, `manifest.json`, and all eight SGS CSVs.
- The workflow verified each CSV's byte length and SHA-256 before commit, then re-fetched every Git blob and verified SHA-256 again. All eight passed.
