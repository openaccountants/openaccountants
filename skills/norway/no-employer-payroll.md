---
name: no-employer-payroll
description: >
  Norway employer payroll for income year 2026: an employer paying wages in
  Norway. Covers the tax card (skattekort) and the duty to fetch it before each
  pay run, table versus percentage deduction, the 50% and 30% rates when no card
  is available, the NOK 100,000 exemption card (frikort), the holiday-pay and
  pre-Christmas withholding breaks, the 25% PAYE source tax for foreign workers,
  payment of withheld tax by the first working day after payday (new from 2026,
  the tax deduction account is gone), the a-melding by the 5th, employer
  national insurance contributions (arbeidsgiveravgift) by zone, 14.1% to 0%,
  paid every two months, the zone Ia NOK 850,000 allowance, coercive fines and
  liability for unpaid withholding. Trigger on: Norway payroll,
  forskuddstrekk, skattekort, a-melding, arbeidsgiveravgift, frikort, kildeskatt
  på lønn, employer contributions Norway. Out of scope: income tax bands
  (no-income-tax) and self-employed contributions (no-social-contributions).
jurisdiction: "NO"
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-30
version: 0.4
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Norway employer payroll (2026) v0.4

Income year 2026. Currency: Norwegian kroner (NOK). Authority: Skatteetaten (the Norwegian Tax Administration). Statutes: Skattebetalingsloven (Tax Payment Act, lov 17 June 2005 nr. 67, "sktbl."), its regulation (forskrift 21 December 2007 nr. 1766, "sktbf."), A-opplysningsloven (lov 22 June 2012 nr. 43) and its regulation (forskrift 24 June 2014 nr. 857), Folketrygdloven (National Insurance Act) § 23-2, and the Storting's 2026 contribution decision (Stortingsvedtak 18 December 2025 nr. 2748, "avgiftsvedtaket"). See Sources.

**What changed for 2026.** The tax deduction account (skattetrekkskonto) scheme is gone. From January 2026 the employer pays withheld tax direct to Skatteetaten no later than the first working day after each payday (sktbl. § 10-10 first paragraph, as amended by lov 20 June 2025 nr. 63, in force 1 January 2026). The a-melding deadline and the two-month cycle for employer contributions do not change. Contribution zones and rates are unchanged from 2025 (Skattedirektoratet, Arbeidsgiveravgift til folketrygden for 2026).

See also: [no-income-tax](no-income-tax.md) (bands and deductions behind the tax card), [no-social-contributions](no-social-contributions.md) (self-employed contributions), [no-individual-residence](no-individual-residence.md) (who is resident).

## Who this applies to

- **Employers.** Anyone who pays wages or other remuneration covered by skatteloven § 5-10 must withhold tax (forskuddstrekk) from it (sktbl. §§ 5-4 first paragraph, 5-6 first paragraph letter a). Cost reimbursements are subject to withholding even when they are not taxable (§ 5-6 second paragraph).
- **Employer contributions.** The employer pays arbeidsgiveravgift on wages and other remuneration for work and assignments, in and outside employment, that it must report (folketrygdloven § 23-2 first paragraph).
- **Foreign workers.** A worker on a short stay who is taxed under skatteloven chapter 20 (the PAYE source-tax scheme, kildeskatt på lønn) is withheld at the card's fixed rate (sktbl. § 5-4 first paragraph, third sentence).
- **Out of scope.** Seafarers, fishing shares, Svalbard, pensions and benefits paid by NAV, financial activity tax (finansskatt) on wages, and the sector exclusions from the reduced zone rates. Worker versus contractor status is not decided here.

## Rates, bands and thresholds

| Item | Amount | Year | Source |
|---|---|---|---|
| Withholding with no access to the latest tax card | 50% of salary, and of benefits under folketrygdloven chapters 4, 8 to 11 and 14 and disability benefits taxed as salary | 2026 | sktbl. § 5-5 first paragraph, second sentence; https://lovdata.no/lov/2005-06-17-67/§5-5 |
| Withholding with no card: other national insurance benefits, pensions, annuities | 30% | 2026 | sktbl. § 5-5 first paragraph, fourth sentence |
| Exemption card (frikort) amount limit | NOK 100,000 | 2026 | Skatteetaten, Forskuddsutskrivingen 2026; https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ |
| Salary above the frikort amount allocated to this employer | 50% of the excess; 50% of all salary if the allocation is NOK 0 | 2026 | Skatteetaten, tax deduction cards for employers; https://www.skatteetaten.no/en/business-and-organisation/employer/tax-deduction-cards-and-tax-deductions/tax-deduction-cards/about-tax-deduction-cards-for-you-as-an-employer/ |
| PAYE source tax on wages (kildeskatt på lønn) | 25% for ages 17 to 69; 22.5% under 17 or over 69; 17.4% where the worker is not a member of the National Insurance Scheme | 2026 | Forskuddsutskrivingen 2026, kildeskatt på lønn and central rates table |
| PAYE scheme income cap | NOK 725,050 (the bracket tax step 3 threshold) | 2026 | Forskuddsutskrivingen 2026; skatteloven § 20-3 |
| Employee national insurance contribution on salary (age 17 to 69) | 7.6% | 2026 | Skatteetaten, National Insurance contributions 2026; https://www.skatteetaten.no/en/rates/national-insurance-contributions/ |
| Employee contribution lower limit | NOK 99,650; the contribution is never more than 25% of income over that limit | 2026 | Forskuddsutskrivingen 2026; folketrygdloven § 23-3 fourth paragraph |
| Employer contribution, zone I | 14.1% | 2026 | Arbeidsgiveravgift til folketrygden for 2026, point 4.2; https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/ |
| Employer contribution, zone Ia | 10.6% until the saving against 14.1% reaches the NOK 850,000 allowance (fribeløp) per legal entity, then 14.1% | 2026 | Same, points 4.2 and 6; https://www.skatteetaten.no/en/rates/employers-national-insurance-contributions/ |
| Employer contribution, zones II / III / IV / IVa / V | 10.6% / 6.4% / 5.1% / 7.9% / 0% | 2026 | Same, point 4.2 |
| De minimis cap on reduced-rate aid | Reduced contributions under the allowance plus other de minimis aid: at most EUR 300,000 per legal entity or group over 3 years, even if the NOK 850,000 is not used up | 2026 | Arbeidsgiveravgift til folketrygden for 2026, point 6.5 (Regulation (EU) 2023/2831) |
| Household employers: no employer contribution | Paid work in a private home or holiday home, where the pay is not deductible for the household and the work is not part of the worker's business, while the household's total such pay (holiday pay and free board and lodging included) is not over NOK 60,000 in the income year. Private childminding of children under 12, or with special care needs, is also free of the contribution | 2026 | folketrygdloven § 23-2 (household limit: seventh paragraph); https://lovdata.no/lov/1997-02-28-19/§23-2; Arbeidsgiveravgift til folketrygden for 2026 |
| Minimum employer contribution to pay per period | NOK 100 (the a-melding is still due) | 2026 | Skatteetaten, payment page (sktbf. § 10-4-1); https://www.skatteetaten.no/en/business-and-organisation/employer/employers-national-insurance-contributions/payment-of-withholding-tax-and-employers-national-insurance-contributions/ |
| Holiday pay: no withholding | Statutory holiday pay paid in the holiday year; agreed holiday pay up to 21% above the statutory amount | 2026 | sktbl. § 5-7 first paragraph letter a; sktbf. § 5-7-1 first paragraph letters a and b; https://lovdata.no/forskrift/2007-12-21-1766/§5-7-1 |
| Pre-Christmas break | Monthly paid: no withholding for the second half of November or the first half of December | 2026 | sktbf. § 5-7-2 first paragraph |
| Court fee (rettsgebyr), the base for fines | NOK 1,345 from 1 January 2026 | 2026 | Rettsgebyrloven § 1, note 1 (forskrift 15 February 1983 nr. 86 § 2-1); https://lovdata.no/lov/1982-12-17-86/§1 |

## The base

1. **Fetch the tax card.** Fetch an electronic card for every employee before the first pay run of the year, and make sure the card data are current before each pay run (sktbl. § 5-1 second paragraph). Skatteetaten notifies the employer when a card changes; fetch the new card before the next run.
2. **Main or secondary employer.** The main employer (where income is usually highest) withholds by table; a secondary employer withholds by the card's percentage. If it is unclear, ask the employee; if it stays unclear, use the percentage (sktbf. § 5-1-4). A PAYE-scheme card uses its fixed rate for every payment, including holiday pay and December, because it is based on 12 months of withholding (Forskuddsutskrivingen 2026, kildeskatt på lønn).
3. **No card.** If the employer cannot access the latest card through no fault of its own, it withholds by the last card issued. If it cannot access any card, it withholds 50% on salary and on the National Insurance benefits listed in § 5-5 first paragraph third sentence, and 30% on other benefits, pensions and annuities (sktbl. § 5-5 first paragraph). In January the employer may use the previous year's card and must correct the deductions to the new card by the end of February (Skatteetaten, how to deduct the correct amount of tax).
4. **Exemption card.** An employee with several employers allocates the frikort amount between them (Skatteetaten, tax deduction cards). Salary up to the amount allocated to this employer is free of withholding; withhold 50% on the excess. If the allocation is NOK 0, withhold 50% on all salary until the employee allocates an amount.
5. **Gross cash and benefits.** Cash pay counts gross (sktbl. § 5-8 first paragraph). Take out of the base the pension contributions and union dues the employer deducts from pay, where the employee will get a deduction for them (§ 5-9 first paragraph). Withhold on benefits in kind only so far as the cash pay covers it; if it does not, tell the tax office at once (§ 5-10 third paragraph).
6. **Withholding breaks.** No withholding on statutory holiday pay in the holiday year. A monthly paid employee is free of withholding for one month in the summer and half a month before Christmas (sktbl. § 5-7 first paragraph letter a; sktbf. §§ 5-7-1 and 5-7-2). An employee with no card does not get these breaks (Skatteetaten, how to deduct the correct amount of tax), nor does a PAYE card.
7. **Higher deduction on request.** The employer must withhold more than the card says if the employee asks in good time (sktbl. § 5-5 second paragraph).
8. **Employer contribution.** Apply the rate of the zone where the enterprise or its sub-unit is registered to the reportable pay. Pension premiums and contributions the employer pays are part of the base in the month paid. Holiday pay is spread over zones in the same way as ordinary pay in the month paid (Arbeidsgiveravgift 2026). In zone Ia, track the allowance across all sub-units: one legal entity has one allowance.

## Deadlines and filing

| What | Deadline | Channel | Source |
|---|---|---|---|
| Fetch tax cards | Before the first pay run of the year, and before each run for new hires and changed cards | Altinn or the payroll system | sktbl. § 5-1 second paragraph |
| Pay net salary | By the agreed payday | Employer | Skatteetaten, how to deduct the correct amount of tax |
| Pay withheld tax (and wage attachments) | No later than the first working day after the payday; a deadline on a Saturday, Sunday or holiday moves to the next working day | Bank transfer with the KID for withholding | sktbl. §§ 10-10 first paragraph, 10-2 |
| a-melding (pay, withholding, contribution basis, employment data) | By the 5th of the month after the month it covers; a weekend or holiday moves it to the next working day | a-ordningen (payroll system or Altinn) | a-opplysningsloven § 4; forskrift 2014-06-24-857 § 2-1 |
| Employer contributions for the two previous months | 15 January, 15 March, 15 May, 15 July, 15 September, 15 November | Bank transfer with the contribution KID | sktbl. § 10-10 second paragraph |
| Annual statement to each employee | January of the following year | Employer | Skatteetaten, how to deduct the correct amount of tax |

Salary is reported for the month it is paid, and the employment is reported each month up to the month the employee leaves. A foreign employer whose assignment starts after the 20th of a month, and who pays salary in that month, files the first a-melding by the 15th of the next month (forskrift 2014-06-24-857 § 2-1 fifth paragraph). Skatteetaten cannot extend the a-melding deadline (deadlines page).

A small group of employers whose staff work in several countries in a month can apply to defer the due date for withheld tax to the 5th of the following month, until the end of 2027. It needs a decision from Skatteetaten (employer obligations page).

## Penalties and interest

- **Liability for withholding (sktbl. § 16-20).** If the employer does not withhold as chapter 5 requires, or does not pay the withheld amount by the § 10-10 deadline, the employer is liable for the amount. Failing to withhold creates no liability if the employer shows it was not due to neglect or lack of care.
- **Coercive fine for a missing a-melding (a-opplysningsloven § 10; forskrift 2014-06-24-857 § 4-2).** Normally 1/10 of the court fee per day for each income recipient not reported: NOK 134.50 a day in 2026. The total is at most 1,000 court fees (NOK 1,345,000).
- **Infringement fee for a late a-melding (a-opplysningsloven § 11).** At most 15 court fees (NOK 20,175).
- **Additional tax (skatteforvaltningsloven §§ 14-3, 14-5, 14-6).** A withholding agent that gives wrong or incomplete information that can give a tax advantage pays 20% of the advantage, plus 20% or 40% where it acted wilfully or with gross negligence.
- **Late-payment interest (sktbl. §§ 11-1, 11-6 first paragraph).** Runs from the due date until payment, at the rate set under the Late Payment Interest Act (forsinkelsesrenteloven § 3 first paragraph).

## Cross-border points

- **PAYE scheme.** A non-resident on a short work stay taxed under skatteloven § 2-3 first paragraph letters d to f or second paragraph is in the chapter 20 scheme: a flat rate on gross pay and no deductions (§ 20-2). Above the income cap the whole income is taxed under the ordinary rules (§ 20-3). The scheme is voluntary. Withheld source tax is reported as ordinary withholding in the a-melding (Forskuddsutskrivingen 2026).
- **Foreign employer.** Reports pay in the a-melding for the month of payment, by the 5th of the next month (Skatteetaten deadlines page).
- **Tax paid abroad.** An employer that shows that withholding or its equivalent is paid abroad on the employee's income may be exempted from Norwegian withholding if it gives security for the amount (sktbl. § 5-5 seventh paragraph).
- **Social security coverage.** Whether employee and employer contributions are due depends on National Insurance membership, including EEA and agreement certificates. NAV decides membership; this skill does not.

## Worked examples

### Example 1: zone I monthly pay run, percentage card

An Oslo company (zone I) pays a secondary-job employee NOK 60,000 on Friday 20 March 2026. The employee's card says 32% (a percentage card; the rate comes from the card, not from the law). There are no benefits, pension or union deductions.

1. Withholding: 60,000 x 32% = NOK 19,200. Net pay NOK 40,800.
2. The NOK 19,200 is due on Monday 23 March 2026, the first working day after the Friday payday (sktbl. §§ 10-10, 10-2).
3. Employer contribution: 60,000 x 14.1% = NOK 8,460. The March and April contributions are due together on 15 May 2026.
4. The March a-melding is due on 5 April 2026. That is Easter Sunday and 6 April is Easter Monday, so the deadline moves to Tuesday 7 April 2026.

```oa-check
name: Norway zone I pay run, NOK 60,000, 32% card, 2026
inputs:
  gross_pay: 60000
  card_rate: 0.32
  zone_i_rate: 0.141
steps:
  - withholding: gross_pay * card_rate
  - net_pay: gross_pay - withholding
  - employer_contribution: gross_pay * zone_i_rate
  - total_cost: gross_pay + employer_contribution
expected:
  withholding: 19200
  net_pay: 40800
  employer_contribution: 8460
  total_cost: 68460
```

### Example 2: zone Ia employer that uses up the NOK 850,000 allowance

A company registered only in zone Ia, in a general industry, not in financial difficulty and with no other de minimis aid, has reportable pay of NOK 30,000,000 in 2026. It pays 10.6% until the saving against 14.1% equals NOK 850,000, then 14.1%.

1. Saving per krone at the reduced rate: 14.1% - 10.6% = 3.5%.
2. Pay that uses up the allowance: 850,000 / 3.5% = NOK 24,285,714.29.
3. Contribution at 10.6% on that pay: NOK 2,574,285.71.
4. The remaining NOK 5,714,285.71 at 14.1%: NOK 805,714.29.
5. Total contribution NOK 3,380,000.00. Check: the full 14.1% (NOK 4,230,000) less the NOK 850,000 allowance.

```oa-check
name: Norway zone Ia employer contribution with NOK 850,000 allowance, 2026
inputs:
  annual_pay: 30000000
  high_rate: 0.141
  low_rate: 0.106
  allowance: 850000
steps:
  - pay_at_low_rate: min(annual_pay, allowance / (high_rate - low_rate))
  - contribution_low: pay_at_low_rate * low_rate
  - contribution_high: (annual_pay - pay_at_low_rate) * high_rate
  - total_contribution: contribution_low + contribution_high
  - check_against_full_rate: annual_pay * high_rate - allowance
expected:
  pay_at_low_rate: 24285714.29
  contribution_low: 2574285.71
  contribution_high: 805714.29
  total_contribution: 3380000.00
  check_against_full_rate: 3380000.00
```

## Ask the client first

1. Where is the work done, and in which zone is the enterprise or sub-unit registered?
2. Is the client the main or secondary employer, and what card (table, percentage, frikort, PAYE) does each employee have?
3. Are any employees non-resident or on short stays (PAYE scheme, A1 or agreement certificates)?
4. What is paid besides cash salary: benefits in kind, reimbursements, pension premiums, holiday pay?
5. What are the paydays, and has Skatteetaten granted a deferral?
6. Is the employer in an excluded sector or in financial difficulty? Both change the zone Ia and reduced rates.

## Sources

| Source | URL | Read on |
|---|---|---|
| Skattebetalingsloven (lov 2005-06-17-67) §§ 5-1 to 5-11, 10-2, 10-10, 11-1, 11-6, 16-20 | https://lovdata.no/dokument/NL/lov/2005-06-17-67 | 2026-10-30 |
| Skattebetalingsforskriften (forskrift 2007-12-21-1766) §§ 5-1-4, 5-7-1, 5-7-2 | https://lovdata.no/forskrift/2007-12-21-1766/§5-7-1 | 2026-10-30 |
| Folketrygdloven (lov 1997-02-28-19) § 23-2 | https://lovdata.no/lov/1997-02-28-19/§23-2 | 2026-10-30 |
| A-opplysningsloven (lov 2012-06-22-43) §§ 4, 10, 11 | https://lovdata.no/dokument/NL/lov/2012-06-22-43 | 2026-10-30 |
| A-opplysningsforskriften (forskrift 2014-06-24-857) §§ 2-1, 4-1, 4-2 | https://lovdata.no/forskrift/2014-06-24-857/§2-1 | 2026-10-30 |
| Skatteforvaltningsloven (lov 2016-05-27-14) §§ 14-3, 14-5, 14-6 | https://lovdata.no/dokument/NL/lov/2016-05-27-14 | 2026-10-30 |
| Skatteloven (lov 1999-03-26-14) §§ 20-1 to 20-3 | https://lovdata.no/lov/1999-03-26-14/§20-3 | 2026-10-30 |
| Rettsgebyrloven (lov 1982-12-17-86) § 1 and note 1 (court fee NOK 1,345 from 1 January 2026) | https://lovdata.no/lov/1982-12-17-86/§1 | 2026-10-30 |
| Skattedirektoratet, Arbeidsgiveravgift til folketrygden for 2026 (6 January 2026) | https://www.skatteetaten.no/rettskilder/type/skattedirektoratets-meldinger/arbeidsgiveravgift-til-folketrygden-for-2026/ | 2026-10-30 |
| Skatteetaten, Forskuddsutskrivingen 2026 (15 December 2025) | https://www.skatteetaten.no/rettskilder/type/uttalelser/uttalelser/forskuddsutskrivingen-2026/ | 2026-10-30 |
| Skatteetaten, employer's national insurance contributions, rates 2026 | https://www.skatteetaten.no/en/rates/employers-national-insurance-contributions/ | 2026-10-30 |
| Skatteetaten, National Insurance contributions, rates 2026 | https://www.skatteetaten.no/en/rates/national-insurance-contributions/ | 2026-10-30 |
| Skatteetaten, a-melding deadlines and payment | https://www.skatteetaten.no/en/business-and-organisation/employer/the-a-melding/deadlines-and-payment/ | 2026-10-30 |
| Skatteetaten, payment of withholding tax and employer's contributions | https://www.skatteetaten.no/en/business-and-organisation/employer/employers-national-insurance-contributions/payment-of-withholding-tax-and-employers-national-insurance-contributions/ | 2026-10-30 |
| Skatteetaten, employer withholding obligations (deferral scheme) | https://www.skatteetaten.no/en/business-and-organisation/employer/tax-deduction-cards-and-tax-deductions/as-an-employer-you-are-obliged-to-make-withholding-tax-deductions/ | 2026-10-30 |
| Skatteetaten, how to deduct the correct amount of tax | https://www.skatteetaten.no/en/business-and-organisation/employer/tax-deduction-cards-and-tax-deductions/how-to-deduct-the-correct-amount-of-tax/ | 2026-10-30 |
| Skatteetaten, tax deduction cards for employers | https://www.skatteetaten.no/en/business-and-organisation/employer/tax-deduction-cards-and-tax-deductions/tax-deduction-cards/about-tax-deduction-cards-for-you-as-an-employer/ | 2026-10-30 |

Not yet confirmed: the simplified settlement scheme (forenklet oppgjørsordning) for household employers; the late-payment interest rate in force in 2026 (set by regulation under forsinkelsesrenteloven § 3); the detailed sector exclusions and financial-difficulty rules for the reduced contribution rates; financial activity tax on wages; valuation of benefits in kind; the withholding tables; seafarer, fishing and Svalbard rules.
