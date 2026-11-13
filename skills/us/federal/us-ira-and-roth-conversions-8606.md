---
name: us-ira-and-roth-conversions-8606
description: Work out a person's 2026 traditional and Roth IRA position. Covers the 2026 contribution limit of USD 7,500 plus the USD 1,100 age-50 catch-up, the traditional IRA deduction phase-outs for active plan participants and their spouses from IRS Notice 2025-67, the Roth IRA income phase-outs, Roth conversions, the section 408(d)(2) pro-rata rule that treats all traditional, SEP and SIMPLE IRAs as one, the backdoor Roth, and the 2026 Form 8606 line by line, with a convert-now-or-not decision. Trigger on "Roth conversion", "backdoor Roth", "pro-rata rule", "Form 8606", "nondeductible IRA", "can I deduct my IRA", "Roth income limit", "IRA basis". Federal only.
version: "1.0"
jurisdiction: US
category: federal-tax
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Traditional and Roth IRAs, conversions and Form 8606, tax year 2026

> **Source-cited draft.** Built from IRS Notice 2025-67, the 2026 Form 8606, the 2025 Instructions for Form 8606, IRS Pub. 590-A, and 26 U.S.C. 219, 408 and 408A on govinfo.gov, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 a person can put up to **USD 7,500** into traditional and Roth IRAs combined, plus **USD 1,100** if 50 or over by year end, but not more than their taxable compensation. The traditional IRA deduction phases out for an active workplace-plan participant between USD 81,000 and USD 91,000 of modified AGI (single, head of household) or USD 129,000 and USD 149,000 (joint). Direct Roth contributions phase out from USD 153,000 to USD 168,000 (single, head of household) and USD 242,000 to USD 252,000 (joint). Anyone can convert a traditional IRA to a Roth IRA at any income; the conversion is taxed except for the share of basis, and that share is worked out over **all** the person's traditional, SEP and SIMPLE IRAs at 31 December, not just the account converted. A 2018 or later conversion cannot be undone.

## Scope and who this is for

In scope: one individual's 2026 IRA contributions (deductible or not), Roth IRA contribution eligibility, conversions of traditional, SEP and SIMPLE IRAs to Roth IRAs, the backdoor Roth, and the 2026 Form 8606 Parts I and II. Each spouse files their own Form 8606.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| 401(k), 403(b), SIMPLE and catch-up limits, Roth catch-up for high earners | `us-secure-2-and-retirement-updates` |
| Required minimum distributions, inherited IRAs, qualified charitable distributions | `us-secure-2-and-retirement-updates` |
| SEP and Solo 401(k) for the self-employed | `us-self-employed-retirement` |
| How a conversion changes taxable Social Security | `us-social-security-benefits-taxation` |
| Tax brackets and the rest of Form 1040 | `us-federal-income-tax-return-1040` |
| The senior deduction phase-out a conversion can trigger | `us-new-deductions-tips-overtime-senior-car-loan` |
| 529 to Roth IRA rollovers | `us-secure-2-and-retirement-updates` |

## Ask the client first

1. **Age at 31 December 2026**, and filing status.
2. **Taxable compensation for 2026** (wages, net self-employment earnings), and the spouse's if one spouse has little or none (spousal IRA).
3. **Was the client, or the spouse, an active participant** in a workplace plan in 2026 (Form W-2 box 13 "Retirement plan" ticked, or a SEP or SIMPLE)?
4. **Modified AGI estimate for 2026**, including any planned conversion.
5. **Every traditional, SEP and SIMPLE IRA** the client owns, with expected 31 December 2026 values. Inherited IRAs and 401(k) balances are not counted.
6. **Prior Form 8606** (line 14 basis from the latest year filed). If none was ever filed for nondeductible contributions, the basis may be undocumented.
7. **Planned 2026 conversions and distributions**, and whether the employer plan accepts roll-ins (which can take pre-tax IRA money out of the pro-rata count).
8. For a conversion decision: the expected marginal rate now and in retirement, where the tax will be paid from, and when the money will be needed.

## The method, step by step

### Rates, bands and thresholds

| Item, 2026 | Amount | Source |
| --- | --- | --- |
| IRA contribution limit, traditional and Roth combined | USD 7,500 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| IRA catch-up, age 50 before year end | USD 1,100 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Deduction phase-out, active participant, single or head of household | USD 81,000 to USD 91,000 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Deduction phase-out, active participant, married filing jointly | USD 129,000 to USD 149,000 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Deduction phase-out, not an active participant but the spouse is (joint) | USD 242,000 to USD 252,000 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Deduction phase-out, married filing separately, active participant (not indexed) | USD 0 to USD 10,000 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth IRA, AGI limitation amount, married filing jointly (start of phase-out) | USD 242,000 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth IRA phase-out range, married filing jointly | USD 242,000 to USD 252,000 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth IRA, AGI limitation amount, single and head of household (start of phase-out) | USD 153,000 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth IRA phase-out range, single and head of household | USD 153,000 to USD 168,000 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth IRA phase-out range, married filing separately (not indexed) | USD 0 to USD 10,000 | [IRS Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Phase-out rounding: reduction rounded down to the next USD 10; no limit below USD 200 unless fully phased out | USD 10 / USD 200 | [26 U.S.C. 219(g)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec219.htm) |
| Penalty for not filing a required Form 8606 for a nondeductible contribution | USD 50 | [Instructions for Form 8606 (2025)](https://www.irs.gov/pub/irs-pdf/i8606.pdf) |
| Penalty for overstating nondeductible contributions | USD 100 | [Instructions for Form 8606 (2025)](https://www.irs.gov/pub/irs-pdf/i8606.pdf) |
| Additional tax on early distributions (under 59½), including converted amounts withdrawn within 5 years | 10% | [26 U.S.C. 72(t)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec72.htm) |

### Step 1: how much can go in

The combined limit is the smaller of USD 7,500 (plus USD 1,100 at 50 or over) and taxable compensation ([26 U.S.C. 219(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec219.htm)). On a joint return a spouse with little compensation can use the couple's combined compensation (219(c)). There is no age limit on traditional IRA contributions. Contributions for 2026 can be made until **15 April 2027**, with no extension.

### Step 2: is the traditional contribution deductible?

- Neither spouse an active participant: fully deductible at any income.
- Otherwise use the phase-out range for the person's situation from the table. Reduction = limit x (modified AGI minus start of range) / width of range (USD 10,000; USD 20,000 for the joint active-participant range), rounded down to the next USD 10 under 219(g)(2)(C), with a USD 200 minimum allowed until the range ends. Modified AGI for this test is AGI after taxable Social Security and passive losses, without the IRA deduction itself and without the student loan, savings bond, adoption and foreign earned income exclusions ([219(g)(3)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec219.htm)).
- Any part not deducted is a **nondeductible contribution**: it becomes basis and must go on Form 8606 line 1.

### Step 3: can the person contribute to a Roth IRA directly?

Apply the same reduction formula to the Roth limit over the Roth range (USD 15,000 wide single; USD 10,000 wide joint) ([26 U.S.C. 408A(c)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408A.htm)). Modified AGI here excludes the income from a Roth conversion. Above the range: no direct Roth contribution; use the backdoor (step 5).

### Step 4: a conversion and the pro-rata rule

1. A conversion is a distribution from the traditional, SEP or SIMPLE IRA that goes into a Roth IRA. It is included in gross income except for the basis share, and the 10% early-distribution tax does **not** apply at conversion ([408A(d)(3)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408A.htm)).
2. **Pro-rata rule:** for working out the basis share, all of a person's traditional, SEP and SIMPLE IRAs are one contract, all distributions in the year are one distribution, and values are taken at the close of the calendar year ([26 U.S.C. 408(d)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408.htm)). Roth IRAs are counted separately ([408A(d)(4)(A)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408A.htm)). A spouse's IRAs and inherited IRAs are not aggregated with the person's own.
3. On the 2026 Form 8606 ([form](https://www.irs.gov/pub/irs-pdf/f8606.pdf)):
   - line 1 nondeductible contributions for 2026; line 2 prior basis (the last Form 8606 line 14); line 3 = 1 + 2;
   - line 4 contributions for 2026 made 1 January to 15 April 2027; line 5 = 3 minus 4;
   - line 6 value of all traditional, SEP and SIMPLE IRAs at 31 December 2026 (plus outstanding rollovers);
   - line 7 other 2026 distributions (not rollovers, QCDs or conversions); line 8 the amount converted;
   - line 9 = 6 + 7 + 8; line 10 = 5 / 9 (at least 3 decimals, capped at 1.000);
   - line 11 = 8 x 10, the nontaxable part of the conversion; line 12 = 7 x 10;
   - line 14 = 3 minus 13, basis carried to 2027;
   - Part II: line 16 = 8, line 17 = 11, **line 18 = 16 minus 17, the taxable conversion**, which goes to Form 1040 line 4b.
4. **No undo.** A conversion made in a tax year beginning after 31 December 2017 cannot be recharacterized back to a traditional IRA ([408A(d)(6)(B)(iii)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408A.htm); [Instructions for Form 8606](https://www.irs.gov/pub/irs-pdf/i8606.pdf)). An annual contribution can still be recharacterized by the extended due date.
5. **Five-year rule for conversions.** If the person is under 59½ and withdraws a converted amount within the 5-taxable-year period starting with the year of the conversion, the 10% additional tax applies to the part that was taxable on conversion ([408A(d)(3)(F)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408A.htm)). Each conversion has its own clock. Separately, earnings come out tax-free only in a qualified distribution: after 59½ (or death or disability) and after the 5-year period from the first Roth contribution ([408A(d)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408A.htm)).

### Step 5: the backdoor Roth

A person over the Roth income range makes a nondeductible traditional IRA contribution (Form 8606 line 1) and then converts it. If they hold no other pre-tax traditional, SEP or SIMPLE IRA money at **31 December** of the conversion year, line 10 is 1.000 and only the earnings between contribution and conversion are taxable. Pre-tax IRA money anywhere makes most of the conversion taxable (worked case 1). The fix is to roll the pre-tax IRA money into an employer plan that accepts it **before 31 December**, since 401(k) balances are not on line 6. Rolling into the plan after the conversion but before year end still works, because line 6 is measured at year end.

### Step 6: convert now or not

The comparison that decides, with the same growth either way:

- Paying the tax out of the converted money, conversion wins only if the marginal rate later is **higher** than the marginal rate now. If the rates are equal, the outcomes are equal.
- Paying the tax from money outside the IRA makes the conversion better, because it moves more money into the tax-free account.
- Count the side effects at today's rate: the conversion raises AGI for 2026, which can make more Social Security taxable (`us-social-security-benefits-taxation`), cut the senior deduction (`us-new-deductions-tips-overtime-senior-car-loan`), and affect premium tax credits and Medicare premiums two years later.
- Converting reduces future required minimum distributions, since Roth IRAs have none during the owner's life (`us-secure-2-and-retirement-updates`).
- Do not convert money needed within five years if under 59½ (step 4.5).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Contribution above the limit or compensation | 6% excise each year it stays (Form 5329) unless withdrawn with earnings by the due date; refer the computation (R-IRA-EXCESS) |
| Roth contribution made, income turns out too high | Recharacterize to a traditional IRA by the extended due date, or withdraw with earnings |
| Pre-tax IRA balance at 31 December | Counted on line 6; makes the backdoor mostly taxable |
| Inherited traditional IRA | Not aggregated with the owner's own IRAs; cannot be converted by a non-spouse beneficiary |
| SEP or SIMPLE IRA | Counted on line 6 for the pro-rata rule; a SIMPLE IRA cannot be converted in its first 2 years of participation |
| Missing earlier Forms 8606 | Basis must be rebuilt from records; file the missing forms; without proof the basis is zero |
| Distribution and conversion in the same year | Both share the same line 10 ratio |
| Qualified charitable distribution | Comes from pre-tax money first; not on line 7 |
| Roth 401(k) rolled to a Roth IRA | Not a conversion; no Form 8606 Part II |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Active participant status | Read W-2 box 13; if no W-2, ask |
| Prior basis | Zero until a prior Form 8606 is produced |
| 31 December IRA values | Estimate with today's balance and flag; rework when year-end statements arrive |
| Future tax rate (for the decision) | Show the answer at the current rate and one bracket higher; do not pick for the client |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Backdoor Roth with any SEP, SIMPLE or rollover IRA balance | Pro-rata rule makes most of it taxable |
| Nondeductible contributions with no Form 8606 ever filed | Basis lost, double tax on withdrawal, USD 50 penalty per missed form |
| Conversion near a Social Security or senior deduction threshold | Extra tax beyond the bracket rate |
| Converting while under 59½ and planning to withdraw soon | 10% additional tax on early withdrawal of converted amounts |
| A request to "undo" a conversion | Not possible for 2018 and later conversions |

## Worked cases

**Case 1, a backdoor Roth caught by the pro-rata rule.** A single filer over the Roth range has no prior basis. In 2026 she contributes USD 7,500 nondeductible to a traditional IRA and converts USD 7,500 in the same year. She also has an old rollover IRA, worth USD 67,500 at 31 December 2026.

Form 8606: line 1 USD 7,500, line 3 USD 7,500, line 5 USD 7,500. Line 6 USD 67,500, line 7 zero, line 8 USD 7,500, line 9 USD 75,000. Line 10 = 7,500 / 75,000 = 0.100. Line 11, the nontaxable part = USD 750. Line 18, taxable conversion = **USD 6,750**. Line 14, basis carried to 2027 = USD 6,750. Had she rolled the USD 67,500 into her 401(k) before 31 December, line 10 would be 1.000 and nothing would be taxable.

```oa-check
name: Backdoor Roth with a pre-tax IRA, Form 8606 (2026)
inputs:
  nondeductible_2026: 7500
  prior_basis: 0
  year_end_ira_value: 67500
  other_distributions: 0
  converted: 7500
steps:
  - line_3: nondeductible_2026 + prior_basis
  - line_9: year_end_ira_value + other_distributions + converted
  - line_10: min(line_3 / line_9, 1)
  - line_11: converted * line_10
  - line_18: converted - line_11
  - line_14: line_3 - line_11 - other_distributions * line_10
expected:
  line_10: 0.10
  line_11: 750.00
  line_18: 6750.00
  line_14: 6750.00
```

**Case 2, a decision: convert USD 50,000 now or not?** A couple's marginal rate now is 22%. They expect 24% when they withdraw. Assume the money doubles before it is used (any growth works, as long as it is the same either way). The tax is paid out of the converted amount.

Convert: USD 50,000 less 22% tax = USD 39,000 in the Roth, doubling to **USD 78,000** tax-free. Do not convert: USD 50,000 doubles to USD 100,000, less 24% on withdrawal = **USD 76,000**. Converting is USD 2,000 better. At equal rates the two are the same; if the later rate were lower than 22%, not converting would win. Before acting, rerun the 2026 Social Security and senior deduction figures on the higher AGI, since those can push the effective rate now above 22%.

```oa-check
name: Convert now or not, same growth (2026)
inputs:
  conversion: 50000
  rate_now: 0.22
  rate_later: 0.24
  growth_factor: 2
steps:
  - roth_value: conversion * (1 - rate_now) * growth_factor
  - traditional_after_tax: conversion * growth_factor * (1 - rate_later)
  - advantage_of_converting: roth_value - traditional_after_tax
expected:
  roth_value: 78000.00
  traditional_after_tax: 76000.00
  advantage_of_converting: 2000.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-IRA-EXCESS | Excess contribution left in past the due date | Refer: Form 5329 6% excise computation |
| R-IRA-BASIS | Basis from years with no Form 8606, or from rollovers of after-tax 401(k) money | Refer: basis reconstruction |
| R-IRA-INHERIT | Inherited IRA questions | `us-secure-2-and-retirement-updates` |
| R-IRA-MEGA | After-tax 401(k) contributions converted in-plan or rolled to a Roth IRA (mega backdoor) | Refer: plan rules and Form 1099-R coding decide |
| R-IRA-NRA | Nonresident or a foreign pension | Refer |

## Filing and payment

Attach Form 8606 (one per spouse) to the 2026 Form 1040, due **15 April 2027**; an extension to 15 October 2027 extends filing, not payment, and does not extend the deadline for 2026 contributions. The taxable conversion goes on Form 1040 line 4b with the gross amount on line 4a. Tax on a conversion is not withheld unless the client asks; plan estimated payments in the quarter of the conversion (`us-quarterly-estimated-tax`). The custodian reports the conversion on Form 1099-R and the year-end value on Form 5498.

## Completion checklist

- Contribution within USD 7,500 (USD 8,600 at 50 or over) and within compensation.
- Active participant status for both spouses checked from W-2 box 13.
- Deductible and nondeductible parts split; nondeductible part on Form 8606 line 1.
- Line 2 taken from the latest Form 8606 line 14.
- Line 6 includes every traditional, SEP and SIMPLE IRA at 31 December 2026, and no inherited or 401(k) balance.
- Line 18 on Form 1040 line 4b.
- Effect of a conversion on taxable Social Security and the senior deduction checked.
- Five-year clock recorded for each conversion.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Notice 2025-67. Read for the 2026 IRA limit (USD 7,500), catch-up (USD 1,100), deduction phase-outs (USD 81,000 to 91,000; USD 129,000 to 149,000; USD 242,000 to 252,000; USD 0 to 10,000) and Roth phase-outs (USD 153,000 to 168,000; USD 242,000 to 252,000; USD 0 to 10,000). | https://www.irs.gov/pub/irs-drop/n-25-67.pdf | 2026-11-13 |
| Form 8606 (2026). Read for Parts I to III, lines 1 to 25c. | https://www.irs.gov/pub/irs-pdf/f8606.pdf | 2026-11-13 |
| Instructions for Form 8606 (2025). Read for the USD 50 and USD 100 penalties and for no recharacterization of conversions after 2017. | https://www.irs.gov/pub/irs-pdf/i8606.pdf | 2026-11-13 |
| IRS Pub. 590-A. Read for contribution, deduction and conversion rules and the recharacterization limit. | https://www.irs.gov/pub/irs-pdf/p590a.pdf | 2026-11-13 |
| 26 U.S.C. 219 (govinfo). Read for (b) the limit and compensation, (c) the spousal IRA, (g)(2) the reduction formula, rounding and USD 200 floor, (g)(3) modified AGI. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec219.htm | 2026-11-13 |
| 26 U.S.C. 408 (govinfo). Read for (d)(2): all IRAs treated as one contract, values at year end. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408.htm | 2026-11-13 |
| 26 U.S.C. 408A (govinfo). Read for (c)(3) Roth phase-out, (d)(2) qualified distributions, (d)(3) conversions and the 5-year rule, (d)(4) aggregation and ordering, (d)(6)(B)(iii) no recharacterization of conversions. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408A.htm | 2026-11-13 |
| 26 U.S.C. 72 (govinfo). Read for (t), the 10% additional tax. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partII-sec72.htm | 2026-11-13 |

Not yet confirmed: the 2026 Instructions for Form 8606 were not yet published when read, so the penalty amounts are from the 2025 instructions (they are statutory under section 6693(b) and do not change yearly); the 6% excess-contribution excise and the SIMPLE IRA 2-year rule are stated from Pub. 590-A without a line quote and are routed to referral rather than computed here.
