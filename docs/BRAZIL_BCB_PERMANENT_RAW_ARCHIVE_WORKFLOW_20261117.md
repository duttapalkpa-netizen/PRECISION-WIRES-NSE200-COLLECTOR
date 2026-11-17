# BCB Priority SGS — Permanent Raw Archive Workflow
Date: 2026-11-17
Purpose: Preserve the already captured and verified seven-series BCB raw CSV artifact in the research branch without re-fetching the source.

## Source artifact
- Capture Run #3 / ID 44075768714 — SUCCESS.
- Artifact ID 14324188933.
- Artifact archive SHA-256: `40a1ff44317b16ffb789b4669496628a048a94010113d55cd40161d6570ee6c8`.
- Seven raw CSV files and manifest already independently inspected; each per-file SHA-256 matched.

## Workflow
`.github/workflows/archive_bcb_priority_sgs_artifact.yml` downloads the exact existing artifact by run ID, verifies all seven raw files against the manifest, writes `.gitattributes` with `*.csv -text` to preserve original CRLF bytes, commits the files under `data/raw/bcb/priority_series_capture_20261117/`, then re-fetches each committed blob with `git show` and verifies SHA-256 again.

The workflow is bounded to 5 minutes, research branch only, and uses GitHub's built-in token with contents-write/actions-read permissions. It does not call BCB endpoints again.

## Acceptance
- Workflow implementation: COMPLETE.
- Runtime archive commit: PENDING.
- Re-fetch and per-file hash verification: PENDING.
- Until runtime completes, do not describe the raw bytes as permanently archived in Git history; the Actions artifact is retained for 90 days.
