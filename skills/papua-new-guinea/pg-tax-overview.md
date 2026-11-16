---
name: pg-tax-overview
description: >
  Route a 2026 Papua New Guinea tax question to the income-tax, corporate, payroll, GST or formation skill. Distinguish resident annual tax, final employment withholding, small business tax, company exceptions and temporary GST relief. Headline figures are sourced; unresolved inputs remain in the detailed skills rather than being assumed.
jurisdiction: PG
category: international
tax_year: 2026
last_updated: 2026-11-16
version: 1.0
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: rates-card
---

# Papua New Guinea tax overview v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Rates, bands and thresholds

For the 2026 calendar tax year, PNG income tax is governed by the Income Tax Act 2025 and its enacted budget amendment. The Internal Revenue Commission administers it. Currency is the Papua New Guinea kina, PGK. This overview selects the correct detailed skill; it is not a universal return-preparation or treaty-rate table.

| Topic | Key rule and conditions | Official source |
|---|---|---|
| Tax year | 1 January to 31 December for the fiscal year; approved company accounting years have separate rules | [Income Tax Act definitions and s. 42](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf); [Finance Department FMM 03.7](https://www.finance.gov.pg/wp-content/uploads/2026/04/FMM-03-07-Financial-Fiscal-Year.pdf) |
| Individual resident annual first band | PGK 20,000 at 0%; the old no-nil-band statement is wrong | [Sch. 1 Part I clause (1)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Individual non-resident annual first band | PGK 20,000 at 22%; residence must be established before selecting a table | [s. 10 and Sch. 1 Part I clause (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Top individual annual marginal rate | 42% above PGK 250,000 | [Sch. 1 Part I clauses (1), (2)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Ordinary company rate | 30%; banks, funds, projects and non-profits require their specific conditions | [s. 11 and Sch. 1 Part I clause (5)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Ordinary individual annual return | Within 3 months of tax-year end, subject to the statutory salary-only exemption and lawful extensions | [ss. 135-136](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Company annual return | Within 6 months, or 9 months when prepared by a registered tax agent | [s. 135](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| GST standard rate | 10%; distinguish exempt and zero-rated supplies | [IRC official GST factsheet](https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf) |
| Listed household-goods relief | Zero-rated from 1 June 2025 through 31 December 2026, under the specific product list, not all food or household purchases | [GST 2025 Budget amendment s. 2](https://static.irc.gov.pg/2025/January/mrifwz-media-goodsandserviceact2024.pdf); [2026 Budget amendment s. 2](https://pdis.parliament.gov.pg/uploads/953e2445-7185-4aa7-9d0f-0fcea47e75a9) |

### Choose the next skill

- **Employee, sole trader, resident status or annual individual return:** `pg-income-tax`. Test whether salary withholding is final and whether small business tax applies before ordinary annual rates. The payroll tax bands differ from annual bands.
- **Employer salary withholding or superannuation:** `pg-payroll-social`. Establish declarations, gross pay and contribution coverage. Unresolved pay-component and remittance-clock conflicts remain visible there.
- **Company income, PNG branch or non-resident payments:** `pg-corporate-income-tax`. A resident generally brings worldwide assessable income into tax, while a non-resident brings PNG-source assessable income. Exemptions, PE attribution, final non-resident tax and treaty conditions must still be tested. [Income Tax Act ss. 7-14 and 66-71](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).
- **GST classification and return:** `png-gst`. Confirm registration and assigned filing period; do not infer either from bank turnover. Standard-rate, zero-rated, exempt and outside-scope transactions have different input-credit consequences.
- **Entity choice and registration:** `pg-company-formation`. Incorporation, foreign-enterprise certification, tax registration and annual company maintenance are separate jobs.

### Ask before routing

Identify the person or entity, period, residence/source facts, activity, question and intended output. Read existing records before asking again. For a calculation, obtain the income or supply base, deductions, GST status, withholding and actual payments. Never treat an unknown jurisdiction, old-year return, resource agreement or missing input as an ordinary current-year case.

### Worked case: route and compute an ordinary resident annual band

A full-year resident consulting professional asks for ordinary annual tax on established taxable income of PGK 33,000, with no dependant or other credit. Load `pg-income-tax`; this is neither a company nor fortnightly SWT and professional services do not qualify for the small-business definition. The first annual band is nil and the next portion produces PGK 3,900. [ss. 11-12 and Sch. 1 annual bands](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG overview ordinary resident annual band
inputs:
  taxable_income: 33000
steps:
  - first_band: min(taxable_income,20000) * 0
  - next_band: max(min(taxable_income,33000)-20000,0) * 0.30
  - tax: first_band + next_band
expected:
  tax: 3900
```


### Boundaries

This is not full coverage of every PNG tax or regulatory obligation. Resource agreements, property stamp duty, treaty rates, current asset-allowance inputs, special benefits and unresolved administrative details must not be invented from the headline rates. Keep any held item in the detailed skill's source list and carry it into the working paper. No named accountant approval is added by this rewrite.

## Sources

Read on 16 November 2026. A scoped read does not certify every provision in a long Act.

| Official source and scope read | URL | Read on |
|---|---|---|
| Read for Finance Department FMM 03.7, current fiscal-year designation, whole one-page instruction | https://www.finance.gov.pg/wp-content/uploads/2026/04/FMM-03-07-Financial-Fiscal-Year.pdf | 2026-11-16 |
| Read for Income Tax Act 2025: definitions, residence/base, regime selection, company accounting year, ss. 135-138 and Schedule 1 headline figures | https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf | 2026-11-16 |
| Read for Income Tax 2026 Budget amendment, enacted commencement and changes | https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050 | 2026-11-16 |
| Read for IRC GST factsheet: standard rate and output/input mechanism | https://static.irc.gov.pg/2021/December/5ExWcL-media-GST-Section-65A-Fact-Sheet.pdf | 2026-11-16 |
| Read for GST 2025 Budget amendment, household-product list and extended-period conditions | https://static.irc.gov.pg/2025/January/mrifwz-media-goodsandserviceact2024.pdf | 2026-11-16 |
| Read for GST 2026 Budget amendment, relief extension to year-end | https://pdis.parliament.gov.pg/uploads/953e2445-7185-4aa7-9d0f-0fcea47e75a9 | 2026-11-16 |

Not yet confirmed: The detailed skills retain unconfirmed registration, regulatory uplift, superannuation component/remittance, wage, levy and special-case inputs. This overview does not turn those held items into confirmed country coverage.
