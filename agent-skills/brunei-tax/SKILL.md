---
name: brunei-tax
description: "Start here for any Brunei Darussalam tax or bookkeeping question in 2026. Routes to the right Brunei skill (company tax, withholding, payroll and SPK, VAT position, personal tax, formation), states the refusals (petroleum, VAT return requests), and gives the bank-statement classification patterns for Brunei books (BIBD, Baiduri, Standard Chartered, HSBC, utilities, TAP). Brunei has no VAT, GST or general domestic personal income tax. Corporate income tax, non-resident withholding and excise can apply. Trigger on Brunei tax, Brunei VAT, Brunei GST, corporate tax Brunei, MOFE filing or Brunei bookkeeping."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/brunei-tax"
  jurisdiction: "BN"
  tax_year: "2026"
  last_updated: "2026-11-22"
---

# Brunei Tax: Start Here v3.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Routing for Brunei Darussalam questions, tax year 2026 (year of assessment 2026 for companies), plus the bank-statement classification patterns used when keeping a Brunei company's books. This file holds no rates: each figure lives in the skill named below, with its official source.

Brunei has no VAT or GST return. Excise applies to specified goods. Individuals and unincorporated businesses have no ordinary domestic income tax return. Withholding rules can still apply to covered payments to or by individuals. Companies can be subject to corporate income tax.

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
4. **Books for a Brunei company.** Record amounts gross: there is no VAT to extract. Bank exports from BIBD and Baiduri come as CSV or PDF in BND, often with Malay descriptions. Reconcile both sides of internal transfers and exclude them from income and expenses. Confirm the transaction behind each bank description before applying the table, then hand the profit to [bn-corporate-income-tax](bn-corporate-income-tax.md) for chargeable income.

### Bank-statement patterns

| Pattern on the statement | Treatment | Note |
|---|---|---|
| BIBD, BANK ISLAM BRUNEI; BAIDURI; STANDARD CHARTERED; HSBC | Match the bank entry to its underlying transaction | Deduct confirmed revenue expenses incurred wholly and exclusively to earn chargeable income |
| INTEREST (debit) | Interest expense: deductible if the borrowing earns taxable income | Check Brunei source, payee status, permanent establishment and treaty relief for non-resident interest |
| MOFE, REVENUE DIVISION | Match to the assessment or payment notice | Company income tax is not deductible |
| TAP, TABUNG AMANAH PEKERJA, SPK | Employer contribution: deductible; employee share is a payroll deduction | Approved fund |
| DES, DEPARTMENT OF ELECTRICAL SERVICES | Confirm the business utility expense | No Brunei VAT or GST |
| DST, PROGRESIF, IMAGINE | Confirm the business telecommunications expense | No Brunei VAT or GST |
| GOOGLE, MICROSOFT, META, AWS, ZOOM, SLACK, CANVA | Confirm the business expense and its revenue or capital treatment | Check whether a payment to a non-resident is a covered royalty or technical fee |
| SALARY, WAGES, GAJI | Staff costs: deductible | No income tax withheld from employees |

### Conservative defaults

| Unknown | Default |
|---|---|
| Whether the client owes an indirect tax | Check import duties or excise for the goods. Brunei has no VAT or GST |
| Whether a payment abroad needs withholding | Flag it and ask what it pays for |
| Whether the client is a company | Ask for the legal form, residence and role in any withholding payment |

## Worked cases

**Case. Two statement lines for a Brunei company.** A BND 10,000 credit from a local client is revenue with no VAT. A BND 500 debit to AWS covers ordinary cloud hosting used wholly and exclusively to earn chargeable income. The stipulated business expense has no Brunei VAT. Check the contract and source before deciding whether the payment falls under non-resident withholding for royalties, use of knowledge or technical services. The operating profit from these two entries is BND 9,500 before any other adjustments.

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
| R-BN-2 | Request to prepare a VAT or GST return | "Brunei has no VAT or GST return. If your question is about goods, check customs import duty and excise." |
| R-BN-3 | Treaty relief on a payment abroad | "Check the treaty, payment and permanent establishment facts. Apply the domestic withholding at payment and use the applicable treaty refund procedure with supporting evidence. See bn-corporate-income-tax." |

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Revenue Division, FAQ corporate tax | Read for who is taxed (companies only) and the absence of personal income tax | https://www.mof.gov.bn/div_revenue_faq_corporatetax/ | 2026-11-14 |
| Revenue Division, types of taxes: income tax | Read for the petroleum rate, deductible and disallowed items (income tax, approved funds) | https://www.mof.gov.bn/div_revenue_typesoftaxes_incometax/ | 2026-11-14 |
| Revenue Division, relevant Acts | Read for the Acts administered (no VAT or GST Act) | https://www.mof.gov.bn/div_revenue_taxresources_relevantacts/ | 2026-11-14 |
| Revenue Division, payment of tax | Read for the banks offering tax payment (Baiduri, BIBD, Standard Chartered) | https://www.mof.gov.bn/div_revenue_paymentoftax/ | 2026-11-14 |

| Income Tax Act, Chapter 35 | Sections 11, 12 and 35–37B on deductions and withholding | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-35-2024-ED-INCOME-TAX-ACT.pdf | 2026-11-22 |
| Income Tax (Petroleum) Act | Section 13 on petroleum tax | https://www.agc.gov.bn/wp-content/uploads/2026/07/CAP-119-6-2022-ED-INCOME-TAX-PETROLEUM-ACT.pdf#page=28 | 2026-11-22 |
| Excise Order 2006 | Excise duty on specified goods | https://www.agc.gov.bn/wp-content/uploads/2026/08/S-40-2006-E.pdf | 2026-11-22 |
| Revenue Division withholding ruling | Section 19 on domestic withholding and treaty refunds | https://www.mof.gov.bn/wp-content/uploads/2025/10/PR_004-2017_Public_Ruling_on_Witholding_of_Tax.pdf | 2026-11-22 |

Not yet confirmed: the provider-specific withholding position for cloud hosting without the contract, source and payee details. Bank export format depends on the account and channel.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-22. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `brunei-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/brunei-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
