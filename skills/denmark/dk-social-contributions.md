---
name: dk-social-contributions
description: "Danish social contributions for 2026 for employees, employers and the self-employed. Covers the 8% labour market contribution (arbejdsmarkedsbidrag, AM-bidrag), its base and the new 2026 rule that nobody pays it before the year they turn 18; ATP Livslang Pension by hours band (DKK 297 a month in total for 117 hours or more, one third employee, two thirds employer); the employer contributions collected through Samlet Betaling (AUB, Barsel.dk, finansieringsbidrag FIB, AES by branch group) and the duty to insure work accidents; voluntary ATP, AES and AM-bidrag for the self-employed; and the 2026 a-kasse and efterløn contributions as context. Trigger on: AM-bidrag, arbejdsmarkedsbidrag, ATP-bidrag, Samlet Betaling, AUB, Barsel.dk, FIB, AES-bidrag, arbejdsskadeforsikring, a-kasse, efterlønsbidrag, employer cost Denmark. Out of scope, see: dk-income-tax (A-skat, bundskat, B-skat), dk-corporate-tax, dk-capital-gains, denmark-vat-return. Payroll withholding of A-skat is not covered."
version: 0.2
jurisdiction: DK
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Denmark: social contributions (AM-bidrag, ATP and employer contributions) v0.1

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's or employer's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Denmark.

Tax year: calendar year 2026. Currency: Danish kroner (DKK). Denmark funds most social security from general taxation, so the payroll-linked charges are small flat amounts plus one percentage charge, the 8% AM-bidrag. AM-bidrag is a tax collected by Skattestyrelsen. ATP and the employer contributions are collected by ATP through Samlet Betaling (virk.dk).

See also: dk-income-tax (state and municipal income tax, personal allowance, B-skat for the self-employed), dk-corporate-tax (companies), dk-capital-gains, denmark-vat-return.

## Who this applies to

- **AM-bidrag.** Every person liable to Danish tax pays AM-bidrag of 8% of the base (Arbejdsmarkedsbidragsloven, AMBL, § 1). The base for employees is pay in money or kind for personal work, including benefits in kind and employer pension contributions (AMBL § 2). The base for the self-employed is the personal income from the business (AMBL §§ 4 and 5).
- **Under 18.** From income year 2026 the rate is 0% up to and including 31 December of the income year in which the person turns 17, so AM-bidrag starts in the calendar year they turn 18 (AMBL § 1, stk. 2, added by lov nr. 96 of 4 February 2025, § 1, with effect from 1 January 2026 under § 7, stk. 4). Pay, B-income and business profit before that year carry no AM-bidrag (skat.dk, AM-bidrag).
- **Income without AM-bidrag.** SU, pensions paid out, efterløn, kontanthjælp, ledighedsydelse, fleksydelse and dagpenge (skat.dk, AM-bidrag).
- **ATP.** An employer pays ATP for each employee aged 16 or over, with no upper age limit, who works in Denmark or is posted abroad by a Danish employer and works at least 9 hours a week, 18 hours in 14 days or 39 hours a month (virk.dk, ATP employer). The employee pays one third, the employer two thirds.
- **Employer contributions.** A private employer that pays ATP also pays AUB, Barsel.dk, FIB and AES through Samlet Betaling. FIB is paid by private employers registered for VAT or payroll tax (lønsumsafgift); foreign employers pay it even without that registration (virk.dk, FIB).
- **Work accident insurance.** Every employer with staff must insure work accidents with an insurance company and join AES for occupational disease (Arbejdsskadesikringsloven § 48, stk. 1 and 4, § 50). The state, regions, municipalities and the church do not insure accidents (§ 48, stk. 5). Household help under 400 hours a year is outside the duty (§ 48, stk. 6).
- **Self-employed.** AM-bidrag is compulsory. ATP, AES and work accident insurance for the owner are voluntary (virk.dk, ATP self-employed; virk.dk, AES; Arbejdsskadesikringsloven § 48, stk. 2).
- **Out of scope.** Public employers on ATP rate groups B to F, Læreplads-AUB settlements, seafarers under DIS rules, Greenland and the Faroe Islands (AMBL § 9).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| AM-bidrag | 8% of the base | 2026 | https://www.retsinformation.dk/eli/lta/2020/121 |
| AM-bidrag, up to 31 December of the year the person turns 17 | 0% | 2026 | https://www.retsinformation.dk/eli/lta/2025/96 |
| ATP, monthly paid, 117 hours or more a month (employee 99, employer 198) | DKK 297.00 a month | 2026 | https://www.borger.dk/pension-og-efterloen/atp-livslang-pension-oversigt/atp-bidraget/atp-satser-for-privat-virksomhed |
| ATP, monthly paid, 78 to 116 hours (employee 66, employer 132) | DKK 198.00 a month | 2026 | same |
| ATP, monthly paid, 39 to 77 hours (employee 33, employer 66) | DKK 99.00 a month | 2026 | same |
| ATP, monthly paid, under 39 hours | DKK 0 | 2026 | same |
| ATP, 14-day paid, 54 hours or more (employee 52.20, employer 104.40) | DKK 156.60 per 14 days | 2026 | https://virk.dk/vejledning/atp/atp-arbejdsgiver/atp-satser/ |
| ATP, weekly paid, 27 hours or more (employee 26.10, employer 52.20) | DKK 78.30 a week | 2026 | same |
| ATP, casual workers (employee 0.71, employer 1.42) | DKK 2.13 an hour | 2026 | same |
| Hourly rate to convert pay to hours when hours are unknown: men / women | DKK 258.69 / DKK 233.62 | 2026 | same |
| ATP collected per full-time employee per quarter (3 x 297) | DKK 891 | 2026 | https://businessindenmark.virk.dk/guidance/samlet-betaling-bid/sb-employer/samlet-betaling-bid-contribution-rates |
| AUB (training levy), per full-time employee (AUB 596.75 plus VEU 108.50 a quarter) | DKK 2,821 a year; DKK 705.25 a quarter | 2026 | https://virk.dk/vejledning/aub/aub-arbejdsgiver/ |
| AUB deduction | First employee and every 50th employee | 2026 | same |
| Barsel.dk (parental leave fund), per full-time employee | DKK 2,200 a year; DKK 550 a quarter | 2026 | https://virk.dk/vejledning/barsel-dk/bdk-privat-arbejdsgiver/fuldt-omfattet/ |
| FIB (financing contribution), per full-time employee per quarter, of which Lønmodtagernes Garantifond DKK 55 | DKK 82.00 | 2026 | https://businessindenmark.virk.dk/guidance/fib-bid-finansieringsbidrag/fib-bid-finansieringsbidrag |
| AES plus work injury levy, yearly per full-time employee, group 71 (finance and business services; 268 + 189) | DKK 457 | 2026 | https://virk.dk/assets/6feKOXUjVtAaPklFxxBz9C/aes_bidragssatser_2026.pdf |
| AES, group 22 (industry) | DKK 1,558 | 2026 | same |
| AES plus work injury levy, group 41 (construction, other; 1,497 + 826) | DKK 2,323 | 2026 | same |
| AES, group 51 (wholesale and retail) | DKK 539 | 2026 | same |
| AES, group 52 (hotels and restaurants) | DKK 389 | 2026 | same |
| AES, group 83 (social institutions, associations, culture) | DKK 2,911 | 2026 | same |
| FerieKonto admin fee, per employee | DKK 4.00 a month | 2026 | https://businessindenmark.virk.dk/guidance/samlet-betaling-bid/sb-employer/samlet-betaling-bid-contribution-rates |
| Lønmodtagernes Feriemidler admin fee | DKK 5.00 | 2026 | same |
| Voluntary ATP, self-employed | DKK 297 a month | 2026 | https://virk.dk/vejledning/atp/atp-selvstaendig |
| A-kasse unemployment insurance contribution to the state, full-time / part-time insured | DKK 407 / DKK 271 a month | 2026 | https://www.retsinformation.dk/eli/retsinfo/2025/10230 |
| A-kasse contribution, members under 25 (full-time / part-time) | DKK 153 / DKK 102 a month | 2026 | same |
| Efterløn (voluntary early retirement) contribution, full-time / part-time | DKK 593 / DKK 396 a month | 2026 | same |
| ATP paid by a-kasse members, full-time / part-time | DKK 7 / DKK 5 a month | 2026 | same |
| Late payment interest on A-skat and AM-bidrag: base rate 0.1% plus 0.85 points | 0.95% a month | 2026 | https://info.skat.dk/data.aspx?oid=2459995 |
| Reminder fee, A-skat and AM-bidrag (reminder sent only when the tax account debit balance exceeds DKK 5,000), to 13 September 2026 | DKK 65 | 2026 | https://info.skat.dk/data.aspx?oid=2168585 |
| Reminder fee, A-skat and AM-bidrag, from 14 September 2026 | DKK 160 | 2026 | https://www.retsinformation.dk/eli/lta/2026/763 |
| Fee for a provisional assessment when no report is filed | DKK 800 | 2026 | https://www.retsinformation.dk/eli/lta/2024/1040 |
| Late payment interest, Samlet Betaling, 1 January to 30 June 2026 (yearly) | 9.75% | 2026 | https://virk.dk/vejledning/atp/atp-arbejdsgiver/ |

The AES table gives eight of the 16 branch groups. Look up the employer's group in the AES PDF. Each figure is the AES contribution plus the work injury levy (arbejdsskadeafgift), and includes DKK 2 per full-time employee to cover the levy's costs (AES 2026 rates; virk.dk, AES).

## The taxable base

**AM-bidrag, employees.** The base is all pay in money or kind for personal work: salary, holiday pay, sick and maternity pay, fees, severance, taxable allowances and benefits in kind at taxable value (free car, board and lodging, phone, holiday home, shares, employer-paid health treatment) (AMBL § 2, stk. 1 and 2; skat.dk, AM-bidrag). Employer payments to a pension scheme are in the base (AMBL § 2, stk. 1, nr. 4). The pension company withholds AM-bidrag on those. The employer withholds AM-bidrag from salary after ATP and the employee's own pension contribution are taken off, and before A-skat (skat.dk, AM-bidrag).

**AM-bidrag, self-employed outside the business scheme.** The base is the personal income from the business (AMBL § 4, stk. 1). Pension contributions and premiums do not reduce it (§ 4, stk. 2). Negative personal income carried forward under Personskatteloven § 13 does reduce it, except the part that came from pension contributions (§ 4, stk. 3).

**AM-bidrag, self-employed in virksomhedsordningen.** The base is the amount transferred to the owner from the business profit, less the capital return, plus transfers from saved profit with the matching business tax, plus interest correction counted as personal income (AMBL § 5). The scheme mechanics are in dk-income-tax.

**AM-bidrag is deductible.** It comes off personal income before income tax (Personskatteloven § 3, stk. 2, nr. 6; Ligningsloven § 8 M; SKAT Juridisk Vejledning C.A.4.1.11).

**ATP.** A flat amount by hours band, not a percentage. If the hours are unknown, divide gross pay by the 2026 hourly rate (DKK 258.69 for men, DKK 233.62 for women) and use the band that gives (virk.dk, ATP rates). The employee share is withheld from pay. Both shares are reported in eIndkomst as one figure.

**Employer contributions.** Samlet Betaling converts reported ATP into full-time employees: ATP paid divided by DKK 891 a quarter (virk.dk, FIB). It then charges FIB, Barsel.dk and AUB per full-time employee. Barsel.dk is not charged for apprentices under 25 registered with AUB (virk.dk, Barsel.dk). AUB is not charged for the first employee or every 50th employee, so a business with one employee pays no AUB (virk.dk, AUB). AES is a yearly amount per full-time employee set by branch group, charged when ATP is paid and paid quarterly on the Samlet Betaling invoice (virk.dk, AES; AES 2026 rates).

**Work accident insurance premium.** Set by the insurer, not by statute. It is a business cost outside Samlet Betaling.

## Deadlines and filing

- **AM-bidrag and A-skat, small and medium employers.** Due on the 1st and payable by the 10th of the month after the pay month; for December pay the deadline is 17 January (Opkrævningsloven § 2, stk. 5, applying stk. 2, 3. pkt.). A deadline on a bank holiday moves to the next banking day (§ 2, stk. 3).
- **Large employers.** Where AM-bidrag over the 12 months from October two years before to September the year before (for 2026: October 2024 to September 2025) exceeded DKK 250,000, or A-skat exceeded DKK 1 million, AM-bidrag and A-skat are due on the last banking day of the month the pay relates to (Opkrævningsloven § 2, stk. 6). This does not apply to regions and municipalities. Skattestyrelsen recalculates each November and notifies changes through Virk (skat.dk, deadlines). The category is on the registration certificate in TastSelv Erhverv.
- **ATP and Samlet Betaling.** ATP is reported in eIndkomst. Samlet Betaling invoices four times a year: Q1 report by 31 May, pay by 1 July; Q2 report by 31 August, pay by 1 October; Q3 report by 30 November, pay by 1 January; Q4 report by 28 February, pay by 1 April (virk.dk, ATP employer). AUB, Barsel.dk, FIB and AES come on the same invoice.
- **Self-employed AM-bidrag.** Paid through B-skat on the preliminary assessment, in 10 instalments in every month except June and December, and settled on the annual return (skat.dk, B-income). Filing dates are in dk-income-tax.
- **Voluntary ATP, self-employed.** Quarterly: Q1 by 1 May, Q2 by 1 August, Q3 by 1 November, Q4 by 1 February (virk.dk, ATP self-employed).
- **Work accidents.** Report in EASY within 14 days of the first day of absence, or of the injury day if there was no absence (virk.dk, AES work accident).

## Penalties and interest

- **Late AM-bidrag or A-skat.** A-skat and AM-bidrag sit on the tax account (skattekonto), where the debit balance carries the Opkrævningsloven § 7, stk. 1 rate (§ 16 c, stk. 1): the § 7, stk. 2 base rate plus 0.85 percentage points a month, calculated daily, not deductible (§ 7, stk. 1 as amended by lov nr. 1694 of 30 December 2024, § 1, nr. 6; SKAT Juridisk Vejledning A.B.4.7.2). The 2026 base rate is 0.1% (SKM2025.720.SKTST), so 0.95% a month. From 1 January 2026 interest on interest on the tax account is abolished (A.B.4.7.2).
- **Reminder fee.** DKK 65 for each reminder up to 13 September 2026, and DKK 160 from 14 September 2026 (Opkrævningsloven § 6, stk. 1, as amended by lov nr. 763 of 8 September 2026, § 1, nr. 1, in force 14 September 2026 under § 8; skat.dk, Payments to your tax account). On the tax account a reminder goes out only when the debit balance exceeds DKK 5,000, and the whole balance is then payable at once (§ 16 c, stk. 4).
- **No report.** Skattestyrelsen can set the amount provisionally and charge DKK 800, one fee per period even where both A-skat and AM-bidrag are set (Opkrævningsloven § 4, stk. 1 and 2). After four provisional assessments in a row it can cancel the registration (§ 4, stk. 3).
- **Late Samlet Betaling.** Interest from the deadline at Nationalbanken's official lending rate plus 8 points a year, 9.75% for 1 January to 30 June 2026 (virk.dk, ATP employer).
- **No work accident insurance.** The employer pays AES an amount equal to the premium it should have paid (Arbejdsskadesikringsloven § 51) and is liable to a fine (§ 82, stk. 1). Failing to keep the insurance in force, to pay AES or to report an accident on time is also fined (§ 82, stk. 2 and 3).
- **Voluntary ATP, self-employed.** After two unpaid reminders, membership as self-employed ends (virk.dk, ATP self-employed).

## Cross-border points

- **One country's social security.** Under EU Regulation 883/2004 a worker is covered in one country. A person posted from Denmark can stay in Danish social security with an A1 for up to 24 months. A person living in Denmark who does 25% or more of their work in Denmark is covered here when working in several countries. Udbetaling Danmark, International Social Sikring, issues A1 certificates (lifeindenmark.borger.dk, social security cover).
- **AM-bidrag follows tax liability.** It is charged on people liable to Danish tax (AMBL § 1). A person fully liable to Danish tax who is socially insured in another country under the EU rules or a social security agreement can deduct the mandatory foreign social contributions from personal income (Ligningsloven § 8 M, stk. 2 and 3; SKAT Juridisk Vejledning C.A.4.1.11). Documentation is normally an A1.
- **Foreign employers.** A foreign employer with staff working in Denmark reports and pays ATP and pays FIB (virk.dk, ATP foreign business; virk.dk, FIB). Employees without a Danish address may need an administrative CPR number from Skattestyrelsen or ATP.
- **Employer pension schemes abroad.** Employer payments to a foreign pension scheme that are not taxable to the employee under a tax treaty are in the AM-bidrag base (AMBL § 2, stk. 1, nr. 5).

## Worked examples

### Example 1: three full-time employees, business services, one quarter

A Danish ApS in branch group 71 (finance and business services) has three monthly paid employees. Each works at least 117 hours a month, earns DKK 40,000 a month, is over 18 and has no pension scheme. We look at Q1 2026.

ATP is DKK 297 a month per employee: DKK 99 from the employee and DKK 198 from the employer. For the quarter Samlet Betaling sees ATP of 3 x 891 = DKK 2,673, which is 3 full-time employees. Barsel.dk is 3 x 550 = DKK 1,650. FIB is 3 x 82 = DKK 246. AUB is charged on 2 employees, because the first is deducted: 2 x 705.25 = DKK 1,410.50. The employer's own cost for the quarter is its ATP share of 3 x 198 x 3 = DKK 1,782 plus those charges: DKK 5,088.50. AES for group 71 comes on top: DKK 457 a year per full-time employee, DKK 1,371 a year for the three, paid through the quarterly invoices. Each employee's AM-bidrag is 8% of DKK 40,000 less the DKK 99 ATP share: DKK 3,192.08 a month.

```oa-check
name: Three full-time employees, group 71, Q1 2026
inputs:
  employees: 3
  months: 3
  monthly_pay: 40000
  atp_employee: 99
  atp_employer: 198
  atp_quarter_fte: 891
  barsel_quarter: 550
  fib_quarter: 82
  aub_quarter: 705.25
  aes_year: 457
  am_rate: 8
steps:
  - atp_total: employees * (atp_employee + atp_employer) * months
  - fte: atp_total / atp_quarter_fte
  - barsel: fte * barsel_quarter
  - fib: fte * fib_quarter
  - aub: (fte - 1) * aub_quarter
  - aes_annual: fte * aes_year
  - employer_atp: employees * atp_employer * months
  - employer_cost: employer_atp + barsel + fib + aub
  - am_monthly: round(pct(monthly_pay - atp_employee, am_rate), 2)
expected:
  atp_total: 2673
  fte: 3
  barsel: 1650
  fib: 246
  aub: 1410.50
  aes_annual: 1371
  employer_cost: 5088.50
  am_monthly: 3192.08
```

### Example 2: sole trader with a pension and a loss carried forward

A self-employed consultant, not in virksomhedsordningen, has 2026 business personal income of DKK 450,000. They pay DKK 60,000 into a private pension and carry forward DKK 30,000 of negative personal income from 2025, none of it from pension contributions. They pay voluntary ATP and are a full-time a-kasse member with efterløn.

The pension does not reduce the AM-bidrag base (AMBL § 4, stk. 2). The carried-forward loss does (§ 4, stk. 3). So the base is 450,000 - 30,000 = DKK 420,000 and AM-bidrag is 8% of that: DKK 33,600. Taking the pension off by mistake would give DKK 28,800, which is DKK 4,800 too little. Voluntary ATP is 297 x 12 = DKK 3,564. The state part of the a-kasse contribution is 407 x 12 = DKK 4,884, and efterløn adds 593 x 12 = DKK 7,116. The a-kasse's own fee comes on top and differs between a-kasser.

```oa-check
name: Sole trader, pension and loss carried forward, 2026
inputs:
  personal_income: 450000
  pension_paid: 60000
  loss_carried: 30000
  am_rate: 8
  atp_month: 297
  akasse_month: 407
  efterlon_month: 593
steps:
  - am_base: personal_income - loss_carried
  - am_bidrag: pct(am_base, am_rate)
  - am_wrong: pct(personal_income - loss_carried - pension_paid, am_rate)
  - understatement: am_bidrag - am_wrong
  - atp_year: atp_month * 12
  - akasse_year: akasse_month * 12
  - efterlon_year: efterlon_month * 12
expected:
  am_base: 420000
  am_bidrag: 33600
  am_wrong: 28800
  understatement: 4800
  atp_year: 3564
  akasse_year: 4884
  efterlon_year: 7116
```

## Ask the client first

1. Employee or self-employed? If self-employed, are you in virksomhedsordningen? That changes the AM-bidrag base (AMBL §§ 4 and 5).
2. For each employee: date of birth, pay frequency and hours a month. Age sets AM-bidrag from 2026 and the hours band sets ATP.
3. What is the business's branch code? It sets the AES group and rate.
4. Is the employer small or large on its SKAT registration certificate? That sets the AM-bidrag payment date.
5. Does anyone work in another country, or come from one, and is there an A1? That decides which country's contributions apply.
6. Self-employed: do you want voluntary ATP, AES or work accident cover, and are you in an a-kasse with efterløn?

## Sources

| Source | URL | Read on |
|---|---|---|
| Arbejdsmarkedsbidragsloven, LBK nr. 121 of 7 February 2020, §§ 1-5, 7, 9 | https://www.retsinformation.dk/eli/lta/2020/121 | 2026-10-23 |
| Lov nr. 96 of 4 February 2025, § 1 (new AMBL § 1, stk. 2: 0% to 31 December of the year the person turns 17) and § 7, stk. 4 (effect from 1 January 2026) | https://www.retsinformation.dk/eli/lta/2025/96 | 2026-10-23 |
| Personskatteloven, LBK nr. 1284 of 14 June 2021, § 3, stk. 2, nr. 6 | https://www.retsinformation.dk/eli/lta/2021/1284 | 2026-10-23 |
| Skattestyrelsen, AM-bidrag (8%, base, exempt income, 2026 age rule, order of deduction) | https://skat.dk/borger/am-bidrag | 2026-10-23 |
| Skattestyrelsen, B-income (B-skat instalments, 2026 age rule) | https://skat.dk/en-us/individuals/b-income | 2026-10-23 |
| SKAT Juridisk Vejledning C.A.4.1.11 (AM-bidrag deductible; foreign social contributions) | https://info.skat.dk/data.aspx?oid=2061784 | 2026-10-23 |
| Opkrævningsloven, LBK nr. 1040 of 13 September 2024, §§ 2, 4, 6, 7, 16 c | https://www.retsinformation.dk/eli/lta/2024/1040 | 2026-10-23 |
| Lov nr. 1694 of 30 December 2024, § 1, nr. 6 and 15 (0.85-point addition; no interest on interest on the tax account) | https://www.retsinformation.dk/eli/lta/2024/1694 | 2026-10-23 |
| SKAT Juridisk Vejledning A.B.4.7.2 (interest base plus 0.85 points; DKK 65 fee before 14 September 2026) | https://info.skat.dk/data.aspx?oid=2168585 | 2026-10-23 |
| Lov nr. 763 of 8 September 2026, § 1, nr. 1 (Opkrævningsloven § 6 reminder fee DKK 65 to DKK 160) and § 8 (in force 14 September 2026) | https://www.retsinformation.dk/eli/lta/2026/763 | 2026-10-23 |
| Skattestyrelsen, Payments to your tax account (reminder fee DKK 160 from 14 September 2026) | https://skat.dk/en-us/businesses/payment-and-the-tax-account-skattekontoen/payments-to-your-tax-account | 2026-10-23 |
| SKM2025.720.SKTST, Opkrævningsloven § 7, stk. 2 rate for 2026 (0.1%) | https://info.skat.dk/data.aspx?oid=2459995 | 2026-10-23 |
| Skattestyrelsen, deadlines for A-skat and AM-bidrag | https://skat.dk/erhverv/ansatte-og-loen/frister-ansatte-og-loen | 2026-10-23 |
| borger.dk, ATP rates for 2026, private employers | https://www.borger.dk/pension-og-efterloen/atp-livslang-pension-oversigt/atp-bidraget/atp-satser-for-privat-virksomhed | 2026-10-23 |
| virk.dk, ATP rates (14-day, weekly, casual, 2026 hourly rates) | https://virk.dk/vejledning/atp/atp-arbejdsgiver/atp-satser/ | 2026-10-23 |
| virk.dk, ATP employer (who, split, quarters, interest) | https://virk.dk/vejledning/atp/atp-arbejdsgiver/ | 2026-10-23 |
| virk.dk, ATP self-employed | https://virk.dk/vejledning/atp/atp-selvstaendig | 2026-10-23 |
| virk.dk, ATP foreign business | https://virk.dk/vejledning/atp/atp-udenlandsk-virksomhed/ | 2026-10-23 |
| virk.dk, Samlet Betaling contribution rates 2017-2026 | https://businessindenmark.virk.dk/guidance/samlet-betaling-bid/sb-employer/samlet-betaling-bid-contribution-rates | 2026-10-23 |
| virk.dk, AUB employer | https://virk.dk/vejledning/aub/aub-arbejdsgiver/ | 2026-10-23 |
| virk.dk, Barsel.dk fully covered employers | https://virk.dk/vejledning/barsel-dk/bdk-privat-arbejdsgiver/fuldt-omfattet/ | 2026-10-23 |
| virk.dk, Finansieringsbidrag (FIB) | https://businessindenmark.virk.dk/guidance/fib-bid-finansieringsbidrag/fib-bid-finansieringsbidrag | 2026-10-23 |
| virk.dk, AES contribution | https://virk.dk/vejledning/aes/aes-bidrag | 2026-10-23 |
| AES rates 2026 (PDF) | https://virk.dk/assets/6feKOXUjVtAaPklFxxBz9C/aes_bidragssatser_2026.pdf | 2026-10-23 |
| virk.dk, AES work accident | https://virk.dk/vejledning/aes/aes-arbejdsulykke/ | 2026-10-23 |
| Arbejdsskadesikringsloven, LBK nr. 667 of 8 July 2026, §§ 48, 50, 51, 82 | https://www.retsinformation.dk/eli/lta/2026/667 | 2026-10-23 |
| Beskæftigelsesministeriet, VEJ nr. 10230 of 9 December 2025, rates for unemployment insurance 2026 (table 4.1) | https://www.retsinformation.dk/eli/retsinfo/2025/10230 | 2026-10-23 |
| lifeindenmark.borger.dk, social security cover when working abroad | https://lifeindenmark.borger.dk/working/social-security-cover | 2026-10-23 |

Not yet confirmed: whether an A1 from another country removes Danish AM-bidrag, rather than only giving a deduction for foreign contributions, was not settled from an official source. Whether Samlet Betaling charges exactly a quarter of the yearly AES amount each quarter on the ATP-based full-time count was not stated on the pages read, so Example 1 shows AES as a yearly figure. How AUB counts "every 50th employee" when the full-time count is a fraction was not read. The SMV payment date rests on Opkrævningsloven § 2, stk. 5 as consolidated in 2024; skat.dk does not publish the 2026 SMV table on the page read. The Samlet Betaling late interest rate from 1 July 2026 was not published on the page read. The commencement order for the 0.85-point addition under lov nr. 1694/2024, § 18, stk. 2 was not located; Den juridiske vejledning 2026-2 applies it. The monthly a-kasse admin fee charged by each a-kasse and work accident insurance premiums were not read.

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
