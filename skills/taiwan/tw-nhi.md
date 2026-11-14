---
name: tw-nhi
description: Use this skill whenever asked about Taiwan National Health Insurance (NHI) contributions in 2026. Trigger on phrases like "NHI Taiwan", "健保", "全民健康保險", "健保費", "supplementary premium", "補充保費", "NHI self-employed", "health insurance Taiwan", "NHIA", "衛生福利部中央健康保險署", or any question about computing, paying, or understanding NHI premiums for employees and self-employed individuals in Taiwan. It covers the general premium formula, the 2026 insured amount floor (NT$29,500) and the NT$42,000 minimum for small employers and most self-employed, premium shares by category, the supplementary premium, payment and tax deductibility. Built from the law, not reviewed by an accountant.
version: "2.0"
jurisdiction: TW
tax_year: 2026
tax_year_notes: "Calendar 2026. Insured amount changes effective 1 January 2026 per the Ministry of Health and Welfare (MOHW) list of measures (data to 23 December 2025). The NHIA premium tables could not be opened in this pass (Cloudflare block); figures not on the MOHW list are under Not yet confirmed."
last_updated: 2026-11-14
depends_on:
  - tw-income-tax
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Taiwan National Health Insurance (全民健康保險) premiums, 2026

> **General reference only.** Built from the law, not reviewed by an accountant. Do not pay or take a position on it without review by a qualified professional in Taiwan.

## Who this applies to

Everyone in the NHI system: employees, employers and self-employed persons, professionals in their own practice, occupational union members, farmers and fishermen, and others. Governing law: National Health Insurance Act (全民健康保險法). Administrator: National Health Insurance Administration (NHIA, 衛生福利部中央健康保險署). Currency: NT$.

| Category | Who | Premium share (insured / employer / government) |
| --- | --- | --- |
| Category 1, employees | Employees of public and private employers | 30% / 60% / 10% |
| Category 1, employers, self-employed, independent professionals | Business owners, self-employed, professionals in their own practice | 100% / 0 / 0 |
| Category 2 | Occupational union members without a fixed employer | 60% / 0 / 40% |
| Category 3 | Farmers, fishermen | 30% / 0 / 70% |
| Category 6 and others | Veterans, low-income and other groups | Mostly government-subsidised |

The shares above are from the old file and the NHI Act (art. 27); the 30% employee and Category 3 shares match the MOHW premium figures in the rates table.

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Lowest insured amount (grade 1) | NT$29,500 a month | From 1 January 2026, following the minimum wage; revised 12 December 2025 | https://www.mohw.gov.tw/dl-98420-ec7a34cc-eb53-400d-9610-ac2001b76ea7.html |
| Category 3 insured amount | NT$29,500 (from 28,590) | Farmers and fishermen; own premium NT$458 a month (from 443) | same |
| Minimum insured amount, small employers and most self-employed | NT$42,000 a month (from 40,100) | Owners of businesses with fewer than 5 insured staff, self-employed in Category 1, and professionals in own practice other than CPAs, lawyers, architects, doctors, dentists and Chinese-medicine doctors; must not be below the highest amount declared for their staff | same |
| Own premium at NT$42,000 | NT$2,171 a month (from 2,073) | Insured person alone, 100% share | same |
| General premium rate | 5.17% | Matches the MOHW figures: 42,000 x 5.17% = 2,171; 29,500 x 5.17% x 30% = 458 | same |

## The base

### General premium (一般保險費)

Monthly premium = insured amount x 5.17% x (1 + number of dependants, up to 3 counted) x share for the category. Each person's premium is computed and rounded separately. Employees: 30%; employer pays 60% under its own formula. Self-employed and employers: 100%. Union members: 60%.

**Insured amount.** Employees: the grade for their monthly salary on the NHIA grade table (lowest 29,500 in 2026). Small employers and most self-employed: at least 42,000 and not less than the highest amount declared for any of their staff. CPAs, lawyers, architects, doctors, dentists and Chinese-medicine doctors in their own practice follow a different minimum (not restated here). Employers with 5 or more insured staff declare by actual income (rules not restated). The old file's other self-declaration rules (average Category 1-3 amount of NT$38,200; grade 6 NT$33,300 for small professionals; top grade NT$219,500) are pre-2026 figures and not confirmed.

### Supplementary premium (補充保險費)

A supplementary premium is withheld at source on certain income that is not part of the insured amount: bonuses above four times the monthly insured amount in the year, part-time salary from a non-primary employer, professional practice fees, dividends, interest and rent above per-payment thresholds. Exemptions include salary from the primary employer (already in the general premium) and certain low-income households. The rate, thresholds and per-payment cap are under Not yet confirmed (old file: 2.11%; threshold NT$28,590 for every item; cap on NT$10,000,000 a payment).

### Tax deductibility

NHI general premiums are deductible without limit as an itemised deduction on the individual return; other personal insurance premiums are capped at NT$24,000 per person (`tw-income-tax`). eFiling pre-fills the premiums. If the standard deduction is taken, NHI premiums are not deducted separately.

## Deadlines and filing

| Item | Detail |
| --- | --- |
| Registration | Through the employer (投保單位), the local NHIA office or professional association for the self-employed, an occupational union (Category 2) or the township office |
| New business | Register with the NHIA promptly on starting (old file: within 30 days; not confirmed) |
| Payment of general premium | Monthly, for the previous month (old file: by the last day of the following month; not confirmed) |
| Supplementary premium | Withheld by the payer and remitted to the NHIA (timing not confirmed) |
| Payment methods | Bank auto-debit, convenience stores, post office, online banking, the NHI Express app, credit card |

## Penalties and interest

Late premiums attract a late fee under the NHI Act (old file: 0.1% a day, up to 15%; not confirmed). Unpaid premiums can lead to suspension of benefits until arrears are paid (emergency care remains). Overseas: an insured person leaving Taiwan for more than six months may apply to suspend NHI (停保); rules on return are not restated here.

## Cross-border points

- Foreign residents with an Alien Resident Certificate join NHI as employees from the first day of employment, or after a waiting period otherwise (period not confirmed here).
- Dual status (employee and self-employed): insured once, under the primary status; supplementary premium still applies to non-primary income.
- Up to three dependants are counted in the premium; further dependants register under another insured family member.

## Two worked examples that recompute

**Example 1: self-employed freelancer at the 2026 minimum, with spouse and child.** Insured amount 42,000. Own premium: 42,000 x 5.17% = 2,171.4, rounded to NT$2,171. Each dependant pays the same: 2,171 x 3 = NT$6,513 a month; NT$78,156 a year.

```oa-check
name: TW 2026 self-employed NHI at NT$42,000, two dependants
inputs:
  insured: 42000
  people: 3
steps:
  - own: round(insured * 0.0517, 0)
  - monthly: own * people
  - annual: monthly * 12
expected:
  own: 2171
  monthly: 6513
  annual: 78156
```

**Example 2: farmer at the 2026 floor (Category 3, 30% share).** 29,500 x 5.17% x 30% = 457.55, rounded to NT$458 a month, as published by the MOHW. Correction: the old file's floor of 28,590 (premium 443) is the 2025 figure.

```oa-check
name: TW 2026 Category 3 NHI premium at the floor
inputs:
  insured: 29500
steps:
  - premium: round(insured * 0.0517 * 0.30, 0)
  - old_premium: round(28590 * 0.0517 * 0.30, 0)
  - increase: premium - old_premium
expected:
  premium: 458
  old_premium: 443
  increase: 15
```

## Ask the client first

1. Category: employee, employer, self-employed, professional in own practice, union member.
2. Number of insured staff (fewer than 5 triggers the 42,000 minimum for the owner).
3. Monthly salary or declared income; highest amount declared for staff.
4. Dependants registered (up to 3 counted).
5. Bonuses, part-time pay, professional fees, dividends, interest or rent received (supplementary premium).
6. Periods abroad (suspension).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| MOHW, January 2026 list of new measures (PDF). Read for the 29,500 floor, the Category 3 premium 443 to 458, and the small employer and self-employed minimum 40,100 to 42,000 with premium 2,073 to 2,171 | https://www.mohw.gov.tw/dl-98420-ec7a34cc-eb53-400d-9610-ac2001b76ea7.html | 2026-11-14 |
| NHIA premium table for employers, self-employed and professionals effective 1 January 2026. Not read: the page returned a Cloudflare challenge (HTTP 403) to curl, WebFetch and web.archive.org | https://www.nhi.gov.tw/ch/cp-19439-f2f35-2580-1.html | 2026-11-14 |

Not yet confirmed: the 2026 top insured amount (a search result said NT$313,000 from 1 January 2025; old file NT$219,500) and the full grade table; the supplementary premium rate (old file 2.11%), thresholds (old file NT$28,590 for every item; likely different for professional fees, dividends, interest and rent) and per-payment cap; the employer share formula and average dependants factor (old file 0.56); late fee rates; payment due dates; registration time limits; the minimum for CPAs, lawyers, architects and doctors in own practice; the old maximum premium example (NT$45,393 a month), which used the 2025 top grade.
