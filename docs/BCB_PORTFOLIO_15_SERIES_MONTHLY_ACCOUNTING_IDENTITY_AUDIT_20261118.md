# BCB Portfolio — 15-Series Monthly Accounting Identity Audit
Date: 2026-11-18
Branch: `research/bcb-priority-metadata-audit-20261117`
Scope: research-only internal consistency check of 15 previously archived official Banco Central do Brasil (BCB) BCData SGS monthly portfolio-investment series. No new data download and no production integration.

## 1. Decision
All six tested monthly accounting identities reconcile within USD 0.1 million across 381 common monthly observations from 1995-01 through 2026-09. The maximum absolute difference for each identity is USD 0.1 million. This is consistent with the source series being published to one decimal place.

Result: **6/6 identities PASS × 381/381 months** at the stated tolerance.

This is an internal consistency result only. It does not establish complete BPM6 semantic equivalence, release-vintage stability, a country-level capital-attraction score, or a trading signal.

## 2. Series included
All 15 inputs were already archived in the two prior capture sets; this audit reused them and did not redownload or overwrite any raw source.

### Aggregate series (7)
- 22905 — Portfolio investment, monthly, net.
- 22906 — Portfolio investment, net acquisition of financial assets, monthly, net.
- 22907 — Portfolio investment, net acquisition of financial assets, monthly, inflows.
- 22908 — Portfolio investment, net acquisition of financial assets, monthly, outflows.
- 22924 — Portfolio investment, net incurrence of liabilities, monthly, net.
- 22925 — Portfolio investment, net incurrence of liabilities, monthly, inflows.
- 22926 — Portfolio investment, net incurrence of liabilities, monthly, outflows.

### Instrument-level series (8)
- Assets: 22909 equities; 22912 investment funds; 22915 debt securities.
- Liabilities: 22927 equities; 22936 investment funds; 22939 debt securities.
- Debt-liability split: 22942 domestic market; 22945 external market.

Provider: Banco Central do Brasil / BCData SGS. Unit: USD million. Both source manifests report complete raw-capture PASS: aggregate 7/7 and instrument-level 8/8; all 15 series report HTTP 200 and 381 observations.

## 3. Tested identities
| Identity | Formula | Result |
|---|---|---|
| Aggregate portfolio net | 22905 = 22906 − 22924 | 381/381 PASS |
| Assets net by instruments | 22906 = 22909 + 22912 + 22915 | 381/381 PASS |
| Assets net by direction | 22906 = 22908 − 22907 | 381/381 PASS |
| Liabilities net by direction | 22924 = 22925 − 22926 | 381/381 PASS |
| Liabilities net by instruments | 22924 = 22927 + 22936 + 22939 | 381/381 PASS |
| Debt liabilities split | 22939 = 22942 + 22945 | 381/381 PASS |

Tolerance: absolute difference <= USD 0.1 million, no wider tolerance. Maximum observed absolute difference for each identity: USD 0.1 million. The raw source values are expressed to one decimal place; small residuals are therefore treated only under this explicit rounding tolerance.

## 4. Sign and direction findings
- The asset-side net identity is outflows minus inflows: 22906 = 22908 − 22907.
- The liability-side net identity is inflows minus outflows: 22924 = 22925 − 22926.
- Aggregate portfolio net is assets net minus liabilities net: 22905 = 22906 − 22924.
- These signs are empirically supported by the six identities across the entire common monthly sample; do not reverse them based on an intuitive interpretation of “inflow” or “outflow”.

## 5. Exclusions / rejected assumptions
- Rejected the reversed asset flow formula (inflows minus outflows).
- Rejected the reversed aggregate net formula (liabilities minus assets).
- Did not infer any unobserved values, forward-fill, or create synthetic periods.
- Did not mix monthly BCB data with quarterly IMF BOP observations.
- Did not treat internal arithmetic agreement as proof of release-vintage correctness or exact cross-provider series equivalence.
- Did not calculate a country score, capital rotation ranking, portfolio-flow trigger or trade signal.

## 6. Reproducibility and evidence
- Script: `scripts/research/audit_bcb_portfolio_internal_identities.py`.
- Machine-readable QA: `data/qa/BCB_PORTFOLIO_INTERNAL_IDENTITY_AUDIT_20261118.json`.
- Existing raw aggregate manifest: `data/raw/bcb/priority_series_capture_20261117/manifest.json`; Git blob `8ece77e0c4fe64d7648d822fe37213ea8621915c`.
- Existing raw instrument manifest: `data/raw/bcb/instrument_net_capture_20261117/manifest.json`; Git blob `9a4657e53b00bfd3a8b9f7f86dfc535b86eedece`.
- The reproducibility script verifies each raw CSV byte length and SHA-256 against its manifest before computing identities. It fails closed for non-HTTP-200 capture, integrity mismatch, missing/duplicate/non-ascending periods, or failed identity.
- A separate GitHub Actions workflow runs the script on changes to the research capture/script inputs and uploads the machine-readable result. Runtime Actions confirmation is tracked separately; this document does not claim an Actions runtime pass.

## 7. Acceptance
| Gate | Status |
|---|---|
| Reuse of existing 15 raw captures | PASS |
| Six monthly accounting identities across 381 periods | PASS — computed from archived raw CSVs |
| Explicit rounding tolerance | PASS — USD 0.1m |
| Reproducible script added | PASS — committed; runtime pending |
| GitHub Actions runtime | NOT_VERIFIED until run evidence is inspected |
| Release vintage / revision attribution | NOT_DONE |
| IMF quarterly BFPA/BFPL semantic crosswalk | NOT_DONE |
| Brazil source admission to production registry | NOT_AUTHORIZED |
| EM-wide panel | NOT_DONE |
| Production integration / trading trigger | NOT_AUTHORIZED |

## 8. Next highest-value action
The next step is not another internal identity check. It is **prospective two-vintage revision comparison** for the 15-series panel: capture a second genuine timestamped BCB snapshot after a new official release, compare common reference months using exact raw hashes and values, and distinguish changed historical values from new observations. In parallel, keep the previously identified February-2026 SGS 22942 historical-vintage cause UNKNOWN until authoritative vintage evidence exists.

## 9. Invariants
₹0; official free sources only; no synthetic observations, inferred timestamps, forward-fill, or overwrites. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, parser admission and production workflows remain unchanged. No production integration authorized.
