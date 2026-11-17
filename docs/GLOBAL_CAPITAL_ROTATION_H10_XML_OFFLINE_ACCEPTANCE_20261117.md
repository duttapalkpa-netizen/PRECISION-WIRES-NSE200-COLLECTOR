# H.10 XML Offline Acceptance — Verification Record
Date: 2026-11-17 (Asia/Kolkata)
Status: LOCAL_RAW_XML_ACCEPTANCE_PASS; FRED_EQUIVALENCE_BLOCKED; CI_CAPTURE_PENDING_AT_CHECKPOINT

## Scope
This is a bounded, offline validation of the already preserved official Federal Reserve H.10 XML ZIP. It does not repeat network retrieval, alter source bytes, resolve unit metadata, reconcile against FRED, or authorize production migration.

## Source identity
- Input archive: previously downloaded artifact from capture Run 44061789458, artifact 14319270830.
- Local path used for this verification: /mnt/data/h10_fred_capture_44061789458/fed_h10_xml.zip
- ZIP byte length: 2,088,268.
- ZIP SHA-256: c424bcdfe0947e48d9bc3937fd3a9e82bf144e5ac6454ae95a68346196394c77.
- H10_data.xml byte length: 27,426,691.
- H10_data.xml SHA-256: 800cc039a51f4403fe37fb8c3dd9a23f874f890be03ba21eb44dc4c0d42555c8.

## Acceptance checks executed locally
All checks below passed against the exact preserved archive:
1. ZIP integrity: PASS; H10_data.xml exists.
2. Target series identity: exactly one SERIES_NAME=JRXWTFB_N.B.
3. Observation count: 5,445.
4. OBS_STATUS=A: 5,231; every value parses as a finite numeric value.
5. OBS_STATUS=ND: 214; every raw OBS_VALUE is -9999. These remain missing by status; never coerce to zero or forward-fill.
6. Dates: chronologically ordered, 5,445 unique dates, no duplicates.
7. Coverage: 2006-01-02 through 2026-11-13.
8. Status vocabulary: only A and ND observed.
9. Raw source metadata retained without normalization: UNIT=Index:_1997_Jan_100; UNIT_MULT=1.

Local verification result: PASS. This is an offline artifact acceptance result, not a GitHub Actions workflow PASS and not a FRED equivalence PASS.

## Durable regression test added
- File: qa/test_h10_xml_acceptance.py
- Commit: f6751c4ba516afeb3a72acf37dcb0c69d53fe17d
- The test requires an explicit H10_XML_ZIP path and skips when no archive is supplied. It validates ZIP integrity, unique target series, vintage-specific counts, date order/uniqueness/coverage, finite active values, ND sentinel preservation, and status vocabulary.
- Invocation: H10_XML_ZIP=/path/to/fed_h10_xml.zip python -m unittest qa.test_h10_xml_acceptance -v
- This new module has not yet been wired into a CI job with a durable archive input; do not represent it as CI-tested.

## Latest CI status at checkpoint
- Capture Run 44063756752 (#6), head commit a5f740220ccf3e2320db11f474c9cd4f30cea855: still in_progress when checked; capture job 133972010919 was in progress and no artifact was yet listed.
- Overlay Run 44063756763 (#241), same head commit: existing overlay unit-test job 133972010507 SUCCESS; embedded H.10 capture job 133972010867 still in_progress; no artifact was yet listed.
- The previous five segmented FRED windows all timed out. This new run is a code-triggered repeat from the same configured source route, not evidence that the network issue is solved. Wait for final status and inspect logs/artifact; do not dispatch another retry.

## Open blockers and next decision
- FRED full-history CSV retrieval and 5,445-date value/missingness equivalence: BLOCKED / NOT_DONE.
- XML UNIT metadata discrepancy (raw XML says Index:_1997_Jan_100 versus previously observed release table JAN06=100): OPEN / UNKNOWN. Do not relabel or apply the 1.014163 factor twice.
- Historical correction/vintage matrix and immutable long-term raw archive: NOT_DONE.
- Collector/registry migration: BLOCKED / NOT_AUTHORIZED.
- Next valuable work after CI settles: verify official Board unit-base and revision/vintage documentation, then write a provenance decision matrix; no production integration until evidence closes the blockers.

## Invariants
Research-only. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged. UNKNOWN never PASS. No synthetic data, no invented timestamps/hashes, no paid API or external spend (₹0).
