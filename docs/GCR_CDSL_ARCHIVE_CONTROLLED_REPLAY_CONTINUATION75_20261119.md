# GCR CDSL Archive Controlled Replay — Continuation 75
Date: 2026-11-19

## Run and artifact
- Workflow: GCR Official India FPI Raw Page Capture
- Run ID: 44521501249 — SUCCESS
- Artifact ID: 14527843295
- Artifact: gcr-india-fpi-raw-pages-4.zip
- ZIP size: 195,431 bytes
- GitHub artifact digest and independently recomputed ZIP SHA-256: 2c8952476f58637c0f346e695793d2b8c8fd170dac551386ace1e37e0e7aea99
- Manifest: 8 sources, 8 HTTP 200, 0 non-200/error.
- Manifest SHA-256: 80dd5662a619f44fe9a661dcc64d4895286efddce1d2ea2ce01529661a43c239
- Summary SHA-256: bcf9b4749ab416fc1835609e0ac143d6623088169957ccd881c6c5a28502e880

## CDSL archive response
- Requested source: https://www.cdslindia.com/Publications/ArchiveDataAfter2009.aspx
- HTTP 200; body 70,430 bytes; SHA-256 3cd92be518721d84e697d42e3f2f8dc8cd6a03df6efea75a3576bf384132c2ec
- Visible archive date in this replay body: 01-Jul-2021 only.
- Previous captures of same URL:
  - Artifact 14524707532: body 297,824 bytes; SHA-256 fc95dc0dade735c9f413ef20a3239e138a6064f2694633aa9635864fd8c7ba2b; 13 visible dates 02–18-Nov-2026.
  - Artifact 14527092174: body 73,784 bytes; SHA-256 aa2a03c6621772e52b0b9ac52f11b525d82f1ce80539554302eda861145304df; one visible date 02-Mar-2026.
  - Artifact 14527843295: body 70,430 bytes; SHA-256 3cd92be518721d84e697d42e3f2f8dc8cd6a03df6efea75a3576bf384132c2ec; one visible date 01-Jul-2021.
- All three responses were HTTP 200. Response size/date coverage materially differs. HTTP 200 does not establish a valid complete archive export.
- Strongest supported interpretation: the initial GET response is sensitive to server-side/default date-selection state and is not a stable complete archive extract. This is not proof that the archive dataset itself is absent or corrupted.
- No POST, form submit, credentials, or undocumented endpoint used. Need inspect documented date selector/form controls and publicly exposed GET links/scripts before any selected export.

## Acceptance
- Replay workflow and ZIP digest: PASS.
- 8/8 page HTTP response status: PASS.
- CDSL archive reproducible complete coverage: BLOCKED.
- Matched-date NSDL/CDSL flow reconciliation: NOT_DONE.
- Production India FPI ingestion: BLOCKED.

## Brazil parallel finding
- IMF official registrations show Brazil IMF:BR1 registered to IMF:BOP6(1.0) and BCB URL; other providers appear under IMF:BOP_BPM6(1.0).
- IMF Reporting Constraints lists BOP_BP6_CONSTRAINT for BOP_BPM6[1.0].
- IMF May-2025 Web Services Guide separates public GET structure queries from private authenticated POST registration/re-registration. Its example distinguishes Dataflow IMF:BOP_BPM6(1.0) from DATA_DOMAIN BOP6.
- These facts do not establish Brazil-specific equivalence/crosswalk. PA Changelog and BOP6/BOP_BPM6 identity remain BLOCKED pending exact PA revision export and authoritative mapping/provider evidence.
- Detailed Brazil identity/access report: docs/BRAZIL_IMF_DATAFLOW_IDENTITY_ACCESS_BOUNDARY_CONTINUATION75_20261119.md, latest commit e91ec3d3f5a5cd519be289509359aa354bd50f39.

## Invariants
₹0; official/free sources only; UNKNOWN is never PASS. No synthetic data, interpolation, inferred gross legs, unapproved conversion or alias. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E unchanged.
