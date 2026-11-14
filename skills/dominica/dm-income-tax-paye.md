---
name: dm-income-tax-paye
description: >
  Commonwealth of Dominica individual income tax and employer PAYE for 2026, not the
  Dominican Republic. Covers the EC$30,000 resident allowance, the bands of 15% on the
  next EC$20,000, 25% on the next EC$30,000 and 35% above, the mortgage interest, student
  loan and donation allowances, who must file by 31 March, the filing exemption for
  employment income below EC$30,000, prepayments for the self-employed, and the monthly
  PAYE return by the 15th and Form TD5 by 31 January. Trigger phrases include Dominica
  income tax, resident allowance, Dominica PAYE, TD5, Schedule G.
version: 1.0
jurisdiction: DM
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Dominica individual income tax and PAYE

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Income tax on individuals in the Commonwealth of Dominica (DM) for the 2026 income year under the Income Tax Act, Chapter 67:01, as published by the Inland Revenue Division (IRD), and employer PAYE. Not the Dominican Republic. Amounts are EC$. Company tax is in [dm-corporate-income-tax](dm-corporate-income-tax.md), social security in [dm-social-contributions](dm-social-contributions.md), VAT in [dm-vat](dm-vat.md). Residence tests, foreign income, nonresident rules, benefits in kind and the monthly withholding tables in detail are outside this skill.

## Ask the client first

1. Is the person resident in Dominica for tax purposes (IRD treats a person physically present more than 183 days as resident)?
2. Income for the year by source: employment, self-employment or business, other.
3. Expenses wholly and exclusively incurred in producing business income.
4. Mortgage interest on a home the person owns and lives in (with the Certificate of Title), student loans with a Dominica institution, donations to approved institutions.
5. For an employer: number of employees, monthly payroll, PAYE deducted.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Resident allowance | EC$30,000 a year, effective 1 January 2018, residents only | [IRD current income tax rates](https://www.ird.gov.dm/customer-service/current-income-tax-rates) |
| Band 1 (income 30,001 to 50,000) | 15% on the next EC$20,000 | same |
| Band 2 (income 50,001 to 80,000) | 25% on the next EC$30,000 | same |
| Band 3 (income above 80,000) | 35% | same |
| Monthly equivalents | Allowance 2,500; next 1,666.67 at 15%; next 2,500 at 25%; above 6,666.67 at 35% | same |
| Mortgage interest allowance | Up to EC$25,000, owner-occupied residence | [IRD personal income tax](https://ird.gov.dm/tax-laws/personal-income-tax) |
| Student loan relief | Up to EC$5,000 a year per student, loan with a Dominica institution | same |
| Carnival fund donation | Not less than EC$1,000 and not more than EC$20,000 | same |
| Filing exemption | Income entirely from employment and less than EC$30,000 | same |
| Individual return | 31 March following the year | [IRD tax due dates](https://ird.gov.dm/customer-service/tax-due-dates) |
| Prepayments (self-employed, employees with business income) | 25% by 31 March, 35% by 30 June, 40% by 30 September, of prior-year tax or a current-year estimate | same |
| Monthly PAYE | Deducted tax paid and return filed by the 15th of the following month, even if nil | [IRD PAYE](https://ird.gov.dm/tax-laws/pay-as-you-earn-p-a-y-e) |
| Annual employer return, Form TD5 | 31 January following the year | [IRD tax due dates](https://ird.gov.dm/customer-service/tax-due-dates) |
| Form IT24 (payments other than wages) | 31 January | same |
| Mortgage interest statements for PAYE adjustments | 15 January | same |

### Steps

1. **Total income** from all sources together; IRD warns against reporting sources separately.
2. **Deduct** business expenses that were wholly and exclusively incurred in producing the income.
3. **Allowances:** EC$30,000 resident allowance (residents only), then mortgage interest, student loan relief and approved donations within their caps.
4. **Chargeable income after allowances (C):** 15% on the first 20,000, 25% on the next 30,000, 35% above 50,000. The IRD rate table shows the same bands with the 30,000 allowance included (no tax to 30,000); never deduct the allowance twice.
5. **Credits:** subtract PAYE withheld and prepayments.
6. **File** by 31 March with Schedule G or a statement of earnings if self-employed.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Employee whose income is entirely employment income below EC$30,000 | Not obliged to file | [IRD personal income tax](https://ird.gov.dm/tax-laws/personal-income-tax) |
| Employee below EC$30,000 who also has any business income | Must file; the exemption is for employment income only | same |
| Nonresident | No resident allowance | same |
| Business ceased or employment ended in the year | File a return (section 67(b) per the IRD FAQ), which also lets an employee recover excess tax | [IRD FAQ](https://ird.gov.dm/f-a-q) |
| Income exactly EC$30,000 from employment | The exemption says "less than"; at exactly 30,000 file | [IRD personal income tax](https://ird.gov.dm/tax-laws/personal-income-tax) |
| Late PAYE or prepayment | Penalty and interest under the relevant Acts | [IRD tax due dates](https://ird.gov.dm/customer-service/tax-due-dates) |

## Worked cases

### Case 1: resident at three income levels

A resident with no other allowances: income 50,000 gives C = 20,000 and tax 3,000; income 80,000 gives C = 50,000 and tax 10,500; income 100,000 gives C = 70,000 and tax 17,500.

```oa-check
name: Dominica resident income tax at 100,000 (2026 bands)
inputs:
  income: 100000
  allowance: 30000
steps:
  - c: max(income - allowance, 0)
  - band1: min(c, 20000) * 0.15
  - band2: min(max(c - 20000, 0), 30000) * 0.25
  - band3: max(c - 50000, 0) * 0.35
  - tax: band1 + band2 + band3
expected:
  c: 70000
  band1: 3000
  band2: 7500
  band3: 7000
  tax: 17500
```

### Case 2 (decision): is the mortgage interest claim worth the paperwork?

The same resident earns 100,000 and paid 12,000 of mortgage interest on the home they own and live in. Claiming it lowers C to 58,000 and tax to 13,300, a saving of 4,200 (12,000 at the 35% top rate). The claim needs the Certificate of Title and the interest statement; for an employee, send the statement by 15 January so PAYE is adjusted.

```oa-check
name: Dominica mortgage interest allowance, 12,000 on 100,000 income
inputs:
  income: 100000
  allowance: 30000
  mortgage: 12000
steps:
  - c: income - allowance - min(mortgage, 25000)
  - tax: min(c, 20000) * 0.15 + min(max(c - 20000, 0), 30000) * 0.25 + max(c - 50000, 0) * 0.35
  - saving: 17500 - tax
expected:
  c: 58000
  tax: 13300
  saving: 4200
```

## When to refuse or refer

- Residence questions beyond the 183-day statement, foreign income, nonresident withholding: refer.
- Benefits in kind, special income, payroll rounding and the monthly withholding tables: not covered.
- Penalty and interest rates: not set out on the IRD pages read; refer to the Act.

## Filing and payment

1. Employers: deduct PAYE each month and file the monthly return with payment by the 15th of the next month, nil returns included ([IRD PAYE](https://ird.gov.dm/tax-laws/pay-as-you-earn-p-a-y-e)); file Form TD5 by 31 January.
2. Individuals: file by 31 March and pay any balance for the previous year by the same date.
3. Self-employed and employees with business income: prepay 25%, 35% and 40% on 31 March, 30 June and 30 September.
4. Keep social security deductions separate from PAYE.

## Completion checklist

- Residence settled; all sources added together.
- Allowance deducted once; caps applied.
- Bands applied to C.
- PAYE and prepayments credited; return filed by 31 March.

## Sources

| Source | URL | Read on |
|---|---|---|
| IRD current income tax rates: read for the EC$30,000 resident allowance, the 15%, 25% and 35% bands, the monthly breakdown and the 25% company rate | https://www.ird.gov.dm/customer-service/current-income-tax-rates | 2026-11-14 |
| IRD personal income tax: read for the 31 March filing duty, 183-day residence note, the employment income below EC$30,000 exemption, Schedule G, and the mortgage, student loan and donation allowances | https://ird.gov.dm/tax-laws/personal-income-tax | 2026-11-14 |
| IRD pay as you earn: read for the post-allowance bands and monthly returns by the 15th, nil returns included, and the annual return by 31 January | https://ird.gov.dm/tax-laws/pay-as-you-earn-p-a-y-e | 2026-11-14 |
| IRD tax due dates: read for TD5 and IT24 by 31 January, mortgage statements by 15 January, returns and balances by 31 March, the 25%, 35% and 40% prepayments and PAYE by the 15th | https://ird.gov.dm/customer-service/tax-due-dates | 2026-11-14 |
| IRD FAQ: read for section 67(b), returns where a business ceased or employment ended | https://ird.gov.dm/f-a-q | 2026-11-14 |

Not yet confirmed: the Income Tax Act Chapter 67:01 text itself (not opened; figures rest on IRD pages); penalty and interest rates; any 2026 budget change to the bands or allowance (none shown on the IRD rate page); the statutory residence test beyond the IRD's 183-day note.
