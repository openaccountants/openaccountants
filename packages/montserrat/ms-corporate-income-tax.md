---
name: ms-corporate-income-tax
description: >
  Montserrat company income tax for 2026 under the Income and Corporation Tax Act,
  Chapter 17.01 (revised to 1 January 2025). Covers the 30% rate on chargeable income
  (section 36), deductible and non-deductible expenses (sections 13 to 16), the return
  by 31 March with a tax calculation (section 43), payment by 30 June or 45 days after
  assessment, the three equal instalments in February, April and June (section 50), the
  15% deduction from Government contract payments (section 37), company-specific rate
  orders and the branch remitted-profit charge. Trigger phrases include Montserrat
  corporation tax, Montserrat company tax 30%, Montserrat tax instalments.
version: 1.0
jurisdiction: MS
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: corporate-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Montserrat company income tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Company income tax in Montserrat for the 2026 year of assessment under the Income and Corporation Tax Act, Cap. 17.01, revised edition showing the law at 1 January 2025. Covers the rate, the base, the return and payments once residence and the basic year are settled. Amounts are EC$. Withholding on payments to nonresidents: [ms-nonresident-withholding](ms-nonresident-withholding.md). Residence, incentives, capital allowances, losses and treaties are outside it.

## Ask the client first

1. Is the company resident, or a nonresident company carrying on business in Montserrat (branch)?
2. Accounting profit for the basic year and each adjustment to chargeable income, with evidence.
3. Tax last assessed (for the instalments).
4. Any rate or exemption order made for the company?
5. Payments received from Government under contracts (15% deducted at source)?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Company rate, s.36 | 30% of chargeable income of any company, building society or body of persons | [Income and Corporation Tax Act Cap. 17.01](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf) |
| Return, s.43 | By 31 March each year (or another prescribed date), with a calculation of the tax payable; may be filed online | same |
| Payment, s.50(1) | By 30 June in the year of assessment or within 45 days of service of the assessment, whichever is later | same |
| Instalments, s.50(2) | A trader pays tax equal to that last assessed in three equal instalments in February, April and June; the Comptroller may adjust where a loss or lower profit is likely | same |
| Government contract payments, s.37 | The Accountant General deducts 15% (or a lesser sum the Comptroller sets), credited against the year's tax | same |
| Company-specific orders | For example SRO 36/2023: Ring Centre Ltd 5% for 2023 to 2025 and 10% for 2026 and 2027; SRO 25/2021: Phoenix Group International Ltd 10% for five years | same |
| Branch remitted profits, s.39(4) | A nonresident company carrying on business is liable to withholding tax on remitted profits in addition to income tax | same |

### Steps

1. **Chargeable income:** start from accounting profit; deduct only expenses wholly and exclusively incurred in producing the income (s.13), with the capital rules in ss.14 and 15; add back private, non-qualifying and capital amounts (s.16).
2. **Tax:** chargeable income x 30%, unless an order sets a different rate for the company.
3. **Instalments:** one third of the last assessed tax in each of February, April and June.
4. **Return** by 31 March with the tax calculation; **pay** the balance by 30 June or 45 days after assessment.
5. **Credits:** instalments and any s.37 deductions.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Forecast shows a lower profit | Instalments stay at last assessed tax unless the Comptroller adjusts them | [Cap. 17.01, s.50(2)](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf) |
| Overpaid instalments | Repaid; underpaid, recovered under the Act | same |
| Nonresident company with a branch | 30% tax plus withholding on remitted profits; not due on profits shown not remitted | [Cap. 17.01, s.39(4)](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf) |
| Interest on borrowed money | Deductible only if the capital was used to acquire the income (s.13 conditions) | same |

## Worked cases

### Case 1: tax and balance

Accounting profit 80,000 plus 5,000 of private expenditure added back gives chargeable income of 85,000 and tax of 25,500. Instalments based on last assessed tax of 24,000 are 8,000 each; the balance is 1,500.

```oa-check
name: Montserrat company tax on 85,000, instalments on 24,000
inputs:
  profit: 80000
  addback: 5000
  last_assessed: 24000
steps:
  - chargeable: profit + addback
  - tax: chargeable * 0.30
  - instalment: last_assessed / 3
  - balance: tax - instalment * 3
expected:
  chargeable: 85000
  tax: 25500
  instalment: 8000
  balance: 1500
```

### Case 2 (decision): ask the Comptroller to cut instalments?

Last assessed tax was 24,000 but a downturn means this year's tax will be about 9,000. Paying as assessed costs 8,000 in each of February, April and June and leaves 15,000 to be repaid. If the Comptroller agrees an adjustment to 9,000, each instalment is 3,000 and 15,000 stays in the business. Apply early with evidence of the expected loss or lower profit.

```oa-check
name: Montserrat instalment adjustment, 24,000 against 9,000
inputs:
  last_assessed: 24000
  expected: 9000
steps:
  - assessed_instalment: last_assessed / 3
  - adjusted_instalment: expected / 3
  - cash_kept: last_assessed - expected
expected:
  assessed_instalment: 8000
  adjusted_instalment: 3000
  cash_kept: 15000
```

## When to refuse or refer

- Residence, source, related-party payments, groups and international relief.
- Capital allowances, losses and incentives beyond the orders listed.
- Amendments after the 1 January 2025 revision.

## Filing and payment

1. File the return of the basic year's income with the tax calculation by 31 March, online if wished (s.43).
2. Pay instalments in February, April and June, and the balance by 30 June or 45 days after assessment (s.50).
3. Keep the profit-to-chargeable-income reconciliation with each adjustment, its section and evidence.

## Completion checklist

- Chargeable income reconciled; 30% (or the order rate) applied.
- Instalments one third of last assessed tax.
- Return by 31 March; balance by 30 June or 45 days.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income and Corporation Tax Act Cap. 17.01, revised to 1 January 2025: read for ss.13 to 16, 36 (30%), 37 (15% on Government contracts), 39(4), 43 (31 March return), 50 (payment and instalments) and the list of rate and exemption orders | https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf | 2026-11-14 |

Not yet confirmed: amendments made after 1 January 2025; penalties and interest for late returns and payments (not read); capital allowance rates.
