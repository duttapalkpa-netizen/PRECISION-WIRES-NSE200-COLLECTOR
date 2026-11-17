# BCB Instrument-Level Net SGS — Permanent Raw Archive
Status: IMPLEMENTED ON RESEARCH BRANCH; RUNTIME PENDING
Source capture Run #1 / ID 44077406268; artifact ID 14326096168.
Artifact ZIP SHA-256: `37dcb1d5f4ad2938741953a1b8aad0cea3030a34c4e83d565379f2dd43fa0090`.
Eight instrument-net series raw CSVs passed initial manifest/hash inspection.

The archive workflow downloads the existing artifact (no BCB source re-fetch), verifies each raw file against its manifest, commits the original CSV bytes under `data/raw/bcb/instrument_net_capture_20261117/` with `*.csv -text`, and re-fetches each committed Git blob to verify SHA-256.

Targeted 5-minute workflow. Do not claim permanent archival until runtime commit and post-commit re-fetch pass.
