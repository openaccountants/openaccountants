---
name: mi-pension-retirement-subtraction
description: "Decide and compute a Michigan retiree's 2026 retirement and pension subtraction (Form 4884) or the age-67 Michigan standard deduction. 2026 is the first year of the full Public Act 4 of 2023 restoration - every retiree, whatever the birth year, may subtract combined public and private retirement benefits up to $67,610 single or $135,220 joint (2026 Withholding Guide); people born before 1946 still subtract public pensions without limit; qualified police, fire and corrections retirees subtract public benefits without limit. For 2026 to 2028, 2025 PA 24 lets people born after 1952 who are 67 or older take both the $20,000 or $40,000 standard deduction and the Social Security subtraction. Social Security, military and railroad retirement are always subtracted. Trigger on \"Michigan pension subtraction\", \"Form 4884\", \"Michigan retirement tax\", \"PA 4 of 2023\", \"Lowering MI Costs Plan\", \"Michigan standard deduction age 67\", \"Michigan tier 1 tier 2 tier 3\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mi-pension-retirement-subtraction"
  jurisdiction: "US-MI"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Michigan retirement and pension subtraction (Form 4884), tax year 2026

> **Source-cited draft.** Built from Revenue Administrative Bulletin 2026-1 (approved 8 January 2026), the Treasury notice on Social Security changes in Public Act 24 of 2025 (17 November 2025), the Treasury Retirement and Pension Benefits page, the 2026 Michigan Income Tax Withholding Guide and the Tax Year 2025 Information page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 the phase-in ends: **any** Michigan retiree may subtract qualifying retirement and pension benefits (public and private combined) up to **$67,610** single or married filing separately, or **$135,220** joint. Retirees born before 1946 subtract public pensions in full and private ones up to what is left of the limit. Qualified police, fire and corrections retirees subtract public benefits in full. Instead of the retirement subtraction, someone **67 or older** may take the **$20,000** ($40,000 joint) Michigan standard deduction against all income, reduced by the personal exemption. For 2026 to 2028, people born after 1952 no longer reduce that standard deduction by their Social Security subtraction. Social Security, military and railroad retirement are subtracted in any case. Compute both routes and take the one with the lower taxable income.

## Scope and who this is for

In scope: a full-year Michigan resident (or couple) for 2026 with retirement or pension income in federal AGI, or aged 67 or older, choosing between the Form 4884 retirement subtraction and the Michigan standard deduction.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The rest of the MI-1040 | `mi-income-tax` |
| Pension withholding by payers | `mi-payroll` |
| City of Detroit treatment (pensions not taxed by Detroit) | `mi-detroit-individual-return` |
| Federal taxation of the distributions | the federal skills |

## Ask the client first

1. **Dates of birth** of the taxpayer and spouse. On a joint return the older (living) spouse's year of birth governs; married filing separately uses each filer's own.
2. **Every 1099-R**, with the payer: public (federal, Michigan, another state's government) or private; distribution code; whether any was an early or separation distribution.
3. **Was any public pension earned as a police officer, firefighter, state police trooper or sergeant, or county corrections officer** (or similar federal service)?
4. **Social Security, railroad retirement, military or Michigan National Guard retirement** amounts in AGI.
5. **Surviving spouse?** Year of the spouse's death, remarriage, and what was subtracted on the joint return for that year.
6. **Other income** (wages, business, interest), which only the standard deduction can shelter.
7. **Retirement from employment not covered by Social Security?** (special Form 4884 sections).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Source |
| --- | --- | --- |
| Retirement subtraction limit for 2026, single or married filing separately (public and private combined; all birth years) | $67,610 | [2026 Michigan Income Tax Withholding Guide](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf) |
| Same, married filing jointly | $135,220 | [2026 Michigan Income Tax Withholding Guide](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf) |
| Phase-in share for 2026 and later | up to 100% | [Treasury, Retirement and Pension Benefits](https://www.michigan.gov/taxes/iit/tax-guidance/tax-situations/retirement-and-pension-benefits) |
| 2025 for comparison: private limit (born before 1946) / phase-in limit (born 1946 to 1966), single | $65,897 / $49,423 | [Tax Year 2025 Information](https://www.michigan.gov/taxes/iit/tax-guidance/tax-year-info/tax-year-2025-guidance) |
| 2025 for comparison, joint | $131,794 / $98,846 | [Tax Year 2025 Information](https://www.michigan.gov/taxes/iit/tax-guidance/tax-year-info/tax-year-2025-guidance) |
| Michigan standard deduction at age 67, single / joint | $20,000 / $40,000 | [RAB 2026-1](https://www.michigan.gov/taxes/rep-legal/rab/2026-revenue-administrative-bulletins/revenue-administrative-bulletin-2026-1) |
| Personal exemption for 2026 (reduces the standard deduction) | $5,900 | [2026 Michigan Income Tax Withholding Guide](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf) |
| Michigan rate for 2026 | 4.25% | [Treasury notice, 15 April 2026](https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/04/15/425-income-tax-rate-for-individuals-and-fiduciaries-in-2026-tax-year) |

### What counts as retirement and pension benefits

Most income reported on Form 1099-R and included in AGI: defined benefit pensions, IRA distributions and most defined contribution plan payments. Deferred compensation generally does not qualify. Distributions taken early (before the plan's retirement terms) do not qualify. Roth IRA distributions not in AGI have nothing to subtract. Sources: [Treasury, Retirement and Pension Benefits](https://www.michigan.gov/taxes/iit/tax-guidance/tax-situations/retirement-and-pension-benefits); [RAB 2026-1](https://www.michigan.gov/taxes/rep-legal/rab/2026-revenue-administrative-bulletins/revenue-administrative-bulletin-2026-1).

Always subtracted, whatever the route, on Schedule 1 (not Form 4884): Social Security included in AGI, military retirement, railroad retirement, Michigan National Guard retirement. Source: [2026 Withholding Guide](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf).

### The options for 2026

A retiree may choose, each year, any one method for which they qualify (Treasury, Retirement and Pension Benefits; RAB 2026-1, Issue 2):

| Option | Who | What is subtracted |
| --- | --- | --- |
| A. Phase-in subtraction (fully phased in) | Anyone, any birth year | Combined public and private benefits up to $67,610 / $135,220 |
| B. Born before 1946 (Tier 1) | Older spouse born before 1946 | Public benefits in full, private up to the limit left after public benefits |
| C. Qualified public safety retiree | Police, fire, state police, county corrections (and similar federal) and qualifying surviving or divorced spouses | Public benefits from that service in full, plus private up to the limit left |
| D. Michigan standard deduction | Age 67 or older (older living spouse on a joint return) | $20,000 / $40,000 against all income, reduced by the personal exemption and by military, railroad and National Guard subtractions; for people born after 1952, in 2026 to 2028 **not** reduced by the Social Security subtraction (2025 PA 24) |

Notes:
- The limit in option A applies to public pensions too, from all sources combined (federal, Michigan, other states), except option B and C cases (RAB 2026-1, Issue 3). So a retiree born after 1945 with $71,000 of public pensions subtracts only up to the limit; before 2012 that would have been fully exempt.
- The limit **is reduced** by the military compensation and military retirement, railroad retirement and Michigan National Guard retirement subtracted on Schedule 1 (RAB 2026-1, Issue 4). Example: a $40,000 military pension leaves $27,610 of a $67,610 single limit for other retirement benefits; the military pension itself is still subtracted in full.
- Married filing separately uses the single limit.
- A surviving spouse who has not remarried may keep using the older spouse's year of birth if a retirement or Social Security subtraction was claimed on the joint return in the year of death (RAB 2026-1, Issues 9 and 10).
- The deduction for retirement benefits under the earlier tier rules (born 1946 to 1952, and Social Security-exempt employment) remains available where it gives more; with the full phase-in it rarely does. The 2026 Form 4884 sections are not yet published.

### Choosing

1. Compute Michigan taxable income with the best of options A, B or C (the retirement subtraction).
2. If 67 or older, compute it with option D (the standard deduction).
3. Take the route with the lower taxable income. A large pension and little other income favours the retirement subtraction; wages, business or investment income with a small pension favours the standard deduction, especially for those born after 1952 who now also keep the Social Security subtraction.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Born after 1966, retired early with a pension in 2026 | Option A is available (no birth-year gate from 2026), but early distributions do not qualify |
| Public pension above $67,610 single, born after 1945 | Subtract only up to the limit |
| Public pension, born before 1946 | Subtract in full |
| Qualified police or fire retiree, any age | Option C: public benefits in full |
| Born after 1952, 67+, with Social Security and wages | Option D with the Social Security subtraction on top (2026 to 2028) |
| Born 1946 to 1952, using the standard deduction | The PA 24 change applies to those born after 1952 only; the older rules for this group are not changed by it |
| Roth IRA qualified distribution | Not in AGI; nothing to subtract |
| Deferred compensation (457) | Generally not a retirement benefit |
| Rollover from a public plan to an IRA | The rolled-over public benefits keep their character; contributions made directly to the IRA and earnings are private (RAB 2026-1, Issue 8; account records may be asked for) |
| Military pension plus other retirement income | Military pension subtracted in full; the limit for the rest is reduced by it |
| Flow-through entity income received by a retiree | Business income, not retirement income |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Dates of birth | No subtraction until known |
| Public or private source of a 1099-R | Treat as private; ask |
| Public safety service | Assume none; ask |
| Prior joint return for a surviving spouse | Use the survivor's own birth year |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| 1099-R code for an early distribution | Does not qualify |
| Combined pensions above the limit | Part is taxed in Michigan |
| Retiree with Michigan withholding at the full rate on a pension under the limit | MI W-4P may need updating; refund due |
| Both routes close | Show the client both figures |

## Worked cases

**Case 1, a decision: retirement subtraction or standard deduction?** A single taxpayer born in 1954 (age 72 in 2026) has wages of $18,000, a $5,000 pension and $12,000 of Social Security in AGI: AGI $35,000. Personal exemption $5,900.

- Standard deduction route: $20,000 - $5,900 = $14,100 left after the exemption; under 2025 PA 24 it is not reduced by Social Security. Taxable income $35,000 - $5,900 - $12,000 - $14,100 = $3,000; tax $127.50.
- Retirement subtraction route: $35,000 - $5,900 - $12,000 - $5,000 = $12,100; tax $514.25.

Take the standard deduction: $386.75 less tax. (In 2025 the standard deduction would also have been reduced by the $12,000 of Social Security, and the retirement route would have won, as in RAB 2026-1 Examples I and J.)

```oa-check
name: MI 2026 born 1954, standard deduction against retirement subtraction
inputs:
  agi: 35000
  social_security: 12000
  pension: 5000
  exemption: 5900
  standard_deduction: 20000
  rate: 0.0425
steps:
  - residual_standard: max(standard_deduction - exemption, 0)
  - taxable_standard: max(agi - exemption - social_security - residual_standard, 0)
  - taxable_retirement: max(agi - exemption - social_security - pension, 0)
  - tax_standard: taxable_standard * rate
  - tax_retirement: taxable_retirement * rate
  - saving: tax_retirement - tax_standard
expected:
  taxable_standard: 3000
  taxable_retirement: 12100
  tax_standard: 127.50
  tax_retirement: 514.25
  saving: 386.75
```

**Case 2, large pensions above the joint limit.** A married couple filing jointly, both born after 1945, have a $80,000 Michigan public pension and $70,000 of IRA distributions ($150,000 of retirement benefits), $25,500 of taxable Social Security and $5,000 of interest: AGI $180,500. Two exemptions: $11,800. The retirement subtraction is capped at $135,220 (public and private combined). Taxable income $180,500 - $25,500 - $135,220 - $11,800 = $7,980; tax $339.15. Had the older spouse been born before 1946, the $80,000 public pension would be subtracted in full and the IRA up to the $55,220 left, giving the same $135,220 here; the difference shows only when public pensions alone exceed the limit.

```oa-check
name: MI 2026 joint, pensions above the combined limit
inputs:
  public_pension: 80000
  ira: 70000
  social_security: 25500
  interest: 5000
  exemptions: 2
  exemption_amount: 5900
  joint_limit: 135220
  rate: 0.0425
steps:
  - agi: public_pension + ira + social_security + interest
  - subtraction: min(public_pension + ira, joint_limit)
  - taxable: max(agi - social_security - subtraction - exemptions * exemption_amount, 0)
  - tax: taxable * rate
expected:
  agi: 180500
  subtraction: 135220
  taxable: 7980
  tax: 339.15
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| MI-PEN-R-01 | Part-year or nonresident | Refuse |
| MI-PEN-R-02 | Public pension from another state whose reciprocity treatment is in doubt | Refer |
| MI-PEN-R-03 | Separation pay or a disability retirement before retirement age | Refer: plan documents decide |
| MI-PEN-R-04 | Surviving spouse without the prior joint return | Refuse until it is produced |
| MI-PEN-R-05 | Public safety service partly outside the qualifying categories | Refer |
| MI-PEN-R-06 | Roth conversions and their source plan | Refer |
| MI-PEN-R-07 | Inherited IRA received by a non-spouse | Refer: the beneficiary's own birth year and status |
| MI-PEN-R-08 | A tax year other than 2026 | Refuse: limits and the phase-in differ |
| MI-PEN-R-09 | City income tax on retirement income | Detroit: `mi-detroit-individual-return`; other cities refused |
| MI-PEN-R-10 | Social Security-exempt employment sections of Form 4884 | Refer until the 2026 form is published |

## Filing and payment

Complete Form 4884 (2026 edition when published) for the retirement subtraction, or the standard deduction worksheet, and carry the result to MI-1040 Schedule 1; file with the MI-1040 by 15 April 2027. Ask pension payers to withhold on the correct basis using Form MI W-4P. If no MI W-4P is on file, payers withhold 4.25% on all taxable distributions. Source: [2026 Withholding Guide](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf).

## Completion checklist

- Birth years and the governing spouse identified.
- Each 1099-R classed as public or private, qualifying or early.
- Public safety and pre-1946 options checked.
- Combined limit of $67,610 or $135,220 applied.
- Standard deduction route computed if 67 or older, with the PA 24 rule for those born after 1952.
- Lower taxable income chosen; both figures kept in the file.
- Social Security, military and railroad subtracted separately.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Revenue Administrative Bulletin 2026-1 (approved 8 January 2026). Read for Issues 2 to 11: the 2026 full phase-in, public benefits under the limit, the public safety rules, surviving spouses, the $20,000 / $40,000 standard deduction and the 2025 PA 24 Social Security change (Examples I and J). | https://www.michigan.gov/taxes/rep-legal/rab/2026-revenue-administrative-bulletins/revenue-administrative-bulletin-2026-1 | 2026-11-13 |
| Treasury notice: Social Security taxation changes in Public Act 24 of 2025 (17 November 2025). Read for the 2026 to 2028 rule for those born after 1952 aged 67 or older. | https://www.michigan.gov/treasury/reference/taxpayer-notices/2025/11/17/social-security-taxation-changes-in-public-act-24-of-2025 | 2026-11-13 |
| Treasury, Retirement and Pension Benefits. Read for the phase-in table (100% for 2026 and beyond), what qualifies and the choice of methods. | https://www.michigan.gov/taxes/iit/tax-guidance/tax-situations/retirement-and-pension-benefits | 2026-11-13 |
| 2026 Michigan Income Tax Withholding Guide (Form 446). Read for the 2026 limits of $67,610 and $135,220, the $5,900 exemption, the always-exempt benefits and pension withholding. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf | 2026-11-13 |
| Treasury, Tax Year 2025 Information. Read for the 2025 limits used for comparison. | https://www.michigan.gov/taxes/iit/tax-guidance/tax-year-info/tax-year-2025-guidance | 2026-11-13 |
| Treasury notice: 4.25% rate for 2026. Read for the rate. | https://www.michigan.gov/treasury/reference/taxpayer-notices/2026/04/15/425-income-tax-rate-for-individuals-and-fiduciaries-in-2026-tax-year | 2026-11-13 |

Not yet confirmed: the 2026 Form 4884 and its instructions (sections, worksheet lines) were not published when read, so form line numbers are not given; the 2026 amounts for Social Security-exempt employment sections ($15,000 per spouse aged 62 and the $35,000 / $55,000 / $70,000 amounts in the old file are 2025-era figures not re-read); MCL 206.30 itself (legislature.mi.gov returned errors, so it was read as quoted in RAB 2026-1).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mi-pension-retirement-subtraction` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mi-pension-retirement-subtraction. If neither is available, confirm every figure against the official source pages cited above before relying on it.
