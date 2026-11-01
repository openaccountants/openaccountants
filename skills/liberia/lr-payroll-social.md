---
name: lr-payroll-social
description: "Computes Liberia NASSCORP contributions for employees within the verified pension and employment-injury categories and sets the separate payroll withholding, contribution payment and employee-detail recording calendars for 2026. Use for Liberia payroll, NASSCORP, employer contributions, pension deductions, employee registration, an expatriate worker or a missed remittance. The Guide reads the 2017 Act with the 2023 General Regulations, distinguishes gross remuneration from excluded expenses and prevents recovery of the employer share from workers. It routes personal tax bands to the income Guide. Entry-age, membership and statutory exclusions must be checked; retroactive employee deductions and live submission details remain explicit gaps, without a claim of professional attestation."
jurisdiction: LR
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
version: 0.2
---

# Liberia Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: 2026. Read on: 2026-11-01. Source-cited country draft; currentness gaps are listed below.

## Who this applies to

Employers with at least one employee enter the statutory pension/injury scheme, subject to express exclusions. Check age of entry, existing membership and category. Armed forces, specified foreign diplomatic/international staff recruited abroad, home outworkers, resident household family, domestic servants and vessel workers have statutory exclusions; nationality alone is not an exemption. [s 89.8(a)–(e),89.15](https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf) [S01]

The Act sets maximum pension entry ages 48 for persons born 1980 or later,51 for persons born before 1980; existing membership and the category schedules matter. This is an entry test, not an instruction to remove an existing member at 48/51. [s89.8(e), s89.16(f)](https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf) [S10] [s 89.8(a)–(e),89.15](https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf) [S01]

## Rates, bands and thresholds

| Rule | Condition and result | Official source |
|---|---|---|
| S02 | For an employee covered by both schemes: employee 4% pension; employer 4% pension plus 2% injury, total 10% gross remuneration. Injury-only and pension-only categories differ; pension contributions cease for persons attaining 65 by month end. | [s 89.16(a),(b)–(f)](https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf) [S02] |
| S03 | Insurable earnings include employment-service payments, salaries/wages/bonuses, but exclude employer ex-gratia payments and travel allowance/concession covering special employment expenses. Do not apply the percentage indiscriminately to every cash movement. | [reg 2 Earnings](https://www.nasscorp.org.lr/wp-content/uploads/2024/06/GenReg-2023.pdf) [S03] |

## The base

Do not deduct/recover employer contributions from employees. Employee deductions are held in trust. The Act restricts later recovery of a missed employee deduction; reg 16(2) has a bona-fide-error recovery clause, so obtain a legal resolution before retroactive deductions rather than assuming that regulation overrides the Act. [s 89.16(m)](https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf) [S07]

An employer hiring staff registers with NASSCORP within 15 days of becoming a legal entity, completes the office application/attachments and receives an employer code/certificate used on correspondence. [reg 4(1),(3),(6)](https://www.nasscorp.org.lr/wp-content/uploads/2024/06/GenReg-2023.pdf) [S08]

Notify NASSCORP in writing within 30 calendar days of suspending operations or an insured employee leaving. Failure can continue contribution liability subject to Director General waiver. [reg 6](https://www.nasscorp.org.lr/wp-content/uploads/2024/06/GenReg-2023.pdf) [S09]

Establish the pension/injury category before multiplying. Use insured remuneration, calculate and segregate employee and employer shares, and reconcile each registered employee. Compute resident income withholding separately using [Personal income tax](lr-income-tax.md). The old assertion that employee pension is deductible for income tax remains unconfirmed; do not silently net it off the salary-tax base.

## Deadlines and filing

Resident wages above the standard-deduction amount require withholding using resident rates. Remit monthly within 10 days after month end with payee identity, payment type/amount and tax withheld. [s 905(e),(j)](https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf) [W04]

Ordinary monthly contributions fall due at that month’s end, not the following month’s 10 th. Part-month/multiple-employer cases follow specified regulation conditions. [s 89.16(h)](https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf) [S04]

Pay monthly through an approved bank, NASSCORP office or directed method with a completed Payroll Submission Form and retain the official receipt, as regulation17 requires. Under regulation18(A)(1), record each employee’s earnings and contributions on the approved e-Payroll form by the end of the following month, matching registered names, numbers and payment currency. That is a recording deadline; a separate transmission deadline has not been confirmed. It does not replace the contribution payment deadline or the duty to accompany payment with the Payroll Submission Form. [regs 17(1)–(3),18(A)](https://www.nasscorp.org.lr/wp-content/uploads/2024/06/GenReg-2023.pdf) [S05]

Maintain separate calendars: contribution payment ordinarily at month-end with its accompanying Payroll Submission Form, and employee-detail recording on e-Payroll by following month-end. No separate e-Payroll transmission deadline is established here. The old following-month10 th social-payment claim is replaced. For LRA use Monthly Withholding Return and Schedule A Salary/Wages from its catalogue; actual boxes and live portal filing remain unverified. Use the official [LRA Forms and Schedules](https://www.lra.gov.lr/forms-and-schedules/) catalogue and [LITAS](https://elitas.lra.gov.lr/) link published by LRA. Select the tax kind, year and TIN; reconcile the return with the working paper and withholding credits; submit the applicable return and schedules, pay against the resulting reference and preserve submission/payment confirmation. The public catalogue was read; live portal screens, box numbers, payment references and a successful filing have not been verified. Stop before submission if the live workflow differs. [amended s50(b),(g),(h)](https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf) [O07]

## Penalties and interest

Default adds 4% of unpaid contributions for each month/part after due date, recoverable as debt. The Act also provides recovery where employer default reduces benefits; legal escalation is separate. [s 89.18](https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf) [S06]

For the general late-filing, late-payment, recordkeeping and interest rules, use [Tax overview](lr-tax-overview.md#penalties-and-interest). Do not invent a fixed interest rate or treat a civil late-payment charge as a criminal conviction.

## Cross-border points

Apply the statutory exclusions to expatriates rather than asserting that all foreigners are automatically exempt or included. Foreign diplomatic/UN recruitment conditions and vessel employment matter. Income-tax residence and NASSCORP category are separate tests. [s 89.8(a)–(e),89.15](https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf) [S01]

## Two worked examples that recompute

### Employee covered by both schemes

Assume monthly insured remuneration LRD 100,000, valid membership and both schemes. Employee pension 4,000; employer pension 4,000 plus injury 2,000; total remitted 10,000. Employer cost before other taxes 106,000. [s 89.16(a),(b)–(f)](https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf) [S02]

```oa-check
name: Employee covered by both schemes
inputs:
  earnings: 100000
steps:
  - employee: earnings * 0.04
  - employer_pension: earnings * 0.04
  - injury: earnings * 0.02
  - total: employee + employer_pension + injury
  - employer_cost: earnings + employer_pension + injury
expected:
  employee: 4000
  employer_pension: 4000
  injury: 2000
  total: 10000
  employer_cost: 106000
```

### Injury-only category changes the remittance

Assume NASSCORP has confirmed injury-only coverage, not a pension member. On LRD 100,000 earnings, employer injury is 2,000 and employee pension is zero. Applying both-scheme 10% would overstate remittance by 8,000. Do not decide category from age alone. [s 89.16(a),(b)–(f)](https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf) [S02]

```oa-check
name: Injury-only category changes the remittance
inputs:
  earnings: 100000
steps:
  - correct: earnings * 0.02
  - both_scheme: earnings * 0.10
  - overstatement: both_scheme - correct
expected:
  correct: 2000
  both_scheme: 10000
  overstatement: 8000
```

## Ask the client first

- Date of birth, scheme entry date, membership and pension/injury classification.
- Employer and employee registration codes and exclusion status.
- Pay components, bonuses, ex-gratia and employment-expense reimbursements.
- Payment dates, prior deductions, e-Payroll records and default history.

## Sources

| Source and actual scope read | Official URL | Read on |
|---|---|---|
| December 2024 general amendment, approved 17 December/printed 20 December 2024, substantive pages 1–9 | https://www.lra.gov.lr/wp-content/uploads/2025/02/TAX-AMENDMENT-ACT-OF-DECEMBER-2024-AMENDING-THE-LIBERIA-CONSOLIDATED-REVENUE-CODE-AS-AMENDED.pdf | 2026-11-01; read in part, specific scope in first column |
| Revenue Code 2020, selected general, income, nonresident, filing and GST provisions | https://www.lra.gov.lr/wp-content/uploads/2021/08/REVENUE-CODE-LIBERIA-REVENUE-CODE-AMENDEMENT-2020-min.pdf | 2026-11-01; read in part, specific scope in first column |
| LRA Forms and Schedules, named return/schedule links read; not a completed portal filing | https://www.lra.gov.lr/forms-and-schedules/ | 2026-11-01; read in part, specific scope in first column |
| NASSCORP General Regulations 2023, regs 1–4,13–21 and Schedules I–III read | https://www.nasscorp.org.lr/wp-content/uploads/2024/06/GenReg-2023.pdf | 2026-11-01; read in part, specific scope in first column |
| December 2025 amendment, approved 24 March/printed 1 April 2026, cover/preliminary/amended 63,74,76,79,90–92,803,805,806,1000,1021; excise schedule not used | https://www.lra.gov.lr/wp-content/uploads/2026/04/LRC-Amendment-December-2025.pdf | 2026-11-01; read in part, specific scope in first column |
| NASSCORP Act 2017, ss 89.8–89.18, employment categories and contributions read | https://www.nasscorp.org.lr/wp-content/uploads/2024/05/NASSCORP-Act-revised-2017.pdf | 2026-11-01; read in part, specific scope in first column |

Not yet confirmed: Live e-Payroll fields, any separate transmission deadline, accepted transmission and bank references; resolution of Act 89.16(m) versus regulation 16(2) for retrospective deductions; individual expatriate/injury-only status; income-tax deductibility of employee pension and later scheme changes.

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
