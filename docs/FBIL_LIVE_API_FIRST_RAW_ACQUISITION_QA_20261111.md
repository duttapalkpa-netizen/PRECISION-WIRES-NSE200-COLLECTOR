# FBIL Live API Acquisition and Validation — 2026-11-11

## Executive result

**PASS — live transport, raw response acquisition, and scoped payload validation for 15–16 October 2026.**

**NOT DONE — recent-window data availability, full history, and production integration.**

## Acquisition evidence

- Official endpoint: `https://www.fbil.org.in/wasdm/refrates/fetchfiltered`
- Request window: 2026-10-15 through 2026-10-16
- Query: `authenticated=false`
- Retrieval UTC: 2026-11-11T07:55:32.114141+00:00
- Retrieval IST: 2026-11-11T13:25:32.114141+05:30
- HTTP status: 200
- Content-Type: application/json
- Raw response size: 1,919 bytes
- Raw response SHA-256: `aeec99630a30d4b5961755c35e05b1e795dec1c39a373e48d95eca5edd165e27`
- JSON root: array
- Raw records: 14
- Workflow run: `42983033561`
- Workflow job: `130397653955`
- Artifact ID: `13837574133`
- Artifact ZIP SHA-256: `48340a456b11aa8b3cc7e6133d00dcd92794b08c8460cbe65742cc25986c56f4`
- Workflow conclusion: success; validator step success; artifact uploaded.

## Validated panel

The fail-closed validator emitted 14 rows: 7 currency products × 2 dates:
- USD, GBP, EUR, JPY (quoted per 100), AED, IDR (quoted per 10,000), RUB.
- All 14 date-currency keys unique.
- All rates numeric, finite and positive.
- Both dates inside the requested range.
- No synthetic rows, gap fill, forward fill, or OHLC derivation.

The 8 overlapping USD/GBP/EUR/JPY cells on 15–16 October match the separately inspected FBIL and NSE public displays (8/8). AED/IDR/RUB are retained as API-returned observations; no independent display parity is claimed for those six cells.

## Freshness probe

A separate request for 2026-11-09 through 2026-11-11 returned:
- HTTP 200
- Content-Type application/json
- Raw size 2 bytes
- SHA-256 `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- JSON array with 0 records

This is **EMPTY_ARRAY / UNKNOWN availability**, not a transport failure. The probe occurred at 13:25 IST. Since the published fixing is normally released around 13:30 IST, publication timing is a plausible explanation, but it is not proven by this single observation. A later same-day retry is required before diagnosing a recent-data outage.

## Repository archive

- Raw JSON: `data/fbil_reference_rates/raw/fbil_reference_rates_20261015_20261016.json`
- Metadata manifest: `data/fbil_reference_rates/manifests/fbil_reference_rates_20261015_20261016.metadata.json`
- Validated panel: `data/fbil_reference_rates/derived/fbil_reference_rates_20261015_20261016.csv`

The raw response is archived unchanged in the repository. The original workflow artifact is also retained for 30 days as independent acquisition evidence.

## Gate decision

| Gate | Status |
|---|---|
| Live HTTP access from GitHub Actions runner | PASS |
| HTTP 200 + JSON response | PASS |
| Non-empty historical response | PASS |
| Raw bytes + SHA-256 | PASS |
| Fail-closed payload validator | PASS |
| 14-row / 14-key structural QA | PASS |
| FBIL–NSE overlap (8 cells) | PASS |
| Recent-window response | EMPTY_ARRAY; retry required |
| Full historical backfill | NOT DONE |
| Daily scheduled collection / missed-day recovery | NOT DONE |
| RBI-primary interbank OHLC | BLOCKED / separate source |
| Factor Registry integration | NOT CONNECTED |
| Production integration | NOT DONE |

## Progress accounting

This closes the FBIL live-access and first historical-sample acquisition subtask. It does not close full historical coverage, the USD/INR OHLC source, Macro-Geo P0, Factor Registry, event-study maturity, or production integration. Therefore the overall V11.3 percentage remains `NOT_CALCULABLE`; no percentage is increased for partial source acquisition alone.

Production selector, `RANKING_SCORE`, `+1 PRESSURE_FADE`, CORE-672, Engines A–E, and Hard Gate are unchanged. Research spend remains ₹0.


## Follow-up: post-publication and date-format diagnostic (13:44–13:45 IST)

Two additional post-13:30 IST runs were completed to test whether the earlier empty recent window was merely a pre-publication timing issue.

### Run A — 13:44:34 IST
- Workflow run: `42985468800`
- Artifact ID: `13839811307`
- Artifact ZIP SHA-256: `c4abc815b0ebfa2a25693582676624b1af8ae537adefbbdc8e8d02536cefa795`
- Historical control (15–16 Oct): HTTP 200, 14 records, same raw SHA-256 as first capture.
- Recent window (9–11 Nov): HTTP 200, 2-byte empty JSON array, SHA-256 `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`.

### Run B — 13:45:54 IST, zero-padded date parameters
- Workflow run: `42985646860`
- Artifact ID: `13839361982`
- Artifact ZIP SHA-256: `be9fff6123f769b3bc7e4cac7ae55019bb162d3cfe589df2bb1de7e0b71ba6fe`
- Request dates explicitly zero-padded as YYYY-MM-DD.
- 05–06 Nov: HTTP 200, empty array.
- 07–11 Nov: HTTP 200, empty array.
- 15–16 Oct control: HTTP 200, 14 records, same raw SHA-256.

### Diagnosis

- Pre-publication timing alone does **not** explain the empty recent-window result: the same dates remained empty after 13:30 IST.
- A date-format bug was found and corrected (un-padded day values were being sent for single-digit days). The zero-padded retest returned the same empty result; therefore date padding was not the root cause.
- The FBIL endpoint is demonstrably reachable and returns historical October observations, but its accessible data window appears stale or otherwise excludes 05–11 November in these tests. Exact cause remains **UNKNOWN**; do not label it a confirmed outage or infer a documented retention policy.
- The NSE page's display of 05-Nov is a separately observed public display and does not prove that the API endpoint's JSON backend contains that date.

### Updated gate

- FBIL API live access: **PASS**
- Historical sample acquisition (15–16 Oct): **PASS, 14 rows**
- Recent API availability for 05–11 Nov: **EMPTY_ARRAY, REPRODUCED**
- Root cause of recent API emptiness: **UNKNOWN**
- Full historical backfill / production daily collector: **NOT DONE**
- No recent rows admitted; no imputation, no forward fill, no synthetic observations.
