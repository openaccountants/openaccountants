---
name: mw-payroll-social
description: "Malawi draft for 2026 payroll reconciliation and occupational pension contribution working papers under the cited pension statute. Use it only after confirming that the mandatory scheme applies to the employer and employees concerned. It separates employer and employee contributions, contribution remittance duties and supplied PAYE amounts, with two arithmetic controls for individual and aggregate payroll schedules. It does not assume that pension contributions are automatically deductible before applying the income-tax bands. Commencement and exemption orders, defined-benefit directions, expatriate coverage, sector levies, current interest and authenticated fund procedures remain explicit limitations. This is a conditional partial job rather than a complete Malawi payroll filing service."
jurisdiction: MW
tax_year: 2026
tax_year_notes: "Intended 2026 research draft; Act 3/2026 and appointed commencement chain unverified; live use held."
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
version: 1.2
---

# Malawi payroll: pension contributions and PAYE reconciliation v1.2

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person’s facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in Malawi.

## Who this applies to

**Current-year source hold.** This is a draft reconstruction of the cited provisions, not confirmed operative 2026 coverage. The enacted Taxation (Amendment) Act 3 of 2026 and appointed commencement notices for the Tax Administration Act and the 2021 administrative cutover have not been read. Do not use this draft to determine an actual 2026 tax position, file, pay or complete a live registration/notice response until those checks are closed. The examples illustrate the cited-text assumptions only. The 2026 year label identifies the intended research period, not completed verification.

Use where the Pension Act 2023 mandatory occupational scheme applies, after confirming the employee/employer is not covered by an exemption order under 11. Section 10 requires covered employees to join a fund. This Guide computes the Act’s minimum contribution amounts and remittance reconciliation; it does not establish every exempt category or the 2023 commencement order. [Pension 10–12](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf). PAYE rates belong to [individual income tax](mw-income-tax.md). Do not claim that this pension exhausts all payroll-linked levies.

## Rates, bands and thresholds

| Covered mandatory occupational scheme rule | Amount / period | Official Act |
|---|---|---|
| Employer minimum contribution | 10% pensionable emoluments | [Pension 12(1)(a)](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf) |
| Employee minimum contribution | 5% pensionable emoluments | [Pension 12(1)(b)](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf) |
| Employer contribution remittance | No later than 14 days after end of month liability arose | [Pension 13(1)](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf) |
| Employee amount deducted or that should be deducted | No later than 14 days after relevant month-end; employer liability on failure to deduct | [Pension 13(2)](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf) |
| Required employee life-insurance cover, additional to pension | At least annual pensionable emoluments | [Pension 14(1)](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf) |

Higher agreed rates require notification to the Registrar; existing higher employer contributions must not be reduced merely to the statutory minimum. An employer can bear all or part of the employee contribution, preserving the minimum total, and defined-benefit funding follows the directives (12(3)–(8)).

## The base

Pensionable emoluments means guaranteed wages and other earnings, excluding personal investment income, capital gains and employer provision of a house or motor vehicle (section 2). Establish that base from the contract and fund rules; do not simply assume basic pay alone. Calculate contributions separately from the confirmed PAYE taxable base. The old instruction to deduct pension automatically before PAYE is not established by the Pension Act and is not used. If the employer fails to deduct the employee share, section 13(2)(b) makes it liable to pay the total that ordinarily represents both shares; this is not a licence to omit remittance. [Pension 2,12–13](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf).

## Deadlines and filing

Reconcile payroll by employee: gross cash, pensionable base, employee deduction, employer expense, independently computed PAYE, net cash and pension/tax payables. Send pension contributions to the trustee or as it directs within the section 13 window and retain the contribution schedule, transfer proof and fund allocation evidence. Keep PAYE records and the monthly statement under PAYE Rule 6; Rule 10 requires remittance within fourteen days after month-end. [Pension 13](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf); [PAYE Rules 6,10](https://elibrary.rat.gov.mw/server/api/core/bitstreams/06b35bf5-faa2-4fa1-81f7-af650cce4dff/content). Use the current approved tax and fund channels; authenticated portal fields have not been inspected.

## Penalties and interest

Pension 13(3)–(4) invokes enforcement under 10(3) and interest prescribed by ministerial order for each month or part, including outstanding penalty interest. No interest rate is invented here. Tax late-payment consequences follow TAA 87 in [company tax](mw-corporate-income-tax.md). Pension arrears and PAYE arrears are distinct liabilities. [Pension 10,13](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf).

## Cross-border points

Check expatriate/secondment coverage and exemptions against actual orders rather than assuming all foreign employees are excluded. A foreign employer/payment location does not by itself settle PAYE source or pension coverage. International social-security or treaty relief remains unverified.

## Two worked examples that recompute

Hypothetical covered employee, ordinary minimum rates, no higher existing rates or defined-benefit directive. Confirmed pensionable base equals the stated gross cash only in this case. PAYE is an independently approved input, not calculated by subtracting pension.

```oa-check
name: Covered payroll reconciliation
inputs:
  gross_cash: 1000000
  pensionable: 1000000
  approved_paye: 249000
steps:
  - employee_pension: pensionable * 0.05
  - employer_pension: pensionable * 0.10
  - pension_payable: employee_pension + employer_pension
  - net_cash: gross_cash - employee_pension - approved_paye
  - employer_cost: gross_cash + employer_pension
expected:
  employee_pension: 50000
  employer_pension: 100000
  pension_payable: 150000
  net_cash: 701000
  employer_cost: 1100000
```

Second, three equal covered employees; distinguish employer expense from total payable.

```oa-check
name: Pension schedule aggregation
inputs:
  employees: 3
  pensionable_each: 800000
steps:
  - base: employees * pensionable_each
  - employee_total: base * 0.05
  - employer_total: base * 0.10
  - fund_payable: employee_total + employer_total
expected:
  base: 2400000
  employee_total: 120000
  employer_total: 240000
  fund_payable: 360000
```

## Ask the client first

Get employment/fund membership and exemption evidence, applicable directives, guaranteed earnings and benefit types, agreed/historical rates, employer-borne employee contributions, pay month, trustee instructions, life-cover policy, independently approved PAYE computation and contribution/payment history.

## Sources

| Official source and portions actually read | Read on |
|---|---|
| [Ministry of Labour Pension Act 2023](https://www.labour.gov.mw/images/documents/Malawi-Pension-Act_2023.pdf), ss 1–2,8–14; contribution and liability provisions read in full | 2026-11-01 |
| [Taxation official-library copy](https://elibrary.rat.gov.mw/server/api/core/bitstreams/06b35bf5-faa2-4fa1-81f7-af650cce4dff/content), PAYE Rules 3,6,10 only; old salary rates not used | 2026-11-01 |
| [TAA 2021](https://elibrary.rat.gov.mw/server/api/core/bitstreams/42eb322b-f2a9-48b9-baaf-01c2ade040f5/content), s 87 tax late-payment framework | 2026-11-01 |

**Not yet confirmed:** enacted Taxation (Amendment) Act 3/2026 effects and appointed commencement notices for TAA/cutover;  current exemption/commencement orders and defined-benefit directives, payroll tax deductibility of contributions, TEVET levy 1%/base and sector levies, pension interest order, complete fund portal process and expatriate coverage. The old blanket no-social-tax claim and automatic pension-before-PAYE rule are not verified. Do not use the illustrative minimum computation before confirming that the mandatory scheme applies.

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
