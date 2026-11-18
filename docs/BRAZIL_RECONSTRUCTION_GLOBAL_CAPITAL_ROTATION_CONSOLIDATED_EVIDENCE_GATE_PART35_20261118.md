# Brazil Reconstruction + Global Capital Rotation — Consolidated Evidence Gate Part-35
Date: 2026-11-18 (Asia/Kolkata)
Branch: qa/imf-brazil-parser-schema-path-hardening
PR: #39 (open/draft/unmerged; no merge authorized)

## Scope
This checkpoint uses the user's uploaded IMF Provision Agreement research archive and the saved Global Capital Rotation Acceptance Gap Matrix. It does not claim either workstream is complete.

## 1. Brazil — uploaded IMF PA archive reinspection
Archive: imf_pa_research(1).zip
Raw archive SHA-256: 8cb2ed4bd96c0b1c4d3f24d0530771a5868f55bba256213404d5acf22a3f2b45
Archive entries and raw-byte SHA-256:
- legacy_all.xml: 53,443,157 bytes; 75b7a55f5daafb0ce566593542f76874f202eeae6b4f09cb572f5372ef44be85
- v2_imf_all.xml: 52,420,642 bytes; 9c8e9c9157da0e3ce33ca23db5afbc25e2517e02f481c8688d3ad0ed7f13ff0e
- v2_all_agencies.xml: 592,196 bytes; 85b951126342dc1e5be7b104e676b519b1e9d1a857fa78a4d91b2a3e35637453
- manifest.json: 1,383,003 bytes; 0954644ea442a76e380cfc3e8ee2d95503fd9b05da088c853f17fd4c320aa903

Exact XML extraction independently repeated from all three PA payloads:
- legacy_all.xml: 1,003 ProvisionAgreement elements.
- v2_imf_all.xml: 992 ProvisionAgreement elements.
- v2_all_agencies.xml: 1,004 ProvisionAgreement elements.
- Each contains the same Brazil PA element:
  URN urn:sdmx:org.sdmx.infomodel.registry.ProvisionAgreement=IMF:BR_BOP_BP6(1.0)
  Name: Brazil Balance of Payments
  StructureUsage: IMF:BOP6(1.0), class Dataflow
  DataProvider: IMF:BR1
- This is a concrete PA-to-Dataflow/provider crosswalk. It is not historical registration chronology and does not prove the BCB XML is consistent with the PA.
- The independently recorded public IMF Registrations row lists provider IMF:BR1 with IMF:BOP6(1.0) and the BCB XML source URL, last updated 2026-10-26T11:47:29.000Z. Last Updated is not an original registration timestamp.
- Prior byte-captured BCB XML evidence declares Dataflow IMF:BOP_BPM6(1.0). The identifiers BOP6 and BOP_BPM6 remain distinct and the BR1 registry-vs-payload mismatch remains CONFIRMED / UNRESOLVED. No alias/equivalence was inferred.
- The archive is a current registry snapshot; it contains no demonstrated immutable event history. Public activity UI was inspected previously, but BR1 filtered registration history, downloadable transaction payload, and Brazil PA changelog bytes were not captured. Chronology remains BLOCKED/NOT_DONE.
- Exact live BCB XML bytes/HTTP metadata/raw SHA-256 still need a fresh retrieval. Do not substitute the IMF registry archive for the BCB payload.
- Exact primary SGS 22707 Sep-2026 value/raw bytes remain NOT_VERIFIED due to local DNS retrieval block; 6,869m remains SECONDARY_ONLY. Official BCB bulletin corroborates only rounded goods surplus ~USD 6.9bn. Do not promote it to exact primary series value.

## 2. Brazil parser/schema status
- Offline parser unit tests: 16/16 PASS, GitHub Actions Run #21 / ID 44329119370.
- SDMX-ML 2.1 authority/tag and direct dependency roots have been documented in Parts 31–32.
- Full recursive XSD dependency closure, archived schema bytes + raw SHA-256 manifest, and offline XSD validation remain NOT_DONE.
- Brazil reconstruction acceptance remains BLOCKED: Dataflow mismatch unresolved; registration chronology unavailable; full XSD validation incomplete; exact primary SGS 22707 value not archived.
- PR #39 remains open/draft/unmerged. No merge or production integration.

## 3. Global Capital Rotation — source matrix status
The saved page-27 acceptance matrix has 13 gaps. Its source-backed statuses are retained:
- GCR-01 cross-border flows: PARTIAL
- GCR-02 domestic institutional allocation: PARTIAL
- GCR-03 FX/currency carry: PARTIAL/UNKNOWN
- GCR-04 global rates/real yields: PARTIAL
- GCR-05 commodities/energy: PARTIAL
- GCR-06 volatility regime: PARTIAL
- GCR-07 market/sector relative strength: PARTIAL
- GCR-08 MF/ETF ownership: PARTIAL/UNKNOWN
- GCR-09 geopolitical/supply-chain stress: UNKNOWN
- GCR-10 macro regime/external balance: PARTIAL
- GCR-11 factor calculation: UNKNOWN; previous registry audit 0/35 fully available, 31 partial, 4 not connected
- GCR-12 historical validation/causal evidence: UNKNOWN
- GCR-13 operational auditability: INCOMPLETE

Key fail-closed decisions:
- No community mirror is promoted to official RBI/FBIL FX data.
- DXY provenance warning and cross-currency carry remain unresolved.
- US nominal yields alone do not close real yields or India G-Sec/FBIL curves.
- FPI/AUC changes are not treated as pure net flow.
- No headline-to-sector/stock beneficiary inference without measured transmission.
- No factor score, overlay rank, or stock selection is promoted without complete point-in-time inputs and no-lookahead validation.
- No synthetic backfill or forward-fill of missing/stale inputs.

## 4. Exact next acceptance actions
Brazil:
1. Obtain live BCB SDMX XML bytes and HTTP headers; hash raw bytes; parse Header/ProvisionAgreement/StructureUsage/Dataflow/Provider.
2. Resolve BOP6 vs BOP_BPM6 only through official structures, PA history/changelog, or an explicit IMF/BCB mapping; otherwise retain mismatch as BLOCKED.
3. Obtain BR1 filtered registration activity and transaction export with event timestamps/actions/URNs; if access boundary prevents export, document as external dependency, not PASS.
4. Complete recursive pinned SDMX-ML 2.1 XSD closure, raw archive manifest, and offline validation.
5. Retrieve official SGS 22707 date-filtered Sep-2026 JSON/CSV on a DNS-capable network, preserve response metadata and SHA-256, then reconcile exact value.

Global Capital Rotation:
1. Ingest and archive official daily NSDL/CDSL final flows and NSE provisional flows separately; reconcile revisions and market scope.
2. Replace USD/INR mirror with RBI/FBIL official reference series; qualify official DXY source; keep cross-currency basis/carry UNKNOWN unless official data is available.
3. Acquire US nominal + real yields and India G-Sec/FBIL curves with release timestamps and revisions.
4. Complete official AMFI/SEBI AUC/ETF holdings, NSE VIX/CBOE, EIA/World Bank commodity, macro CPI/WPI/IIP/BoP/reserves/trade and official geopolitical event registry.
5. Populate and test all 35 factor schemas, transformations, normalization, missingness and no-lookahead controls.
6. Run point-in-time rolling regime-aware H+1/H+3/H+5 backtest, ablation and cost-adjusted incremental-value analysis (matrix specifies 0.22% costs).
7. Implement immutable manifests, raw-byte hashes, staleness/schema drift gates and fail-closed UNKNOWN.

## 5. Invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56x12), Engines A-E unchanged. No paid APIs, no fabricated timestamps, no synthetic data, no trading admission, no production integration, no PR merge. UNKNOWN is not PASS.

## Acceptance decision
Brazil Reconstruction: INCOMPLETE / BLOCKED.
Global Capital Rotation: INCOMPLETE / BLOCKED.
Combined 100% acceptance: NOT MET. No overall completion percentage is asserted because the remaining gates are not closed and evidence weights are not reconciled.
