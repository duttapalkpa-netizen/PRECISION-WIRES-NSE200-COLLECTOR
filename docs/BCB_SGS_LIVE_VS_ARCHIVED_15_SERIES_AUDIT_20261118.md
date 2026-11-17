# BCB SGS Live API vs Immutable 15-Series Archive — Snapshot Equality Audit
Date: 2026-11-18
Research branch: research/bcb-priority-metadata-audit-20261117
Scope: compare the current official BCB BCData/SGS JSON observations against all 15 previously archived official SGS CSV series. No raw archive overwrite and no production integration.

## 1. Decision
The current official SGS API and the immutable 2026-11-17 archive are identical for all 15 series across all 381 common monthly observations from 1995-01 through 2026-09:
- Series: 15/15
- Overlapping series-month observations: 5,715
- Changed observations: 0
- Unchanged observations: 5,715
- February-2026 SGS 22942: archived 2,783.2; live API 2,783.2; delta 0.0 USD million.

This is a strong collector-integrity and current-snapshot stability result. It establishes that the 2026-11-17 archive did not corrupt or diverge from the live SGS API. It does NOT establish the original March-2026 Table 10 as-published value or revision cause.

## 2. February 2026 anomaly interpretation updated
The captured March-2026 workbook Table 10 row 24 is USD 2,579.49220364m. The current SGS API and 2026-11-17 raw archive both report USD 2,783.2m. Thus the +USD 203.70779636m difference is between the later-modified March-labelled workbook snapshot (HTTP Last-Modified 18-Oct-2026) and the current SGS observation. It is not a difference between the 2026-11-17 raw SGS archive and the current live API.

The official contemporaneous 27-Mar-2026 BCB press release rounds February domestic debt securities to USD 2.6bn, consistent with the workbook value. The exact original XLSX is still NOT_PROVEN; the date/cause by which the later SGS value reached USD 2,783.2m remains UNKNOWN / NOT_ATTRIBUTED.

## 3. Series comparison
All 15 series have 381 archived rows and 381 live rows, same coverage 1995-01 to 2026-09, and zero changed overlapping observations. Per-series raw CSV SHA-256, live JSON response SHA-256, and February-2026 values are recorded in:
data/qa/BCB_SGS_LIVE_VS_ARCHIVED_15_SERIES_20261118_SUMMARY.json

The full machine-readable GitHub Actions artifact includes each API response hash, archive hash, HTTP status, observation counts, overlap counts and changed-observation list.

## 4. Official source interpretation
- Official BCData/SGS JSON endpoint for series 22942: https://api.bcb.gov.br/dados/serie/bcdata.sgs.22942/dados?formato=json. Live response reports February 2026 = USD 2,783.2m and latest period 2026-09.
- BCB Open Data catalog defines 22942 as monthly net portfolio-investment debt securities liabilities issued in the domestic market, unit USD million, source BCB/Department of Economics. Catalog metadata last-updated field is 26-Mar-2026; that is the metadata record's update date, not the observation vintage. The live JSON API contains observations through 2026-09, so do not use the catalog metadata timestamp as the data-through date.
- Official catalog says the series is monthly and sourced from SGS; see https://opendata.bcb.gov.br/dataset/22942-portfolio-investment---debt-securities----issued-in-the-domestic-market---monthly---net.
- Official API response is a current snapshot, not a versioned release history.

## 5. Reproducibility and runtime
- Script: scripts/research/audit_bcb_sgs_live_vs_archived_15_series.py
- Workflow: .github/workflows/bcb_sgs_live_vs_archived_audit.yml
- Workflow Run #1: 44155240821 — SUCCESS; commit e5287c4056789cfc2387498d7d67174c40187fd9; job 134294094688; all 6 steps PASS.
- Artifact ID: 14361126097; name bcb-sgs-live-vs-archived-15-series-44155240821; 2,951 bytes.
- GitHub artifact digest and downloaded ZIP SHA-256 independently match: 767fd57b7307552beea3135da86220e6a45943c9ea5b2e91160b80c504355216.
- Extracted JSON SHA-256: 5a81ad698557bb4de61b24704a88cce226229004980efaf3cbf8eaec3a72f860.
- Artifact expiry: 2027-02-15.
- Summary committed as data/qa/BCB_SGS_LIVE_VS_ARCHIVED_15_SERIES_20261118_SUMMARY.json.

## 6. Acceptance
| Gate | Status |
|---|---|
| 15/15 official API endpoints HTTP 200 | PASS |
| Archive raw SHA/byte-length verification | PASS |
| 5,715/5,715 live-vs-archive observations equal | PASS |
| February-2026 SGS 22942 live/archive match | PASS |
| Archive collector integrity | PASS |
| Exact March original XLSX vintage | NOT_PROVEN |
| Exact revision date | UNKNOWN |
| Revision cause | UNKNOWN / NOT_ATTRIBUTED |
| Brazil pilot | NOT_ACCEPTED |
| Production integration | NOT_AUTHORIZED |

## 7. Next action
Do not repeat the 15-series API comparison or six accounting identities. The next task is to locate the exact original March-2026 BCB Table 10 XLSX or a pre-18-Oct-2026 immutable file version. If inaccessible, preserve the exact-vintage blocker and do not infer the revision cause.

## 8. Invariants
₹0; official/free sources only; no synthetic data, invented timestamps, forward-fill, raw overwrites or duplicate audit implementation. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E, Hard Gate, parser admission and production workflows remain unchanged.
