---
name: au-payroll-tax
description: >
  Use this skill for any Australian state or territory payroll tax question in
  New South Wales, Victoria, Queensland, Western Australia, South Australia,
  Tasmania, the ACT or the Northern Territory: registration thresholds, rates,
  deductions and phase-outs, grouping, contractor and employment agency
  provisions, nexus rules for interstate and overseas workers, taxable wages,
  exempt allowances, surcharges and levies, and monthly and annual return due
  dates. Trigger on "payroll tax", "payroll tax threshold", "payroll tax rate",
  "designated group employer", "relevant contract", "payroll tax grouping",
  "mental health levy", "payroll tax nexus", "annual reconciliation". Covers the
  2026-27 financial year for employers, payroll staff and advisers.
version: 1.0
jurisdiction: AU
tax_year: 2026
tax_year_notes: "2026-27 income year (1 July 2026 to 30 June 2027)"
last_updated: 2026-09-27
review_status: pending_review
depends_on:
  - australia-payroll
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# AU Payroll Tax

## Australia State and Territory Payroll Tax v1.0

> **General reference only.** This skill is general tax and accounting reference material for
> AI-assisted workflows. It has not been reviewed for any specific person's facts, documents,
> elections, deadlines, residency, filing status or local procedures. Do not rely on it to
> lodge, pay, amend or take a tax position without review by a qualified professional.

## Section 1 - Quick Reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Australia, all eight states and territories |
| Financial year covered | 2026-27 (1 July 2026 to 30 June 2027) |
| What is taxed | Taxable wages paid by an employer or group above the jurisdiction's threshold, self-assessed |
| Who administers it | Each state and territory revenue office; the ATO has no role |
| Harmonised areas | Return timing, motor vehicle and accommodation allowances, fringe benefits, work performed outside a jurisdiction, employee share schemes, super for non-working directors and grouping; WA aligned its provisions from 1 July 2012 |
| Registration trigger | Australia-wide taxable wages exceed the jurisdiction's monthly threshold |
| Monthly return | Due on the 7th of the following month |
| Annual return | Due 21 July, or 28 July in the ACT, NSW and SA |
| Annual thresholds 2026-27 | $1.0m in VIC and WA, $1.2m NSW, $1.25m TAS, $1.3m QLD, $1.5m SA, $1.75m ACT, $2.5m NT |
| Records | Keep for at least five years, in English, available on request |
| Reviewed by | Pending. Australian CPA or CA review required |

## Section 2 - The calculation workflow

**Step 1. Identify taxable wages.**
Wages is defined broadly: salary, allowances, bonuses, commissions, director's fees,
superannuation contributions, the grossed-up value of fringe benefits, employment termination
payments, shares and options, payments to contractors under relevant contracts and payments by
employment agents to on-hired workers. See Section 4.

**Step 2. Assign each employee's wages to a jurisdiction.**
Apply the nexus rules month by month. See Section 6.

**Step 3. Test grouping.**
Related corporations, common control, shared employees and traced interests form a group that
shares one threshold and is jointly and severally liable. See Section 7.

**Step 4. Work out the threshold or deduction.**
Apportion it for part-year employment and for the share of Australian wages paid in the
jurisdiction, then apply the jurisdiction's phase-out or diminishing formula. See Section 3 and
Section 5.

**Step 5. Apply the rate and any levy or surcharge.**
Queensland's mental health levy, Victoria's two surcharges and the higher rates for large
employers in the ACT and the NT all turn on Australia-wide wages. See Section 3.

**Step 6. Register, lodge and pay.**
Register in every jurisdiction where wages are paid once Australia-wide wages exceed its
threshold, lodge monthly by the 7th and reconcile annually by 21 July or 28 July. See Section 9.

## Section 3 - Rates and thresholds for 2026-27

**Rates and thresholds by jurisdiction**

| Jurisdiction | Annual threshold | Rate | How the threshold reduces | Levies and surcharges |
| --- | --- | --- | --- | --- |
| ACT | $1,750,000 (monthly $145,833.33) | 6.75% where Australia-wide wages are $20m or less, 6.85% to $50m, 7.35% to $100m, 7.85% to $150m and 8.75% above $150m | Apportioned by days employed and by the ACT share of Australia-wide wages; a group member that is not the DGE gets none | None; eligible ACT universities are capped at 6.85% |
| NSW | $1,200,000 | 5.45% | Apportioned by days employed and by the NSW share of Australian wages | None |
| NT | $2,500,000 (monthly $208,333) | 5.5%, or 6.5% for employers and group members with Australia-wide wages of $100m or more | Apportioned; confirm the current deduction rules with the Territory Revenue Office | None |
| QLD | $1,300,000 (monthly $108,333) | 4.75% where Australian wages are $6.5m or less, 4.95% above; regional employers get a 1% discount until 30 June 2030 | The deduction falls by $1 for every $7 of Australian wages above $1.3m and reaches nil at $10.4m | Mental health levy of 0.25% on Queensland wages where Australian wages exceed $10m, plus a further 0.5% above $100m |
| SA | $1,500,000 (monthly $125,000) | Variable from 0% to 4.95% where Australian wages exceed $1.5m but not $1.7m, then 4.95% | Maximum deduction $600,000 | None |
| TAS | $1,250,000 | 4% on the band from $1,250,001 to $2,000,000 and 6.1% on wages above $2,000,000 | Monthly threshold is the days in the month over the days in the year, multiplied by the annual amount | None |
| VIC | $1,000,000 (monthly $83,333) | 4.85%, or 1.2125% for regional employers | Full deduction where Australian wages are below $3m, phased out at 50 cents in the dollar between $3m and $5m, and nil above $5m; also apportioned by days and by the Victorian share | Mental health and wellbeing surcharge plus COVID-19 debt surcharge: a combined 1% on the Victorian share of wages above $10m Australian wages and 2% above $100m, until 30 June 2033 |
| WA | $1,000,000 (monthly $83,333) | 5.5% | The deduction falls by $2 for every $13 of Australian wages above $1m and reaches nil at $7.5m | None |

- **Where the figures come from** — The Payroll Tax Australia site lists every jurisdiction's current rate, threshold and deduction with a link to the revenue office page, and was last updated on 2 September 2026. Check it before relying on any figure above.  _([Payroll Tax Australia, Rates and thresholds](https://www.payrolltax.gov.au/harmonisation/payroll-tax-rates-and-thresholds))_
- **ACT tiers from 1 July 2026** — The rate depends on the group's Australia-wide wages, and the tax-free threshold is apportioned by the days wages were paid and by the ACT share of Australia-wide wages.  _([ACT Revenue Office, Calculating payroll tax](https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/calculating-payroll-tax))_
- **Northern Territory** — The threshold rose to $2.5m from 1 July 2025, and from 1 July 2026 a 6.5% rate applies to employers and group members with Australia-wide wages of $100m or more.  _([Territory Revenue Office, Payroll tax rates and thresholds](https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax/payroll-tax-rates-and-thresholds))_
- **Queensland deduction and levy** — The $1.3m deduction reduces by $1 for every $7 of Australian taxable wages above the threshold and is exhausted at $10.4m; only the designated group employer claims it, and it can nominate a member to receive any excess. The mental health levy applies proportionately to Queensland wages once the group's Australian wages pass $10m.  _([QRO, Payroll tax deductions](https://qro.qld.gov.au/payroll-tax/calculate/deductions/))_
- **Victorian phase-out** — An employer with Australian wages between $3m and $5m loses 50 cents of threshold for every dollar of wages above $3m (after apportionment), so a metropolitan employer paying $4.2m only in Victoria for a full year gets $400,000. Above $5m there is no threshold.  _([SRO Victoria, Threshold and phase-out rate](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/threshold-and-phase-out-rate))_
- **Victorian surcharges** — The two surcharges are calculated on the same basis and only on the Victorian share of wages above the $10m and $100m thresholds; the COVID-19 debt surcharge runs to 30 June 2033.  _([SRO Victoria, Payroll tax current rates](https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/payroll-tax-current-rates))_
- **Western Australia** — The deductable amount is $1,000,000 less two-thirteenths of the wages above $1,000,000, so annual wages of $1,200,000 give a deduction of $969,231. Employers at $7.5m or more pay 5.5% on all WA wages.  _([WA Department of Treasury and Finance, Calculation](https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/calculation-payroll-tax-employer-guide))_
- **South Australia** — The rate is set by Australia-wide wages before the deduction is subtracted, rising from 0% at $1.5m to 4.95% at $1.7m, and the deduction is capped at $600,000. Exempt allowance rates for 2026-27 are 88 cents per kilometre and $328.85 per night.  _([RevenueSA, Rates and thresholds](https://www.revenuesa.sa.gov.au/payrolltax/rates-and-thresholds))_
- **Tasmania and NSW** — Tasmania publishes two rates and two thresholds for 2026-27 and an annual adjustment return guideline for part-year calculations; NSW publishes monthly thresholds of $92,055, $98,630 and $101,918 for 28-, 30- and 31-day months.  _([SRO Tasmania, Rates and thresholds](https://www.sro.tas.gov.au/payroll-tax/rates-thresholds))_

## Section 4 - Taxable wages, exemptions and allowances

- **Definition of wages** — The harmonised definition is not limited to salary. It covers remuneration, allowances, bonuses, commissions, director's fees, superannuation contributions, fringe benefits, shares and options, employment termination payments and deemed wages under the contractor and employment agency provisions.  _([Payroll Tax Australia, Definitions: wages](https://www.payrolltax.gov.au/definitions-acronyms-list/w))_
- **Termination payments** — An employment termination payment within s 82-130 ITAA 1997 that would be included in the employee's assessable income is wages, as is a payment that would be an ETP but for being made more than 12 months after termination. The tax-free component and the tax-free part of a genuine redundancy payment are not assessable and so are not wages, while accrued leave paid on termination is. See `au-employment-termination-payments.md`.  _([Payroll Tax Australia, Definitions: employment termination payment](https://www.payrolltax.gov.au/employment-termination-payment))_
- **Exempt allowances** — Under the harmonised ruling PTA 005 a motor vehicle allowance is exempt up to the ATO cents-per-kilometre rate for the previous income year (88 cents in 2026-27) and an accommodation allowance up to the ATO reasonable amount for the lowest capital city and lowest salary band for the current year ($328.85 per night in 2026-27). Anything above those rates is wages.  _([RevenueSA, Rates and thresholds](https://www.revenuesa.sa.gov.au/payrolltax/rates-and-thresholds))_
- **Fringe benefits** — Benefits that are fringe benefits under the FBT law are wages at their grossed-up value; each office publishes the gross-up rate to use and the option to declare the previous FBT year's figures.  _([Revenue NSW, Fringe benefits](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/fringe-benefits))_
- **Common exemptions** — Each Act exempts particular wages, for example wages paid during maternity, paternity or adoption leave, workers compensation payments, and wages paid by certain charities for exempt work; some jurisdictions also exempt apprentices and trainees. The lists differ, so confirm each exemption on the relevant office's site before claiming it.  _([Payroll Tax Australia, Revenue rulings table](https://www.payrolltax.gov.au/revenue-rulings-table))_
- **Audit findings** — The revenue offices report the same errors year after year: omitted director's fees, super and fringe benefits; undeclared employee share scheme benefits; wrongly claimed exemptions; wages declared in the wrong jurisdiction; employees classified as contractors; and wrong grouping status.  _([Payroll Tax Australia, Lodging](https://www.payrolltax.gov.au/lodging))_

## Section 5 - Thresholds, deductions and apportionment

- **Part-year employment** — Multiply the annual threshold by the days wages were paid divided by the days in the financial year. In NSW an employer paying wages for 184 days of 2025-26 received $604,931.51.  _([Revenue NSW, Thresholds and rates](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/thresholds-and-rates))_
- **Interstate wages** — Multiply the threshold by the jurisdiction's wages divided by total Australian wages. NSW wages of $900,000 out of $3,000,000 Australian wages give a NSW threshold of $360,000. Interstate wages must be declared in every return even where they fall below the other jurisdiction's threshold.  _([Revenue NSW, Interstate wages](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/interstate-wages))_
- **Both adjustments** — Where an employer both employs for part of the year and pays interstate wages, multiply the threshold by both fractions; Victoria's worked example gives $210,030 for 335 days and a 1.5m of 3.5m Victorian share, after its phase-out step.  _([SRO Victoria, Threshold and phase-out rate](https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/threshold-and-phase-out-rate))_
- **Groups** — One threshold per group, claimed by the designated group employer. Other members pay the flat rate on all their wages. In some jurisdictions an unused deduction can be allocated to another member at the annual return.  _([Payroll Tax Australia, Lodging](https://www.payrolltax.gov.au/lodging))_
- **Registration in several jurisdictions** — Liability is tested on Australia-wide wages, so an employer whose total wages exceed a state's threshold must register there even if the wages paid in that state alone are below it.  _([Payroll Tax Australia, Registration](https://www.payrolltax.gov.au/registration))_

## Section 6 - Nexus: which jurisdiction taxes the wages

- **Services wholly in one jurisdiction** — Where an employee's services in a calendar month are performed wholly in one state or territory, the wages for that month are taxable there, even if the employee normally works elsewhere.  _([Revenue NSW, Nexus provisions](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/nexus-provisions))_
- **Services in more than one place** — Apply a four-tier test in order for that month: the employee's principal place of residence (the one held on the last day of the month if there is more than one); then the employer's ABN address, or principal place of business if there is no single ABN address; then the jurisdiction where the wages are paid, using the largest portion where they are paid in several; then the jurisdiction where the services are mainly performed, meaning more than half the time worked. A deemed corporate employee's residence is its ABN address or principal place of business.  _([Revenue NSW, Nexus provisions](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/nexus-provisions))_
- **Working overseas** — Wages for services performed wholly overseas are taxable in the jurisdiction where they are paid for up to six continuous months. Once the continuous period exceeds six months the wages are exempt, including the first six months. A holiday, or a return of less than a month for work related to the overseas assignment, does not break continuity. Services performed offshore but outside any state or territory are taxable where the wages are paid, however long the assignment.  _([Revenue NSW, Nexus provisions](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/nexus-provisions))_
- **Harmonised ruling** — Revenue Ruling PTA 039 sets out the nexus rules and their deeming provisions, and each office publishes its own copy.  _([Payroll Tax Australia, Revenue rulings table](https://www.payrolltax.gov.au/revenue-rulings-table))_

## Section 7 - Grouping

- **How a group forms** — Related corporations within s 50 of the Corporations Act 2001; common employees, where an employee of one business performs duties for another; common control, where the same person or set of persons controls two businesses; tracing of interests, where an entity holds a controlling interest in a corporation; and subsuming, where smaller groups join a larger one. Grouping applies across jurisdictions and industries.  _([Revenue NSW, What is payroll tax grouping](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping))_
- **Consequences** — The gross wages of every member are added together, a single threshold applies to the group, the threshold is apportioned by the group's share of wages in the jurisdiction, and every member is liable for any unpaid payroll tax of any other member. Group Australia-wide wages also set the rate tier and levy position in the ACT, NT, QLD and VIC.  _([Revenue NSW, What is payroll tax grouping](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping))_
- **Claiming the threshold** — In NSW the group claims through a designated group employer (which must itself exceed the monthly threshold) or a group single lodger (mandatory where no member exceeds it on its own). Lodging one way or the other does not change the group's total liability. The DGE does not need to be the same entity in every jurisdiction.  _([Revenue NSW, What is payroll tax grouping](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping))_
- **Exclusion** — A member can apply to be excluded where its business is carried on independently of, and is not connected with, the other members. Related corporations cannot be excluded.  _([Revenue NSW, What is payroll tax grouping](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping))_
- **Registration failures** — Revenue offices penalise employers each year for failing to register a related entity under the grouping provisions, including holding and subsidiary relationships, common shareholders or directors and shared employees.  _([Payroll Tax Australia, Registration](https://www.payrolltax.gov.au/registration))_

## Section 8 - Contractors and employment agents

- **Employee first** — Test the totality of the relationship using only the legal rights and obligations in the contract. An ABN, a company structure or a label such as independent contractor does not settle it. All wages paid to a common law employee are taxable, and the contractor exemptions do not apply.  _([Revenue NSW, Contractors](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/contractors))_
- **Relevant contracts** — A relevant contract is one under which a person in the course of business supplies or receives services for the performance of work, or gives out goods for work to be done on them and re-supplied. The contractor is deemed the employee and the payer the employer, and the labour component of the payments is wages unless an exemption applies. Western Australia has no relevant contract provisions and relies on the employee tests.  _([Payroll Tax Australia, relevant contract](https://www.payrolltax.gov.au/relevant-contract))_
- **The seven exemptions** — Any one exemption takes all payments to that contractor out of wages: services ancillary to the supply of goods; services not ordinarily required by the business; services required for 180 days or less in the year; services provided by the contractor for 90 days or less in the year; a contractor who provides similar services to the public; services performed by two or more people engaged by the contractor; and owner-drivers. Keep the evidence for each exemption claimed.  _([Revenue NSW, Contractors](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/contractors))_
- **Non-labour deductions** — Materials, tools, equipment, a vehicle and the GST component are not wages. Where the invoice does not separate labour from the rest, the harmonised ruling PTA 018 allows a fixed percentage deduction for listed trades.  _([Revenue NSW, Contractors](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/contractors))_
- **Employment agents** — Where an agent procures workers for a client's business, the agent is liable on the wages it pays the on-hired workers and the contractor exemptions do not apply.  _([Revenue NSW, Contractors](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/contractors))_
- **Principal contractor recovery** — In NSW the Chief Commissioner can recover a subcontractor's unpaid payroll tax from the principal unless the principal holds a signed subcontractor's statement covering the work. The statement does not remove the principal's own liability on payments to the subcontractor.  _([Revenue NSW, Contractors](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/contractors))_
- **Medical and allied health practices** — Practices that engage practitioners under service agreements have been an audit focus, and several offices publish rulings and concessions on when the relevant contract provisions apply. Check the ruling in the relevant jurisdiction before assuming the practitioners fall outside the provisions.  _([ACT Revenue Office, Designated medical practices with general practitioners](https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/designated-medical-practices-with-general-practitioners))_

## Section 9 - Registration, lodgment and compliance

- **Register before the first return** — Payroll tax is self-assessed. Register with each revenue office where wages are paid once Australia-wide taxable wages, or group wages, exceed the threshold, and cancel the registration when the business stops employing there, drops below the threshold or moves to a new ABN.  _([Payroll Tax Australia, Registration](https://www.payrolltax.gov.au/registration))_
- **Monthly returns** — Due on the 7th of the following month, or the next business day where the 7th falls on a weekend or public holiday. Some jurisdictions offer other periods.  _([Payroll Tax Australia, Lodging](https://www.payrolltax.gov.au/lodging))_
- **Annual return** — Every registered employer lodges an annual reconciliation (in some jurisdictions an annual adjustment return) by 21 July, or by 28 July in the ACT, NSW and SA, even where the result is nil.  _([Payroll Tax Australia, Lodging](https://www.payrolltax.gov.au/lodging))_
- **Final returns** — Ceasing to employ, a change of grouping status or the appointment of an administrator or receiver can require a final return in each jurisdiction.  _([Payroll Tax Australia, Registration](https://www.payrolltax.gov.au/registration))_
- **Penalties and disclosure** — Interest applies to any underpayment and penalty tax can follow; a voluntary disclosure attracts a lower rate of penalty tax than an underpayment found by data matching with the ATO and other agencies.  _([Revenue NSW, Interstate wages](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/interstate-wages))_
- **Records** — Keep records showing how each jurisdiction's wages were calculated for at least five years, in English or a form easily translated, and available for audit.  _([Revenue NSW, Interstate wages](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/interstate-wages))_

## Section 10 - Worked example

**Worked example facts**

| Item | Detail |
| --- | --- |
| Employer | Harbour Fitouts Pty Ltd, not a member of a group, metropolitan, employing for all of 2026-27 |
| NSW taxable wages | $1,500,000 |
| Victorian taxable wages | $1,000,000 |
| Australian taxable wages | $2,500,000 |
| Contractors and fringe benefits | None |

**Facts.** All figures are synthetic.

**Step 1, registration.** Monthly Australian wages of about $208,333 exceed the NSW and Victorian
monthly thresholds, so the company is registered in both and lodges monthly returns by the 7th.

**Step 2, NSW.**

```
NSW threshold 1,200,000 x (1,500,000 / 2,500,000)        720,000
NSW taxable wages                                       1,500,000
Wages above the threshold                                 780,000
Payroll tax at 5.45%                                       42,510
```

**Step 3, Victoria.** Australian wages are below $3m, so the phase-out does not apply and the
deduction is simply apportioned. Australian wages are below $10m, so neither surcharge applies.

```
Victorian deduction 1,000,000 x (1,000,000 / 2,500,000)  400,000
Victorian taxable wages                                 1,000,000
Wages above the deduction                                 600,000
Payroll tax at 4.85%                                       29,100
```

**Step 4, total.** $71,610 for the year, reconciled in the NSW annual return by 28 July 2027 and
the Victorian annual reconciliation by 21 July 2027.

**The same $2,500,000 payroll paid in one jurisdiction only**

| Jurisdiction | Threshold or deduction | Taxable amount | Payroll tax |
| --- | --- | --- | --- |
| NSW | $1,200,000 | $1,300,000 | $70,850 |
| VIC, metropolitan | $1,000,000 | $1,500,000 | $72,750 |
| QLD, non-regional | $1,300,000 less ($1,200,000 / 7) = $1,128,571 | $1,371,429 | $65,143 |
| WA | $1,000,000 less ($1,500,000 x 2 / 13) = $769,231 | $1,730,769 | $95,192 |
| SA | $600,000 | $1,900,000 at 4.95% | $94,050 |
| TAS | $1,250,000 | $750,000 at 4% plus $500,000 at 6.1% | $60,500 |
| ACT | $1,750,000 | $750,000 at 6.75% | $50,625 |
| NT | $2,500,000 | Nil | Nil |

**Why the spread matters.** The same payroll costs nothing in the NT and $95,192 in WA. Interstate
employers should model the group's Australian wages in each jurisdiction before assuming a single
national rate.

## Section 11 - Common errors

- Claiming the full threshold while paying interstate wages, or not updating the interstate figure after another office's audit.
- Leaving out director's fees, superannuation contributions, grossed-up fringe benefits and employee share scheme benefits.
- Declaring wages in the wrong jurisdiction when services were performed wholly in one state for the month.
- Treating a worker with an ABN or a company as outside the contractor provisions without testing the exemptions.
- Missing the employment agency provisions, which switch off the contractor exemptions.
- Lodging as non-grouped when a common director, shareholder or shared employee creates a group.
- Applying the Victorian phase-out or the Queensland deduction taper to the jurisdiction's wages rather than Australian wages.
- Forgetting that the ACT rate, the NT 6.5% rate, the Queensland levy and the Victorian surcharges are set by group Australia-wide wages.
- Missing the 7th of the month, or the 21 July and 28 July annual due dates.
- Failing to declare portable long service leave and redundancy scheme payments in WA and the ACT.

## Section 12 - Self-checks

- [ ] Every component of remuneration, including super, fringe benefits and ETPs, is in the wages figure.
- [ ] Each employee's wages are assigned month by month under the nexus rules.
- [ ] Grouping has been tested for related corporations, common control, shared employees and traced interests.
- [ ] The threshold is apportioned for part-year employment and for the jurisdiction's share of Australian wages.
- [ ] The jurisdiction's phase-out or diminishing formula is applied to Australian wages.
- [ ] Levies and surcharges are tested against Australia-wide wages at group level.
- [ ] Every contractor exemption claimed has evidence on file.
- [ ] Exempt allowance rates match the current year's published figures.
- [ ] Monthly and annual returns are lodged in every registered jurisdiction, including nil returns.
- [ ] Records supporting each jurisdiction's wages are kept for five years.

## Section 13 - Sources

- Payroll Tax Act 2007 (NSW), Payroll Tax Act 2007 (Vic), Payroll Tax Act 1971 (Qld), Pay-roll Tax Assessment Act 2002 (WA), Payroll Tax Act 2009 (SA), Payroll Tax Act 2008 (Tas), Payroll Tax Act 2011 (ACT) and Payroll Tax Act 2009 (NT); links on the Payroll Tax Australia legislation table.
- Payroll Tax Australia, Rates and thresholds, https://www.payrolltax.gov.au/harmonisation/payroll-tax-rates-and-thresholds
- Payroll Tax Australia, Registration, https://www.payrolltax.gov.au/registration
- Payroll Tax Australia, Lodging, https://www.payrolltax.gov.au/lodging
- Payroll Tax Australia, Revenue rulings table, https://www.payrolltax.gov.au/revenue-rulings-table
- Payroll Tax Australia, definitions of wages, relevant contract and employment termination payment, https://www.payrolltax.gov.au/definitions-acronyms-list/w
- Revenue NSW, Payroll tax thresholds and rates, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/lodge-and-pay-returns/thresholds-and-rates
- Revenue NSW, Payroll tax and interstate wages, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/interstate-wages
- Revenue NSW, Nexus provisions for payroll tax, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/nexus-provisions
- Revenue NSW, Contractors and payroll tax, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/taxable-wages/contractors
- Revenue NSW, What is payroll tax grouping, https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/payroll-tax/grouping/what-is-payroll-tax-grouping
- SRO Victoria, Payroll tax current rates, https://www.sro.vic.gov.au/about-us/rates-and-statistics/current-rates/payroll-tax-current-rates
- SRO Victoria, Threshold and phase-out rate, https://www.sro.vic.gov.au/businesses-and-organisations/payroll-tax/thresholds-and-grouping/threshold-and-phase-out-rate
- Queensland Revenue Office, Payroll tax rates and thresholds, https://qro.qld.gov.au/payroll-tax/calculate/rates-thresholds/
- Queensland Revenue Office, Payroll tax deductions, https://qro.qld.gov.au/payroll-tax/calculate/deductions/
- Queensland Revenue Office, Mental health levy, https://qro.qld.gov.au/payroll-tax/mental-health-levy/
- WA Department of Treasury and Finance, Calculation: Payroll Tax Employer Guide, https://www.wa.gov.au/government/multi-step-guides/payroll-tax-employer-guide/calculation-payroll-tax-employer-guide
- RevenueSA, Rates and thresholds, https://www.revenuesa.sa.gov.au/payrolltax/rates-and-thresholds
- SRO Tasmania, Rates and thresholds, https://www.sro.tas.gov.au/payroll-tax/rates-thresholds
- ACT Revenue Office, Calculating payroll tax, https://www.revenue.act.gov.au/business-taxes-and-levies/payroll-tax/calculating-payroll-tax
- Territory Revenue Office, Payroll tax rates and thresholds, https://treasury.nt.gov.au/dtf/territory-revenue-office/payroll-tax/payroll-tax-rates-and-thresholds

Sources were checked on 27 September 2026.

> **Working paper only, not a lodged return.** Have a qualified Australian CPA or CA review this before registering, lodging or amending a payroll tax return. Thresholds, deduction formulas and levies change with each state budget, and grouping and contractor positions turn on the facts.

> Contributed by Ryan Duguid.

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
