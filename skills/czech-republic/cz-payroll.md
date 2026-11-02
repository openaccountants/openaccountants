---
name: cz-payroll
description: "Use for running Czech payroll as an employer in 2026. Covers registration with ČSSZ, the tax office and health insurers under the new single monthly employer report (JMHZ), the monthly gross-to-net sequence (employee social insurance 7.1%, health insurance 4.5%, the 15% and 23% tax advance, the signed prohlášení k dani, the CZK 2,570 monthly taxpayer credit and child credits), DPP and DPČ agreements and the 15% withholding tax below CZK 12,000 and CZK 4,500, the 2026 minimum wage of CZK 22,400, the CZK 129.50 tax-free meal contribution, sick pay for the first 14 days (náhrada mzdy), the annual reconciliation and vyúčtování, payslips, record keeping and penalties. Trigger on: Czech payroll, mzdy, výplatní páska, záloha na daň, srážková daň, DPP, DPČ, prohlášení poplatníka, JMHZ, stravenkový paušál, náhrada mzdy, roční zúčtování. Out of scope: cz-employee-income-tax (the employee's own return), cz-employee-contributions (contribution rules in depth), cz-social-health (self-employed), cz-cross-border."
version: 0.3
jurisdiction: CZ
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Czech Republic: running payroll (2026)

This skill takes an employer through one Czech payroll month and the year-end steps for 2026. The employee's own tax return is in [cz-employee-income-tax](cz-employee-income-tax.md). The rules on who pays social and health insurance, the bases and the exceptions are in [cz-employee-contributions](cz-employee-contributions.md). Self-employed contributions are in [cz-social-health](cz-social-health.md). Non-residents, treaties and moving in or out are in [cz-cross-border](cz-cross-border.md).

2026 is a transition year. The Act on the single monthly employer report (zákon č. 323/2025 Sb., JMHZ) took effect on 1 January 2026. One electronic monthly report to ČSSZ (JMH) now carries the data of more than 30 earlier forms, in full or in part, including the social insurance statement (přehled o výši pojistného), the DPP report and the ELDP (ČSSZ list of forms). No přehled or DPP report is filed for any month of 2026: the January to March data went into JMH reports filed from 1 April to 30 June 2026, and monthly JMH filing runs from the April 2026 report (MPSV, jmhz.mpsv.cz). The annual tax statement (vyúčtování) for 2026 is still filed in 2027. It is abolished for later years.

## Who this applies to

- Any person or company that employs at least one employee, of any size or legal form, including an SVJ that pays a reward and a company that pays its jednatel. This is the JMHZ definition of an employer from 1 January 2026 (323/2025 Sb.; ČSSZ "Kdo podává JMH").
- All employment income under the Income Taxes Act (586/1992 Sb., ITA) § 6: an employment contract (pracovní poměr), a DPP (dohoda o provedení práce, at most 300 hours a year per employer, Labour Code § 75), a DPČ (dohoda o pracovní činnosti, at most half the standard weekly hours on average, Labour Code § 76), and pay to a jednatel or board member.
- The employer is the tax payer (plátce daně) for the employee's tax advance, the payer of both halves of social insurance to ČSSZ, and the payer of both parts of health insurance to the employee's health insurer.
- Out: a self-employed person with no employees (no JMHZ duty); work under a business contract with an OSVČ.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Minimum wage, 40-hour week | CZK 22,400 a month, CZK 134.40 an hour | 2026 | https://www.mpsv.cz/minimalni-mzda |
| Average wage used for tax limits | CZK 48,967 (46,278 x 1.0581) | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Tax advance rate | 15% up to CZK 146,901 a month; 23% above | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Annual 23% threshold (36 x average wage) | CZK 1,762,812 | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Basic taxpayer credit | CZK 30,840 a year, CZK 2,570 a month | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Child credit, first / second / third and later child | CZK 1,267 / 1,860 / 2,320 a month (doubled for a ZTP/P child) | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Monthly child bonus paid if | bonus at least CZK 50 and monthly pay at least CZK 11,200 (half the minimum wage) | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Disability credits | CZK 210 / 420 / 1,345 a month (1st-2nd degree / 3rd degree / ZTP/P) | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Employee social insurance | 7.1% (6.5% pension, 0.6% sickness) | 2026 | https://www.cssz.gov.cz/web/cz/vyse-a-sazba |
| Employer social insurance | 24.8% (21.5% pension, 2.1% sickness, 1.2% employment policy); 27.8% for employees in risky employment (rizikové zaměstnání); 29.8% for paramedics and company fire brigade members | 2026 | https://www.cssz.gov.cz/web/cz/vyse-a-sazba |
| Maximum annual social insurance base | CZK 2,350,416 (48 x average wage) | 2026 | https://www.cssz.gov.cz/web/cz/maximalni-vymerovaci-zaklad |
| Health insurance | 13.5% of the base: employee one third (4.5%), employer two thirds (9%) | 2026 | https://e-sbirka.gov.cz/sb/1992/592 (§ 2); https://e-sbirka.gov.cz/sb/1997/48 (§ 9(2)) |
| Health insurance minimum base | the minimum wage, CZK 22,400 | 2026 | https://e-sbirka.gov.cz/sb/1992/592 (§ 3(6)) |
| DPP: insured and no withholding tax from | CZK 12,000 a month with one employer | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Small-scale employment and DPČ: insured from | CZK 4,500 a month (rozhodný příjem) | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Withholding tax (srážková daň) on § 6(4) income | 15% | 2026 | https://e-sbirka.gov.cz/sb/1992/586 (§ 36(2)(m)) |
| Tax-free meal contribution per shift | CZK 129.50 (70% of the CZK 185 meal allowance cap for a 5-12 hour trip) | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Home office flat allowance, tax-free | CZK 4.70 per hour started | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |
| Mandatory employer contribution to an old-age savings product (category 3 risky work, at least 3 such shifts in the month, once the employee has notified the employer) | 4% of the month's assessment base; counts toward the CZK 50,000 annual exemption for such contributions | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/informace-stanoviska-sdeleni/2026/informace-k-povinnemu-prispevku-na-produkty-na-stari |
| Sick pay reduction thresholds (hourly, for náhrada mzdy) | CZK 285.78 / 428.58 / 856.98 (the sickness insurance thresholds of CZK 1,633 / 2,449 / 4,897 times 0.175, rounded up to the haléř) | 2026 | https://www.cssz.gov.cz/web/cz/-/prehled-nejdulezitejsich-udaju-pro-socialni-zabezpeceni-v-roce-2026; Labour Code § 192(2) |
| Company car benefit | 1% of the car's price a month (0.5% low-emission, 0.25% zero-emission), at least CZK 1,000 | 2026 | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace |

## The taxable base

**The monthly sequence for one employee.**

1. **Gross pay.** Add all taxable pay and benefits for the month, in cash or in kind (ITA § 6(1)). Leave out exempt items: travel allowances within the legal limits, the meal contribution up to CZK 129.50 per shift of at least 3 hours (a second contribution is allowed for a shift over 11 hours), the home office flat amount up to CZK 4.70 an hour (ITA § 6(7), § 6(9)(b)), and statutory sick pay for the first 14 days up to the legal minimum (ITA § 6(9)(p)). Amounts above a limit are taxable pay.
2. **Social insurance.** The base is the taxable pay that is not exempt (Act 589/1992 Sb.). Round the base and the contribution up to whole crowns. Deduct 7.1% from the employee. The employer adds 24.8% on the total of its employees' bases. Stop both once the employee's bases with this employer reach CZK 2,350,416 in the year. With several employers, the employee claims the overpayment back from ČSSZ (ČSSZ, maximum base).
3. **Health insurance.** Use the same base, but at least the minimum wage (Act 592/1992 Sb. § 3(4), (6)). Exceptions apply, for example ZTP/P holders and people the state also insures (§ 3(8)). Work out 13.5% and round up. The employee pays one third, the employer two thirds (Act 48/1997 Sb. § 9(2)). If the base is below the minimum, the employee pays 13.5% of the shortfall through the employer. If the shortfall is caused by the employer, the employer pays it (§ 3(10)). The minimum is cut pro rata for a part month (§ 3(9)).
4. **Tax advance.** The base is the month's taxable pay. Since 2024 there is no "super-gross" uplift. Round the base up to whole crowns if it is CZK 100 or less. Round it up to the next CZK 100 if it is more. Apply 15% up to CZK 146,901 and 23% above, then round the advance up to whole crowns (ITA § 38h(1)-(3)).
5. **Credits.** If the employee signed the prohlášení k dani with this employer, subtract the monthly CZK 2,570 credit and any disability credit, down to zero. Then subtract the child credit. Any child credit left over is paid as a monthly bonus if the rules in the table are met (ITA § 38h(4), § 35d). Without a signed prohlášení, no credits apply (§ 38h(5)).
6. **Net pay** = gross pay minus employee social insurance, employee health insurance and the advance after credits, plus any child bonus.

**Sick pay (náhrada mzdy) for the first 14 days.** An employee who is signed off sick or in quarantine gets sick pay from the employer for the working days (and paid public holidays) in the first 14 calendar days, if they meet the conditions for sickness benefit on the first day (Labour Code § 192(1)). From day 15 ČSSZ pays sickness benefit (nemocenské) instead. A DPP or DPČ worker gets it on the same terms (§ 194), so only in a month when they are insured. The computation:
1. Take the employee's average hourly earnings (průměrný výdělek) from the previous calendar quarter (Labour Code § 354(1), § 356(1)).
2. Reduce it: 90% of the part up to CZK 285.78, 60% of the part from CZK 285.78 to CZK 428.58, 30% of the part from CZK 428.58 to CZK 856.98, and nothing above (§ 192(2), applying Act 187/2006 Sb. § 21(1)(a)).
3. Pay 60% of the reduced figure for each hour of the shifts missed (§ 192(2)). Halve it where sickness benefit would be halved (§ 192(4)). The employer may pay more by agreement or internal rule, but not more than the average earnings (§ 192(3)).
4. Sick pay up to this legal minimum is exempt from income tax (ITA § 6(9)(p)), so it is outside the social and health insurance bases, which only take taxable income that is not exempt (Act 589/1992 Sb. § 5(1); Act 592/1992 Sb. § 3(1)). Any top-up above the minimum is taxable pay and insurable.

**The prohlášení k dani** (form MFin 5457, vzor 27). The employee signs it with one employer only for the same period. The deadline is within 30 days of starting, then each year by 15 February (ITA § 38k(3)-(4)). It gives monthly credits. It is also needed for the annual reconciliation. A non-resident gets only the basic credit monthly (§ 38h(13)).

**DPP, DPČ and the 15% withholding tax.** In 2026, pay is taxed by a final 15% withholding tax instead of the advance when the employee has not signed a prohlášení with that employer and one of these applies (ITA § 6(4), § 36(2)(m)):
- the pay is under a DPP, and the DPP pay from that employer is below CZK 12,000 in the month; or
- the total pay from that employer in the month is below CZK 4,500.

The base is rounded down to whole crowns (§ 36(3)). Contributions follow the same thresholds. A DPP worker is insured for social and health insurance only in a month when DPP pay from one employer reaches CZK 12,000. Several DPPs with the same employer are added together (Act 187/2006 Sb. § 7a; Act 48/1997 Sb. § 5). A DPČ or small job is insured from CZK 4,500 (Act 187/2006 Sb. § 6). A resident can include the withheld income in a tax return and credit the tax (ITA § 36(6)). From 1 January 2027 this withholding tax is replaced by the normal advance (zákon č. 360/2025 Sb., čl. VI bod 10, in force 2027).

**Annual reconciliation (roční zúčtování).** The employee asks the last employer of the year by 15 February and hands in certificates from earlier employers. This works only if every employer that year was consecutive and the employee signed a prohlášení with each. The employer computes the annual tax by 31 March. It refunds any overpayment over CZK 50 with the March payroll. It does not collect an underpayment (ITA § 38ch). An employee who must file a return (for example, two employers at the same time) files their own return instead. That is covered in [cz-employee-income-tax](cz-employee-income-tax.md).

## Deadlines and filing

| What | When | Where and how | Source |
|---|---|---|---|
| Employer registration (new employer from 1 July 2026) | At least 2 working days before the first employee starts, at most 15 days before. From 1 April to 30 June 2026 it was within 8 days of the first employee starting (before a foreign employee starts) | ČSSZ employer evidence (evidence zaměstnavatelů), electronic only. This replaces the separate tax office registration of a payroll payer (ITA § 39 repealed from 1 April 2026) | ČSSZ evidence zaměstnavatelů; 323/2025 Sb. § 35(1); 360/2025 čl. VI bod 97 |
| Employee registration (from 1 July 2026) | Before the employee starts work, at most 8 days before. From 1 April to 30 June 2026 it was within 8 days of starting | ČSSZ employee evidence. Except for a foreign employee, the employer may register partial data first (name, birth number, place of birth, citizenship, expected start date) and the rest within 8 days of starting | ČSSZ evidence zaměstnanců; 323/2025 Sb. § 35(3) |
| Changes and deregistration | Within 8 days | ČSSZ evidence | ČSSZ evidence zaměstnanců |
| Health insurer: start and end of employment | Within 8 days; for a worker on DPP or DPČ only, by the 20th of the following month | The employee's health insurer | Act 48/1997 Sb. § 10(1)(a) |
| Social and health insurance payment | 1st to 20th of the following month | ČSSZ (OSSZ account); each health insurer | ČSSZ platba a termíny; Act 592/1992 Sb. § 5(2) |
| Single monthly report (JMH) | 1st to 20th of the following month (April 2026 report by 20 May 2026). January to March 2026 reports were due 1 April to 30 June 2026 | ČSSZ, electronic only: data box, ePortál ČSSZ or API | ČSSZ kdo podává JMH; jmhz.mpsv.cz |
| Tax advances paid over | By the 20th of the month in which the duty to withhold arose | The employer's tax office | ITA § 38h(10) |
| Withholding tax (§ 6(4)) paid over | By the end of the month after the month it was withheld | The tax office | ITA § 38d(3) |
| Employee's prohlášení and reconciliation request | 15 February 2027 for 2026 | Kept by the employer | ITA § 38k(4), § 38ch(1) |
| Annual reconciliation done | By 31 March 2027; refund with the March payroll | Payroll | ITA § 38ch(4)-(5) |
| Vyúčtování daně z příjmů ze závislé činnosti for 2026 | Paper: two months after the year end, which is 1 March 2027 because 28 February 2027 is a Sunday. Electronic: 20 March, which moves to Monday 22 March 2027. The deadline cannot be extended. It must be electronic if the employer paid non-residents, unless it is an individual with at most 10 of them | The tax office | ITA § 38j(4)-(7); Tax Code § 33(4); FS Q&A 2026 |
| Vyúčtování of withholding tax for 2026 | Within 3 months of the year end, by 31 March 2027 | The tax office | Tax Code § 137(2); FS Q&A 2026 |

From the 2027 tax year the vyúčtování is abolished. The tax is treated as assessed on 20 March of the following year from the advances reported in the JMH (360/2025 čl. VI body 63 and 80, in force 1 January 2027). ELDP forms are no longer filed for 2026. JMHZ carries the pension data, and an ELDP is made only where insurance ended before 1 April 2026 or ČSSZ asks for one (360/2025 čl. V bod 8).

**Payslip and records.** Each monthly payslip shows the parts of pay and every deduction. On request, the employer shows how the pay was computed (Labour Code § 142(6)). Keep a payroll sheet (mzdový list) for each employee with the items in ITA § 38j(2). On request, issue a certificate of the year's pay, advances and credits within 10 days (ITA § 38j(3)). Keep payroll sheets for pension purposes for 45 years after the year they cover (10 years for an old-age pensioner). Keep other insurance records for 6 years (Act 582/1991 Sb. § 35a(4)).

## Penalties and interest

- **Late or missing JMH:** a fine of up to CZK 5,000 times the number of employees in the employee evidence. **Not registering the employer or an employee on time:** up to CZK 100,000. **Late change notices:** up to CZK 20,000. **Late deregistration of an employee:** up to CZK 50,000 (323/2025 Sb. § 28).
- **Late vyúčtování:** after 5 working days late, 0.05% of the tax that should have been reported for each further day, at most 0.5%. It is not charged if under CZK 1,000. It is at least CZK 500 if never filed, and at most CZK 300,000. It is halved if the statement is filed within 30 days of the deadline and no other late filing was found that year (Tax Code § 250(2)-(5), (7)).
- **Late payment of advances or withholding tax:** default interest from the fourth day after the due date, at the Civil Code default interest rate (Tax Code § 252(2), (4)). It is not charged if the total for one tax and period is CZK 1,000 or less (§ 251a(2)).
- **Records and notices for the tax office:** a fine of up to CZK 500,000 (Tax Code § 247a(1)).
- **Late social insurance:** penále at the Civil Code default interest rate for each day from the day after the due date (Act 589/1992 Sb. § 20).
- **Late health insurance:** penále at the Civil Code default interest rate. It is not charged if it is CZK 200 or less for the year (Act 592/1992 Sb. § 18(4)).

## Cross-border points

- A non-resident employee working in the Czech Republic has advances withheld like a resident, but with only the basic credit. Other credits come only on the annual return, and only for an EU or EEA resident with at least 90% of their income from Czech sources (ITA § 38h(13); FS general information 2026).
- From 1 January 2026, pay to a non-resident member of a company body (dozorčí rada, představenstvo) is taxed by the advance at 15% and 23%, not by withholding tax. The member can sign a prohlášení (360/2025 Sb.; FS general information 2026).
- If workers do the work under a Czech company's instructions but a person abroad pays them, the Czech company is the employer for tax (ITA § 6(2)).
- An employee covered by another EU state's social security with an A1 certificate is not insured in the Czech Republic for that work. A foreign employee must be registered in the JMHZ employee evidence before starting work (ČSSZ evidence zaměstnavatelů). Residence, treaties and A1 rules are in [cz-cross-border](cz-cross-border.md).

## Worked examples

**Example 1. Full-time employee, gross CZK 50,000, signed prohlášení, one child.** The employee pays social insurance of 7.1% (CZK 3,550). Health insurance is 13.5% of CZK 50,000, CZK 6,750 in total. The employee's third is CZK 2,250 and the employer's two thirds CZK 4,500. The advance base is CZK 50,000, already a round hundred. 15% gives CZK 7,500. The basic credit of CZK 2,570 brings it to CZK 4,930, and the first child's credit of CZK 1,267 to CZK 3,663. Net pay is CZK 40,537. The employer also pays 24.8% social insurance (CZK 12,400) and its health share. Its total cost is CZK 66,900.

```oa-check
name: CZ payroll, gross CZK 50,000, prohlaseni signed, one child (2026)
inputs:
  gross: 50000
  basic_credit: 2570
  child_credit: 1267
steps:
  - social_employee: ceil(gross * 0.071)
  - health_total: ceil(gross * 0.135)
  - health_employee: health_total / 3
  - advance_base: ceil(gross / 100) * 100
  - advance: ceil(advance_base * 0.15)
  - advance_after_basic: max(advance - basic_credit, 0)
  - advance_final: advance_after_basic - child_credit
  - net_pay: gross - social_employee - health_employee - advance_final
  - social_employer: ceil(gross * 0.248)
  - health_employer: health_total - health_employee
  - employer_cost: gross + social_employer + health_employer
expected:
  social_employee: 3550
  health_total: 6750
  health_employee: 2250
  advance: 7500
  advance_final: 3663
  net_pay: 40537
  social_employer: 12400
  health_employer: 4500
  employer_cost: 66900
```

**Example 2. DPP worker paid CZK 11,900 in the month, with and without a prohlášení.** The DPP pay is below CZK 12,000, so there is no social or health insurance. If the worker has not signed a prohlášení with this employer, the employer withholds the final 15% tax: CZK 1,785, leaving CZK 10,115. If the worker signs a prohlášení instead, the normal advance applies. 15% of CZK 11,900 is CZK 1,785. The CZK 2,570 basic credit cuts it to nil, and the basic credit is never paid out as a bonus. So the worker keeps the full CZK 11,900. Signing changes the month's withholding by CZK 1,785. The edge case: if the same DPP pay reached CZK 12,000, the worker would be insured. Social insurance of 7.1% and health insurance would then apply, and withholding tax would no longer be possible.

```oa-check
name: CZ DPP CZK 11,900 below the 12,000 limit, withholding tax vs signed prohlaseni (2026)
inputs:
  pay: 11900
  dpp_limit: 12000
  basic_credit: 2570
steps:
  - shortfall_to_limit: dpp_limit - pay
  - withholding_base: floor(pay)
  - withholding_tax: floor(withholding_base * 0.15)
  - net_without_prohlaseni: pay - withholding_tax
  - advance_base: ceil(pay / 100) * 100
  - advance: ceil(advance_base * 0.15)
  - advance_after_credit: max(advance - basic_credit, 0)
  - net_with_prohlaseni: pay - advance_after_credit
  - difference: net_with_prohlaseni - net_without_prohlaseni
expected:
  shortfall_to_limit: 100
  withholding_tax: 1785
  net_without_prohlaseni: 10115
  advance: 1785
  advance_after_credit: 0
  net_with_prohlaseni: 11900
  difference: 1785
```

**Example 3. Sick pay for one week.** An employee on a 40-hour week has average hourly earnings of CZK 250 from the previous quarter and is signed off sick for five 8-hour working days, all in the first 14 days. CZK 250 is below the first threshold of CZK 285.78, so the reduced figure is 90%: CZK 225.00. Sick pay is 60% of that, CZK 135.00 an hour. For 40 hours the employer pays CZK 5,400. It is exempt from income tax, and no social or health insurance is due on it. If the employer topped it up to the full CZK 250 an hour, the extra CZK 4,600 (CZK 115 x 40) would be taxable and insurable pay.

```oa-check
name: CZ sick pay (nahrada mzdy), average hourly earnings CZK 250, 40 hours (2026)
inputs:
  avg_hourly: 250
  rh1: 285.78
  rh2: 428.58
  rh3: 856.98
  hours: 40
steps:
  - band1: min(avg_hourly, rh1) * 0.9
  - band2: max(min(avg_hourly, rh2) - rh1, 0) * 0.6
  - band3: max(min(avg_hourly, rh3) - rh2, 0) * 0.3
  - reduced: band1 + band2 + band3
  - hourly_sick_pay: reduced * 0.6
  - sick_pay: hourly_sick_pay * hours
  - top_up_to_full: (avg_hourly - hourly_sick_pay) * hours
expected:
  reduced: 225.00
  hourly_sick_pay: 135.00
  sick_pay: 5400.00
  top_up_to_full: 4600.00
```

## Ask the client first

1. What type of contract does each person have (employment contract, DPP, DPČ, jednatel), and what is the expected pay each month?
2. Has the employee signed a prohlášení k dani with you, and do they claim children, disability or ZTP/P? Do they work for another employer at the same time?
3. Is the employee tax resident in the Czech Republic? Do they hold an A1 certificate from another state?
4. Which health insurer is each employee with?
5. Are you already in the ČSSZ employer evidence, with your employees completed for JMHZ (data box, payroll software)?
6. Which benefits do you give (meal vouchers or cash meal contribution, company car, home office allowance, shares or options)?
7. Does anyone do risky work (category 3 or 4), and what were each employee's earnings and hours in the last calendar quarter (for sick pay)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Finanční správa, employment income for 2026 (rates, average wage, credits, child bonus, DPP and DPČ thresholds, meal and home office limits, car benefit, withholding tax, forms) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace | 2026-10-23 |
| Finanční správa, Q&A on employment income for 2025 and 2026 (vyúčtování deadlines) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/dotazy-a-odpovedi/2026/aktualni-dotazy-a-odpovedi-k-dani-z | 2026-10-23 |
| Finanční správa, mandatory employer contribution to old-age savings products (Act 324/2025 Sb.) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/informace-stanoviska-sdeleni/2026/informace-k-povinnemu-prispevku-na-produkty-na-stari | 2026-10-23 |
| ČSSZ, main social security figures for 2026 (sickness reduction thresholds) | https://www.cssz.gov.cz/web/cz/-/prehled-nejdulezitejsich-udaju-pro-socialni-zabezpeceni-v-roce-2026 | 2026-10-23 |
| MPSV, minimum wage 2026 | https://www.mpsv.cz/minimalni-mzda | 2026-10-23 |
| ČSSZ, social insurance rates | https://www.cssz.gov.cz/web/cz/vyse-a-sazba | 2026-10-23 |
| ČSSZ, maximum assessment base | https://www.cssz.gov.cz/web/cz/maximalni-vymerovaci-zaklad | 2026-10-23 |
| ČSSZ, calculation of contributions | https://www.cssz.gov.cz/web/cz/vypocet-pojistneho | 2026-10-23 |
| ČSSZ, payment and due dates | https://www.cssz.gov.cz/web/cz/platba-a-terminy | 2026-10-23 |
| ČSSZ, who files the JMH, deadlines and content | https://www.cssz.gov.cz/web/cz/kdo-podava-jmh- | 2026-10-23 |
| ČSSZ, what JMHZ is, and the list of forms it replaces (XLSX attached to the page) | https://www.cssz.gov.cz/web/cz/co-je-jmhz- | 2026-10-23 |
| ČSSZ, employer evidence | https://www.cssz.gov.cz/web/cz/evidence-zamestnavatelu-prihlaseni-zmena-odhlaseni- | 2026-10-23 |
| ČSSZ, employee evidence | https://www.cssz.gov.cz/web/cz/evidence-zamestnancu-prihlaseni-zmena-odhlaseni- | 2026-10-23 |
| MPSV, JMHZ project site (phases and deadlines) | https://jmhz.mpsv.cz | 2026-10-23 |
| Income Taxes Act 586/1992 Sb., § 6 (incl. § 6(9)(p)), § 35ba-35d, § 36, § 38d, § 38h, § 38ch, § 38j, § 38k | https://e-sbirka.gov.cz/sb/1992/586 | 2026-10-23 |
| Act 360/2025 Sb. (JMHZ amendments; čl. V, VI, VII (transitional rules: the 2026 vyúčtování is still due), XXXIV) | https://e-sbirka.gov.cz/sb/2025/360 | 2026-10-23 |
| Act 323/2025 Sb. on the single monthly employer report, § 28, § 35 | https://e-sbirka.gov.cz/sb/2025/323 | 2026-10-23 |
| Act 592/1992 Sb. on health insurance contributions, § 2, § 3, § 5, § 18 | https://e-sbirka.gov.cz/sb/1992/592 | 2026-10-23 |
| Act 48/1997 Sb. on public health insurance, § 5, § 9, § 10 | https://e-sbirka.gov.cz/sb/1997/48 | 2026-10-23 |
| Act 589/1992 Sb. on social insurance contributions, § 5, § 20 | https://e-sbirka.gov.cz/sb/1992/589 | 2026-10-23 |
| Act 187/2006 Sb. on sickness insurance, § 6, § 7a, § 21 | https://e-sbirka.gov.cz/sb/2006/187 | 2026-10-23 |
| Tax Code 280/2009 Sb., § 33, § 247a, § 250, § 251a, § 252 | https://e-sbirka.gov.cz/sb/2009/280 | 2026-10-23 |
| Labour Code 262/2006 Sb., § 75, § 76, § 142, § 192, § 194, § 354, § 356 | https://e-sbirka.gov.cz/sb/2006/262 | 2026-10-23 |
| Act 582/1991 Sb. on social security administration, § 35a | https://e-sbirka.gov.cz/sb/1991/582 | 2026-10-23 |

Not yet confirmed: whether the health insurance minimum base applies to a worker insured only through a DPP or DPČ (Act 592/1992 Sb. § 3(8) does not list them; the examples avoid the point); how the employee's one-third health share is rounded when 13.5% of the base does not divide by three (the examples use bases where it does); the legal basis, and the 2026 form, of any monthly statement each health insurer asks employers for (JMHZ does not replace it under the ČSSZ list); the current Civil Code default interest rate used for late-payment interest and penále (not given on the pages read); how the reduced hourly figure for sick pay is rounded when it is not a whole number of haléře (Labour Code § 192(2) applies the sickness benefit method "in a similar way"; Example 3 uses earnings below the first threshold, where the point does not arise).

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
