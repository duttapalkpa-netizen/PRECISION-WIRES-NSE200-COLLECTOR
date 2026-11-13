# NSE CM-MII Security Master Variant Scope Semantics Audit
Audit date: 2026-11-13 (Asia/Kolkata)
Status: OFFICIAL_SCOPE_SEMANTICS_PASS / RAW_PAYLOAD_VALIDATION_PENDING
Scope: resolve why NSE publishes two CM-MII security-master variants and identify the official BSE-exclusive marker. This audit does not claim either daily payload has been downloaded or parsed.

## Primary official evidence
NSE Member Service Department Circular NSE/MSD/67344, Circular Ref. 13/2025, dated 28-Mar-2025:
https://nsearchives.nseindia.com/content/circulars/MSD67344.pdf

Relevant provisions:
- Page 1, lines 17–36: alternative trading venue applicability is limited to applicable BSE-exclusive securities/contracts; cash-market categories include equity main board, SME, partly paid shares, rights entitlements and T0 securities, if any.
- Page 2, lines 52–75:
  - BSE-exclusive symbols in the NSE security master have a trailing "$".
  - The legacy security master field `PermittedToTrade` (field 6) uses value `2`, description "BSE listed".
  - In `NSE_CM_security_ddmmyyyy.csv.gz`, field 17 is `PrtdToTrad`; the circular identifies the BSE-exclusive value as tradeable only upon invocation of the alternative trading venue mechanism.
  - BSE security names may be truncated to 25 characters; tick size follows BSE details.
- Page 3, lines 84–122: NSE publishes two separate MII security files:
  1. "CM-MII Security File (.gz) - (NSE Listed securities)"
  2. "CM-MII Security File (.gz) - (NSE Listed and BSE Exclusive securities)"
  Members are advised to upload the appropriate master daily before trading hours.
- Page 4, lines 145–157: exclusive NSE trading members should refrain from placing orders in BSE-exclusive securities; EOD bhavcopy etc. may include BSE-exclusive securities after invocation; price/OHLC/OI information is exclusive to activity at NSE.

## 2026 catalogue cross-check
NSE All Reports, opened 13-Nov-2026:
https://www.nseindia.com/all-reports
For 11-Nov-2026 it displays:
- NSE Listed securities variant: `NSE_CM_security_11112026.csv.gz`, 1.22 MB.
- NSE Listed and BSE Exclusive securities variant: same displayed filename, 1.49 MB.
For 12-Nov-2026, the captured report list does not show these two CM-MII entries. No file for 12-Nov is inferred.

## Reconciled interpretation
- The two variants are not arbitrary duplicate downloads. The official 2025 circular explicitly distinguishes an NSE-only master from an NSE + BSE-exclusive master.
- The combined master can contain BSE-exclusive records that are not ordinarily tradeable on NSE; their official marker is `PrtdToTrad` field 17 and their symbols carry a trailing `$` as described in the circular.
- Therefore, presence in the combined master is not evidence of ordinary NSE tradability. For the normal NSE swing-trading universe, the BSE-exclusive marker must be treated as a distinct eligibility state, not as an ordinary PASS.
- Do not infer that every row in the combined master with any other nonstandard value is tradable. Parse the actual schema and validate values against the circular.
- Do not truncate symbols, strip "$", or merge BSE-exclusive rows into NSE-listed rows without preserving original symbol, source scope, field 17 value and source vintage.
- BSE-exclusive security names can be truncated to 25 characters; company-name joins must not rely on exact name alone. Prefer verified identifiers and retain source name verbatim.
- The larger displayed 1.49 MB size is consistent with a broader scope but does not prove exact row inclusion or a strict superset; only raw payload comparison can prove that.

## Research pipeline treatment (recommendation, not production change)
- Maintain separate source scope metadata: `NSE_LISTED` and `NSE_LISTED_PLUS_BSE_EXCLUSIVE`.
- Add a research-side classification state for records explicitly marked BSE-exclusive / `PrtdToTrad=2`: `ALTERNATIVE_VENUE_ONLY` or `NOT_ORDINARILY_NSE_TRADEABLE`.
- Keep these records out of ordinary NSE tradeability PASS calculations unless an official invocation event and date-specific exchange notice establish that the alternative venue was invoked.
- If field 17 is absent, malformed, or unrecognized, mark classification UNKNOWN; do not infer from symbol alone.
- This is a research data classification recommendation only. No production selector, ranking score, CORE-672 diagnostic, or Hard Gate change is authorized or made.

## Acceptance status
- PASS: official circular resolves the purpose and distinction between the two variants.
- PASS: official marker and operational caveats identified (`PrtdToTrad` field 17, value 2, trailing "$", alternative-venue-only condition).
- PASS: current NSE catalogue confirms the two distinct 11-Nov-2026 labels.
- UNKNOWN: raw 11-Nov payloads, exact hrefs, HTTP response metadata, bytes, SHA-256, gzip integrity, parsed schemas and row counts.
- NOT_STARTED: row-level proof that combined file contains the BSE-exclusive subset and comparison with NSE-only file.
- NOT_ESTABLISHED: whether a specific alternative-venue invocation occurred on any date; no inference from the master file.
- No production integration, no PR merge, no spending, no paid API.

## Fail-closed validation steps
1. Download each catalogue entry via its exact href independently.
2. Verify HTTP response, MIME, actual byte count, gzip magic and SHA-256.
3. Decompress and preserve raw headers and row data.
4. Confirm field 17 name/value distribution and symbol suffix behavior against Circular 67344.
5. Compare two variants by stable keys; quantify BSE-exclusive-only rows and any conflicting values.
6. Cross-check same-date official NSE bhavcopy/security deliverable; never equate inclusion in a combined master with normal tradeability.
7. Record all outputs in an immutable manifest before any downstream eligibility use.

## Protected project invariants
Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56 Steps × 12 Filters), Engines A–E, and Hard Gate remain unchanged. ₹0 spend; free official sources only. No PR merge or production integration without explicit user approval.
