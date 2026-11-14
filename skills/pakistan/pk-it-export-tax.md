---
name: pk-it-export-tax
description: Use for pakistan it and freelance export tax. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
version: 1.1
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
category: international
depends_on:
  - income-tax-workflow-base
tier: 2
domain: income-tax
type: computation
---

# Pakistan IT and freelance export tax v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Pakistan tax year 2026 means 1 July 2025 to 30 June 2026, under ITO s.74. This skill computes withholding on qualifying exported computer software, IT and IT-enabled services, and separates domestic business receipts. A foreign platform or client alone does not establish the concession. Load `pk-income-tax` for ordinary income and `pk-sales-tax-services` for any services-tax obligation.

Quick answer: PSEB-registered qualifying proceeds attract 0.25%; another qualifying s.154A case attracts 1%. Final taxation requires the statutory compliance conditions below. This is a gross-proceeds charge, not a tax on net profit. [ITO s.154A and First Schedule Part III Division IVA](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Rates, bands and thresholds

| Receipt and conditions for tax year 2026 | Rate and base | Official source |
|---|---|---|
| Export proceeds of computer software, IT or IT-enabled services by persons registered with PSEB; the published table covers tax years 2024 through 2026 | 0.25% of proceeds | [First Schedule Part III Division IVA, row 1](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Any other case within s.154A, including qualifying exported services; lack of PSEB does not itself prove that ordinary slabs apply | 1% of proceeds | [Division IVA, row 2; s.154A(1)(b)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |
| Normal tax year, unless an authorised special year applies | 12 months ending 30 June; tax year 2026 starts 1 July 2025 (derived calendar dates) | [s.74](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf) |

## The base

1. Obtain the service contract, invoices, platform gross settlements, refunds/fees, bank realisation advices/e-PRCs and PSEB certificate with its applicable period. Keep PKR and foreign-currency accounts separately reconciled.
2. Identify the actual statutory service category. Design, BPO and remote work are descriptions requiring classification, not automatic proof of IT/ITeS. Match each foreign-exchange receipt realised by an authorised dealer to the export and the bank's withholding. Apply the rate to gross proceeds within s.154A, not an assumed exchange rate or net business profit.
3. Test finality under s.154A(2): annual return filed; withholding statements filed if required; required federal/provincial sales-tax returns filed, except that this last condition does not apply to the PSEB IT exporter in s.154A(1)(a); no foreign-tax credit allowed. The exception is to the final-tax condition, not an exemption from services tax itself.
4. Check the annual option out under s.154A(3). If conditions fail or the person opts out, final treatment does not apply; refer the ordinary assessment and credit mechanics to `pk-income-tax`. Do not simply call every bank deduction final or minimum tax.
5. Keep domestic-client income outside the export concession, with its attributable expenses and withholding separately recorded. Missing banking evidence means pause the affected concession; missing PSEB means test the other statutory case rather than automatically include all receipts in progressive slabs. These steps implement [s.154A(1)-(3)](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Deadlines and filing

Report qualifying proceeds and bank deduction in the applicable IRIS final/fixed-tax schedule, and ordinary domestic business income in its own schedule. Reconcile the resident individual's wealth statement. The ordinary individual/AOP return date is 30 September after year end under s.118; tax year 2026 therefore has an ordinary date of 30 September 2026 (derived), subject to any valid extension. Confirm the applicable extension before describing a return as late. Generate a PSID for an amount due and retain the CPR after payment; a CPR is evidence of payment, not the payment instruction. [ITO ss.114,116,118,137,154 A](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Penalties and interest

A missing return may defeat finality as well as trigger return penalties. Missing required withholding statements need separate correction. Do not invent a penalty or treat payment of withholding as completion of filing. Refer notices, late filing, interest or disputes for the applicable ss.182/205 assessment. [ITO ss.154A,182,205](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Cross-border points

Use the actual authorised-dealer realisation and supporting remittance evidence. Do not advise cash, informal transfer or crypto receipt as a way around banking rules. Foreign tax cannot also be credited against the s.154A final stream. A foreign client, foreign platform and foreign-source income are different questions. No blanket exemption from provincial services tax is created here. [ITO s.154A](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Two worked examples that recompute

Both cases assume documented qualifying proceeds, full statutory compliance and no option out. Inputs are illustrative PKR proceeds, not a current USD exchange rate.

The earlier USD 30,000 / PKR 8,400,000 illustration is retained as an assumed conversion only. On the PKR amount the PSEB result is 21,000 and the other qualifying-case result is 84,000; the difference is 63,000 (all derived).

```oa-check
name: PSEB qualifying export proceeds
inputs:
  proceeds: 8400000
steps:
  - withheld: proceeds * 0.0025
  - net_bank: proceeds - withheld
expected:
  withheld: 21000
  net_bank: 8379000
```

```oa-check
name: Same proceeds in another qualifying export-service case
inputs:
  proceeds: 8400000
steps:
  - withheld: proceeds * 0.01
  - net_bank: proceeds - withheld
  - rate_difference: withheld - proceeds * 0.0025
expected:
  withheld: 84000
  net_bank: 8316000
  rate_difference: 63000
```

## Ask the client first

Obtain residence, legal form, actual tax period, service classification, contracts and foreign-client evidence, gross proceeds and fees by receipt, domestic receipts, bank/e-PRC support, PSEB registration/certification dates, actual tax deductions, required returns/statements, any foreign tax and the annual option. Recommend checking PSEB eligibility for genuine IT/ITeS exports; never backdate or assume registration. Refuse a final tax result where eligibility or finality evidence is missing.

For the actual tax-year-2026 filing cycle, FBR Circular 04 of 2026-27 dated 15 October 2026 extends the filing date to **31 October 2026** for persons originally due 30 September 2026 and previously extended to 15 October. It does not extend every company return. Apply any individual further order only on its evidence; this circular does not itself state a general payment extension. [Official circular](https://download1.fbr.gov.pk/Docs/20261015221039470Extension.pdf), read and scanned page inspected 2026-11-14.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for Circular 04 of 2026-27, 15 October 2026, the 31 October extension for the original 30 September cohort; scanned signed page inspected | https://download1.fbr.gov.pk/Docs/20261015221039470Extension.pdf | 2026-11-14 |
| Read for ITO ss.74,114,116,118,137,154 A(1)-(3),182,205; Division IVA rows 1-2 and neighboring provisions; tax year 2026 law | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |
| Read for June 2026 consolidation s.154A and Division IVA footnote extending the period through tax year 2029; distinguish later amendments from this tax year | https://download1.fbr.gov.pk/Docs/2026724177725705IncomeTaxOrdinanace2001.pdf | 2026-11-14 |

Not yet confirmed: the taxpayer's PSEB period, classification, gross proceeds, actual remittances/withholding and compliance; any later case-specific extension and current IRIS box identifiers; treatment of a failed-condition or opted-out case beyond this withholding computation. No USD/PKR exchange rate is asserted by the examples. Future tax years need their own effective-law check.
