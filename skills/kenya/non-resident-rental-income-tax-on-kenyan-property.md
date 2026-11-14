---
name: non-resident-rental-income-tax-on-kenyan-property
description: "Non-resident rental income tax on Kenyan property: a guide for foreign landlords"
jurisdiction: KE
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: corporate-tax
version: 0.1
type: situation-rules
category: international
---

# Non-resident rental income tax on Kenyan property (2026)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Non-resident income from use or occupation of property situated in Kenya is subject to final rental income tax under [ITA s6B](https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf), effective from 1 July 2026 under [Finance Act 2026 ss1(c),4](https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf). For immovable property, the Third Schedule Head B para3(c)(i) specifies 30% of the gross amount. Confirm residence, the property and collection route before computing.

## Who this applies to

A non-resident person, individual or company, receiving income from Kenyan immovable property. Resident landlords use a different regime. Company/trust ownership, uncertain residence and treaty claims require professional review. This file does not settle commercial-letting VAT or a foreign tax credit.

## Rates, bands and thresholds

| Item | Amount and complete condition | Official source |
|---|---|---|
| Immovable-property rent | 30% of gross amount payable to non-resident, Head B para3(c)(i), in words on the page | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Nature | Final tax on the s6B income; do not include it again as taxable income | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Direct collection return/payment | By 20th day of following month for which rent is paid, s6B(2)(b), in words on the page | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Resident collection agent | s6B(2) does not apply when rent received by resident for non-resident is subject to s35(1)(c) withholding | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Withholding remittance and certificate | Within 5 working days after deduction, s35(5), in words on the page | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| Commencement | 1 July 2026, FA2026 s1(c) | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf |

## The base

Use gross rent, reconcile each property and month, and do not deduct repairs, commissions or other expenses from the gross statutory base. Establish whether the landlord receives it directly or a resident receives it on their behalf and is subject to s35(1)(c). Do not freely elect between the routes or leave a gap where neither accounts. Keep leases, rent statements, bank records, agent agreements, PIN/registration evidence and withholding certificates. No rent in a month is a filing-status question, not permission to assume deregistration.

## Deadlines and filing

For direct collection, s6B(2) requires registration/accounting through the simplified framework prescribed by the Commissioner, followed by monthly return and payment by the deadline above. Obtain KRA's current registration and return instructions; this source does not give the live form name, boxes or payment screen, so do not invent them. For resident-agent collection within s35(1)(c), the agent deducts, remits and supplies the certificate under s35(5); match that certificate to gross rent. Keep the final-tax income separate from other return income to avoid double taxation.

## Penalties and interest

[TPA ss38,83,83A](https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf) govern late compliance. Identify the actual return type and taxpayer before using a late-return minimum; this file does not claim the individual annual-return minimum governs a new monthly simplified return. Late tax ordinarily attracts a 5% late-payment penalty and 1% simple interest per month or part under ss83A and38, in words on the page. Refer an assessment or late registration promptly. Under s38(8), aggregate accrued late interest cannot exceed the principal tax liability. Section38(6) stops accrual between notification and payment where the outstanding tax, including interest to notification, is paid in full within the notice’s specified time. Section38(2) refunds interest to the extent the underlying principal is found not payable. Under s38(8), aggregate accrued late interest cannot exceed the principal tax liability. Section38(6) stops accrual between notification and payment where the outstanding tax, including interest to notification, is paid in full within the notice’s specified time. Section38(2) refunds interest to the extent the underlying principal is found not payable.

## Cross-border points

The property remains situated in Kenya even if rent is paid abroad. Obtain the landlord's residence-country details and applicable treaty text before granting any treaty treatment. A treaty's property article, beneficial ownership, relief procedure and residence-country credit must be assessed separately. Commercial property may trigger VAT and other obligations as well.

## Two worked examples that recompute

Direct collection: hypothetical monthly gross Kenyan property rent KES 100,000 gives final tax KES 30,000 and KES 70,000 after tax, before expenses. File and pay under s6B(2).

```oa-check
name: Direct non-resident immovable rent
inputs:
  gross: 100000
steps:
  - tax: gross * 0.30
  - after_tax: gross - tax
expected:
  tax: 30000
  after_tax: 70000
```

Resident-agent decision: on hypothetical gross rent KES 200,000 and an assumed separately charged KES 10,000 management fee, withholding remains KES 60,000 on gross rent, not KES 57,000 on rent net of fees. The landlord receives KES 130,000 after both deductions. Use the agent route only when s35(1)(c) applies and retain its certificate.

```oa-check
name: Agent withholding is on gross rent
inputs:
  gross: 200000
  fee: 10000
steps:
  - withholding: gross * 0.30
  - incorrect_net_basis: (gross - fee) * 0.30
  - landlord_cash: gross - withholding - fee
expected:
  withholding: 60000
  incorrect_net_basis: 57000
  landlord_cash: 130000
```

## Ask the client first

- Residence status for the period, ownership entity and residence country/treaty.
- Kenyan PIN, simplified registration and prior filing history.
- Lease, property location, residential/commercial use and gross monthly rent, including vacant periods.
- Direct collection or resident agent; agreement, deductions and certificates.
- Other taxes, missed deadlines, assessments or outstanding payments.

## Sources

| Source and passages actually read | Official URL | Read on |
|---|---|---|
| Read for ITA ss6B,35(1)(c),35(5), Third Schedule Head B para3(c)(i)-(ii), rate, finality and two collection routes | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf | 2026-11-14 |
| Read for Finance Act 2026 ss1,4, new regime and effective date | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf | 2026-11-14 |
| Read for TPA ss38,83,83A, late compliance framework | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf | 2026-11-14 |

Not yet confirmed: Exact simplified-registration portal route, form/box names, nil-month procedure and the late-return classification for s6B. No treaty rate or relief is established here. The old file left both rental rates open; the immovable-property rate is now sourced.

## Need help

FFP Consult registers and files non-resident rental income tax on behalf of foreign landlords. Reach us at ffp.co.ke.

> Contributed by Julian Njoroge Maina, 25241.
