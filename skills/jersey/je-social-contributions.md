---
name: je-social-contributions
description: >
  Jersey social security contributions for 2026, covering ordinary monthly
  Class 1 employee and employer contributions, earnings thresholds and caps,
  Class 2 registration and assessment, and long-term care collection. Use
  for Jersey social security, self-employed contributions, minimum earnings,
  startup contributions or the upper earnings limit. Includes selected earnings,
  absence, accommodation, tips, leaving-payment and earnings-rounding rules.
  Explains why Class 2 and long-term care need separate inputs. Exemptions,
  credits, mixed employment, monetary rounding and complete non-monthly
  treatment require further checks. This source-cited draft awaits professional
  review; complete operational contribution outputs remain unfinished.
jurisdiction: JE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-15
version: 1.2
review_status: pending_review
depends_on:
  - workflow-base
  - social-contributions-workflow-base
---

# Jersey social contributions: 2026

## Scope and source conditions

This partial reference covers selected Class 1 rules and routes to the existing Class 2 guide. It does not complete every contributor category, programme, cross-border condition, remittance pattern, penalty or output slot in the social-contributions base. Unknown rules or mandatory outputs hold the dependent amount and complete engagement package. A job title alone does not establish liability.

The fresh [Social Security Law](https://www.jerseylaw.je/laws/current/l_22_1974) capture applies from 1 January 2026; the [Contributions Order](https://www.jerseylaw.je/laws/current/ro_6108) capture from 22 April 2025. Calendar-2026 guidance supplies the indexed amounts. The Law's displayed historical starting figures are subject to annual indexation. Schedule 1A A1 indexes the minimum threshold by minimum wage; paragraph 2 uses the Jersey Index of Earnings for monthly limits. The minimum earnings threshold differs from the lower earnings limit used for supplementation.

## Class 1 earnings and attribution

[Social Security Law Articles 3 to 7 and Schedule 1A paragraph 1](https://www.jerseylaw.je/laws/current/l_22_1974) establish insured classification, contributions and the broad earnings base. It includes wages, salary, fees, bonuses, commission, overtime and other emoluments/benefits, subject to modifying Orders. Article 7 prohibits recovering employer secondary contributions from an employee. Classification, credits, reduced/exempt primary status and foreign-coverage conditions need their evidence.

[Contributions Order Article A2 and Schedule 1](https://www.jerseylaw.je/laws/current/ro_6108) modify earnings and attribution:

| Payment or event | Selected statutory condition |
|---|---|
| Holiday pay | Included unless paid more than one month after termination; the specified insolvency-benefit holiday component has a separate modification |
| Family leave or illness | Employer remuneration during the listed maternity/paternity/adoption/parental leave or illness is included; qualifying employer-policy permanent-health-insurance benefits are included |
| Incapacity benefit reimbursement | Reduce continuing earnings by the incapacity benefit only where the employee agreed to reimburse the employer an equal amount |
| Leaving employment | Exit-month earnings include amounts paid that month and earnings due but unpaid by month end, unless the Minister is satisfied they will not be paid |
| Payment in lieu of notice | The exit-month rule includes it except a payment made after the termination month; the specified insolvency-benefit notice component has a separate modification |
| Director fees | Included for an established Class 1 insured person when paid by the employing company or its connected company; connection uses Income Tax Law Article 3A |
| Tips, gratuities and service charges | Inclusion under paragraph 4 requires employer distribution or another distribution scheme |
| Accommodation/board and lodging | Included at the earnings the employer would have paid had the benefit not been provided; do not substitute an unsupported market rent |
| Employment expenses | Specific and distinct payments of, or contributions towards, expenses incurred in connection with employment are disregarded under paragraph 10; a label alone does not prove those conditions |

Paragraph 13 ordinarily attributes earnings to the month paid. Its holiday-period exception attributes qualifying holiday pay to the month for which it is due, excluding a supplement to the pay rate. Paragraph 2's leaving rules and paragraph 1's absence rules remain separate. Jointly paid spouses/civil partners use the income-tax allocation, or equality where none exists, within paragraph 2(4). Paragraph 2(3) disregards post-death earnings when calculating earlier contribution months.

The [employer guidance](https://www.gov.je/Working/Contributions/Employers/Pages/ScheduleGuide.aspx) requires correction of the relevant return for advance holiday pay, later ordinary wages and qualifying sick-benefit adjustments. Its broad leaving-payment summary does not settle every post-month payment in lieu of notice. Establish payment type, entitlement, timing and the applicable rule before choosing its month or excluding it altogether.

Keep this base separate from income-tax earnings and benefit valuation. Article A4 generally excludes LTC liability/credits from this Contributions Order, apart from its stated Articles 17/18 exceptions. Class 1 exclusions and earnings rounding do not automatically apply to LTC or Class 2.

## Class 1 monthly contributions

First establish insured status, relevant earnings and any exemption or contribution credit. For an ordinary monthly Class 1 case, the [2026 employer schedule](https://www.gov.je/Working/Contributions/Employers/pages/tables.aspx) and [Social Security Law, Schedule 1A](https://www.jerseylaw.je/laws/current/l_22_1974) supply the rates:

| 2026 monthly item | Amount or rate |
|---|---|
| Minimum earnings threshold (MET) | GBP 618 |
| Standard earnings limit (SEL) | GBP 6,062 |
| Upper earnings limit (UEL) | GBP 27,632 |
| Employee primary contribution | 6% up to SEL |
| Employer secondary contribution | 6.5% up to SEL plus 2.5% between SEL and UEL |

Below MET, no Class 1 contribution is due under the ordinary schedule. At or above MET, calculate on the whole relevant earnings up to SEL, not only the excess over MET. Secondary contributions on the upper band stop at UEL. The employee does not pay the secondary contribution.

The [2026 schedule](https://www.gov.je/Working/Contributions/Employers/pages/tables.aspx) and [employer guidance](https://www.gov.je/Working/Contributions/Employers/Pages/ScheduleGuide.aspx) instruct monthly contribution earnings to be rounded **down to whole pounds**. For nonnegative established monthly contribution earnings E, G below is that rounded base. This does not establish fractional-penny contribution, internal fund-allocation or net-pay rounding. Actual amounts with an unknown monetary method remain held.

With established ordinary monthly status and rounded contribution earnings G, the illustrative percentage arithmetic is:

1. If G is below MET, primary and secondary are zero.
2. Otherwise, lower-band earnings are the smaller of G and SEL.
3. Primary is 6% of lower-band earnings.
4. Secondary is 6.5% of lower-band earnings plus 2.5% of the positive excess of the smaller of G and UEL over SEL.

| Rounded monthly G (GBP) | Primary (GBP) | Secondary (GBP) |
|---:|---:|---:|
| 617 | 0 | 0 |
| 618 | 37.08 | 40.17 |
| 1,000 | 60 | 65 |
| 7,062 | 363.72 | 419.03 |
| 27,632 | 363.72 | 933.28 |
| 30,000 | 363.72 | 933.28 |

For GBP 7,062, secondary is GBP 394.03 on GBP 6,062 plus GBP 25 on GBP 1,000. The [2026 schedule](https://www.gov.je/Working/Contributions/Employers/pages/tables.aspx) supplies these thresholds and rates. These selected totals have exact two-decimal arithmetic; they do not establish a general monetary rounding method. Schedule 1A paragraph 3 allocates primary as 0.8% health insurance and 5.2% other contributions; secondary as 1.2% health insurance and 5.3% other contributions below SEL, plus 2.5% above SEL to UEL. The blended totals do not demonstrate complete fund allocation/rounding.

The same 2026 page publishes METs of GBP 143 weekly, GBP 286 fortnightly, GBP 572 four-weekly and GBP 618 monthly. The guidance rounds weekly earnings down to 25p and requires a calendar-month running total for weekly employees so monthly SEL is not exceeded. Its retained GBP 5,450 cumulative example uses an older limit; 2026 SEL is GBP 6,062. Do not copy its old arithmetic, create a weekly ceiling by division, or infer complete fortnightly/four-weekly conversion and rounding. Those mechanics and statutory period mapping remain open before actual non-monthly calculations.

For multiple jobs with one employer, the guidance aggregates earnings. An optional single-service arrangement for multiple employers has separate conditions; without one each employer reports separately. Article 5's ordinary employment-specific liability is subject to modifying law. Establish employers and arrangements before combining earnings or applying one cap.

Class 1 payments are due within 15 days after month end under the same [schedule](https://www.gov.je/Working/Contributions/Employers/pages/tables.aspx).

## Hypothetical Class 1 positions

These 2026 examples assume ordinary primary/secondary liability, established contribution earnings and no other adjustment. Sources are Schedule 1A and the Contributions Order/guidance above. They do not establish ITIS earnings, monetary rounding or complete outputs.

1. **Below the monthly threshold.** Earnings GBP 617.99 round down to GBP 617, below GBP 618. Ordinary illustrated primary and secondary contributions are zero. No credit or benefit entitlement follows.
2. **At the threshold.** Earnings GBP 618.99 round down to GBP 618. The whole base gives GBP 37.08 primary at 6% and GBP 40.17 secondary at 6.5%; only taxing the excess above MET would be wrong.
3. **Monthly earnings rounding.** Earnings GBP 2,100.89 become GBP 2,100, giving GBP 126 primary and GBP 136.50 secondary. This does not round the ITIS base to GBP 2,100.
4. **Qualifying sickness adjustment.** Continued wages GBP 1,500 and incapacity benefit GBP 265.93 satisfy paragraph 1(2)'s reimbursement agreement. Earnings become GBP 1,234.07 and the monthly base GBP 1,234, giving GBP 74.04 primary and GBP 80.21 secondary. Correct the affected absence month's return as applicable. No reduction is inferred without the agreement and qualifying benefit.
5. **Accommodation value.** Cash earnings GBP 1,000 plus GBP 200 that would have been paid without the supplied accommodation give GBP 1,200 contribution earnings, GBP 72 primary and GBP 78 secondary. The GBP 200 is established under paragraph 5, not an assumed market or ITIS value.
6. **Distributed tips.** Salary GBP 1,000 and employer-distributed tips GBP 90 give GBP 1,090 earnings, GBP 65.40 primary and GBP 70.85 secondary. Unknown distribution arrangements do not qualify automatically under paragraph 4.
7. **Ordinary late wages on leaving.** Exit-month wages GBP 4,000 plus ordinary wages GBP 2,900 due for that employment give GBP 6,900 under paragraph 2. Primary is GBP 363.72; secondary is GBP 394.03 plus GBP 20.95 on the GBP 838 upper band, totalling GBP 414.98. Against original amounts GBP 240/GBP 260, adjustments are GBP 123.72 primary and GBP 154.98 secondary. This is not post-month pay in lieu of notice or insolvency benefit.
8. **Weekly base only.** Published guidance changes GBP 567.49 earnings to GBP 567.25. Actual weekly contributions remain held until period/monthly-cap and monetary rounding are verified. Do not invent a weekly SEL or round a contribution to 25p.

## Class 2

Use [je-class2-contributions](je-class2-contributions.md) for insured status, reduced-rate branches, startup concessions and reconciliation. [Social Security Law, Article 3](https://www.jerseylaw.je/laws/current/l_22_1974) and the [Residence Order, Article 2](https://www.jerseylaw.je/laws/current/ro_6081) use school leaving age and prescribed residence conditions with exceptions. Age 18 and 6 months since arrival are not unconditional tests. The [Classification Order, Schedule 1 Part 2](https://www.jerseylaw.je/laws/current/ro_6107) includes low-earnings employment and specified company ownership/control cases; confirm the applicable classification.

The [2026 Class 2 guidance](https://www.gov.je/Working/Contributions/Payments/pages/class2contributionsstatement.aspx) gives annual bands of 12.5% up to GBP 72,744 and 2.5% from there to GBP 331,584, and a full monthly amount of GBP 1,297. [Contributions Order, Articles 13 to 13B and Schedule 2](https://www.jerseylaw.je/laws/current/ro_6108) ordinarily use 2024 income with 2026 limits, but different branches use different deemed earnings. Current salary or total taxable income alone cannot establish a reduced-rate payment.

[Collection Order, Article 6](https://www.jerseylaw.je/laws/current/ro_89_2013) ordinarily requires payment by day 15 of the following month, subject to a verified extension. The Article 13C Class 1 offset applies to its specific low-earnings classification; company ownership alone does not establish it. Article 13D startup concessions require application and qualifying conditions; Article 13E reconciliation uses actual concession-year income and payments. Follow the [dedicated guide](je-class2-contributions.md) and the official notice for the applicable periods and amounts.

## Long-term care

[Funding guidance](https://www.gov.je/Benefits/LongTermCareScheme/pages/funding.aspx) gives a maximum contribution rate of 1.5%, marginal rate of 1.95%, tax allowances and reliefs, and an upper income limit linked to the social security UEL. Revenue Jersey assesses the contribution and includes it in the ITIS effective rate or direct tax payment. A flat 1.5% of uncapped gross salary is not a complete calculation.

## Limits and provenance

Record contributor/employer and period, insured/classification evidence, each payment/benefit, payment and entitlement dates, employment/leaving dates, absence agreements, pay frequency and monthly running totals, exemption/credit notices, separate remittances and corrections. Keep official notices separate from calculator guidance; the calculator expressly cannot override a notice. No missing amount, classification or credit becomes zero by default.

| Code and trigger | Verbatim response |
|---|---|
| R-JE-SOC-1: unknown classification, earnings or source condition | Needs Input: establish the Jersey contributor status, applicable earnings and source conditions before calculating this contribution. |
| R-JE-SOC-2: unresolved period, rounding or notice conflict | Needs Input: verify the contribution period, rounding method and applicable notice before producing the affected amount. |
| R-JE-SOC-3: unsupported remittance allocation or credit | Needs Input: obtain evidence matching this payment or credit to the correct contributor, programme and period. |
| R-JE-SOC-4: incomplete mandatory companion or outputs | Needs Input: the complete Jersey contribution companion and financial package are not ready. |

Every monetary or status decision requires reviewer attention regardless of value; this is review policy. Extend the reviewer brief with status/source evidence, separate programme bases and shares, indexed limits, earnings attribution/rounding, correction month and remittance reconciliation. Recompute caps and compare the same amounts, dates, allocations and holds across every output. Do not issue a completed package while a mandatory rule or output is missing.

Monetary rounding, complete non-monthly conversion, exemptions, credits, pension-age cases and standalone LTC remain research gaps. The dedicated Class 2 guide supplies selected reduced-rate/startup mechanics; complete income mapping, administrative grant conditions, top-up practice, benefits and tax-expense timing remain unresolved. Programme allocation, payment-pattern and penalty coverage is incomplete.

The dated 2026 schedule and current Social Security Law agree on 2.5% for the employer upper band. The generic moving-to-Jersey page says 2%; its conflicting figure is not used. Version 1.2 adds selected earnings/period conditions, earnings rounding and guidance checked on 15 October 2026. Reused Class 2/LTC evidence retains its prior limits. See `references.md` for hashes and periods; this draft awaits professional review.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
