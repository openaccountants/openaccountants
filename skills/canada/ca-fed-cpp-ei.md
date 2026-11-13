---
name: ca-fed-cpp-ei
description: >
  Calculate 2026 Canada Pension Plan contributions and voluntary Employment
  Insurance premiums for a self-employed individual. Use for CPP, CPP2,
  Schedule 8, EI opt-in, Schedule 13, mixed T4 and business income, age
  elections, deductions and contribution overpayments. Separate CPP from
  Quebec QPP and distinguish an annual estimate from filing a published
  return. Confirm the year, province, actual T4 contributions, eligibility
  months and EI agreement before calculating. Do not apply employer payroll
  rates to business profit or assume a missing client fact.
version: 2.2
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-13
depends_on:
  - social-contributions-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Canada self-employed CPP and EI v2.2

## Scope

Calculate annual 2026 CPP and voluntary self-employed EI in CAD, with separate contribution, deduction and credit amounts. This revision is **Built from the law** and **Not yet approved**. An earlier version's professional approval is not approval of these changed rules and figures.

CPP applies to contributory self-employed earnings, not gross sales, company profit or dividends merely because someone owns a company. Confirm residence and pension coverage first. Quebec QPP/QPIP belongs in [qc-individual-return](quebec/qc-individual-return.md); employer withholding belongs in [canada-payroll](canada-payroll.md), with [qc-employer-contributions](quebec/qc-employer-contributions.md) for Quebec payroll. Quebec residents may still participate in federal self-employed EI at its Quebec rate. Do not refuse all EI work merely because QPP replaces CPP. [CPP Act, sections 10 and 13](https://laws-lois.justice.gc.ca/eng/acts/C-8/FullText.html); [Service Canada premiums](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html).

**Year boundary:** the rates below are 2026. On November 13, 2026, CRA's Schedule 8 and Schedule 13 download pages still offer 2025 forms. References to their parts and T1 destinations describe the latest published filing route, not a verified 2026 form layout. Obtain the correct 2026 forms/software before filing. Full-year standalone estimates below are supported; partial-year or complex mixed-income filing needs the applicable current instructions. Never relabel a 2025 PDF as 2026. [Schedule 8](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5000-s8.html); [Schedule 13](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5000-s13.html).

## Ask the client first

- Which tax year, province of residence at year-end and residence periods? Was there employment or self-employment connected with Quebec, another province or another country?
- What is the individual's pensionable net business/professional/partnership income, with the tax computation and business statements? Separate company salary, dividends and any earnings already insured under a special arrangement.
- Obtain every T4, especially pensionable/insurable earnings and CPP, CPP2, QPP, QPP2 and EI actually deducted. Confirm multiple employers, amended slips and any optional-contribution election.
- Obtain date of birth, CPP/QPP retirement and disability pension dates, death if applicable, and the actual election/revocation and effective dates. Do not default missing pension status to compulsory contributions.
- Has Service Canada confirmed an EI agreement? Obtain its date, any cancellation/withdrawal and whether self-employed special benefits were received. An unknown agreement is not proof of zero EI.
- Is the task an annual estimate, a return or an overpayment claim? Obtain prior assessments, instalment reminders, payments and any CRA ruling, religious exemption or certificate of coverage that changes it.

## The method, step by step

### 1. Establish the pensionable and insurable income separately

Reconcile net business income after the relevant tax adjustments, including the person's share of partnership profit. CRA identifies net self-employment amounts on lines 13500, 13700, 13900, 14100 and 14300; partnership and other eligible earnings must also be considered. The old instruction to use T1 line 12200 alone was incomplete. Use the applicable Schedule 8 income reconciliation rather than treating gross receipts, a bank deposit or one return line as the contribution base. [CRA self-employment income](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/self-employment-income-lines-13499-14299-gross-income-lines-13500-14300-net-income.html); [line 22200](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html).

For CPP, a self-employment loss does not refund or reduce CPP correctly paid through employment. Include only the individual's partnership share. Check special treatment for placement-agency earnings, exempt earnings and elections rather than automatically adding every T4 box to business profit. [CRA line 22200](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html).

EI's eligible earnings can differ from CPP's. Schedule 13 includes specific controlling-shareholder employment and exempt-income cases, and excludes qualifying self-employed earnings already insured through T4 arrangements. Obtain the slips and classification before choosing the base. Dividends alone do not create voluntary self-employed EI earnings. [Schedule 13, page 1](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s13/5000-s13-25e.pdf); [CRA line 31217](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31217-employment-insurance-premiums-on-self-employment-other-eligible-earnings.html).

### 2. Select the 2026 rates and ceilings

These are annual full-year values. CPP base and first additional contributions share one earnings band; CPP2 uses a separate upper band. EI has no CPP-style CAD 3,500 exemption. Use the row for 2026 even when a source already displays 2027 above it.

| Item | 2026 value | Official source |
|---|---|---|
| CPP year's maximum pensionable earnings (YMPE) | CAD 74,600 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html |
| CPP basic exemption / first-band contributory maximum | CAD 3,500 / CAD 71,100 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html |
| First-band CPP rate, self-employed / employee | 11.90% / 5.95% | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-enhancement.html |
| Self-employed base / first additional portions | 9.90% / 2.00% | https://laws-lois.justice.gc.ca/eng/acts/C-8/FullText.html |
| Maximum first-band CPP, self-employed / employee | CAD 8,460.90 / CAD 4,230.45 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html |
| CPP additional maximum pensionable earnings (YAMPE) / second band | CAD 85,000 / CAD 10,400 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-enhancement.html |
| CPP2 rate, self-employed / employee | 8% / 4% | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-enhancement.html |
| Maximum CPP2, self-employed / employee | CAD 832 / CAD 416 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html |
| Maximum combined self-employed CPP, derived | CAD 9,292.90 | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-enhancement.html |
| EI maximum insurable earnings | CAD 68,900 | https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/ei-employers/premium-reduction-program/2026-maximum-insurable-earnings.html |
| Voluntary self-employed EI outside Quebec | 1.63%; maximum CAD 1,123.07 | https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html |
| Voluntary self-employed EI for Quebec residents | 1.30%; maximum CAD 895.70 | https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html |
| Federal non-refundable credit percentage | 14%; the credit amount is not a cash refund | https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html |

### 3. Calculate full-year self-employment-only CPP

Use this branch only for non-Quebec CPP coverage, a full contributory year, no pensionable employment and no special election or exemption. Let N be eligible net self-employed earnings, floored at zero for this calculation:

1. First-band earnings A = max(0, min(N, 74,600) minus 3,500).
2. Base CPP = A x 9.90%; first additional CPP = A x 2.00%. Their combined maximum is CAD 8,460.90.
3. Second-band earnings B = max(0, min(N, 85,000) minus 74,600). CPP2 = B x 8.00%, maximum CAD 832.
4. Total CPP = base + first additional + CPP2. Show all three components, not only the total.

Retain calculation precision and round reportable amounts to cents using decimal half-up arithmetic. Do not use binary floating point to decide a half-cent. Reconcile the final amounts to the applicable return instructions. [CPP Act, sections 10, 13 and 16-20](https://laws-lois.justice.gc.ca/eng/acts/C-8/FullText.html); [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html).

### 4. Handle employment plus self-employment without a shortcut

Obtain actual T4 pensionable earnings, box 16 CPP and box 16A CPP2. If there is QPP in boxes 17/17A, select the applicable Schedule 8 or RC381 under CRA's residence and coverage branches. A Quebec resident with QPP only uses the Quebec Schedule 8; mixed CPP/QPP situations use RC381. Load the Quebec personal-return method where needed. The ordinary standalone formula is not sufficient. [CRA line 22200](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html).

The published 2025 Schedule 8 first reconciles employment in Part 3, then mixed income in Part 5; self-employment only uses Part 4. It separates base, first additional and second additional contributions and accounts for employment underpayments/overpayments. Follow the actual form's branching and adjustments, including optional CPT20 contributions where relevant. Do not invent a nine-line substitute or subtract employee CPP just once from a two-share self-employed liability. [2025 Schedule 8, parts 3-5](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf).

For the simple full-year mixed case in Worked case 4, twice the correctly paid employee first-tier CPP reduces the combined first-tier annual limit. That is a reasonableness calculation under the stated assumptions, not a universal Schedule 8 formula. Multiple employers, employment below the exemption, under-deductions, over-deductions, CPP2 on T4s and partial-year eligibility require the full applicable form.

### 5. Split CPP into the deduction and credit base

For the standalone branch, the income deduction equals half the base contribution plus all first additional and second additional contributions. The other half of the base contribution is the non-refundable credit base. Thus deduction = A x 4.95% + A x 2% + CPP2; credit base = A x 4.95%. Never deduct half the combined CPP total and call the other half a credit. [Income Tax Act, paragraph 60(e)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-60.html).

The latest published T1 destinations are line **22200** for the self-employed deduction and **31000** for the base credit amount. Employment enhancement uses its separate deduction, **22215**, rather than being claimed again as self-employed. Use Schedule 8/RC381 outputs for mixed cases. [CRA line 31000](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31000-cpp-qpp-contributions-on-self-employment-other-earnings.html); [2025 Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf).

At the 2026 federal credit percentage, multiply the eligible credit base by 14%, subject to tax otherwise payable. This is separate from the deduction's effect at the person's marginal rate and any provincial credit; do not promise that the credit base itself is refunded. [Income Tax Act, section 118.7](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.7.html); [CRA 2026 rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html).

### 6. Check the voluntary EI agreement and whole-year liability

Self-employed special-benefit participation requires a Service Canada agreement; it does not automatically follow from having a business or paying CPP. It covers qualifying maternity, parental, sickness and caregiving benefits, not regular unemployment benefits. Registration generally must be active for at least 12 months before benefit entitlement; citizenship/permanent residence, eligible earnings, reduced work and benefit-specific conditions also apply. Do not describe 12 months as the only eligibility condition or confuse it with a claim waiting period. [Service Canada eligibility](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/eligibility.html).

EI premiums cover eligible self-employed earnings for the **whole calendar year of entry**, not merely months after registration. If there is no insurable employment, premium = max(0, min(eligible earnings, 68,900)) x the applicable 2026 rate. Do not add an employer 1.4 multiplier. For mixed income, reduce the available annual earnings ceiling by insurable employment earnings and check premiums already paid and the applicable Schedule 13 conditions. A person already at the annual insured ceiling must not pay a second full self-employed maximum. [EI Act, subsection 152.21(2)-(3)](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/page-21.html); [Schedule 13](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s13/5000-s13-25e.pdf).

The latest published Schedule 13 sends the self-employed premium to **42120** as payable and **31217** as the credit base, separate from employment EI on 31200. CPP payable uses **42100**. These do not all come from Schedule 8. [CRA line 31217](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31217-employment-insurance-premiums-on-self-employment-other-eligible-earnings.html); [Schedule 13, page 2](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s13/5000-s13-25e.pdf).

### 7. Apply EI cancellation and withdrawal correctly

Cancellation within 60 days of entering the agreement means no premiums. Withdrawal after that window leaves premiums payable through December 31 of the withdrawal year. It does not refund earlier participation years. Once self-employed special benefits have been **received**, premiums continue for the duration of self-employment and withdrawal is unavailable. Do not replace received with merely applied. A new agreement after cancellation restarts the 12-month qualifying period. The individual can manage withdrawal through MSCA, Employment Insurance, View my agreement status (self-employed). Preserve confirmation before changing the calculation. [Service Canada withdrawal](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/withdraw.html).

## Boundary and exception table

| Situation | Treatment and evidence |
|---|---|
| Under 18, turns 18 or turns 70 | Full-year CPP is not automatic. Contributions start after the 18th-birthday month and include the 70th-birthday month. Someone already 70 at the year's start has no compulsory CPP. Use applicable proration instructions. https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf |
| Retirement pension before 65 | Pension receipt alone does not stop CPP. The working-beneficiary rules continue to apply. https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/cpp/canada-pension-plan-cpp-contributions-cpp-working-beneficiaries.html |
| Age 65 to under 70, receiving CPP/QPP retirement pension, self-employed only | Elect through the applicable Schedule 8 section, not CPT30. Earliest effective month can be the month the person turns 65, with pension receipt confirmed. Obtain the effective date and applicable election deadline; a 2025 election deadline is not a 2026 deadline. https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/cpp/canada-pension-plan-cpp-contributions-cpp-working-beneficiaries.html |
| Same pension condition, employed or mixed income | CPT30 goes to CRA and all employers. Employee cessation is effective the following month. A prior self-employed-only election needs CPT30 if employment starts in a later year. An election cannot be revoked in the same calendar year. Self-employed-only revocation uses Schedule 8; employee/mixed revocation uses CPT30, normally effective the following month. https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/cpp/canada-pension-plan-cpp-contributions-cpp-working-beneficiaries.html |
| Full-year CPP/QPP disability pension | The published Schedule 8 Part 2(b) assigns zero CPP contributory months for a pension received all year. Confirm pension evidence; benefit entitlement and the impact of returning to work are separate. https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf |
| Partial year, disability or death | Do not prorate only CAD 3,500. Published instructions adjust several ceilings and may prorate earnings, with a distinct death rule. Obtain pension/disability dates and current form instructions; do not infer benefit entitlement or its effect from this contribution calculation. https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html |
| Quebec or mixed CPP/QPP | Use the personal QPP method and applicable RC381. Federal voluntary EI remains possible at the Quebec rate; QPIP is separate. Never apply CPP's retirement age/election or rate to QPP. https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html |
| Religious exemption | Verify CRA approval of the individual's CPT16 and membership in a certified sect. CPT17 certifies the sect, not the individual. Do not exempt earnings on religion alone. https://www.canada.ca/en/revenue-agency/services/tax/canada-pension-plan-cpp-employment-insurance-ei-rulings/cpp-ei-explained/canada-pension-plan-members-religious-sects.html |
| Non-resident, foreign work or social-security agreement | Section 10's residence condition and the applicable coverage agreement matter. Canadian-source receipts alone do not prove self-employed CPP liability. Obtain the ruling/certificate and refer unresolved coverage. https://laws-lois.justice.gc.ca/eng/acts/C-8/FullText.html |
| Loss, low income or business starts mid-year | A standalone loss has zero contribution base; it does not erase employment CPP. A business starting mid-year does not by itself justify a birthday-style CPP exemption proration. EI's entry year still uses whole-year eligible earnings. https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html ; https://laws-lois.justice.gc.ca/eng/acts/E-5.6/page-21.html |

## Worked cases

All cases are fictional annual estimates for 2026. CPP cases assume Ontario residence, full-year eligibility, age 40 and no election/disability unless stated. EI is zero only where non-participation is confirmed. The arithmetic checks prove the displayed numbers, not legal eligibility or an unpublished form layout.

### Case 1. CAD 50,000 profit and the EI participation decision

No T4 income. First-band earnings are CAD 46,500: base CPP CAD 4,603.50, enhancement CAD 930 and no CPP2. Total CPP is CAD 5,533.50, deduction CAD 3,231.75 and credit base CAD 2,301.75. Confirmed non-participation gives zero voluntary EI; a qualifying active agreement adds CAD 815 for the year, making contributions CAD 6,348.50. This compares premium cost only; it does not decide whether benefits justify participation.

```oa-check
name: 2026 standalone profit 50000 and EI participation decision
inputs:
  profit: 50000
steps:
  - band: max(0, min(profit, 74600) - 3500)
  - base_cpp: round(band * 0.099, 2)
  - additional_cpp: round(band * 0.02, 2)
  - cpp2: round(max(0, min(profit, 85000) - 74600) * 0.08, 2)
  - cpp: base_cpp + additional_cpp + cpp2
  - deduction: round(base_cpp / 2 + additional_cpp + cpp2, 2)
  - credit_base: round(base_cpp / 2, 2)
  - ei_if_participating: round(min(profit, 68900) * 0.0163, 2)
  - total_if_participating: cpp + ei_if_participating
expected:
  base_cpp: 4603.50
  additional_cpp: 930.00
  cpp2: 0
  cpp: 5533.50
  deduction: 3231.75
  credit_base: 2301.75
  ei_if_participating: 815.00
  total_if_participating: 6348.50
```

### Case 2. CAD 120,000 profit, both CPP ceilings

First-band CPP is capped at CAD 8,460.90; CPP2 is CAD 832, total CAD 9,292.90. The deduction is CAD 5,773.45 and base credit amount CAD 3,519.45. An EI participant with no insurable employment pays the separate CAD 1,123.07 maximum, not an employer premium.

```oa-check
name: 2026 standalone profit 120000 hits CPP and EI ceilings
inputs:
  profit: 120000
steps:
  - band: max(0, min(profit, 74600) - 3500)
  - base_cpp: round(band * 0.099, 2)
  - enhancement: round(band * 0.02, 2)
  - cpp_first: base_cpp + enhancement
  - cpp2: round(max(0, min(profit, 85000) - 74600) * 0.08, 2)
  - total_cpp: cpp_first + cpp2
  - deduction: round(base_cpp / 2 + enhancement + cpp2, 2)
  - credit_base: round(base_cpp / 2, 2)
  - ei: round(min(profit, 68900) * 0.0163, 2)
expected:
  cpp_first: 8460.90
  cpp2: 832
  total_cpp: 9292.90
  deduction: 5773.45
  credit_base: 3519.45
  ei: 1123.07
```

### Case 3. CAD 75,000 profit, just into CPP2

Only CAD 400 lies above YMPE, so CPP2 is CAD 32, not the maximum. Total CPP is CAD 8,492.90. Use both ceilings rather than applying 8% to the whole profit.

```oa-check
name: 2026 profit 75000 between CPP ceilings
inputs:
  profit: 75000
steps:
  - first: round(max(0, min(profit, 74600) - 3500) * 0.119, 2)
  - second: round(max(0, min(profit, 85000) - 74600) * 0.08, 2)
  - total: first + second
expected:
  first: 8460.90
  second: 32
  total: 8492.90
```

### Case 4. Employment CAD 45,000 and self-employment CAD 40,000

Assume one full-year correctly deducted T4, pensionable earnings CAD 45,000, box 16 CAD 2,469.25, no box 16A, no QPP and no shortfall/overpayment. The annual first-tier self-employed remainder is CAD 8,460.90 less twice CAD 2,469.25 = CAD 3,522.40. Combined earnings reach YAMPE, giving CAD 832 self-employed CPP2. The reasonableness total is CAD 4,354.40. Confirm the actual return result through the applicable mixed-income form before filing. Do not treat this limited example as an employment-underpayment algorithm.

If EI participation is confirmed and actual insurable employment is also CAD 45,000, the remaining EI earnings band is CAD 23,900 and self-employed EI CAD 389.57. Do not charge the full standalone maximum again.

```oa-check
name: 2026 simple mixed-income annual reconciliation
inputs:
  employment: 45000
  business_profit: 40000
  t4_cpp: 2469.25
steps:
  - first_limit: (74600 - 3500) * 0.119
  - se_first: round(first_limit - 2 * t4_cpp, 2)
  - se_second: round(max(0, min(employment + business_profit, 85000) - 74600) * 0.08, 2)
  - se_cpp: se_first + se_second
  - remaining_ei_earnings: max(0, 68900 - employment)
  - se_ei: round(min(business_profit, remaining_ei_earnings) * 0.0163, 2)
expected:
  se_first: 3522.40
  se_second: 832
  se_cpp: 4354.40
  remaining_ei_earnings: 23900
  se_ei: 389.57
```

### Case 5. Register for EI in August

Assume no cancellation within 60 days, no T4 insurable earnings and CAD 50,000 eligible self-employed earnings for 2026. Premiums cover the whole year: CAD 815 outside Quebec or CAD 650 for a Quebec resident. They are not five-twelfths of those amounts. Benefit eligibility still requires its own agreement and qualifying tests.

```oa-check
name: 2026 EI entry year uses annual earnings in both regions
inputs:
  annual_eligible_earnings: 50000
steps:
  - non_quebec: round(min(annual_eligible_earnings, 68900) * 0.0163, 2)
  - quebec: round(min(annual_eligible_earnings, 68900) * 0.013, 2)
expected:
  non_quebec: 815
  quebec: 650
```

### Case 6. Floor, loss and age boundaries

With no employment, a full-year CPP-eligible person's CAD 2,500 profit or CAD 5,000 loss gives zero CPP. A person aged 72 throughout 2026 also has no compulsory CPP, even with CAD 80,000 earnings. None of those facts alone proves that voluntary EI is zero or that no tax return is required. A person turning 70 during the year needs the partial-year calculation; it is not the same case.

```oa-check
name: 2026 standalone CPP low income and loss
inputs:
  low_profit: 2500
  loss: -5000
steps:
  - low_cpp: round(max(0, min(low_profit, 74600) - 3500) * 0.119 + max(0, min(low_profit, 85000) - 74600) * 0.08, 2)
  - loss_cpp: round(max(0, min(loss, 74600) - 3500) * 0.119 + max(0, min(loss, 85000) - 74600) * 0.08, 2)
expected:
  low_cpp: 0
  loss_cpp: 0
```

## When to refuse or refer

Calculate supported components and state the missing fact or unresolved coverage; do not assume Ontario, no T4 contributions, no EI agreement or no pension just to return a number. Do not substitute CPP for QPP, promise regular EI benefits, treat a non-refundable credit as cash, or apply an old year's form figures to the current year.

Refer unresolved worker classification, non-residence, international coverage, disability benefit impacts, religious approval and interprovincial contribution disputes to a Canadian practitioner with the relevant facts. For a partial-year or mixed-income filing, obtain the applicable form rather than representing the standalone estimate as a completed return. Record the facts, source, supported calculation, unresolved point and responsible reviewer. Do not invent a named accountant's approval.

## Filing and payment

For an ordinary self-employed individual's 2026 return, filing is due **June 15, 2027**, while the balance is payable **April 30, 2027**. The tax-shelter business exception can make filing due April 30 as well. Confirm death and other special-case deadlines separately. [CRA 2027 deadlines for 2026 income](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html).

Use CRA My Account or an authorized representative and the applicable year's certified software/forms. Reconcile Schedule 8/RC381 and Schedule 13 separately to the T1. Save the submitted return, assessment, payment reference and bank confirmation. Preparation is not submission or payment. CPP and voluntary EI are included in the individual's income-tax balance; they are not employer payroll remittances. [CPP Act, collection of self-employed contributions](https://laws-lois.justice.gc.ca/eng/acts/C-8/FullText.html); [EI Act, sections 152.22-152.26](https://laws-lois.justice.gc.ca/eng/acts/E-5.6/page-21.html).

For 2026, CRA's ordinary instalment test is net tax owing above CAD 3,000 (CAD 1,800 for Quebec) in 2026 and either 2025 or 2024. The tax-owing threshold test and the instalment amount are different: the calculation then adds applicable CPP and voluntary EI. Use the reminder/no-calculation, prior-year or current-year method, not business profit alone. Standard due dates are March 15, June 15, September 15 and December 15, adjusted under CRA's weekend/holiday rule. Farming/fishing and an August-only reminder have separate instructions. [Who pays](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html); [due dates](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html).

### Overpayments and penalties

The latest published non-Quebec CPP overpayment destination is **44800**, through Schedule 8/RC381, including the applicable contribution reconciliation; there is no separate CPP2 line 44801 in that published route. Quebec residents claim remaining pension excess through the Quebec return instead. Check the four-year CPP refund request limit. [CRA line 44800](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44800-cpp-overpayment.html); [line 22200 refund limit](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html).

EI premium overpayment uses **45000**; repayment of EI benefits is a different issue. Quebec EI/PPIP coordination uses the applicable Schedule 10 instructions and may transfer part of the excess to Revenu Quebec. Do not call an EI participation-year premium refundable merely because the person withdrew later. [CRA line 45000](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-45000-employment-insurance-overpayment.html).

CRA charges compound daily interest from the day after the applicable balance-due date; fetch the prescribed quarterly rate for the actual overdue period, rather than hard-code a rate here. The ordinary late-income-tax-return penalty where a balance is owed is 5% plus 1% per full late month, up to 12 months. A demanded return after a recent late-filing penalty can attract 10% plus 2% per full month, up to 20 months, under Income Tax Act subsections 162(1)-(2). Instalment interest/penalties are separate. Do not apply employer remittance penalty bands to a self-employed T1 balance. [CRA interest and penalties](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html); [Income Tax Act, section 162](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html).

### Bank-entry reconciliation

| Description clue | Provisional classification | Evidence needed |
|---|---|---|
| CRA / Canada Revenue Agency / Receiver General / Rec Gen Canada | Possible personal tax payment, instalment or other CRA account | Match account, period and CRA statement; the name alone does not identify a CPP/EI component. |
| CRA instalment / quarterly instalment | Possible T1 instalment asset/payment | Match reminder, payment reference and assessment. Do not split a bank total into guessed CPP and EI. |
| CRA refund / tax refund | Possible tax refund | Reconcile assessment and account; do not assume all of it is pension overpayment. |
| Service Canada / ESDC / EI maternity / EI parental / EI sickness | Possible benefit receipt or adjustment | Obtain benefit statement/T4E. Registration is not inferred from an unidentified payment. |
| RRQ / Retraite Quebec / QPP / RQAP / QPIP | Quebec pension/parental item | Load the correct personal or employer method and match the document before posting. |

These are bookkeeping clues, not statutory counterparty codes. Produce proposed classifications for human approval; make no ledger posting or payment.

## Completion checklist

- Confirm year, province/coverage, actual net earnings and all employment slips; keep CPP, QPP, EI and QPIP distinct.
- Show base CPP, first additional CPP, CPP2, voluntary EI and total separately, with annual limits and eligibility assumptions.
- Reconcile deduction, credit base, payable and overpayment destinations using the applicable published forms. A credit base is not tax saved or a refund.
- Preserve registration, election, exemption and withdrawal evidence. Never manufacture missing client facts or professional approval.
- Match the return and payments to CRA records; retain a working paper with sources, read date, rounding and unresolved items.

## Sources

Read on **2026-11-13**. Official material is in English. The 2026 annual figures are confirmed separately from the still-2025 filing forms.

| Source | Section or table read | Read on |
|---|---|---|
| https://laws-lois.justice.gc.ca/eng/acts/C-8/FullText.html | Read for CPP Act sections 10-20: coverage, components, earnings, ceilings; collection/refunds | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html | Read for 2026 first-band CPP table | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-enhancement.html | Read for 2026 CPP2 ceilings and two-share SE rates | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html | Read for 2026 CPP2 maximum | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5000-s8.html | Read for Schedule 8 year availability | 2026-11-13 |
| https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf | Read for Latest published 2025 contribution/election/mixed-income filing route, not 2026 internal lines | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/self-employment-income-lines-13499-14299-gross-income-lines-13500-14300-net-income.html | Read for Net business income reporting | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html | Read for Partnership/loss rules, CPP/QPP form selection, proration and refund limit; current page refers to 2025 filing | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/cpp/canada-pension-plan-cpp-contributions-cpp-working-beneficiaries.html | Read for Schedule 8 versus CPT30, pension/age/election timing | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/canada-pension-plan-cpp-employment-insurance-ei-rulings/cpp-ei-explained/canada-pension-plan-members-religious-sects.html | Read for CPT16 individual exemption and CPT17 sect certification | 2026-11-13 |
| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-60.html | Read for Deduction under paragraph 60(e); employment enhancement is separate | 2026-11-13 |
| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.7.html | Read for CPP/EI credit base after deduction | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31000-cpp-qpp-contributions-on-self-employment-other-earnings.html | Read for Published base-credit destination | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html | Read for 2026 14% first federal rate | 2026-11-13 |
| https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/ei-employers/premium-reduction-program/2026-maximum-insurable-earnings.html | Read for 2026 EI annual insured ceiling | 2026-11-13 |
| https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html | Read for Federal self-employed EI rates including Quebec | 2026-11-13 |
| https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/eligibility.html | Read for Agreement and special-benefit eligibility | 2026-11-13 |
| https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/withdraw.html | Read for 60-day cancellation and later withdrawal/benefit lock | 2026-11-13 |
| https://laws-lois.justice.gc.ca/eng/acts/E-5.6/page-21.html | Read for Section 152.21: annual and mixed-income premium base; collection | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5000-s13.html | Read for Schedule 13 year availability | 2026-11-13 |
| https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s13/5000-s13-25e.pdf | Read for Published 2025 EI earnings reconciliation and destinations | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31217-employment-insurance-premiums-on-self-employment-other-eligible-earnings.html | Read for EI self-employed credit and payable route | 2026-11-13 |
| https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html | Read for 2027 filing/payment deadlines for 2026 income | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html | Read for 2026 instalment threshold, prior-year test and options | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html | Read for Instalment dates and farming/fishing distinction | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44800-cpp-overpayment.html | Read for Pension overpayment route, including Quebec distinction | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-45000-employment-insurance-overpayment.html | Read for EI premium overpayment versus benefit repayment | 2026-11-13 |
| https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html | Read for Balance interest and ordinary/repeated late-return penalties | 2026-11-13 |

| https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html | Read for subsections 162(1)-(2), ordinary and repeated late-filing conditions | 2026-11-13 |

**Not yet confirmed:** 2026 Schedule 8/13 internal line numbering and final partial-year/mixed-income form implementation are not yet available in the linked form packages. This skill does not calculate benefits, international coverage determinations or a disputed exemption. Those boundaries remain open; a current tax-year header is not proof of complete Canadian coverage.
