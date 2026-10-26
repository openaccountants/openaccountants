---
name: fi-employer-payroll
description: >
  Prepare ordinary Finnish employer payroll for tax year 2026, including wage
  classification, tax-card ceilings, fringe-benefit valuation, employee deductions,
  employer contributions, Incomes Register reporting and corrections. Covers
  private-sector employees, working owners and insurance eligibility screens;
  separates TyEL pensions, unemployment, health, accident and group-life cover.
  Use for Finnish payslips, cash plus benefits, payroll taxes, salary reporting,
  employer's separate report, contribution bases and missing tax cards. Includes
  current statutory and annual-decision sources, payment deadlines, late-reporting
  consequences and two executable examples. Pension contributions for entrepreneurs
  are computed in the linked YEL Guide; international coverage requires the
  actual A1 or applicable-law decision.
jurisdiction: FI
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-26
version: 0.8
---

# Finland employer payroll reporting v0.8

**Tax year:** 2026. Ordinary private-sector payroll, including taxable benefits. Local source-cited draft awaiting fresh independent whole-pack review.

## Who this applies to

Start with the actual employment/fee relationship, payer, residence and applicable insurance law. Prepayment Act section 13 treats employment compensation, fringe benefits and specified personal fees as wages; some board/management fees are tax wages even without an employment contract. That does not automatically put them in every insurance base. Business trade income follows section 25's prepayment-register/withholding route. Resolve working-owner YEL versus TyEL separately. [Prepayment Act 1118/1996, sections 9, 13, 25][prepayment-law]; [Employees Pensions Act 395/2006, sections 4, 7, 70][tyel-law].

Keep cash wages, taxable benefits, tax-free reimbursements, statutory insurance wages and payment dates in separate columns. Wage withholding, employee pension/unemployment deductions and **employer** contributions are different liabilities. State/public pensions, seafarers, athletes and some foreign assignments use their own statutory coverage; do not force them into ordinary TyEL. [Employees Pensions Act, sections 3–4][tyel-law]; [Unemployment Financing Act, sections 12–15][fund-law].

## Rates, bands and thresholds

| Item | 2026 rule | Primary source |
|---|---|---|
| Wage withholding | Valid tax-card basic/additional rates and income ceiling; ordinary missing-data rate 60% where no other prescribed rate applies | [Prepayment Decree 1124/1996, sections 2–4][decree] |
| Employer health | 1.91% of qualifying wages; starts the month after 16th birthday and ends after the month of 68th birthday, Finnish health coverage required | [Act 771/2016, sections 4–5][employer-health]; [Decree 1026/2025, section 3][health-rates] |
| Employee health | Care 1.10% wage/work base; daily allowance 0.88% on its full qualifying base if annual wage/work total at least EUR 17,255; included in ordinary tax-card withholding | [Decree 1026/2025, sections 1–2][health-rates]; [Health Insurance Act chapter 18][health-law] |
| Employee TyEL | 7.30% for covered employees in 2026; insurer invoices determine the full premium | [Employees Pensions Act, sections 152–153][tyel-law]; [Vero 2026 contributions][insurance] |
| TyEL monthly minimum | EUR 71.72 per employee/employer; indexed statutory threshold | [Employees Pensions Act, sections 4, 96][tyel-law]; [Finnish Centre for Pensions annual statutory-amount table][tyel-index] |
| TyEL ages | From month after 17th birthday; through birthday month for upper age 68 (born through 1957), 69 (1958–1961), 70 (1962 onward) | [Employees Pensions Act, section 4][tyel-law] |
| Ordinary employer unemployment | 0.31% on ordinary annual payroll through EUR 2,509,500; 1.23% above | [Unemployment Financing Act 555/1998, section 18][fund-law] |
| Employee unemployment | 0.89%; part-owner 0.39%; employer on part-owner wages 0.31% | [Unemployment Financing Act, section 18][fund-law] |
| Unemployment small payroll | Fund-payment threshold EUR 1,500/year; employee deduction still required below threshold | [Act 555/1998, sections 12a, 21][fund-law]; [Employment Fund liability][fund-scope] |
| Accident / group life | Employer-only actual policy premiums; accident policy required above the indexed annual wage threshold; no universal flat rate | [Accident Act 459/2015, sections 3, 166, 268][accident-law]; [Vero 2026 contributions][insurance] |

Separate part-owner wages from the ordinary employer unemployment band. State enterprises' upper rate is 0.72% and universities' 0.79%, not the ordinary 1.23%. A TyEL average (24.40% total / 17.10% employer in 2026) is an estimate, not a substitute for the actual insurer rate, expenses, bonuses and large-employer risk component. [Unemployment Financing Act, section 18][fund-law]; [Ilmarinen contribution calculation][tyel-calculation].

| Ordinary fringe benefit | 2026 valuation | Official annual decision provision |
|---|---|---|
| Mobile/fixed telephone private-use benefit | EUR 20/month | [Benefit Decision, section 26][benefits] |
| Ordinary employer meal | EUR 8.80 if direct cost including VAT EUR 8.80–14.00; otherwise actual direct cost | [Sections 10–11][benefits] |
| Qualifying restricted meal voucher | 75% nominal value, minimum EUR 8.80, nominal value at most EUR 14; otherwise nominal; working-day/use restrictions apply | [Sections 13–14][benefits] |
| Unlimited / limited company car, first used 2024–2026 | Basic 1.5% adjusted replacement price + EUR 285 / 105 monthly, or 19 / 7 cents private km | [Sections 17–24][benefits] |
| First used 2021–2023 | 1.2% + EUR 300 / 120 monthly, or 20 / 8 cents private km | [Sections 17–24][benefits] |
| First used before 2021 | 0.9% + EUR 315 / 135 monthly, or 21 / 9 cents private km | [Sections 17–24][benefits] |
| Workplace charging, own/limited-benefit car | EUR 30/month pure electric; EUR 20/month plug-in hybrid | [Section 25][benefits] |
| Central-heated housing, Helsinki 1 / 2 | EUR 299 + 13.20/m² / EUR 298 + 12.10/m² per month | [Sections 2–8, postal-code map][benefits] |
| Helsinki 3/Espoo/Kauniainen; Helsinki 4/Vantaa | EUR 266 + 11.20/m²; EUR 214 + 11.20/m² monthly | [Sections 2–8][benefits] |
| Listed regional cities / other metropolitan municipalities; elsewhere | EUR 206 + 9.70/m²; EUR 178 + 8.70/m² monthly | [Sections 2–8, full location list][benefits] |

These are valuation rules after eligibility/classification, not automatic benefits every worker has. Obtain the full annual decision for housing heating/electricity/garage exceptions and car details. [Benefit Decision][benefits].

## The base

### Build the taxable and insured bases

For every pay item record contractual gross cash, benefit value, employee reimbursement, taxable value, each insurance flag and income type. Ordinary salary, bonuses, holiday pay and compensation for unused leave are wages; a true termination damages payment can be taxable without being pension/unemployment earnings. Board fees, stock options, staff benefits and profit-sharing require their specific base exclusions. The insurance bases follow TyEL section 70, Unemployment Financing Act section 19, Accident Act section 81 and employer-health Act section 5, not merely the tax-wage total. [Prepayment Act, section 13][prepayment-law]; [TyEL Act, section 70][tyel-law]; [Act 555/1998, section 19][fund-law]; [Accident Act, section 81][accident-law]; [Act 771/2016, section 5][employer-health].

For taxable benefits, deduct the employee's after-tax reimbursement from the benefit value without reducing contractual cash salary twice. Car replacement-price base is the recommended new retail price less EUR 3,400 plus taxable accessories above EUR 1,200; round the percentage basic component down to EUR 10. Unlimited means employer pays all costs; limited means employee pays at least fuel/energy. Commuting is private driving. Use a driving log for actual-km valuation and the decision's adjustments, including business driving over 30,000 km, pure-electric/qualifying hybrid operating reductions, and Income Tax Act section 64a's EUR 170/month zero-emission car-benefit reduction where eligible. Do not continue the expired workplace-charging exemption in 2026. [Benefit Decision, sections 17–25][benefits]; [Income Tax Act, sections 64–64a][income-law].

Housing value uses correct postal district, full private floor area, heating/electricity and statutory reductions; ordinary rent charged to the employee reduces the taxable benefit. For meals record actual workdays, direct cost, restricted-payment terms, free meals elsewhere and employee payments. A cash meal allowance is not automatically valued at the voucher discount. Section 69's staff-benefit exemption needs collective, ordinary/reasonable arrangements and the particular condition; the October amendment increases the eligible annual personal sports/culture benefit to EUR 540 for tax year 2026, not just benefits provided after 13 October. [Benefit Decision, sections 2–14][benefits]; [Income Tax Act, section 69 and Act 873/2026 commencement][income-law].

Tax-free travel reimbursements require an actual qualifying temporary business trip, travel claim and decision limits. Normal commuting to the regular workplace does not qualify. For 2026 own-car business mileage the basic maximum is EUR 0.55/km (qualifying additions separately); domestic partial per diem EUR 25 for **over six** hours, full EUR 54 for **over ten** hours, with both distance tests (over 15km from departure and over 5km from both home/regular workplace) and free-meal reductions. Foreign per diems require the decision's country/day rules. The 2027 schedule is a different year even if it is now the “latest version.” [Income Tax Act, sections 71–73][income-law]; [2026 Travel Decision, sections 3–14][travel]; [Prepayment Decree, section 17][decree].

### Withhold using the card and available cash

Keep valid electronic/card instruction, effective dates, ceiling and this payer's cumulative covered payments during validity. Allocate the current taxable wage base to remaining basic-rate capacity, then additional-rate excess. A revised card starts its own effective instruction; requesting a higher rate alone does not change its ceiling. Prepayment Decree section 4 includes covered payments made using the prior-year carryover instruction where applicable. A missing paper card is irrelevant if valid electronic data is available; absent applicable data use the statutory default, normally 60% for wages. [Prepayment Decree, sections 2–4][decree]; [Vero tax-card ceiling][ceiling].

Withholding on cash plus benefits is calculated on the taxable total but cannot exceed available gross cash under Prepayment Act section 11. For example, EUR 500 cash + EUR 1,500 benefits at an assumed 40% gives EUR 800 theoretical withholding but only EUR 500 collectible cash. Record the shortfall; do not invent a negative bank payment or silently remove benefits. Noncash benefits ordinarily join each cash-pay period; an occasional benefit can use the decree's same-year allocation, including the at-most-EUR 400 small occasional route. Benefits-only months still require reporting and employer-health/insurance checks. [Prepayment Act, section 11][prepayment-law]; [Prepayment Decree, section 9][decree].

### Insurance eligibility and net pay

Resolve Finnish applicable law/A1 first, then each scheme independently. TyEL starts/ends by the birthday-month rules and monthly minimum in the table; it covers qualifying remuneration even for a pensioner working below the upper age. A working manager with more than 30% personally or more than 50% with family ownership/control is screened for YEL instead; indirect control and family definitions matter. Do not apply both schemes to the same entrepreneurial work. [TyEL Act, sections 4, 7][tyel-law]; [YEL Act, section 3][yel-law].

Unemployment begins the month after turning 18. For those born before 1965 it ends after the month of turning 65; later cohorts use their statutory minimum pension age under section 12a. In 2026 the older-cohort age rule is the relevant upper transition. YEL/MYEL entrepreneurs, specified athletes, seasonal workers and foreign-law cases are excluded. Working part-owners who are not YEL entrepreneurs use reduced employee contribution: leading role with personal ownership at least 15% or personal+family at least 30%, or nonleading ownership/control at least 50%, applying the statutory family/indirect-control rules on payday. Keep the classification evidence. [Unemployment Financing Act, sections 12a, 15, 18–19][fund-law]; [Employment Fund part-owner guidance][fund-scope].

Deduct liable employee unemployment even where total employer annual wages do not exceed EUR 1,500; the employer then retains the deduction, and still reports liability. Above threshold the Fund invoices both shares using actual reported earnings. For covered ordinary annual payroll compute `min(payroll,2509500) × 0.0031 + max(0,payroll−2509500) × 0.0123`; calculate part-owner employer wages at 0.31% separately. [Unemployment Financing Act, sections 12a, 18, 21][fund-law].

Employer health requires Finnish health-insured employee and its age/entrepreneur exceptions; a working YEL owner salary requires the statutory obligation screen, not automatic TyEL. Multiply the established wage base by 1.91%, round the period total to cents. Employee health is already in resident/progressive withholding. Accident cover is arranged before work when the indexed annual wage agreement/payment threshold is exceeded; the employer alone pays the risk/policy rate. Group life is required where the applicable collective agreement requires it, using the actual policy rate; it is not an employee deduction. No single employer all-in percentage can replace these schedules. [Act 771/2016, sections 4–5][employer-health]; [Decree 1026/2025][health-rates]; [Accident Act, sections 3, 166, 268][accident-law]; [Vero insurance][insurance].

Net cash is cash wages + genuine cash reimbursements − collectible withholding − employee pension/unemployment and other legally authorised cash deductions. Benefits are tax/insurance bases, not extra cash. Check cash insufficiency and deduction/recovery rules before finalising a low/no-cash payslip; retain employee amounts still recoverable and insurer obligations separately. Employer cost is gross contractual wage/benefit cost plus **employer** shares; adding the full TyEL invoice after already counting employee deductions overstates employer cost. [Prepayment Act, section 11][prepayment-law]; [TyEL Act, section 152][tyel-law]; [Act 555/1998, section 21][fund-law].

## Deadlines and filing

| Obligation | Ordinary deadline / route | Source |
|---|---|---|
| Worker earnings payment report | Five calendar days after pay is available; weekend/holiday fifth day moves to next business day | [Incomes Register Act 53/2018, section 12][ir-law]; [official deadlines][deadlines] |
| Benefits-only month | By fifth of following month; special following-month cash-pay allocation follows section 12(4) | [Incomes Register Act, section 12][ir-law] |
| Employer separate report | Fifth of following month; regular employer no-wages data required; casual employer relevant payment months | [Incomes Register Act, sections 6, 12][ir-law]; [reporting instructions][reporting] |
| Withholding / employer health payment | Monthly period: next month's 12th, next business day when relevant; approved longer tax periods use their own payment calendar | [Vero reporting/payment][reporting] |
| TyEL | Insurer invoice/contract; earnings reporting uses statutory Incomes Register timing | [TyEL Act, sections 142–144, 152][tyel-law] |
| Unemployment | Fund decision/invoice; quarterly invoices in April, July, October, January | [Act 555/1998, section 21][fund-law]; [Fund payment page][fund-payment] |

Regular employers register and report monthly; a casual employer's limited reporting does not remove each earnings-payment report. Preserve accepted report IDs, tax-period liabilities, actual due dates and payment references; reporting does not make a payment. On errors, replace the original report with complete corrected information using its identifier; cancellation/replacement is required for the particular identifying facts that cannot be replaced. Correct the separate report if employer-health totals change. Overpayments require an unjust-enrichment report and separate recovery details; do not merely net an old error against an unrelated later salary. Under section 12, unjust benefit data are due without undue delay and within one month of discovery; recovery details within five days after receipt of the required repayment information. [Incomes Register Act, sections 6, 12][ir-law]; [Incomes Register correction guidance][corrections].

## Penalties and interest

The five-day filing duty and late-fee trigger are separate. Incomes Register Act sections 22–23 generally start the monthly late-fee clock **after the following month's eighth day**: EUR 3/day, maximum EUR 135; after 45 calendar days add 1% of late taxable remuneration or the larger pension-insured earnings. The amount-based component is capped at EUR 15,000/month. Corrections within 45 days of that eighth-day trigger avoid the fee; later positive corrections use the 1% route. Valid-reason/independent-cause and specified personal-payer exceptions apply. Do not use the self-assessed dividend/VAT return's 2% formula on an earnings report. [Incomes Register Act, sections 22–23][ir-law].

Failure to withhold/pay tax and omitted employer-health liabilities can cause assessed tax and tax increases under Self-assessed Tax Procedure Act sections 37–38: ordinary 10% of tax imposed; 15–50% repeated/manifest disregard; 25% estimated tax; 3% specified unclear/unreasonable cases; up to EUR 200 when no tax imposed, with statutory waiver conditions. Ordinary late tax payment interest is 9.5% annually for 2026, actual days after due date through payment/365. Pension, Fund and accident neglect/default charges follow their own laws/invoices, not the tax-interest rate by assumption. [Act 768/2016, sections 37–38][self-act]; [Vero interest][interest].

## Cross-border points

Tax residence, PE, wage source, treaty exemption and social coverage are distinct tests. Use the [individual cross-border Guide](fi-individual-cross-border-residence.md) before choosing source-tax/progressive cards or the foreign-employment six-month exemption. An A1 determines applicable social law within its scope, not income tax. When Finnish insurance continues on a qualifying foreign posting, statutory **insurance salary** can replace actual foreign wages for pension/health/unemployment bases. The foreign-work wage exemption does not by itself remove minimum health withholding. [TyEL Act, section 72][tyel-law]; [Health Insurance Act, chapter 18 sections 17–18][health-law]; [Act 771/2016, section 5][employer-health]; [Act 555/1998, section 13][fund-law].

## Two worked examples that recompute

**1. Ordinary employee and separate employer health.** Assume EUR 3,000 cash wages, valid assumed 20% tax-card rate without a ceiling issue, all wages eligible for employee TyEL 7.30%, unemployment 0.89% and employer health 1.91%, no benefits/other deductions. Net cash is EUR 2,154.30; EUR 57.30 employer health is additional employer liability. The employee's health is already in the assumed tax-card rate. Actual total employer cost also requires the insurer/Fund/policy charges.

```oa-check
name: Finland 2026 employee net cash and separate employer health
inputs:
  cash_wages: 3000
  assumed_card_rate: 0.20
steps:
  tax_withheld: cash_wages * assumed_card_rate
  employee_pension: cash_wages * 0.073
  employee_unemployment: cash_wages * 0.0089
  net_cash: cash_wages - tax_withheld - employee_pension - employee_unemployment
  employer_health: cash_wages * 0.0191
expected:
  tax_withheld: 600
  employee_pension: 219
  employee_unemployment: 26.70
  net_cash: 2154.30
  employer_health: 57.30
```

**2. Benefit crosses the card ceiling.** Assume EUR 4,000 cash plus eligible EUR 20 phone benefit, all subject to these employee insurance bases. This payer previously paid EUR 28,000 covered income under a valid EUR 30,000 ceiling; assumed card rates 20%/40%. Current EUR 4,020 base splits EUR 2,000 basic / EUR 2,020 additional: tax EUR 1,208 within available cash. Employee pension EUR 293.46, unemployment EUR 35.78 after cent rounding; net cash EUR 2,462.76. Employer health EUR 76.78 is separate. Coverage/card facts are explicit assumptions.

```oa-check
name: Finland phone benefit ceiling crossing and payslip
inputs:
  cash_wages: 4000
  taxable_phone_benefit: 20
  card_ceiling: 30000
  prior_payments: 28000
  basic_rate: 0.20
  additional_rate: 0.40
steps:
  taxable_base: cash_wages + taxable_phone_benefit
  basic_base: min(taxable_base, max(0, card_ceiling - prior_payments))
  additional_base: taxable_base - basic_base
  calculated_withholding: basic_base * basic_rate + additional_base * additional_rate
  collectible_withholding: min(cash_wages, calculated_withholding)
  employee_pension: round(taxable_base * 0.073, 2)
  employee_unemployment: round(taxable_base * 0.0089, 2)
  net_cash: cash_wages - collectible_withholding - employee_pension - employee_unemployment
  employer_health: round(taxable_base * 0.0191, 2)
expected:
  taxable_base: 4020
  basic_base: 2000
  additional_base: 2020
  calculated_withholding: 1208
  collectible_withholding: 1208
  employee_pension: 293.46
  employee_unemployment: 35.78
  net_cash: 2462.76
  employer_health: 76.78
```

## Ask the client first

1. Who is paid, what legal relationship/ownership role applies, where is work done and when is pay available?
2. Which Finnish/A1/other insurance decisions, birth dates and scheme identifiers apply?
3. What cash, benefits, reimbursements and nonordinary payments need classification and valuation?
4. What valid tax-card dates/rates/ceiling and this payer's cumulative earnings apply?
5. Which insurer/policy rates, annual payroll bands and regular-employer/tax-period registrations apply?
6. Which reports, errors, repayments, invoices and paid amounts need correction/reconciliation?

## Sources

| Primary source | Provisions / purpose | Read on |
|---|---|---|
| [Prepayment Act 1118/1996][prepayment-law]; [Decree 1124/1996][decree] | Act sections 9–13, 25; decree sections 2–4, 9, 17; wage/card/cash rules | 2026-10-26 |
| [Income Tax Act 1535/1992][income-law]; [2026 Benefit Decision][benefits]; [2026 Travel Decision][travel] | Sections 64–69, 71–73, Act 873/2026 commencement; annual valuation/reimbursement rules | 2026-10-26 |
| [TyEL Act 395/2006][tyel-law]; [indexed statutory amounts][tyel-index]; [Vero insurance][insurance]; [Ilmarinen contribution calculation][tyel-calculation] | Sections 4, 7, 70, 72, 142–144, 152–153; current threshold/share | 2026-10-26 |
| [YEL Act 1272/2006][yel-law] | Section 3 owner/entrepreneur test | 2026-10-26 |
| [Unemployment Financing Act 555/1998][fund-law]; [Fund liability][fund-scope]; [Fund payment][fund-payment] | Sections 12–15, 18–21; 2026 rates and reporting/invoices | 2026-10-26 |
| [Employer Health Act 771/2016][employer-health]; [Health Insurance Act 1224/2004][health-law]; [Decree 1026/2025][health-rates] | Coverage, wages, insurance salary and 2026 annual rates | 2026-10-26 |
| [Accident Act 459/2015][accident-law] | Sections 3, 8–9, 81, 166, 268; scope, wage and actual rate | 2026-10-26 |
| [Incomes Register Act 53/2018][ir-law]; [deadlines][deadlines]; [reporting][reporting]; [corrections][corrections] | Sections 6, 12, 22–23; reports, recovery and late fees | 2026-10-26 |
| [Self-assessed Tax Procedure Act 768/2016][self-act]; [Vero interest][interest] | Tax collection/understatement penalties and 2026 late interest | 2026-10-26 |

Not yet confirmed: separately scoped public/seafarer/athlete schemes, share incentives, unusual termination and foreign coverage cases. Their own laws apply; the ordinary payroll route above awaits independent pack review. No professional attestation is claimed.

[prepayment-law]: https://www.finlex.fi/fi/lainsaadanto/1996/1118
[decree]: https://www.finlex.fi/fi/lainsaadanto/1996/1124
[income-law]: https://www.finlex.fi/fi/lainsaadanto/1992/1535
[benefits]: https://www.vero.fi/en/detailed-guidance/decisions/47380/in-kind-benefits-fringe-benefits-2026/
[travel]: https://www.vero.fi/syventavat-vero-ohjeet/paatokset/47405/verohallinnon-paatos-verovapaista-matkakustannusten-korvauksista-vuonna-2026/
[insurance]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/being-an-employer/social-insurance-contributions/
[tyel-law]: https://www.finlex.fi/fi/lainsaadanto/2006/395
[tyel-index]: https://www.telp.fi/indeksit/tyoelakelaeissa_saadetyt_rahamaarat_vuodesta-2/tyel_2026/
[tyel-calculation]: https://www.ilmarinen.fi/en/employer/managing-tyel-insurance/determining-the-tyel-contribution/
[yel-law]: https://www.finlex.fi/fi/lainsaadanto/2006/1272
[fund-law]: https://www.finlex.fi/fi/lainsaadanto/1998/555
[fund-scope]: https://www.tyollisyysrahasto.fi/en/Unemploymentinsurancecontribution/payment-liability-for-unemployment-insurance-contributions/
[fund-payment]: https://www.tyollisyysrahasto.fi/en/Unemploymentinsurancecontribution/paying-unemployment-insurance-contributions/
[employer-health]: https://www.finlex.fi/fi/lainsaadanto/2016/771
[health-law]: https://www.finlex.fi/fi/lainsaadanto/2004/1224
[health-rates]: https://www.finlex.fi/fi/lainsaadanto/saadoskokoelma/2025/1026
[accident-law]: https://www.finlex.fi/fi/lainsaadanto/2015/459
[ir-law]: https://www.finlex.fi/fi/lainsaadanto/2018/53
[deadlines]: https://www.vero.fi/en/incomes-register/companies-and-organisations/deadlines-for-reporting/
[reporting]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/being-an-employer/how-to-report-wages-and-employers-contributions/
[ceiling]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/tax_card/tax-rate-and-income-ceiling/
[corrections]: https://www.vero.fi/en/incomes-register/companies-and-organisations/reporting-data-to-the-incomes-register/correcting-data/
[self-act]: https://www.finlex.fi/fi/lainsaadanto/2016/768
[interest]: https://www.vero.fi/en/individuals/payments/paying-taxes/interest-on-late-payments/
