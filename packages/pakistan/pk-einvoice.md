---
name: pk-einvoice
description: Use for pakistan electronic invoicing and integration. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
version: 1.2
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-22
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: e-invoicing
type: filing-howto
---

# Pakistan electronic invoicing and integration v1.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

For Pakistan federal sales-tax registered businesses and their invoicing controls in 2026. Federal digital invoicing/POS and provincial services systems are separate. Keep PKR invoice values and any evidenced currency conversion explicit. A Punjab services business tests PRA rules separately; federal registration for a goods business creates its own FBR analysis. An unregistered solo freelancer does not become an integrated federal sales-tax taxpayer merely by issuing a business invoice. Registration liability still needs its own check. [STA s.23](https://download1.fbr.gov.pk/Docs/20267171373418951SalesTaxAct1990updatedupto30.06.2026.pdf).

## Ask the client first

Obtain NTN/STRN and provincial registrations, entity and goods/services categories, outlets/POS list, applicable notification and integration date, integrator approval/testing evidence, invoices and FBR acknowledgements, error/cancellation logs and the actual period. Keep export banking evidence under `pk-bookkeeping`; a digital invoice alone does not prove the export-income concession.

## The method, step by step

1. Establish whether the taxpayer falls in the notified federal integration class, including Tier-1 retailer POS obligations. SRO 1852(I)/2025 superseded SRO 1413(I)/2025 and sets the original registration, testing and issue dates by category. Check the taxpayer's category and any applicable later order. The original dates do not provide current grace periods. [SRO 1852(I)/2025](https://download1.fbr.gov.pk/SROs/2025924149054920SRO1852.pdf).
2. Identify the relevant licensed integrator/PRAL arrangement. Under STGO 01/2026 a registered person may engage more than 1 approved/notified licensed integrator where required; do not assume only 1 is permitted. Register outlets and electronic invoice/POS systems through the Board's system and retain integration/test evidence. The count 1 is in words on the page. [Rules 150 Q-150 R](https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf); [STGO](https://download1.fbr.gov.pk/Docs/2026331133557466STGO01of2026.pdf).
3. Capture supplier and recipient identities/registration, date/period, goods description, quantity, exclusive value, rate, tax and inclusive value, with applicable withholding/extra/further tax/FED, discount, invoice reference, HS code, unit and SRO particulars. Preserve the unique FBR number and verifiable QR code. Rule 150 R(13) gives the particulars and its retailer proviso. Section 23(1)(b) requires the NIC or NTN for a manufacturer or importer's supplies to an unregistered distributor. The Finance Act 2026 replaced the earlier card or digital-payment exception from 1 July 2026. Check any notified invoice conditions that apply to the taxpayer. [STA s.23](https://download1.fbr.gov.pk/Docs/20267171373418951SalesTaxAct1990updatedupto30.06.2026.pdf); [rule 150 R(13)](https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf).
4. Transmit through the integrated system, retain acknowledgement, preserve the reported data and reconcile issued invoices to return data. Rules 150 R/150 S require real-time verifiable invoices, electronic debit/credit notes and retained records. The software populates Annexure-C under rule 150 R(5); verify completeness instead of assuming every local invoice reached FBR. [Rules 150 R-150 S](https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf).
5. For a bona fide mistake, the March 2026 order permits cancellation/deletion/editing of a valid electronic sales-tax invoice through the Board system within 72 hours. After that obtain prior Commissioner Inland Revenue approval; do not erase a local record to hide an invoice. Preserve the audit trail. The 72-hour window is printed in words and numerals on the page. [STGO 01/2026, operative paragraphs](https://download1.fbr.gov.pk/Docs/2026331133557466STGO01of2026.pdf).


### Invoices for advance payments

For a registered person within section 23, apply rule 160 to each advance receipt, including an instalment. Issue and link advance invoices as required and include the output tax in the receipt period. Reference the advances on the final invoice and calculate tax on the remaining value. Use the rate applicable at each advance receipt and the supply-date rate for the balance. [SRO 2063(I)/2026](https://download1.fbr.gov.pk/SROs/202611512115850979SRO2063dated5-11-2026.pdf).

### Post 72 hour correction in the November 2026 IRIS manual

FBR's 5 November 2026 manual provides an IRIS application to edit or cancel eligible invoices after 72 hours with concerned CIR approval. An invoice cannot be both edited and cancelled. Section 4.4 excludes invoices already linked to Annex C/FED return, approved under another application, previously submitted/rejected, or pending elsewhere. Approval loads updated data into Annex C; rejection restores the original invoice. Retain application/evidence/status and reconcile the actual return; do not bypass these gates or promise approval. [Manual sections 4.1-4.4](https://download1.fbr.gov.pk/Docs/20261151611157507SalesTaxManual.pdf), read 2026-11-14.

## Boundary and exception table

| Situation | Rule and conditions | Official source |
|---|---|---|
| Electronic invoices and debit/credit notes | Keep for 6 years on electronic media under s.24 (in words on the page); proceedings/other retention duties need their own check | [Rule 150 S(1)-(2)](https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf) |
| Invoice correction for bona fide mistake | 72-hour window from generation; later correction requires prior Commissioner approval (window in words and numerals on the page) | [STGO 01/2026](https://download1.fbr.gov.pk/Docs/2026331133557466STGO01of2026.pdf) |
| Existing integrated POS | Rule 150 Q proviso treats the already integrated system as integrated under the chapter; confirm actual status | [Rule 150 Q](https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf) |
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
| Read for FBRNovember 2026 manual sections 4.1-4.4 post 72 hour amendment/cancellation route, exclusions and approval/rejection effects on 2026-11-14 | https://download1.fbr.gov.pk/Docs/20261151611157507SalesTaxManual.pdf. | 2026-11-14 |
| Read for Sales Tax Act s.23 invoice particulars, replacement provisos, registered issuer and integration powers | https://download1.fbr.gov.pk/Docs/20267171373418951SalesTaxAct1990updatedupto30.06.2026.pdf | 2026-11-24 |
| Read for the superseding integration scope and the original category dates | https://download1.fbr.gov.pk/SROs/2025924149054920SRO1852.pdf | 2026-11-24 |
| Read for rule 160 advance receipt invoices, linking, tax periods and rate timing | https://download1.fbr.gov.pk/SROs/202611512115850979SRO2063dated5-11-2026.pdf | 2026-11-24 |
| Read for SRO 69(I)/2025 substituted chapter XIV, rules 150 Q,150 R and 150 S, including invoice data/retention and existing-POS proviso | https://download1.fbr.gov.pk/SROs/2025129141598258SRO69(I)2025.pdf | 2026-11-14 |
| Read for STGO 01/2026 dated 30 March 2026: SRO 1413 scope recital, multiple licensed integrators, 72-hour correction and prior-approval proviso | https://download1.fbr.gov.pk/Docs/2026331133557466STGO01of2026.pdf | 2026-11-14 |

Not yet confirmed: later class- or taxpayer-specific integration extensions and orders, current technical API/schema/portal screens, taxpayer-specific integration status and each province's separate digital-invoice rules. Earlier SRO 709 dates are not presented as current filing relief. No penalty amount is asserted without its own source check.
