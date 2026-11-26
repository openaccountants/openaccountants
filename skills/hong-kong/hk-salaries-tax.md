---
name: hk-salaries-tax
description: Use this skill whenever asked about Hong Kong salaries tax for the year of assessment 2026/27 (1 April 2026 to 31 March 2027). Trigger on phrases like "Hong Kong tax", "salaries tax", "BIR60", "IRD", "net chargeable income", "standard rate", "progressive rate HK", "personal allowance Hong Kong", "provisional tax HK", "tax return Hong Kong", or any question about computing, filing, or planning salaries tax for an individual in Hong Kong. It covers the progressive and standard rate calculations, the 2026/27 allowances (basic HKD 145,000), deductions, provisional tax and BIR60 filing. Built from the law, not reviewed by an accountant.
version: "2.1"
jurisdiction: HK
tax_year: 2026
tax_year_notes: "Year of assessment 2026/27, the year containing most of 2026. Allowances from the 2026-27 Budget (enacted, gazetted 22 May 2026). Filing dates are the 2025/26 cycle (BIR60 issued 4 May 2026)."
last_updated: 2026-11-26
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
| Progressive rate, first HKD 50,000 | 2% | Net chargeable income, after deductions and allowances | https://www.ird.gov.hk/eng/pdf/pam61e.pdf |
| Next HKD 50,000 | 6% | Same | same |
| Next HKD 50,000 | 10% | Same | same |
| Next HKD 50,000 | 14% | Same | same |
| Remainder | 17% | Same | same |
| Standard rate, first HKD 5,000,000 of net income | 15% | YA 2024/25 onwards | same |
| Standard rate, net income above HKD 5,000,000 | 16% | Same | same |
| Basic allowance | HKD 145,000 | From YA 2026/27 (2025/26: 132,000) | https://www.ird.gov.hk/eng/tax/budget.htm |
| Married person's allowance | HKD 290,000 | From YA 2026/27 (2025/26: 264,000) | same |
| Single parent allowance | HKD 145,000 | From YA 2026/27. The claimant must qualify for child allowance and provide day-to-day care and supervision. Financial support alone is insufficient | same |
| Child allowance, 1st to 9th child | HKD 140,000 each | From YA 2026/27 (2025/26: HKD 130,000). Check the unmarried-child, age, education or incapacity and maintenance conditions | same |
| Additional child allowance | HKD 140,000 on top of the basic child allowance for each eligible year | From YA 2026/27. Apply the under-2 test at the end of the year and the transitional birth-date rule for children born from 1 April 2025 | same |
| Dependent parent or grandparent, aged 60 or older or eligible for Disability Allowance | HKD 55,000 | From YA 2026/27. Ordinary Hong Kong residence and maintenance required. An extra HKD 55,000 applies where the dependant lives with the taxpayer throughout the year without paying full cost | same |
| Dependent parent or grandparent, aged 55 to 59 | HKD 27,500 | From YA 2026/27. Same ordinary residence and maintenance conditions. An extra HKD 27,500 applies where the dependant lives with the taxpayer throughout the year without paying full cost | same |
| Elderly residential care expenses | Up to HKD 110,000 | From YA 2026/27. Qualifying costs actually paid, net of reimbursements. Check the age or disability and care-provider conditions. The same dependant cannot generate both claims in the same year | same |
| Dependent brother or sister allowance | HKD 37,500 | Ongoing care and supervision of an eligible unmarried sibling | https://www.ird.gov.hk/eng/pdf/pam61e.pdf |
| Personal disability allowance | HKD 75,000 | Eligible under the Government’s Disability Allowance Scheme | same |
| Disabled dependant allowance | HKD 75,000 each | Check the disability and applicable relationship or ordinary allowance conditions | same |
| MPF mandatory contributions deduction | Up to HKD 18,000 | Qualifying mandatory contributions paid by the taxpayer | same |
| Self-education expenses | Up to HKD 100,000 | Prescribed courses and examinations | same |
| Home loan interest, basic deduction | Up to HKD 100,000 | Qualifying interest on a Hong Kong home used as the taxpayer’s residence. Up to 20 years of assessment | https://www.ird.gov.hk/eng/faq/adc.htm |
| Home loan interest or domestic rent, with additional deduction | Up to HKD 120,000 | From YA 2024/25. Elect for the additional amount under the residence and child conditions. The additional home loan interest deduction is limited to 19 years of assessment | same |
| Domestic rent, basic deduction | Up to HKD 100,000 | Qualifying stamped tenancy on a Hong Kong residence under IRO Part 4A Div 8. Prorate or apportion if required. See the spouse and housing exclusions below | https://www.ird.gov.hk/eng/tax/drd.htm |
| Qualifying VHIS premiums | Up to HKD 8,000 per insured person | For a qualifying policy on the taxpayer or a specified relative | https://www.ird.gov.hk/eng/pdf/pam61e.pdf |
| QDAP and tax-deductible MPF voluntary contributions | Up to HKD 60,000 combined | Claim eligible TVC first and qualifying annuity premiums second | same |
| Approved charitable donations | Up to 35% of income | After allowable outgoings, expenses and depreciation allowances. At least HKD 100 in aggregate | same |
| Rental value of quarters, flat or serviced apartment | Generally 10% | Apply the percentage to employer and associated-company income net of qualifying outgoings and expenses, excluding self-education expenses from those deductions. Subtract any rent the employee pays. The employee may elect for rateable value where applicable | https://www.ird.gov.hk/eng/tax/ere_house.htm |
| Rental value, hotel, hostel or boarding house | 8% for 2 rooms or 4% for 1 room | Same income base. Count the rooms the employer provides | same |
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
| Housing provided by the employer | Add the taxable rental value calculated using the table above. Cash housing allowances generally enter assessable income directly |
| Share options and awards | Options are generally taxed on exercise, assignment or release. Check the award terms to determine when a share award is taxable, generally at vesting. A gain may remain taxable after employment ends |
| Employer MPF mandatory contributions | Not assessable |
| Reimbursed expenses wholly for business | Not assessable |
| Education benefit for children | Assessable as a perquisite |
| Severance or long service payment | Exempt up to the statutory entitlement |

### Deductions (IRO s. 12 and Part 4A)

Order of work: total assessable income, less deductions (MPF mandatory, self-education, donations, elderly care, home loan interest, VHIS, QDAP and TVC, domestic rent) = **net income** (used for the standard rate); less allowances = **net chargeable income** (used for the progressive rates). Tax payable is the lower of the two results. The elderly residential care deduction and the dependent parent allowance cannot both be claimed for the same parent in the same year.

### Worksheet

A. Assessable income: salary, bonus, rental value of quarters, share gains, other perquisites. B. Deductions: MPF (max 18,000), self-education (max 100,000), donations (max 35%), home loan interest (max 100,000, or 120,000 with the additional deduction), QDAP plus TVC (max 60,000), VHIS (max 8,000 per person), domestic rent (max 100,000, or 120,000), elderly care (max 110,000). C. Net income = A less B. D. Allowances. E. Net chargeable income = C less D. F. Progressive tax on E; standard rate on C; tax = lower. G. Less any one-off reduction for the year. H. Provisional tax adjustments.

### Special situations

- **Employment partly outside Hong Kong.** For a non-Hong Kong employment, ordinarily tax income attributable to Hong Kong services. Under ss. 8(1A)(b)(ii) and 8(1B), qualifying Hong Kong visits totalling no more than 60 days are disregarded when testing whether all services were rendered outside Hong Kong. This can apply to a Hong Kong employment too. Check whether the stays are visits and whether an exclusion applies, including government employees and ship or air crew.
- **Lump sums.** Employment gratuities and remuneration can be assessable. Statutory severance and long service payments are exempt to the extent provided by the IRO. For other termination payments, identify whether they remunerate employment or compensate for lost employment rights. Recognised scheme lump sums have separate conditions.
- **Personal assessment (IRO s. 41).** An eligible taxpayer who elects may set off business losses against other income. Mortgage interest against let-property income has its own test. Compare an eligible joint election with separate outcomes for a married couple.
- **Married couples.** Calculate the available separate and joint outcomes using the relevant salaries tax or personal assessment rules. The married person’s allowance may apply when a spouse has no assessable income or when the couple is jointly assessed.
- **Domestic rent deduction (from YA 2022/23).** A married couple living together shares one ceiling for the same period, including under joint assessment. A taxpayer and spouse living together cannot both claim different premises for the same period. Check the stamped tenancy, ownership, related landlord, employer-provided housing and public housing conditions.

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
| Due date | For the YA 2025/26 cycle, ordinary BIR60 filing was due 4 June 2026, or 4 August for taxpayers who wholly owned an unincorporated business. IRD allowed an automatic month for ordinary e-filing. Represented cases under the block arrangement had deadlines of 4 July 2026 or 5 October 2026 if sole proprietorship accounts were included |
| Signature | Sign the paper return or use the authorised electronic signing procedure |
| Provisional salaries tax | Generally based on the year just assessed. Credit provisional tax against the final liability for the same year of assessment. The demand note specifies the amounts and due dates for each instalment |
| Holdover of provisional tax | One ground is actual or expected net chargeable income below 90% of the prior year’s net chargeable income or the estimate used to charge provisional tax. Apply by 28 days before the due date or 14 days after issue of the notice, whichever is later |
| Objection | The IRD must receive a written objection stating the grounds within one month after the date of the assessment notice. For an estimated assessment under s. 59(3), also submit the completed return. The tax remains payable unless held over |

**Key dates (typical year).** 1 April: YA starts. Early May: BIR60 issued. June to July: filing. Later in the year to early the next year: notices of assessment and the first provisional tax instalment. 31 March: YA ends.

## Penalties and interest

| Offence | Penalty |
| --- | --- |
| Late or no return, incorrect return, failure to notify chargeability, without reasonable excuse (s. 80(2)) | Fine of HKD 10,000 plus treble the tax undercharged; or additional tax up to treble under s. 82A |
| Wilful evasion (s. 82) | Fine of HKD 50,000, treble the tax undercharged and up to 3 years' imprisonment |
| Late payment | An initial surcharge of up to 5% of unpaid tax. After 6 months in default a further 10% can apply to the unpaid balance, including the first surcharge |

## Cross-border points

- Identify the employment source and Hong Kong services before applying the cross-border exemption and any treaty relief.
- For a chargeable employee leaving Hong Kong for more than one month, the employer generally files IR56G and the employee generally tells IRD at least one month before departure. The employer withholds money due for one month from notice or until earlier written release by IRD. Check the exception for frequent departures required by the employment.
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

**Married taxpayer with two qualifying children.** Salary HKD 1,200,000 and spouse with no assessable income. Assume HKD 18,000 qualifying mandatory MPF and neither child qualifies for an additional child allowance. Net income is HKD 1,182,000. Deduct HKD 290,000 married person’s allowance and HKD 280,000 child allowances to give net chargeable income of HKD 612,000. Progressive tax is HKD 16,000 + 17% × HKD 412,000 = HKD 86,040. Standard tax is HKD 177,300. Final salaries tax is HKD 86,040 before any provisional credit.

**Example 2: dependent parent allowance or elderly residential care deduction.** A single taxpayer with HKD 800,000 net income before the care deduction pays HKD 80,000 of unreimbursed eligible fees to a qualifying Hong Kong care home for their 80-year-old mother. Assume the mother is ordinarily resident in Hong Kong and meets the maintenance test for the parent allowance. With the HKD 55,000 parent allowance, progressive tax is HKD 84,000. With the HKD 80,000 care deduction, within the HKD 110,000 cap, progressive tax is HKD 79,750. Progressive tax is lower than standard under both options. The care deduction therefore saves HKD 4,250 more. An eligible dependant who lived with the taxpayer throughout the year could instead attract a combined HKD 110,000 parent allowance.

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
  - tax_a: min(16000 + (nci_a - 200000) * 0.17, net_income * 0.15)
  - tax_b: min(16000 + (nci_b - 200000) * 0.17, (net_income - min(care_cost, 110000)) * 0.15)
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
| IRD, rates, allowances and deductions for YA 2026/27 | https://www.ird.gov.hk/eng/pdf/pam61e.pdf | 2026-11-26 |
| IRD, domestic rent deduction and the married couple ceiling | https://www.ird.gov.hk/eng/tax/drd.htm | 2026-11-26 |
| IRD, conditions and periods for additional home loan interest and domestic rent deductions | https://www.ird.gov.hk/eng/faq/adc.htm | 2026-11-26 |
| IRD, housing benefits and rental value | https://www.ird.gov.hk/eng/tax/ere_house.htm | 2026-11-26 |
| IRD, Practice Note 10 on territorial employment income and the 60-day test | https://www.ird.gov.hk/eng/pdf/dipn10.pdf | 2026-11-26 |
| IRD, salaries tax on severance and long service payments | https://www.ird.gov.hk/eng/tax/abo_offset.htm | 2026-11-26 |
| IRD, practice note 57 on eligible TVC and QDAP deductions | https://www.ird.gov.hk/eng/pdf/dipn57.pdf#page=26 | 2026-11-26 |
| IRD, employer notification and withholding on departure | https://www.ird.gov.hk/eng/tax/ere_obl.htm | 2026-11-26 |
| IRD, BIR60 filing deadlines for YA 2025/26 | https://www.ird.gov.hk/eng/tax/ind_rem.htm | 2026-11-26 |
| IRD, specimen assessment and objection time limit | https://www.ird.gov.hk/eng/pdf/irc6401e.pdf | 2026-11-26 |
| IRD, application for provisional tax holdover | https://www.ird.gov.hk/eng/faq/hpt.htm | 2026-11-26 |
| IRD, late payment surcharges in the recovery chapter | https://www.ird.gov.hk/eng/pdf/2026/BriefGuide20252026.pdf#page=37 | 2026-11-26 |

Not yet confirmed: the exact YA 2026/27 BIR60 issue date, any new one-off tax reduction for YA 2026/27 and enactment of the proposed HKD 160,000 child and additional child allowances. Check each demand notice for actual instalment amounts and due dates.
