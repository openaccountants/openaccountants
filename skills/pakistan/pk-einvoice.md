---
name: pk-einvoice
description: >
  Use this skill whenever asked about electronic/digital invoicing and POS integration in Pakistan.
  Trigger on phrases like "Pakistan e-invoicing", "FBR digital invoicing", "FBR POS integration",
  "electronic invoice sales tax Pakistan", "FBR SRO e-invoice". Covers the FBR's electronic invoicing
  requirements for sales-tax-registered persons, POS/real-time integration for retailers, and invoice
  requirements. ALWAYS read before any Pakistan e-invoicing work.
version: 1.1
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: e-invoicing
type: filing-howto
---

# Pakistan electronic invoicing and integration v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For Pakistan federal sales-tax registered businesses and their invoicing controls in 2026. Federal digital invoicing/POS and provincial services systems are separate. A Punjab services business tests PRA rules separately; federal registration for a goods business creates its own FBR analysis. An unregistered solo freelancer does not become an integrated federal sales-tax taxpayer merely by issuing a business invoice. Registration liability still needs its own check. [STA s.23](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf).

## Ask the client first

Obtain NTN/STRN and provincial registrations, entity and goods/services categories, outlets/POS list, applicable notification and integration date, integrator approval/testing evidence, invoices and FBR acknowledgements, error/cancellation logs and the actual period. Keep export banking evidence under `pk-bookkeeping`; a digital invoice alone does not prove the export-income concession.

## The method, step by step

1. Establish whether the taxpayer falls in the notified federal integration class, including Tier-1 retailer POS obligations. Do not treat the original implementation dates as current grace periods. FBR's March 2026 order describes all sales-tax registered persons as subject to integration and digital invoicing under SRO 1413(I)/2025. The detailed category/calendar still requires the operative notification. [STGO 01/2026](https://download1.fbr.gov.pk/Docs/2026331133557466STGO01of2026.pdf).
2. Identify the relevant licensed integrator/PRAL arrangement. Under STGO 01/2026 a registered person may engage more than 1 approved/notified licensed integrator where required; do not assume only 1 is permitted. Register outlets and electronic invoice/POS systems through the Board's system and retain integration/test evidence. [Rules 150Q-150R](https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf); [STGO](https://download1.fbr.gov.pk/Docs/2026331133557466STGO01of2026.pdf).
3. Capture supplier and recipient identities/registration, date/period, goods description, quantity, exclusive value, rate, tax and inclusive value, with applicable withholding/extra/further tax/FED, discount, invoice reference, HS code, unit and SRO particulars. Preserve the unique FBR number and verifiable QR code. Rule 150R(13) has particulars and a retailer proviso; s.23 has recipient/NIC exceptions, so do not impose the older blanket CNIC-on-every-unregistered-invoice claim. [STA s.23](https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf); [rule 150R(13)](https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf).
4. Transmit through the integrated system, retain acknowledgement, preserve the reported data and reconcile issued invoices to return data. Rules 150R/150S require real-time verifiable invoices, electronic debit/credit notes and retained records. The software populates Annexure-C under rule 150R(5); verify completeness instead of assuming every local invoice reached FBR. [Rules 150R-150S](https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf).
5. For a bona fide mistake, the March 2026 order permits cancellation/deletion/editing of a valid electronic sales-tax invoice through the Board system within 72 hours. After that obtain prior Commissioner Inland Revenue approval; do not erase a local record to hide an invoice. Preserve the audit trail. [STGO 01/2026, operative paragraphs](https://download1.fbr.gov.pk/Docs/2026331133557466STGO01of2026.pdf).

## Boundary and exception table

| Situation | Rule and conditions | Official source |
|---|---|---|
| Electronic invoices and debit/credit notes | Keep for 6 years on electronic media under s.24 (in words on the page); proceedings/other retention duties need their own check | [Rule 150S(1)-(2)](https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf) |
| Invoice correction for bona fide mistake | 72-hour window from generation; later correction requires prior Commissioner approval | [STGO 01/2026](https://download1.fbr.gov.pk/Docs/2026331133557466STGO01of2026.pdf) |
| Existing integrated POS | Rule 150Q proviso treats the already integrated system as integrated under the chapter; confirm actual status | [Rule 150Q](https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf) |
| Provincial services tax | PRA/SRB/KPRA/BRA rules and returns are separate; no federal integration exemption from provincial obligations | [FBR legal provisions and provincial authority links](https://www.fbr.gov.pk/di-legal-provisions/173967/173968) |

## Worked cases

Inputs are operational evidence examples, and all results are derived. No statutory tax rate is invented by these cases.

```oa-check
name: Invoice reconciliation detects missing transmission
inputs:
  local_invoices: 120
  acknowledged_invoices: 117
  local_exclusive_total: 1000000
  acknowledged_exclusive_total: 970000
steps:
  - missing_count: local_invoices - acknowledged_invoices
  - unreconciled_value: local_exclusive_total - acknowledged_exclusive_total
expected:
  missing_count: 3
  unreconciled_value: 30000
```

```oa-check
name: Correction timing before and after Commissioner boundary
inputs:
  hours_since_generation: 80
  window_hours: 72
steps:
  - hours_beyond_window: max(0, hours_since_generation - window_hours)
  - hours_remaining: max(0, window_hours - hours_since_generation)
expected:
  hours_beyond_window: 8
  hours_remaining: 0
```

The second case needs prior approval. A correction at 48 hours would have 24 hours remaining (derived), but still needs a bona fide mistake and use of the Board system.

## When to refuse or refer

Never tell an in-scope registered person to skip integration, treat a provincial services return as the federal system, claim a rolling implementation date without the operative SRO, erase a transmitted invoice outside the prescribed correction process, or assume a freelancer's non-registration is lawful without testing liability. Refer disputed notification scope, penalties, failed integration and provincial e-invoicing requirements.

## Filing and payment

Reconcile invoice/return data and supply the transmission/correction evidence to the reviewed sales-tax return workflow in `pk-sales-tax-federal` or `pk-sales-tax-services`. Integration does not itself file or pay the return. Do not describe an invoice acknowledgement as a tax-payment receipt.

## Completion checklist

Registration and authority identified; applicable notification/calendar obtained; integrator approval and testing retained; outlets registered; invoice fields/QR/number present; acknowledgements reconciled; corrections authorised/timed; provincial obligations considered.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Sales Tax Act s.23 invoice particulars, NIC/digital-payment exception, registered issuer and integration powers | https://download1.fbr.gov.pk/Docs/202586148252375SalesTaxActupdatedupto2025-26.pdf | 2026-11-14 |
| Read for SRO 69(I)/2025 substituted chapter XIV, rules 150Q,150R and150S, including invoice data/retention and existing-POS proviso | https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf | 2026-11-14 |
| Read for STGO 01/2026 dated 30 March 2026: SRO 1413 scope recital, multiple licensed integrators, 72-hour correction and prior-approval proviso | https://download1.fbr.gov.pk/Docs/2026331133557466STGO01of2026.pdf | 2026-11-14 |

Not yet confirmed: complete operative category-by-category integration calendar and later extensions/SROs, current technical API/schema/portal screens, taxpayer-specific integration status and each province's separate digital-invoice rules. Earlier SRO 709 dates are not presented as current filing relief. No penalty amount is asserted without its own source check.
