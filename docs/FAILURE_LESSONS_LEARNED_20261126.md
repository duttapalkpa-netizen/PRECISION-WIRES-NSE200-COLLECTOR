# Failure & Lessons Learned Research Log — 26-Nov-2026
## PRECISION-WIRES V11.3 | Observation-only pre-market review

**Review as-of:** 26-Nov-2026 08:40:05 IST  
**Market cutoff:** 25-Nov-2026 close  
**Next NSE session:** 26-Nov-2026; 24-Nov was an official equity-market holiday.

## 1. Run and source evidence

- Re-read Master Continuity Ledger C254, 25-Nov morning/nightly reports, 25-Nov failure register, Missed-Winner Integration note and prior Run #410 evidence.
- Run #411: run ID 45695700887; job 139492398062; artifact 15061666636; workflow head fa3220dbddf3dc204eb2f20d08a0a44af719950a; audit-branch commit f96f9e84; runtime approximately 8m35s.
- Artifact ZIP SHA-256 independently verified: 6685f9d5d092ff4a8fe505040b0a08f4183e78339a56a53bcfaa6d666d256897.
- Run #411 QA says 200 raw files, 200 requested dates, 3,001 symbols, 504,971 rows and 100% delivery coverage. This is not semantic acceptance: no raw per-file manifest or internal DATE1/session reconciliation is present in the artifact. Earlier reports conflict between 187 and 188 unique content sessions; unresolved.
- Artifact output hashes: latest_picks.csv bc489366de4cfad3811042d8ca9a362489039ed3fcd6eb2fb71e7f56c9f5bedc; watchlist_ledger.csv 3d4e04063b200044ae89529dc6f3b7349bd83d81b17ab19e3748e7ab4c58f3e2; walk_forward_metrics.json 1353f7df37fbbbf3f1bdebd9b9af16c812988e1ca866c2f8b0eb762ee461ef83; qa_report.json 77ee88c0ec576ce644597492174e3ab5a498662e5adf9443b83e85627f80599c.
- No raw source ZIP/per-file provenance, full-universe point-in-time decision ledger or full-universe matured outcome rows in the artifact.

## 2. Cohort maturity and failure status

- 23-Nov cutoff cohort: 7 unique symbols / 10 selector rows — BI, KDDL, ONIXSOLAR, SALASAR, SHALPAINTS, SHARDUL, UFBL.
- Run #411 watchlist ledger has populated T1_HIGH_PCT and MATURED_T1=True, but OUTCOME_LAST_DATE is blank. 24-Nov was an NSE holiday. Correct H+1/H+3/H+5 are 25-Nov/27-Nov/01-Dec. Therefore old T1 labels remain rejected/PENDING until 25-Nov row and exact horizon-end date are independently reconciled.
- 25-Nov cutoff cohort: 10 selector rows / 7 unique symbols — APLAPOLLO, ASHIKAG, NECCLTD, OAL, ORIENTLTD, PASHUPATI, SHALPAINTS. At 26-Nov pre-market all H+1/H+3/H+5 outcomes are PENDING; expected dates are 26-Nov/30-Nov/02-Dec.
- Full-universe missed winners and false negatives: UNKNOWN/BLOCKED. No reconciled point-in-time eligible-universe decision ledger or full-universe outcome rows.
- No selected-stock false positive/success label assigned to an immature or calendar-invalid row.

## 3. Raw model leads and admission audit

Run #411 CURRENT_WINNER_PROB raw leads (percentile ranks, not probabilities): SHALPAINTS 99.5620; APLAPOLLO 99.4526; PASHUPATI 99.4161; OAL 99.2336; NECCLTD 99.0876. None admitted to the Top-5 list.

- SHALPAINTS: official NSE quote page latest accessible 20-Nov close ₹97.42; loss-making for eight quarters, overall encumbered share >50%, impact cost 0.71, traded value ₹1.19 Cr. 25-Nov official close not verified.
- APLAPOLLO: official NSE close ₹1,476.00 on 25-Nov, −11.62%; ST ASM-1; 52-week low ₹1,342.20; 1W −31.70%, 1M −27.42%; traded value ₹6,638.38 Cr, delivery 26.39%.
- PASHUPATI: official NSE close ₹29.93 on 25-Nov, +4.98%; LT ASM-1; closed at its upper 5% band; 100% applicable margin; P/E >50 for prior four trailing quarters; traded value ₹12.75 Cr; 1M −28.26%.
- OAL: latest accessible official quote 20-Nov close ₹516.70, +20% upper band; 20% band; deliverable/traded quantity 2.73%; impact cost 0.32; 25-Nov price missing.
- NECCLTD: latest accessible official quote 20-Nov close ₹23.17; ST ASM-1; 50% margin; impact cost 1.27; traded value ₹71.81 lakh; 25-Nov price missing.

These are exclusion/admission observations, not matured forecast failures. No target probability, target price, stop or executable return inferred.

## 4. Existing immutable lessons updated, not duplicated

- PW-LSN-20261121-001 — forward-session label defect: OPEN; Run #411 aggregate metrics do not close it.
- PW-LSN-20261121-002 — H+5 JSON/CSV parity: OPEN.
- PW-LSN-20261121-003 — raw NSE source manifest/provenance: OPEN; no per-file raw manifest in Run #411 artifact.
- PW-LSN-20261123-001 — holiday/session spine: OPEN; 187/188 unique-session conflict unresolved.
- PW-LSN-20261124-002 — fail-closed source readiness: OPEN.
- PW-LSN-20261124-003 — high-touch vs close-to-close vs executable outcome: OPEN.
- PW-LSN-20261124-004 — CI/denominator reconciliation: OPEN.
- PW-LSN-20261124-005 — export manifest/provenance: OPEN.
- PW-LSN-20261125-001 — tracker treats next sorted row as next session and omits OUTCOME_LAST_DATE: OPEN. Run #411 provides another occurrence; 23-Nov cohort remains PENDING.

## 5. New immutable lesson

### PW-LSN-20261126-001 — Raw prospective model lead percentile is not a risk-qualified admission

**Evidence:** Run #411 latest_picks.csv and audit-branch source pipeline/live_prospective_selector.py. The selector produces percentile-based ranking fields but does not join current official surveillance, price-band, margin, impact-cost, fresh quote, catalyst timestamp or sector-validation fields. Official NSE quote pages show multiple current/stale risk flags among its five raw leads.

**Root cause:** VERIFIED at code/schema level — final admission/risk fields are absent from the raw selector output. Predictive impact or causal future loss is UNKNOWN.

**Why it escaped:** a percentile-ranked model lead can be mistaken for a qualified stock if the separate hard-gate audit is skipped.

**Research question:** Are all raw prospective leads independently reconciled against official NSE identity, price/time, volume/value/delivery, liquidity, price-band, ASM/GSM/surveillance, applicable margin, sector and cutoff-time catalyst before admission?

**Bounded test:** join each unique latest_picks symbol to the official NSE quote/security master and dated filings for the same cutoff. Retain exact URL, broadcast/retrieval time and raw hash. Stale/missing/unknown fields leave the slot unfilled.

**Leakage control:** use only data published by the original cutoff; no next-session price/news. Minimum 50 matured observations per state remains unchanged. This test is observation-only.

**Acceptance:** 100% symbol/ISIN/series and current price/time/risk fields independently reconciled; percentile never presented as probability; no production code, threshold or ranking change.

**Expected artifact:** prospective_risk_gate_admission_audit.json. Confidence: code-level gap HIGH; predictive impact UNKNOWN. Carry-forward: add to next morning and nightly checklists.

## 6. Next verification tests

1. calendar_aware_tracker_regression.json — 23-Nov→25-Nov/27-Nov/01-Dec; reject 24-Nov holiday row; require exact OUTCOME_LAST_DATE.
2. point_in_time_decision_ledger_audit.json — one row per eligible symbol/cutoff with inclusion/exclusion, rank, per-filter state, source timestamp and code/config hash.
3. universe_missed_winner_reconciliation.json — reconcile the accepted ledger to official NSE EOD high/close/corporate-action rows for +2/+5/+10/+15/+20 at H+1/H+3/H+5.
4. missed_winner_root_cause_audit.json — cutoff-only feature/catalyst reconstruction; exact filter attribution only with a decision trace.
5. prospective_risk_gate_admission_audit.json — raw lead vs official current risk/liquidity/freshness gates.

Keep each job bounded to 10 minutes and reuse existing evidence. Do not dispatch broad or long workflows.

## 7. আজকের শিক্ষা → গবেষণায় সংযোজন → পরবর্তী যাচাই

**আজকের শিক্ষা:** model percentile probability নয়; raw lead qualified নয়; holiday-invalid maturity labels must remain rejected.

**গবেষণায় সংযোজন:** append new Run #411 evidence to PW-LSN-20261125-001; register PW-LSN-20261126-001; carry forward the existing forward-label, H+5 parity, holiday spine, source provenance, timestamp, denominator and execution-outcome lessons.

**পরবর্তী যাচাই:** calendar-aware tracker regression first; then raw 25-Nov source manifest/session parity; then full-universe decision/outcome reconciliation and risk-gate admission audit. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672, Engines A–E and IPO-PLX V2.0 remain unchanged.
