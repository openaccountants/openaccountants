---
name: ms-nonresident-withholding
description: "Montserrat withholding tax on payments to nonresidents for 2026 under section 39 and Schedule 1 of the Income and Corporation Tax Act. Covers what payments are in scope, the presumption of nonresidence for payments to an overseas address, the rates (15% dividends, 10% rent of immovable property, 20% rent of movable property, 20% public entertainers, 20% other payments), year-end accruals, payment within 15 days after the month end, certificates and payer liability, and treaty directions. Trigger phrases include Montserrat withholding tax, nonresident tax Montserrat, Schedule 1 withholding."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ms-nonresident-withholding"
  jurisdiction: "MS"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Montserrat withholding on payments to nonresidents

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Deduction of tax from payments to nonresidents in 2026 under section 39 and Schedule 1 of the Income and Corporation Tax Act, Cap. 17.01 (revised to 1 January 2025). Amounts are EC$. Employment emoluments are under section 51 (PAYE) and outside this skill. Company tax and the branch remitted-profit charge: [ms-corporate-income-tax](ms-corporate-income-tax.md).

## Ask the client first

1. Who is the recipient and where is it resident? Is the payment going to an address outside Montserrat?
2. What is the payment: dividend, interest, rent (land or equipment), royalty, management charge, commission or fee, periodic payment, trust distribution, services performed in Montserrat?
3. Does the recipient carry on business in Montserrat through a permanent establishment?
4. Is the amount agreed gross or net of tax? Is it accrued but unpaid at year end?
5. Is there a Comptroller direction for a lower treaty rate?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Dividends | 15% | [Income and Corporation Tax Act Cap. 17.01, Schedule 1 para.3](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf) |
| Rent of immovable property | 10% | same |
| Rent of movable property | 20% | same |
| Fees of public entertainers | 20% | same |
| Other payments in para.1 | 20% | same |
| Due date, s.52 | Within 15 days after the end of the month in which tax was deducted or deductible | same |
| Accruals, para.1(3) | An amount charged as an expense in the basic year but unpaid is treated as paid on the last day of that year | same |
| Treaty direction, s.39(3) | The Comptroller may direct a lower deduction under an agreement made under s.55 | same |

### Steps

1. **Residence:** a payee paid at an address outside Montserrat is presumed nonresident unless the contrary is proved (s.39(2)).
2. **Scope:** Schedule 1 para.1 payments, plus independent personal services performed in Montserrat other than through a permanent establishment; not other payments to a nonresident carrying on business or employment in Montserrat.
3. **Deduct** from the gross payment at the para.3 rate; the payment is not chargeable income of the recipient (para.2), so no expense deductions run against it.
4. **Accrual businesses:** deduct as at the last day of the basic year for unpaid charges.
5. **Pay** within 15 days after the month end; give each recipient a certificate; file the return with copies.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Contract states a net amount | Gross up and check who bears the tax; the gross examples below do not apply | [Cap. 17.01, Schedule 1](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf) |
| Payer fails to deduct | Payer personally liable (para.6) | same |
| Payment to a bank or agent for a nonresident | Still within the Schedule (para.2 proviso (c)) | same |
| Payment by one nonresident to another | Comptroller may charge the recipient directly without relieving the payer (para.2 proviso (b)) | same |
| Exemption orders | Some projects are exempt by SRO (for example SRO 22/2021, SRO 25/2022) | same |

## Worked cases

### Case 1: three gross payments of EC$10,000

Dividend: tax 1,500, paid 8,500. Rent of land: 1,000 and 9,000. Royalty: 2,000 and 8,000.

```oa-check
name: Montserrat withholding on 10,000 dividend, rent and royalty
inputs:
  gross: 10000
steps:
  - dividend_tax: gross * 0.15
  - rent_tax: gross * 0.10
  - royalty_tax: gross * 0.20
  - royalty_net: gross - royalty_tax
expected:
  dividend_tax: 1500
  rent_tax: 1000
  royalty_tax: 2000
  royalty_net: 8000
```

### Case 2 (decision): pay the December fee now or in February?

An accrual-basis company charges a 12,000 management fee from a nonresident at its 31 December year end. Paying in February does not delay the tax: the fee is treated as paid on 31 December, so 2,400 is due by 15 January. If the contract instead promises the supplier 12,000 net, the gross is 15,000 and the tax 3,000.

```oa-check
name: Montserrat year-end accrual and net-of-tax gross-up, 12,000 fee
inputs:
  fee: 12000
  rate: 0.20
steps:
  - tax_on_accrual: fee * rate
  - gross_if_net: fee / (1 - rate)
  - tax_if_net: gross_if_net * rate
expected:
  tax_on_accrual: 2400
  gross_if_net: 15000
  tax_if_net: 3000
```

## When to refuse or refer

- Permanent establishment questions, branch remitted profits, source disputes.
- Treaty entitlement: needs a Comptroller direction.
- Specific exemptions and amendments after 1 January 2025.

## Filing and payment

1. Pay tax deducted within 15 days after the month end (s.52).
2. Give each recipient a certificate of gross payment and tax deducted; keep a calendar-year record by payment type, amount, tax and recipient (para.4).
3. File the return with the remittance and copies of the certificates (para.5).

## Completion checklist

- Residence and scope recorded; rate chosen by payment type.
- Year-end accruals included; paid within 15 days.
- Certificates issued and copied with the return.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income and Corporation Tax Act Cap. 17.01, revised to 1 January 2025: read for s.39, s.52, Schedule 1 paras.1 to 6 (scope, accruals, rates, certificates, return, payer liability) and the exemption orders list | https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf | 2026-11-14 |

Not yet confirmed: amendments after 1 January 2025; the treaty rate matrix (no s.55 agreements read); penalties for late payment.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ms-nonresident-withholding` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ms-nonresident-withholding. If neither is available, confirm every figure against the official source pages cited above before relying on it.
