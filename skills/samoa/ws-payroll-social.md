---
name: ws-payroll-social
description: "Samoa payroll and social contributions for 2026: source-cited rules, conditions, filing boundaries and recomputing cases. Not yet approved by an accountant."
jurisdiction: WS
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
category: payroll
version: 0.1
---

# Samoa Payroll and Social Contributions v0.1

> **General reference only.** This skill supports AI-assisted working papers. It is not approval to file, pay or take a tax position for a particular person. Obtain qualified local review of the facts, applicable law and filing instructions.

## Who this applies to

Employers paying ordinary wages in Samoa in 2026: operate PAYE, register and contribute to SNPF, and separately register/pay ACC levies. Establish employee status, wage components, pay frequency and any exemption before computing. SNPF’s statutory employee definition extends beyond conventional full-time employees; do not exclude casual or family-business work solely because no formal employment contract exists. [section 93](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 19](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf); [section 20](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf); [registration and levy payment frequency](https://acc.gov.ws/index.php/faq/).

## Rates, bands and thresholds

| Item | Rule or amount | Official source |
|---|---|---|
| Primary PAYE, fortnight | WST 0-576: 0% (in words on the page: nil); WST 577-962: 20% of the slice above WST 576; above WST 962: 27% of the excess plus WST 77.20 derived band tax. Use the official whole-tala table and its rounding instructions. | [Schedule 1 paragraph 7](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [fortnightly whole-tala table, effective 1 January 2018](https://revenue.gov.ws/wp-content/uploads/2022/09/Manual-Schedule-Fortnight-1.pdf) |

| Annual bands | The annual 0% / 20% / 27% scale and WST 15,000 / WST 25,000 breakpoints belong to [personal income tax](ws-income-tax.md). Do not divide annual thresholds to replace the published fortnightly thresholds. | [Schedule 1 paragraphs 1-2](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [Schedule 1 paragraph 7](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf) |

| Secondary employment | 27 sene per tala of secondary earnings where working for multiple employers in the same pay period, equivalent to 27% derived; the official table requires an annual return for secondary-income employees. | [footnotes, secondary employment](https://revenue.gov.ws/wp-content/uploads/2022/09/Manual-Schedule-Fortnight-1.pdf) |

| SNPF ordinary split | 10% employee deduction plus 10% employer contribution, total 20% of gross wages. Older 7% figures are superseded; the current employer instructions and Act specify the current split. | [Employees Contribution, current 10% + 10%](https://www.npf.ws/employers-guide); [section 22](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf) |

| SNPF low-paid exception | If wages are below the statutory minimum rate, no employee deduction: employer pays the full 20%. Do not use the stale minimum-wage amount on the SNPF webpage; verify the applicable employment rate. | [section 22](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf); [Employees Contribution, current 10% + 10%](https://www.npf.ws/employers-guide) |

| ACC employee and employer | Each pays 1 sene per complete tala of wages: 1% equivalent derived, with the complete-tala condition retained. This is separate from the SNPF base and remittance. | [section 52, complete tala and payment determination](https://acc.gov.ws/wp-content/uploads/2026/05/ACC-ACT-Consolidated-2022-1.pdf) |

| Combined ordinary employer share | 11% derived only where the ordinary SNPF 10% employer share and ACC 1% equivalent use the same whole-tala wage base. It is a subtotal for these contributions, not a universal all-in employment cost; the low-paid SNPF exception changes it. | [section 22](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf); [section 52, complete tala and payment determination](https://acc.gov.ws/wp-content/uploads/2026/05/ACC-ACT-Consolidated-2022-1.pdf) |

## The base

SNPF wages include gross wages, salary, remuneration and commission, overtime, allowances, bonuses and employment compensation, and statutory board/lodging/support components. Section 22 applies to wages paid or payable without stating an earnings ceiling; do not invent a cap, or assume every noncash component has the cash valuation used in the examples. Keep a contribution schedule and duplicate. Extra voluntary deductions require the employee’s written instruction; the ordinary deduction cannot be increased at will. [section 2, wages definition](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf); [section 22](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf).

Compute PAYE using the actual pay-period table, then statutory employee deductions; add employer contributions separately to gross wages. PAYE salary/wage tax is generally final, while mixed wage/business income needs the personal-income statutory interaction and secondary employment needs its stated reconciliation. Do not treat the employee’s annual allowance as an additional payroll deduction. The older PAYE sheet’s minister-of-religion treatment is superseded by the later Income Tax amendment and is not a safe instruction. [Schedule 1 paragraph 7](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [fortnightly whole-tala table, effective 1 January 2018](https://revenue.gov.ws/wp-content/uploads/2022/09/Manual-Schedule-Fortnight-1.pdf); [footnotes, secondary employment](https://revenue.gov.ws/wp-content/uploads/2022/09/Manual-Schedule-Fortnight-1.pdf); [section 9](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 60](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [sections 1-6, scanned pages visually checked](https://revenue.gov.ws/wp-content/uploads/2025/01/Income-Tax-Amendment-Act-2022-No.5-1.pdf).

## Deadlines and filing

Register for PAYE using IR11; file monthly P4 showing every employee, including those below the taxable threshold. File and pay by the 15th of the following month. Use the correct current form and actual payroll records; the information sheet was printed in 2020 and republished in October 2026. [Employer obligations; printed 21 August 2020, republished October 2026](https://revenue.gov.ws/wp-content/uploads/2026/10/IS02_Salary-and-Wage-Income-Tax-2026.pdf); [section 99](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf).

SNPF ordinary contributions and schedule are monthly, due no later than the 7th of the next month after wages were paid or became due/payable, unless a written CEO direction changes the method/date. Register the employer and employees first, with incorporation/licence and employee/wage records. ACC is paid separately to ACC; its frequency depends on wage frequency and statutory/Corporation directions, not automatically SNPF’s date. Obtain the actual ACC schedule or notice. [section 19](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf); [section 20](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf); [section 22](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf); [section 52, complete tala and payment determination](https://acc.gov.ws/wp-content/uploads/2026/05/ACC-ACT-Consolidated-2022-1.pdf); [registration and levy payment frequency](https://acc.gov.ws/index.php/faq/).

## Penalties and interest

PAYE late returns/payments are subject to the [income-tax penalty and interest rules](ws-income-tax.md#penalties-and-interest); the payer remains personally liable for failure to withhold/remit. SNPF section 25 imposes a 24% annual surcharge from due date if contributions remain unpaid 14 days after due date; the guide describes 2% monthly after month-end grace, an equivalent nominal rate but not a substitute day-count calculation. The Fund may remit surcharge. [section 99](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [section 25](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf); [Employees Contribution, current 10% + 10%](https://www.npf.ws/employers-guide).

ACC has a separate late-levy surcharge with a 14-day trigger, daily rate of 1/20%, statutory accrual reference after 7 days from wage payment, WST 1 minimum and rounding up to the next WST 1. Do not apply the SNPF surcharge to ACC or calculate ACC arrears without the wage dates, due-date direction, payment date and statutory text. [section 52A, late levy surcharge](https://acc.gov.ws/wp-content/uploads/2026/05/ACC-ACT-Consolidated-2022-1.pdf).

## Cross-border points

Do not import American Samoa, New Zealand or Fiji payroll rules. Cross-border employment needs the Samoa employment-source rule, residence and exemption evidence. SNPF alternative funds and separate health-scheme provisions require their own application/operational evidence; the subtotal here covers the identified ordinary SNPF and ACC contributions only. [section 7](https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf); [Part 13 section 90, separate Medisave provisions](https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf).

## Two worked examples that recompute

### Ordinary fortnightly employee

Assume WST 1,000 whole-tala cash wages in a primary job, no exempt benefits, ordinary SNPF coverage and wages above the applicable minimum. PAYE = WST 77.20 + 27% × WST 38 = WST 87.46. Employee SNPF is WST 100 and ACC WST 10; net is WST 802.54. Employer SNPF and ACC total WST 110, giving WST 1,110 cash cost for these items, all derived.

```oa-check
name: Ordinary fortnightly employee
inputs:
  gross: 1000
steps:
  - paye: (962 - 576) * 0.20 + (gross - 962) * 0.27
  - employee_npf: gross * 0.10
  - employee_acc: floor(gross) * 0.01
  - net: gross - paye - employee_npf - employee_acc
  - employer_cost: gross + gross * 0.10 + floor(gross) * 0.01
expected:
  paye: 87.46
  net: 802.54
  employer_cost: 1110
```

### SNPF deduction barred by low wage

Assume WST 400 fortnightly cash wages, with the worker proved to fall below the applicable statutory minimum-rate condition. This example illustrates the contribution consequence and does not approve underpayment of wages. Primary PAYE is nil. Employee SNPF is nil, employer SNPF WST 80, and each ACC share WST 4. Net is WST 396 and employer cost for these items WST 484, derived. The ordinary 11% employer subtotal would be wrong here.

```oa-check
name: SNPF deduction barred by low wage
inputs:
  gross: 400
steps:
  - paye: 0
  - employee_npf: 0
  - employer_npf: gross * 0.20
  - employee_acc: floor(gross) * 0.01
  - employer_acc: floor(gross) * 0.01
  - net: gross - paye - employee_npf - employee_acc
  - employer_cost: gross + employer_npf + employer_acc
expected:
  net: 396
  employer_cost: 484
```

## Ask the client first

- Which worker status, citizenship/residence, working location and fund registrations?
- Which pay period, primary/secondary job, gross components and noncash benefits?
- What hours and applicable minimum wage, voluntary instructions or approved alternative arrangements?
- What PAYE returns, SNPF schedule, ACC payment direction and arrears dates?

## Sources

Read on **2026-11-15** for the stated sections. The Attorney General tax consolidations are official texts as at 31 December 2023; current Ministry guidance and the later instruments expressly identified below were checked separately. A recent upload path does not change a document’s printed date.

| Source and scope actually read | URL | Read on |
|---|---|---|
| Read for section 52, complete tala and payment determination; section 52A, late levy surcharge | https://acc.gov.ws/wp-content/uploads/2026/05/ACC-ACT-Consolidated-2022-1.pdf | 2026-11-15 |
| Read for registration and levy payment frequency | https://acc.gov.ws/index.php/faq/ | 2026-11-15 |
| Read for Schedule 1 paragraphs 1-2; section 60; section 7; section 9; section 93; section 99; Schedule 1 paragraph 7 | https://www.ag.gov.ws/wp-content/uploads/2024/02/Income-Tax-Act-2012.pdf | 2026-11-15 |
| Read for Part 13 section 90, separate Medisave provisions; section 19; section 20; section 22; section 25; section 2, wages definition | https://www.npf.ws/_files/ugd/2b7bf6_424e99682c134c08aa7789baf544d3c3.pdf | 2026-11-15 |
| Read for sections 1-6, scanned pages visually checked | https://revenue.gov.ws/wp-content/uploads/2025/01/Income-Tax-Amendment-Act-2022-No.5-1.pdf | 2026-11-15 |
| Read for fortnightly whole-tala table, effective 1 January 2018; footnotes, secondary employment | https://revenue.gov.ws/wp-content/uploads/2022/09/Manual-Schedule-Fortnight-1.pdf | 2026-11-15 |
| Read for Employer obligations; printed 21 August 2020, republished October 2026 | https://revenue.gov.ws/wp-content/uploads/2026/10/IS02_Salary-and-Wage-Income-Tax-2026.pdf | 2026-11-15 |
| Read for Employees Contribution, current 10% + 10% | https://www.npf.ws/employers-guide | 2026-11-15 |

Not yet confirmed: Client-specific exemptions and noncash valuations; non-fortnightly PAYE conversion/rounding beyond the published table; exact ACC payment notice; separate Medisave/Medinsure operational liability and alternative-fund conditions; a universal SNPF/ACC combined remittance date. Do not present the 11% subtotal as all payroll costs or apply obsolete 7% SNPF or the guide’s stale minimum-wage amount.
