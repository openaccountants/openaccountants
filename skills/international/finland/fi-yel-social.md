---
name: fi-yel-social
description: >
  Compute ordinary Finnish self-employed social contributions for tax year 2026.
  Establish YEL eligibility and working-owner classification, confirmed annual work
  income, pension premiums, startup reduction, review transitions and insured-person
  health contributions. Use for YEL income, entrepreneur pension insurance, side
  businesses, family work, company-owner salaries, contribution flexibility and
  pension-payment deductions. Separates the pension provider's contribution from
  tax-collected health contributions, applies substituted YEL bases to prevent
  double charging, and links employee TyEL, unemployment and employer contributions
  to the payroll Guide. Includes statutory source dates, filing/payment and neglect
  procedures and two recomputable examples. Individual benefit awards and MYEL
  agricultural/grant schemes require their own entitlement decisions.
version: 1.6
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - fi-income-tax
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Finland YEL and self-employed social insurance v1.6

**Tax year:** 2026. Ordinary entrepreneur contributions, read together with [employee payroll/social insurance](fi-employer-payroll.md). Independent source-review evidence is in the [pack README](README.md).

## Who this applies to

YEL is required only if all of these hold: the person works in the activity (simply owning a company is not enough); is self-employed, not in an employment or service relationship; has reached the beginning of the calendar month after their 18th birthday and is below the age end for their birth year; the qualifying self-employment has lasted at least four months without interruption; they live in Finland, or live in another EU country while working as self-employed in Finland (the EU Regulation or a social security agreement can displace this); and 2026 annual confirmed income is at least €9,423.09. Self-employment carried on alongside a job, or seasonally, is covered if it meets these conditions: the employment does not remove the YEL obligation, and TyEL for the job and YEL for the business run side by side. Voluntary pension insurance does not replace YEL. The obligation ends at 68 for people born in 1957 or earlier, 69 for 1958–1961, and 70 for 1962 or later, and it ends at the end of the calendar month in which the person reaches that age.

The lower age boundary follows YEL Act section 4(1)(1): turning 18 during a month does not start coverage that day. [YEL Act, section 4](https://www.finlex.fi/fi/lainsaadanto/2006/1272)

The 2026 upper confirmed-income limit is €214,000. A kiosk operated for three months each year can still require YEL where the seasonal activity continues year to year and the other conditions are met: the YEL policy is continuous and valid year round.

Pensioners: a person drawing an old-age or early old-age pension does not have to take out YEL; they may take it out voluntarily. A person drawing a partial old-age pension must keep valid YEL if the self-employment continues. Drawing a disability or unemployment pension does not remove the obligation.

By business form:

- Sole trader (with or without a business name): YEL if the conditions are met. Where both spouses work in the business and it is registered in one spouse's name, both spouses are insured under YEL. For a spouse who is not paid, ETK states the test: the spouse works in the company, has split earnings in taxation, and meets the other YEL conditions. Another unpaid family member working in the business is also self-employed under YEL; a paid family member other than the spouse is insured under TyEL.
- General partnership: each partner who works in the company needs YEL. Limited partnership: the active (responsible) partner who works in it needs YEL; a silent partner is not YEL-insured (TyEL if paid).
- Oy: a shareholder in a senior position needs YEL only where they hold more than 30% alone or more than 50% with family members, of the shares or the votes, directly or through an intermediary company. A shareholder who does not work in the company is not insured. The same more than 30% / more than 50% test applies to a cooperative member in a leadership position.

A light entrepreneur using an invoicing service is, as a rule, self-employed and needs YEL if the work is not totally random and the work input reaches the 2026 limit. The worker can still be in an employment relationship with the ordering party; an employee belongs in TyEL. In unclear employment/YEL cases obtain the Finnish Centre for Pensions applicable-act decision. MYEL agricultural/grant insurance is a separate scheme. [YEL Act, sections 3–4][yel]; [ETK YEL scope][etk].



A paid employee's pension/unemployment/health/accident/group-life duties are computed in the payroll Guide; they are not missing simply because this Guide follows the entrepreneur route. When a person has a separate job and self-employment, assess each activity and aggregate only the bases the particular statute requires. An invoicing service does not turn actual employment into entrepreneurship. Retain contracts, ownership/votes including indirect holdings, family relationship, work evidence, pension status and the applicable-law decision. [YEL Act, sections 3–4][yel]; [TyEL Act, sections 4, 7][tyel].

## Rates, bands and thresholds

| Item | Applicable 2026 figure | Statutory / official source |
|---|---|---|
| Annual confirmed-income minimum / maximum | EUR 9,423.09 / EUR 214,000, indexed statutory values | [YEL Act, sections 4, 89, 112][yel]; [ETK current values][etk]; [Työeläke income][income] |
| Standard pension contribution | 24.40% for all ages | [YEL Act, section 114][yel]; [ETK 2026 contribution][etk] |
| Eligible startup contribution | 78% of standard, i.e. 22% reduction, first 48 qualifying months; second period can use remainder | [YEL Act, section 115][yel] |
| Working Oy manager | More than 30% personally / more than 50% with family shares or votes; indirect-control rules apply | [YEL Act, section 3][yel] |
| Review transition | Specified EUR 4,000 increase cap absent consent; history/transition below | [YEL Act, Acts 1157/2022 and 1400/2025 commencement][yel] |
| Contribution flexibility | Increase 10–100% / decrease 10–20%; decrease at most three of any seven consecutive years; eligibility restrictions apply | [YEL Act, sections 116–117][yel] |
| Ordinary pension accrual | 1.5% of annual pensionable earnings, subject to paid-premium/other pension rules | [YEL Act, sections 61, 67][yel]; [ETK 2026 changes][changes] |
| Health care on work base | 1.10% of the statutory substituted/deducted base | [Health Insurance Act, chapter 18 section 14][health]; [Decree 1026/2025, section 1][health-rates] |
| General daily allowance | 0.88% of full qualifying wage+work base if aggregate annual wage/work income at least EUR 17,255; zero below | [Health Insurance Act, chapter 18 section 15][health]; [Decree 1026/2025, section 2][health-rates] |
| YEL daily-allowance supplement | 0.23% of YEL confirmed income, also below that aggregate threshold, subject to age/coverage | [Decree 1026/2025, section 2][health-rates] |

Do not read nominal base-year statutory euros as current indexed values. Likewise the pension provider's invoice dates, timing adjustment and actual policy-period amount are not a universal annual rate divided by twelve. [YEL Act, sections 89, 114][yel].

## The base

### Value work, then compute premiums

YEL confirmed income is the annual wage reasonably payable to an equally skilled substitute, or equivalent remuneration for the work, determined on an overall assessment. Under section 112 use the relevant sector's full-time median wage together with actual work quantity/value, activity scale, skills and other evidence. Aggregate entrepreneurial work across businesses. Revenue/profit/dividends do not mechanically set confirmed income. Annualise the **work-value assessment** even for a midyear start; the insured period then controls the premium. Obtain the appealable provider decision. [YEL Act, section 112][yel].

Compute standard full-year premium as confirmed annual income × 24.40%; apply an established startup reduction only to eligible months. The initial 48-month rule counts the actual qualifying entrepreneurial history; unused months can be used on a second activity period on request, and compulsory ETK insurance loses this reduction. Retain prior-policy dates, provider eligibility and period calculation. A planned 2028 reform does not change 2026 law. [YEL Act, sections 114–115][yel]; [ETK 2026 rate][etk].

Annual coefficient indexation under section 89 is separate from three-year work-income review under section 112a. Respond to the provider's written proposal within its statutory two-week period with work evidence; absent response the proposal/conditional-decision procedure applies. An increase no more than 5% does not trigger a new-income proposal. Ordinary work-income changes are prospective; section 112a permits a retrospective disability-pension event adjustment. [YEL Act, sections 89, 112a][yel].

For pre-reform confirmed income, the first **two** transitional review increases are capped at EUR 4,000 each unless the entrepreneur consents to more. Act 1400/2025 extends a cap to the first review before 1 January 2029 for income first confirmed to start in 2023–2025. This is a conditional review cap, not an annual guaranteed uplift. For example, qualifying indexed EUR 20,000 income and proposed EUR 27,000, without higher consent, produces EUR 24,000 at that review. Establish current work value and transition eligibility first. [YEL Act, commencement of Acts 1157/2022 and 1400/2025][yel].

Flexibility changes that year's contributions, not permanently confirmed income. Notify the provider in writing during the relevant calendar year. No flexibility when statutory pension is being drawn, YEL arrears exist, the insurance does not continue all year with the same provider or the startup reduction applies. Keep the statutory indexed minimum/maximum premium bounds and the three-of-seven-years restriction on decreases. Pensionable earnings follow paid premiums where flexibility/partial payment/default applies; do not show full accrual on contributions that expire unpaid. [YEL Act, sections 67, 116–117][yel].

### Health: substitute once, distinguish the bases

Health Insurance Act chapter 18 section 14 substitutes confirmed YEL/MYEL income for the specified business earned portion, own-company owner salary/work compensation and other listed entrepreneurial income. Unrelated employment and income not replaced remain under their own rules. For health care, compute the relevant municipal-tax-like deductions on the substituted income, **without deducting YEL/MYEL pension premiums**. Thus care contribution is not invariably gross YEL × 1.10%, and it is never care on both confirmed income and the entrepreneurial income it replaces. For mixed wages/pensions/benefits, compute basic care at `1.10% × established care base C` plus `0.39% × max(0, C − statutory daily-allowance base D)` for the surcharge-eligible income. The §14(2) entrepreneurial receipts are excluded from the 0.39% surcharge: retain their classification rather than treating all care-base excess as pension. A below-threshold daily-allowance payment of zero does not itself make D zero. D includes only actual age/coverage-eligible receipts: from the month after the 16th birthday through the 68th-birthday month. Ordinary wages outside that period can bear the care surcharge; the §14(2) entrepreneur-income exclusion still applies. For an ordinary wage/pension mix with C EUR 35,000, D EUR 30,000 and no excluded entrepreneur receipts, the total is EUR 404.50; compute the substituted entrepreneur route separately under the same statutory exclusion. See the [individual computation](fi-income-tax.md) for the mixed-income sequence. [Health Insurance Act, chapter 18 sections 14–20][health]; [Decree 1026/2025, section 1][health-rates].

For daily allowance, aggregate covered wage income from outside employment and confirmed YEL/MYEL work income under section 15, omitting own-company salary replaced by YEL. If that aggregate is at least EUR 17,255, charge 0.88% on the **whole** qualifying aggregate, not only the excess. Add 0.23% on YEL confirmed income. If the aggregate is below EUR 17,255, the 0.88% component is zero but the YEL 0.23% supplement remains where applicable. This produces 1.11% for a solely YEL base over the threshold, not 1.11% on unrelated wages as well. Apply the actual age/coverage and posting rules. [Health Insurance Act, chapter 18 sections 15–18, 24][health]; [Decree 1026/2025, section 2][health-rates].

These health contributions are collected through personal tax cards/prepayments/assessment, separately from the YEL invoice. A company paying a working owner's actual salary also tests its **employer** health obligation; YEL does not replace it with employer health on confirmed income. An ordinary YEL entrepreneur is outside employee unemployment/TyEL insurance for that same work. Entrepreneur accident cover is a separate voluntary route under Accident Act sections 188 onward; employ staff under their own mandatory cover. [Health Insurance Act, chapter 18][health]; [Employer Health Act, sections 4–5][employer-health]; [Unemployment Financing Act, section 12a][fund-law]; [Accident Act][accident-law].

### Tax deduction and benefit records

Deduct eligible paid YEL once. Where a company pays for the entrepreneur's work, establish its business-expense basis. A sole trader can claim through Form 5, the personal return or the spouse route; section 96 prohibits double use where already deducted in business/agriculture. If business books include the cost but the personal/spouse return claims it, add it back in Form 5. Record payer, payment date, amount, reimbursement and chosen claim location. [Income Tax Act, section 96][ita]; [Business Income Tax Act, sections 7–8][business]; [Vero YEL instructions][deduction].

Confirmed income also affects sickness/parental/unemployment security. Keep the provider decision and history for the relevant benefit authority, but a pension premium calculation is not a benefit award or proof of unemployment-fund entitlement. Employment and entrepreneur benefit contribution/qualification periods and any fund membership need the separate Kela/Fund decision. These benefit-award computations are outside the ordinary **contribution** scope. [ETK YEL scope][etk].

## Deadlines and filing

Arrange the policy within six months of qualifying entrepreneurial work starting, effective from the actual mandatory-coverage start. Choose an earnings-related pension provider or eligible industry pension fund. Retain policy start, confirmed annual income, actual covered days/months, premium decision, startup history and invoice schedule. Report material work changes promptly for a new prospective decision and respond to three-year-review proposals within two weeks. Provider terms determine instalment dates; the monthly equivalent in an example is not a payment instruction. [YEL Act, sections 109, 112–114][yel].

Late arrangement can cover the current and three preceding calendar years. ETK first directs correction and can then arrange insurance at the entrepreneur's expense within that window. Close/alter the policy when qualifying activity ends/changes rather than simply stop paying invoices. Deduction claims/elections follow the personal/business assessment dates in the [income Guide](fi-income-tax.md). [YEL Act, sections 111–112a, 143][yel].

## Penalties and interest

YEL Act section 122 authorises a neglect fee up to the neglected period's pension contribution, determined by the State Treasury on the provider's application using duration, repetition, intent, premium and income. Statutory nonintentional/reasonableness exceptions apply; the maximum is not automatic. Compulsory insurance loses the startup reduction under section 115. Premium default interest follows Interest Act section 4a(1), incorporated by YEL section 123; use the relevant actual period/rate and invoice, not Vero's tax-interest rate. Unpaid/expired contributions can reduce pensionable earnings. [YEL Act, sections 115, 122–123][yel].

Personal tax reporting/late-payment consequences for deductible premiums or health contributions follow the [individual income Guide](fi-income-tax.md); employee reporting/insurance neglect follows the [payroll Guide](fi-employer-payroll.md). Keep these liabilities distinct.

## Cross-border points

Use the actual EU/social-security agreement applicable-law determination and A1 before deciding Finland YEL. Domestic residence or a Finnish company registration alone does not displace foreign applicable law. Multi-state work, posting and transitions require dates and activity in every country; YEL section 4's exclusions and EU/agreements control. For a person with an outside Finnish job plus Finnish self-employment, TyEL and YEL can coexist on the different work, while the health aggregate/substitution rules above prevent double counting. [YEL Act, sections 1, 4][yel]; [ETK applicable-act decisions][applicable].

## Two worked examples that recompute

**1. Standard YEL and a mixed daily-allowance base.** Assume covered confirmed YEL EUR 30,000 for a full year at 24.40%, with no startup/flexibility, plus EUR 20,000 covered outside wages and no replaced own-company wages added twice. YEL is EUR 7,320 (EUR 610 monthly arithmetic equivalent). Aggregate daily-allowance base EUR 50,000 exceeds EUR 17,255: 0.88% gives EUR 440, and 0.23% on YEL gives EUR 69, total EUR 509. Health care requires its separately deducted substituted base; it is not included here.

```oa-check
name: Finland standard YEL and mixed daily allowance base
inputs:
  confirmed_yel_income: 30000
  outside_covered_wages: 20000
steps:
  annual_yel: confirmed_yel_income * 0.244
  monthly_equivalent: annual_yel / 12
  daily_allowance_base: confirmed_yel_income + outside_covered_wages
  general_daily_allowance: daily_allowance_base * 0.0088
  yel_supplement: confirmed_yel_income * 0.0023
  total_daily_allowance: general_daily_allowance + yel_supplement
expected:
  annual_yel: 7320
  monthly_equivalent: 610
  daily_allowance_base: 50000
  general_daily_allowance: 440
  yel_supplement: 69
  total_daily_allowance: 509
```

**2. Confirmed startup reduction.** Assume EUR 30,000 confirmed full-year income and established entitlement to the initial reduction throughout the period, no compulsory-insurance exclusion or flexibility. Standard EUR 7,320 × 78% gives EUR 5,709.60. This does not lower confirmed income or the health base.

```oa-check
name: Finland confirmed startup YEL reduction
inputs:
  confirmed_annual_income: 30000
  contribution_rate: 0.244
  eligible_reduction: 0.22
steps:
  standard_contribution: confirmed_annual_income * contribution_rate
  contribution_after_reduction: standard_contribution * (1 - eligible_reduction)
expected:
  standard_contribution: 7320
  contribution_after_reduction: 5709.60
```

## Ask the client first

1. What are the birth date, pension being drawn, actual work start/duration and countries/applicable-law decisions?
2. What entity, management role, direct/indirect shares/votes and family work/payment facts apply?
3. What annual outsider-wage/work-input evidence and provider confirmed-income decisions support the base?
4. Which prior YEL periods, startup months, review histories, consent, arrears and flexibility decisions exist?
5. What own-company receipts, outside wages and other earned income must be substituted/aggregated for health?
6. Who paid premiums, where were they booked/claimed, and which policy invoices/tax assessments remain to reconcile?

## Sources

| Primary source | Provisions / scope | Read on |
|---|---|---|
| [YEL Act 1272/2006][yel] | Sections 3–4, 61, 67, 89, 109–117, 122–123, 143; review amendments' commencement | 2026-10-26 |
| [ETK self-employed][etk]; [Työeläke confirmed income][income]; [2026 changes][changes] | Indexed 2026 amounts, rate and accrual | 2026-10-26 |
| [Health Insurance Act 1224/2004][health]; [Decree 1026/2025][health-rates] | Chapter 18 sections 14–24; substituted bases and 2026 rates | 2026-10-26 |
| [Employer Health Act 771/2016][employer-health]; [TyEL Act][tyel]; [Unemployment Financing Act][fund-law]; [Accident Act][accident-law] | Working-owner and employee separation; accident voluntary route | 2026-10-26 |
| [Income Tax Act][ita]; [Business Income Tax Act][business]; [Vero YEL deduction][deduction] | Deduct paid premiums once and choose return route | 2026-10-26 |
| [ETK applicable-act decisions][applicable] | Applicable-law determination and disputed worker status | 2026-10-26 |

Not yet confirmed: separately scoped MYEL/agriculture/grant cases, multi-country applicable-law disputes and individual social-benefit awards. Current contribution source-review evidence is recorded in the pack README; no professional attestation is claimed.

[yel]: https://www.finlex.fi/fi/lainsaadanto/2006/1272
[etk]: https://www.etk.fi/en/finnish-pension-system/pensions/pension-coverage-and-insurance/self-employed/
[income]: https://www.tyoelake.fi/en/pensions-for-the-self-employed/what-is-yel-income/
[changes]: https://www.etk.fi/en/topical-issues/how-earnings-related-pensions-will-change-in-2026/
[health]: https://www.finlex.fi/fi/lainsaadanto/2004/1224
[health-rates]: https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2025/1026
[employer-health]: https://www.finlex.fi/fi/lainsaadanto/2016/771
[tyel]: https://www.finlex.fi/fi/lainsaadanto/2006/395
[fund-law]: https://www.finlex.fi/fi/lainsaadanto/1998/555
[accident-law]: https://www.finlex.fi/fi/lainsaadanto/2015/459
[ita]: https://www.finlex.fi/fi/lainsaadanto/1992/1535
[business]: https://www.finlex.fi/fi/lainsaadanto/1968/360
[deduction]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/taxation-of-self-employed-individuals/deductions/pension-premiums-yel/
[applicable]: https://www.etk.fi/en/finnish-pension-system/pensions/pension-coverage-and-insurance/decision-on-the-applicable-earnings-related-pension-act/

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
