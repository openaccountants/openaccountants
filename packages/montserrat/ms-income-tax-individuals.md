---
name: ms-income-tax-individuals
description: >
  Montserrat personal income tax for 2026 under the Income and Corporation Tax Act,
  Cap. 17.01 (revised to 1 January 2025) and the Tax Administration Act, Cap. 17.26.
  Covers residence and source, the EC$18,000 general deduction (s.33(1)(g), from
  assessment year 2024), the bands after the deduction (5%, 20%, 25%, 30%, 40% above
  EC$132,000), resident pensioners at 0% to EC$60,000 and 5% above (Schedule 3), the
  return dates (31 March, 28 February for employment or pension income, 31 January in
  the rules and MCRS guidance), payment by 30 June or 45 days after assessment, TIN
  registration, records and interest. Trigger phrases include Montserrat income tax,
  Montserrat personal allowance 18000, Montserrat tax bands, MCRS individual return.
version: 1.0
jurisdiction: MS
tax_year: 2026
tax_year_notes: "Year of assessment 2026 (basic year 2025). The Schedule 2 bands and the EC$18,000 deduction apply to years of assessment from 1 January 2024 and still stood in the 1 January 2025 revision; no later change was found."
last_updated: 2026-11-14
category: international
type: computation
domain: income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Montserrat personal income tax

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Annual income tax of individuals in Montserrat for the 2026 year of assessment under the Income and Corporation Tax Act, Cap. 17.01, revised edition showing the law at 1 January 2025 (made authoritative on 23 February 2026 by SRO 8/2026), and the Tax Administration Act, Cap. 17.26 (in force 1 January 2024 under Act 13 of 2023; it keeps prior law for earlier events and lets certain old forms continue, ss.98 and 99). Amounts are EC$ (Cap. 17.26 s.54). Employer withholding on wages: [ms-paye-employer-withholding](ms-paye-employer-withholding.md). Companies: [ms-corporate-income-tax](ms-corporate-income-tax.md). Payments to nonresidents: [ms-nonresident-withholding](ms-nonresident-withholding.md).

## Ask the client first

1. Is the person resident in the basic year: permanent abode and presence, 183 days or more, or continuous presence spanning an adjacent year? Ordinarily resident and domiciled?
2. Income for the basic year by type: employment, trade, pension, rent, foreign income (and whether remitted).
3. Will the person complete a return and give the prescribed particulars (the condition for the EC$18,000 deduction)?
4. Other allowances claimed: incapacitated dependants, eligible social security contributions, residential mortgage interest.
5. Is the income only employment or pension income (it moves the return date)?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| General deduction, s.33(1)(g) | EC$18,000 for years of assessment from 1 January 2024, for a resident individual who completes a return and gives the prescribed particulars (old s.34(1), renumbered after old s.21 was deleted) | [Cap. 17.01, s.33](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=36) |
| Band 1, Schedule 2 | 5% on the first EC$7,000 after the deduction (Schedule 2 labels it EC$18,001 to EC$25,000 of income) | [Cap. 17.01, Schedule 2](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=54) |
| Band 2 | 20% on the next EC$10,000, to EC$17,000 after the deduction (derived; Schedule 2 prints EC$25,001 to EC$35,000) | same |
| Band 3 | 25% on the next EC$10,000, to EC$27,000 after the deduction (derived; Schedule 2 prints EC$35,001 to EC$45,000) | same |
| Band 4 | 30% on the next EC$105,000, to EC$132,000 after the deduction (derived; Schedule 2 prints EC$45,001 to EC$150,000) | same |
| Band 5 | 40% on the excess over EC$132,000 after the deduction (derived; Schedule 2 prints beyond EC$150,000) | same |
| Incapacitated dependant, s.33(3) | EC$2,400 each, or a share where maintained jointly | [Cap. 17.01, s.33](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=36) |
| Resident pensioner, s.35(b) and Schedule 3 | 0% on pension up to EC$60,000; 5% on the excess (years from 1 January 2008) | [Cap. 17.01, Schedule 3](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=56) |
| Return, s.43(1) | 31 March, unless another date is prescribed | [Cap. 17.01, s.43](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=41) |
| Return, employment or pension income, s.43(4) | 28 February | same |
| Payment, s.50(1) | By 30 June in the year of assessment or 45 days after service of the assessment, whichever is later | same |
| TIN registration, Cap. 17.26 ss.9 and 10 | Within 30 days after starting a covered activity, if not registered | [Cap. 17.26, ss.9 and 10](https://www.gov.ms/wp-content/uploads/2026/02/17.26-Tax-Administration-Act.pdf#page=16) |
| Interest, Cap. 17.26 s.57 | 6% simple a year, variable by Gazette order | [Cap. 17.26, s.57](https://www.gov.ms/wp-content/uploads/2026/02/17.26-Tax-Administration-Act.pdf) |

### The base

- **Residence, s.2.** Alternative tests: permanent abode and presence (with permitted absences), physical presence of at least 183 days in the basic year, or the continuous-presence branch spanning a qualifying adjacent year.
- **Income charged, s.3.** Specified income from Montserrat and elsewhere, with provisos for remittance, temporary presence and partly offshore trades. Settle ordinary residence, domicile, source, remittance and any treaty entitlement before taxing foreign income.
- **Basic year, s.4.** Generally the 12 months to 31 December before the year of assessment; the Comptroller may allow a different trade accounting date. Keep the annual assessment separate from pay periods.
- **The return method.** The 2024 individual return subtracts the EC$18,000 allowance and then applies the bands as widths (the table above). Schedule 2 prints the same widths and rates as absolute figures starting at EC$18,001. Apply the general deduction once.
- **Pensions.** Establish the pension's statutory class, any exemption, foreign pension treatment and the effect of other income before using Schedule 3.

### Steps

1. **Residence and income:** settle residence (s.2) and the income charged (s.3) for the basic year (s.4).
2. **Deductions:** subtract the EC$18,000 general deduction (s.33(1)(g)) if the return is completed with the particulars, then the other allowances whose conditions are met.
3. **Tax:** apply the bands to taxable income after deductions; tax a resident pensioner's pension under Schedule 3.
4. **Credits:** PAYE deducted by employers (s.51(13)) and any other tax withheld.
5. **File** by the date for the taxpayer's branch; **pay** the balance by 30 June or 45 days after assessment.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| MCRS online calculator | Its text uses the after-deduction bands, but its calculation code (read 2026-11-14) uses a different field in two bands and a base of 36400 in the last band (written as in its code). Use Schedule 2 and the return method; do not rely on the calculator's result | [MCRS calculator](https://mcrs.ms/income-tax-calculator/); [Cap. 17.01, Schedule 2](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=54) |
| Employment-only income: which return date? | s.43(4) prints 28 February; Income Tax Rules r.3 prints 31 January for the public-revenue part of public officers' and pensioners' income and 31 March otherwise (and still cites old s.50); the MCRS individual page says 31 January for all employment-only income and 31 March otherwise. Use the earliest date that can apply until MCRS confirms | [Cap. 17.01, s.43](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=41); [Income Tax Rules, r.3](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=71); [MCRS individual guidance](https://mcrs.ms/individual-tax-information/) |
| Late or missing return | MCRS guidance: a penalty not exceeding EC$2,000, or up to four months' imprisonment in default; an extension asked for before the due date avoids it; a penalty charged before the extension request stands | [MCRS individual guidance](https://mcrs.ms/individual-tax-information/) |
| Return not completed with the particulars | No s.33(1) general deduction | [Cap. 17.01, s.33](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=36) |
| Pension income of a resident pensioner | Schedule 3, not Schedule 2 | [Cap. 17.01, s.35 and Schedule 3](https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf#page=56) |
| Amended return | Allowed within 6 years after the tax period ends (Cap. 17.26 s.22) | [Cap. 17.26, ss.19 and 22](https://www.gov.ms/wp-content/uploads/2026/02/17.26-Tax-Administration-Act.pdf#page=20) |
| Deadline on a closed office day | Cap. 17.26 s.19 receipt and closed-day rules apply | same |
| Extension | Apply before the deadline (s.51); interest still runs | [Cap. 17.26, s.51](https://www.gov.ms/wp-content/uploads/2026/02/17.26-Tax-Administration-Act.pdf#page=20) |
| PAYE over-deducted January to July 2024 | SRO 37/2024 relief for the overpayment from Act 20's changes; see the PAYE skill | [SRO 37/2024](https://www.gov.ms/wp-content/uploads/2024/10/SRO-No.-37-of-2014-Income-and-Corporation-Tax-Individual-Exemption-Order.pdf) |

## Worked cases

### Case 1: taxable income of EC$133,000 after deductions

The first EC$132,000 gives EC$36,350 (350 + 2,000 + 2,500 + 31,500) and the excess EC$1,000 at 40% gives EC$400, for EC$36,750 before credits.

```oa-check
name: Montserrat personal tax on 133,000 after deductions
inputs:
  taxable: 133000
steps:
  - b1: min(taxable, 7000) * 0.05
  - b2: max(min(taxable, 17000) - 7000, 0) * 0.20
  - b3: max(min(taxable, 27000) - 17000, 0) * 0.25
  - b4: max(min(taxable, 132000) - 27000, 0) * 0.30
  - b5: max(taxable - 132000, 0) * 0.40
  - tax: b1 + b2 + b3 + b4 + b5
expected:
  b4: 31500
  b5: 400
  tax: 36750
```

### Case 2 (decision): complete the return with the particulars, or not?

A resident with EC$60,000 of income who completes the return gets the EC$18,000 deduction: taxable 42,000, tax 9,350 (derived). Without it the whole 60,000 runs through the bands: tax 14,750 (derived). Filing the return with the prescribed particulars saves 5,400.

```oa-check
name: Montserrat general deduction claimed or lost, income 60,000
inputs:
  income: 60000
  deduction: 18000
steps:
  - t1: income - deduction
  - tax_with: min(t1, 7000) * 0.05 + max(min(t1, 17000) - 7000, 0) * 0.20 + max(min(t1, 27000) - 17000, 0) * 0.25 + max(min(t1, 132000) - 27000, 0) * 0.30 + max(t1 - 132000, 0) * 0.40
  - tax_without: min(income, 7000) * 0.05 + max(min(income, 17000) - 7000, 0) * 0.20 + max(min(income, 27000) - 17000, 0) * 0.25 + max(min(income, 132000) - 27000, 0) * 0.30 + max(income - 132000, 0) * 0.40
  - saving: tax_without - tax_with
expected:
  tax_with: 9350
  tax_without: 14750
  saving: 5400
```

## When to refuse or refer

- Residence, domicile, remittance and source disputes; treaty claims.
- Foreign pensions and pension classification.
- Allowances beyond those listed (social security contributions, mortgage interest) until their conditions are read.
- Penalty computations: Cap. 17.01 and Cap. 17.26 provisions overlap (Cap. 17.26 s.4(2) gives the revenue law precedence).
- Any year after 2026 until later law and tables are checked.

## Filing and payment

1. Register for a TIN within 30 days of starting a covered activity (Cap. 17.26 ss.9 and 10).
2. File the individual return by the date for the branch (31 March generally; 28 February under s.43(4) for employment or pension income; 31 January per the rules and MCRS for the cases they name).
3. Pay the balance by 30 June or 45 days after the assessment is served (s.50(1)).
4. Keep records in Montserrat for 7 years from the transaction, or longer while the assessment time limit is open (Cap. 17.26 s.20).

## Completion checklist

- Residence and income charged settled.
- EC$18,000 deduction applied once, with the return completed.
- Bands applied as widths after the deduction; pension under Schedule 3.
- PAYE credited; return date chosen for the branch.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income and Corporation Tax Act Cap. 17.01, revised to 1 January 2025: read for ss.2 to 4 (residence, income, basic year), s.33 (EC$18,000 and dependant allowances), s.35 and Schedules 2 and 3 (bands and pension rates), s.43 (return dates), s.50 (payment), s.51(13) and the Income Tax Rules r.3 | https://www.gov.ms/wp-content/uploads/2026/02/17.01-Income-and-Incorporation-Tax-Act.pdf | 2026-11-14 |
| Income and Corporation Tax (Amendment) Act 20 of 2024: read for ss.3 and 4 inserting the EC$18,000 deduction and the 2024 bands | https://www.gov.ms/wp-content/uploads/2024/08/Act-No.-20-of-2024-Income-and-Corporation-Tax-Amendment-Act.pdf | 2026-11-14 |
| Tax Administration Act Cap. 17.26, revised to 1 January 2025: read for ss.4, 9, 10, 19, 20, 22, 45, 51 and 55 to 58 (TIN, records, filing rules, extension, 6% interest) | https://www.gov.ms/wp-content/uploads/2026/02/17.26-Tax-Administration-Act.pdf | 2026-11-14 |
| SRO 8/2026, Revised Edition of the Laws Order: read for the 2025 revised edition being authoritative from 23 February 2026 | https://www.gov.ms/wp-content/uploads/2026/02/SRO-No.-8-of-2026-Revised-Edition-of-the-Laws-Order-.pdf | 2026-11-11 |
| MCRS 2024 individual income tax return: read for the return method (deduction first, then the bands) | https://mcrs.ms/wp-content/uploads/2025/01/Individual-Income-Tax-Return-Form-2024.pdf | 2026-11-11 |
| MCRS individual tax information: read for the 31 January and 31 March return dates and the late filing penalty of up to EC$2,000 | https://mcrs.ms/individual-tax-information/ | 2026-11-14 |
| MCRS income tax calculator: read for the calculation that differs from Schedule 2 (36400 base in its code) | https://mcrs.ms/income-tax-calculator/ | 2026-11-14 |

Not yet confirmed: Acts and SROs after the 1 January 2025 revision (named exemptions and tax information exchange amendments are listed by the Attorney General; a full Gazette check is open); the operative return date for employment-only income; the conditions for the social security and mortgage interest allowances; the 2024 return form is scanned and its pages were read from Ryan Duguid's notes of 11 November 2026, not re-read here.
