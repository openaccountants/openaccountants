---
name: cz-employee-contributions
description: "Czech social security and public health insurance contributions on employment income for tax year 2026. Covers the employee social rate of 7.1% (6.5% pension, 0.6% sickness) and the employer rate of 24.8%, health insurance of 13.5% split one third employee (4.5%) and two thirds employer (9%), the 2026 annual cap on the social base of CZK 2,350,416 (48 times the average wage), the health minimum base of CZK 22,400, the CZK 4,500 small-scope threshold and the CZK 12,000 threshold for work agreements (DPP), employer discounts, monthly payment by the 20th, the new single monthly employer report (JMHZ), penalties and EU posting rules. Trigger on: Czech payroll contributions, sociální pojištění zaměstnance, zdravotní pojištění zaměstnavatel, DPP, DPČ, JMHZ, maximální vyměřovací základ. Out of scope: self-employed contributions (cz-social-health), income tax withholding, residence and treaties (cz-cross-border)."
jurisdiction: CZ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Czech Republic: employee and employer social and health contributions (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure below comes from the Czech Social Security Administration (ČSSZ), the General Health Insurance Company (VZP), the Czech National Bank and the statutes in the Collection of Laws (e-Sbírka), read on 23 October 2026. It prepares working papers; it is not authority to file or pay.

This skill covers contributions on employment income. Related skills in this pack:

- Self-employed (OSVČ) social and health insurance: [cz-social-health](cz-social-health.md).
- Residence, non-residents and treaties: [cz-cross-border](cz-cross-border.md).
- Income tax for the self-employed: [cz-income-tax](cz-income-tax.md). Overview: [cz-tax-overview](cz-tax-overview.md).

The law is Act No. 589/1992 Coll. on social security premiums (zákon o pojistném na sociální zabezpečení, "SSPA"), Act No. 187/2006 Coll. on sickness insurance ("SIA"), Act No. 592/1992 Coll. on public health insurance premiums ("HIPA"), Act No. 48/1997 Coll. on public health insurance ("PHIA") and, from 1 January 2026, Act No. 323/2025 Coll. on the single monthly employer report ("JMHZ Act"). Social insurance goes to ČSSZ and its district offices. Health insurance goes to the health insurer the employee has chosen (VZP or another insurer). Currency: Czech koruna (CZK).

## Who this applies to

**Employees.** Social insurance (sickness, pension and the state employment policy contribution) applies to employees who work in the Czech Republic and meet the earnings threshold (SIA § 6(1)). The SIA list of employees is wide (SIA § 5(a)). It covers people in an employment contract (pracovní poměr), on an agreement to complete a job (DPP) or an agreement to perform work (DPČ). It also covers partners and managing directors (jednatelé) of an s.r.o. who work for it outside an employment contract, members of company bodies, liquidators and holders of a commercial power of attorney (prokura).

**Earnings thresholds.**

- **Employment contract and DPČ.** The employee is insured in a month if the agreed monthly earnings are at least CZK 4,500 (SIA § 6(1)(b) and (2)). Below that, the job is small-scope employment (zaměstnání malého rozsahu). The employee is then insured only in months where the earnings actually reach CZK 4,500. Several small-scope jobs with the same employer are added together (SIA § 7).
- **DPP.** The employee is insured only in months where earnings from all DPPs with the same employer reach CZK 12,000 (SIA § 7a; MPSV Communication 396/2025 Coll.). Each employer is tested separately.

**Health insurance** applies to anyone with employment income under ITA § 6 (PHIA § 5(a)). The exceptions follow the same thresholds: a DPP below CZK 12,000 a month with one employer, and a DPČ below CZK 4,500, carry no health insurance (PHIA § 5(a) points 3 and 6). An employment contract carries health insurance at any level of earnings, and the minimum base applies (see The taxable base).

**Employers.** Every person employing at least one employee is an employer. This includes an employer whose only staff are uninsured DPP workers. From 1 January 2026, every employer files the single monthly report (JMH) (ČSSZ, Kdo podává JMH).

**Out of scope here:** the self-employed ([cz-social-health](cz-social-health.md)), and income tax withheld from wages.

## Rates, bands and thresholds

| Item | 2026 figure | Year | Source |
|---|---|---|---|
| Employee social insurance | 7.1% of the base (6.5% pension, 0.6% sickness) | 2026 | [ČSSZ, Sazby pojistného](https://www.cssz.gov.cz/web/cz/vyse-a-sazba); SSPA § 7(1)(d) |
| Employer social insurance, ordinary employees | 24.8% of the base (21.5% pension, 2.1% sickness, 1.2% state employment policy) | 2026 | ČSSZ, Sazby pojistného; SSPA § 7(1)(a) |
| Employer rate for paramedics and company fire brigade members | 29.8% | 2026 | SSPA § 7(1)(b)(4) |
| Employer rate for staff in risk jobs (rizikové zaměstnání) | 27.8% (28.8% in 2027, 29.8% from 2028) | 2026 | SSPA § 7(1)(c)(2) |
| Health insurance, total | 13.5% of the base | 2026 | [VZP, Vyměřovací základ a výpočet pojistného](https://www.vzp.cz/platci/informace/zamestnavatel/vymerovaci-zaklad-a-vypocet-pojistneho); HIPA § 2(1) |
| Health insurance split | One third employee (4.5% of the base), two thirds employer (9%) | 2026 | PHIA § 9(2); [VZP, Splatnost](https://www.vzp.cz/platci/informace/zamestnavatel/splatnost-a-dalsi-zasady-pro-platbu-pojistneho) |
| Average wage for 2026 | CZK 48,967 | 2026 | derived: CZK 2,350,416 divided by 48 ([ČSSZ](https://www.cssz.gov.cz/web/cz/maximalni-vymerovaci-zaklad)); ČSSZ also gives half (CZK 24,484) and a quarter (CZK 12,242) ([ČSSZ, Výpočet pojistného](https://www.cssz.gov.cz/web/cz/vypocet-pojistneho)) |
| Annual maximum social insurance base per employee (48 times the average wage) | CZK 2,350,416 | 2026 | [ČSSZ, Maximální vyměřovací základ](https://www.cssz.gov.cz/web/cz/maximalni-vymerovaci-zaklad); SSPA § 15a(1) |
| Maximum health insurance base | None | 2026 | VZP, Vyměřovací základ a výpočet pojistného |
| Minimum health insurance base (the minimum wage) | CZK 22,400 a month; minimum premium CZK 3,024 (minimum wage CZK 24,900 from 1 January 2027) | 2026 | [MPSV Communication 356/2025 Coll.](https://e-sbirka.gov.cz/sb/2025/356); [MPSV Communication 171/2026 Coll.](https://e-sbirka.gov.cz/sb/2026/171); [VZP, Minimální mzda](https://www.vzp.cz/platci/informace/obzp/minimalni-mzda); HIPA § 3(6) |
| Earnings threshold for an employment contract or DPČ (rozhodný příjem) | CZK 4,500 a month | 2026 | [SIA § 6(2)](https://e-sbirka.gov.cz/sb/2006/187); [ČSSZ](https://www.cssz.gov.cz/web/cz/vypocet-pojistneho) (twice the threshold is CZK 9,000 in 2026) |
| Earnings threshold for a DPP | CZK 12,000 a month per employer (CZK 12,500 from 1 January 2027) | 2026 | [MPSV Communication 396/2025 Coll.](https://e-sbirka.gov.cz/sb/2025/396); [MPSV Communication 184/2026 Coll.](https://e-sbirka.gov.cz/sb/2026/184); SIA § 7a(1) |
| Employer discount for qualifying part-time staff | 5% of their bases | 2026 | SSPA § 7a and § 7b(1) |
| Ceiling for that discount: monthly base per employee | 1.5 times the average wage, CZK 73,451 (rounded up) | 2026 | SSPA § 7a(3)(a); [ČSSZ, Sleva na pojistném zaměstnavatele](https://www.cssz.gov.cz/web/cz/slevy-na-pojistnem) |
| Ceiling for that discount: base per hour worked | 1.15% of the average wage, CZK 564 (rounded up) | 2026 | SSPA § 7a(3)(b); ČSSZ, Sleva na pojistném zaměstnavatele |
| Discount for a working old-age pensioner (employee's share) | 6.5% of the base, so the employee pays 0.6% | 2026 | [ČSSZ, Sleva na pojistném zaměstnance](https://www.cssz.gov.cz/web/cz/sleva-na-pojistnem-zamestnance); SSPA § 7e |
| Discount for a DPP worker in fruit or vegetable growing (employee's share) | 7.1% of the base, so the employee pays nothing; not due if the month's DPP income from that employer exceeds the average wage rounded down to CZK 500 | 2026 | SSPA §§ 7f and 7g |
| Voluntary sickness insurance for an employee of a foreign employer | 2.7% | 2026 | ČSSZ, Sazby pojistného; SSPA § 7(1)(g) |
| Late payment penalty (penále), social and health | Civil-law default interest: CNB repo rate on the first day of the half-year when the default began, plus 8 points. 11.50% a year for defaults starting 1 January to 30 June 2026 (repo 3.50%). 11.75% for defaults starting 1 July to 31 December 2026 (repo 3.75% from 19 June 2026). VZP gives 0.0322% a day | 2026 | SSPA § 20(1); HIPA § 18(1); [Government Regulation 351/2013 Coll. § 2](https://e-sbirka.gov.cz/sb/2013/351); [CNB repo history](https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt); [VZP, Dlužné pojistné](https://www.vzp.cz/platci/informace/zamestnavatel/dluzne-pojistne-penale-pokuty) |

Bases and premiums are rounded up to whole koruna (SSPA § 7(3); HIPA § 2(2)).

## The taxable base

**What is in the base.** For both social and health insurance, the employee's base is the total employment income that is subject to Czech personal income tax and not exempt, that the employer has booked (zúčtoval) for the month (SSPA § 5(1); HIPA § 3(1)). Benefits in kind and other advantages count. These are left out of both bases (ČSSZ, Výpočet pojistného; HIPA § 3(2)):

- compensation for damage under the Labour Code;
- severance pay (odstupné) and similar payments on leaving;
- miners' loyalty bonus;
- payments to an old-age or third-degree invalidity pensioner more than one year after the job ended;
- one-off hardship relief after a natural disaster, fire or similar event.

**The employer's base** is the total of its employees' bases, split by rate group: ordinary staff, paramedics and fire brigade, and risk jobs (ČSSZ, Výpočet pojistného). The employer deducts the employee's share from pay. It pays that share together with its own (ČSSZ, Obecné informace).

**Annual social cap.** Social insurance is charged on at most CZK 2,350,416 of an employee's bases in 2026 (SSPA § 15a(1)).

- **One employer.** Once the year's bases pass the cap, neither the employee nor the employer pays social insurance on the excess. This also applies to several jobs with the same employer (§ 15a(2)(a) and (4)).
- **Several employers.** Each employer keeps deducting. The employee's premium on the total above the cap is an overpayment. The employee claims it back in writing from the district social security office where they have permanent residence, with confirmations from each employer. Each employer must issue its confirmation within 8 days. The claim must be made within 5 years after the year ends. Employer premiums on the excess are not refunded (§ 15a(2)(b) and (3); [ČSSZ, Vrácení přeplatku](https://www.cssz.gov.cz/web/cz/vraceni-preplatku-na-pojistnem-pri-dosazeni-maximalniho-vymerovaciho-zakladu)).

Health insurance has no cap.

**Health minimum base.** Health insurance for an employee is charged on at least the minimum wage, CZK 22,400 a month in 2026 (HIPA § 3(4) and (6)). VZP describes it as the minimum base for employees in an employment contract (VZP, Minimální mzda). If actual earnings are lower, the employee pays 13.5% of the difference through the employer. If the shortfall is the employer's fault (an obstacle on the employer's side), the employer pays it (HIPA § 3(10)). The minimum is pro-rated by calendar days where the job did not last the whole month, where the employee had time off for important personal obstacles, or where the employee joined one of the exempt groups below during the month (HIPA § 3(9)). The minimum does not apply where the condition lasts the whole month (HIPA § 3(8)) for:

- a holder of a ZTP or ZTP/P disability card;
- a person who has reached pension age but does not meet the other conditions for an old-age pension;
- an employee who is also self-employed and pays health advances on at least the self-employed minimum;
- a person for whom the state also pays health insurance (for example a student or pensioner);
- a person whose only income is a foster carer's allowance.

Example: a part-time employee on an employment contract earns CZK 4,000 a month. That is below CZK 4,500, so there is no social insurance. Health insurance on CZK 4,000 is CZK 540: CZK 360 from the employer and CZK 180 from the employee. The top-up on the CZK 18,400 shortfall is CZK 2,484, paid by the employee. Total health insurance: CZK 3,024, the 2026 minimum.

**Employer discounts.**

- **Part-time staff (SSPA § 7a and § 7b).** The employer deducts 5% of the bases of qualifying employees from its social premium. The employee must be on an employment contract of 8 to 30 hours a week and fall in one of these groups:
  - aged 55 or over;
  - caring for their own child under 10, or caring for a dependent close person;
  - a student under 26;
  - joined from retraining in the last 12 months;
  - a person with a disability.

  An employee under 21 qualifies without the part-time condition. No discount is due for a month where (SSPA § 7a(3)):
  - the employee's bases from all employment contracts with that employer exceed 1.5 times the average wage (CZK 73,451 in 2026);
  - those bases per hour worked exceed 1.15% of the average wage (CZK 564 in 2026);
  - the hours worked, including time treated as work, exceed 138 (pro-rated if the job did not last the whole month). This limit does not apply to an employee under 21;
  - the employee is disabled and the employer is a recognised protected labour market employer;
  - the employee is included in a claim for the part-time work (kurzarbeit) allowance.

  The discount for one employee goes to one employer only. The employer must notify ČSSZ of its intention to claim it, at the earliest 1 month before and at the latest by the JMH deadline for the first month claimed. Where two employers notify, the first to do so gets it. The discount is deducted in the JMH and only on a JMH filed on time; a late or corrected report cannot add it. When the conditions stop, the employer notifies ČSSZ within 8 days after the last month claimed (SSPA § 7a(4) and (5), § 7b; ČSSZ, Sleva na pojistném zaměstnavatele).
- **Working old-age pensioners (SSPA § 7e).** An employee who draws a full old-age pension can claim a discount of 6.5% of their base. They pay only 0.6%. The claim is made to the employer with proof of the pension, for the month of the claim onwards, never backwards (ČSSZ, Sleva na pojistném zaměstnance). The employer's own 24.8% is unchanged. The discount is rounded up separately and deducted from the 7.1% premium (SSPA § 7e(1)).
- **DPP workers in fruit and vegetable growing (SSPA §§ 7f and 7g).** A DPP worker whose agreement meets § 6 of the Agriculture Act gets a discount of 7.1% of the base, so pays no employee social insurance. It is not due for a month in which the worker's income from all such DPPs with that employer is above the average wage rounded down to the nearest CZK 500. The employer claims it in the JMH. The employer's 24.8% is unchanged.

## Deadlines and filing

- **Payment.** Social insurance for a month is due from the 1st to the 20th of the following month, to the account of the district social security office (SSPA § 9(1); [ČSSZ, Platba a termíny](https://www.cssz.gov.cz/web/cz/platba-a-terminy)). Health insurance is due on the same dates, to each insurer with which employees are insured (HIPA § 5(2) and (3)). Payment counts on the day it reaches the account. Cash is not accepted for social insurance.
- **Single monthly report (JMH) to ČSSZ.** From 1 January 2026 the JMHZ Act replaced the separate social insurance returns and the DPP income report. The JMH carries the employer's base, the premium, discounts and per-employee data. Its data go to MPSV, ČSSZ, the Statistics Office, the Labour Office, the Ministry of Finance and the Financial Administration ([ČSSZ, Co je JMHZ](https://www.cssz.gov.cz/web/cz/co-je-jmhz-)). It is filed electronically only (data box, ČSSZ ePortal, or the ČSSZ data interface), from the 1st to the 20th of the following month (JMHZ Act §§ 7(1) and 8(1)). The report for April 2026 was due 1 to 20 May 2026. The reports for January, February and March 2026 were filed separately between 1 April and 30 June 2026 ([ČSSZ, Kdo podává JMH](https://www.cssz.gov.cz/web/cz/kdo-podava-jmh-); SSPA § 9(2)).
- **Registering the employer with ČSSZ.** From 1 July 2026 an employer must register in the ČSSZ employer register (evidence zaměstnavatelů), with each payroll office, at the latest 2 working days before its first employee starts work and at the earliest 15 days before. Changes are due within 8 days of learning of them. An employer whose last employee has left deregisters within 8 days (JMHZ Act § 17(1) to (6); § 40(b)). The data interface cannot be used for these filings (§ 8(1)(c)).
- **Registering employees with ČSSZ.** From 1 July 2026 the employer must register each employee before they start work, at the earliest 8 days before. A partial registration (name, birth number, place of birth, citizenship and start date) is allowed for staff who are not foreigners. The remaining details then follow within 8 days of the start. A foreign employee must be fully registered before starting. Changes and deregistration are due within 8 days (JMHZ Act § 19; [ČSSZ, Evidence zaměstnanců](https://www.cssz.gov.cz/web/cz/evidence-zamestnancu-prihlaseni-zmena-odhlaseni-)).
- **Health insurer.** The employer notifies the employee's insurer of the start and end of a job within 8 days. For an employee on only a DPP or only a DPČ, the deadline is the 20th of the month after the month they became, or stopped being, a payer (PHIA § 10(1)(a)). The employer also files a monthly payment report (přehled o platbách pojistného) with each insurer by the payment due date, electronically only. The report shows the total bases, the total premium and the number of employees. Corrections are due within 8 days of finding the error (HIPA § 25(3), (4) and (7)). ČSSZ does not list the health insurers among the bodies that receive JMH data, so this report continues alongside the JMH.

## Penalties and interest

- **Late payment penalty (penále).** Unpaid or underpaid social or health insurance carries a penalty at the civil-law default interest rate (SSPA § 20(1); HIPA § 18(1)). The rate is the CNB repo rate on the first day of the half-year in which the default began, plus 8 points (Government Regulation 351/2013 Coll. § 2). That gives 11.50% a year for defaults that began in January to June 2026 and 11.75% for July to December 2026. For social insurance it runs from the day after the due date to the day of payment and is rounded up to whole koruna (SSPA § 20(2) and (5)). Health insurance paid to the wrong insurer or under the wrong variable symbol counts as unpaid (HIPA § 18(1)).
- **JMHZ offences (JMHZ Act § 28).**
  - Failing to file a JMH on time, filing one that is ineffective after the deadline, or not filing after a ČSSZ request: a fine of up to CZK 5,000 times the number of employees on the register.
  - Failing to register with the employer register, or failing to register an employee on time or with correct data: up to CZK 100,000.
  - Most other registration failures: up to CZK 20,000 or CZK 50,000.
- **Health insurer fines.** For failing to file the payment report or other reporting duties: up to CZK 50,000 for each breach (HIPA § 26(1)). If the report is still missing after a written request, the insurer can fix a probable premium by decision and charge the penalty on it (HIPA § 25a).
- **Wrong pensioner discount.** If the employer deducts a discount the employee was not entitled to, the shortfall is the employer's debt. The employee must repay the employer the discount and any penalty if they gave wrong information (ČSSZ, Sleva na pojistném zaměstnance).

## Cross-border points

- **One country only inside the EU.** Regulation (EC) 883/2004 applies within the EU, EEA and Switzerland. A worker is covered by one country's social security law, normally the country where the work is done.
- **Postings.** A worker posted temporarily from another state stays in the sending state's system if the posting is expected to last no more than 24 months, proved by an A1 certificate (Art. 12). A longer posting needs an exception agreed in advance (Art. 16) ([ČSSZ, Vyslaní pracovníci](https://www.cssz.gov.cz/vyslani-pracovnici)).
- **Czech employer, work permanently abroad.** An employee of a Czech-based employer working permanently abroad is insured in Czechia only if they are not compulsorily insured in the work state and have permanent residence in the Czech Republic or another EU state (SIA § 6(1)(a)(2)).
- **Foreign employer without a Czech base.** An employee of such an employer can join pension insurance voluntarily, and then sickness insurance, at 2.7% (SIA § 6(3); SSPA § 7(1)(g); ČSSZ, Sazby pojistného). In the month of joining and the next 3 months, the sickness base cannot exceed half the average wage, CZK 24,484 in 2026 (ČSSZ, Výpočet pojistného).
- **Third-country nationals without a valid residence permit** who work in the Czech Republic are excluded from sickness insurance (SIA § 9(2)).
- **Income tax** for incoming and outgoing employees: see [cz-cross-border](cz-cross-border.md).

## Worked examples

### Example 1: full-time employee on CZK 60,000 a month

An employee on an employment contract earns a gross salary of CZK 60,000 in May 2026. She has one employer, no discount applies, and the minimum base is not an issue.

1. Social insurance, employee share: 7.1% of 60,000 = CZK 4,260, deducted from pay.
2. Social insurance, employer share: 24.8% of 60,000 = CZK 14,880.
3. Health insurance, total: 13.5% of 60,000 = CZK 8,100. The employee pays one third, CZK 2,700. The employer pays two thirds, CZK 5,400.
4. The employer pays CZK 19,140 to the district social security office (4,260 + 14,880) and CZK 8,100 to her health insurer, all by 20 June 2026. The May JMH and the insurer's payment report are due by the same date.
5. Employer cost: 60,000 + 14,880 + 5,400 = CZK 80,280. Contributions deducted from her pay: 4,260 + 2,700 = CZK 6,960 (income tax is extra).

```oa-check
name: CZ employee CZK 60,000 a month, 2026 contributions
inputs:
  gross: 60000
steps:
  - social_employee: gross * 0.071
  - social_employer: gross * 0.248
  - health_total: gross * 0.135
  - health_employee: health_total / 3
  - health_employer: health_total - health_employee
  - employer_cost: gross + social_employer + health_employer
  - employee_deductions: social_employee + health_employee
expected:
  social_employee: 4260
  social_employer: 14880
  health_total: 8100
  health_employee: 2700
  health_employer: 5400
  employer_cost: 80280
  employee_deductions: 6960
```

### Example 2: a manager on CZK 250,000 a month reaches the social cap

A manager earns CZK 250,000 every month of 2026 (CZK 3,000,000 for the year) from one employer.

1. January to September: the bases total 9 × 250,000 = CZK 2,250,000. Each month the employee pays CZK 17,750 (7.1%) and the employer CZK 62,000 (24.8%).
2. October: only CZK 100,416 of the salary is left under the CZK 2,350,416 cap. The employee pays 7.1% of that: 7,129.536, rounded up to CZK 7,130. The employer pays 24.8%: 24,903.168, rounded up to CZK 24,904.
3. November and December: no social insurance for either party (SSPA § 15a(2)(a) and (4)).
4. Year totals: employee CZK 166,880, employer CZK 582,904. Without the cap they would have been CZK 213,000 and CZK 744,000.
5. Health insurance has no cap: 13.5% of 250,000 = CZK 33,750 every month, CZK 405,000 for the year. The employee pays CZK 135,000 of that, the employer CZK 270,000.

If the manager had a second employer, both would keep deducting. The manager would then claim the employee's excess back from ČSSZ after the year end.

```oa-check
name: CZ salary CZK 250,000 a month, 2026 social cap reached in October
inputs:
  monthly: 250000
  cap: 2350416
steps:
  - base_to_september: monthly * 9
  - base_october: min(monthly, cap - base_to_september)
  - employee_month: monthly * 0.071
  - employer_month: monthly * 0.248
  - employee_october: ceil(base_october * 0.071)
  - employer_october: ceil(base_october * 0.248)
  - employee_social_year: employee_month * 9 + employee_october
  - employer_social_year: employer_month * 9 + employer_october
  - health_year: monthly * 12 * 0.135
  - health_employee_year: health_year / 3
  - health_employer_year: health_year - health_employee_year
expected:
  base_to_september: 2250000
  base_october: 100416
  employee_october: 7130
  employer_october: 24904
  employee_social_year: 166880
  employer_social_year: 582904
  health_year: 405000
  health_employee_year: 135000
  health_employer_year: 270000
```

## Ask the client first

1. What type of contract each worker has (employment contract, DPČ or DPP), and the agreed monthly earnings. This decides whether the CZK 4,500 or CZK 12,000 threshold applies, or neither.
2. Whether any worker has other jobs, with you or with other employers, in 2026. This affects the small-scope and DPP tests and the social cap.
3. Whether any worker draws a full old-age pension, is aged 55 or over, a student under 26, under 21, disabled, or a parent of a child under 10 working part-time. These decide the discounts.
4. Whether the state also pays health insurance for the worker, or whether they are self-employed paying at least the minimum advances. This decides the health minimum base.
5. Where each worker lives and works, and whether they hold an A1 certificate from another state.
6. Each worker's health insurer, and whether the employer is already in the ČSSZ employer register under the JMHZ Act.

## Sources

| Source | URL | Read on |
|---|---|---|
| ČSSZ, Sazby pojistného (2026 rates) | https://www.cssz.gov.cz/web/cz/vyse-a-sazba | 2026-10-23 |
| ČSSZ, Výpočet pojistného (base, 2026 thresholds CZK 9,000, 12,242, 24,484) | https://www.cssz.gov.cz/web/cz/vypocet-pojistneho | 2026-10-23 |
| ČSSZ, Maximální vyměřovací základ (CZK 2,350,416 for 2026) | https://www.cssz.gov.cz/web/cz/maximalni-vymerovaci-zaklad | 2026-10-23 |
| ČSSZ, Vrácení přeplatku při dosažení maximálního vyměřovacího základu | https://www.cssz.gov.cz/web/cz/vraceni-preplatku-na-pojistnem-pri-dosazeni-maximalniho-vymerovaciho-zakladu | 2026-10-23 |
| ČSSZ, Platba a termíny | https://www.cssz.gov.cz/web/cz/platba-a-terminy | 2026-10-23 |
| ČSSZ, Obecné informace (pojistné) | https://www.cssz.gov.cz/web/cz/platba-pojistneho-obecne-informace | 2026-10-23 |
| ČSSZ, Sleva na pojistném zaměstnance pracujícího důchodce | https://www.cssz.gov.cz/web/cz/sleva-na-pojistnem-zamestnance | 2026-10-23 |
| ČSSZ, Sleva na pojistném zaměstnavatele (2026 limits CZK 73,451 and CZK 564; notice of intention) | https://www.cssz.gov.cz/web/cz/slevy-na-pojistnem | 2026-10-23 |
| ČSSZ, Co je JMHZ? | https://www.cssz.gov.cz/web/cz/co-je-jmhz- | 2026-10-23 |
| ČSSZ, Kdo podává JMH, způsob, lhůty a jeho obsah | https://www.cssz.gov.cz/web/cz/kdo-podava-jmh- | 2026-10-23 |
| ČSSZ, Evidence zaměstnanců (přihlášení, změna, odhlášení) | https://www.cssz.gov.cz/web/cz/evidence-zamestnancu-prihlaseni-zmena-odhlaseni- | 2026-10-23 |
| ČSSZ, JMHZ a odměny členů volebních komisí 2026 (CZK 4,500 small-scope threshold) | https://www.cssz.gov.cz/web/cz/-/jmhz-a-odmeny-clenu-volebnich-komisi-prehled-pravidel-pro-rok-2026 | 2026-10-23 |
| ČSSZ, Vyslaní pracovníci (Regulation 883/2004, A1, 24 months) | https://www.cssz.gov.cz/vyslani-pracovnici | 2026-10-23 |
| VZP, Vyměřovací základ a výpočet pojistného (13.5%, minimum CZK 22,400, no maximum) | https://www.vzp.cz/platci/informace/zamestnavatel/vymerovaci-zaklad-a-vypocet-pojistneho | 2026-10-23 |
| VZP, Minimální mzda (CZK 22,400, premium CZK 3,024) | https://www.vzp.cz/platci/informace/obzp/minimalni-mzda | 2026-10-23 |
| VZP, Splatnost a další zásady pro platbu pojistného (one third and two thirds, due 1st to 20th) | https://www.vzp.cz/platci/informace/zamestnavatel/splatnost-a-dalsi-zasady-pro-platbu-pojistneho | 2026-10-23 |
| VZP, Dlužné pojistné, penále, pokuty (0.0322% a day) | https://www.vzp.cz/platci/informace/zamestnavatel/dluzne-pojistne-penale-pokuty | 2026-10-23 |
| Act No. 589/1992 Coll. (SSPA), consolidated: §§ 5, 7, 7a, 7b, 7e, 7f, 7g, 8, 9, 15a, 20 | https://e-sbirka.gov.cz/sb/1992/589 | 2026-10-23 |
| Act No. 187/2006 Coll. (SIA), version in force 1 July to 31 December 2026: §§ 5, 6, 7, 7a, 9 | https://e-sbirka.gov.cz/sb/2006/187 | 2026-10-23 |
| Act No. 592/1992 Coll. (HIPA), consolidated: §§ 2, 3, 5, 18, 25, 25a, 26 | https://e-sbirka.gov.cz/sb/1992/592 | 2026-10-23 |
| Act No. 48/1997 Coll. (PHIA), consolidated: §§ 5, 9, 10 | https://e-sbirka.gov.cz/sb/1997/48 | 2026-10-23 |
| Act No. 323/2025 Coll. (JMHZ Act): §§ 7, 8, 17, 19, 28, 34, 40 | https://e-sbirka.gov.cz/sb/2025/323 | 2026-10-23 |
| MPSV Communication No. 396/2025 Coll. (DPP threshold CZK 12,000 from 1 January 2026) | https://e-sbirka.gov.cz/sb/2025/396 | 2026-10-23 |
| MPSV Communication No. 184/2026 Coll. (DPP threshold CZK 12,500 from 1 January 2027) | https://e-sbirka.gov.cz/sb/2026/184 | 2026-10-23 |
| MPSV Communication No. 356/2025 Coll. (minimum wage CZK 22,400 for 2026) | https://e-sbirka.gov.cz/sb/2025/356 | 2026-10-23 |
| MPSV Communication No. 171/2026 Coll. (minimum wage CZK 24,900 for 2027) | https://e-sbirka.gov.cz/sb/2026/171 | 2026-10-23 |
| Government Regulation No. 351/2013 Coll., § 2 (default interest: repo plus 8 points) | https://e-sbirka.gov.cz/sb/2013/351 | 2026-10-23 |
| Czech National Bank, two-week repo rate history | https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt | 2026-10-23 |

Not yet confirmed: whether the health minimum base applies to DPP and DPČ workers who pass the earnings threshold (VZP describes the minimum for employees in an employment contract; HIPA § 3(8) does not list agreements among the exceptions, and no other statutory exclusion was found); how the employee's one third of the health premium is rounded when the total is not divisible by 3 (PHIA § 9(2) sets the split but not the rounding); the CZK 4,500 small-scope threshold for 2027 (no MPSV communication found).
