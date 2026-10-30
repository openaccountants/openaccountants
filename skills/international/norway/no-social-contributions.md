---
name: no-social-contributions
description: "Use this skill for Norwegian social contributions for income year 2026: the national insurance contribution (trygdeavgift) paid by employees, pensioners and the self-employed, and the employer's national insurance contribution (arbeidsgiveravgift) and financial tax on pay. It covers membership of the National Insurance Scheme, the three contribution rates (5.1%, 7.6% and 10.8%), the NOK 99,650 lower limit and the 25% phase-in limit applied once to total personal income, sole proprietors (enkeltpersonforetak) and their calculated personal income, the seven employer zones from 14.1% to 0%, the NOK 850,000 allowance, sector rules, private households, payment dates, fines and cross-border coverage. Trigger on: trygdeavgift, arbeidsgiveravgift, national insurance Norway, NAV contributions, self-employed contributions Norway, AGA, finansskatt på lønn. Out of scope: no-employer-payroll (withholding, a-melding detail), no-income-tax (income tax and bracket tax), no-individual-residence, no-corporate-income-tax, no-vat-return."
version: 2.1
jurisdiction: "NO"
tax_year: 2026
last_updated: 2026-10-30
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Norway: social contributions (income year 2026)

This skill covers Norwegian social contributions for income year 2026. There are two separate liabilities. The person's own national insurance contribution (trygdeavgift) is charged on personal income and collected with income tax. The employer's national insurance contribution (arbeidsgiveravgift) is charged on pay the employer gives out and reported in the monthly a-melding. A sole proprietor pays trygdeavgift on their own business income and arbeidsgiveravgift only on pay to employees.

The law is the National Insurance Act (folketrygdloven, lov 1997-02-28-19), chapter 2 for membership and chapter 23 for contributions. The Storting sets the rates each year: for 2026 in the decision on contributions to the National Insurance Scheme (FOR-2025-12-18-2748, amended 19 June 2026) and the decision on financial tax on pay (FOR-2025-12-18-2749). Skatteetaten assesses and collects. NAV decides membership questions. Amounts are in Norwegian kroner (NOK).

Read [no-income-tax](no-income-tax.md) for income tax and bracket tax on the same personal income, [no-employer-payroll](no-employer-payroll.md) for withholding, the a-melding and the full employer pay run, [no-individual-residence](no-individual-residence.md) for tax residence and [no-corporate-income-tax](no-corporate-income-tax.md) for companies.

## Who this applies to

- **Members of the National Insurance Scheme.** A person resident in Norway is a compulsory member. Resident means a stay that is meant to last, or has lasted, at least 12 months; someone moving to Norway is resident from the date of arrival. Legal residence is a condition (folketrygdloven § 2-1).
- **Workers in Norway.** A person who is not a member under § 2-1 is still a compulsory member as an employee in Norway or on the Norwegian continental shelf, unless the Act says otherwise (§ 2-2).
- **Coverage under the EEA rules and social security agreements.** International coordination rules can put a person under another country's scheme (§ 2-1 a). Then no Norwegian trygdeavgift is due. NAV decides. Skatteetaten does not accept an A1 or another state's form on its own as proof that a person is not a member; it needs NAV's confirmation (Forskuddsutskrivingen 2026).
- **Who pays trygdeavgift.** Every member with personal income above NOK 99,650: employees, pensioners, people on benefits that count as personal income, and sole proprietors and partners on their business income.
- **Who pays arbeidsgiveravgift.** Every employer paying wages or other remuneration for work, including a foreign employer with workers in Norway. A private household is exempt while its pay for work in the home is not over NOK 60,000 in the year (folketrygdloven § 23-2).
- **Not covered here.** Product tax for fishing, voluntary membership premiums and the special rules for workers on the continental shelf and on foreign ships. They are flagged, not computed.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Trygdeavgift, low rate: pensions, and personal income of anyone under 17 or over 69 | 5.1% | 2026 | Decision on contributions 2026 § 6; https://lovdata.no/dokument/STV/forskrift/2025-12-18-2748 |
| Trygdeavgift, middle rate: pay and other income in § 23-3 second paragraph no. 2 | 7.6% | 2026 | same decision § 7 |
| Trygdeavgift, high rate: business income | 10.8% | 2026 | same decision § 8 |
| Lower limit | No trygdeavgift when personal income is up to NOK 99,650 | 2026 | folketrygdloven § 23-3 fourth paragraph; https://lovdata.no/lov/1997-02-28-19/§23-3 |
| Phase-in limit | Trygdeavgift never more than 25% of personal income above NOK 99,650 | 2026 | folketrygdloven § 23-3 fourth paragraph |
| Upper limit on the base | None | 2026 | folketrygdloven § 23-3 (no ceiling in the section) |
| Arbeidsgiveravgift zone I | 14.1% | 2026 | Decision on contributions 2026 § 3 |
| Zone Ia | 10.6% while the saving against 14.1% stays within the de minimis limit (NOK 850,000), then 14.1% | 2026 | same § 3 and § 4 fourth and fifth paragraphs |
| Zone II | 10.6% | 2026 | same § 3 |
| Zone III | 6.4% | 2026 | same § 3 |
| Zone IV | 5.1% | 2026 | same § 3 |
| Zone IVa (Tromsø, Bodø) | 7.9% | 2026 | same §§ 2 and 3 |
| Zone V (Finnmark and seven Nord-Troms municipalities) | 0% | 2026 | same §§ 2 and 3 |
| Sector-excluded employers | Zone I rate in all zones, except within NOK 850,000 a year (group-wide) | 2026 | same § 4 |
| Products outside the EEA Agreement (listed farming, fishing and food codes) | 5.1% in zone IVa; 10.6% in zone Ia | 2026 | same § 5 |
| Workers posted from the USA, Canada or South Korea, members only of the sickness benefit part | 7% | 2026 | Skattedirektoratet, Arbeidsgiveravgift 2026, citing forskrift 19 December 2025 nr. 2786; https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/ |
| Private household exemption | No arbeidsgiveravgift while household pay is not over NOK 60,000 in the year | 2026 | folketrygdloven § 23-2 |
| Minimum payment of arbeidsgiveravgift per period | NOK 100 (the a-melding is still due) | 2026 | Skattedirektoratet, Arbeidsgiveravgift 2026 (skattebetalingsforskriften § 10-4-1) |
| Financial tax on pay (finansskatt på lønn) | 5% | 2026 | Decision on financial tax on pay 2026; https://lovdata.no/dokument/STV/forskrift/2025-12-18-2749 |
| Additional 5% employer contribution on high pay | Discontinued from 1 January 2025 | 2026 | Skatteetaten, Employer's additional national insurance contributions (discontinued) |
| Late-payment interest | 12% from 1 January 2026; 12.25% from 1 July 2026 | 2026 | skattebetalingsloven § 11-1; https://www.skatteetaten.no/satser/forsinkelsesrenter/ |
| Court fee (basis of enforcement fines) | NOK 1,345 | 2026 | Skatteetaten, Enforcement fines |

## The taxable base

### Trygdeavgift

The base is personal income under skatteloven § 12-2 (folketrygdloven § 23-3 first paragraph). It is gross: no personal allowance, interest, minimum deduction or loss reduces it. Each kind of personal income has its rate (§ 23-3 second paragraph):

- **Low rate, 5.1%.** Pensions in and outside employment, lump sums from pension schemes, transitional benefit under chapter 17 A, supplementary benefit for people aged 67 or more, and all personal income of a person under 17 or over 69.
- **Middle rate, 7.6%.** Pay and other remuneration for work; work assessment allowance, disability benefit and similar benefits; qualification and introduction benefits; and two kinds of business income: a business that pays product tax under § 23-5 (fishing), and childminding in the childminder's own home of children under 12 or children with special care needs.
- **High rate, 10.8%.** All other personal income, in practice business income from a sole proprietorship or partner income from a partnership.

Benefits that replace income (unemployment, sickness, care and parental benefits under chapters 4, 8, 9 and 14) carry the rate of the income they replace (§ 23-3 third paragraph). On Svalbard, ordinary income from a sole proprietorship carries the middle rate (§ 23-3 fifth paragraph).

**One limit for all income.** Add up all personal income across the three rates. If the total is NOK 99,650 or less, nothing is due. If it is higher, compute each part at its rate and add them up. The total cannot be more than 25% of the total income above NOK 99,650 (§ 23-3 fourth paragraph; Forskuddsutskrivingen 2026 repeats it). Apply the lower limit and the 25% limit once, to the total, never once per income type. There is no upper ceiling: above the phase-in range the rates apply to all the income.

With only business income at 10.8%, the 25% limit is the lower figure up to about NOK 175,440. With only pay at 7.6%, it is lower up to about NOK 143,175. These crossover points are arithmetic from the two official figures, not thresholds in the law.

**Age.** The low rate for people under 17 or over 69 applies to all their personal income, including pay and business income (§ 23-3 second paragraph no. 1 c). A sole proprietor over 69 pays 5.1%, not 10.8%.

### Sole proprietors: the calculated personal income

For an owner of an enkeltpersonforetak (ENK), the base is the calculated personal income (beregnet personinntekt) under skatteloven §§ 12-10 to 12-13, not turnover, cash received or accounting profit. It starts from ordinary business income before losses brought forward, adds back capital costs and losses, takes out capital income and gains, and deducts the shield deduction on the business assets (§ 12-11). The full bridge is in [no-income-tax](no-income-tax.md).

- A negative calculated personal income gives no negative contribution base. It cannot be set against pay or pensions. It is carried forward against later positive results from the same business, and the right is lost to the extent it is not used in the first year possible (§ 12-13).
- In the contribution calculation, enter a remaining negative business result as zero; do not net it against pay.
- A small business with revenue of NOK 50,000 or less that does not file the business specification has personal income equal to business income, and cannot carry a negative result forward (skatteforvaltningsforskriften § 8-2-1 third paragraph).
- Do not subtract the trygdeavgift itself from the base. It is not a business cost.

### Arbeidsgiveravgift

The base is wages and other remuneration that the employer must report, including benefits in kind. The detail of what counts as pay is in [no-employer-payroll](no-employer-payroll.md). The rate follows the zone where the employer must be registered in the Central Coordinating Register for Legal Entities; a private individual employer uses the zone of their registered home (Decision § 1 second paragraph). Each registered sub-unit is its own calculation unit (§ 1 third paragraph).

- **Mobile work.** Where most of an employee's work in a calendar month (more than half the working days) is done in another zone and the business is mobile, the other zone's rate applies to that pay. For remote work that need not be done at a set place, this applies only when the other zone's rate is higher (§ 1 fourth paragraph).
- **Moving.** If the employer or sub-unit moves zone, the new zone's rate applies from the calendar month after the registered moving date (§ 1 fifth paragraph).
- **Zone Ia.** The 10.6% rate applies while the difference between 14.1% and 10.6% stays within the de minimis limit in § 4 fourth and fifth paragraphs; Skatteetaten's guidance and the payroll skill call this the NOK 850,000 allowance. Health trusts and state administration get no reduced rate in zone Ia (§ 3 first paragraph).
- **Sector rules.** Employers in zones II to V that produce steel products or work in the coal sector must use the zone I rate for that activity. Employers whose main activity is financial services (industry area L), or in-group head-office or management consultancy (codes 70.10 and 70.22), use the zone I rate for all employees. A clear accounting split lets a mixed employer use the zone rate on the rest (§ 4 first to third paragraphs).
- **Allowance for excluded employers.** An excluded employer may still use the zone rate as long as the saving against zone I is not over NOK 850,000 in 2026, counted for the whole group (§ 4 fourth paragraph). The total of this saving and any other de minimis aid cannot exceed NOK 850,000 in 2026 (§ 4 fifth paragraph).
- **Employers in economic difficulty**, and employers with an unpaid claim to repay illegal state aid, use zone I, except within the same de minimis limit (§ 3 second paragraph). Employers on reduced rates must declare whether they are in difficulty and report other aid towards pay costs (§ 3 third and fourth paragraphs).
- **Financial tax on pay.** Employers in the financial sector also pay 5% financial tax on pay (folketrygdloven § 23-2 a; 2026 decision). Companies that pay it are taxed at 25% instead of 22% on income (Stortingets skattevedtak § 3-3).
- **Private household.** No arbeidsgiveravgift is due on pay for work in a private home or holiday home, where the pay is not deductible for the employer and the work is not part of the worker's business, while that pay is not over NOK 60,000 in the year. No arbeidsgiveravgift is due on private childcare for children under 12 or with special needs (§ 23-2).
- **No extra 5%.** The extra 5% employer contribution on pay above a yearly threshold was discontinued from 1 January 2025. Skatteetaten rejects an a-melding that reports it for payments in 2025. Do not add it for 2026.
- **Contractors.** Arbeidsgiveravgift is on pay. A fee to a person doing the work as part of their own business is not pay; check the contractor's status before treating it as wages.

## Deadlines and filing

| Step | When | Source |
|---|---|---|
| Trygdeavgift, employees | Withheld with income tax on each pay run under the tax card | [no-employer-payroll](no-employer-payroll.md) |
| Trygdeavgift, sole proprietors | Included in advance tax: four instalments, 15 March, 15 June, 15 September, 15 December; under NOK 2,000 due 15 June | skattebetalingsloven § 10-20 |
| Extra advance tax without interest charge | By 31 May of the following year | skattebetalingsloven § 11-5 |
| Annual settlement | Tax return by end of April (employees, pensioners) or end of May (ENK owners); residual tax due three weeks after the assessment, not before 20 August | skatteforvaltningsforskriften § 8-2-3; skattebetalingsloven § 10-21 |
| a-melding (reports pay and arbeidsgiveravgift) | By the 5th of the month after; next working day if the 5th is a weekend or holiday | Skatteetaten, a-melding deadlines and payment |
| Arbeidsgiveravgift and financial tax on pay | Paid for the two previous months on 15 January, 15 March, 15 May, 15 July, 15 September and 15 November | skattebetalingsloven § 10-10 second paragraph |
| Withheld tax (includes employee trygdeavgift) | First working day after the pay is paid (from 2026) | skattebetalingsloven § 10-10 first paragraph |
| Correction of own a-melding or return | Up to three years after the deadline | skatteforvaltningsloven § 9-4 |

An employer reports arbeidsgiveravgift one month at a time in the a-melding and pays it every two months. A calculated arbeidsgiveravgift under NOK 100 for a period need not be paid, but the a-melding must still be sent. The personal trygdeavgift has no separate return: it is part of the tax return and the assessment, which is the control point.

## Penalties and interest

- **Late or wrong a-melding.** Enforcement fine of 1/10 of a court fee per day for each income recipient missing or wrongly reported, at most 1,000 court fees per period: NOK 134.50 a day per recipient and at most NOK 1,345,000 per period in 2026 (Skatteetaten, enforcement fines).
- **Late tax return.** Half a court fee per day, at most 50 court fees, so NOK 672.50 a day and at most NOK 67,250 (skatteforvaltningsforskriften § 14-1-1; skatteforvaltningsloven § 14-1).
- **Additional tax.** 20% of the tax advantage from wrong or missing information in a return, 10% where the same information was also given by an employer or other third party; aggravated additional tax adds 20% or 40% (skatteforvaltningsloven §§ 14-5 and 14-6). No additional tax under NOK 1,000, on obvious errors or on a voluntary correction (§ 14-4).
- **Late-payment interest.** From the due date until payment, 12% from 1 January 2026 and 12.25% from 1 July 2026 (skattebetalingsloven § 11-1). For advance tax, a missed instalment makes the later instalments fall due at once (§ 10-20 fourth paragraph), and Skatteetaten can start enforced collection of the rest of the year's advance tax (Skatteetaten, advance tax).

## Cross-border points

- **One country's scheme.** Contributions follow the scheme that covers the person, not tax residence. The international coordination rules decide which scheme applies, and NAV decides for Norway (folketrygdloven § 2-1 a).
- **Not a Norwegian member.** At the advance stage Skatteetaten treats a person as not a member when NAV confirms it, when the person receives only a pension or disability benefit covered by the EEA regulation in another state, or when all work is abroad for a foreign employer. An A1 alone is not enough (Forskuddsutskrivingen 2026).
- **PAYE scheme.** A foreign worker on the flat PAYE scheme pays 25%, which includes the contribution, or 17.4% if not a member of national insurance (Forskuddsutskrivingen 2026; Stortingets skattevedtak § 3-9). See [no-income-tax](no-income-tax.md).
- **Foreign employers.** A foreign employer with workers in Norway pays arbeidsgiveravgift on pay to members of the scheme. Workers posted from the USA, Canada or South Korea who are members only of the sickness benefit part carry a 7% rate.
- **Svalbard.** Pay taxed under the Svalbard tax law carries 0% arbeidsgiveravgift (Decision § 3 first paragraph).

## Worked examples

Amounts are unrounded working-paper figures. Use the official assessment for filing.

### Example 1: sole proprietor, calculated personal income NOK 300,000

A sole proprietor aged 40 is a member of the scheme and has no other income. The business tax information shows calculated personal income of NOK 300,000. The high rate gives NOK 32,400. The 25% limit is 25% of NOK 200,350, which is NOK 50,087.50. The lower figure applies: trygdeavgift is NOK 32,400. It is paid through the four advance tax instalments and settled in the assessment.

```oa-check
name: NO sole proprietor trygdeavgift, personal income NOK 300,000 (2026)
inputs:
  business: 300000
  lower_limit: 99650
steps:
  - at_rate: pct(business, 10.8)
  - phase_in_cap: pct(max(business - lower_limit, 0), 25)
  - trygdeavgift: min(at_rate, phase_in_cap)
expected:
  at_rate: 32400.00
  phase_in_cap: 50087.50
  trygdeavgift: 32400.00
```

### Example 2: small pay plus small business, the 25% limit binds

A member aged 40 has pay of NOK 60,000 and calculated business personal income of NOK 60,000. Each part at its own rate gives NOK 4,560 (7.6%) and NOK 6,480 (10.8%), together NOK 11,040. Total personal income is NOK 120,000, so the one 25% limit is 25% of NOK 20,350, which is NOK 5,087.50. That is lower, so trygdeavgift is NOK 5,087.50. The business does not get its own NOK 99,650 lower limit.

```oa-check
name: NO pay 60,000 plus business 60,000, 25% limit (2026)
inputs:
  pay: 60000
  business: 60000
  lower_limit: 99650
steps:
  - total_income: pay + business
  - at_rates: pct(pay, 7.6) + pct(business, 10.8)
  - phase_in_cap: pct(max(total_income - lower_limit, 0), 25)
  - trygdeavgift: min(at_rates, phase_in_cap)
expected:
  total_income: 120000.00
  at_rates: 11040.00
  phase_in_cap: 5087.50
  trygdeavgift: 5087.50
```

## Ask the client first

- Are you a member of the Norwegian National Insurance Scheme for all of 2026? Do you have an A1 or a NAV decision putting you under another country's scheme?
- What is your date of birth? (Under 17 or over 69 in 2026 means 5.1% on all personal income.)
- What personal income do you have: pay, pension, benefits, and the calculated personal income from any sole proprietorship?
- Is the business fishing, or childminding in your own home of children under 12 or with special needs?
- Do you employ anyone? Where is the business registered (municipality and sub-units), what is its main activity, and is it in economic difficulty or receiving other state aid?
- For a household: how much did you pay for work in your home in 2026?

## Sources

| Source | URL | Read on |
|---|---|---|
| Stortingsvedtak om fastsetting av avgifter mv. til folketrygden for 2026, FOR-2025-12-18-2748, amended 19 June 2026 (§§ 1 to 8) | https://lovdata.no/dokument/STV/forskrift/2025-12-18-2748 | 2026-10-30 |
| Stortingsvedtak om fastsetting av finansskatt på lønn for 2026, FOR-2025-12-18-2749 | https://lovdata.no/dokument/STV/forskrift/2025-12-18-2749 | 2026-10-30 |
| Stortingets skattevedtak 2026, FOR-2025-12-18-2747 (§§ 3-3, 3-9) | https://lovdata.no/dokument/STV/forskrift/2025-12-18-2747 | 2026-10-30 |
| Folketrygdloven, lov 1997-02-28-19 (§§ 2-1, 2-1 a, 2-2, 23-2, 23-2 a, 23-3) | https://lovdata.no/lov/1997-02-28-19 | 2026-10-30 |
| Skatteloven, lov 1999-03-26-14 (§§ 12-2, 12-11, 12-13) | https://lovdata.no/lov/1999-03-26-14 | 2026-10-30 |
| Skatteforvaltningsloven, lov 2016-05-27-14 (§§ 9-4, 14-1, 14-4 to 14-6) | https://lovdata.no/lov/2016-05-27-14 | 2026-10-30 |
| Skatteforvaltningsforskriften, FOR-2016-11-23-1360 (§§ 8-2-1, 8-2-3, 14-1-1) | https://lovdata.no/forskrift/2016-11-23-1360 | 2026-10-30 |
| Skattebetalingsloven, lov 2005-06-17-67 (§§ 10-10, 10-20, 10-21, 11-1, 11-5) | https://lovdata.no/lov/2005-06-17-67 | 2026-10-30 |
| Skatteetaten, Forskuddsutskrivingen 2026 | https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ | 2026-10-30 |
| Skattedirektoratet, Arbeidsgiveravgift til folketrygden for 2026 | https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/ | 2026-10-30 |
| Skatteetaten, Employer's additional national insurance contributions (discontinued) | https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/the-a-melding-guide/employers-national-insurance-contributions-and-financial-activity-tax/employers-additional-national-insurance-contributions/ | 2026-10-30 |
| Skatteetaten, a-melding deadlines and payment | https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/deadlines-and-payment/ | 2026-10-30 |
| Skatteetaten, Advance tax | https://www.skatteetaten.no/en/person/taxes/tax-deduction-card-and-advance-tax/advance-tax/ | 2026-10-30 |
| Skatteetaten, Enforcement fines | https://www.skatteetaten.no/en/business-and-organisation/start-and-run/deadlines-certificates-and-accounting/enforcement-fines/ | 2026-10-30 |
| Skatteetaten, Forsinkelsesrenter | https://www.skatteetaten.no/satser/forsinkelsesrenter/ | 2026-10-30 |

Not yet confirmed: how the EU de minimis ceiling (which [no-employer-payroll](no-employer-payroll.md) gives as EUR 300,000 per entity or group over three years) sits beside the NOK 850,000 limit in § 4 fifth paragraph of the 2026 decision as amended on 19 June 2026; whether a member of the Norwegian scheme can get any foreign tax credit against trygdeavgift (the previous version said no, citing the 2026 guidance; not found there today); the treatment of a person who turns 17 or 70 during the year; how Skatteetaten splits a capped contribution between income types where a system needs it; spouse coordination of a joint business's personal income; voluntary membership premiums and the continental shelf and foreign-ship rules.

> Contributed by Michael Cutajar.

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
