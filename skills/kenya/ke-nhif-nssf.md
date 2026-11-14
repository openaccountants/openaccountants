---
name: ke-nhif-nssf
description: Use this skill whenever asked about Kenyan social contributions for self-employed individuals -- SHIF (formerly NHIF) health insurance and NSSF pension. Trigger on phrases like "NHIF self-employed", "SHIF contributions", "NSSF Tier I", "NSSF Tier II", "Kenya social security", "Kenya health insurance", or any question about Kenyan social contribution obligations for self-employed persons. Covers the SHIF 2.75% rate (replacing NHIF brackets from October 2024), NSSF Tier I/II structure, voluntary registration, and edge cases. ALWAYS read this skill before touching any Kenyan social contribution work.
jurisdiction: KE
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
version: 2.2
type: computation
category: payroll
---

# Kenya self-employed SHIF and voluntary NSSF (2026) v2.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This skill distinguishes non-salaried household health insurance from voluntary self-employed pension contributions. Do not apply an employee's NSSF Tier I/II formula to voluntary membership or treat an individual's declared bank income as SHA's household means-test result. Employees and employers use [ke-payroll-paye-nssf-shif-ahl](ke-payroll-paye-nssf-shif-ahl.md), which owns current employee tiers and employer deadlines.

## Ask the client first

- Salaried, non-salaried, voluntary NSSF, or mixed employment/self-employment status.
- SHA registration, household members and the Authority's means-test income/contribution assessment.
- Coverage year, annual-expiry date, notices and any premium-financing arrangement.
- NSSF membership category, actual voluntary deposits, annual statement and formal-employment contributions.
- Residency/lawful residence, identity/PIN records and any claimed exemption or financial assistance.
- Other pension/medical deductions and the tax-year documentation.

## The method, step by step

### Apply the correct scheme before calculating

| Item | Amount and complete condition | Official source |
|---|---|---|
| Non-salaried SHIF | Annual contribution at 2.75% of household income determined by means-testing instrument, reg18(1), not simply declared individual earnings | https://libraryir.parliament.go.ke/bitstreams/4783efac-60c6-4dd0-8d16-265504c9ae8d/download |
| SHIF floor | KES 300 per month, equivalent annual KES 3,600 derived, reg18(2); no upper cap specified in reg18 | https://libraryir.parliament.go.ke/bitstreams/4783efac-60c6-4dd0-8d16-265504c9ae8d/download |
| Non-salaried annual renewal payment | 14 days before annual contribution lapses, reg18(3), in words on the page | https://libraryir.parliament.go.ke/bitstreams/4783efac-60c6-4dd0-8d16-265504c9ae8d/download |
| Premium financing | Authority-arranged financing for non-salaried persons; remittance directly to Authority, reg18(4)-(6) | https://libraryir.parliament.go.ke/bitstreams/4783efac-60c6-4dd0-8d16-265504c9ae8d/download |
| Voluntary NSSF contribution | Minimum amount KES 200; minimum aggregate in year KES 4,800 under s23(1)(a)-(b), in words on the page; not a 12% employee/employer formula | https://www.nssf.or.ke/download/download-the-nssf-act?wpdmdl=3590 |
| Voluntary registration | Self-employed person may register; must register employees under contract of service separately, s19(3) | https://www.nssf.or.ke/download/download-the-nssf-act?wpdmdl=3590 |
| Receipt/account | Mobile money, designated office or specified electronic transfer; notification and individual Provident Fund Credit, ss23-24 | https://www.nssf.or.ke/download/download-the-nssf-act?wpdmdl=3590 |
| SHIF tax treatment | Deductible under ITA s15(2)(ae); do not give insurance relief on the same SHIF contribution | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |
| NSSF/pension tax treatment | NSSF deemed registered defined-contribution fund under s22A(8); apply the actual member-category and lesser-of limits in the income-tax skill, not a blanket monthly deduction | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf |

1. **Register and establish household status.** Regulations11-14 cover registration/beneficiaries, including former NHIF members. Do not use historic NHIF brackets as current SHIF charges or assume legacy registration proves current cover. Retain the SHA registration/assessment.
2. **Use SHA's assessment.** Regulation21 uses household data and means testing, including housing, basic services, household composition and the Fifth Schedule instrument. Do not invent the assessed income from a monthly bank balance or add a spouse's earnings without the household assessment.
3. **Recompute the premium.** Once the annual assessed household income is established, annual SHIF is the greater of that income times the rate above and the annualised floor. A monthly equivalent is a budgeting figure, not an independent monthly filing obligation. Use the annual renewal and financing conditions above.
4. **Keep NSSF categories separate.** A voluntary self-employed member contributes to the Provident Fund under s23. Employee/employer contributions under s20 and Tier I/II are a different route. Do not impose their cap, employer match, monthly deadline or late penalty on a voluntary member without a separate rule.
5. **Register and pay with evidence.** NSSF's [current voluntary page](https://www.nssf.or.ke/voluntary-member) directs a visit with National ID, Alien Card or passport and a photocopy, capture of details and an initial minimum deposit, then a membership card. It describes top-ups via USSD *222# and M-PESA. Match each deposit to the individual account and retain notification/annual statement. SHA payment channel and financing should follow the issued assessment, not an invented universal mobile-money route.
6. **Apply deductions once.** Retain paid SHIF and pension evidence for the income-tax working paper. Contributions are deductions subject to the applicable law, not an automatic credit at their full value. The former blanket KES 30,000/month pension deduction is not established for every self-employed member: ss22A-22B distinguish employee/individual-retirement membership, actual contributions, pensionable-income percentage and annual/part-year ceilings, with NSSF reducing the individual-retirement monetary ceiling. The linked income-tax skill states those limits; establish eligibility before deducting. The former blanket KES 30,000/month pension deduction is not established for every self-employed member: ss22A-22B distinguish employee/individual-retirement membership, actual contributions, pensionable-income percentage and annual/part-year ceilings, with NSSF reducing the individual-retirement monetary ceiling. The linked income-tax skill states those limits; establish eligibility before deducting. See [ke-income-tax](ke-income-tax.md).

## Boundary and exception table

| Old topic / situation | Current treatment |
|---|---|
| Irregular/informal income | Means-tested household assessment; floor and financing may matter; do not declare a guessed individual average as final |
| Employed plus self-employed | Identify the household/category and existing employer deductions with SHA; no automatic extra premium on business income or assumed maxed pension |
| High income | SHIF reg18 specifies no ceiling; voluntary NSSF does not inherit the employee earnings cap |
| Non-citizen resident | Check lawful-residence/registration category and documents; do not presume exemption |
| Minimum income/financial hardship | Apply assessed household floor; reg19 addresses households needing government assistance |
| Constitutionality/court dispute | Refer; do not advise on constitutional validity or assume a pending-case outcome |

## Worked cases

Assume SHA has assessed annual household income KES 600,000. Annual SHIF is KES 16,500, monthly budgeting equivalent KES 1,375. If the member chooses KES 400 voluntary NSSF per month for a full year, annual NSSF is KES 4,800 and combined annual cash budget KES 21,300. The chosen pension amount is example input, not a percentage rule.

```oa-check
name: Assessed household health and chosen voluntary pension
inputs:
  assessed_annual_income: 600000
  chosen_monthly_nssf: 400
steps:
  - annual_shif: max(assessed_annual_income * 0.0275, 300 * 12)
  - monthly_equivalent: annual_shif / 12
  - annual_nssf: chosen_monthly_nssf * 12
  - annual_total: annual_shif + annual_nssf
expected:
  annual_shif: 16500
  monthly_equivalent: 1375
  annual_nssf: 4800
  annual_total: 21300
```

Low-income decision: an assumed assessed annual household income KES 60,000 gives percentage premium KES 1,650, below annualised floor KES 3,600. Voluntary NSSF deposits of KES 200 in each of 12 months total KES 2,400 and fall KES 2,400 short of s23's annual aggregate. A low monthly deposit alone does not prove annual compliance; consider SHA financial assistance/financing where appropriate.

```oa-check
name: Health floor and voluntary annual aggregate
inputs:
  assessed_annual_income: 60000
  monthly_nssf: 200
steps:
  - percentage_shif: assessed_annual_income * 0.0275
  - annual_shif: max(percentage_shif, 300 * 12)
  - annual_nssf: monthly_nssf * 12
  - pension_shortfall: max(0, 4800 - annual_nssf)
expected:
  percentage_shif: 1650
  annual_shif: 3600
  annual_nssf: 2400
  pension_shortfall: 2400
```

## When to refuse or refer

Refer missing household assessments, dual-status contributions, hardship/eligibility, court challenges, disputed premiums, late/expired cover and foreign residence. State the issue, relevant documents, options and the review required; never label the answer definitive while the category or assessed base is unknown.

## Filing and payment

Use SHA's issued household assessment, coverage/expiry and payment instructions. The annual renewal rule does not establish the initial due date for every new member. For voluntary NSSF, use the official registration/payment route and reconcile deposits against Provident Fund Credit and annual statement. Employment remittance rules belong to the payroll sibling. No generic voluntary late-payment penalty is quantified here.

## Completion checklist

Confirm household/category, assessment and dates; floor; annual premium/financing; voluntary vs employee NSSF; deposit amounts and annual aggregate; statements; and deductible payments without double relief.

## Sources

| Source and passages actually read | Official URL | Read on |
|---|---|---|
| Read for LN49/2024 consolidated to 28 February 2025, Parliament library copy, regs11-14,17-19,21-24 and Fifth Schedule: household route, means test, floor, timing and records; operative passages not entire benefits schedule | https://libraryir.parliament.go.ke/bitstreams/4783efac-60c6-4dd0-8d16-265504c9ae8d/download | 2026-11-14 |
| Read for NSSF Act ss19(3),20-24, voluntary Provident Fund versus employee Pension Fund and annual minimum, official NSSF download legislation as at 31 December 2022 | https://www.nssf.or.ke/download/download-the-nssf-act?wpdmdl=3590 | 2026-11-14 |
| Read for NSSF current voluntary registration, documents, initial deposit and top-up channel | https://www.nssf.or.ke/voluntary-member | 2026-11-14 |
| Read for ITA s15(2)(ae),ss22A(8),22B, contribution deductibility and limits | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf | 2026-11-14 |

Not yet confirmed: Initial SHA payment timing for a new non-salaried member, case-specific mixed-income category, actual financing terms, live portal labels and constitutional litigation outcomes. The Ministry-hosted unsigned draft with blank legal-notice/date was rejected; the gazetted Parliament copy governs the cited regulation numbering. Old NHIF KES 150-1,700 brackets/KES 500 self-employed charge are historical and not used. Old NSSF 12% voluntary formula, KES 1,080/12,960 voluntary limits, employment 9th-day deadline and 5% monthly voluntary penalty were misapplied; former example totals KES 7375/18460/3600 and automatic KES 1100 dual-status SHIF are not current voluntary instructions. Employee limits remain in the payroll sibling.
