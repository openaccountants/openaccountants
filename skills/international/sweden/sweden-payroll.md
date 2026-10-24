---
name: sweden-payroll
description: "Use for running Swedish payroll in 2026: preliminary tax withheld from pay (preliminärskatt) under the 2026 tax tables (skattetabeller), the 30% rate, jämkning and SINK decisions; employer contributions (arbetsgivaravgifter) of 31.42%, 10.21% from age 67, the youth reduction for those born 2003-2007 from 1 April 2026 (20.81% up to SEK 25,000 a month) and the växa refund for a first or second employee; taxable benefits (förmåner) in the base; the monthly employer return (arbetsgivardeklaration, AGI) and payment by the 12th (17th in January and August; 26th filing for large VAT payers); late-filing fees, tax surcharges and cost interest. Trigger on: Swedish payroll, preliminärskatt, skattetabell, arbetsgivaravgifter, AGI, arbetsgivardeklaration, net salary Sweden, växa-stöd, semesterlön, sjuklön. Out of scope: se-employee-income-tax (the employee's annual return), se-social-contributions (egenavgifter), se-income-tax (sole traders), se-benefits-and-allowances (benefit valuation), se-cross-border (residence, SINK and expert relief)."
version: 1.1
jurisdiction: SE
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Sweden payroll and PAYE

This skill runs one month of Swedish payroll for 2026: what to withhold from the employee, what the employer pays on top, and how both are reported and paid. The employee's own annual return, the job tax credit formula and the state tax computation are in [se-employee-income-tax](se-employee-income-tax.md). Self-employed contributions are in [se-social-contributions](se-social-contributions.md) and sole-trader income tax in [se-income-tax](se-income-tax.md). How to value a car, meal or housing benefit is in [se-benefits-and-allowances](se-benefits-and-allowances.md). Residence, SINK status and the expert relief are in [se-cross-border](se-cross-border.md).

## Who this applies to

- Anyone who pays cash pay for work (ersättning för arbete) must withhold preliminary tax from it (SFL 10 kap. 3 §) and pay employer contributions on it (SAL 2 kap. 1 and 4 §§). This covers Swedish companies, sole traders with staff, and foreign employers paying for work done in Sweden.
- Pay for work includes salary, fees, holiday pay, sick pay paid by the employer, and taxable benefits. Pensions are also pay for withholding purposes (SFL 10 kap. 3 § andra stycket 1).
- An employer registers before the first payment and then files a return for every month while registered. If a month has nothing to report, file a zero return in the e-service.
- No withholding and no employer contributions when the payer expects to pay the person less than SEK 1,000 in the calendar year (SFL 10 kap. 4 § 2; SAL 2 kap. 14 §). No withholding on a single payment under SEK 100 (SFL 10 kap. 4 § 1).
- A private individual who pays for work that is not a business expense does not withhold if the year's total to that person is expected to be under SEK 10,000 and the other conditions in SFL 10 kap. 4 § 3 are met. Treat the employer-contribution side as a separate question.
- Payments to a person approved for F-tax (F-skatt) carry no withholding and no employer contributions; the payee pays their own (SFL 10 kap. 11 §; SAL 2 kap. 5 §). That is in [se-social-contributions](se-social-contributions.md).
- Out of scope here: collective-agreement pay rules, pension plan design, share options, and the employee's final tax.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Employer contributions, full rate (born 1959 or later) | 31.42% of pay and benefits: 18.80% social contributions (SAL 2 kap. 26 §) plus 12.62% general payroll fee (allmän löneavgift, Lag 1994:1920 3 §) | 2026 | https://data.riksdagen.se/dokument/sfs-2000-980.text ; https://data.riksdagen.se/dokument/sfs-1994-1920.text |
| Parts of the 18.80% | Health 3.55%, parental 2.00%, old-age pension 10.21%, survivor's pension 0.30%, labour market 2.64%, work injury 0.10% | 2026 | SAL 2 kap. 26 § (Lag 2025:1362) |
| Age 67 or over at 1 January 2026 (born 1938-1958) | 10.21% (old-age pension contribution only; no general payroll fee) | 2026 | SAL 2 kap. 27 § (Lag 2022:889, in force 1 January 2026); Lag 1994:1920 1 § |
| Born 1937 or earlier | 0% | 2026 | SAL transitional rules to Lag 2000:980, point 5; https://www.skatteverket.se/arbetsgivaravgifter |
| Youth reduction, aged 18 but not 23 at 1 January 2026 (born 2003-2007), pay from 1 April 2026 to 30 September 2027 | 20.81% on pay up to SEK 25,000 per calendar month (full old-age pension contribution plus half of the rest, truncated to two decimals); 31.42% on the excess | 2026 | Lag (2026:100) 2 § and transitional rules; https://data.riksdagen.se/dokument/sfs-2026-100.text |
| Employer with no permanent establishment in Sweden | 18.80% (born 1959 or later); 10.21% (born 1938-1958); 14.50% (born 2003-2007, from 1 April 2026). No general payroll fee: it is a tax, and a foreign employer without a PE does not pay it (Skatteverket legal guidance, citing prop. 1994/95:122 p. 18) | 2026 | https://www.skatteverket.se/arbetsgivaravgifter ; https://www4.skatteverket.se/rattsligvagledning/1333.html |
| Växa refund (first and second employee of a sole trader in active business, an aktiebolag, or a handelsbolag with at most two partners) | Refund of the contributions and general payroll fee paid, except the 10.21% old-age pension part, on pay up to SEK 35,000 a month, for the first 24 months of the employment; employment of at least three months and at least 20 hours a week; SEK 25,000 cap for someone hired before 1 May 2024 under the old växa rules; within EU de minimis limits; apply per month within one year | 2026 | Lag (2025:1334) 7-8, 13 §§ and transitional rule 3; https://data.riksdagen.se/dokument/sfs-2025-1334.text |
| Annual threshold for contributions and withholding | Pay under SEK 1,000 to one person in the year | 2026 | SAL 2 kap. 14 §; SFL 10 kap. 4 § 2 |
| Withholding on main income | Tax table number on the A-tax decision, column by age and income type | 2026 | SFL 11 kap. 16-17 §§; SKVFS 2025:20 tables |
| 30% withholding | Pay that is not main income; work meant to last less than a week; pay from a foreign employer with no PE in Sweden | 2026 | SFL 11 kap. 20 § |
| Withholding with no A-tax or SINK decision shown | Table for the employer's municipality plus 10% of the table amount | 2026 | SFL 11 kap. 21 § |
| One-off payments, column 1 | Estimated annual pay (leaving out the one-off amount) up to SEK 25,041: 0%; 25,042-82,800: 10%; 82,801-192,000: 21%; 192,001-477,600: 26%; 477,601-660,000: 34%; over 660,000: 54% | 2026 | SFL 12 kap. 6 §; https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/skatteavdrag/engangsbelopp.4.361dc8c15312eff6fd3225e.html ; https://www4.skatteverket.se/rattsligvagledning/325047.html |
| State tax threshold (skiktgräns) | 20% on taxable earned income above SEK 643,000 | 2026 | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html |
| Breakpoint (brytpunkt), before basic deduction | SEK 660,400 a year if under 66 at 1 January; SEK 760,500 if 66 or over | 2026 | same page |
| Price base amount (prisbasbelopp) | SEK 59,200 (higher amount SEK 60,500) | 2026 | same page |
| Income base amount (inkomstbasbelopp) | SEK 83,400 | 2026 | same page |
| Student certificate (SKV 434) limit | Expected 2026 pay under SEK 25,042 and living in Sweden all year | 2026 | https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html |
| SINK withholding (non-resident under a SINK decision) | 22.5% (20% from 1 January 2027) | 2026 | Lag (1991:586) 7 §; https://data.riksdagen.se/dokument/sfs-1991-586.text |
| Special payroll tax on pension costs | 24.26% | 2026 | Lag (1991:687) 1 §; https://data.riksdagen.se/dokument/sfs-1991-687.text |
| Late-filing fee, employer return | SEK 625; SEK 1,250 if filed after an order | 2026 | SFL 48 kap. 6 § |
| Tax surcharge (skattetillägg) | 20% of tax that would have been lost; 5% of tax not withheld; 2% or 5% for a timing error | 2026 | SFL 49 kap. 11, 13, 18 §§ |
| Cost interest (kostnadsränta) | Base rate 2.5% (since 1 December 2024); late payment: base rate plus 15 points = 17.5% | 2026 | SFL 65 kap. 3-4, 13 §§; https://www.skatteverket.se/rantapaskattekontot |

## The taxable base

**Contribution base.** Cash gross pay plus the value of taxable benefits. Value benefits under IL 61 kap. 2-17 §§ (SFL 11 kap. 9 §); the methods are in [se-benefits-and-allowances](se-benefits-and-allowances.md). Reduce a benefit by what the employee paid for it out of net pay. A fuel benefit is the exception in the return: report the full marked-up value in box 018 and the employee's payment in box 098.

**The SEK 1,000 gate.** Track each A-tax payee's pay for the whole year. If the year's total is expected to stay under SEK 1,000, report the pay in box 131 and enter 0 in box 001. If a later payment takes the year to SEK 1,000 or more, contributions are due on the whole year's pay. Report the full amount in box 011 in the month you find this and enter the amount earlier reported as not contribution-liable in box 010. Do not reopen the earlier month. Withhold tax on the later payment under the normal rules. Example: SEK 500 in May, SEK 1,000 in November, born 1990: contributions are 1,500 × 31.42% = SEK 471.30, all in November.

**Withholding base.** Cash pay plus taxable benefits (SFL 11 kap. 4 §). If no cash is paid, no tax can be withheld from a benefit; flag it before closing the month.

**Choosing the withholding method.**

1. Main income: use the table number on the employee's A-tax decision (A-skattsedel). In January you may still use last year's table (SFL 11 kap. 16 §). The table number is the employee's total rate (municipal tax, regional tax and burial fee, plus the Church of Sweden fee for members) rounded to a whole number: 32.50 gives table 32, 32.51 gives table 33.
2. Column 1 is for pay to someone under 66 at 1 January 2026 whose pay earns the job tax credit (jobbskatteavdrag). Column 3 is for pay to someone 66 or over (born 1959 or earlier). Columns 2, 4, 5 and 6 cover pensions, sickness compensation and other benefits. The tables already build in municipal and regional tax, state tax, the burial fee and any registered faith community fee, the public service fee, the basic deduction, the pension contribution and its credit, the job tax credit and the earned income credit (SFL 12 kap. 3 §). The job tax credit formula (IL 67 kap. 7 §) is in [se-employee-income-tax](se-employee-income-tax.md).
3. 30% instead of the table (SFL 11 kap. 16 and 20 §§) when the pay is not main income (a second job), when the work is meant to last less than a week, and when the employer is foreign with no PE in Sweden.
4. A jämkning decision or a SINK decision overrides the table. Follow a new decision no later than two weeks after receiving it (SFL 11 kap. 27 §). Report SINK tax in box 274, not box 001.
5. Main income, no decision shown after you asked for one, and you have not got the information from Skatteverket (for example through its API): table for the municipality of your office plus 10% of the table amount (SFL 11 kap. 21 §). When the decision arrives, use it from then on. Do not correct earlier months.
6. The employee may ask you to withhold more. Start no later than the first pay day two weeks after the request (SFL 11 kap. 22 §).

**One-off payments.** A bonus, back pay, holiday compensation, severance or commission that is not regular pay uses the one-off table (engångstabell) for the column, by the employee's estimated annual pay from you. Leave the one-off amount out of that estimate (Skatteverket legal guidance, Skattetabeller). If paid with regular pay, withhold on each part separately. With no regular time-based pay, withhold 30% on the one-off amount. On termination, final regular pay and one-off amounts paid that month, plus a final settlement paid by the next month, count as main income; use the ordinary table for the last regular pay and the one-off table for the rest.

**Advances.** Withhold the same share of the tax as the advance is of the total pay. If the total is not known, treat the advance as the whole pay for the period (SFL 11 kap. 23 §).

**Students.** A school or university student who will earn under SEK 25,042 in 2026 and lives in Sweden all year can give you form SKV 434. You then withhold nothing and enter 0 in box 001. Employer contributions are still due.

**Over- or under-withholding.** If you find before filing that you withheld too much, repay the employee. If you withheld too little, you can be made to pay the shortfall.

**Holiday pay (Semesterlag 1977:480).** Check the collective agreement first; it can replace the statutory method. Each employee is entitled to 25 holiday days a year (4 §); how many are paid depends on days earned. Same-pay rule (16 a §): keep paying monthly or weekly salary and add 0.43% of monthly pay (1.82% of weekly pay) per paid day, after adding fixed supplements. Variable pay gives 12% of the variable pay due in the holiday year. Percentage rule (16 b §): 12% of the earning-year pay. Unused paid days are paid out on termination, normally within one month.

**Sick pay (Lag 1991:1047).** The employer pays for the first day of illness and the next 13 calendar days (6-7 §§): 80% of lost pay and benefits, less a qualifying deduction of 20% of an average week's sick pay. No new deduction after ten in 12 months, or when a new sick period starts within five days of the last one. From the seventh calendar day after the sick report, the employer need only pay if the employee gives a doctor's or dentist's certificate (8 §). For a contract shorter than one month, the right starts after 14 days in a row of employment (3 §).

**Pension costs.** Employer pension costs carry special payroll tax of 24.26%. It is declared in the employer's income tax return, not in the monthly return.

**Reconcile.** Bank pay = cash gross + cash expense refunds − tax withheld − agreed net deductions. Benefits raise the bases but are not paid in cash. Tie each person's figures to the payroll ledger, the return and the tax account.

## Deadlines and filing

- **Return.** One employer return (arbetsgivardeklaration, AGI) per calendar month, with a statement for each payee (SFL 26 kap. 3 §). File in the e-service or as a checked file.
- **Due dates, most employers (VAT base up to SEK 40 million, or no VAT):** the 12th of the next month; the July return is due 17 August and the December return 17 January (SFL 26 kap. 26 and 32 §§).
- **Large VAT payers (VAT base over SEK 40 million):** return due the 26th of the next month; the November return 27 December, the December return 26 January (SFL 26 kap. 30 §). Payment of withheld tax and employer contributions is still due on the 12th of the next month, 17th in January (SFL 62 kap. 3 §). Use the VAT test, not the size of the payroll.
- **Payment.** Withheld tax and contributions must be on the tax account by the due date. A payment counts when it is booked to the account (SFL 62 kap. 2-3 §§).
- **Payee statement.** Use a unique, non-zero specification number for each payee and keep it; a correction must reuse it. Cash salary in box 011, benefits in their own boxes (012 other benefits, 013 car, 018 fuel), tax in exactly one tax box (001, or 274 for SINK). Tick box 302 if the employer has no permanent establishment in Sweden.
- **Absence details.** Since the January 2025 period, report absence that may qualify for parental benefit (boxes 821-827) with the same return and tell the employee. These details cannot be added or corrected later.
- **Tell the employee** what you reported, for example on the payslip, by the filing date.
- **Corrections.** File a new return for the affected month, reusing the specification number. You can correct up to six years back (2020 onward in 2026). Contributions can go up or down; withheld tax can be increased but normally not reduced.
- **Växa refund.** File the return with the contributions due, then apply for the refund month by month, electronically, within one year after the month ends (Lag 2025:1334 13-14 §§).
- **Växa and the youth reduction together.** Both apply to the same pay. The växa law bars only employers that used the old växa rules (Lag 2016:1053) or Lag 2021:423 elsewhere (10 §), and it refunds the fees actually reported other than the old-age pension part (8 §). On pay up to SEK 25,000 to an employee born 2003-2007 you report 20.81% and get back 10.60%, so the net cost is 10.21%, the same as with växa alone.

## Penalties and interest

- **Late return:** SEK 625 per filing date, even if several returns are late at once; SEK 1,250 if filed after an order (SFL 48 kap. 5-6 §§).
- **Wrong information:** 20% of the tax that would have been lost (SFL 49 kap. 11 §). If the error only puts an amount in the wrong month: 2% when the period is at most three months and the amount sits within four months of the right period, otherwise 5% (49 kap. 13 §).
- **Tax not withheld:** surcharge of 5% of the tax that should have been withheld (49 kap. 18 §), and the employer can be made liable for the tax.
- **No surcharge** if you correct on your own initiative. A correction does not count as your own initiative if Skatteverket announced a general check, the correction is linked to it, and you make it two months or more after the end of the month of the announcement (49 kap. 10 §).
- **Cost interest:** charged daily on a deficit on the tax account at the base rate (2.5% since 1 December 2024, floor 1.25%). On tax not paid by the due date the rate is base rate plus 15 points, now 17.5%, until the debt goes to the Enforcement Authority (SFL 65 kap. 3-4, 13 §§). It is not deductible.

## Cross-border points

- **Foreign employer, work in Sweden.** Withhold only for work done in Sweden if the employer has no permanent establishment here (SFL 10 kap. 6 §), at 30% unless the employee shows a jämkning or SINK decision (SFL 11 kap. 20 § 4). Without a Swedish PE, use the no-PE rates in the table and tick box 302; no general payroll fee is due.
- **A1 or certificate of coverage.** If a valid certificate names the employee and covers the pay month, no Swedish contributions are due on that pay. Report it in box 131. Check the person, the issuing body and the dates. Withholding is a separate question.
- **Social security agreement (socialavgiftsavtal).** A foreign employer with no PE can agree that the employee pays the contributions. The employer still registers, withholds 30% on pay for work in Sweden (unless the employee has another decision) and files monthly.
- **Postings to and from treaty countries** (USA, Canada, India, Japan, South Korea, Québec, the Philippines) have their own codes and reduced rates on Skatteverket's rate table.
- **Third-country nationals.** Notify Skatteverket by the end of the third month after the month the employment started.
- **Non-residents on SINK** pay 22.5% in 2026; residence tests and the expert relief are in [se-cross-border](se-cross-border.md).

## Worked examples

### Example 1: ordinary monthly salary

Lina is born 1990 and lives in a municipality whose A-tax decision gives table 32. She earns SEK 40,000 a month, paid in May 2026, with no benefits. The employer is a small company that files VAT quarterly.

- Withholding: table 32, column 1, row 39,801-40,000 = SEK 8,151.
- Net pay: 40,000 − 8,151 = SEK 31,849.
- Employer contributions: 40,000 × 31.42% = SEK 12,568.
- Due to Skatteverket by 12 June 2026: 8,151 + 12,568 = SEK 20,719. The May return is due the same day.

```oa-check
name: Monthly salary SEK 40,000, table 32 column 1, May 2026
inputs:
  salary: 40000
  table_tax: 8151
  contribution_rate: 0.3142
steps:
  - contributions: salary * contribution_rate
  - net_pay: salary - table_tax
  - employer_cost: salary + contributions
  - due_to_skatteverket: table_tax + contributions
expected:
  contributions: 12568.00
  net_pay: 31849.00
  employer_cost: 52568.00
  due_to_skatteverket: 20719.00
```

### Example 2: young employee with a bonus, after 1 April 2026

Emil is born in 2005, so at 1 January 2026 he is over 18 and under 23 and inside the youth reduction. His A-tax decision gives table 32. In June 2026 he is paid his regular SEK 28,000 salary plus a one-off bonus of SEK 10,000. His estimated annual pay from this employer, leaving out the bonus, is SEK 336,000, which falls in the 26% one-off band.

- Withholding on salary: table 32, column 1, row 27,801-28,000 = SEK 5,215.
- Withholding on the bonus: one-off table, column 1, 26% × 10,000 = SEK 2,600.
- Net pay: 38,000 − 5,215 − 2,600 = SEK 30,185.
- Contribution base for the month: SEK 38,000. The youth rate covers the first SEK 25,000: 25,000 × 20.81% = SEK 5,202.50. The rest at the full rate: 13,000 × 31.42% = SEK 4,084.60. Total SEK 9,287.10.
- Due by 12 July 2026: 5,215 + 2,600 + 9,287.10 = SEK 17,102.10.

```oa-check
name: Youth employee, salary SEK 28,000 plus SEK 10,000 bonus, June 2026
inputs:
  salary: 28000
  bonus: 10000
  table_tax: 5215
  youth_cap: 25000
  youth_rate: 0.2081
  full_rate: 0.3142
  one_off_rate: 0.26
steps:
  - bonus_tax: bonus * one_off_rate
  - total_tax: table_tax + bonus_tax
  - gross: salary + bonus
  - net_pay: gross - total_tax
  - youth_part: min(gross, youth_cap) * youth_rate
  - full_part: max(gross - youth_cap, 0) * full_rate
  - contributions: youth_part + full_part
  - due_to_skatteverket: total_tax + contributions
expected:
  bonus_tax: 2600.00
  net_pay: 30185.00
  youth_part: 5202.50
  full_part: 4084.60
  contributions: 9287.10
  due_to_skatteverket: 17102.10
```

## Ask the client first

1. Each employee's year of birth, and the table number, column and any jämkning or SINK decision on their A-tax decision.
2. Is this pay their main income from you, or a second job?
3. Does the company have a permanent establishment in Sweden, and does anyone hold an A1 or certificate of coverage?
4. Is the company's VAT base expected to exceed SEK 40 million this year?
5. Is this the first or second person the business has employed since 1 January 2024 (växa refund)?
6. Any benefits, bonuses, back pay or termination payments this month, and does a collective agreement set holiday or sick pay?

## Sources

| Source | URL | Read on |
|---|---|---|
| Socialavgiftslag (2000:980), as amended to SFS 2026:493: 2 kap. 1, 4, 14, 26-27 §§; transitional rules 2000:981 point 5, 2022:889 | https://data.riksdagen.se/dokument/sfs-2000-980.text | 2026-10-24 |
| Lag (1994:1920) om allmän löneavgift, 1 and 3 §§ (as amended by 2025:1360) | https://data.riksdagen.se/dokument/sfs-1994-1920.text | 2026-10-24 |
| Lag (2026:100) om särskild beräkning av arbetsgivaravgifter och allmän löneavgift för personer som vid årets ingång fyllt 18 men inte 23 år | https://data.riksdagen.se/dokument/sfs-2026-100.text | 2026-10-24 |
| Lag (2025:1334) om återbetalning av vissa avgifter till växa-företag, 1-14 §§ and transitional rules | https://data.riksdagen.se/dokument/sfs-2025-1334.text | 2026-10-24 |
| Skatteförfarandelag (2011:1244), as amended to SFS 2026:1305: 10 kap. 3-6 §§; 11 kap. 2-4, 9, 16-23, 27 §§; 12 kap. 3, 6 §§; 26 kap. 3, 26, 30-32 §§; 48 kap. 5-6 §§; 49 kap. 10-11, 13, 18 §§; 62 kap. 2-3 §§; 65 kap. 3-4, 13 §§ | https://data.riksdagen.se/dokument/sfs-2011-1244.text | 2026-10-24 |
| Lag (1991:586) om särskild inkomstskatt för utomlands bosatta, 7 § | https://data.riksdagen.se/dokument/sfs-1991-586.text | 2026-10-24 |
| Lag (1991:687) om särskild löneskatt på pensionskostnader, 1 § | https://data.riksdagen.se/dokument/sfs-1991-687.text | 2026-10-24 |
| Semesterlag (1977:480), 4, 16 a, 16 b §§ | https://data.riksdagen.se/dokument/sfs-1977-480.text | 2026-10-24 |
| Lag (1991:1047) om sjuklön, 3, 6-8 §§ | https://data.riksdagen.se/dokument/sfs-1991-1047.text | 2026-10-24 |
| Skatteverket, arbetsgivaravgifter (rates and codes 2026) | https://www.skatteverket.se/arbetsgivaravgifter | 2026-10-24 |
| Skatteverket, employer contributions (English) | https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html | 2026-10-24 |
| Skatteverket, skattetabeller 2026 and monthly table 32 (SKVFS 2025:20) | https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/skattetabeller.4.96cca41179bad4b1aa8a46.html | 2026-10-24 |
| Skatteverket, så läser du skattetabellen (columns 2026) | https://www.skatteverket.se/privat/skatter/arbeteochinkomst/askattsedelochskattetabeller/salaserdutabellen.4.319dc1451507f2f99e875f.html | 2026-10-24 |
| Skatteverket, engångsbelopp (one-off tables 2026) | https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/skatteavdrag/engangsbelopp.4.361dc8c15312eff6fd3225e.html | 2026-10-24 |
| Skatteverket, belopp och procent inkomstår 2026 | https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html | 2026-10-24 |
| Skatteverket, deducted tax | https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/deductedtax.4.2fb39afe18dabf1e4d255d0.html | 2026-10-24 |
| Skatteverket, PAYE return box by box | https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/howtofillinthepayetaxreturnboxbybox.4.309a41aa1672ad0c8379f84.html | 2026-10-24 |
| Skatteverket, filing a PAYE return (absence details) | https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn.4.2cf1b5cd163796a5c8b107cd.html | 2026-10-24 |
| Skatteverket, correcting a PAYE return | https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/correctingapayereturn.4.13948c0e18e810bfa0c2e34.html | 2026-10-24 |
| Skatteverket, hiring workers from abroad | https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/hiringworkersfromabroad.4.6532ae7518aff8c118f984.html | 2026-10-24 |
| Skatteverket, social security agreement for employers | https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/socialsecurityagreementforyouasanemployer.4.2fb39afe18dabf1e4d21c41.html | 2026-10-24 |
| Skatteverket, ränta på skattekontot | https://www.skatteverket.se/rantapaskattekontot | 2026-10-24 |
| Skatteverket, rättslig vägledning: Arbetsgivaravgifternas storlek (2026) | https://www4.skatteverket.se/rattsligvagledning/1333.html | 2026-10-24 |
| Skatteverket, rättslig vägledning: Skattetabeller (one-off amounts) | https://www4.skatteverket.se/rattsligvagledning/325047.html | 2026-10-24 |

Not yet confirmed: nothing open. Settled on review: the no-PE rate basis (Skatteverket legal guidance 1333), the one-off annual-pay rule (legal guidance 325047), the table-number rounding (Skatteverket, skattetabeller) and how växa and the youth reduction combine (Lag 2025:1334 8 and 10 §§).

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
