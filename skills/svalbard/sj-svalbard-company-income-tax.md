---
name: sj-svalbard-company-income-tax
description: >
  Svalbard company income-tax scope and rate reference for 2026. Covers local office and management, nonresident business duration, property income, allocation between Svalbard and mainland activity, ordinary sixteen-percent taxation and the special twenty-two-percent profit band. Uses the enacted annual decision rather than a budget proposal and includes numerical examples showing how payroll and physical assets affect the higher-rate slice. Distinguishes companies from sole proprietors and employee residence. Filing guidance is included with scope limits. Formation, detailed deductions, international relief, withholding procedures and independent accountant review remain outstanding.
version: 0.2
jurisdiction: SJ
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Svalbard: company income tax in 2026

## Which companies and income are within scope?

A company with an office on Svalbard that is managed from there is resident under [Svalbard Tax Act section 2-3](https://lovdata.no/dokument/NL/lov/1996-11-29-68). The starting point is liability on all income, subject to the statutory exceptions. Business income earned outside Svalbard is excluded where it is demonstrated to be taxable under other Norwegian taxation or in a foreign state. Income from property or installations outside Svalbard is separately excluded. Do not treat a registered address as proof of actual management.

A nonresident company's income from Svalbard business falls within section 2-4 if that business lasts **at least thirty continuous days**. Local real-property rules also apply through section 2-2(3); they are not conditional on a thirty-day business stay. [Sections 2-2 to 2-4](https://lovdata.no/dokument/NL/lov/1996-11-29-68).

The administration's [business page](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/svalbard/naring-pa-svalbard/) uses both “over thirty” and “thirty or more” wording. The statute controls: exactly thirty continuous days satisfies section 2-4. Company activity and individual employee stays must be tested separately. A rotating workforce does not establish that the company's activity was interrupted whenever one employee left.

## Tax base and 2026 rates

Section 3-2 applies the Norwegian Tax Act to other income with specified exceptions. It does not simply import every mainland deduction and tax regime. The [2026 Svalbard tax decision, section 3](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780) provides:

- **16%** for other income under paragraph (c), including ordinary company profit outside the higher-rate slice.
- **22%** on the part of company profit that exceeds **NOK 15 million** and also exceeds the sum of ten times payroll costs subject to Svalbard withholding plus 20% of the tax value of installations, real property and other physical capital situated on Svalbard at year end.

Both higher-rate thresholds must be exceeded. Use qualifying payroll costs and tax values of qualifying physical assets, not all group payroll or accounting book value. [Decision section 3(b)](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780).

For positive taxable company profit P, qualifying payroll W and qualifying year-end physical-asset tax value A, a calculation expressing the statutory thresholds is:

`higher-rate slice = max(0, P − max(15,000,000, 10 × W + 0.20 × A))`

`tax = 16% × (P − higher-rate slice) + 22% × higher-rate slice`

This is an explanatory calculation of section 3, not a replacement for determining taxable profit or qualifying costs/assets.

## Worked company examples

All amounts are NOK. Assume the supplied profit is taxable company profit, payroll and assets qualify, and no other relief or special rule changes the result.

| Profit | Payroll | Physical-asset tax value | Substance threshold | 22% slice | Income tax |
|---:|---:|---:|---:|---:|---:|
| 10,000,000 | 0 | 0 | 0 | 0 | 1,600,000 |
| 20,000,000 | 1,000,000 | 10,000,000 | 12,000,000 | 5,000,000 | 3,500,000 |
| 20,000,000 | 2,000,000 | 10,000,000 | 22,000,000 | 0 | 3,200,000 |
| 30,000,000 | 2,000,000 | 10,000,000 | 22,000,000 | 8,000,000 | 5,280,000 |

The second example uses the NOK 15 million floor despite the lower substance threshold. The fourth uses NOK 22 million because that exceeds the floor. [2026 decision section 3](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780).

## Allocation and filing

For activity split between mainland Norway and Svalbard, the [Tax Administration](https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/svalbard/naring-pa-svalbard/) requires allocation in the business specification under “Fordelt beregnet næringsinntekt”, supported by an attachment explaining Svalbard income and deductible costs. Project accounts can support that explanation. Keep the duration and location evidence alongside the allocation; a percentage split without supporting activity records does not establish the statutory source conditions.

The same page gives **31 May** as the ordinary electronic business-return deadline. Check the relevant filing-year calendar, extensions and payment schedule separately; a return deadline is not proof of a tax-payment deadline.

## Distinguish other taxpayers and distributions

Sole proprietors have special rules under section 3-2(4), including income taxed at the salary rates and participation in the combined twelve-basic-amount threshold. They must not use this company-rate worksheet. The NOK 20,000 paragraph (c) deduction in the annual decision is for individual taxpayers, not a general company allowance. [Act section 3-2](https://lovdata.no/dokument/NL/lov/1996-11-29-68); [decision section 3](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780).

The annual decision's section 6 specifies **20%** for dividends within its cross-reference to Norwegian Tax Act section 10-13. This Guide does not establish every recipient's withholding liability or any relief. Determine the recipient, statutory scope and applicable relief before a distribution; do not substitute the company's 16% rate for a shareholder calculation. [Decision section 6](https://lovdata.no/dokument/STV/forskrift/2025-12-19-2780).

## Verification limits

Svalbard only; Jan Mayen is outside this Guide. Checked 22 October 2026 against the consolidated Act and enacted annual decision. Formation, accounts, detailed deductions and losses, special company regimes, withholding administration, VAT/customs, treaties, payment and independent accountant review remain outstanding. These three initial topics do not constitute comprehensive jurisdiction coverage.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
