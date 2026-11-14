---
name: us-self-employed-retirement
description: "Compute the 2026 US retirement plan deduction for a sole proprietor or single-member LLC owner with no employees, and choose between a SEP IRA, a solo 401(k), a SIMPLE IRA and a traditional or Roth IRA. Uses the 2026 limits from IRS Notice 2025-67 ($24,500 elective deferral, $8,000 catch-up at 50, $11,250 at ages 60 to 63, $72,000 annual additions, $360,000 compensation cap, $17,000 SIMPLE, $7,500 IRA plus $1,100) and the IRS Publication 560 self-employed worksheet (the 20% reduced rate on net profit less the deductible half of self-employment tax). Covers the traditional IRA deduction phase-outs and Roth IRA income limits for 2026, set-up and contribution deadlines, and the effect on QBI. Trigger on \"SEP IRA\", \"solo 401(k)\", \"self-employed retirement\", \"how much can I put in\", \"Schedule 1 line 16\", \"SIMPLE IRA\", \"IRA deduction\". Load after us-schedule-c-and-se-computation. Federal only."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-self-employed-retirement"
  jurisdiction: "US"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# US self-employed retirement contributions, tax year 2026

> **Source-cited draft.** Built from IRS Notice 2025-67, IRS Publication 560 (the 2025 edition, the latest printed), Schedule 1 (Form 1040) 2025 and 26 U.S.C. 219, 401, 402, 404, 408, 408A, 414 and 415, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 a self-employed person's plan "compensation" is net profit less the deductible half of self-employment tax. The employer contribution to a SEP or to the profit-sharing side of a solo 401(k) is at most 20% of that amount (the 25% plan rate reduced to 0.25 / 1.25). A solo 401(k) adds elective deferrals of up to **USD 24,500**, plus a catch-up of **USD 8,000** at age 50 or over or **USD 11,250** for ages 60 to 63. Deferrals plus employer contributions cannot exceed **USD 72,000** (catch-ups sit on top), nor the person's earned income. The pre-tax amount is deducted on Schedule 1 (line 16 on the 2025 form) and reduces QBI; it does not reduce self-employment tax.

## Scope and who this is for

In scope, for tax year 2026: one self-employed individual with Schedule C income and no common-law employees, choosing and computing a SEP IRA, a one-participant (solo) 401(k), a SIMPLE IRA, and traditional or Roth IRA contributions.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Schedule C net profit and the deductible half of self-employment tax | `us-schedule-c-and-se-computation` |
| Catch-up rules in detail, the Roth catch-up for higher-paid employees, RMDs, inherited accounts, QCDs, 529-to-Roth, Saver's Credit and Saver's Match | `us-secure-2-and-retirement-updates` |
| Health insurance deduction, which uses this result | `us-self-employed-health-insurance` |
| QBI, which this deduction reduces | `us-qbi-deduction` |
| Owner with an S corporation (contributions on W-2 wages) | `us-form-1120-s-s-corporation-return` |
| Defined benefit and cash balance plans, plans with employees | refer (see the refusal table) |

## Ask the client first

1. **Age at 31 December 2026** (for the catch-up band) and filing status.
2. **Which plans exist** and when each was adopted. For a new solo 401(k), the adoption date; for an existing one, whether the 2026 deferral election was made by 31 December 2026.
3. **W-2 jobs:** elective deferrals already made to any employer 401(k), 403(b) or SIMPLE in 2026 (the USD 24,500 limit is shared per person), and whether the person was an active participant in an employer plan.
4. **Roth or pre-tax:** whether deferrals are designated Roth (no deduction) and whether the plan offers Roth employer contributions.
5. **Other self-employment:** every Schedule C and partnership with self-employment income, since net earnings are combined and a loss reduces them.
6. **IRA facts:** modified AGI estimate, existing pre-tax IRA balances (for the pro-rata rule on a backdoor Roth), and spouse's earned income for a spousal IRA.
7. **Plan assets** at the end of 2026, for the Form 5500-EZ test.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| Elective deferral limit, 401(k) including solo 401(k), per person across all plans | USD 24,500 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Catch-up, age 50 or over at year end | USD 8,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Catch-up, attains age 60, 61, 62 or 63 in 2026 (if the plan offers it) | USD 11,250 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Annual additions limit (deferrals plus employer contributions, before catch-ups), section 415(c) | USD 72,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Compensation limit, sections 401(a)(17) and 408(k) | USD 360,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth catch-up wage threshold (2025 FICA wages from the plan sponsor) | USD 150,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SEP participation compensation threshold | USD 800 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE IRA or SIMPLE 401(k) deferral limit | USD 17,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE deferral limit for certain plans with the higher limit | USD 18,100 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE catch-up, age 50 or over | USD 4,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE catch-up in certain higher-limit plans, age 50 or over | USD 3,850 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE catch-up, ages 60 to 63 | USD 5,250 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| SIMPLE employer match, or nonelective contribution | up to 3% of compensation, or 2% | [26 U.S.C. 408(p)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408.htm) |
| SEP and profit-sharing plan contribution rate on compensation | up to 25% | [26 U.S.C. 404(a)(3) and (h)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec404.htm) |
| Reduced rate for the self-employed at a 25% plan rate (0.25 / 1.25) | 20% | [Pub. 560, Rate Table for Self-Employed](https://www.irs.gov/pub/irs-pdf/p560.pdf) |
| IRA contribution limit, traditional and Roth combined | USD 7,500 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| IRA catch-up, age 50 or over | USD 1,100 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Traditional IRA deduction phase-out, active participant, single or head of household | USD 81,000 to 91,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Traditional IRA deduction phase-out, active participant, married filing jointly | USD 129,000 to 149,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Traditional IRA deduction phase-out, not active but spouse is | USD 242,000 to 252,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Traditional IRA deduction phase-out, married filing separately, active participant | USD 0 to 10,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth IRA contribution phase-out, single or head of household | USD 153,000 to 168,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth IRA contribution phase-out, married filing jointly | USD 242,000 to 252,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |
| Roth IRA contribution phase-out, married filing separately | USD 0 to 10,000 | [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf) |

The age for the catch-up bands is the age at the end of 2026: people born 1963 to 1966 get the ages 60 to 63 catch-up. The details are in `us-secure-2-and-retirement-updates`.

### Step 1: the plan compensation (Pub. 560 Deduction Worksheet, steps 1 to 3)

1. Step 1: net profit from Schedule C line 31 (all self-employment businesses, combined; a loss in one reduces the total).
2. Step 2: the deductible half of self-employment tax (Schedule 1, line 15), from `us-schedule-c-and-se-computation`.
3. Step 3: net earnings for the plan = step 1 − step 2. Do not subtract the health insurance deduction. Source: [Pub. 560](https://www.irs.gov/pub/irs-pdf/p560.pdf) and [26 U.S.C. 401(c)(2)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec401.htm).

### Step 2: the employer contribution (SEP or profit-sharing)

4. The reduced rate is plan rate / (1 + plan rate): 20% at a 25% plan rate. The circularity is that the owner's compensation is itself reduced by the contribution; the reduced rate solves it. Never apply 25% to step 3.
5. Employer contribution = the smallest of: step 3 x the reduced rate; the plan rate x USD 360,000 (USD 90,000 at 25%); and the USD 72,000 dollar limit. Source: [Pub. 560](https://www.irs.gov/pub/irs-pdf/p560.pdf) and [Notice 2025-67](https://www.irs.gov/pub/irs-drop/n-25-67.pdf).

### Step 3: solo 401(k) deferrals

6. Deferrals (pre-tax and Roth together) are at most USD 24,500 less any deferrals made to other employers' plans in 2026.
7. With deferrals, the employer contribution is also limited to USD 72,000 less the deferrals, and to one-half of (step 3 − deferrals), so the total cannot exceed earned income. The deferral is then limited to step 3 less the employer contribution. These are steps 9 to 15 of the Pub. 560 worksheet.
8. Add the catch-up for the age band. It is above the USD 72,000 limit, and limited by what is left of step 3.

### Step 4: SIMPLE IRA

9. Deferrals up to USD 17,000 (USD 18,100 in higher-limit plans), plus the catch-up for the age band, plus either a match of up to 3% of net earnings or a 2% nonelective contribution on compensation up to USD 360,000. A SIMPLE IRA must be the only plan the employer maintains for the year.

### Step 5: IRAs on top

10. A traditional or Roth IRA contribution of up to USD 7,500 (USD 8,600 at 50 or over) can be made in addition, but needs earned income (a spousal IRA can use the spouse's). A SEP, solo 401(k) or SIMPLE makes the owner an active participant, so the traditional IRA deduction phases out across the ranges in the table; a nondeductible contribution goes on Form 8606. The Roth phase-out uses modified AGI.

### Step 6: where it goes

11. Pre-tax SEP, SIMPLE and solo 401(k) amounts for the owner go on Schedule 1 (line 16 on the 2025 form); a deductible traditional IRA on line 20. Roth deferrals and Roth IRA contributions are not deducted and do not reduce QBI. Contributions for employees go on Schedule C line 19. Source: [Schedule 1 (Form 1040)](https://www.irs.gov/pub/irs-pdf/f1040s1.pdf).
12. Pass the deduction to `us-self-employed-health-insurance` (Form 7206 line 9) and `us-qbi-deduction`.

### Which plan

For a person with no employees, a solo 401(k) gives at least as much as a SEP at every income, because it adds deferrals to the same employer amount. With step 3 between about USD 40,800 and USD 237,500 the solo 401(k) allows the full USD 24,500 more than a SEP (below about USD 40,800 the earned income cap trims it). The solo 401(k) reaches USD 72,000 when step 3 is USD 237,500 (20% x 237,500 = 47,500, plus 24,500); a SEP reaches USD 72,000 only at step 3 of USD 360,000, so the gap narrows between those two points. A SEP is simpler, has no Form 5500-EZ, and can be set up and funded after year end up to the extended due date, so it is the fallback when the deferral election deadline was missed. A SIMPLE IRA rarely suits a person with no employees.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Schedule C loss, or step 3 is zero | No self-employed plan contribution; an IRA needs other earned income |
| Deferrals at a W-2 job already USD 15,000 | Solo 401(k) deferral limited to USD 9,500; employer contributions are per plan |
| Age 59 at 31 December 2026 | Age-50 catch-up only (USD 8,000) |
| Turns 64 in 2026 | Back to the USD 8,000 catch-up |
| Self-employment income only, no FICA wages | The Roth catch-up rule does not apply (see `us-secure-2-and-retirement-updates`) |
| SEP | No deferrals, so no catch-up; Roth SEP contributions only if the plan allows them |
| Part-year self-employment | Limits are not prorated; step 3 still caps the total |
| Existing solo 401(k), deferral elected after 31 December 2026 | Not allowed for 2026; only the employer contribution |
| New solo 401(k) adopted after year end by the return due date | Treated as adopted on 31 December 2026; first-year deferrals allowed if paid by the unextended due date (15 April 2027) |
| SIMPLE IRA within 2 years of first participation | Rollover limits apply, and the early distribution tax is 25%, not 10% |
| Spouse with no earned income, joint return | Spousal IRA up to the IRA limit, if combined earned income covers both |
| Plan assets above USD 250,000 at year end | Form 5500-EZ due by 31 July 2027 for a calendar plan year |
| Common-law employees | Coverage and nondiscrimination rules: refer |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Plan type | Solo 401(k) only if an adoption date is documented; otherwise SEP |
| Age | Under 50 (no catch-up); ask |
| Solo 401(k) deferral election date | Treat as not made in time; employer contribution only |
| Roth or pre-tax | Pre-tax (deductible); confirm with the plan statement |
| Modified AGI for the IRA tests | Treat as above the phase-outs (no deductible IRA, no Roth recommendation) |
| Existing pre-tax IRA balances | Assume some exist, so the pro-rata rule applies to any backdoor Roth |
| Amount to contribute | Compute the maximum and let the client choose |
| SIMPLE against other plans | Do not default to a SIMPLE |

### Red flags for the reviewer

| Flag | Why it matters |
| --- | --- |
| Total contributions above USD 50,000 | Check the USD 72,000 limit and step 3 |
| Solo 401(k) adopted late in 2026 or after year end | Check the deferral election and deposit dates |
| Step 3 below USD 24,500 | The earned income cap binds |
| Age 60 to 63 | Check the plan offers the higher catch-up |
| More than one plan, or a W-2 401(k) as well | The deferral limit is shared |
| Backdoor Roth intended | Pro-rata rule under section 408(d)(2) |
| Modified AGI near an IRA phase-out | Small income changes move the result |
| Plan assets near USD 250,000 | Form 5500-EZ duty |

## Worked cases

**Case 1, a decision: SEP or solo 401(k)?** A single consultant aged 45 has 2026 Schedule C net profit of USD 100,000, no wages and no other plan.

Deductible half of self-employment tax: USD 100,000 x 92.35% x 15.3% / 2 = USD 7,064.78. Step 3: USD 92,935.23. Employer contribution: 20% = USD 18,587.05, well under USD 72,000 and the USD 90,000 compensation-cap amount. SEP: USD 18,587.05. Solo 401(k): USD 24,500 + USD 18,587.05 = USD 43,087.05, within USD 72,000 and within step 3. The solo 401(k) lets her put away USD 24,500 more; at a 22% income tax rate the deferral saves about USD 5,390 more income tax this year. Choose the solo 401(k) if the 2026 deferral election can still be made by 31 December 2026 (or the plan is new and adopted by the return due date); otherwise a SEP by the extended due date.

```oa-check
name: SEP against solo 401(k), age 45 (2026)
inputs:
  net_profit: 100000
  deferral_limit: 24500
  dollar_limit: 72000
steps:
  - half_se: net_profit * 0.9235 * 0.153 / 2
  - step_3: net_profit - half_se
  - employer: min(step_3 * 0.20, 360000 * 0.25, dollar_limit)
  - sep_total: employer
  - solo_total: min(deferral_limit + employer, dollar_limit, step_3)
  - solo_advantage: solo_total - sep_total
expected:
  half_se: 7064.78
  step_3: 92935.23
  employer: 18587.05
  sep_total: 18587.05
  solo_total: 43087.05
  solo_advantage: 24500.00
```

**Case 2: low profit, the earned income cap.** A part-time photographer aged 30 has 2026 net profit of USD 20,000 and a solo 401(k), and elects deferrals of USD 15,000.

Deductible half: USD 20,000 x 92.35% x 15.3% / 2 = USD 1,412.96. Step 3: USD 18,587.05. The 20% employer figure would be USD 3,717.41, but with deferrals the employer contribution is also capped at one-half of (USD 18,587.05 − USD 15,000) = USD 1,793.52. Total: USD 16,793.52, which leaves step 3 not exceeded. (The old version of this skill allowed deferral plus the full 20%, a total above her earned income.)

```oa-check
name: Solo 401(k) earned income cap (2026)
inputs:
  net_profit: 20000
  deferral: 15000
  dollar_limit: 72000
steps:
  - half_se: net_profit * 0.9235 * 0.153 / 2
  - step_3: net_profit - half_se
  - employer_20: step_3 * 0.20
  - employer: min(employer_20, dollar_limit - deferral, (step_3 - deferral) / 2)
  - total: deferral + employer
expected:
  half_se: 1412.96
  step_3: 18587.05
  employer_20: 3717.41
  employer: 1793.52
  total: 16793.52
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-RET-DB | Defined benefit or cash balance plan | Needs an actuary; can exceed the section 415(c) limit: refer |
| R-RET-EMPLOYEES | The business has common-law employees | Coverage, nondiscrimination and top-heavy rules: refer to a plan administrator |
| R-RET-EXCESS | Contributions above a limit | 6% excise tax under section 4973 for IRAs, plan corrections for 401(k) and SEP: refer |
| R-RET-RMD | Age 73 or over, or distributions | Use `us-secure-2-and-retirement-updates` |
| R-RET-ROTHCONV | Roth conversion or backdoor Roth mechanics | Flag only: pro-rata rule, state tax, premium tax credit and Medicare effects; refer |
| R-RET-PARTNER | Partner or S corporation owner | Different compensation base: refer or use the entity skill |

Never apply the 25% rate directly to a sole proprietor's net earnings. Never allow deferrals plus employer contributions above step 3 or above USD 72,000 (catch-ups aside). Never give a catch-up outside the age band. Never extend the IRA deadline with a filing extension. Never treat Roth amounts as deductible.

## Filing and payment

| Action, 2026 plan year | Deadline |
| --- | --- |
| Adopt a new solo 401(k) | By the due date of the 2026 return, including extensions; treated as adopted on 31 December 2026 |
| Elect deferrals to an existing solo 401(k) | By 31 December 2026 |
| Deposit deferrals of a sole owner's new plan in its first year | By the unextended due date, 15 April 2027 |
| Deposit deferrals (other cases) and employer contributions | By the return due date including extensions (15 October 2027 if extended) |
| Set up and fund a SEP | By the return due date including extensions |
| Set up a SIMPLE IRA for 2026 | By 1 October 2026 (later only for a business started after that date) |
| Traditional and Roth IRA contributions for 2026 | By 15 April 2027; an extension does not help |
| Form 5500-EZ, if plan assets exceed USD 250,000 | 31 July 2027 for a calendar plan year |

The deduction is claimed on the 2026 Form 1040, Schedule 1. Nondeductible IRA contributions go on Form 8606. Sources: [Pub. 560](https://www.irs.gov/pub/irs-pdf/p560.pdf), [26 U.S.C. 401(b)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec401.htm), [26 U.S.C. 219(f)(3)](https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec219.htm).

## Completion checklist

- Step 3 computed from net profit less the deductible half, with no health insurance deduction taken off.
- Reduced rate used (20% at 25%), and the USD 360,000 and USD 72,000 caps applied.
- Deferral limit shared with any W-2 plan, and the earned income cap applied.
- Catch-up matched to the age at 31 December 2026 and to the plan terms.
- Deferral election and adoption dates documented.
- IRA deduction and Roth eligibility tested against the 2026 phase-outs.
- Roth amounts kept out of the deduction and out of the QBI reduction.
- Result passed to Form 7206 line 9 and to the QBI computation.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IRS Notice 2025-67. Read for the 2026 limits: $24,500 deferrals, $8,000 and $11,250 catch-ups, $72,000 section 415(c), $360,000 compensation, $150,000 Roth catch-up wage threshold, $800 SEP threshold, SIMPLE $17,000, $18,100, $4,000, $3,850, $5,250, IRA $7,500 and $1,100, and the IRA and Roth phase-out ranges. | https://www.irs.gov/pub/irs-drop/n-25-67.pdf | 2026-11-13 |
| IRS Publication 560 (2025, latest printed). Read for the Rate Table and Deduction Worksheet for Self-Employed (steps 1 to 21) and the plan deadlines. | https://www.irs.gov/pub/irs-pdf/p560.pdf | 2026-11-13 |
| Schedule 1 (Form 1040) 2025. Read for lines 15, 16 and 20. | https://www.irs.gov/pub/irs-pdf/f1040s1.pdf | 2026-11-13 |
| 26 U.S.C. 401 (govinfo). Read for (b) late adoption and (c)(2) earned income of the self-employed. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec401.htm | 2026-11-13 |
| 26 U.S.C. 404 (govinfo). Read for the 25% deduction limit and (h) SEPs. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec404.htm | 2026-11-13 |
| 26 U.S.C. 408 (govinfo). Read for (k) SEPs and (p) SIMPLE match and nonelective contributions. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartA-sec408.htm | 2026-11-13 |
| 26 U.S.C. 219 (govinfo). Read for (f)(3) the IRA contribution deadline and (g) the active participant phase-out. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapB-partVII-sec219.htm | 2026-11-13 |
| 26 U.S.C. 415 (govinfo). Read for (c)(1) the dollar limit and the 100% of compensation limit. | https://www.govinfo.gov/content/pkg/USCODE-2024-title26/html/USCODE-2024-title26-subtitleA-chap1-subchapD-partI-subpartB-sec415.htm | 2026-11-13 |

Not yet confirmed: the 2026 edition of Publication 560 and the 2026 Schedule 1 were not published when read, so worksheet step numbers and line numbers are from the 2025 editions; the break-even profit figures in "Which plan" are rounded and computed here, not printed by the IRS.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-self-employed-retirement` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-self-employed-retirement. If neither is available, confirm every figure against the official source pages cited above before relying on it.
