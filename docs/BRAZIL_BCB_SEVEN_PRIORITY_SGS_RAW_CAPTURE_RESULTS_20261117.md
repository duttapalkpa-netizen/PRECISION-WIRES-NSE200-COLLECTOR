# Brazil BCB Seven Priority SGS — Raw Capture & Structural QA Results
Date: 2026-11-17 (Asia/Kolkata)
Branch: `research/bcb-priority-metadata-audit-20261117`
Capture workflow: Run #3 / ID `44075768714` — SUCCESS
Artifact: ID `14324188933`, ZIP SHA-256 `40a1ff44317b16ffb789b4669496628a048a94010113d55cd40161d6570ee6c8`

## 1. Raw capture result
All seven official BCB SGS CSV resources were retrieved with HTTP 200 and Content-Type `text/csv; charset=utf-8`. The artifact was downloaded and independently inspected. The ZIP contains `manifest.json` and seven CSV files. Each raw file's SHA-256 and byte length were recomputed and matched the capture manifest.

| SGS | Bytes | SHA-256 |
|---|---:|---|
| 22905 | 8,908 | `76391aef708216f537ead5fb140730c2dbd55164373b9689634aaa45f96b4837` |
| 22906 | 8,513 | `dfdcec3b7c1618c070063ce76f3b722fdd4dadeac5d5fe0f1205fad61af64eaf` |
| 22907 | 8,486 | `14105f48a0954c0da0615f136fb8e95885259a47c3395164ef922667dee8bbbf` |
| 22908 | 8,512 | `82917f2f093a87f95733ecadabda2d59e8ddbf782b64c150bbc41e1627c5f1d7` |
| 22924 | 8,809 | `f3769425aed38b4ab6ddfce555f10d886d875d21e7c3e46338b7d9bc131524b2` |
| 22925 | 9,005 | `44f5e93d196355fa9c99d649667d240aff1c217bfa7f2448a1e6863da59ab75e` |
| 22926 | 8,987 | `b03dfecbc6617a4ce772388b2b3131943df4e1921e7637d6c8a6ee84ec3e463e` |

All seven CSV files use UTF-8, header `data;valor`, semicolon delimiter, DD/MM/YYYY dates, and decimal comma. Each contains 381 monthly observations from 1995-01-01 through 2026-09-01. All seven date sequences are unique, strictly increasing, and have complete common monthly coverage over this interval. No numeric values were missing.

## 2. Empirical net/component identity checks
Using exact Decimal arithmetic on the displayed CSV values:

| Candidate identity | Tested months | Exact matches | Within ±0.1 USD million | >0.1 difference | Maximum absolute difference |
|---|---:|---:|---:|---:|---:|
| 22906 = 22908 − 22907 | 381 | 275 | 381 | 0 | 0.1 |
| 22924 = 22925 − 22926 | 381 | 283 | 381 | 0 | 0.1 |
| 22905 = 22906 − 22924 | 381 | 285 | 381 | 0 | 0.1 |

Interpretation: the proposed sign orientation is empirically consistent to within one displayed decimal unit for all 381 months, with 0.0 / ±0.1 differences only. This is not a formal PASS of the series accounting identity: the CSV exposes only one decimal place, and no approved rounding tolerance has been established. Do not round, adjust or overwrite source observations to force exact equality.

## 3. Official methodology boundary
- The BCB official Financial Account methodological note defines financial transactions as net changes in assets (acquisitions less disposals) and net changes in liabilities (issuance less repayment), and defines the financial-account balance as net changes in financial assets less net changes in liabilities: https://www.bcb.gov.br/htms/infecon/patflu/arquivos/notametod_contafinanc_contapatrim.pdf
- BCB's BPM6 hierarchy places 22905 under Portfolio Investment, 22906–22908 under Assets, and 22924–22926 under Liabilities: https://dadosabertos.bcb.gov.br/pages/temas
- The current BCB external-sector statistical framework states that Brazil compiles external-sector statistics under BPM6: https://www.bcb.gov.br/content/estatisticas/Documents/notas_metodologicas/balanco_pagamentos/bpm6/Nota%20Explicativa%20-%20Indicadores%20do%20Setor%20Externo.pdf
- The general methodology supports the broad asset-minus-liability sign logic. The empirical data supports the candidate component orientation, but a series-specific explanation mapping Portuguese `receita/despesa` to the selected SGS codes is still required before accounting acceptance.

## 4. Acceptance status
- Official metadata identities: PASS (prior audit).
- Raw CSV capture: PASS, 7/7.
- HTTP metadata, byte lengths, SHA-256: PASS, 7/7.
- Structural monthly coverage QA: PASS, 381/381 rows per series.
- Candidate net/component arithmetic: ROUNDING-CONSISTENT; formal tolerance approval pending.
- Series-specific sign/perimeter methodology: PARTIAL / UNKNOWN.
- Country-period independent cross-check: NOT_DONE.
- Brazil pilot acceptance: NOT_ACCEPTED.
- EM-wide panel: NOT_DONE.
- Trusted feature admission / production integration: NOT_AUTHORIZED.

## 5. Reproducibility
The deterministic audit script `scripts/research/audit_bcb_priority_sgs_csv.py` reads the captured raw CSVs and manifest, verifies each raw SHA-256, validates exact dates and rows, and computes the three identities without altering source values. Its output is `qa_report.json` in the capture directory. The raw capture artifact remains retained by GitHub Actions for 90 days; permanent raw-byte repository archival is a separate pending step and must not be claimed until a committed archive can be fetched back and re-hashed.
