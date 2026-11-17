# BCB Instrument-Level Net Series — Raw Capture & Reconciliation Results
Date: 2026-11-17
Capture Run #1 / ID `44077406268`: SUCCESS.
Artifact ID: `14326096168`.
Artifact ZIP SHA-256: `37dcb1d5f4ad2938741953a1b8aad0cea3030a34c4e83d565379f2dd43fa0090`.

## Raw capture
All eight instrument-level net series returned HTTP 200 and `text/csv; charset=utf-8`. Artifact was downloaded and inspected; each raw CSV hash and byte length matched the manifest.

| SGS | Instrument | Bytes | SHA-256 |
|---|---|---:|---|
| 22909 | Asset equities net | 8,209 | `cbfe7caa331d814ef4801940d08bd1966f8bca9d9cd6a024b4e1cacf79a34382` |
| 22912 | Asset investment funds net | 8,385 | `f9552bad9d7aac7d6190fca1783a81c25ad0593d802b2b4570706ae270a8087f` |
| 22915 | Asset debt securities net | 8,357 | `0b2275648eb640cae39f3a900451aef316913ada7ca5ba9505324da24780faa1` |
| 22927 | Liability equities net | 8,666 | `6108baede8f25e95dce65943699fe915c5ebaa97e5c57f7b894ab62a56e0549c` |
| 22936 | Liability investment funds net | 8,006 | `0d1b040d5b11af0b1b98704a70f4972f2790bdfe3c6e78bb16948c7a31640e24` |
| 22939 | Liability debt securities net | 8,757 | `24080225e1758010a0f4f6fd995b0a5887a77395caa90a7365d74bab18a240ca` |
| 22942 | Liability domestic-market debt net | 8,579 | `4c09c850decf3317d27d1c0f4dc4aa68dc4f0b3aa2aafacfece113ff7f9c7169` |
| 22945 | Liability external-market debt net | 8,705 | `452695200d21d72ae34fa972304b76f4418aaa6be1e838395cf4bba22061d563` |

All eight contain 381 monthly observations, 1995-01-01 to 2026-09-01, with unique ordered dates and no missing numeric values. All share the parent seven-series common monthly calendar.

## Candidate instrument identities
Exact Decimal arithmetic against the parent raw CSVs:

| Candidate identity | Months | Exact | Within ±0.1 USD mn | >0.1 |
|---|---:|---:|---:|---:|
| Asset net 22906 = 22909 + 22912 + 22915 | 381 | 253 | 381 | 0 |
| Liability net 22924 = 22927 + 22936 + 22939 | 381 | 266 | 381 | 0 |
| Liability debt 22939 = 22942 + 22945 | 381 | 295 | 381 | 0 |

All differences are 0 or ±0.1. This is rounding-consistent, not a formal PASS; no rounding tolerance has been approved. Do not force equality or alter source values.

## Status
- Eight child metadata records: PASS.
- Eight raw CSV captures + SHA-256: PASS.
- Structural coverage QA: PASS, 381/381 for each series.
- Instrument sum identities: PARTIAL_EMPIRICAL_ALIGNMENT.
- Country-period QA: NOT_DONE.
- Brazil pilot acceptance: NOT_ACCEPTED.
- EM-wide panel: NOT_DONE.
- Production integration: NOT_AUTHORIZED.
