# IMF BOP Continuation — Chapter 34 Progress Log
Date: 2026-11-17
Workstream: Global Capital Rotation & Relative-Attraction Overlay
Branch: `research/bcb-priority-metadata-audit-20261117`

## 1. Completed Tasks

| Task | Status | Evidence |
|---|---|---|
| Official IMF BOP DSD 2.6.0 raw acquisition | PASS | Run #2 / 44095286184 |
| BOP_BPM6 dataflow raw acquisition | PASS | HTTP 200, XML parsed |
| BOP_BP6_CONSTRAINT raw acquisition | PASS | HTTP 200, XML parsed |
| Actual dataflow-referenced DSD acquisition | PASS | IMF:ECOFIN_DSD:1.0 |
| Raw HTTP provenance, byte length and SHA-256 | PASS | Manifest capture 20261117T134325Z |
| Exact DSD/dataflow/constraint identity and attachment QA | PASS | Run #2 / 44095286184 |
| Portfolio indicator semantic candidate crosswalk | PASS | Run #1 / 44096119287 |
| GitHub raw evidence archive | PASS | Commit bd2a7d123b949f4ffcc426608a36de706a8fd658 |
| Crosswalk QA result committed | PASS | Commit 62e0e4132b9567bc4e8cd6ff82a7e3e9d8536dfc |

### Verified metadata facts
- IMF:BOP:2.6.0 DSD raw bytes: 895,438; SHA-256 `073afeeb971dfa797460ba2233c7af4aa7dfffe4908657b5364e24fc77314f2f`.
- IMF:BOP_BPM6:1.0 dataflow raw bytes: 22,078; SHA-256 `74a8f3a58ff3e0bc6e6681c4143cd042cc642edee06f8080e86c29dc3b64e919`.
- IMF:BOP_BP6_CONSTRAINT:1.0 raw bytes: 18,675; SHA-256 `aa6c002fb3a2498420ed8796621664b492c18f58d75918d5c1bf8737fc917656`.
- Actual referenced IMF:ECOFIN_DSD:1.0 raw bytes: 42,707,649; SHA-256 `81f4bf8bf43d466f94f8a429f8c8c40eccffe480845018421a1c384aae97d045`.
- All four HTTP responses returned 200 / application/xml; raw files and request/response metadata committed under `evidence/imf_bop_dsd/20261117T134325Z/`.
- Manifest content SHA-256: `e029afe097cb5267113663eb0a40b0c1990290c9ff8c1bf1c0469a080d6331fb`.
- Dataflow references ECOFIN_DSD:1.0, not BOP:2.6.0. This is a confirmed structural distinction, not an error to normalize away.
- Constraint: DATA_DOMAIN=BOP6; COUNTERPART_AREA=W1; 98 allowed indicator codes. Seven portfolio-related candidates are allowed: BFPA and BFPL in EUR/USD/XDC; BFP aggregate in EUR only.
- BFPA_BP6_USD = net acquisition of financial assets; BFPL_BP6_USD = net incurrence of liabilities. BFP_BP6_USD is not in the captured allowed list.
- BOP DSD concepts: FUNCTIONAL_CAT=P = Portfolio Investment; ACCOUNT_ENTRY=A = Assets (Net Acquisition of); L = Liabilities (Net Incurrence of).
- Crosswalk QA result blob SHA: `5bf166cf5bbcf36a5ce55738c185b96ae259b79c`.

## 2. Rejected List / Failure Lessons

- Direct equivalence between IMF:BOP:2.6.0 and IMF:ECOFIN_DSD:1.0: REJECTED; exact dataflow reference proves they are distinct structures.
- Treating BFP_BP6_USD aggregate as constraint-allowed: REJECTED; current constraint only includes BFP_BP6_EUR aggregate.
- Treating BFPL as equity-only FPI or gross inflow: REJECTED; metadata says net incurrence of liabilities, broader portfolio investment.
- Treating BFPA as gross outflow: REJECTED; metadata says net acquisition of financial assets.
- First acquisition attempts #44095045778 and #44095061664: FAIL; initial verifier assumed the wrong DSD reference and had an output-root error. Those failed attempts are preserved, not relabelled.
- Acquisition Run #44095238615: raw capture and semantic checks succeeded, but Git push was rejected because the branch advanced during the run. Artifact ID 14333906221 preserved the response. The corrected queued run was used for the canonical archive.
- No BOP_BPM6 observation panel, no reporter coverage pass, no actual-vs-estimate classification, no PIT vintage acceptance, no EM aggregation, and no production integration claimed.

## 3. Progress Percentages

| Work package | Progress |
|---|---:|
| Official structure metadata acquisition | 100% |
| Dataflow/constraint identity and attachment | 100% |
| Portfolio indicator semantic candidate crosswalk | 100% |
| BOP_BPM6 country observation pilot | 0% |
| Reporter-level actual/estimate and coverage gate | 0% |
| Historical vintage / PIT gate for this exact dataflow | 0% |
| EM portfolio-flow aggregation eligibility | 0% |

Percentages apply only to this Chapter 34 work package; do not present them as total overlay/project progress.

## 4. Exact Next Action Items

1. Inspect exact BOP_BPM6 SDMX observation key order and query contract from the captured ECOFIN_DSD/dataflow; do not reuse the older IMF Portal DSD24 key syntax without proof.
2. Run one bounded India quarterly observation pilot for the two constraint-allowed USD indicators `BFPA_BP6_USD` and `BFPL_BP6_USD`, with DATA_DOMAIN=BOP6 and COUNTERPART_AREA=W1; verify REF_AREA/FREQ values and exact key order from metadata before constructing a request.
3. Capture untouched response bodies, request/final URL, HTTP status, content type, retrieval UTC timestamp, byte length, SHA-256, and data attributes.
4. Reconcile indicator direction, currency/unit multiplier, frequency, periods, observation status, derivation type, actual-vs-estimate flags and publication/vintage metadata.
5. Compare with existing IMF Portal BOP dataset observations only as an independent cross-source check; never merge series or imply structural equivalence.
6. If the bounded pilot passes, extend reporter coverage using the already-built WEO/EMDE crosswalk and existing prior 154-country coverage work; do not repeat completed 2015–2025 coverage matrices.
7. Keep quarterly/annual BOP data as slow-moving macro context only. No 1–3 day trading trigger and no production integration.

## 5. Hard Invariants

₹0 spend; free official sources only; no credentials, paid APIs, external contact, synthetic observations, guessed timestamps, or inferred country eligibility. Preserve raw bytes and SHA-256. UNKNOWN remains UNKNOWN. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E, Hard Gate, parser admission and production workflows unchanged.

## 6. Main Evidence Links

- Acquisition run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44095286184
- Crosswalk QA run: https://github.com/duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR/actions/runs/44096119287
- Acquisition report: `docs/IMF_BOP_DSD_OFFICIAL_METADATA_ACQUISITION_20261117.md`
- Crosswalk report: `docs/IMF_BOP_PORTFOLIO_INDICATOR_SEMANTIC_CROSSWALK_20261117.md`
- Raw capture: `evidence/imf_bop_dsd/20261117T134325Z/`
- Crosswalk QA: `data/qa/IMF_BOP_BPM6_PORTFOLIO_INDICATOR_CROSSWALK_20261117.json`
