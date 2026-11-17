# BCB Portfolio Investment — Monthly Accounting Identity Audit
Date: 2026-11-17 | Research-only | Unit: USD million

Coverage: 381 common monthly observations, 1995-01 to 2026-09.
Acceptance: **PASS_ALL_6_IDENTITIES**. Raw CSV bytes and SHA-256 revalidated against both archived manifests.

| Identity | Pass / Total | Max absolute residual (USD mn) | Status |
|---|---:|---:|---|
| 22906 = 22908 - 22907 | 381 / 381 | 0.1 | PASS |
| 22924 = 22925 - 22926 | 381 / 381 | 0.1 | PASS |
| 22905 = 22906 - 22924 | 381 / 381 | 0.1 | PASS |
| 22906 = 22909 + 22912 + 22915 | 381 / 381 | 0.1 | PASS |
| 22924 = 22927 + 22936 + 22939 | 381 / 381 | 0.1 | PASS |
| 22939 = 22942 + 22945 | 381 / 381 | 0.1 | PASS |

## Sign conventions observed
- Assets net acquisition: 22906 = 22908 (outflows) − 22907 (inflows).
- Liabilities net incurrence: 22924 = 22925 (inflows) − 22926 (outflows).
- Portfolio investment net: 22905 = 22906 − 22924.

## Guardrails
- Reconciliation tolerance: USD 0.11 million, reflecting one-decimal-million SGS series precision.
- No forward-fill, imputation, fabricated observations or timestamps.
- Identities validate accounting consistency only; no causality, attractiveness, predictive power or 1–3 day signal eligibility.
- Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A–E remain unchanged. Production integration NOT_AUTHORIZED.

## Raw provenance
- SGS 22905: 381 rows; 1995-01–2026-09; 8908 bytes; SHA-256 76391aef708216f537ead5fb140730c2dbd55164373b9689634aaa45f96b4837; title: Portfolio investment - monthly - net.
- SGS 22906: 381 rows; 1995-01–2026-09; 8513 bytes; SHA-256 dfdcec3b7c1618c070063ce76f3b722fdd4dadeac5d5fe0f1205fad61af64eaf; title: Portfolio investment - Net acquisition of financial assets - monthly - net.
- SGS 22907: 381 rows; 1995-01–2026-09; 8486 bytes; SHA-256 14105f48a0954c0da0615f136fb8e95885259a47c3395164ef922667dee8bbbf; title: Portfolio investment - Net acquisition of financial assets - monthly - inflows.
- SGS 22908: 381 rows; 1995-01–2026-09; 8512 bytes; SHA-256 82917f2f093a87f95733ecadabda2d59e8ddbf782b64c150bbc41e1627c5f1d7; title: Portfolio investment - Net acquisition of financial assets - monthly - outflows.
- SGS 22924: 381 rows; 1995-01–2026-09; 8809 bytes; SHA-256 f3769425aed38b4ab6ddfce555f10d886d875d21e7c3e46338b7d9bc131524b2; title: Portfolio investment - Net incurrence of liabilities - monthly - net.
- SGS 22925: 381 rows; 1995-01–2026-09; 9005 bytes; SHA-256 44f5e93d196355fa9c99d649667d240aff1c217bfa7f2448a1e6863da59ab75e; title: Portfolio investment - Net incurrence of liabilities - monthly - inflows.
- SGS 22926: 381 rows; 1995-01–2026-09; 8987 bytes; SHA-256 b03dfecbc6617a4ce772388b2b3131943df4e1921e7637d6c8a6ee84ec3e463e; title: Portfolio investment - Net incurrence of liabilities - monthly - outflows.
- SGS 22909: 381 rows; 1995-01–2026-09; 8209 bytes; SHA-256 cbfe7caa331d814ef4801940d08bd1966f8bca9d9cd6a024b4e1cacf79a34382; title: Portfolio investment - equities - assets - monthly - net.
- SGS 22912: 381 rows; 1995-01–2026-09; 8385 bytes; SHA-256 f9552bad9d7aac7d6190fca1783a81c25ad0593d802b2b4570706ae270a8087f; title: Portfolio investment - investment funds - assets - monthly - net.
- SGS 22915: 381 rows; 1995-01–2026-09; 8357 bytes; SHA-256 0b2275648eb640cae39f3a900451aef316913ada7ca5ba9505324da24780faa1; title: Portfolio investment - debt securities - assets - monthly - net.
- SGS 22927: 381 rows; 1995-01–2026-09; 8666 bytes; SHA-256 6108baede8f25e95dce65943699fe915c5ebaa97e5c57f7b894ab62a56e0549c; title: Portfolio investment - equities - liabilities - monthly - net.
- SGS 22936: 381 rows; 1995-01–2026-09; 8006 bytes; SHA-256 0d1b040d5b11af0b1b98704a70f4972f2790bdfe3c6e78bb16948c7a31640e24; title: Portfolio investment - investment funds - liabilities - monthly - net.
- SGS 22939: 381 rows; 1995-01–2026-09; 8757 bytes; SHA-256 24080225e1758010a0f4f6fd995b0a5887a77395caa90a7365d74bab18a240ca; title: Portfolio investment - debt securities - liabilities - monthly - net.
- SGS 22942: 381 rows; 1995-01–2026-09; 8579 bytes; SHA-256 4c09c850decf3317d27d1c0f4dc4aa68dc4f0b3aa2aafacfece113ff7f9c7169; title: Portfolio investment - debt securities - liabilities - domestic market - monthly - net.
- SGS 22945: 381 rows; 1995-01–2026-09; 8705 bytes; SHA-256 452695200d21d72ae34fa972304b76f4418aaa6be1e838395cf4bba22061d563; title: Portfolio investment - debt securities - liabilities - external market - monthly - net.
