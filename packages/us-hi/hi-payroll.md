---
name: hi-payroll
description: "Compute Hawaii 2026 state wage withholding using Booklet A annualized tables and unemployment contributions using the 2026 wage base and employer rate, with registration, payment schedules, HW-14 and UC-B6 filing."
version: "0.1"
jurisdiction: US-HI
category: payroll
tax_year: 2026
last_updated: 2026-11-13

tier: 2
domain: payroll
type: computation
---

# Hawaii payroll withholding and unemployment insurance, tax year 2026

> **General reference only.** Built from the official sources identified below. Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply this material to the taxpayer's actual facts and the law for the relevant period, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of any federal tax implications. Federal computations belong to the linked federal skills.

**Answer first.** Employers must operate two state accounts: DOTAX wage withholding and DLIR unemployment insurance (UI). For 2026 UI, Schedule C applies, taxable wages stop at USD 64,500 per employee, a new employer normally pays 2.4%, and the separate E&T assessment is 0.01%. Use the employer's assigned rate for an experienced account. Withholding is computed from employee HW-4 and the official 2026 Booklet A tables; do not substitute the annual individual income-tax calculation. Sources: [2026 UI rate schedule](https://labor.hawaii.gov/ui/tax-rate-schedule-and-weekly-benefit-amount/); [Booklet A, appendix effective January 1, 2026](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf).

## Scope

Hawaii employers paying covered employee wages, including ordinary resident and Hawaii-workplace payroll. State withholding, UI and the E&T assessment are distinct from federal employment tax. Load `us-form-941-940-payroll` for federal payroll; federal figures are not repeated here. This skill does not compute temporary disability insurance, prepaid health care, workers' compensation or retirement-program obligations, which must be checked separately.

Booklet A is labelled Rev. 2025 but its appendix expressly applies to withholding January 1, 2026 and thereafter. Its reference to Schedule C for UI is unrelated to federal sole-proprietor Schedule C.

## Ask the client first

1. Entity, legal employer, first hire date, employee versus contractor status and any household, agricultural, family or owner exclusions.
2. Each worker's work locations, residence, military-spouse status and any approved HW-6/HW-7 withholding exception.
3. HW-4 marital status and allowances, wages, pay frequency, additional withholding and supplemental payments.
4. Annual state withholding liability, federal deposit frequency, electronic filing obligations and number of wage statements.
5. Each employee's year-to-date covered/UI taxable wages, predecessor wages and assigned 2026 UI rate notice.
6. Registration numbers, prior reports/payments, acquisitions, cessation and any delinquent periods.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 amount and conditions | Official source |
|---|---|---|
| Annual regular withholding allowance | USD 1,144 per HW-4 allowance under annualized method | [Booklet A, appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Annualized extra lump-sum allowance | USD 4,350 under Part 1 method | [Booklet A, appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| UI taxable wage base | USD 64,500 per employee for calendar 2026 | [2026 column](https://labor.hawaii.gov/ui/tax-rate-schedule-and-weekly-benefit-amount/) |
| New-employer UI rate | 2.4% under 2026 Schedule C | [2026 column](https://labor.hawaii.gov/ui/tax-rate-schedule-and-weekly-benefit-amount/) |
| Maximum assigned UI rate | 5.6% under 2026 Schedule C; use actual rate notice | [2026 column](https://labor.hawaii.gov/ui/tax-rate-schedule-and-weekly-benefit-amount/) |
| Minimum experienced UI rate | 0% possible under Schedule C, depending on reserve ratio; reporting still required | [Contribution Rate Schedules and Experience Rating](https://labor.hawaii.gov/ui/test-handbook-for-employers/) |
| E&T assessment | 0.01% of taxable wages in 2026, separate from UI | [2026 column](https://labor.hawaii.gov/ui/tax-rate-schedule-and-weekly-benefit-amount/) |
| Quarterly withholding remittance | Annual state withholding liability no more than USD 5,000, absent semiweekly federal trigger | [Section 3(a)](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Monthly withholding remittance | Annual state withholding liability over USD 5,000 and no more than USD 40,000, absent semiweekly federal trigger | [Section 3(b)](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Semiweekly withholding remittance | Annual state liability over USD 40,000 or federal semiweekly deposit schedule | [Section 3(c)](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Mandatory electronic wage statements from 2026 | At least 10 Forms W-2 and/or HW-2 | [Section 4, 2026 electronic filing change](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |

The following is **withholding** on annualized wages after the Part 1 allowances, not final N-11 tax. Single includes unmarried heads of household in this withholding table. The appendix's final withholding band is 7.9%; do not import the higher individual-return rates from `hi-income-tax`.

| Annualized wages after allowances, single including head of household (USD) | Annual withholding | Official source |
|---|---|---|
| 0 through 9,600 | 1.4% of adjusted wages | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 9,600 through 14,400 | USD 134 + 3.2% of excess over USD 9,600 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 14,400 through 19,200 | USD 288 + 5.5% of excess over USD 14,400 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 19,200 through 24,000 | USD 552 + 6.4% of excess over USD 19,200 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 24,000 through 36,000 | USD 859 + 6.8% of excess over USD 24,000 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 36,000 through 48,000 | USD 1,675 + 7.2% of excess over USD 36,000 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 48,000 through 125,000 | USD 2,539 + 7.6% of excess over USD 48,000 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 125,000 | USD 8,391 + 7.9% of excess over USD 125,000 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |

| Annualized wages after allowances, married (USD) | Annual withholding | Official source |
|---|---|---|
| 0 through 19,200 | 1.4% of adjusted wages | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 19,200 through 28,800 | USD 269 + 3.2% of excess over USD 19,200 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 28,800 through 38,400 | USD 576 + 5.5% of excess over USD 28,800 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 38,400 through 48,000 | USD 1,104 + 6.4% of excess over USD 38,400 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 48,000 through 72,000 | USD 1,718 + 6.8% of excess over USD 48,000 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 72,000 through 96,000 | USD 3,350 + 7.2% of excess over USD 72,000 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 96,000 through 250,000 | USD 5,078 + 7.6% of excess over USD 96,000 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |
| Over 250,000 | USD 16,782 + 7.9% of excess over USD 250,000 | [Appendix Part 1, page 20](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf) |

1. Register withholding through **Hawaii Tax Online**, https://hitax.hawaii.gov/, using **BB-1**; retain the employer withholding tax ID. Obtain each employee's **HW-4** and determine covered wages before calculating. Ordinary Hawaii services are subject to withholding, and certain out-of-state services remain covered where the employee's regular place of employment is Hawaii or wages are paid from the specified Hawaii office. Exceptions require their actual conditions and documentation. Source: [Sections 5 to 13](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf).
2. Choose one official method: appendix Part 1 annualized computation, Part 2 period-specific formulas, or Part 3 wage tables. For Part 1 multiply period wages by periods per year, subtract HW-4 allowances times USD 1,144 and the USD 4,350 extra allowance, floor at zero, apply the correct annual withholding schedule above, then divide by periods per year. Add any valid employee additional withholding. Separate bonuses/supplemental wages require section 15 treatment; do not apply the ordinary example blindly. Source: [Section 15 and appendix Parts 1 to 3](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf).
3. Register UI independently at **https://uiclaims.hawaii.gov/**. An owner/officer creates an online profile and completes **UC-1**; paper forms and future hire dates are not accepted. The handbook requires the status report within 20 days after hiring. UI account issuance follows the coverage determination. Source: [Employer FAQ, registration](https://labor.hawaii.gov/ui/906-2/); [Registration](https://labor.hawaii.gov/ui/test-handbook-for-employers/).
4. Test UI coverage. Ordinary employees generally enter the wage report. Sole-proprietor draws and wages paid to the proprietor's spouse, parents or children under 21 are excluded; the FAQ extends the same exclusions to a disregarded single-member LLC. Corporate ownership is not automatically exempt: the limited family-corporation exclusion requires an application and qualifying ownership. Agricultural, household, nonprofit and other statutory exclusions require separate review. Source: [family exclusions and family-owned corporation](https://labor.hawaii.gov/ui/906-2/).
5. For each covered employee compute current-quarter taxable wages as the smaller of covered wages paid this quarter and remaining USD 64,500 annual base, not below zero. Report total covered wages even after the base is exhausted. Approved predecessor and out-of-state wage treatment can affect the remaining base; do not restart it mechanically after a transfer. Multiply taxable wages by the employer's assigned rate, or new-employer 2.4% where applicable; add taxable wages times 0.01% for E&T. These are employer costs, not employee deductions. Sources: [2026 rate schedule](https://labor.hawaii.gov/ui/tax-rate-schedule-and-weekly-benefit-amount/); [Taxable Wages and quarterly contributions](https://labor.hawaii.gov/ui/test-handbook-for-employers/).
6. Reconcile the two state accounts independently to payroll records. Annual withholding is a payment on the employee's income-tax return; UI/E&T is not personal income-tax withholding. Maintain total wages, taxable wages, excess wages, employer rate and payment references.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Annual withholding exactly USD 5,000 | Booklet A section 3 says quarterly; exactly USD 40,000 is monthly, subject to federal semiweekly trigger |
| Brief nonresident assignment | Booklet A section 11(a) has multiple conditions including no more than 60 Hawaii days and an out-of-state pay office/regular workplace; construction-contractor employees are excluded from that exception |
| Military spouse | Test actual residence/election and qualifying facts; retain HW-4/HW-6 evidence and current military relief law |
| Withholding exemption | Does not itself establish exemption from final Hawaii income tax |
| Employee exceeds UI base mid-quarter | Only remaining base is taxable; all covered wages are still reported |
| Experienced employer or business acquisition | Use rate notice and predecessor/base rules; do not default to new-employer rate |
| No wages in quarter or UI rate 0% | UC-B6 reporting remains required |
| Worker labelled contractor | Review actual control and business facts before excluding from payroll |

## Worked cases

**Case 1: ordinary weekly withholding.** Invented single employee, one job, USD 500 weekly wages, three valid HW-4 allowances, no additional withholding. Annual wages USD 26,000, less USD 3,432 regular allowances and USD 4,350 extra allowance = USD 18,218. Annual withholding USD 288 + 5.5% x USD 3,818 = USD 497.99. Divide by 52: USD 9.5767, or USD 9.58 weekly. These figures follow appendix Part 1 rather than the final-return standard deduction.

```oa-check
name: Hawaii 2026 weekly annualized withholding
inputs:
  weekly: 500
  allowances: 3
steps:
  - annual_wages: weekly * 52
  - adjusted: max(annual_wages - allowances * 1144 - 4350, 0)
  - annual_tax: 288 + (adjusted - 14400) * 0.055
  - weekly_tax: annual_tax / 52
expected:
  annual_wages: 26000
  adjusted: 18218
  annual_tax: 497.99
  weekly_tax: 9.5767307692
```

**Case 2: annual UI base crossed.** Invented new employer pays USD 20,000 this quarter to an employee with USD 60,000 prior covered taxable wages in 2026. Remaining base USD 4,500: UI USD 108 and E&T USD 0.45, total USD 108.45. Applying the rates to all quarter wages instead would produce USD 482, an overpayment of USD 373.55. Report the full USD 20,000 wages with USD 15,500 excess wages.

```oa-check
name: Hawaii 2026 UI wage base crossing
inputs:
  prior: 60000
  wages: 20000
steps:
  - taxable: min(wages, max(64500 - prior, 0))
  - excess: wages - taxable
  - ui: taxable * 0.024
  - et: taxable * 0.0001
  - total: ui + et
  - overpayment: wages * 0.0241 - total
expected:
  taxable: 4500
  excess: 15500
  ui: 108
  et: 0.45
  total: 108.45
  overpayment: 373.55
```

## When to refuse or refer

Refer worker classification disputes, supplemental-pay special cases, military residence conflicts, multi-state UI localization, successor-rate elections and special industry exclusions. Verify TDI, health coverage and workers' compensation with the responsible Hawaii program separately. No employer may manipulate workforce transfers to evade UI rates.

## Filing and payment

**Withholding:** In Hawaii Tax Online choose the withholding account, quarter and **HW-14**, enter total wages/tax withheld, reconcile payments and balance, submit and retain acceptance/payment references. HW-14 is quarterly, due 15 April, 15 July, 15 October and 15 January following the quarter. Deposit frequency is separate: quarterly/monthly payments are due the fifteenth of the next relevant month; semiweekly deposits are due Wednesday for preceding Wednesday-Friday payroll, Friday for preceding Saturday-Tuesday payroll, subject to the banking-day rules. Sources: [Sections 2 to 4 and 16](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf).

Give employees **HW-2 or applicable W-2 by 31 January** following the year and transmit the state wage statements by that date under Booklet A. Paper statements use **HW-30**; electronic EFW-2 upload uses no HW-30. **HW-3 is obsolete**, despite a stale DOTAX employee FAQ referring to it. At least 10 statements require electronic filing from 2026. Save the transmission acknowledgement. Source: [Sections 2, 4, 17 and 18](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf).

**UI:** On the employer UI portal select **Employer Reporting**, quarter and **UC-B6**, with UC-B6A continuation where applicable. Enter employee wage records, total/excess/taxable wages, covered-worker counts for each month's pay period including the twelfth, assigned contribution rate, UI and E&T assessment. Review and submit, pay and save the confirmation. UC-B6 and payment are due by the last day of the month after quarter end: 30 April, 31 July, 31 October and 31 January, with applicable nonbusiness-day relief. Zero-wage quarters still require a report. Sources: [Employer FAQ, quarterly reporting](https://labor.hawaii.gov/ui/906-2/); [Quarterly Wage, Contribution and E&T Assessment Report](https://labor.hawaii.gov/ui/test-handbook-for-employers/).

The UI handbook states late contributions incur 10%, minimum USD 100; unpaid contributions and penalty accrue two-thirds of 1% interest per month or part when unpaid within 15 days after due date. Late UC-B6 incurs USD 30 and may cause maximum-rate assessment. Withholding late-return/payment penalties and interest are described in Booklet A; identify the specific failure before calculating. Source: [Penalties](https://labor.hawaii.gov/ui/test-handbook-for-employers/); [Section 19](https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf).

## Completion checklist

- Both state registrations established; employee coverage and HW-4 documented.
- 2026 withholding appendix used; deposits separated from quarterly return frequency.
- Assigned UI rate and USD 64,500 base applied employee by employee; E&T added separately.
- HW-14, wage-statement upload and UC-B6 acknowledgements retained with payment confirmations.

## Sources

| Source and scope actually read | URL | Read on |
|---|---|---|
| DOTAX Booklet A Rev. 2025, effective for 2026 withholding. Read sections 2 to 7, 10 to 19, appendix heading and Part 1 page 20 formulas and example; Part 2/3 structure checked for method alternatives. | https://files.hawaii.gov/tax/news/pubs/25BkltA.pdf | 2026-11-13 |
| DLIR Tax Rate Schedule and Weekly Benefit Amount. Read complete 2026 column for Schedule C, USD 64,500, 2.4%, 5.6% and 0.01%. | https://labor.hawaii.gov/ui/tax-rate-schedule-and-weekly-benefit-amount/ | 2026-11-13 |
| DLIR Employer FAQ. Read account registration, owner/family exclusions, quarterly filing and predecessor/family-corporation questions. | https://labor.hawaii.gov/ui/906-2/ | 2026-11-13 |
| DLIR Handbook for Employers. Read registration, coverage, quarterly reporting, taxable wages, penalties, contribution schedules and experience rating sections. | https://labor.hawaii.gov/ui/test-handbook-for-employers/ | 2026-11-13 |

Not yet confirmed: account-specific 2026 experienced UI rate (obtain the rate notice); employee-specific multi-state localization and current military-spouse elections; 2026 temporary disability, prepaid health-care and workers compensation amounts, which are separate program obligations and are not replaced by UI. No unsupported dollar figures for these programs are supplied.
