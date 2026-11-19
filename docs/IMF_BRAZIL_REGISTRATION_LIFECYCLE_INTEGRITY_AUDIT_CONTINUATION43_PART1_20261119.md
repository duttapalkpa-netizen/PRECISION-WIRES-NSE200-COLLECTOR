# Brazil IMF Registration Lifecycle — Immutable 40-Event Integrity Audit
Date: 2026-11-19 (Asia/Kolkata)
Continuation: Research verification 43, Part-1
Decision: **40/40 returned registration events independently re-parsed from the immutable archived artifact and semantically reconciled to one Brazil registration, PA and BCB URL.** This closes the returned-snapshot lifecycle integrity gate; it does not prove events outside the returned snapshot or resolve PA/Dataflow identity.

## Progress Log
### Reused evidence — no repeated source retrieval
- Reused Run 44465947951 / artifact 14502380926. No IMF endpoint or BCB XML was re-fetched.
- Downloaded the original artifact ZIP and independently recomputed its SHA-256: `2a3266a0c2d3e1948955e9de789c2a3f9acb5ecd12ffca42cd54bbad0bb37f41` (matches the prior GitHub artifact digest).
- Reused exact Registration URN `IMF:D429E36CD161E2F2A34ECAF137994E89(1.0)`.

## Audit method
- Read the archived `registration_history.json` and `event_index.json`; required 40 history rows and 40 indexed events.
- Required 40 unique transaction IDs and chronological order by source epoch milliseconds.
- Independently opened each of the 40 transaction XML files from the ZIP; parsed XML; verified exactly one Registration element and one ProvisionAgreement reference per event.
- Verified every XML carries the same registration ID, PA reference `IMF:BR_BOP_BP6(1.0)`, and exact registered BCB Data URL.
- Verified registry-history Action and embedded SDMX RegistrationRequest action as separate fields; never conflated them.
- Compared each event timestamp with Registration@lastUpdated. The transaction timestamp is 0.460–15.037 seconds later for the 40 events.

## Results
| Check | Result |
|---|---:|
| Original artifact ZIP SHA-256 | PASS |
| History rows / event index rows | 40 / 40 |
| Unique transaction IDs | 40 / 40 |
| XML files parsed and semantically verified | 40 / 40 |
| One exact Registration ID | 40 / 40 |
| One exact ProvisionAgreement `IMF:BR_BOP_BP6(1.0)` | 40 / 40 |
| Exact BCB registered URL | 40 / 40 |
| Registry Action | Replace 40 / 40 |
| Embedded RegistrationRequest action | Information 40 / 40 |
| Chronological event order | PASS |
| Event timestamp minus lastUpdated | +0.460 to +15.037 seconds |

- First returned event: transaction 667, 2023-09-22 09:42:16.389 UTC.
- Last returned event: transaction 37877, 2026-10-26 11:47:33.098 UTC.
- 40 events span 1,130.087 days.
- The event-index `registry_history_type` field is populated only for the first row (Registration); 39 rows omit it. However, all 40 transaction item XMLs independently contain a Registration element under SubmitRegistrationsRequest. Treat the missing event-index Type field as an index-schema omission, not evidence of a different object type.
- All 40 embedded RegistrationRequest actions are Information while all 40 registry history actions are Replace. These are different layers and must remain separately represented.

## Reproducibility
- Added offline verifier: `scripts/research/audit_imf_brazil_registration_history_artifact.py`.
- It requires the exact known source ZIP digest and fails closed on mismatched artifact, count, chronology, registration ID, PA, URL, action or timestamp alignment.
- Independent local execution against the downloaded original ZIP: PASS, 40/40. Output fields and checks are reproducible from the archived ZIP without network calls.
- Original source run: `44465947951`; artifact `14502380926`; original ZIP SHA above.
- Detailed report commit: recorded in Git history.

## Acceptance and remaining boundary
| Gate | Status |
|---|---|
| Exact returned registration-history snapshot integrity | PASS |
| 40/40 transaction XML semantic reconciliation | PASS |
| Current BR1 registration identity (PA + BCB URL) | PASS |
| Events outside the 40-row returned snapshot | UNKNOWN |
| PA structure transaction 2 detailed Changelog | BLOCKED (prior public detail calls HTTP 500; no retry) |
| Registered PA Dataflow `BOP6` vs BCB payload `BOP_BPM6` | CONFIRMED MISMATCH / UNRESOLVED |
| Brazil Reconstruction 100% | NO — BLOCKED |

The 40 registration events establish that the same registration ID, PA `IMF:BR_BOP_BP6(1.0)`, and BCB URL were repeatedly replaced over the returned period. They do not show that the XML payload's declared `IMF:BOP_BPM6(1.0)` is equivalent to the PA's referenced `IMF:BOP6(1.0)`. Shared DSD or a common registration URL is not an authoritative alias/crosswalk.

## Next highest-value dependency
Obtain the actual official Provision Agreement revision/Changelog or owner-side registration export that links the PA to the Dataflow and records any historical change. If the public GUI/export requires an authorized session, the repository owner must provide the export. No credentials, undocumented endpoint, inferred alias or guessed transaction chronology.

## GCR / production guard
- Brazil BCB internal asset/liability identities remain 762/762 PASS; IMF scale/sign benchmark remains 94/94 PASS. Those are separate checks and not PA identity resolution.
- GCR country vintage/coverage/BPM gates remain blocked: Chile 2026-Q1/Q2 vintage review, 40 EMDE countries with no observations, 83 empty country-entry cells, 13 interior-gap series.
- No EMDE aggregate or relative-attraction score. ₹0; no synthetic values; UNKNOWN is not PASS. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 and Engines A-E unchanged.
