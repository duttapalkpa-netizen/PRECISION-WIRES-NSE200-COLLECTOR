# GCR Continuation 292 — Nigeria IMF/CBN vintage-attribute semantics audit
Date: 2026-11-28 (Asia/Kolkata)
Task ID: GCR-C292-NGA-VINTAGE-SEMANTICS-01
Scope: Research-only, bounded audit of whether existing Nigeria Q2-2026 IMF rows establish a same-vintage bridge to the national CBN observations.

## 1. Preflight / duplicate prevention
- Re-read current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, immutable 63-country matrix and C291 report before selecting this task.
- Reused existing Nigeria IMF/CBN dual-leg comparison report (6/6 numeric comparisons PASS), existing IMF raw CSVs and CBN Q2-2026 BOP Highlights; no IMF re-query, no CBN re-download, no cohort rebuild and no repeated asset/liability arithmetic.
- Reused C291 independent second-publication corroboration from the CBN Q2-2026 Economic Report. This task tests metadata semantics only.

## 2. Existing evidence re-inspected
- IMF raw asset CSV: `docs/evidence/gcr_nigeria_bop_20261119/IMF_NGA_A_NFA_T_P_F_Q.csv`; Git blob SHA-1 `75b5df0e3768392dba3740cbc2f1e16faeeb9cc5`; original SHA-256 retained in C289/earlier Nigeria report: `4e7ea3a3f3e171e7b72895ff1b0ad32ee4e8cbba69cf48d2bc2f63f7d2419f24`.
- IMF raw liability CSV: `docs/evidence/gcr_nigeria_bop_20261119/IMF_NGA_L_NIL_T_P_F_Q.csv`; Git blob SHA-1 `b754a4ac71fcb08e7be8c69af6e2480f1c19cd7e`; original SHA-256: `c6e5bec075e950aa6731380b78c0293a15f38fc7c69a725574971ce115584c45`.
- Both CSVs identify dataflow `IMF.STA:BOP(21.0.0)`, country NGA, quarterly USD, portfolio investment (P_F), Q2-2026 observations. Both rows carry `ACTION=R`; the exported `STATUS` field is blank in the captured Q2-2026 rows. No observation-specific publication date, revision timestamp, CBN release ID, IMF receipt ID or common vintage key is present in these captured rows.
- Existing CBN report identifies Q2-2026 BOP statistics as provisional. C291 found the same A/L values in two distinct CBN Q2-2026 publications, but neither inspected report provides an observation-level revision identifier linking the CBN values to the archived IMF receipt.

## 3. Critical SDMX interpretation — correction to prevent false PASS
The SDMX data-message specification defines dataset `action` as the sender's intended processing instruction (e.g. Replace, Append, Delete, Information). It is not an observation's statistical vintage or revision-status timestamp. The SDMX technical documentation describes Replace as a data-message action. Therefore IMF CSV `ACTION=R` means Replace in the message semantics; it does **not** mean that the Q2-2026 statistical observation is a revised/final value or that it matches the CBN provisional vintage.

Source: SDMX-JSON Data Message specification, section 2.4.1 “action”, https://sdmx.org/wp-content/uploads/sdmx-json-data-message.pdf
Corroborating SDMX-CSV field guide: https://github.com/sdmx-twg/sdmx-csv/blob/master/data-message/docs/sdmx-csv-field-guide.md

## 4. CBN source boundary
- Official Q2-2026 BOP Highlights explicitly labels the Q2-2026 BOP statistics provisional. Official source: https://www.cbn.gov.ng/Out/2026/STD/Q2%202026%20BOP%20Highlights_%20revised.pdf
- Separate official CBN Economic Report, Second Quarter 2026, independently repeats portfolio assets USD0.70bn and liabilities USD7.09bn, but the cross-publication match is not an observation-specific vintage bridge. Official source: https://www.cbn.gov.ng/Out/2026/RSD/Second%20Quarter%202026%20Economic%20Report.pdf
- Publication/report date or the date on which a file was retrieved is not, by itself, the statistical vintage date. IMF CSV retrieval on 19-Nov-2026 records when this research artifact was captured, not necessarily when the underlying observation was first submitted or last revised.

## 5. Decision
| Test | Result | Reason |
|---|---|---|
| Existing IMF raw rows and keys re-inspected | PASS | Both raw CSVs and Q2-2026 rows present; no re-query needed |
| CBN Q2 provisional status | PASS | Explicitly stated by official BOP Highlights |
| CBN independent publication corroboration | PASS (reused C291) | Two CBN publications match A/L values |
| Meaning of IMF ACTION=R | PASS | SDMX action is message-processing instruction, not vintage flag |
| Observation-level IMF revision/publication timestamp | NOT_CAPTURED | No such field/value in captured CSV rows |
| Exact same-vintage bridge CBN ↔ IMF | NOT_ESTABLISHED | No common release/revision identifier or matched vintage timestamp |
| Nigeria VINTAGE_PASS | NO — remains PENDING | Evidence insufficient |
| Nigeria FULL_PASS / aggregate admission | NO / NOT_AUTHORIZED | Existing hard gate unchanged |

## 6. Research impact
This audit prevents a potentially serious false-positive: treating `ACTION=R` as evidence that the IMF Q2 observation is revised and therefore aligned with CBN. That interpretation is rejected. The task improves metadata semantics and protects the cohort from an unsupported VINTAGE_PASS, but it does not promote Nigeria or the aggregate.

## 7. Exact next evidence needed
Only pursue a supported, public, official, observation-specific metadata source that supplies:
1. CBN Q2-2026 portfolio A/L release or revision identifier and effective timestamp;
2. IMF Q2-2026 observation's corresponding first-release / last-update / receipt-vintage metadata;
3. a direct, reproducible bridge showing both A/L entries correspond to the same statistical vintage.
If no such public metadata exists, retain VINTAGE_PENDING; do not infer from `ACTION`, retrieval time, publication month, matching values or provisional labels.

## 8. Invariants and acceptance
₹0; official/free sources only; no paid APIs, external contact, fabricated timestamps, inferred revisions, synthetic values, net-to-leg back-solving, IIP-stock-as-flow, IMF re-query or cohort rebuild. Fixed 63-country cohort unchanged. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged. UNKNOWN is neither PASS nor FAIL. No production integration or aggregate release.

Status: **TASK COMPLETE — METADATA SEMANTICS AUDIT PASS; VINTAGE GATE STILL BLOCKED/PENDING.**
