---
name: nc-bailey-settlement-retirement
description: "North Carolina tax treatment of retirement income on Form D-400 Schedule S for tax year 2026, centred on the Bailey settlement. A retiree (or survivor) of North Carolina state or local government, or of the federal government including the military, deducts the benefits in full if the retiree had five or more years of creditable service in a qualifying system as of August 12, 1989 (for the State 401(k) and 457 plans, contributed by that date) (G.S. 105-153.5(b)(5); NCDOR Directive PD-99-1). Also covers the uniformed services retirement deduction for 20-year or medically retired members and Survivor Benefit Plan payments (G.S. 105-153.5(b)(5a)), the full Social Security and Railroad Retirement deduction (G.S. 105-153.5(b)(3)), rollovers out of Bailey plans, and the full taxation of private pensions, IRAs and other states' pensions at 3.99%. Trigger on \"Bailey settlement\", \"Bailey exclusion\", \"NC retirement tax\", \"TSERS tax\", \"LGERS tax\", \"NC military retirement deduction\", \"Schedule S l"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nc-bailey-settlement-retirement"
  jurisdiction: "US-NC"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# North Carolina Bailey settlement and retirement income, tax year 2026

> **Source-cited draft.** Built from G.S. 105-153.5 and 105-153.7, NCDOR Directive PD-99-1, the NCDOR page "Bailey Decision Concerning Federal, State and Local Retirement Benefits" and the NCDOR 2025 D-401 instructions, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** North Carolina does not tax retirement benefits from NC state or local government, or from the federal government (including the military), if the retiree had **five or more years of creditable service as of August 12, 1989** in a qualifying system. For the State's 401(k) and 457 plans the test is having **contributed (or contracted to contribute) before August 12, 1989**. These are deducted in full on Schedule S line 20 (2025 numbering). Separately, military retirees with **20 years of service or a medical retirement** deduct their retirement pay on line 21, whatever their service date. **Social Security** is never taxed in NC. Everything else (private pensions, IRAs, 401(k)s, other states' pensions) is taxed at **3.99%** for 2026.

## Scope

In scope: a full-year North Carolina resident (or a survivor beneficiary) with retirement income in 2026: government pensions, State 401(k) and 457 plans, military retired pay, Survivor Benefit Plan payments, Social Security and Railroad Retirement, private plans and IRAs. Output: the Schedule S Part B retirement deductions that flow into D-400 line 9.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The rest of the D-400 (standard deduction, rate, credits) | `nc-income-tax` |
| Federal taxation of the same benefits | federal skills (`us-self-employed-retirement`, `us-secure-2-and-retirement-updates`) |
| Withholding on pensions (Form NC-4P) | refer |

## Ask the client first

1. **Which plan pays each benefit** (TSERS, LGERS, Consolidated Judicial, Legislative, CSRS, FERS, military, State 401(k) or 457, a local plan, a private plan, an IRA)? The 1099-R payer tells you.
2. **Creditable service as of August 12, 1989** in that system (or, for the State 401(k) and 457, whether contributions started before that date). Ask for a service history or letter from the plan.
3. **For military pay: 20 or more years of service, or a medical retirement under 10 U.S.C. Chapter 61?** Or Survivor Benefit Plan payments as a beneficiary?
4. **Was any Bailey money rolled over**, and into what (another qualifying Bailey account, an IRA, a Roth)?
5. **Is the client the retiree or a survivor beneficiary?**

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or date | Source |
| --- | --- | --- |
| Vesting date for Bailey | August 12, 1989 | [NCDOR Bailey page](https://www.ncdor.gov/taxes-forms/individual-income-tax/filing-topics/bailey-decision-concerning-federal-state-and-local-retirement-benefits); [Directive PD-99-1](https://www.ncdor.gov/taxes-forms/individual-income-tax/personal-taxes-division-directives/directive-pd-99-1) |
| Creditable service needed by that date (most systems) | 5 years | [NCDOR Bailey page](https://www.ncdor.gov/taxes-forms/individual-income-tax/filing-topics/bailey-decision-concerning-federal-state-and-local-retirement-benefits) |
| Share of a qualifying Bailey benefit deducted | 100% of the amount in federal AGI | [G.S. 105-153.5(b)(5)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Uniformed services retirement deduction: years served (or medical retirement under 10 U.S.C. Chapter 61) | 20 years | [G.S. 105-153.5(b)(5a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Social Security and Railroad Retirement deducted | 100% of the amount in federal AGI | [G.S. 105-153.5(b)(3)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html) |
| Tax rate on taxable retirement income, 2026 | 3.99% | [G.S. 105-153.7](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html) |
| Settlement fund appropriated for 1989 to 1997 refunds (history) | $799,000,000 | [Directive PD-99-1](https://www.ncdor.gov/taxes-forms/individual-income-tax/personal-taxes-division-directives/directive-pd-99-1) |

### Step 1: why Bailey exists (one paragraph)

Until August 12, 1989, NC exempted state and local government pensions but taxed most federal ones. After *Davis v. Michigan* (US Supreme Court, 1989), the General Assembly taxed all government pensions alike from that date. In *Bailey v. State*, the NC Supreme Court on **May 8, 1998** held that taxing retirees who had five or more years of service on August 12, 1989 impaired their contracts. The case, with *Emory* and *Patton* (federal retirees), was settled; the court approved the settlement on **October 7, 1998**. Vested retirees do not pay NC tax on those benefits in future years ([Directive PD-99-1](https://www.ncdor.gov/taxes-forms/individual-income-tax/personal-taxes-division-directives/directive-pd-99-1)). The deduction is now G.S. 105-153.5(b)(5).

### Step 2: is the plan a qualifying system?

**NC state and local systems** named by the court (Order Regarding Class Definition, 20 November 1998, in PD-99-1): Teachers' and State Employees' Retirement System (TSERS); Local Governmental Employees' Retirement System (LGERS); Consolidated Judicial Retirement System; Legislative Retirement System; Disability Income Plan (short and long term); Supplemental Retirement Income Plan (the State 401(k)); the State law enforcement officers' 401(k); Deferred Compensation Plan (the State 457); National Guard Pension Fund; Sheriffs' Supplemental Pension Fund; Registers of Deeds' Supplemental Pension Fund; local law enforcement officers' supplemental plan; Firemen's and Rescue Squad Workers' Pension Fund; Charlotte Firefighters' Retirement System; Firemen's Supplemental Fund of Hickory; Winston-Salem Police Officers' Retirement System. Other local plans that were tax-exempt before 1989 may also qualify.

**Federal systems**: the Civil Service Retirement System, the Federal Employees' Retirement System, and US military retirement ([NCDOR Bailey page](https://www.ncdor.gov/taxes-forms/individual-income-tax/filing-topics/bailey-decision-concerning-federal-state-and-local-retirement-benefits)).

**Not qualifying**: other states' and their local governments' pensions; local government optional contribution plans (local 457s); 403(b) plans, including the optional retirement program for university employees (TIAA), unless the court later rules otherwise.

### Step 3: was the retiree vested on August 12, 1989?

| Plan | Vested if, by August 12, 1989 |
| --- | --- |
| Most systems (TSERS, LGERS, judicial, legislative, CSRS, FERS, military) | 5 or more years of creditable service in a qualifying system |
| State 401(k) or State 457 | Contributed (or contracted to contribute) to **that** plan; contributions to one do not vest the other |
| Firemen's and Rescue Squad Workers' Pension Fund | 5 years of service **and** 5 years of contributions |
| Sheriffs' or Registers of Deeds' Supplemental Pension Fund | 5 years as sheriff or register (not a deputy or assistant) **and** 5 years in LGERS or an equivalent local plan |

A vested employee who left and later came back stays vested unless they withdrew their contributions ([Directive PD-99-1](https://www.ncdor.gov/taxes-forms/individual-income-tax/personal-taxes-division-directives/directive-pd-99-1)). Bailey is all or nothing: 4 years and 11 months gives no deduction.

### Step 4: deduct on Schedule S

| Benefit | Deduction | 2025 Schedule S Part B line |
| --- | --- | --- |
| Social Security (Title II) and Railroad Retirement (Tier 1 and 2, including railroad unemployment and sickness benefits) included in federal AGI | All of it | Line 19 |
| Vested Bailey benefits included in federal AGI | All of it; attach the 1099-R or W-2 | Line 20 |
| Uniformed services retired pay (20 years, or medically retired under 10 U.S.C. Chapter 61; not separation severance pay), and Survivor Benefit Plan payments to the beneficiary of such a member, not deducted on line 20 | All of it; attach the 1099-R | Line 21 |

The same dollars cannot be deducted under both line 20 and line 21 ([G.S. 105-153.5(b)(5a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html)). Even if all retirement income is deductible, the retiree must still file if gross income meets the filing requirement (2025 D-401).

### Step 5: rollovers

All distributions from a qualifying Bailey account in which the retiree was vested on August 12, 1989 are exempt, whatever the source of the money in it. Bailey money **rolled into another plan loses its character** and is taxable when paid out, unless the receiving plan is itself a qualifying Bailey account in which the retiree was vested. A rollover from a qualifying Bailey account **to a Roth** is exempt in the year of rollover and deducted to the extent it is in federal AGI ([NCDOR Bailey page](https://www.ncdor.gov/taxes-forms/individual-income-tax/filing-topics/bailey-decision-concerning-federal-state-and-local-retirement-benefits); Directives PD-04-1, PD-14-1).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| TSERS retiree hired after August 12, 1984 with no earlier service | Fewer than 5 years by August 12, 1989: not Bailey, fully taxable |
| Federal retiree with CSRS service before 1989 | Bailey if 5 years by August 12, 1989 |
| FERS employee hired after 1984 with no CSRS service | Under 5 years by the date: not Bailey |
| Military retiree with 20 years, service began after 1984 | Not Bailey, but deducts on line 21 |
| Military reservist retired with under 20 years, not medically retired, and under 5 years by 1989 | No deduction |
| Survivor beneficiary of a vested retiree | Bailey applies to the survivor's benefits |
| State 401(k) contributions started June 1989, State 457 in October 1989 | Vested in the 401(k) only |
| Local government 457 plan | Not Bailey |
| 403(b), TIAA optional retirement program | Not Bailey |
| Pension from another state's retirement system | Taxable in NC |
| Bailey money rolled to a private IRA | IRA withdrawals taxable |
| Private pension, 401(k), traditional IRA, SEP or SIMPLE | Taxable; NC has no general retirement exclusion |
| Qualified Roth distribution | Not in federal AGI, so nothing to deduct |
| Social Security | Always deducted in full |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| No proof of service on August 12, 1989 | Do not take line 20 until the plan's service record is in hand |
| Rollover history unknown | Treat IRA withdrawals as taxable |
| Military years of service unknown | No line 21 until confirmed from the retirement documents |

## Worked cases

### Case 1: a married retiree couple with five kinds of income

Married filing jointly, 2026. Income in federal AGI: TSERS pension $36,000 (Bailey vested, service letter on file), military retired pay $14,000 (22 years of Army service), taxable Social Security $15,300, a private 401(k) $24,700 and a traditional IRA $30,000. Federal AGI $120,000. Deductions: line 19 $15,300, line 20 $36,000, line 21 $14,000, total $65,300. NC income $54,700; less the joint standard deduction $25,500: taxable $29,200. Tax at 3.99%: **$1,165.08**. Only the 401(k) and IRA are taxed.

```oa-check
name: NC 2026 retirees, Bailey, military and Social Security
inputs:
  tsers: 36000
  military: 14000
  social_security: 15300
  k401: 24700
  ira: 30000
  std: 25500
  rate: 0.0399
steps:
  - fagi: tsers + military + social_security + k401 + ira
  - deductions: social_security + tsers + military
  - taxable: fagi - deductions - std
  - tax: round(taxable * rate, 2)
expected:
  fagi: 120000
  deductions: 65300
  taxable: 29200
  tax: 1165.08
```

### Case 2: does the TSERS pension qualify? The vesting date decides

A single retiree draws $55,000 from TSERS in 2026 and has no other income. If they started State work on March 1, 1991, they had no service on August 12, 1989: no Bailey deduction, taxable income $42,250 and tax **$1,685.78**. If instead they started on July 1, 1984, they had just over 5 years on the date: the whole $55,000 is deducted and the NC tax is **$0**. The difference is $1,685.78 a year.

```oa-check
name: NC 2026 Bailey vesting decision
inputs:
  pension: 55000
  std: 12750
  rate: 0.0399
  vested_1991_start: 0
  vested_1984_start: 1
steps:
  - tax_not_vested: round(max(pension - pension * vested_1991_start - std, 0) * rate, 2)
  - tax_vested: round(max(pension - pension * vested_1984_start - std, 0) * rate, 2)
  - difference: tax_not_vested - tax_vested
expected:
  tax_not_vested: 1685.78
  tax_vested: 0
  difference: 1685.78
```

## When to refuse or refer

| Situation | Action |
| --- | --- |
| No service record for August 12, 1989, or service near 5 years (purchased or transferred service) | Do not claim line 20; get the plan's written service history and refer if still unclear |
| CSRS and FERS service mixed in one annuity | Refer; the plan must split the benefit |
| Foreign government pension | Refer; treaty questions |
| Part-year resident or nonresident | Refer; Schedule PN |
| Amended returns for years before 2014 (old statute G.S. 105-134.6) | Refer |
| Multi-year Roth conversions or rollovers between several Bailey and non-Bailey plans | Refer |
| A local plan not in the court's list that claims pre-1989 exemption | Refer |

## Filing and payment

| Item | Rule | Source |
| --- | --- | --- |
| Where the deduction goes | Schedule S Part B lines 19, 20, 21 (2025 numbering), total to D-400 line 9 | [NCDOR 2025 D-401](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open) |
| Attachments | The 1099-R or W-2 from the payer for any line 20 or line 21 deduction | [NCDOR Bailey page](https://www.ncdor.gov/taxes-forms/individual-income-tax/filing-topics/bailey-decision-concerning-federal-state-and-local-retirement-benefits); [2025 D-401](https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open) |
| Return due | April 15, 2027 for 2026 | `nc-income-tax` |

## Completion checklist

- [ ] Each 1099-R matched to a plan and classified (Bailey, military, Social Security, taxable)
- [ ] August 12, 1989 service (or contribution) proved for every line 20 amount
- [ ] Military 20 years or Chapter 61 medical retirement confirmed for line 21
- [ ] No amount on both lines 20 and 21
- [ ] Rollover history checked
- [ ] 1099-Rs attached

## Sources

| Source | URL | Read for | Read on |
| --- | --- | --- | --- |
| G.S. 105-153.5 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html | Read for (b)(3) Social Security, (b)(5) Bailey, (b)(5a) uniformed services, standard deduction | 2026-11-13 |
| G.S. 105-153.7 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html | Read for the 3.99% rate | 2026-11-13 |
| NCDOR, Bailey Decision Concerning Federal, State and Local Retirement Benefits | https://www.ncdor.gov/taxes-forms/individual-income-tax/filing-topics/bailey-decision-concerning-federal-state-and-local-retirement-benefits | Read for the vesting test, plans, rollovers, Roth rollovers, attachments | 2026-11-13 |
| NCDOR Directive PD-99-1 | https://www.ncdor.gov/taxes-forms/individual-income-tax/personal-taxes-division-directives/directive-pd-99-1 | Read for the history, court dates, settlement amount, qualifying systems and special vesting rules | 2026-11-13 |
| NCDOR 2025 D-401 instructions | https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open | Read for Schedule S lines 19, 20, 21 and 41 and attachments | 2026-11-13 |

Not yet confirmed: the 2026 Schedule S line numbers (the 2025 numbers are used); Directives PD-00-1, PD-04-1 and PD-14-1 (named on the NCDOR Bailey page, not opened); the "Bailey letter" process at the NC Retirement Systems Division (v0.1 described it; not checked on a Treasurer page); whether NCDOR has accepted purchased service credit toward the 5-year test (v0.1 said so; not found in PD-99-1 as read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nc-bailey-settlement-retirement` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nc-bailey-settlement-retirement. If neither is available, confirm every figure against the official source pages cited above before relying on it.
