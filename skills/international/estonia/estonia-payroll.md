---
name: estonia-payroll
description: "Estonian payroll for tax year 2026: running a monthly payroll for employees and board members of an Estonian employer. Covers the 22% withholding income tax, the flat 2026 basic exemption (EUR 700 a month, EUR 776 at pensionable age, no income taper), the 1.6% employee and 0.8% employer unemployment insurance premiums, the 2%, 4% or 6% funded pension (II pillar) contribution, the 33% employer social tax on the EUR 886 monthly minimum base, the order of deductions, fringe benefits at 22/78, the employment register, form TSD and payment by the 10th, interest at 0.06% a day and coercive fines. Trigger on: Estonia payroll, gross to net Estonia, palgaarvestus, netopalk, maksuvaba tulu 2026, TSD lisa 1, kinnipeetav tulumaks, II sammas, töötuskindlustusmakse. Out of scope: estonia-social-contributions (social tax in depth, self-employed FIE), estonia-income-tax (annual return), ee-corporate-income-tax, ee-cross-border (non-resident employees in depth)."
version: 0.2
jurisdiction: EE
category: international
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
verified_by: pending
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia payroll, tax year 2026

> **Source-cited draft.** Built by Michael Cutajar and the OpenAccountants team from the Income Tax Act (Tulumaksuseadus, TuMS), the Social Tax Act (Sotsiaalmaksuseadus, SMS), the Unemployment Insurance Act (Töötuskindlustuse seadus, TKindlS), the Funded Pensions Act (Kogumispensionide seadus, KoPS) and the Taxation Act (Maksukorralduse seadus, MKS), with Estonian Tax and Customs Board (EMTA) and Ministry of Finance pages, read on 2026-10-24. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Estonian professional.

Tax year: the calendar year. Currency: euro. Estonian payroll is cash based: the rates of the month the pay is actually paid out apply, and the payment is declared in the TSD for that month. One body collects everything: EMTA, through the monthly form TSD.

Five charges come off or on top of each gross wage:

| Charge | Who bears it | 2026 rate |
|---|---|---|
| Income tax (tulumaks) | Employee, withheld | 22% after deductions |
| Unemployment insurance premium (töötuskindlustusmakse) | Employee, withheld | 1.6% |
| Funded pension contribution (kogumispensioni makse, II pillar) | Employee, withheld | 2%, 4% or 6% |
| Social tax (sotsiaalmaks) | Employer, on top | 33%, minimum base EUR 886 a month |
| Unemployment insurance premium | Employer, on top | 0.8% |

Related skills: `estonia-social-contributions` (social tax, the II pillar split and self-employed FIE in depth), `estonia-income-tax` (the annual return and the year-end basic exemption), `ee-corporate-income-tax` (fringe benefits sit in the same TSD), `ee-cross-border` (residence and treaties), `ee-tax-overview`.

## Who this applies to

- **Employers.** A resident company, a state or local authority, a sole proprietor (FIE) who employs people, and a non-resident with a permanent establishment in Estonia or acting as an employer in Estonia (TuMS § 48(2); TKindlS § 4(2); SMS § 4). The employer withholds and pays.
- **Employees and officials.** Pay under an employment contract or public service is "palgatulu" (TuMS § 13(1)). It carries all five charges.
- **Board members** (juhatuse liige) of a legal person. Fees are taxed like pay (TuMS § 13(2)) and carry social tax (SMS § 2(1) point 4) and the II pillar (KoPS § 7(1)). A board member not covered by the Employment Contracts Act is not insured for unemployment, so no unemployment premium is due (TKindlS § 3(2) point 3).
- **Service contracts** (töövõtu-, käsundusleping). Income tax is withheld (TuMS § 41 point 3). Social tax and the II pillar are due unless the payee is a registered FIE and the fee is business income (SMS § 9(1) point 2; KoPS § 11(1) point 2).
- **Out of scope:** the self-employed person's own social tax (see `estonia-social-contributions`) and the annual personal return (see `estonia-income-tax`).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Income tax rate | 22% | 2026 | https://www.riigiteataja.ee/akt/109072026066 (TuMS § 4(1)) |
| Basic exemption, annual (maksuvaba tulu) | EUR 8,400 | 2026 | https://www.riigiteataja.ee/akt/109072026066 (TuMS § 23(1)) |
| Basic exemption the employer may give each month, on written application | up to 1/12 of EUR 8,400 = EUR 700 | 2026 | https://www.riigiteataja.ee/akt/109072026066 (TuMS § 42(1)) |
| Basic exemption from the year a person reaches pensionable age | EUR 9,312 a year (EUR 776 a month) | 2026 | https://www.riigiteataja.ee/akt/109072026066 (TuMS § 23⁵(1)) |
| Income taper on the basic exemption | Abolished from 1 January 2026; the exemption no longer falls as income rises | 2026 | https://www.fin.ee/uudised/2026-aastal-joustuvad-seadusemuudatused |
| Employee unemployment insurance premium | 1.6% | 2026 to 2029 | https://www.riigiteataja.ee/akt/130092025003 (Government Regulation No. 78 of 25.09.2025, § 1(1)) |
| Employer unemployment insurance premium | 0.8% | 2026 to 2029 | https://www.riigiteataja.ee/akt/130092025003 (§ 1(2)) |
| Funded pension (II pillar) contribution | 2% default; 4% or 6% if chosen | 2026 | https://www.riigiteataja.ee/akt/103122024016 (KoPS § 9) |
| Social tax rate | 33% | 2026 | https://www.riigiteataja.ee/akt/121052026019 (SMS § 7(1)) |
| Social tax monthly minimum base (kuumäär) | EUR 886 (minimum social tax EUR 292.38) | 2026 | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Minimum monthly wage, full time | EUR 886 to 31 March 2026; EUR 946 from 1 April 2026 (EUR 5.67 an hour) | 2026 | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates (Government Regulation No. 36 of 23.03.2026) |
| Fringe benefit income tax | 22/78 of the benefit | 2026 | https://www.riigiteataja.ee/akt/109072026066 (TuMS §§ 4(1¹), 48) |
| Tax-free birth allowance from employer | Up to 5 × EUR 700 = EUR 3,500 per child (still subject to social tax, unemployment premium and II pillar) | 2026 | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/income-tax-and-basic-exemption |
| Employee health promotion costs exempt from fringe benefit tax | EUR 400 per employee a year | 2026 | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates |
| Interest on late payment | 0.06% a day | 2026 | https://www.riigiteataja.ee/akt/116102026009 (MKS § 117(1)) |

The planned rise of the income tax rate to 24% from 2026 was cancelled; the rate stays 22% (Ministry of Finance, 2026 law changes).

## The taxable base

**Income tax, step by step.** The employer computes withholding each month in this order (TuMS § 42):

1. Start with gross pay for the month (TuMS § 13).
2. Deduct the employee's unemployment premium (1.6%) withheld from it (§ 42(5)).
3. Deduct the II pillar contribution withheld from it, for a resident (§ 42(6)).
4. Deduct the basic exemption, up to EUR 700, if the employee has given this employer a written application (§ 42(1)). Only one payer may apply it, except that a person who also gets a state pension may split it between the two, within the monthly limit (§ 42(2) and (2³)).
5. Withhold 22% of what is left (§ 43(1) point 1).

The 2026 basic exemption is flat. Up to 2025 it fell from EUR 654 a month to zero as income rose. That taper is repealed (TuMS § 23(2) to (5), repealed from 1 January 2026). A payroll still applying the 2025 taper gives too little exemption to anyone above the old taper start and over-withholds.

The monthly limit is a cap, not a carry-forward. If pay after deductions is below EUR 700, the employer does not give the unused part in a later month. The employee gets it back through the annual return, where the full EUR 8,400 applies (TuMS § 23(1)).

**Pensionable age.** From the year a person reaches pensionable age the basic exemption is EUR 9,312 a year, and the Social Insurance Board applies it to the state pension first. Any part the pension does not use can be applied by the employer on a written application (TuMS § 42(1³)). The employee unemployment premium stops at the end of the month the person reaches pensionable age or is granted an early or flexible old-age pension; the employer's 0.8% continues (TKindlS § 42(1) point 1, § 40(1) point 2).

**Social tax base.** Social tax is charged on the gross pay, with no ceiling. For an employee or official it is charged on at least EUR 886 a month even if pay is lower (SMS § 2(2)), so the minimum is EUR 292.38. If the person has several employers, the minimum applies only through the employer that gives the basic exemption (SMS § 2(2¹)). It does not apply, and social tax is paid on actual pay, for among others: a state pensioner or a person with partial or no work capacity; a parent raising a child under 3 or three or more children under 19; a person with shortened working time under the Employment Contracts Act § 43(4) or (6); and for up to 12 months after hiring someone who was registered unemployed for at least six months (SMS § 2(4)). For a month where the employee refused work under the Employment Contracts Act § 19, the minimum is pro-rated by time worked (SMS § 2(3)). See `estonia-social-contributions` for the full list.

**What is outside the base.** Business travel expense reimbursements and foreign per diems within the limits (EUR 75 a day for the first 15 days in a month, EUR 40 a day after that) are not income (TuMS § 13(3) point 1) and carry no social tax (SMS § 3 point 1). Statutory severance pay carries income tax and social tax but no unemployment premium (TKindlS § 40(2) point 1).

**Fringe benefits (erisoodustus).** Any benefit given because of employment or board membership, such as private use of a company car, paid housing costs or non-statutory insurance, is taxed on the employer, not withheld from the employee (TuMS § 48(1) and (4)). Income tax is 22/78 of the benefit's value. Social tax at 33% is then due on the benefit plus that income tax, and it is not attributed to the person (SMS § 2(1) point 7, § 9(1) point 3). Both go in the TSD.

## Deadlines and filing

| What | When | Where |
|---|---|---|
| Register the start of work in the employment register (töötamise register) | No later than the moment the person starts work (MKS § 25²(3)) | e-MTA |
| Register a suspension or end of work | Within 10 days (MKS § 25²(4)) | e-MTA |
| Form TSD (income tax, social tax, unemployment premiums, II pillar, fringe benefits) | 10th day of the month after the month of payment (TuMS § 54(1) and (2); SMS § 9(1) point 4; TKindlS § 42(1) point 3) | e-MTA |
| Payment of everything on the TSD | Same day, the 10th (TuMS § 54(4); SMS § 9(1) point 4; TKindlS § 42(1) point 3) | EMTA prepayment account |
| Employee's choice of II pillar rate (4% or 6%, or back to 2%) | Application to the pension registrar by 30 November; the new rate applies from 1 January of the next year (KoPS § 17²(8)) | Pension registrar or account manager |

The employer must check with the pension register whether each payee owes the II pillar contribution, and at what rate (KoPS § 11(1) point 1). EMTA says the obligation can change on 1 January, 1 May and 1 September, and recommends checking in December, April and August.

A deadline falling on a weekend moves to the next working day; EMTA's own example is the September 2026 TSD, due Monday 12 October 2026.

**Data-based TSD.** From 1 October 2026 EMTA accepts salary data sent straight from payroll software and builds the TSD from it. Annexes 1 and 2 are replaced by one view of salary payments. October 2026 payments, due 10 November 2026, are the first that can go through the new system. The old CSV upload stays available until the end of 2027.

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| Tax or premium not paid by the 10th | Interest at 0.06% a day from the day after the due date to the day of payment, inclusive | MKS §§ 115(1), 117(1) |
| TSD not filed | EMTA sets a new deadline with a warning; coercive fine up to EUR 1,300 the first time, EUR 2,000 the second, EUR 3,300 in total for the same return | MKS § 91 |
| Work not registered in the employment register | Coercive fine up to EUR 1,300 the first time, EUR 2,000 the second, EUR 3,300 in total | MKS § 25⁸ |
| Intentionally false or missing data that reduces a tax or withholding liability | Fine up to 300 fine units (EUR 8 each, so EUR 2,400) for a person; up to EUR 32,000 for a legal person | MKS § 153¹; Penal Code (KarS) § 47(1) |

The unemployment premium is treated as a tax for collection, interest and sanctions (TKindlS § 42(4) and (5)).

## Cross-border points

- **Non-resident employees** paid for work in Estonia: the employer withholds 22%. Only the unemployment premium is deducted first; the employer does not give the basic exemption (TuMS § 41 point 2, § 42(5)). A non-resident does not pay into the II pillar, because KoPS § 6 covers residents only. Treaty relief and the 183-day test are in `ee-cross-border`.
- **Social security coordination.** Inside the EU, EEA and Switzerland, Regulation (EC) No 883/2004 decides which country's social security applies. A worker posted to Estonia with an A1 certificate from another state stays in that state's system; one posted out of Estonia with an Estonian A1 stays on Estonian social tax. Check the A1 before the first payroll.
- **Foreign employer with staff in Estonia.** A non-resident acting as an employer in Estonia must withhold and pay the unemployment premium and declare it in the TSD (TKindlS § 4(2) point 4), and is liable for fringe benefit tax (TuMS § 48(2)).
- **Seafarers** on qualifying ships have a special social tax base and rate (SMS § 2(4) point 8, § 7(2¹)). Out of scope here.

## Worked examples

### Example 1: resident employee, EUR 2,500 gross, II pillar 2%, basic exemption claimed (2026)

Maria works full time for Alpha OÜ in Tallinn for EUR 2,500 a month, paid on the last day of the month. She is under pensionable age, a II pillar member at the default 2%, and has given Alpha OÜ her basic exemption application.

The unemployment premium is 1.6% of 2,500, so EUR 40.00. The II pillar contribution is 2%, so EUR 50.00. Taxable pay is 2,500 minus 40, minus 50, minus the EUR 700 basic exemption, so EUR 1,710.00. Income tax at 22% is EUR 376.20. Maria's net pay is EUR 2,033.80.

On top, Alpha OÜ pays social tax of 33% on EUR 2,500, so EUR 825.00, and the employer premium of 0.8%, so EUR 20.00. Her total cost to Alpha is EUR 3,345.00. The TSD for an October payment, due 10 November, shows EUR 1,311.20 to pay.

```oa-check
name: Estonia 2026, resident employee EUR 2,500 gross, II pillar 2%, basic exemption claimed
inputs:
  gross: 2500
  ui_employee_pct: 1.6
  pillar_pct: 2
  basic_exemption_month: 700
  income_tax_pct: 22
  social_tax_pct: 33
  ui_employer_pct: 0.8
steps:
  - ui_employee: pct(gross, ui_employee_pct)
  - pillar: pct(gross, pillar_pct)
  - taxable: max(0, gross - ui_employee - pillar - basic_exemption_month)
  - income_tax: pct(taxable, income_tax_pct)
  - net_pay: gross - ui_employee - pillar - income_tax
  - social_tax: pct(gross, social_tax_pct)
  - ui_employer: pct(gross, ui_employer_pct)
  - employer_cost: gross + social_tax + ui_employer
  - paid_to_emta: income_tax + ui_employee + pillar + social_tax + ui_employer
expected:
  ui_employee: 40.00
  pillar: 50.00
  taxable: 1710.00
  income_tax: 376.20
  net_pay: 2033.80
  social_tax: 825.00
  ui_employer: 20.00
  employer_cost: 3345.00
  paid_to_emta: 1311.20
```

### Example 2: part-time employee at EUR 600, II pillar 4%, minimum social tax base bites (2026)

Jaan works part time for Beta OÜ for EUR 600 a month. This is his only job, Beta OÜ applies his basic exemption, and none of the SMS § 2(4) exceptions apply: he is not a pensioner, has no child under 3 and was not recently unemployed. He chose a 4% II pillar rate.

The unemployment premium is EUR 9.60 and the II pillar EUR 24.00. Pay after those is EUR 566.40, below the EUR 700 monthly exemption, so the exemption used is EUR 566.40 and no income tax is withheld. The unused EUR 133.60 is not carried to the next month by the employer; Jaan can only use it in his annual return. Net pay is EUR 566.40.

Social tax is the edge. Beta OÜ pays 33% on the higher of actual pay and the EUR 886 minimum base, so on EUR 886: EUR 292.38, not EUR 198.00. The employer premium is on actual pay only: EUR 4.80. Beta's cost is EUR 897.18.

```oa-check
name: Estonia 2026, part-time EUR 600, II pillar 4%, minimum social tax base EUR 886
inputs:
  gross: 600
  ui_employee_pct: 1.6
  pillar_pct: 4
  basic_exemption_month: 700
  income_tax_pct: 22
  social_tax_pct: 33
  social_tax_min_base: 886
  ui_employer_pct: 0.8
steps:
  - ui_employee: pct(gross, ui_employee_pct)
  - pillar: pct(gross, pillar_pct)
  - before_exemption: gross - ui_employee - pillar
  - exemption_used: min(before_exemption, basic_exemption_month)
  - unused_exemption: basic_exemption_month - exemption_used
  - income_tax: pct(before_exemption - exemption_used, income_tax_pct)
  - net_pay: gross - ui_employee - pillar - income_tax
  - social_tax_base: max(gross, social_tax_min_base)
  - social_tax: pct(social_tax_base, social_tax_pct)
  - ui_employer: pct(gross, ui_employer_pct)
  - employer_cost: gross + social_tax + ui_employer
expected:
  ui_employee: 9.60
  pillar: 24.00
  before_exemption: 566.40
  exemption_used: 566.40
  unused_exemption: 133.60
  income_tax: 0.00
  net_pay: 566.40
  social_tax_base: 886.00
  social_tax: 292.38
  ui_employer: 4.80
  employer_cost: 897.18
```

## Ask the client first

1. **When is pay actually paid out?** The month of payment, not the month worked, fixes the rates and the TSD (cash basis). December 2025 pay paid in January 2026 uses 2026 rules.
2. **Has the employee given you a basic exemption application, and do they work for anyone else or get a state pension?** Only one payer gives it (two if one is the Social Insurance Board), and the social tax minimum follows the employer that gives it.
3. **Is the person a resident, and do they have an A1 from another country?** This decides the basic exemption, the II pillar and whether Estonian social tax applies at all.
4. **Does an SMS § 2(4) exception apply** (pensioner, partial work capacity, child under 3 or three children under 19, recent unemployment, shortened hours)? If so, social tax is on actual pay, not EUR 886.
5. **What is the II pillar status and rate in the pension register this month?** None, 2%, 4% or 6%.
6. **Board member, employee or contractor?** Board fees carry no unemployment premium; a registered FIE's business invoice carries no social tax from the payer.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act (Tulumaksuseadus), consolidated text in force from 01.10.2026, §§ 4, 13, 23, 23⁵, 41, 42, 43, 48, 54 | https://www.riigiteataja.ee/akt/109072026066 | 2026-10-24 |
| Social Tax Act (Sotsiaalmaksuseadus), consolidated text in force 22.05.2026 to 24.10.2026, §§ 2, 2¹, 3, 4, 7, 9 | https://www.riigiteataja.ee/akt/121052026019 | 2026-10-24 |
| Unemployment Insurance Act (Töötuskindlustuse seadus), consolidated text in force from 01.10.2026, §§ 3, 4, 40, 41, 42 | https://www.riigiteataja.ee/akt/130062026040 | 2026-10-24 |
| Government Regulation No. 78 of 25.09.2025, unemployment insurance premium rates 2026 to 2029 | https://www.riigiteataja.ee/akt/130092025003 | 2026-10-24 |
| Funded Pensions Act (Kogumispensionide seadus), consolidated, §§ 6, 7, 9, 11, 17² | https://www.riigiteataja.ee/akt/103122024016 | 2026-10-24 |
| Taxation Act (Maksukorralduse seadus), consolidated text in force from 17.10.2026, §§ 25², 25⁸, 91, 115, 117, 153¹ | https://www.riigiteataja.ee/akt/116102026009 | 2026-10-24 |
| Penal Code (Karistusseadustik), § 47 (fine unit EUR 8) | https://www.riigiteataja.ee/akt/109072026028 | 2026-10-24 |
| EMTA, Tax rates (2024 to 2026, minimum wage table) | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates | 2026-10-24 |
| EMTA, Social tax (2026 minimum base) | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax | 2026-10-24 |
| EMTA, Income tax and basic exemption (birth allowance 2026) | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/income-tax-and-basic-exemption | 2026-10-24 |
| EMTA, Contributions to mandatory funded pension | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension | 2026-10-24 |
| EMTA, Submission of declaration form TSD (data-based TSD from 1 October 2026) | https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/submission-declaration-form-tsd | 2026-10-24 |
| Ministry of Finance, Law changes in force in 2026 | https://www.fin.ee/uudised/2026-aastal-joustuvad-seadusemuudatused | 2026-10-24 |

Not yet confirmed: the 2026 State Budget Act text that sets the EUR 886 social tax monthly rate (taken from EMTA and the Ministry of Finance, not read in the Act itself); the Social Tax Act version in force from 25.10.2026 (not read); the pensionable age in 2026 (not stated here); the weekend roll-forward rule in the Taxation Act (taken from EMTA's example, not the Act).
