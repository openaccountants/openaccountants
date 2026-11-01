---
name: mu-income-tax
description: >
  Mauritius personal income tax for the income year 1 July 2026 to 30 June 2027. Covers residence, the 0, 10, 20 and 35 percent bands set by the Finance Act 2026, the end of the individual Fair Share Contribution, dependent deductions and reliefs, the Current Payment System, the 1 percent presumptive tax for small enterprises, the annual return due 15 October, penalties and foreign income. Use for questions on how much tax an employee, self-employed person or landlord pays in Mauritius, MRA individual returns, CPS statements, or when a Mauritius tax return is due.
jurisdiction: MU
category: international
tax_year: 2026
tax_year_notes: "Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28)"
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mauritius Personal Income Tax v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year covered: Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28).

## Who this applies to

Individuals with Mauritius-source income, and residents with foreign income. Resident means domiciled in Mauritius unless the permanent place of abode is abroad, or present 183 days or more in the income year, or 270 days or more in aggregate over the income year and the 2 preceding income years (Income Tax Act s.73(1)(a)). The income year runs 1 July to 30 June. Non-residents are taxed on Mauritius-source income and get no reliefs, deductions or allowances ([MRA foreign income page](https://www.mra.mu/index.php/individuals/foreign-income)). Payroll mechanics sit in [Payroll social](mu-payroll-social.md). Foreign income rules sit in [Cross-border](mu-cross-border.md).

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Band 1 | 0% on first Rs 500,000 of chargeable income | Income year from 1 July 2026 | 2026/27 | https://www.mra.mu/download/ITAConsolidated.pdf |
| Band 2 | 10% on next Rs 500,000 | same | 2026/27 | same |
| Band 3 | 20% on next Rs 11 million | same | 2026/27 | same |
| Band 4 | 35% on the remainder, above Rs 12 million | same; new by Finance Act 2026 s.7(v), s.28(12) | 2026/27 | https://www.mra.mu/download/FinanceAct2026.pdf |
| Prior year bands | 0% first Rs 500,000, 10% next Rs 500,000, 20% remainder | Income year 1 July 2025 to 30 June 2026 only | 2025/26 | https://www.mra.mu/download/PayrollTaxes.pdf |
| Individual Fair Share Contribution | 15% of leviable income above Rs 12 million, where the threshold income exceeds Rs 12 million | Only income year starting 1 July 2025 (s.16C(3) as cut by Finance Act 2026 s.7(b)) | 2025/26 | https://www.mra.mu/download/ITAConsolidated.pdf |
| Deduction, 1 dependent | Rs 110,000 | Resident only; dependent income limit Rs 110,000 | 2026/27 | https://www.mra.mu/individuals/reliefs-deductions-allowances |
| Deduction, 2 dependents | Rs 190,000 | Second dependent income limit Rs 80,000 | 2026/27 | same |
| Deduction, 3 dependents | Rs 275,000 | Third dependent income limit Rs 85,000 | 2026/27 | same |
| Deduction, 4 or more | Rs 355,000 | Fourth dependent income limit Rs 80,000 | 2026/27 | same |
| Tertiary education extra | Rs 500,000 per dependent | Non-sponsored full-time course; 6 years maximum; undergraduate in Mauritius needs tuition of at least Rs 34,800 | 2026/27 | https://www.mra.mu/download/ITAConsolidated.pdf |
| Private school fees extra | Fees paid or Rs 60,000, the lower | Registered fee-paying primary or secondary school | 2026/27 | same |
| Medical insurance relief | Rs 25,000 self, Rs 25,000 first dependent, Rs 20,000 each for second to fourth | Not where the employer pays or for combined medical and life cover | 2026/27 | same |
| Housing loan interest relief | Interest payable on the loan | Secured loan for own house; not where the person or spouse already owned a residence when the loan was made, or total income exceeds Rs 4 million | 2026/27 | https://www.mra.mu/individuals/reliefs-deductions-allowances |
| Charitable donations | Up to Rs 100,000 | Paid electronically to charitable institutions | 2026/27 | same |
| Personal pension | Up to Rs 50,000 | Approved individual pension scheme | 2026/27 | same |
| Solar and rainwater investment | Amount invested | Couple with no dependent spouse may split the claim | 2026/27 | same |
| Abolished from 1 July 2025 | Household employee wage deduction, animal adoption relief, angel investor allowance | Do not claim | 2025/26 on | https://www.mra.mu/download/PayrollTaxes.pdf |
| Return trigger, net income | Above Rs 500,000 | Also if tax was withheld, TDS suffered, or chargeable income exists | 2026/27 | https://www.mra.mu/download/ITAConsolidated.pdf |
| Return trigger, business | Gross business income above Rs 2 million | s.112(1)(a)(ii) | 2026/27 | same |
| CPS trigger | Prior-year CPS gross income above Rs 4 million | Off if tax on the quarter is Rs 500 or less | 2026/27 | same |
| Presumptive tax | 1% of gross income | Small enterprise: Thirteenth Schedule activity, gross income up to Rs 10 million, other income up to Rs 400,000; irrevocable; no deductions | 2026/27 | same |

## The base

Chargeable income is gross income less allowable deductions, exemptions and reliefs ([MRA obligation page](https://www.mra.mu/index.php/individuals/obligation-to-file-a-return)). Employment expenses must be wholly, exclusively and necessarily incurred in the duties (s.17). Business and rental expenses must be exclusively incurred in producing the income (s.18). Losses, bad debts and annual allowance replace depreciation. Dividends from a resident company are exempt (Second Schedule Part II Sub-part B item 1). Where a person claims dependents, the spouse cannot also claim. "Dependent" covers a spouse, a child under 18, an older child in full-time education or unable to earn because of disability, and a bedridden next of kin eligible for the carer's allowance.

From 1 July 2026 a new exemption covers qualifying non-citizen employees installing, commissioning or operating a solar photovoltaic manufacturing plant, for 4 income years, and a disturbance allowance for public officers on tour in Rodrigues or the Outer Islands (Finance Act 2026 s.7(w)).

## Deadlines and filing

1. Annual return: due 15 October after the income year, submitted electronically, tax paid at the same time (s.112(1)). The return for the year to 30 June 2027 is due 15 October 2027. Log in at [MRA e-Services](https://www.mra.mu/index.php/e-services) under File and Pay, Individual.
2. A person who has filed once keeps filing each year unless the Director-General agrees otherwise (s.112(1A)).
3. A self-employed person outside s.112 files a simplified return by the same date (s.112A).
4. CPS, by quarter (s.106): 1 July to 30 September is due 2 days before the end of December, excluding Saturdays and public holidays; 1 October to 31 December is due 31 March; 1 January to 31 March is due 2 days before the end of June, same exclusion. Quarter tax is computed on 25% of prior chargeable income scaled to CPS income (s.107), or on actual figures by option.
5. Statement of Assets and Liabilities: listed in the [MRA calendar](https://www.mra.mu/important-dates) on the same 15 October date.
6. Presumptive tax: elect by irrevocable notice on or before the return due date, then pay with the return after offsetting tax withheld (s.111V).
7. A due date on a Saturday, Sunday or public holiday moves to the next working day ([MRA calendar](https://www.mra.mu/important-dates)).

**AUDIT FLASH POINT** The MRA self-employed page still shows a 30 September return date, a 15% CPS rate and old penalties. The consolidated Act to Finance Act 2026 says 15 October and the penalties below. Follow the Act.

## Penalties and interest

| Item | Figure | Conditions | Source |
|---|---|---|---|
| Late return | Rs 2,000 per month or part, cap Rs 20,000 | s.121(1) | https://www.mra.mu/download/ITAConsolidated.pdf |
| Late return, small | Cap Rs 5,000 | Small enterprise up to Rs 10 million turnover or individual not in business | same |
| Late payment | 2.5% of the tax | s.122(1) | same |
| Late payment, small | 1% | Same group as above | same |
| Interest | 0.25% per month or part | s.122D(1)(b) | same |
| CPS late payment | 2.5% of unpaid tax | s.110 | same |
| Overclaimed loss | Up to 2.5% of the overclaim | s.122DA | same |

## Cross-border points

Foreign income of a resident individual is derived when received in Mauritius or dealt with there for the person (s.5(3)). Premium visa and golden visa holders pay on remote-work income only when remitted (s.73B). Foreign tax credit and treaties are in [Cross-border](mu-cross-border.md).

## Two worked examples that recompute

**Example 1. High earner.** Resident, chargeable income Rs 15,000,000 in 2026/27. Tax is Rs 50,000 at 10%, Rs 2,200,000 at 20%, and Rs 1,050,000 at 35% on Rs 3,000,000: Rs 3,300,000.

```oa-check
name: Chargeable income Rs 15m, 2026/27 bands
inputs:
  income: 15000000
steps:
  - b10: (min(income, 1000000) - 500000) * 0.10
  - b20: (min(income, 12000000) - 1000000) * 0.20
  - b35: (income - 12000000) * 0.35
  - tax: b10 + b20 + b35
expected:
  tax: 3300000.00
```

**Example 2. Decision: presumptive tax or normal tax.** A qualifying small enterprise has gross income Rs 8,000,000, expenses Rs 7,000,000 and one dependent. Normal chargeable income is Rs 890,000, tax Rs 39,000. Presumptive tax is Rs 80,000. Normal tax wins here, by Rs 41,000. With expenses of Rs 5,000,000 the normal route costs more, so test both before electing, because the election is irrevocable.

```oa-check
name: Presumptive 1 percent against normal tax
inputs:
  gross: 8000000
  expenses: 7000000
  dependent: 110000
steps:
  - chargeable: gross - expenses - dependent
  - normal: (min(chargeable, 1000000) - 500000) * 0.10
  - presumptive: gross * 0.01
  - saving: presumptive - normal
expected:
  normal: 39000.00
  presumptive: 80000.00
  saving: 41000.00
```

## Ask the client first

1. Which income year, and resident under s.73?
2. Employee, self-employed, landlord or a mix?
3. Gross business income this year and last year?
4. Number of dependents and each one's income?
5. Any foreign income, and was it brought to Mauritius?
6. Does the activity fall in the Thirteenth Schedule?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act consolidated to Finance Act 2026, sections read: ss.5, 16C, 17, 18, 73, 73B, 106 to 112A, 111U to 111W, 121, 122, 122D, 122DA; First, Third and Sixth Schedules | https://www.mra.mu/download/ITAConsolidated.pdf | 2026-11-01 |
| Finance Act 2026 (Act 14 of 2026), read in sections 7 and 28 | https://www.mra.mu/download/FinanceAct2026.pdf | 2026-11-01 |
| MRA reliefs page for the income year ending 30 June 2027, read in full | https://www.mra.mu/individuals/reliefs-deductions-allowances | 2026-11-01 |
| MRA letter to employers of 6 October 2025, read in full | https://www.mra.mu/download/PayrollTaxes.pdf | 2026-11-01 |
| MRA foreign income page, read in full | https://www.mra.mu/index.php/individuals/foreign-income | 2026-11-01 |
| MRA obligation to file page, read in full | https://www.mra.mu/index.php/individuals/obligation-to-file-a-return | 2026-11-01 |
| MRA self-employed page, read in full, found out of date on dates and penalties | https://www.mra.mu/index.php/individuals/self-employed | 2026-11-01 |
| MRA tax calendar July to December 2026, read in full | https://www.mra.mu/important-dates | 2026-11-01 |
| MRA e-Services menu, read in full | https://www.mra.mu/index.php/e-services | 2026-11-01 |

Not yet confirmed: field-by-field steps of the individual e-return inside the login, which we could not open; the Thirteenth Schedule activity list was not copied here; the carer deduction amount; the MRA obligation page still shows the 2025/26 bands, and the Act governs 2026/27.

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
