---
name: bw-payroll-social
description: >
  Botswana payroll for 2026-27: PAYE tables from 1 July 2026, 27.5% monthly top band, benefits, allowances, remittance in 14 days, annual return, no state social security. Use for Botswana payroll.
version: 1.0
jurisdiction: BW
category: international
tax_year: 2026
tax_year_notes: "2026-27 (1 July 2026 to 30 June 2027)"
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Botswana Payroll and Social Contributions v1.0

> **General reference only.** This skill is general tax reference material. It has not been reviewed for any specific person's facts. Check figures against the official sources named here.

Tax year: 2026-27 (1 July 2026 to 30 June 2027). The Income Tax Act, 2026, Tax Administration Act, 2026 and Value Added Tax Act, 2026 commenced on 1 July 2026 and replace the old Cap. 52:01 and Cap. 50:03 regimes.

## Who this applies to

Employers paying employment income in Botswana, and approved retirement funds (ITA s 129).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| PAYE table | BURS tables effective 1 July 2026 | 2026-27 | https://www.burs.org.bw/images/Tax%20Table_2026.pdf |
| Resident monthly free amount | P4,000 (P48,000 a year) | 2026-27 | https://www.burs.org.bw/images/Tax%20Table_2026.pdf (Example 12 heading) |
| Top monthly band, resident | 27.5% above P33,333; tax on P33,333 is P6,170.83 | 2026-27 | https://www.burs.org.bw/images/Tax%20Table_2026.pdf (Example 4) |
| Non-resident tax on first P33,333 | P6,370.83 | 2026-27 | https://www.burs.org.bw/images/Tax%20Table_2026.pdf (Example 5) |
| Motor vehicle benefit | 10% of cost a year | 2026-27 | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 (SI 92 reg 24) |
| Housing benefit cap | prescribed table; above P58,600 income, 27.5% of income | 2027 onward | https://www.burs.org.bw/images/Tax%20Table_2026.pdf (housing table) |
| Employer retirement deduction | up to 20% of employment income | 2026-27 | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 (s 28(2)) |
| Severance and gratuity | 50% not taxed | 2026-27 | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 (s 17(3)) |

Annual bands sit in [Income tax](bw-income-tax.md).

## The base

Employment income includes cash and benefits (table note 3). The only deduction in the table is the employee's contribution to an approved fund (note 5). Use a Form ITW 5 directive from BURS over the tables where one exists (note 2).

Taxable allowances include bonus, overtime, housing, car, education, utilities, medical allowance, acting and responsibility. Non-taxable if reasonable and for duties: subsistence, out of pocket, car kilometreage, uniform, duty travel, transfer, meal.

Benefit values from Example 14: rent-free rated housing at 10% of rateable value, school fees in full, employer medical aid contribution exempt, concessional loan at the difference from the commercial rate. The Example's text shows P600,000 and P500,000 for the same rateable value; use reg 19 of SI 92.

No state social security or national pension contribution appears in the 2026 tax table or the Income Tax Act; the old file says none exists. Workplace pension funds are employer-arranged and approved under the Act.

## Deadlines and filing

1. Each pay run, find the amount in the monthly table; above the table, apply the Example 4 steps.
2. Pay BURS within 14 days after the month of payment, using the remittance return (ITA s 138). The BURS Payments page says 15 days and predates the Act.
3. Give each employee a withholding certificate (s 137); form ITW8 per the BURS returns page.
4. Within 28 days after 30 June, lodge ITW10 with the list of employees through e-Tax at https://eservices.burs.org.bw/ (s 139). The old file said 31 July.

## Penalties and interest

Interest is 1.5% a month or part month, simple (TAA s 41(2), Regs reg 21). Late filing of an income tax return: the greater of P100 a day (cap P20,000) or 10% of unpaid tax a month; the fixed amount never exceeds the tax on the return (TAA s 101). VAT return: the greater of P50 a day (cap P5,000) or 10% a month. Other documents: P50 a day, cap P5,000. Late payment: the greater of P50 a day or 10% a month (TAA s 102), but reg 33 of SI 90 waives this penalty for 12 months from commencement, which runs to 30 June 2027; interest still runs. False statement made deliberately or recklessly: 75% of the shortfall; any other false or misleading statement: 20%. Add 10 points on a second application and 25 on a third or later; half off on voluntary disclosure before discovery or audit (TAA s 103). Failure to e-file or e-pay where required: P20 manual fee (reg 30). Failure to register: 100% of the tax for the period, or P10,000 a month if none is due (TAA s 98).

Late payment interest on withholding tax is the employer's own cost (TAA s 41(3)).

## Cross-border points

A foreign employee here no more than 90 days in 12 months can be exempt (ITA Sch 2 Pt VI para 6). Non-residents have no tax-free band.

## Two worked examples that recompute

Example 1. BURS Example 4: P34,000 a month resident.

```oa-check
name: PAYE P34,000
inputs:
  pay: 34000
steps:
  - tax: 6170.83 + (pay - 33333) * 0.275
expected:
  tax: 6354.26
```

Example 2. A decision: company car or cash? A car costing P160,000 adds P16,000 a year; a P2,000 monthly car allowance adds P24,000.

```oa-check
name: Car or allowance
inputs:
  cost: 160000
  allowance: 2000
steps:
  - car: cost * 0.10
  - cash: allowance * 12
  - difference: cash - car
expected:
  car: 16000.00
  cash: 24000.00
  difference: 8000.00
```

## Ask the client first

- Resident or non-resident employees?
- Any benefits: housing, car, school fees, loans?
- Any BURS directive?
- Approved retirement fund?
- Monthly, weekly or daily pay?

## Sources

| Source | Link | Read |
|---|---|---|
| BURS Tax Table and Guidance Notes, effective 1 July 2026: notes, Examples 4, 5, 14, housing table, allowances | https://www.burs.org.bw/images/Tax%20Table_2026.pdf | 2026-11-01 |
| Income Tax Act, 2026 (No. 13 of 2026), read: ss 7, 8, 17, 28, 34 to 37, 53, 96, 117, 119, 123 to 144, Schedules 1 to 3; Regulations SI 92 and Commencement Order SI 93 in the same file | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 | 2026-11-01 |
| Tax Administration Act, 2026 (No. 14 of 2026), read: ss 14, 18, 27, 41, 98, 101 to 103; Regulations SI 90 regs 3, 4, 21, 28, 30, 33, 34 in the same file | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026 | 2026-11-01 |
| BURS Returns page, form names only (page predates the 2026 Acts) | https://www.burs.org.bw/index.php/tax/returns | 2026-11-01 |

Not yet confirmed: Vocational Training Levy of 0.2% of turnover up to BWP 2 billion and 0.05% above (old file, no official page opened; the BURS and HRDC pages read do not show it); ITW8 date of 31 March from the old file (the Act ties certificates to s 138); Retirement Funds Act detail on occupational funds; whether social security law has changed outside tax law.

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
