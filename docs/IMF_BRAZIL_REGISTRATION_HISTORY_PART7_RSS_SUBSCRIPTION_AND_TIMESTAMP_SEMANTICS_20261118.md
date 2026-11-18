# গবেষণা যাচাই অব্যাহত 36 — Part-7: IMF RSS subscription route and registration timestamp semantics
Date: 2026-11-18

## Objective
Identify an official, no-cost, owner-actionable way to preserve future Brazil registration events, and clarify whether the current registration Last Updated timestamp proves original registration chronology.

## Primary official source inspected
IMF SDMX Central User Guide, last updated May 2025:
https://dsbb.imf.org/content/pdfs/IMFSDMXCentralUserGuide.pdf
Relevant sections: §6 Registering Data (PDF pp.16–17), §7 Subscribing as a Service (PDF pp.18–19).

## Finding A — Last Updated is not necessarily original registration date
The guide states:
- The Registrations table shows Dataflow, Data Provider, URL and Last Updated.
- When a URL is registered, the Last Updated column reflects the time when the data registration event took place.
- An existing URL can be selected and Re-Register can be performed.
- After confirmation, the Last Updated column reflects the new registration of the same URL.
Therefore, a Last Updated timestamp can be refreshed by a re-registration. It cannot, by itself, be interpreted as the original creation date or full registration chronology. For the Brazil row timestamp 2026-10-26T11:47:29.000Z, the event type (new registration vs re-registration) and earlier history remain UNKNOWN until an actual transaction document/log proves it.

## Finding B — Official prospective monitoring is possible without an IMF account
The same guide documents three update-notification mechanisms:
1. RSS feed: https://sdmxcentral.imf.org/rss.xml
2. Email notification
3. HTTP POST notification

The guide states:
- RSS is updated each time a transaction occurs.
- Transactions include structure additions/modifications/deletions and data registrations/deletions.
- Each RSS item links to an underlying SDMX 2.1 RegistryInterface document containing SubmitStructureRequest or SubmitRegistrationRequest.
- Users can create subscriptions from the “Subscribe to Changes” footer link.
- No IMF SDMX Central account is required to receive subscription notifications; a valid email address and selected event types are required.
- The UI lists event types “All Data Events” and “All Structure Events”, and offers “Refine Events”.
- Email notifications include a ZIP attachment containing the SDMX document for the change.
- HTTP POST notifications deliver the SDMX 2.1 RegistryInterface document to a user-defined URL.
This is a prospective alert route, not a way to reconstruct past events. The guide does not establish whether the UI can narrow “All Data Events” to exactly provider IMF:BR1 or the Brazil BCB URL; this must be checked in the interactive “Refine Events” UI before claiming provider-specific filtering.

## Operational recommendation (no credentials / no cost)
- Owner may open the official SDMX Central site and use footer -> Subscribe to Changes.
- Select All Data Events, then inspect Refine Events for any supported exact provider/dataflow filter. Do not assume the filter exists.
- Use an email address controlled by the owner; complete confirmation email if prompted.
- Preserve the original ZIP attachment, extracted RegistryInterface XML, email received timestamp, message headers, and SHA-256 in the repository archive. Record whether the event is SubmitRegistrationRequest or SubmitStructureRequest; parse provider, dataflow, URL, action and transaction timestamp from the payload.
- If no provider filter is offered, subscribe to All Data Events and locally filter incoming payloads for exact IMF:BR1, BCB URL and BOP6/BOP_BPM6. Keep all other events out of Brazil evidence.
- Do not send email address or credentials to the assistant. Do not create an external subscription without the owner's explicit action.

## What this does NOT resolve
- Does not identify historical Brazil registration create/replace/delete events.
- Does not prove whether 2026-10-26 was initial registration or re-registration.
- Does not resolve the current IMF:BOP6(1.0) registration vs the BCB XML payload's IMF:BOP_BPM6(1.0) identity mismatch.
- Does not authorize Brazil admission, EM aggregation or market use.
- The prior 33 RSS transaction sample remains bounded; its no-Brazil-match finding is valid only for that sample/window.

## Acceptance matrix
| Item | Status |
|---|---|
| Official guide and §6 registration semantics inspected | PASS |
| Re-Register refreshes Last Updated timestamp | PASS |
| Last Updated treated as original creation date | REJECTED |
| Official RSS event-document mechanism | PASS |
| Email/POST subscription mechanism documented | PASS |
| No IMF account needed for subscription notifications | PASS |
| Exact IMF:BR1 filter availability in Refine Events UI | NOT_DONE |
| Owner subscription activated | NOT_DONE (owner action required) |
| Historical Brazil event XML/CSV | NOT_DONE |
| Brazil registration chronology | UNKNOWN |
| BOP6 vs BOP_BPM6 mismatch | CONFIRMED |
| Brazil admission / EM aggregation / market use | BLOCKED / NOT_AUTHORIZED |

## Exact next actions
1. Owner-side: optionally subscribe to All Data Events via official “Subscribe to Changes”; inspect Refine Events for exact IMF:BR1/BOP6 filtering. No credentials required, but a valid owner-controlled email and confirmation may be required.
2. Owner-side historical retrieval remains separate: select a historical transaction in the official activity GUI and export its SDMX-XML/CSV, if available. Provide only the exported file, not login credentials.
3. On receipt, validate XML schema/well-formedness, classify SubmitRegistrationRequest vs SubmitStructureRequest, extract exact identifiers and event semantics, and archive raw + parsed evidence with SHA-256.

## Guardrails
₹0, official sources only. No fabricated dates, no inference from Last Updated alone, no guessed endpoint/transaction IDs, no synthetic data. No production changes, PR merge, Brazil/EM admission, or macro overlay weights. Production Selector, RANKING_SCORE, +1 PRESSURE_FADE, CORE-672 (56×12), Engines A–E unchanged; UNKNOWN is not PASS.
