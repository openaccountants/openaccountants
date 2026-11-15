---
name: nepal-payroll
description: Use this skill whenever asked about Nepal payroll processing for employed persons. Trigger on phrases like "Nepal payroll", "PAYE Nepal", "TDS on salary Nepal", "eTDS Nepal", "salary tax Nepal", "SSF contribution", "Social Security Fund Nepal", "provident fund Nepal", "gratuity Nepal", "CIT Nepal", "EPF Nepal", "net pay Nepal", "salary calculation Nepal", "NPR payroll", "Nepalese Rupee payroll", "minimum wage Nepal", "PAN Nepal", "D-01 D-03 Nepal", "female tax credit Nepal", "remote area allowance", "married couple tax Nepal", or any question about computing employee pay, salary withholding, or social security contributions for Nepal-based employees. This skill covers monthly TDS/PAYE salary withholding on progressive resident slabs (single and married-couple), the 1% first-band Social Security Tax and its SSF interaction, retirement-fund and insurance deductions, the female tax credit, the 31% Social Security Fund contribution (20% employer / 11% employee), provident fund and gratuity for non-SSF employers, the minimum wage, filing forms (eTDS, D-01/D-02/D-03) and penalties. Nepal DOES levy a personal income tax (progressive PAYE). ALWAYS read this skill before processing any Nepal payroll.
jurisdiction: NP
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
version: 1.0
type: computation
tax_year_notes: "Calendar 2026 includes FY 2082/83 (2025/26) and FY 2083/84 (2026/27); apply the labelled period."
---

# Nepal payroll: salary withholding and social security

## Scope

Prepare salary withholding, employee deductions, employer contributions and a payroll working paper for Nepal employment. This source-cited draft has no accountant approval. It covers ordinary formal-sector payroll; establish coverage before applying it to a public-sector, informal/self-employed, expatriate or special-scheme worker.

Calendar 2026 spans FY 2082/83 (2025/26) and FY 2083/84 (2026/27). The personal tax scale changes from **Shrawan 1, 2083**. The current and historical scales and all personal deduction/credit limits have one home in `nepal-income-tax`; load that skill before computing salary tax. Both ordinary remittance deadlines below are established from primary legislation, independently of the old secondary-source research notes.

## Ask the client first

- Nepali payroll month and income year; year-to-date pay/tax and the remaining pay/bonus projection.
- Each employee's residence under abode, rolling presence and government-posting tests; spouse/election information for the relevant year and treaty evidence where needed.
- Actual employer/employee SSF registration and contribution history, applicable employment scheme and verified basic pay separated from allowances/dearness/overtime.
- Gross cash remuneration, taxable benefits, employer retirement contributions, reimbursed costs, deductions, absences and other employers/income.
- Approved retirement statements, eligible insurance/remote/pension/disability evidence, and remuneration-only female-credit eligibility.
- PAN, prior eTDS/SSF acknowledgements and payments, annual-return position, and any payroll/SSF/wage notice applying to this employer.

No unknown scheme, residence or deduction is resolved by a higher assumed tax rate. A missing couple election cannot justify historical couple bands; a common current scale does not eliminate the election facts.

## The method, step by step

### 1. Establish the salary-tax base

A resident's assessable employment includes wages/salary, leave/overtime, commissions, bonus, allowances including dearness, benefits and employer retirement contributions, subject to statutory exclusions. A net bank credit is not the gross base. Genuine employer-business reimbursements and the specific common workplace-meal exclusions must be identified under section 8, not inferred from a narration. [Income Tax Act §8(1)-(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=20); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=21).

Reconcile annual assessable remuneration and eligible deductions to `nepal-income-tax`. That skill owns residence (including the continuous-period day test), both year scales, first-band exceptions, approved retirement cap, life/health/building insurance limits, remote areas, pension/disability additional deductions, diplomatic foreign allowances and female/medical credits. Do not treat all SSF remittances as an approved retirement deduction or deduct employer contributions without checking their inclusion and qualifying component.

### 2. Compute annual tax, then periodic withholding

Use the correct year's marginal slices on annual taxable income, apply the statutory first-band exception only when established, then eligible tax credits. The first-band remuneration-based tax paid to IRD is different from the SSF employee contribution. The public IRD FAQ identifies revenue code 11211 for that remuneration-based tax; confirm the actual portal code/current category before posting a payment. It is not an SSF fund account. [§87](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=107); [IRD FAQ: code 11211](https://ird.gov.np/faq/?gid=97).

Income Tax Rule 31 requires monthly apportionment of tax on annual remuneration and allows the section 51 medical credit. For an unchanged full-year projection, annual tax / 12 is the simple illustration; for starters/leavers, changes, bonuses or prior under/over-withholding, reconcile the projected annual liability with tax already withheld and remaining payments. Do not apply a monthly fragment of the annual threshold independently without annual reconciliation. [Rule 31](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AF%20(%E0%A4%B8%E0%A5%8B%E0%A4%B9%E0%A5%8D%E0%A4%B0%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7kddd2d.pdf#page=12).

Registered sole-proprietor/pension cases and actual SSF/pension contributors have the statutory first-band exception described in `nepal-income-tax`; those categories do not all describe ordinary employees. Non-resident employment taxable income has the separate flat rule in that skill, subject to source/treaty review. Female credit needs resident remuneration-only eligibility; never apply resident-only credits automatically to a non-resident.

### 3. Calculate SSF on verified basic remuneration

| Ordinary covered formal-sector item | Rate/base and timing | Official provision |
|---|---|---|
| Employee cash deduction | 11% of basic remuneration | [Operation Procedure §25](https://www.ssf.gov.np/images/news/17406520344566_Social%20Security%20Operation%20Procedure%202075%20with%205th%20ammendment.pdf#page=17) |
| Employer added contribution | 20% of basic remuneration, in addition to employee gross pay | [Operation Procedure §25](https://www.ssf.gov.np/images/news/17406520344566_Social%20Security%20Operation%20Procedure%202075%20with%205th%20ammendment.pdf#page=17) |
| Total remittance | 31% of basic remuneration, derived reconciliation 11% + 20% | [Operation Procedure §25](https://www.ssf.gov.np/images/news/17406520344566_Social%20Security%20Operation%20Procedure%202075%20with%205th%20ammendment.pdf#page=17) |
| Health, medical treatment and maternity allocation | 1.20% of basic remuneration | [§25(क)](https://www.ssf.gov.np/images/news/17406520344566_Social%20Security%20Operation%20Procedure%202075%20with%205th%20ammendment.pdf#page=17) |
| Accident and disability allocation | 0.80% of basic remuneration | [§25(ख)](https://www.ssf.gov.np/images/news/17406520344566_Social%20Security%20Operation%20Procedure%202075%20with%205th%20ammendment.pdf#page=17) |
| Dependent-family allocation | 0.67% of basic remuneration | [§25(ग)](https://www.ssf.gov.np/images/news/17406520344566_Social%20Security%20Operation%20Procedure%202075%20with%205th%20ammendment.pdf#page=17) |
| Old-age allocation | 28.33% of basic remuneration; scheme conditions govern pension/retirement benefits | [§25(घ)](https://www.ssf.gov.np/images/news/17406520344566_Social%20Security%20Operation%20Procedure%202075%20with%205th%20ammendment.pdf#page=17) |
| SSF contribution deposit | Within 25 days after the month in which contributory income is payable ends | [SSF Act §4(3)-(4), as amended in 2082](https://www.ssf.gov.np/images/news/17655918798529_%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%A6%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A4%BE%20%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%A4%20%E0%A4%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AD%E0%A5%AA.pdf#page=4) |
| New employee listing by a covered listed employer | Within 3 months after the employment relationship starts, not 3 months after the employer's listing | [SSF Act §20(1)](https://www.ssf.gov.np/images/news/17655918798529_%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%A6%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A4%BE%20%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%A4%20%E0%A4%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AD%E0%A5%AA.pdf#page=11) |

The four allocation rates total 31%, derived. They allocate the **combined** fund contribution; do not deduct an allocation separately from pay or identify the employee's extra percentage as a second IRD tax. The fifth-amendment procedure's page 17 was rendered and read visually because its embedded legacy font does not extract correctly. These allocation rates resolve the old conflicting medical/old-age summaries.

The statutory base says **basic remuneration**, not "basic plus dearness". Keep the employment-contract/payroll breakdown and the applicable wage notice. The income-tax base includes taxable allowances; that does not make those allowances the SSF base. Reject an artificial pay structure unsupported by the contract/wage law. The alleged monthly SSF cap is not confirmed and must not reduce the remittance.

SSF Act section 19 ties employer listing to the notified scope of industry/service/business. For covered private-sector employment there is no small-employer exemption established in these provisions: do not skip registration merely because there is only 1 employee. Establish the notification and special-scheme status for a live employer, rather than asserting every worker in every sector or every foreign employee is covered identically. Informal/self-employed workers and overseas workers have separate sections 5/5A. [§§19-20](https://www.ssf.gov.np/images/news/17655918798529_%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%A6%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A4%BE%20%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%A4%20%E0%A4%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AD%E0%A5%AA.pdf#page=11); [§§5-5A](https://www.ssf.gov.np/images/news/17655918798529_%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%A6%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A4%BE%20%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%A4%20%E0%A4%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AD%E0%A5%AA.pdf#page=5).

### 4. Provident fund and gratuity where the alternative statutory route applies

| Item | Employee | Employer | Official source |
|---|---|---|---|
| Provident fund under Labour Act §52 | 10% of basic | Matching 10% of basic | [Labour Act §52](https://labourcourt.gov.np/assets/uploads/ea43b3437b12a2cb4a51a4cd154c428c.pdf#page=22) (in words on the page) |
| Gratuity under Labour Act §53 | No employee contribution specified here | 8.33% of basic each month | [Labour Act §53(1)](https://labourcourt.gov.np/assets/uploads/ea43b3437b12a2cb4a51a4cd154c428c.pdf#page=22); [§53 continuation](https://labourcourt.gov.np/assets/uploads/ea43b3437b12a2cb4a51a4cd154c428c.pdf#page=23) (in words on the page) |

These are not voluntary substitutes for a covered employer's SSF duty. Sections 52-53 address deposit into SSF, specified circumstances before SSF operation/applicability, transfer of existing balances and the stated fallback where deposit cannot be made. Start-date and scheme conditions govern; an EPF/CIT bank narration alone does not prove exemption. Do not charge provident fund and gratuity a second time when already included in the applicable SSF arrangement. For context, the procedure's old-age allocation consolidates the retirement components; the combined SSF cash deduction remains the aggregate contribution above.

### 5. Check minimum remuneration independently

The read Gazette notices commence **Shrawan 1, 2082** and remain the sourced wage schedules used here in calendar 2026. The ordinary notice excludes tea estates, which have their own notice. These are statutory minima; contractual benefits, provident fund/gratuity and other required entitlements are additional, and an agreement cannot undercut the applicable minimum. Do not equate an income-tax deduction with permission to pay below the wage floor.

| Worker/rate | Basic + dearness = total NPR | Official Gazette |
|---|---|---|
| Ordinary monthly, excluding tea estates | 12,170 + 7,380 = 19,550 | [Ordinary notice, rate table](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B8%E0%A4%BE%E0%A4%89%E0%A4%A8%20%E0%A5%A7_250826_112619_eudzntr_5f2rztd.pdf#page=1) |
| Ordinary daily | 470 + 284 = 754; the seed's 469 + 285 components were wrong | [Ordinary notice, rate table](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B8%E0%A4%BE%E0%A4%89%E0%A4%A8%20%E0%A5%A7_250826_112619_eudzntr_5f2rztd.pdf#page=1) |
| Ordinary hourly | 63 + 38 = 101 | [Ordinary notice, rate table](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B8%E0%A4%BE%E0%A4%89%E0%A4%A8%20%E0%A5%A7_250826_112619_eudzntr_5f2rztd.pdf#page=1) |
| Ordinary part-time hourly | 107 total | [Ordinary notice, rate table](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B8%E0%A4%BE%E0%A4%89%E0%A4%A8%20%E0%A5%A7_250826_112619_eudzntr_5f2rztd.pdf#page=1) |
| Tea-estate monthly | 10,096 + 5,603 = 15,699; do not use the seed's older 13,893 | [Tea notice, rate table](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2%20%E0%A4%B0%E0%A4%BE%E0%A4%9C%E0%A4%AA%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BE%20%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%95%E0%A4%BE%E0%A4%B6%E0%A4%BF%E0%A4%A4%20%E0%A4%9A%E0%A4%BF%E0%A4%AF%E0%A4%BE%20%E0%A4%AC%E0%A4%97%E0%A4%BE%E0%A4%A8%E0%A4%95%E0%A4%BE%20%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%95%E0%A4%BE%20%E0%A4%B2%E0%A4%BE%E0%A4%97%E0%A4%BF%20%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%82%E0%A4%9A%E0%A4%A8%E0%A4%BE_blfvfy6.pdf#page=2) |
| Tea-estate daily/hourly | Daily 362 + 203 = 565; hourly 45 + 25 = 70 | [Tea notice, rate table](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2%20%E0%A4%B0%E0%A4%BE%E0%A4%9C%E0%A4%AA%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BE%20%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%95%E0%A4%BE%E0%A4%B6%E0%A4%BF%E0%A4%A4%20%E0%A4%9A%E0%A4%BF%E0%A4%AF%E0%A4%BE%20%E0%A4%AC%E0%A4%97%E0%A4%BE%E0%A4%A8%E0%A4%95%E0%A4%BE%20%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%95%E0%A4%BE%20%E0%A4%B2%E0%A4%BE%E0%A4%97%E0%A4%BF%20%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%82%E0%A4%9A%E0%A4%A8%E0%A4%BE_blfvfy6.pdf#page=2) |
| Tea-processing/factory workers and the listed tea-estate supervisory/watch roles | Additional daily allowance NPR 70 under the specific notice row | [Tea notice, row 4](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2%20%E0%A4%B0%E0%A4%BE%E0%A4%9C%E0%A4%AA%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BE%20%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%95%E0%A4%BE%E0%A4%B6%E0%A4%BF%E0%A4%A4%20%E0%A4%9A%E0%A4%BF%E0%A4%AF%E0%A4%BE%20%E0%A4%AC%E0%A4%97%E0%A4%BE%E0%A4%A8%E0%A4%95%E0%A4%BE%20%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%95%E0%A4%BE%20%E0%A4%B2%E0%A4%BE%E0%A4%97%E0%A4%BF%20%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%82%E0%A4%9A%E0%A4%A8%E0%A4%BE_blfvfy6.pdf#page=2) |

The ordinary notice requires statutory benefits in addition to minimum pay and replaces the earlier ordinary-wage notice; the tea notice similarly replaces its earlier tea schedule. Both Gazette tables and neighboring conditions were visually read. [conditions](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B8%E0%A4%BE%E0%A4%89%E0%A4%A8%20%E0%A5%A7_250826_112619_eudzntr_5f2rztd.pdf#page=2); [conditions](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2%20%E0%A4%B0%E0%A4%BE%E0%A4%9C%E0%A4%AA%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BE%20%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%95%E0%A4%BE%E0%A4%B6%E0%A4%BF%E0%A4%A4%20%E0%A4%9A%E0%A4%BF%E0%A4%AF%E0%A4%BE%20%E0%A4%AC%E0%A4%97%E0%A4%BE%E0%A4%A8%E0%A4%95%E0%A4%BE%20%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%95%E0%A4%BE%20%E0%A4%B2%E0%A4%BE%E0%A4%97%E0%A4%BF%20%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%82%E0%A4%9A%E0%A4%A8%E0%A4%BE_blfvfy6.pdf#page=2); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2%20%E0%A4%B0%E0%A4%BE%E0%A4%9C%E0%A4%AA%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BE%20%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%95%E0%A4%BE%E0%A4%B6%E0%A4%BF%E0%A4%A4%20%E0%A4%9A%E0%A4%BF%E0%A4%AF%E0%A4%BE%20%E0%A4%AC%E0%A4%97%E0%A4%BE%E0%A4%A8%E0%A4%95%E0%A4%BE%20%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%95%E0%A4%BE%20%E0%A4%B2%E0%A4%BE%E0%A4%97%E0%A4%BF%20%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%82%E0%A4%9A%E0%A4%A8%E0%A4%BE_blfvfy6.pdf#page=3).

### 6. Prepare cash pay and employer cost

Net pay = cash gross - salary tax withheld - employee SSF (or the applicable employee fund deduction) - other authorised deductions. Employer cost = cash gross + employer contributions + any other employer-paid benefits/costs. Keep taxable non-cash benefits and employer retirement contributions in the annual tax-base reconciliation without counting them as cash salary a second time. Payroll instructions to a bank require the fully reconciled period, not only an annual-tax illustration.

### 7. Preserve the payment pattern and terminology catalogue

Bank narration is an intake cue, not proof of contribution status, tax paid, or gross assessable income. Reconcile to payslips, employment records and actual authority acknowledgements.

#### Salary credits (to the employee)

**Salary credits table**

| Pattern on statement | Nepali term | Classification |
| --- | --- | --- |
| TALAB, SALARY, PAYROLL | तलब (talab = salary) | Salary cash receipt; reconstruct gross from payslip |
| EMPLOYER [name] TRANSFER, WAGES | -- | Salary cash receipt; reconstruct gross from payslip |
| BONUS, BHATTA | बोनस / भत्ता (bhatta = allowance) | Bonus / allowance (taxable, in TDS base) |
| OT, OVERTIME, ADHIK SAMAYA | अधिक समय | Overtime pay |
| MAHANGI BHATTA | महंगी भत्ता | Dearness allowance |

#### Employer debits (to the authorities)

**Employer debits table**

| Pattern on statement | Classification |
| --- | --- |
| IRD, TDS, eTDS, AYAKAR | TDS / income-tax remittance to IRD (due within 25 days) |
| SSF, SAMAJIK SURAKSHYA KOSH | SSF contribution remittance (due within 25 days) |
| EPF, PROVIDENT FUND, SANCHAYA KOSH | Provident fund remittance; establish the scheme, not an automatic SSF exemption |
| CIT, NAGARIK LAGANI KOSH | Citizen Investment Trust remittance |
| NET WAGES, SALARY RUN, PAYROLL | Net salary disbursement to employees |

"AYAKAR" (आयकर) means income tax; "SAMAJIK SURAKSHYA" means social security. Any IRD debit referencing salary tax = monthly TDS remittance.


**Terminology guide**

| Term (Nepali / romanised) | Meaning |
| --- | --- |
| तलब (talab) | Salary |
| भत्ता (bhatta) | Allowance |
| महंगी भत्ता (mahangi bhatta) | Dearness allowance |
| बोनस (bonus) | Bonus |
| अधिक समय (adhik samaya) | Overtime |
| आयकर (ayakar) | Income tax (TDS) |
| सामाजिक सुरक्षा कोष (samajik surakshya kosh) | Social Security Fund (SSF) |
| सञ्चय कोष (sanchaya kosh) | Provident Fund (EPF) |
| नागरिक लगानी कोष (nagarik lagani kosh) | Citizen Investment Trust (CIT) |
| स्थायी लेखा नम्बर (PAN) | Permanent Account Number |


## Boundary and exception table

| Situation retained from the original refusal/judgement catalogue | Action |
|---|---|
| Unknown abode/presence or expatriate residence | Hold final tax; use all residence tests, source and treaty facts. |
| Unknown single/couple election | Do not use historical couple bands; current common scale does not settle election/reporting. |
| Unconfirmed SSF contributions/registration | Hold the first-band exception and scheme calculation until evidenced; do not invent a final payroll result. |
| Female credit requested without remuneration-only evidence | Hold; mixed business/investment income may defeat the condition. |
| Unsupported deduction or amount above cap | Exclude unsupported amounts from a final claim; apply verified caps to eligible costs only. |
| Alleged SSF ceiling or arbitrary basic/dearness split | No cap or invented base; obtain the actual legal/payroll evidence. |
| Small employer requests no SSF | Establish covered status and enforce it; small size is not an established exemption. |
| Per-scheme rate proposed as a cash deduction | Do not replace the statutory employee/employer aggregate; allocations are fund distribution. |
| Remote-area, pension or disability claim | Establish category, evidence and current-period quantum through `nepal-income-tax`. |
| EPF/CIT/pension fund | Verify approved retirement status and applicable employment scheme, not merely the acronym. |
| Treaty or special non-resident business | Refer before treating it as ordinary salary. |
| Arrears/penalties, scheme dispute or benefit claim | Reconcile the authority account and refer legal/actuarial eligibility; no automatic waiver. |

## Worked cases

Amounts are hypothetical inputs. Cases A-F and regression topics remain **FY 2082/83 historical examples**, so their earlier bands must not be reused for FY 2083/84. Annual taxable-income inputs are assumed already correctly determined after allowable deductions. Monthly annual-tax / 12 illustrations assume a stable full-year projection and require rounding/year-to-date reconciliation.

### A. Single SSF contributor, annual taxable NPR 800,000

Historical tax: first band excluded; NPR 200,000 × 10% + NPR 100,000 × 20% = NPR 40,000; monthly NPR 3,333.33, derived.

```oa-check
name: Historical A single SSF salary
inputs:
  taxable: 800000
steps:
  - annual: min(max(taxable - 500000, 0), 200000) * 0.10 + max(taxable - 700000, 0) * 0.20
  - monthly: annual / 12
expected:
  annual: 40000
  monthly: 3333.33
```

### B. Same historical income without a first-band exception

NPR 5,000 employment first-band tax + NPR 20,000 + NPR 20,000 = NPR 45,000; monthly NPR 3,750. The difference from A is NPR 5,000. Non-registration is not assumed lawful or proof of all other payroll facts.

```oa-check
name: Historical B ordinary employment
inputs:
  first: 500000
  second: 200000
  third_used: 100000
steps:
  - annual: first * 0.01 + second * 0.10 + third_used * 0.20
  - monthly: annual / 12
  - difference: annual - 40000
expected:
  annual: 45000
  monthly: 3750
  difference: 5000
```

### C. Electing couple with SSF exception, annual taxable NPR 1,500,000

Historical tax: NPR 200,000 × 10% + NPR 300,000 × 20% + NPR 400,000 × 30% = NPR 200,000; monthly NPR 16,666.67, derived.

```oa-check
name: Historical C electing couple SSF salary
inputs:
  taxable: 1500000
steps:
  - annual: 200000 * 0.10 + 300000 * 0.20 + (taxable - 1100000) * 0.30
  - monthly: annual / 12
expected:
  annual: 200000
  monthly: 16666.67
```

### D. Eligible resident woman, remuneration only and SSF, annual taxable NPR 1,000,000

Historical pre-credit tax NPR 80,000, eligible credit NPR 8,000, annual tax NPR 72,000 and monthly NPR 6,000. Confirm eligibility independently; the example is not a credit for every woman or mixed-income taxpayer.

```oa-check
name: Historical D remuneration-only female credit
inputs:
  taxable: 1000000
steps:
  - before: 200000 * 0.10 + (taxable - 700000) * 0.20
  - credit: before * 0.10
  - annual: before - credit
  - monthly: annual / 12
expected:
  before: 80000
  credit: 8000
  annual: 72000
  monthly: 6000
```

### E. Basic pay NPR 40,000, cash gross NPR 60,000

Use verified **basic** NPR 40,000, excluding separately identified dearness/other allowances from that SSF base. Employee SSF NPR 4,400, employer SSF NPR 8,000, total NPR 12,400, employer cash cost before other benefits NPR 68,000. Cash remaining before salary tax is NPR 55,600.

The seed combined these monthly figures with annual taxable NPR 800,000 without reconciling the annual base. NPR 60,000 × 12 cash pay is NPR 720,000, so it does not by itself establish that annual taxable amount. Only if a **separately evidenced annual projection**, including employer contributions, additional remuneration/benefits and deductions, establishes historical taxable NPR 800,000 can A's monthly NPR 3,333.33 tax and net cash NPR 52,266.67 be used. Otherwise hold final salary tax/net pay. Do not invent a bonus to reconcile the gap or infer an SSF cap from the pay level.

```oa-check
name: Historical E SSF and conditional net cash
inputs:
  basic: 40000
  cash_gross: 60000
  verified_historical_annual_tax: 40000
steps:
  - employee_ssf: basic * 0.11
  - employer_ssf: basic * 0.20
  - total_ssf: employee_ssf + employer_ssf
  - before_tax: cash_gross - employee_ssf
  - conditional_net: before_tax - verified_historical_annual_tax / 12
  - employer_cost: cash_gross + employer_ssf
  - annual_cash: cash_gross * 12
expected:
  employee_ssf: 4400
  employer_ssf: 8000
  total_ssf: 12400
  before_tax: 55600
  conditional_net: 52266.67
  employer_cost: 68000
  annual_cash: 720000
```

### F. Non-resident Nepal-source employment taxable NPR 1,200,000

Subject to source/treaty review, ordinary tax is NPR 300,000 and monthly illustration NPR 25,000. Residence for tax is not itself the SSF-coverage test. The original basic NPR 40,000 example gives employee NPR 4,400/employer NPR 8,000 only if the actual worker is covered by that SSF scheme; do not assert every foreign worker is covered identically.

```oa-check
name: F ordinary non-resident employment
inputs:
  taxable: 1200000
steps:
  - annual: taxable * 0.25
  - monthly: annual / 12
expected:
  annual: 300000
  monthly: 25000
```

### Current-year decision: same taxable salary, different first-band eligibility

For FY 2083/84 annual taxable remuneration NPR 1,600,000: ordinary first-band charge NPR 10,000 + NPR 50,000 + NPR 20,000 = NPR 80,000, monthly NPR 6,666.67. With the evidenced SSF exception, annual tax NPR 70,000, monthly NPR 5,833.33. These are annual taxable-income inputs after the base reconciliation, not gross salary. The current couple scale is the same.

```oa-check
name: Current 2083-84 ordinary versus SSF exception
inputs:
  taxable: 1600000
steps:
  - ordinary: 1000000 * 0.01 + 500000 * 0.10 + (taxable - 1500000) * 0.20
  - ssf: 500000 * 0.10 + (taxable - 1500000) * 0.20
  - ordinary_monthly: ordinary / 12
  - ssf_monthly: ssf / 12
expected:
  ordinary: 80000
  ssf: 70000
  ordinary_monthly: 6666.67
  ssf_monthly: 5833.33
```

### Remaining original regression checks

Original tests 1-4 are A-D above; test 7 is E, test 8 is F and test 9 is the contribution split. Retain historical ordinary single tax at NPR 2,000,000 = NPR 385,000, historical ordinary couple tax there = NPR 356,000, and ordinary minimum monthly remuneration NPR 19,550 = NPR 12,170 basic + NPR 7,380 dearness. The new allocation reconciliation checks that fund schemes sum to the aggregate; it does not add a second payroll deduction.

```oa-check
name: Historical boundary, scheme and wage regressions
inputs:
  basic_wage: 12170
  dearness: 7380
steps:
  - single_two_million: 500000 * 0.01 + 200000 * 0.10 + 300000 * 0.20 + 1000000 * 0.30
  - couple_two_million: 600000 * 0.01 + 200000 * 0.10 + 300000 * 0.20 + 900000 * 0.30
  - scheme_total: 1.20 + 0.80 + 0.67 + 28.33
  - aggregate: 20 + 11
  - minimum_monthly: basic_wage + dearness
expected:
  single_two_million: 385000
  couple_two_million: 356000
  scheme_total: 31
  aggregate: 31
  minimum_monthly: 19550
```

## When to refuse or refer

Apply the boundary table before a final payroll run. Never skip an employer contribution, add the employer share as an employee deduction, use an unconfirmed cap, substitute scheme allocations for cash rates, or treat unknown registration as lawful exemption. No unsupported allowance or credit belongs in a final return. Label work estimated and route to a qualified Nepal practitioner before implementation.

The former non-resident shipping/air/telecom and foreign-PE-remittance rows concern separate businesses, not salary. For no-loss routing: Income Tax Act §70 and Schedule 1 §2(7) set the special **5%** transport/communications base with a **2%** domestic/non-departing exception; §68 and Schedule 1 §2(6) set **5%** on foreign-PE repatriated income. Do not apply any of them to salary. Establish the full statutory business/base/treaty conditions through the corporate/cross-border computation. [§70](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=90); [§70 bases and exclusions](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=91); [Schedule 1 §2(6)-(7)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=164).

## Filing and payment

| Obligation | Deadline/condition | Official source |
|---|---|---|
| Salary withholding statement and deposit to IRD | Within 25 days after the Nepali month ends | [§90(1)-(2)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=113) |
| Employment withholding certificate | Within 30 days after income-year end or after employment ends, for the period worked for that payer | [§91(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=114); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=115) |
| SSF contribution | Within 25 days after the payable month ends; monthly unless otherwise determined | [§4(3)-(4)](https://www.ssf.gov.np/images/news/17655918798529_%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%A6%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A4%BE%20%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%A4%20%E0%A4%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AD%E0%A5%AA.pdf#page=4) |
| Annual income return where required | Ordinary 3-month deadline, possible application-based extension; conditional employment-only exemption and income-threshold override are in `nepal-income-tax` | [§§96-98](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=124); [§97(2),§98](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=127); [current §97(1)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf#page=197) |

PAN registration before income/withholding is governed by Rule 23; employee listing is tied to the start of employment as above. Do not mislabel D-01 as the generic salary or natural-person return: `nepal-income-tax` distinguishes D-01 presumptive, D-02 turnover and normal D-03.

For IRD, use the [Taxpayer Portal](https://ird.gov.np/): identify payer PAN/month, prepare employee PAN/payment/gross-tax data, reconcile eTDS totals to payroll, obtain submission/verification acknowledgement, generate and pay the correct voucher and retain certificates. For SSF, use the [official SSF portal](https://www.ssf.gov.np/): confirm establishment and employee identifiers, upload/enter the contribution schedule on verified basic pay, reconcile employee/employer totals, generate/pay the reference and retain receipt plus member allocation. Exact authenticated screen labels and upload schema must be checked before actual submission; no invented form fields or automatic filing.

### Penalties and interest

| Failure and condition | Statutory treatment | Official source |
|---|---|---|
| Late eTDS statement | 2.5% per annum on tax required to be withheld, for each month/part of delay; not the old asserted NPR 100/day capped at NPR 5,000 | [§117(3)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=146) (in words on the page) |
| Late salary-tax deposit | Normal interest at 15% per annum for each month/part under §119; the old extra 1.5% per month was unsupported and is not added | [§2(कब)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=15); [§119](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=147) (in words on the page) |
| Failure to deduct/pay | Section 90 liabilities and possible §120 shortfall charges; do not assume failure to deduct excuses deposit | [§90(3)-(8)](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=113); [continuation](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=114); [§120](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf#page=148) |
| SSF contribution not deposited on time | §9(1) provides recovery with 10% interest; this text does not itself establish the seed's annual time-basis | [§9(1)](https://www.ssf.gov.np/images/news/17655918798529_%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%A6%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A4%BE%20%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%A4%20%E0%A4%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AD%E0%A5%AA.pdf#page=6) (in words on the page) |
| SSF circumstances outside employer's control | Within 30 days, apply with grounds for the statutory permission/partial or complete interest relief; not an automatic waiver | [§9(2)-(3)](https://www.ssf.gov.np/images/news/17655918798529_%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%A6%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A4%BE%20%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%A4%20%E0%A4%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AD%E0%A5%AA.pdf#page=7) |
| Misappropriation/fraudulent benefit or other specified SSF offence under §47 | Fine equal to the offence amount where ascertainable; where not, up to NPR 100,000 or up to 1 year's imprisonment or both. This is not a generic automatic 2× contribution late-payment penalty | [§47(1)-(2)](https://www.ssf.gov.np/images/news/17655918798529_%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%A6%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A4%BE%20%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%A4%20%E0%A4%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AD%E0%A5%AA.pdf#page=26) (in words on the page) |

Section 9 also permits specified recovery restrictions and, after the 2082 amendment, makes the employer bear the equivalent accident/death benefit where contribution default leaves a worker without the statutory benefit during the default period. Do not present interest payment as eliminating those consequences. [§9(4)-(6)](https://www.ssf.gov.np/images/news/17655918798529_%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%A6%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A4%BE%20%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%A4%20%E0%A4%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AD%E0%A5%AA.pdf#page=7). Annual-return/record and instalment penalties are sourced in `nepal-income-tax`. Obtain an authority account computation before quoting an overdue total.

### Excel working paper retained and updated

One row per employee; include year, year-to-date withholding and remaining-period reconciliation in addition to the original A-Q columns.

| Col | Field | Formula/evidence |
|---|---|---|
| A | Employee name | Verified payroll input |
| B | Residency R/NR | All statutory tests/treaty evidence |
| C | Status S/M | Election/year; current common scale does not remove the fact |
| D | Actual SSF participation | Evidence, not merely a registration checkbox |
| E | Annual taxable income | Reconciled gross/benefit/employer-contribution/deduction schedule |
| F | First-band rate | Set only after the statutory exception is established |
| G | Annual tax before credits | Correct year marginal formula below |
| H | Female remuneration-only eligibility | Evidence |
| I | Female credit | Eligible portion of G × statutory credit; hold unproved eligibility |
| J | Annual tax after credits | G less eligible credits; NR uses the sourced non-resident rule |
| K | Period salary tax | Reconciled annual projection/YTD; J/12 only for the stable illustration |
| L | Monthly basic remuneration | Contract/wage evidence; not automatically basic plus dearness |
| M | Employee SSF | L × applicable employee rate if covered |
| N | Employer SSF | L × applicable employer rate if covered |
| O | Monthly cash gross | Payroll input |
| P | Net cash | O - K - M - other authorised deductions |
| Q | Employer cash cost | O + N + other employer cash costs |

For current FY 2083/84 resident ordinary remuneration, with E as non-negative annual taxable income and F as the established first-band rate, the derived spreadsheet formula is:

```
=MIN(E,1000000)*F
 +MAX(MIN(E-1000000,500000),0)*10%
 +MAX(MIN(E-1500000,1000000),0)*20%
 +MAX(MIN(E-2500000,1500000),0)*27%
 +MAX(E-4000000,0)*29%
```

For historical FY 2082/83 SINGLE only, retain the old formula's logic:

```
=MIN(E,500000)*F
 +MAX(MIN(E-500000,200000),0)*10%
 +MAX(MIN(E-700000,300000),0)*20%
 +MAX(MIN(E-1000000,1000000),0)*30%
 +MAX(MIN(E-2000000,3000000),0)*36%
 +MAX(E-5000000,0)*39%
```

Historical couple uses the separate slice widths in `nepal-income-tax`. The old nested-IF constants 80,000, 380,000 and 1,460,000 excluded the first-band tax, which was separately added by the F term. The old explanatory note claiming those constants already included it was wrong; do not subtract it again. These formulas cover ordinary resident remuneration after base adjustments, not special capital gains or every mixed-income case.

## Completion checklist

Confirm PAN and actual scheme registration; check the year and residence; reconcile annual taxable pay/benefits/contributions; evidence every deduction/credit; verify basic pay and the wage notice; compute employee cash and employer cost separately; reconcile salary tax and SSF to submitted statements, receipts and member allocations; preserve certificates and pending items. Missing setup facts permit a clearly labelled provisional working paper, never a final bank payroll instruction or unverified filing.

## Sources

| Source and actual material read | Official URL | Read on |
|---|---|---|
| Read for employment base, withholding/certificates, conditional return rules, late charges, non-resident special-business routing and historical Schedule 1; personal scales/allowances owned by the linked income-tax skill; PDF pages 15,20-21,90-91,107,113-115,124-127,146-148,157-164 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AE%20(%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%90%E0%A4%A8%2C%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B2%E0%A5%87%20%E0%A4%97%E0%A4%B0%E0%A5%87%E0%A4%95%E0%A5%8B%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7h85rod.pdf) | 2026-11-15 (in words on the page) |
| Read for enacted commencement and personal/return changes; current scale applied through linked income-tax skill; PDF pages 1,197-200 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%B0%E0%A5%8D%E0%A4%A5%E0%A4%BF%E0%A4%95%20%E0%A4%B5%E0%A4%BF%E0%A4%A7%E0%A5%87%E0%A4%AF%E0%A4%95%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AE%E0%A5%A9_mqsvmdf.pdf) | 2026-11-15 (in words on the page) |
| Read for Rule 31 monthly apportionment and Rule 23 PAN registration; PDF pages 9,12 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%86%E0%A4%AF%E0%A4%95%E0%A4%B0%20%E0%A4%A8%E0%A4%BF%E0%A4%AF%E0%A4%AE%E0%A4%BE%E0%A4%B5%E0%A4%B2%E0%A5%80%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AB%E0%A5%AF%20(%E0%A4%B8%E0%A5%8B%E0%A4%B9%E0%A5%8D%E0%A4%B0%E0%A5%8C%E0%A4%82%20%E0%A4%B8%E0%A4%82%E0%A4%B6%E0%A5%8B%E0%A4%A7%E0%A4%A8%20%E0%A4%B8%E0%A4%B9%E0%A4%BF%E0%A4%A4)_7kddd2d.pdf) | 2026-11-15 |
| Read for current SSF Act contribution deadline, recovery/default consequences, scope/listing and offences; PDF pages 4-7,11-12,26 | [Official text](https://www.ssf.gov.np/images/news/17655918798529_%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%A6%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A4%BE%20%E0%A4%86%E0%A4%A7%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%A4%20%E0%A4%B8%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%81%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE%20%E0%A4%90%E0%A4%A8%2C%20%E0%A5%A8%E0%A5%A6%E0%A5%AD%E0%A5%AA.pdf) | 2026-11-15 |
| Read for fifth-amendment Operation Procedure §25 contribution base, aggregate and four scheme allocations; visually rendered page; PDF pages 17 | [Official text](https://www.ssf.gov.np/images/news/17406520344566_Social%20Security%20Operation%20Procedure%202075%20with%205th%20ammendment.pdf) | 2026-11-15 |
| Read for Labour Act §§52-53 including deposit/fallback conditions; official Labour Court hosted text; PDF pages 22-23 | [Official text](https://labourcourt.gov.np/assets/uploads/ea43b3437b12a2cb4a51a4cd154c428c.pdf) | 2026-11-15 |
| Read for ordinary minimum wage, effective date, full table and conditions; visually read Gazette; PDF pages 1-2 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A5%A6%E0%A5%AE%E0%A5%A8%20%E0%A4%B8%E0%A4%BE%E0%A4%89%E0%A4%A8%20%E0%A5%A7_250826_112619_eudzntr_5f2rztd.pdf) | 2026-11-15 |
| Read for tea-estate minimum wage, effective date, full table and conditions; visually read Gazette; PDF pages 1-3 | [Official text](https://giwmscdnone.gov.np/media/pdf_upload/%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2%20%E0%A4%B0%E0%A4%BE%E0%A4%9C%E0%A4%AA%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BE%20%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%95%E0%A4%BE%E0%A4%B6%E0%A4%BF%E0%A4%A4%20%E0%A4%9A%E0%A4%BF%E0%A4%AF%E0%A4%BE%20%E0%A4%AC%E0%A4%97%E0%A4%BE%E0%A4%A8%E0%A4%95%E0%A4%BE%20%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%E0%A4%95%E0%A4%BE%20%E0%A4%B2%E0%A4%BE%E0%A4%97%E0%A4%BF%20%E0%A4%A8%E0%A5%8D%E0%A4%AF%E0%A5%82%E0%A4%A8%E0%A4%A4%E0%A4%AE%20%E0%A4%AA%E0%A4%BE%E0%A4%B0%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A4%AE%E0%A4%BF%E0%A4%95%20%E0%A4%B8%E0%A5%82%E0%A4%9A%E0%A4%A8%E0%A4%BE_blfvfy6.pdf) | 2026-11-15 |
| Read for IRD FAQ excerpt identifying remuneration-based social security tax revenue code 11211; not its historical rate tables; PDF pages not applicable: HTML excerpt | [Official text](https://ird.gov.np/faq/?gid=97) | 2026-11-15 |

Not yet confirmed: any universal headcount-only SSF scope claim without the applicable §19 notification; special public-sector/foreign-worker scheme coverage; alleged NPR 350,000 monthly SSF ceiling (and its reported predecessor NPR 300,000); contractual basic-pay disputes; exact time-basis/annualisation of §9 SSF interest; authenticated eTDS/SSF screen labels, upload schema and current revenue-code selection; taxpayer-specific treaty and benefit eligibility. Do not apply those unconfirmed legacy cap or penalty assumptions.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed chartered accountant or registered auditor in Nepal) before implementation.
