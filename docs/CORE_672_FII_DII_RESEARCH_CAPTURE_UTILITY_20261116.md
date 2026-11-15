# Isolated NSE FII/DII Raw Capture Utility

Date: 2026-11-16  
Status: **UTILITY COMMITTED; LIVE CAPTURE NOT RUN / NOT VERIFIED**  
Branch: `research/nse-raw-manifest-retention-20261115`

## Purpose
A one-off research utility was added at `tools/research/capture_nse_fii_dii.py`. It is isolated from production modules and workflows. It is intended to:
1. Save the official NSE FII/DII report HTML.
2. Bootstrap a public NSE website session.
3. Capture exact raw bytes from `https://www.nseindia.com/api/fiidiiTradeReact`.
4. Save a separately serialized parsed JSON copy.
5. Download the official NSE-only and combined NSE+BSE+MSEI CSVs.
6. Compute SHA-256 for every saved payload and write a local manifest.
7. Return exit code 2 and `ACCESS_BLOCKED` when any required capture cannot be completed.

## Run locally
Requires Python 3 and `requests`:
```bash
python -m pip install requests
python tools/research/capture_nse_fii_dii.py --out-dir /tmp/nse-fii-dii-capture
```

If the report HTML does not expose descriptive download-link text, copy the exact two CSV URLs from the official NSE report page and pass both explicitly:
```bash
python tools/research/capture_nse_fii_dii.py \
  --out-dir /tmp/nse-fii-dii-capture \
  --nse-only-csv-url 'EXACT_NSE_ONLY_URL' \
  --combined-csv-url 'EXACT_COMBINED_URL'
```
Replace placeholders only with URLs copied from the two distinct official NSE report controls. The utility checks that URLs use NSE domains and differ from one another.

## Security and retention
- Request cookies/session headers are not written to disk or manifest.
- Do not commit raw response, CSV payloads, cookies, session IDs, or tokens.
- The manifest includes the exact request URL, selected CSV URLs/labels, HTTP status/content type, timestamps, byte lengths and SHA-256 hashes.
- Review the manifest and raw payload locally before sharing. Redact any unexpected sensitive response fields before creating a report.
- Utility is not wired into CI, cron, scheduled collector, or production pipeline.

## Validation status and limitations
- GitHub file commit exists; source-level review only.
- Live NSE HTTP capture has **not** been executed in this environment.
- Python runtime/compile test has **not** been run here.
- CSV link discovery is intentionally fail-closed; if rendered labels are generic, supply the exact URLs manually.
- No claim is made that the API scope is NSE-only or combined until raw API values and both CSV rows are captured and compared for the same date.
- This utility does not calculate an aggregation window, freshness policy, market state, or CORE-672 signal.

## Progress
- Research-only utility authoring: 100%.
- Secret/cookie non-persistence guard: 100% source review.
- GitHub commit and retrieval verification: pending at report creation.
- Python compile/runtime test: 0% / NOT_RUN.
- Live API and official CSV capture: 0% / NOT_RUN.
- API-to-table scope reconciliation: BLOCKED.
- Production integration: 0% / NOT_AUTHORIZED.


## 2026-11-16 quality hardening addendum
- Source review found the first utility version accepted plain HTTP NSE URLs and retained CSV query strings in the local manifest. Hardened `safe_nse_url` to require HTTPS, an exact NSE-owned hostname or subdomain, no embedded username/password, and only default/443 port; malformed URLs return false.
- Added `manifest_url` and applied it to API and CSV URL fields so query strings/fragments (which may contain tokens) are not written to the manifest. Both CSV URL overrides must be supplied together.
- Added offline unit tests at `tools/research/tests/test_capture_nse_fii_dii.py`: official-host allowlist, hostile lookalike host rejection, HTTP rejection, credential/port rejection, malformed URL handling, query redaction, SHA-256 known vector, HTML anchor extraction, and byte-write hashing.
- GitHub source hardening commit: `9e08de5aef60ae876a1fd91e32d4db7796487485`; final manifest-redaction correction commit: `e2876b213826fa951b9cef92c9e1155b1c6da80f`, source blob SHA `b5d59bd284df342927814335ed7e8357f71cf7a0`.
- Offline test file commit: `66b7330e9b5980c3161f1f75f85eb8c372008a38`.
- Execution boundary: this environment has no DNS/outbound network (raw GitHub fetch from the shell failed with name-resolution error). Therefore Python compile/test execution and live NSE capture remain NOT_RUN. The test suite is committed but not PASS until run in a Python environment with `requests` installed. No Actions/CI run was triggered.
