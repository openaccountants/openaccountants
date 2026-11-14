---
name: brunei-tax
description: Start here for any Brunei Darussalam tax or bookkeeping question in 2026. Routes to the right Brunei skill (company tax, withholding, payroll and SPK, VAT position, personal tax, formation), states the refusals (petroleum, VAT return requests), and gives the bank-statement classification patterns for Brunei books (BIBD, Baiduri, Standard Chartered, HSBC, utilities, TAP). Brunei has no VAT or GST and no personal income tax; companies pay corporate income tax. Trigger on Brunei tax, Brunei VAT, Brunei GST, corporate tax Brunei, MOFE filing or Brunei bookkeeping.
version: 3.0
jurisdiction: BN
category: orchestrator
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# Brunei Tax: Start Here v3.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Routing for Brunei Darussalam questions, tax year 2026 (year of assessment 2026 for companies), plus the bank-statement classification patterns used when keeping a Brunei company's books. This file holds no rates: each figure lives in the skill named below, with its official source.

**Two facts that prevent most errors.** Brunei has no VAT, GST or any consumption tax, so there is never a VAT return to prepare. Brunei has no personal income tax, so individuals and business names file nothing for income tax. Corporate income tax applies to companies only.

## The method, step by step

1. **Identify the person.** Company (Sdn Bhd, Bhd, branch), sole proprietor or partnership (business name), individual, or a foreign business paying or selling into Brunei.
2. **Route by question.**

| Question | Load |
|---|---|
| Company tax, ECI, the 30 June return, thresholds, deductions, capital allowances, tax credits, penalties | [bn-corporate-income-tax](bn-corporate-income-tax.md) |
| Paying a non-resident (interest, royalties, technical or management fees, rent of equipment, directors' fees), treaties | [bn-corporate-income-tax](bn-corporate-income-tax.md), Cross-border points |
| Salary tax, expat tax, sole proprietor tax | [bn-income-tax](bn-income-tax.md) |
| VAT, GST, sales tax, imported services, stamp duty basics | [bn-vat-gst](bn-vat-gst.md) |
| Payroll, TAP, SCP, SPK, e-Amanah | [bn-payroll-social](bn-payroll-social.md) |
| Setting up a company, ROCBN, OCP | [bn-company-formation](bn-company-formation.md) |
| What taxes exist at all | [bn-tax-overview](bn-tax-overview.md) |

3. **Before computing**, ask: entity type; financial year end; oil and gas activity (refuse); payments to non-residents; staff who are citizens or permanent residents.
4. **Books for a Brunei company.** Record amounts gross: there is no VAT to extract. Bank exports from BIBD and Baiduri come as CSV or PDF in BND, often with Malay descriptions. Exclude internal transfers. Classify with the table below, then hand the profit to [bn-corporate-income-tax](bn-corporate-income-tax.md) for chargeable income.

### Bank-statement patterns

| Pattern on the statement | Treatment | Note |
|---|---|---|
| BIBD, BANK ISLAM BRUNEI; BAIDURI; STANDARD CHARTERED; HSBC | Bank charges: deductible expense | No VAT component |
| INTEREST (debit) | Interest expense: deductible if the borrowing earns taxable income | Interest paid to a non-resident lender carries withholding |
| MOFE, REVENUE DIVISION | Income tax payment: not deductible | Income tax is a disallowed deduction |
| TAP, TABUNG AMANAH PEKERJA, SPK | Employer contribution: deductible; employee share is a payroll deduction | Approved fund |
| DES, DEPARTMENT OF ELECTRICAL SERVICES | Utilities: deductible | No consumption tax |
| DST, PROGRESIF, IMAGINE | Telecoms: deductible | No consumption tax |
| GOOGLE, MICROSOFT, META, AWS, ZOOM, SLACK, CANVA | Software and services: deductible | Check whether the payment is a royalty or technical fee to a non-resident (withholding) |
| SALARY, WAGES, GAJI | Staff costs: deductible | No income tax withheld from employees |

### Conservative defaults

| Unknown | Default |
|---|---|
| Whether the client owes consumption tax | No: none exists |
| Whether a payment abroad needs withholding | Flag it and ask what it pays for |
| Whether the client is a company | Ask; only companies pay income tax |

## Worked cases

**Case. Two statement lines for a Brunei company.** A BND 10,000 credit from a local client is revenue with no VAT. A BND 500 debit to AWS for cloud hosting is a deductible expense with no VAT; it is a service, so ask whether the contract makes it a payment for use of technical knowledge (withholding applies to some such payments) before closing the line.

```oa-check
name: Brunei statement lines, no VAT to extract
inputs:
  sale: 10000
  aws: 500
steps:
  - vat_on_sale: sale * 0
  - vat_on_aws: aws * 0
  - profit_effect: sale - aws
expected:
  vat_on_sale: 0.00
  vat_on_aws: 0.00
  profit_effect: 9500.00
```

## When to refuse or refer

| Code | Trigger | Message |
|---|---|---|
| R-BN-1 | Client in oil and gas exploration or production | "Petroleum companies are taxed under the Income Tax (Petroleum) Act (Chapter 119) at 55%. This is outside these skills; please refer to a specialist." |
| R-BN-2 | Request to prepare a VAT or GST return | "Brunei has no VAT, GST or other consumption tax, so no such return exists. I can help with corporate income tax instead." |
| R-BN-3 | Treaty relief on a payment abroad | "Read the agreement with the payee's country and obtain a certificate of residence first; see bn-corporate-income-tax." |

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Revenue Division, FAQ corporate tax | Read for who is taxed (companies only) and the absence of personal income tax | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ | 2026-11-14 |
| Revenue Division, types of taxes: income tax | Read for the petroleum rate, deductible and disallowed items (income tax, approved funds) | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ | 2026-11-14 |
| Revenue Division, relevant Acts | Read for the Acts administered (no VAT or GST Act) | https://www.mof.gov.bn/div_revenue_taxresources_relevantacts/ | 2026-11-14 |
| Revenue Division, payment of tax | Read for the banks offering tax payment (Baiduri, BIBD, Standard Chartered) | https://www.mof.gov.bn/div_revenue_paymentoftax/ | 2026-11-14 |

Not yet confirmed: the old file's "55% + 20%" petroleum rate (the Revenue Division page states 55% only; the 20% is removed); the old file's 15% royalty withholding rate, which was wrong (the Revenue Division table gives 10%, now in bn-corporate-income-tax).
