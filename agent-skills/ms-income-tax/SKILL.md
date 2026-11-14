---
name: ms-income-tax
description: "Mississippi 2026 resident wage and sole-proprietor income tax: separate state income computation, 4% above $10,000, deductions/exemptions, retirement, combined spouses and estimates."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ms-income-tax"
  jurisdiction: "US-MS"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Mississippi individual income tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Mississippi's 2026 individual tax is 4% on taxable income above $10,000. Compute the state income and adjustments separately, then deductions/exemptions; do not multiply federal AGI by 4%. [DOR year-specific rate table](https://www.dor.ms.gov/general-information); [HB1 section1 amending27-7-5](https://billstatus.ls.state.ms.us/documents/2025/html/HB/0001-0099/HB0001SG.htm).

## Scope

Ordinary full-year Mississippi residents with wages, sole-proprietor/disregarded LLC profit, rents, interest, gains and retirement income. Form 80-105 is the resident return. Nonresident/part-year Form 80-205, complex K-1/PTE, amendments and multistate allocation require separate review. `ms-corporate-tax`, `ms-sales-tax` and `ms-payroll` own the other core jobs. Federal business profit, SE tax, insurance, retirement and asset computations remain with `us-schedule-c-and-se-computation`, `us-self-employed-health-insurance`, `us-self-employed-retirement` and `us-section-179-and-bonus-depreciation`.

## Ask the client first

1. Domicile, move dates, homes, other-state work and returns; is each spouse a full-year resident?
2. Filing status, each spouse's separate income, dependents, age/blindness and claimed exemptions?
3. Wages, Schedule C/F/E profit, gains, interest by issuer, dividends, pension plan/retirement eligibility and Social Security?
4. Federal/state asset reconciliations, self-employed insurance/retirement contributions, SE deduction and state itemized versus standard deductions?
5. Withholding, credits/other-state actual liability, estimates, federal extension and prior-year return?

## The method, step by step

1. **Classify the resident and filing method.** Use the domicile/home and citizenship-rights evidence described in the DOR booklet; the old blanket 183-day test was not verified. A resident reports all-source taxable income, with specific exclusions. For married taxpayers compare permissible joint/combined or separate filings. A combined return computes each spouse's tax separately and adds it; one spouse's income cannot be split merely to manufacture a second zero-rate band. [2025 instructions pp.4-6; 2025-2026 filing cycle](https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf); [DOR combined-return rule](https://www.dor.ms.gov/general-information).
2. **Build Mississippi income category by category.** Reconcile wages, business/farm/rental profit, gains, taxable interest/dividends and other income. Federal schedules support the computation but state differences require a reconciliation. U.S. and Mississippi government-obligation interest is exempt; other-state municipal interest is taxable. Gains generally use the ordinary state rate, with special ownership-interest provisions requiring review. Social Security is exempt; qualified retirement income from federal/state/private systems is generally exempt when plan requirements are met. Early/excess distributions and separation pay are different. [2025 instructions pp.10-11; 2025-2026 filing cycle](https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf); [DOR retirement/SS FAQ](https://www.dor.ms.gov/individual/individual-income-tax-frequently-asked-questions).
3. **Apply state adjustments once.** The opened booklet allows the federally claimed half-SE-tax deduction, self-employed health insurance and qualifying self-employed retirement contribution deduction. Carry the federal owner result, attach the appropriate schedules and reconcile state differences. Do not simply start from federal AGI and deduct the same item again. Depreciation/section179/bonus conformity needs its own current state authority; the legacy blanket conformity claim remains unresolved. [2025 instructions pp.12-13; 2025-2026 filing cycle](https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf); [SB2858 section2, SE adjustment](https://billstatus.ls.state.ms.us/documents/2016/html/SB/2800-2899/SB2858SG.htm).
4. **Choose state deductions and exemptions.** Compare properly adjusted Mississippi itemized deductions with standard deduction. State income tax is not deductible on the state itemized schedule; check additional exclusions such as Mississippi gambling losses in current instructions. Use the table below and actual spouse allocation. Separate filers cannot transfer an unused half to the spouse; if one itemizes, both must. [DOR deductions/exemptions](https://www.dor.ms.gov/general-information); [2025 instructions pp.5-6](https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf); [Itemized deductions FAQ](https://www.dor.ms.gov/individual/individual-income-tax-frequently-asked-questions).
5. **Calculate and reconcile.** For each proper taxpayer computation: taxable income = max(0, state income - allowed adjustments - deduction - exemptions). 2026 gross tax = max(0, taxable income -10000)x0.04. Apply substantiated credits, then withholding/estimates. Other-state credit uses actual tax liability, not withholding, and requires the other return. [2026 rate row](https://www.dor.ms.gov/general-information); [Other-state credit FAQ](https://www.dor.ms.gov/individual/individual-income-tax-frequently-asked-questions).

### Rates, bands and thresholds

| 2026 item | Amount or rule | Authority |
| --- | --- | --- |
| Individual income tax | 0% first $10,000;4% excess | [DOR 2026 rate](https://www.dor.ms.gov/general-information); [27-7-5 in HB1§1](https://billstatus.ls.state.ms.us/documents/2025/html/HB/0001-0099/HB0001SG.htm) |
| Standard deduction | Single/MFS$2,300; joint/combined$4,600; Head of Family$3,400 | [DOR deductions table](https://www.dor.ms.gov/general-information) |
| Filing-status exemption | Single/MFS$6,000; joint/combined$12,000; Head of Family$8,000 with qualifying dependent | [DOR exemptions table](https://www.dor.ms.gov/general-information) |
| Additional exemptions | $1,500 each qualifying dependent; $1,500 each taxpayer/spouse qualifying age or blindness | [DOR exemptions table](https://www.dor.ms.gov/general-information) |
| Estimates | Annual liability exceeds $200 and less than80% prepaid through withholding | [Estimated-tax FAQ](https://www.dor.ms.gov/individual/individual-income-tax-frequently-asked-questions) |

### Boundary table

| Fact | Treatment |
| --- | --- |
| 2025-2026 filing cycle | 2025 rate is4.4% above $10,000; use dated form instructions only for their stated year. [DOR 2025 comparison row](https://www.dor.ms.gov/general-information). |
| Future phase-out | DOR confirms3.75% for 2027; later reductions are not evidence that2026 tax is repealed. [DOR 2027 row](https://www.dor.ms.gov/general-information); [2025 enacted-law summary](https://www.dor.ms.gov/forms-resources/laws-regulations/2025-legislation). |
| Two working spouses | Income stays with its earner; allocate permitted joint deductions/exemptions without exceeding totals and compute separately when using combined filing. |
| Qualified retirement versus early payout | Identify plan and service/age requirements. An ordinary retirement exemption is not a blanket exemption for every1099-R. [Retirement FAQ](https://www.dor.ms.gov/individual/individual-income-tax-frequently-asked-questions). |
| Part-year/nonresident/mixed-residency spouses | Form 80-205 and prorated deductions require separate work. [Residency FAQ](https://www.dor.ms.gov/individual/individual-income-tax-frequently-asked-questions). |
| No local income tax and state estate-tax absence | Both are legacy topics held under Sources; neither is an unsupported rule in this computation. |

## Worked cases

### Resident wage earner

A single full-year resident has $60,000 state-taxable wages, no adjustments/credits/dependents, and uses the current$2,300 standard deduction and$6,000 exemption. Taxable income is$51,700 and2026 tax $1,668. With$1,600 withholding, the illustrative balance is$68 before any other payments.

```oa-check
name: MS single wage income 2026
inputs:
  wages: 60000
  withheld: 1600
steps:
  - taxable: max(0, wages - 2300 - 6000)
  - tax: max(0, taxable - 10000) * 0.04
  - balance: tax - withheld
expected:
  taxable: 51700
  tax: 1668
  balance: 68
```

### Combined spouses keep separate taxable income

Assume a proper combined return leaves spouse A with $30,000 taxable income and spouse B with $18,000 after valid allocation of deductions/exemptions. Their 2026 taxes are$800 and$320, total$1,120. Applying only one$10,000 band to the total would overstate the combined result. These are already taxable amounts, so no second deduction is allowed.

```oa-check
name: MS combined separate spouse tax
inputs:
  a_taxable: 30000
  b_taxable: 18000
steps:
  - a_tax: max(0, a_taxable - 10000) * 0.04
  - b_tax: max(0, b_taxable - 10000) * 0.04
  - total: a_tax + b_tax
expected:
  a_tax: 800
  b_tax: 320
  total: 1120
```

## When to refuse or refer

Refer nonresident/multistate allocation, entity/PTE adjustments, amended returns, complex retirement payouts, special gains and unresolved asset conformity. Corporate/franchise questions go to `ms-corporate-tax`. Use the actual tax year; do not carry phase-out rates across years or treat the old unsupported183-day rule as established.

## Filing and payment

The recurring resident due date is April15 for calendar years, fifteenth day of the fourth month for fiscal years, subject to applicable weekend/holiday relief. The opened **2025-2026 filing cycle** instructions recognize the federal filing extension but require tax by the original due date. Pay through TAP or the proper payment voucher; confirm final 2026 return deadlines/lines and relief before submitting. [2025 instructions p.4](https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf); [Filing FAQ](https://www.dor.ms.gov/individual/individual-income-tax-frequently-asked-questions).

Individual estimates normally use April15, June15, September15 and January15 following the year. DOR's 80%/exceeds $200 rule above controls; special farming/fishing and later-liability exceptions need their actual conditions. [2025 instructions p.22, 2025-2026 filing cycle](https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf); [Estimated payments FAQ](https://www.dor.ms.gov/individual/individual-income-tax-frequently-asked-questions).

The old form map is corrected:80-100 is the instruction booklet;80-105 resident return;80-205 nonresident/part-year;80-106 payment voucher;80-107 Income/Withholding Tax Schedule;80-108 schedules including itemized deductions/adjustments;80-320 underestimated-tax interest/penalty worksheet. They are not respectively a generic adjustment form, credit summary and estimate declaration as formerly claimed. Final2026 line numbers remain a gap. [2025 booklet form instructions](https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf).

## Completion checklist

Confirm residency/year, reconcile every income category and federal owner, substantiate retirement/interest exclusions, allocate spouse deductions correctly, apply2026 rate, reconcile payments and retain attachments and filing confirmation.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| DOR general information; read for for all current exemption/deduction rows and2025-2027 rate table/combined example. | https://www.dor.ms.gov/general-information | 2026-11-13 |
| 2025 Form 80-100 instructions; read for for pp.4-6 residence/filing/spouses, pp.10-13 income/adjustments and p.22 estimates;2025-2026 filing cycle. | https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf | 2026-11-13 |
| DOR individual FAQ; read for for retirement/SS, nonresident/mixed-residency, itemized/other-state credit, estimate and filing sections. | https://www.dor.ms.gov/individual/individual-income-tax-frequently-asked-questions | 2026-11-13 |
| 2025 HB1 final sent-to-governor text; read for for section1 current27-7-5 and section3 grocery amendment, plus adjacent effective-date/phase-out paragraphs. | https://billstatus.ls.state.ms.us/documents/2025/html/HB/0001-0099/HB0001SG.htm | 2026-11-13 |
| DOR 2025 enacted legislation; read for for HB1 individual-rate and grocery provisions confirming implemented legislation. | https://www.dor.ms.gov/forms-resources/laws-regulations/2025-legislation | 2026-11-13 |
| SB2858 of2016; read for for section2 half-SE deduction and adjacent rate/franchise effective-date provisions. | https://billstatus.ls.state.ms.us/documents/2016/html/SB/2800-2899/SB2858SG.htm | 2026-11-13 |

Not yet confirmed: final 2026 Form 80-105/205 lines and filing relief; 2026 depreciation, section179 and bonus conformity; legacy183-day residency claim, no-local-income-tax assertion and estate-tax absence. The separate state income/adjustment method and SE health/retirement/half-SE deductions are verified from the2025-2026 filing cycle; final 2026 continuation/instructions remain a filing gate. The rate and current deduction/exemption tables above are separately confirmed by DOR current guidance; no2025 rate is extrapolated.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ms-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ms-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
