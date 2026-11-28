# GCR Continuation 304 — CCIL FX-Clear official FAQ cancellation / trade identity boundary
Date: 28-Nov-2026 (Asia/Kolkata)
Repository: duttapalkpa-netizen/PRECISION-WIRES-NSE200-COLLECTOR
Scope: bounded official-document follow-up to C303; no new CSV acquisition or row transformation.

## Preflight and duplicate prevention
- Re-read the current Master Continuity Ledger, GCR Master Priority Queue, Historical Task Registry, immutable 63-country Q2-2026 matrix, Library Mother File (Continuations 1–53) and C303 report.
- C303's raw-byte SHA-256 checks, row counts, duplicate arithmetic, invalid-price counts, 182-day window arithmetic and existing CCIL product-page review were reused. No repeated CSV materialization, hash calculation, row scan, deduplication, OHLC build, IMF query, cohort rebuild or country-matrix edit was performed.
- Selected the only new, directly relevant official evidence gap: whether CCIL's own USD/INR settlement FAQ clarifies amendment/cancellation and transaction identity mechanics. This is a source-semantics audit, not a CSV schema certification.

## New first-party evidence
Official CCIL USD/INR Settlement FAQ:
https://dr.ccilindia.com/web/ccil/faqmoduleforex-settlement
- FAQ Annexure IFN 300 format identifies Field 20 as Transaction Reference Number and Field 21 as Related Reference; fresh transactions use NEWT, amendments AMND, cancellations CANC. For AMND/CANC, Field 20 carries the original transaction reference. (FAQ lines 224–267.)
- CCIL business validations include duplicate-message rejection, original-deal existence for amendment/cancellation, and rejection of amendments to already accepted trades. (Lines 275–300.)
- CCIL states accepted/matched Spot trade cancellation before the Spot cut-off requires both counterparties' cancellation; unmatched NEWT/AMND/CANC deals can be unilaterally cancelled by reporting CANC. (Lines 343–346.)
- FX-Clear / FX-Retail platform trades flow directly to CCIL; banks need not separately report them. (Lines 336–341.)
- The FAQ describes member settlement/reporting workflows and IFN300 messages. It does not document the public Individual Trade Details CSV's export population, cancellation-row representation, status field, stable trade identifier, or exact Quantity unit/scale and Trade Price definition.

## Reconciliation against C303
| Question | C304 result | Acceptance |
|---|---|---|
| Are NEWT / AMND / CANC and original transaction reference mechanics documented? | Yes, in IFN300 settlement/reporting FAQ | Methodology evidence PASS, limited to IFN300 |
| Is there an official cancellation workflow for accepted/matched vs unmatched trades? | Yes: bilateral cancellation for accepted/matched Spot before cut-off; unmatched can be cancelled unilaterally with CANC | Methodology evidence PASS, limited to FAQ scope |
| Does this establish how cancelled trades appear in the public Individual Trade Details CSV? | No | NOT_ESTABLISHED |
| Does it supply a stable trade ID in the public CSV? | No; IFN300 has a transaction reference, but no mapping to CSV fields | NOT_ESTABLISHED |
| Does it define public CSV Quantity unit/scale? | No | NOT_ESTABLISHED |
| Does it define ordinary SPOT CSV Trade Price precision, side, or status? | No | NOT_ESTABLISHED |
| Can identical four-field CSV tuples be deduplicated safely? | No | BLOCKED |
| Can the five files be converted to OHLC / admitted to GCR? | No | NOT_ADMITTED |

## Important version/scope caution
- CCIL FX-Clear page lists SPOT, C-SPOT and R-SPOT separately and describes Individual Trade Details CSV with a maximum 182-day date range. This product-page statement does not provide a field dictionary.
- The surfaced 21-Jun-2019 FX-Clear regulations document explicitly says it was superseded by Notification CDS/FX-CLEAR/20/06 dated 21-Aug-2020. Its historical Spot / Customer Spot distinction is not treated as current CSV schema evidence.
- The 07-Oct-2022 Reference Rate Spot notification concerns R-Spot matched spread / final price mechanics only; it is not generalized to ordinary SPOT.
- CCIL FAQ content is sufficient to show that cancellation lifecycle exists and that an original transaction reference is used in IFN300; it is not sufficient to map cancellation or trade identity into the public CSV.

## Decision
- C303's raw-file integrity result remains unchanged; no data row has been admitted.
- Cancellation workflow understanding: PARTIAL / FAQ-SCOPE PASS.
- Public CSV cancellation inclusion, trade identity, Quantity units, ordinary SPOT Trade Price semantics: NOT_ESTABLISHED.
- Exact-tuple duplicate removal: BLOCKED; preserve all raw rows.
- Non-positive price treatment: BLOCKED; quarantine, do not silently remove or repair.
- Official trading-session coverage: NOT_ESTABLISHED.
- Daily OHLC and GCR ingestion: NOT_ADMITTED.
- No matrix row changed because this is a cross-cutting FX source intake audit, not a national-source cohort gate.

## Exact next action
Require a current CCIL/Clearcorp public export field dictionary, Individual Trade Details report specification, or official export metadata that explicitly maps:
1. instrument/product (SPOT vs C-SPOT vs R-SPOT);
2. Quantity unit and scale;
3. Trade Price meaning, precision, quote convention and status;
4. stable trade reference / identifier;
5. whether NEWT/AMND/CANC, matched/accepted, rejected and cancelled trades are included and how represented;
6. duplicate/export overlap policy and file-generation timestamp.
Until that evidence is available, retain original CSVs unchanged and keep all transformations/admission blocked. Do not contact CCIL or bypass access restrictions without user approval.

## Invariants
₹0 spend; free official sources only; UNKNOWN is neither PASS nor FAIL; no synthetic data, guessed units, inferred trade IDs, silent deduplication, price repair, unsupported OHLC, paid access, external contact, workflow dispatch, production integration, selector/ranking/threshold changes or merge. CORE-672 (56×12), Engines A–E, Production Selector, RANKING_SCORE, +1 PRESSURE_FADE and IPO-PLX V2.0 unchanged.

## Sources
- CCIL USD/INR Settlement FAQ: https://dr.ccilindia.com/web/ccil/faqmoduleforex-settlement (IFN300 fields and NEWT/AMND/CANC; duplicate and cancellation validation; cancellation workflow).
- CCIL FX-Clear product page: https://www.ccilindia.com/en/fx-clear (SPOT/C-SPOT/R-SPOT distinction and 182-day Individual Trade Details CSV cap).
- CCIL superseded 2019 FX-Clear notification: https://www.ccilindia.com/documents/d/ccil/cdsfxclear190421jun19-pdf (used only for superseded-version warning).
- CCIL R-Spot reference-rate notification, 07-Oct-2022: https://www.ccilindia.com/documents/d/ccil/notificationtomembersfbilreferencerateonfxclear07oct2022-pdf (R-Spot-specific; not generalized).
