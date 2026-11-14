---
name: bz-income-tax
description: "Belize individual income tax for employed persons in tax year 2026. Since basis year 2020 income tax is charged only on employed persons, at 25% of chargeable income; a resident employee with total income under BZD 29,000 is not chargeable, above it a basic deduction of BZD 20,000 applies, and between BZD 29,000 and 32,000 a tapering tax credit reduces the tax. Covers who is taxed, the computation on form BTS203, PAYE, the annual return by 31 March, penalties, the UK pension election and how self-employed income is handled instead through business tax. Trigger phrases include Belize income tax, Belize PAYE, BTS203, Belize personal allowance, Belize tax free threshold and Belize employee tax return."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bz-income-tax"
  jurisdiction: "BZ"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Belize individual income tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** From basis year 2020 onward, Belize charges income tax only on **employed persons**, at **25% of chargeable income** accruing in or derived from Belize (Income and Business Tax Act, Cap. 55, s.6 as replaced by Act No. 40 of 2024, in force 1 January 2025). A resident employee whose total income is **under BZD 29,000** is not chargeable. Above BZD 29,000 a **basic deduction of BZD 20,000** applies, and between BZD 29,000 and BZD 32,000 a **tax credit of BZD 2,250 less 75% of the income above BZD 29,000** also applies. Self-employed people and businesses pay business tax on receipts instead: see [bz-corporate-income-tax](bz-corporate-income-tax.md). Tax year: calendar year 2026. Currency: BZD. Authority: Belize Tax Service (BTS).

## Who this applies to

- **In:** employed persons, meaning people receiving emoluments, including consultants who work for one employer for periods adding up to 60 days or more in the year (BTS treats them as employees under PAYE) ([BTS Business Tax Guide, FAQ 5](https://media.bts.gov.bz/uploads/Business_Tax_Guide_20250929_fc95296232.pdf)).
- **Scope of the charge:** chargeable income accruing in or derived from Belize, whether received in Belize or not. An employed person engaged in a trade, business or profession whose revenue or income is derived outside Belize is not liable to Belize income tax (Cap. 55 s.6(3) and (4) as replaced in 2024).
- **Not charged:** any person other than an employed person (s.6(2)). Self-employed income, partnerships and companies pay business tax. A person with both employment income and business receipts files two returns and does not combine them ([BTS Business Tax Guide, FAQ 4](https://media.bts.gov.bz/uploads/Business_Tax_Guide_20250929_fc95296232.pdf)).
- **Out of this skill:** petroleum operations (40%, payable in US dollars, s.6(3)(a)) and Designated Processing Area operations (3% of net chargeable income, s.6(3)(b)).

## Rates, bands and thresholds

| Item | Figure (2026) | Conditions | Source |
|---|---|---|---|
| Income tax rate, employed persons | 25% of chargeable income | Basis year 2020 onward; income accruing in or derived from Belize | [Act No. 40 of 2024, s.3 (new s.6(3))](https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf) |
| Not chargeable | Total income from all sources under BZD 29,000 | Resident employed individual | [Act No. 40 of 2024, s.4 (new s.16(2))](https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf) |
| Basic deduction | BZD 20,000 | Resident employed individual whose total income exceeds BZD 29,000 | [Act No. 40 of 2024, s.4 (new s.16(1))](https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf) |
| Tax credit, taper band | BZD 2,250 less 75% of (total income less BZD 29,000), not more than the tax | Total income above BZD 29,000 and not above BZD 32,000; the BTS203 form caps the credit at the tax payable | [BTS203 return, effective 2025 (Tax Credit line formula)](https://media.bts.gov.bz/uploads/BTS_203_Income_Tax_Return_For_Employees_Fillable_Effective2025_c69fde410f.xlsx) |
| Petroleum operations | 40% of chargeable income from those operations, payable in US dollars | s.6(3)(a) | [Act No. 40 of 2024, s.3](https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf) |
| Designated Processing Area operations | 3% of net chargeable income | s.6(3)(b) | same |
| Qualified retired person, UK pension election | 2% of the gross UK pension above GBP 3,500 (or its equivalent) | Election under s.6(5) and (6); retired persons authorisation card required | same |
| Credit for gifts to sports or education | Lesser of BZD 30,000 or 1% of the tax payable | s.108B | same |
| Annual return due | Last day of the third month after the basis year (31 March 2027 for 2026) | Employees with only emoluments need not file unless claiming a refund, asked by the Commissioner, or tax is unpaid | [Cap. 55 s.31(1) and (2)](https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf) |
| Late return penalty | 3% of the unpaid tax for each month or part month, for up to 20 months | Not levied on a return filed only to claim a refund | [Cap. 55 s.31(5) and (7)](https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf) |
| Late payment | 1½ per cent of the unpaid tax per month | From the day after the prescribed period until payment | [Cap. 55 s.55(a)](https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf) |

## The base

The BTS203 Income Tax Return for Employees (effective 2025) sets the order of the computation ([BTS203 form](https://media.bts.gov.bz/uploads/BTS_203_Income_Tax_Return_For_Employees_Fillable_Effective2025_c69fde410f.xlsx)):

1. **Total income from employment** (listed by employer on the back of the form). Emoluments include most cash and benefits; medical or dental insurance premiums paid by the employer for employees are not emoluments ([Payment of Income Tax (Amendment) Rules 2010, rule 2](https://media.bts.gov.bz/uploads/2010_Statutory_Instrument_No_73_of_2010_1c910fbfaa.pdf)).
2. **Deductions:** personal relief (the BZD 20,000 basic deduction), charitable donations, contributions to sports and contributions to education, each as the guide to the form allows.
3. **Chargeable income** = total taxable income less deductions; nil where total income is BZD 29,000 or less on the form.
4. **Tax** = chargeable income x 25%.
5. **Tax credit** where total income is above BZD 29,000 and not above BZD 32,000, capped at the tax.
6. **Income tax due** = tax less credit; then subtract tax deducted at source (PAYE) and instalments to reach the balance due or refund; add the late filing penalty (3% a month) and interest (1.5% a month) if late.

Business tax paid by someone who is not an employed person counts as a credit against any income tax on the same chargeable income, and an excess carries forward as an expense (s.21 as replaced in 2024). Interest on time deposits is no longer taxed (the 2024 Act's long title: "to remove the tax on interest income on time deposits").

## Deadlines and filing

- **PAYE:** employers deduct income tax from emoluments and remit it with form BTS200 (monthly remittance of income tax withheld); an employer who fails to deduct and remit is liable for the amount ([Cap. 55, PAYE provisions](https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf); [BTS tax resources, forms](https://bts.gov.bz/tax_resources)). Payroll detail is in [bz-payroll-social](bz-payroll-social.md).
- **Annual return:** BTS203 by 31 March 2027 for basis year 2026, filed online on [IRIS Belize](https://irisbelize.bts.gov.bz) (BTS publishes a tutorial for "Employee Income Tax Submission Online"). An employee whose only income is emoluments need not file unless claiming a refund, asked by the Commissioner, or tax remains unpaid (s.31(2)).
- **Notice to file:** anyone served with a notice must file within 15 days of service (s.31(4)).

## Penalties and interest

- Late return: 3% of the unpaid tax per month or part month, up to 20 months (s.31(5)); the Income Tax Appeal Board may vary or discharge it for reasonable cause (s.31(6)).
- Late payment: 1.5% per month on unpaid tax (s.55(a)), shown on BTS203 as "Interest on Balance Due (1.5% per month)".

## Cross-border points

- An employed person whose trade, business or profession revenue is derived outside Belize is not liable to Belize income tax (s.6(4) as replaced in 2024).
- Double taxation relief applies to tax paid in any treaty country (s.47 as replaced in 2024): for a resident, relief at the treaty-country rate if it does not exceed half the Belize rate, otherwise at half the Belize rate.
- A qualified retired person resident in Belize may elect to be taxed in Belize on UK pension income at 2% above GBP 3,500 (s.6(5) and (6)).
- Payments to non-residents (dividends, interest, management and technical fees) are covered by withholding in [bz-corporate-income-tax](bz-corporate-income-tax.md).

## Two worked examples that recompute

**Example 1: employee earning BZD 40,000 (simple).** Total income 40,000 exceeds 29,000, so the BZD 20,000 basic deduction applies. Chargeable income 20,000; tax 25% = BZD 5,000. Income above 32,000, so no tax credit.

```oa-check
name: Belize employee, BZD 40,000, basic deduction and 25%
inputs:
  total_income: 40000
  basic_deduction: 20000
  rate: 0.25
steps:
  - chargeable: total_income - basic_deduction
  - tax: chargeable * rate
expected:
  chargeable: 20000.00
  tax: 5000.00
```

**Example 2: employee earning BZD 30,000, inside the taper band (edge case).** Chargeable income 30,000 less 20,000 = 10,000; tax 2,500. Tax credit = 2,250 less 75% x (30,000 less 29,000) = 1,500, below the tax, so income tax due is BZD 1,000. An employee earning BZD 28,000 is not chargeable at all.

```oa-check
name: Belize employee, BZD 30,000, taper credit
inputs:
  total_income: 30000
  basic_deduction: 20000
  rate: 0.25
  credit_base: 2250
  credit_floor_income: 29000
  taper: 0.75
steps:
  - chargeable: total_income - basic_deduction
  - tax: chargeable * rate
  - credit: min(credit_base - (total_income - credit_floor_income) * taper, tax)
  - tax_due: tax - credit
expected:
  chargeable: 10000.00
  tax: 2500.00
  credit: 1500.00
  tax_due: 1000.00
```

## Ask the client first

1. Is the person an employee (emoluments), or self-employed, or both? Consultants for one payer for 60 days or more are employees.
2. Total income from all sources in 2026 (the BZD 29,000 and BZD 32,000 lines).
3. Is the person resident in Belize, and is any of the income derived outside Belize?
4. PAYE deducted by each employer, and any instalments paid.
5. Donations to charity, sports or education, with receipts.
6. Is the person a qualified retired person with UK pension income?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income and Business Tax (Amendment) Act No. 40 of 2024, read for the new s.6 (charge only on employed persons, 25%, 40% petroleum, 3% DPA, foreign-derived income, UK pension election), s.16 (BZD 29,000, BZD 20,000, tax credit), s.21, s.47, s.108B and commencement 1 January 2025 | https://media.bts.gov.bz/uploads/Act_No_40_of_2024_Income_and_Business_Tax_Amendment_Act_2024_b6bf496b66.pdf | 2026-11-14 |
| BTS203 Income Tax Return for Employees, effective 2025 (spreadsheet), read for the line order and the formulas for chargeable income, 25% and the tax credit | https://media.bts.gov.bz/uploads/BTS_203_Income_Tax_Return_For_Employees_Fillable_Effective2025_c69fde410f.xlsx | 2026-11-14 |
| Income and Business Tax Act, Cap. 55, Revised Edition 2011, read for s.31 (returns, 3% late penalty) and s.55 (1½ per cent interest) and the PAYE provisions | https://media.bts.gov.bz/uploads/Income_and_Business_Tax_Act_2011_13d48a3c6e.pdf | 2026-11-14 |
| Payment of Income Tax (Amendment) Rules 2010 (SI 73 of 2010), read for medical and dental insurance premiums not being emoluments | https://media.bts.gov.bz/uploads/2010_Statutory_Instrument_No_73_of_2010_1c910fbfaa.pdf | 2026-11-14 |
| BTS Business Tax Guide (September 2025), read for FAQ 4 and 5 (employment and business receipts, the 60-day consultant rule) | https://media.bts.gov.bz/uploads/Business_Tax_Guide_20250929_fc95296232.pdf | 2026-11-14 |
| BTS tax resources page, read for the list of income tax forms (BTS200, BTS203) | https://bts.gov.bz/tax_resources | 2026-11-14 |

Not yet confirmed: the PAYE remittance due date (the 1970 payment rules on the BTS site are a scanned image and were not readable); the caps on the charitable, sports and education deductions on BTS203 (the form formulas show limits but the guide to the form was not read); the statutory residence test (the old file's 183-day benchmark is not in the text read); any Order varying the BZD 29,000 or BZD 20,000 amounts for 2026 (s.16(3) lets the Minister vary them); the consolidated Revised Edition 2020 text.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bz-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bz-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
