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
- The manifest includes query-free request URL provenance (scheme/host/path), selected CSV URL paths/labels, HTTP status/content type, timestamps, byte lengths and SHA-256 hashes. Query strings and fragments are intentionally omitted to avoid token leakage.
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


## 2026-11-16 offline test-path correction and bounded helper validation
- Reviewed the committed test module and found its import path used `Path(__file__).parents[2]`, which resolved one directory too high. Corrected it to `parents[1]` so the test imports the sibling capture utility from `tools/research/`.
- Test correction commit: `b4509318799b72ff23e7ddec5b18111a41dee9c3`; test blob SHA `41be6239d896e1a0c4229fc9e49c0b9d4a9fc80f`.
- Because DNS prevented fetching the exact repository checkout into the local shell, executed a temporary offline helper harness reconstructed from the committed utility's helper functions and the same seven test cases. Python 3.13.5 and requests 2.32.5 were present. Harness py_compile PASS; 7/7 helper tests PASS in 0.002 sec. This does NOT count as execution of the exact committed repository checkout or its complete main() capture flow.
- Exact GitHub checkout py_compile/test execution remains NOT_VERIFIED; live NSE capture remains NOT_RUN. Do not upgrade repository test status to PASS until the exact committed files are run in GitHub Actions or a network-enabled checkout.

## 2026-11-16 follow-on source hardening: exception URL/token leakage
- Static review of the exact GitHub source identified that exception text was copied into capture_manifest.json. HTTP/request exceptions can include full URLs, including query parameters. Replaced raw exception message serialization with exception class plus a fixed diagnostic string; request headers/cookies and URL query tokens are not serialized through this error field.
- Source commit: 6eb13368faae01c4b054dcfb6df74d835c25f246; source blob SHA: 534a290ab5ec244150e97cce1b92de9c7076dea5.
- Exact committed test suite remains NOT_RUN in this environment; prior bounded helper harness 7/7 PASS is not a substitute. Live capture NOT_RUN. Re-run exact suite after this source change before any capture attempt.
## 2026-11-16 execution-path capability check
- Inspected the research branch workflow directory. Existing workflows include unrelated test/acquisition workflows; no dedicated NSE FII/DII capture-utility unit-test workflow exists.
- The available GitHub connector exposes repository/file reads and workflow-run/artifact/log reads, but no workflow_dispatch/run-workflow action. Therefore this session cannot trigger a GitHub Actions run through the connected GitHub capability. No workflow file was added and no production workflow was touched.
- Exact committed tests remain NOT_RUN; live NSE capture remains NOT_RUN. Next valid execution path is a user-triggered Actions run after adding/reviewing a dedicated test-only workflow, or running the exact checkout in a network-enabled Python environment. Do not report PASS until the exact committed checkout runs.
## 2026-11-16 dedicated manual-only test workflow added
- Added `.github/workflows/nse_fii_dii_capture_unit_tests.yml` on the research branch. It is `workflow_dispatch` only, has `contents: read`, a 5-minute job timeout, Python 3.12, installs the sole runtime dependency (`requests`), compiles the utility, and runs only `test_capture_nse_fii_dii.py` offline. It does not call NSE, upload artifacts, access secrets, or touch production collector workflows.
- Workflow commit: `91f116a2dd426427845dd8bf4343cb8c6b0e259f`.
- This connector cannot dispatch a workflow run. The workflow is committed but NOT_RUN. User can start it from GitHub Actions → 'NSE FII-DII Capture Utility Unit Tests' → Run workflow, selecting branch `research/nse-raw-manifest-retention-20261115`.
- Expected scope is py_compile plus 7 unit tests; do not call it PASS until a completed GitHub Actions run confirms success.

## 2026-11-16 exact GitHub Actions execution evidence
- GitHub Actions Run #13: run ID `43869585899`; workflow ID `419761357`; workflow commit `c130ebbd919cf07b74e1841cb123862e0b95a4ce`; branch `main`; conclusion SUCCESS; elapsed 11 seconds.
- Job `capture-utility-tests`, job ID `133306894900`: SUCCESS. Actual checkout was `research/fii-dii-contract-tests-20261116` at commit `e551cf303c48efa2c050fc1fe8b5328531aa7de0`.
- Python 3.12.16; `py_compile` PASS.
- Exact committed capture utility offline suite: 7/7 PASS.
- Exact committed FII-DII mapping contract suite: 14/14 PASS.
- Total: 21/21 offline unit tests PASS. The log shows no NSE HTTP capture command; live capture remains NOT_RUN.
- This is an execution result for the isolated research branch only. It does not authorize production mapping or establish actual CSV/API scope.
