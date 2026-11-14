---
name: hk-salaries-tax
description: Use this skill whenever asked about Hong Kong salaries tax for the year of assessment 2026/27 (1 April 2026 to 31 March 2027). Trigger on phrases like "Hong Kong tax", "salaries tax", "BIR60", "IRD", "net chargeable income", "standard rate", "progressive rate HK", "personal allowance Hong Kong", "provisional tax HK", "tax return Hong Kong", or any question about computing, filing, or planning salaries tax for an individual in Hong Kong. It covers the progressive and standard rate calculations, the 2026/27 allowances (basic HKD 145,000), deductions, provisional tax and BIR60 filing. Built from the law, not reviewed by an accountant.
version: "2.0"
jurisdiction: HK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27, the year containing most of 2026. Allowances from the 2026-27 Budget (enacted, gazetted 22 May 2026). Filing dates are the 2025/26 cycle (BIR60 issued 4 May 2026)."
last_updated: 2026-11-14
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Hong Kong salaries tax (薪俸稅), year of assessment 2026/27

> **General reference only.** Built from the law, not reviewed by an accountant. Do not file, pay or take a tax position on it without review by a qualified professional in Hong Kong.

## Who this applies to

Salaries tax is charged on every person on income arising in or derived from Hong Kong from an office or employment, or a pension (Inland Revenue Ordinance (IRO), Cap. 112, s. 8). Year of assessment (YA) 2026/27 runs 1 April 2026 to 31 March 2027. Currency: HKD only. Tax authority: Inland Revenue Department (IRD); filing through eTAX.

**Method.** Salaries tax is the LOWER of (1) the progressive rates on net chargeable income (after deductions AND allowances) and (2) the standard rate on net income (after deductions but BEFORE allowances).

Out of scope: profits tax (`hk-corporate-income-tax`), MPF contribution rules (`hk-mpf`), property tax (`hong-kong-tax`).

## Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Progressive rate, first HKD 50,000 | 2% | Net chargeable income; YA 2020/21 onwards | https://www.gov.hk/en/residents/taxes/taxfiling/taxrates/salariesrates.htm |
| Next HKD 50,000 | 6% | Same | same |
| Next HKD 50,000 | 10% | Same | same |
| Next HKD 50,000 | 14% | Same | same |
| Remainder | 17% | Same | same |
| Standard rate, first HKD 5,000,000 of net income | 15% | YA 2024/25 onwards | same |
| Standard rate, net income above HKD 5,000,000 | 16% | Same | same |
| Basic allowance | HKD 145,000 | From YA 2026/27 (2025/26: 132,000) | https://www.ird.gov.hk/eng/tax/budget.htm |
| Married person's allowance | HKD 290,000 | From YA 2026/27 (2025/26: 264,000) | same |
| Single parent allowance | HKD 145,000 | From YA 2026/27 | same |
| Child allowance, 1st to 9th child | HKD 140,000 each | From YA 2026/27 (2025/26: 130,000) | same |
| Additional child allowance, newborn | HKD 140,000 each year for the first two years | From YA 2026/27 (period extended from one to two years; HKD 280,000 in total) | same |
| Dependent parent or grandparent, aged 60 or above (or on Disability Allowance) | HKD 55,000 | From YA 2026/27; additional HKD 55,000 if living with the taxpayer all year | same |
| Dependent parent or grandparent, aged 55 to 59 | HKD 27,500 | From YA 2026/27; additional HKD 27,500 if living together all year | same |
| Elderly residential care expenses | Up to HKD 110,000 | From YA 2026/27; excludes the parent allowance for the same person | same |
| Dependent brother or sister allowance | HKD 37,500 | 2025/26 onwards, not changed by the 2026-27 Budget | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf |
| Personal disability allowance | HKD 75,000 | Same | same |
| Disabled dependant allowance | HKD 75,000 each | Same | same |
| MPF mandatory contributions deduction | Up to HKD 18,000 | 2019/20 onwards | same |
| Self-education expenses | Up to HKD 100,000 | Prescribed courses and examinations | same |
| Home loan interest, basic deduction | Up to HKD 100,000 | Hong Kong home used as residence; 20 years of assessment | same |
| Home loan interest or domestic rent, with additional deduction | Up to HKD 120,000 | From YA 2024/25 where the prescribed conditions (child) are met | same |
| Domestic rent, basic deduction | Up to HKD 100,000 | Hong Kong residence, conditions in s. 26J | same |
| Qualifying VHIS premiums | Up to HKD 8,000 per insured person | 2019/20 onwards | same |
| QDAP and tax-deductible MPF voluntary contributions | Up to HKD 60,000 combined | Same | same |
| Approved charitable donations | Up to 35% of income | After allowable expenses and depreciation | same |
| Rental value of quarters, flat or serviced apartment | 10% of total income | Employer-provided residence; may elect rateable value | same |
| Rental value, hotel, hostel or boarding house | 8% (up to 2 rooms) or 4% (1 room) | Same | same |
| One-off reduction, YA 2025/26 final tax | 100%, capped at HKD 3,000 | Per taxpayer (per couple if jointly assessed); not for 2026/27 | https://www.ird.gov.hk/eng/tax/budget.htm |
| BIR60 for 2025/26 | Issued 4 May 2026 | Represented taxpayers: 4 July 2026, or 5 October 2026 with sole proprietorship accounts | https://www.ird.gov.hk/eng/pdf/bel26e.pdf |

**Proposed, not yet law (2026 Policy Address):** child allowance and the newborn additional allowance raised from HKD 140,000 to HKD 160,000 for second and later children born on or after 16 September 2026, from YA 2026/27, after legislation. Do not apply until enacted.

## The base

### Assessable income

| Component | Treatment |
| --- | --- |
| Salary, wages, commission | Fully assessable |
| Bonus (discretionary or contractual) | Fully assessable |
| Leave pay, end-of-contract gratuity | Assessable (time-apportioned if partly Hong Kong service) |
| Housing provided by the employer | Add rental value: 10% of net income for a flat; 8% or 4% for a hotel, hostel or boarding house |
| Share options and awards | Assessable gain on exercise or vesting; still taxable after the employment ends |
| Employer MPF mandatory contributions | Not assessable |
| Reimbursed expenses wholly for business | Not assessable |
| Education benefit for children | Assessable as a perquisite |
| Severance or long service payment | Exempt up to the statutory entitlement |

### Deductions (IRO s. 12 and Part 7)

Order of work: total assessable income, less deductions (MPF mandatory, self-education, donations, elderly care, home loan interest, VHIS, QDAP and TVC, domestic rent) = **net income** (used for the standard rate); less allowances = **net chargeable income** (used for the progressive rates). Tax payable is the lower of the two results. The elderly residential care deduction and the dependent parent allowance cannot both be claimed for the same parent in the same year.

### Worksheet

A. Assessable income: salary, bonus, rental value of quarters, share gains, other perquisites. B. Deductions: MPF (max 18,000), self-education (max 100,000), donations (max 35%), home loan interest (max 100,000, or 120,000 with the additional deduction), QDAP plus TVC (max 60,000), VHIS (max 8,000 per person), domestic rent (max 100,000, or 120,000), elderly care (max 110,000). C. Net income = A less B. D. Allowances. E. Net chargeable income = C less D. F. Progressive tax on E; standard rate on C; tax = lower. G. Less any one-off reduction for the year. H. Provisional tax adjustments.

### Special situations

- **Employment partly outside Hong Kong:** income is time-apportioned by Hong Kong days where the employment is non-Hong Kong. The old file's visit exemption for short stays is on the Not yet confirmed line: do not apply it.
- **Lump sums (s. 11D):** gratuity or severance connected with Hong Kong employment is assessable; a recognised retirement scheme lump sum is exempt if conditions are met; a golden handshake is assessable.
- **Personal assessment (IRO s. 41):** lets an individual set off business losses against salaries income, claim home loan interest against other income and pool a married couple's income for the progressive rates.
- **Married couples:** joint assessment helps when one spouse has low or no income (allowances pooled); separate taxation helps when both are high earners on the standard rate; personal assessment (joint) for business losses or mortgage interest.
- **Domestic rent deduction (from 2022/23):** taxpayer not provided with quarters; property not owned by the taxpayer or a connected person; tenancy stamped. Each spouse claims up to the cap on separate tenancies; total up to twice the cap on joint assessment.

### Conservative defaults

| Ambiguity | Default |
| --- | --- |
| Unknown marital status | Apply the basic allowance (HKD 145,000) only |
| Unknown whether children qualify | Do not claim child allowance |
| Unknown dependent parent arrangement | Do not claim the additional (living together) allowance |
| MPF deduction | Cap at HKD 18,000 |
| Progressive or standard lower | Calculate both; apply the lower |
| One-off reduction | None for 2026/27 unless announced; 2025/26: 100% capped at HKD 3,000 |
| 2026 Policy Address child allowance increase | Do not apply until enacted |

### Recent one-off reductions

| Year of assessment | Reduction | Ceiling |
| --- | --- | --- |
| 2022/23 | 100% | HKD 6,000 |
| 2023/24 | 100% | HKD 3,000 |
| 2024/25 | 100% | HKD 1,500 |
| 2025/26 | 100% | HKD 3,000 (enacted 22 May 2026) |

## Deadlines and filing

| Item | Detail |
| --- | --- |
| Form | BIR60 (個別人士報稅表) |
| Issue | Bulk issue early May (4 May 2026 for 2025/26; 2026/27 returns in May 2027) |
| Due date | Normally one month from issue; e-filing gets a further month; represented taxpayers 4 July 2026, or 5 October 2026 with sole proprietorship accounts (2025/26) |
| Signature | Taxpayer (paper), or eTAX login |
| Provisional salaries tax | Charged with the final assessment, based on the year just assessed; applied against the next year's final tax |
| Holdover of provisional tax | If income is expected to fall by more than 10% (or on other grounds); apply not later than 28 days before the due date or 14 days after the notice is issued, whichever is later |
| Objection | Written notice to the Assessor stating the grounds; the time limit (IRO s. 64) is on the Not yet confirmed line, so object as soon as the notice of assessment arrives |

**Key dates (typical year).** 1 April: YA starts. Early May: BIR60 issued. June to July: filing. Later in the year to early the next year: notices of assessment and the first provisional tax instalment. 31 March: YA ends.

## Penalties and interest

| Offence | Penalty |
| --- | --- |
| Late or no return, incorrect return, failure to notify chargeability, without reasonable excuse (s. 80(2)) | Fine of HKD 10,000 plus treble the tax undercharged; or additional tax up to treble under s. 82A |
| Wilful evasion (s. 82) | Fine of HKD 50,000, treble the tax undercharged and up to 3 years' imprisonment |
| Late payment | 5% surcharge on the whole balance of the demand notice; any further surcharge is on the Not yet confirmed line, do not apply it |

## Cross-border points

- Only Hong Kong-sourced employment income is charged; a non-Hong Kong employment is taxed on Hong Kong-day services.
- Employees leaving Hong Kong: the employer must notify the IRD at least one month before the employee leaves and withhold money due to the employee for one month after the notice; the employee leaving for more than one month must notify at least one month before departure.
- Double taxation arrangements (including with the Mainland) may give relief; Mainland liability of Mainland-domiciled individuals continues (`china-to-singapore-relocation-tax` explains domicile).

## Two worked examples that recompute

**Example 1: single employee, YA 2026/27.** Salary HKD 600,000 plus bonus 50,000 = 650,000. MPF mandatory 18,000. Net income 632,000. Less basic allowance 145,000: net chargeable income 487,000. Progressive: 16,000 on the first 200,000 plus 17% of 287,000 (48,790) = HKD 64,790. Standard: 15% of 632,000 = 94,800. Tax payable: HKD 64,790. (Under the old 2024/25 figures the old file showed 67,000 less a 1,500 reduction.)

```oa-check
name: HK 2026/27 single employee, salary plus bonus HKD 650,000
inputs:
  income: 650000
  mpf: 18000
  basic: 145000
steps:
  - net_income: income - min(mpf, 18000)
  - nci: net_income - basic
  - progressive: 16000 + (nci - 200000) * 0.17
  - standard: net_income * 0.15
  - tax: min(progressive, standard)
expected:
  net_income: 632000
  nci: 487000
  progressive: 64790
  standard: 94800
  tax: 64790
```

**Married with two children (not an oa-check).** Salary 1,200,000, spouse no income. Net income 1,182,000; married person's allowance 290,000; two children 280,000; net chargeable income 612,000. Progressive: 16,000 + 17% of 412,000 (70,040) = 86,040. Standard: 177,300. Tax: HKD 86,040.

**Example 2: decision, dependent parent allowance or elderly residential care deduction.** A single taxpayer with net income of HKD 800,000 pays HKD 80,000 to a licensed care home for a mother aged 80, who therefore does not live with the taxpayer. Option A, dependent parent allowance: 55,000 (no additional allowance). Option B, elderly residential care deduction: 80,000 (within the 110,000 cap). Both reduce income taxed at 17%. Option B saves 17% of 25,000 = HKD 4,250 more. The deciding figure is the care home cost against the allowance (55,000, or 110,000 if the parent lived with the taxpayer all year).

```oa-check
name: HK 2026/27 parent allowance vs elderly care deduction
inputs:
  net_income: 800000
  basic: 145000
  allowance: 55000
  care_cost: 80000
steps:
  - nci_a: net_income - basic - allowance
  - nci_b: net_income - min(care_cost, 110000) - basic
  - tax_a: 16000 + (nci_a - 200000) * 0.17
  - tax_b: 16000 + (nci_b - 200000) * 0.17
  - saving: tax_a - tax_b
expected:
  nci_a: 600000
  nci_b: 575000
  tax_a: 84000
  tax_b: 79750
  saving: 4250
```

## Ask the client first

1. Employment: Hong Kong or non-Hong Kong employment, days in Hong Kong, and all income components for 1 April 2026 to 31 March 2027.
2. Marital status and spouse's income (joint assessment or separate).
3. Children (ages, births since 2025) and dependent parents or grandparents (ages, living together, care home).
4. Deductible payments: MPF, self-education, home loan interest or rent, VHIS, QDAP, TVC, donations.
5. Housing provided by the employer.
6. Provisional tax already charged and whether a holdover applies.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| GovHK, tax rates of salaries tax and personal assessment. Read for the progressive bands and the 15% and 16% standard rates | https://www.gov.hk/en/residents/taxes/taxfiling/taxrates/salariesrates.htm | 2026-11-14 |
| IRD, 2026-27 Budget tax measures. Read for the YA 2026/27 allowances, the 110,000 elderly care cap, the two-year newborn allowance and the YA 2025/26 reduction | https://www.ird.gov.hk/eng/tax/budget.htm | 2026-11-14 |
| IRD, 2026 Policy Address tax measures. Read for the proposed 160,000 child allowance (not yet enacted) | https://www.ird.gov.hk/eng/tax/policyaddress2026.htm | 2026-11-14 |
| IRD, A brief guide to taxes 2025/26 (PDF). Read for the other allowances, deduction caps, rental value percentages, provisional tax and holdover, departure notices | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf | 2026-11-14 |
| IRD, block extension letter for 2025/26 (PDF). Read for the BIR60 issue and extended dates | https://www.ird.gov.hk/eng/pdf/bel26e.pdf | 2026-11-14 |
| IRD penalty policy. Read for ss. 80(2), 82 and 82A | https://www.ird.gov.hk/eng/pol/ppo.htm | 2026-11-14 |
| GovHK, consequence of not paying tax on time. Read for the 5% surcharge | https://www.gov.hk/en/residents/taxes/taxfiling/consequences/consequencenotpaytax.htm | 2026-11-14 |

Not yet confirmed: the 60-day visit exemption for non-Hong Kong employment; the further 10% surcharge; the one-month objection period (IRO s. 64 not opened); the split of provisional tax instalments (old file said 75% in January and 25% in April); the 2026/27 BIR60 issue date (May 2027); the 2026 Policy Address child allowance of HKD 160,000 (pending legislation).
