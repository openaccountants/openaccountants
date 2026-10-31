---
name: tr-payroll-social
description: "Turkish payroll and social security for tax year 2026: SGK premiums under the Social Insurance Law no. 5510, unemployment insurance under Law 4447, income tax withholding on wages under the Income Tax Law no. 193 and stamp tax on wages under Law 488. Covers employees (4/1-a) and the self-employed (Bağ-Kur, 4/1-b), the 2026 minimum wage (TRY 1,101 a day, TRY 33,030 a month gross, TRY 28,075.50 net), the premium floor and the new ceiling of nine times the floor (TRY 297,270 a month), the 2026 rates (pension 21%, employee 15% in total, employer 23.75% before the 2-point incentive), the minimum-wage income tax and stamp tax exemptions, tax-free meal, transport and childcare benefits, the monthly combined return (MUHSGK) by the 26th, and penalties. Trigger on: SGK primi, bordro, asgari ücret 2026, Bağ-Kur, muhtasar ve prim hizmet beyannamesi, Turkish payroll, SGK tavan. Out of scope: annual income tax (turkey-pit), company tax (tr-corporate-income-tax), VAT (turkey-vat)."
version: 0.1
jurisdiction: TR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Türkiye: payroll and social security (2026) v0.1

An employer in Türkiye withholds the employee's social security and unemployment premiums, income tax and stamp tax from each wage payment, adds its own premiums, and reports all of it on one monthly return, the muhtasar ve prim hizmet beyannamesi (MUHSGK), filed with the Revenue Administration (GİB). Premiums go to the Social Security Institution (Sosyal Güvenlik Kurumu, SGK). Figures below come from the consolidated Law 5510 (as amended by Law 7566 from 1 January 2026), Law 4447, the Income Tax Law 193, the Stamp Tax Law 488, the 2026 minimum wage decision and GİB's table of filing dates.

## Who this applies to

- **Employees (4/1-a).** People working under an employment contract for one or more employers are insured under Law 5510 art. 4(1)(a). Their employer pays and reports the premiums. Unemployment insurance applies to them under Law 4447 art. 49.
- **Self-employed (4/1-b, Bağ-Kur).** People insured under art. 4(1)(b), who work on their own account and not under an employment contract, pay their own premiums at the 4/1-b rate (art. 81(1)(g)).
- **Income tax withholding.** Every employer that is a company, public body, association, foundation, co-operative, or a trader or professional who declares real income must withhold tax on wages it pays (GVK art. 94(1)).
- **Out of this skill:** civil servants (4/1-c); the annual income tax return (see [turkey-pit](turkey-pit.md)); severance pay (kıdem tazminatı) and its ceiling; sector and regional premium incentives other than the general 2-point incentive.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Minimum wage, gross, per day | TRY 1,101 (1 January to 31 December 2026) | 2026 | Minimum Wage Determination Commission decision 2025/1, Official Gazette 26 December 2025 no. 33119, https://www.resmigazete.gov.tr/eskiler/2025/12/20251226-6.pdf |
| Minimum wage, gross, per month (30 days) | TRY 33,030 | 2026 | Decision 2025/1 (TRY 1,101 x 30) |
| Premium base floor | Minimum wage: TRY 1,101 a day, TRY 33,030 a month | 2026 | Law 5510 art. 82(1), https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5510.pdf |
| Premium base ceiling | 9 times the floor: TRY 9,909 a day, TRY 297,270 a month (7.5 times until 2025) | 2026 | Law 5510 art. 82(1) as amended by Law 7566 art. 24, in force 1 January 2026 |
| Ceiling for Turkish workers sent to countries with no social security agreement | 3 times the floor | 2026 | Law 5510 art. 82(1) |
| Pension (disability, old-age and death) premium | 21%: employee 9%, employer 12% (was 20%: 9% and 11%) | 2026 | Law 5510 art. 81(1)(a), amended by Law 7566 art. 23 from January 2026 |
| Short-term insurance premium | 2.25%, employer only | 2026 | Law 5510 art. 81(1)(c) |
| General health insurance premium | 12.5%: employee 5%, employer 7.5% | 2026 | Law 5510 art. 81(1)(f) |
| Unemployment insurance | 1% employee, 2% employer, 1% state | 2026 | Law 4447 art. 49, https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4447.pdf |
| Employee total | 15% (9 + 5 + 1) | 2026 | sum of the above |
| Employer total before incentive | 23.75% (12 + 2.25 + 7.5 + 2) | 2026 | sum of the above |
| Treasury incentive for private-sector employers | 2 points of the employer pension share (was 4 points), so 21.75% | 2026 | Law 5510 art. 81(1)(ı), amended by Law 7566 art. 23 |
| Self-employed (4/1-b) total | 35.75% (21 + 2.25 + 12.5), less a 5-point Treasury incentive if premiums are paid on time: 30.75% | 2026 | Law 5510 art. 81(1)(g), (j) |
| Income tax on wages | Wage scale 15% to TRY 190,000; 20% to 400,000; 27% to 1,500,000; 35% to 5,300,000; 40% above | 2026 | GVK art. 94(1), 103, https://www.mevzuat.gov.tr/MevzuatMetin/1.5.193.pdf |
| Minimum-wage income tax exemption | Wage up to gross minimum wage less employee pension, health and unemployment premiums (TRY 28,075.50 a month) | 2026 | GVK art. 23(18) |
| Stamp tax on wage payments | 0.759% (7.59 per thousand) | 2026 | Stamp Tax Law 488, table 1, IV-1(b), https://www.mevzuat.gov.tr/MevzuatMetin/1.5.488.pdf |
| Stamp tax exemption | The part of the wage equal to the gross minimum wage | 2026 | Law 488, table 2, IV-34 |
| Meal paid in cash or card where no meal is served | Exempt up to TRY 300 a working day | 2026 | GVK art. 23(8) |
| Transport paid by card or ticket where no transport is provided | Exempt up to TRY 158 a working day | 2026 | GVK art. 23(10) |
| Childcare paid to a nursery for female employees | Exempt up to 50% of the monthly gross minimum wage per child (TRY 16,515) | 2026 | GVK art. 23(16); Decision 2018/11674 |
| Disability allowance deducted from wages, monthly | TRY 12,000 / 7,000 / 3,000 (1st / 2nd / 3rd degree) | 2026 | GVK art. 31 |
| SGK late payment | 3% a month for the first three months, plus late interest | 2026 | Law 5510 art. 89 |

## The taxable base

**Premium base.** Premiums are computed on the employee's monthly earnings counted for premiums, but never on less than the floor or more than the ceiling. Where earnings are below the floor, the premiums on the difference are paid entirely by the employer (art. 82). If a person works in more than one job in the same insurance status and total premiums exceed what the ceiling would give, the excess employee share is refunded on request (art. 82).

**Income tax base.** Taxable wages are gross wages less the employee's own pension, health and unemployment premiums (GVK art. 63; art. 23(18)), less exempt benefits under art. 23 and any disability allowance (art. 31). The wage scale in art. 103 is applied to the employee's cumulative taxable wages for the year from January, so the rate rises during the year as the cumulative base crosses each band (art. 23(18) and art. 94(1) with art. 103 and 104).

**Minimum-wage exemption** (art. 23(18)). The part of the wage equal to the month's gross minimum wage less the employee's premiums is exempt. Tax is first computed on the whole taxable wage, with the exempt amount counted in the bands; then the tax that falls on the exempt part is deducted. The relief cannot exceed the tax on the minimum wage for that month. With more than one employer, only the highest wage gets the exemption.

**Stamp tax.** 0.759% of the gross wage, with the first TRY 33,030 a month (the gross minimum wage) exempt (Law 488, tables 1 and 2).

**Tax-free benefits** (art. 23). Meals provided at the workplace are exempt; where no meal is served, a cash or card payment up to TRY 300 a working day is exempt and any excess is taxed. Employer-organised transport is exempt; a ticket or card payment up to TRY 158 a working day is exempt where no transport is provided, and cash paid for transport is taxed. Nursery payments for female employees, paid directly to the nursery, are exempt up to 50% of the gross minimum wage per child per month.

## Deadlines and filing

- **Monthly MUHSGK return.** Filed by the 26th of the following month, 23:59, and paid within the filing period (GİB filing table). It combines the withholding return and the monthly premium and service document (GVK art. 98/A). The law sets the 23rd for filing (art. 98) and the 26th for paying withheld tax (art. 119); GİB's table gives the 26th for both.
- **Quarterly filing for small employers.** An employer with 10 or fewer employees may, after notifying its tax office, file quarterly: by 26 April, 26 July, 26 October and 26 January (GVK art. 98; GİB table).
- **SGK premiums.** The employer deducts the employee share from wages and pays it with its own share by the day SGK sets (Law 5510 art. 88).
- **Hiring notice.** The employer notifies SGK of each new employee in the form and by the time the law sets (art. 8); late or missing notice is fined (see below).
- **Records.** Employers keep workplace books and records for ten years from the start of the following year (art. 86).

## Penalties and interest

- **Late SGK premiums.** Unpaid premiums increase by a late payment charge (gecikme cezası) of 3% for each month for the first three months, plus monthly late interest (gecikme zammı) at the Treasury bill rate (Law 5510 art. 89).
- **Missing or late hiring notice.** An administrative fine of one gross minimum wage per employee (TRY 33,030 in 2026); two minimum wages if found by inspection or from other public bodies' data; five if repeated within a year (Law 5510 art. 102(1)(a)).
- **Late tax return or tax.** A late MUHSGK is a first-degree irregularity under VUK art. 352 (TRY 35,000 for capital companies in 2026). Tax not withheld or not paid carries a tax loss penalty of one times the tax (VUK art. 344) and late-payment surcharge of 3.7% a month (Law 6183 art. 51).

## Cross-border points

- **Foreign employers.** Wages paid in foreign currency by an employer with no legal or business seat in Türkiye, out of profits earned outside Türkiye, are exempt from income tax (GVK art. 23(14)). SGK insurance follows Law 5510 and any social security agreement, not the tax rule.
- **Turkish workers sent abroad** by employers working in countries with no social security agreement have a premium ceiling of three times the floor (art. 82(1)). Private-sector employers get a 5-point Treasury incentive on the general health premium for workers taken abroad from Türkiye (art. 81(1)(i)).
- **Wages for work abroad on construction, repair, assembly and technical services**, paid from the employer's foreign earnings, are exempt from income tax (GVK art. 23(19)).
- **Social security agreements.** Where Türkiye has an agreement with the other country, a posted worker may stay insured in the home country. The list of agreements is not covered here.

## Worked examples

### Example 1: Employee on the minimum wage, 2026

The employee earns the gross minimum wage of TRY 33,030 a month. Employee premiums are 14% (TRY 4,624.20) and 1% unemployment (TRY 330.30). The taxable wage is TRY 28,075.50. All of it is inside the minimum-wage exemption, so income tax is nil, and the gross wage is inside the stamp tax exemption, so stamp tax is nil. Net pay is TRY 28,075.50. The employer pays 19.75% SGK premiums after the 2-point incentive (TRY 6,523.43) and 2% unemployment (TRY 660.60), so the monthly cost is TRY 40,214.03.

```oa-check
name: Minimum-wage employee, gross TRY 33,030 (2026)
inputs:
  gross: 33030
  min_wage: 33030
steps:
  - base: min(gross, min_wage * 9)
  - emp_sgk: base * 0.14
  - emp_ui: base * 0.01
  - taxable: gross - emp_sgk - emp_ui
  - exempt_base: min_wage - min_wage * 0.15
  - tax_before: min(taxable, 190000) * 0.15
  - relief: min(exempt_base, 190000) * 0.15
  - income_tax: max(tax_before - relief, 0)
  - stamp: max(gross - min_wage, 0) * 0.00759
  - net: gross - emp_sgk - emp_ui - income_tax - stamp
  - employer_sgk: base * (0.12 + 0.0225 + 0.075 - 0.02)
  - employer_ui: base * 0.02
  - employer_cost: gross + employer_sgk + employer_ui
expected:
  taxable: 28075.50
  income_tax: 0
  net: 28075.50
  employer_cost: 40214.03
```

### Example 2: January pay above the premium ceiling

A manager earns TRY 400,000 gross in January 2026. Premiums are capped at the ceiling of TRY 297,270: employee premiums are TRY 41,617.80 (14%) and TRY 2,972.70 (1%). The taxable wage is TRY 355,409.50. As the first month of the year, the cumulative base is the January base: 15% on TRY 190,000 (TRY 28,500) plus 20% on TRY 165,409.50 (TRY 33,081.90), so TRY 61,581.90 before relief. The minimum-wage relief is 15% of TRY 28,075.50, which is TRY 4,211.33. Income tax withheld is TRY 57,370.58. Stamp tax is 0.759% of TRY 366,970 (the wage above the gross minimum wage): TRY 2,785.30. Net pay is TRY 295,253.62. The employer's premiums are on the ceiling too: 19.75% SGK and 2% unemployment, TRY 64,656.23 in total.

```oa-check
name: January pay TRY 400,000, premiums capped at the 2026 ceiling
inputs:
  gross: 400000
  min_wage: 33030
steps:
  - base: min(gross, min_wage * 9)
  - emp_sgk: base * 0.14
  - emp_ui: base * 0.01
  - taxable: gross - emp_sgk - emp_ui
  - band_15: min(taxable, 190000) * 0.15
  - band_20: max(min(taxable, 400000) - 190000, 0) * 0.20
  - band_27: max(min(taxable, 1500000) - 400000, 0) * 0.27
  - tax_before: band_15 + band_20 + band_27
  - exempt_base: min_wage - min_wage * 0.15
  - relief: exempt_base * 0.15
  - income_tax: tax_before - relief
  - stamp: max(gross - min_wage, 0) * 0.00759
  - net: gross - emp_sgk - emp_ui - income_tax - stamp
  - employer_premiums: base * (0.12 + 0.0225 + 0.075 - 0.02 + 0.02)
expected:
  base: 297270
  taxable: 355409.50
  tax_before: 61581.90
  income_tax: 57370.58
  stamp: 2785.30
  net: 295253.62
  employer_premiums: 64656.23
```

## Ask the client first

1. Is each worker an employee (4/1-a) or self-employed (4/1-b)? Any civil servants, apprentices or students?
2. What is each employee's gross monthly pay, and what was their cumulative taxable wage earlier in the year (new hires part-way through the year)?
3. Does any employee have a second employer, and which pays more?
4. Do you pay meal, transport or nursery benefits, and how (cash, card, direct to the provider)?
5. How many employees do you have (10 or fewer can file quarterly), and are you private sector and up to date with SGK (for the 2-point incentive)?
6. Does anyone work abroad, or come from abroad on a posting?

## Sources

| Source | URL | Read on |
|---|---|---|
| Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu no. 5510, consolidated (to Law 7590): arts. 4, 81, 82, 86, 88, 89, 102 and amendment table (Law 7566 in force 1 January 2026) | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5510.pdf | 2026-10-31 |
| İşsizlik Sigortası Kanunu no. 4447, art. 49 | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.4447.pdf | 2026-10-31 |
| Asgari Ücret Tespit Komisyonu Kararı 2025/1, Official Gazette 26 December 2025 no. 33119 | https://www.resmigazete.gov.tr/eskiler/2025/12/20251226-6.pdf | 2026-10-31 |
| Gelir Vergisi Kanunu no. 193, consolidated (2026 amounts from Communiqué 332): arts. 23, 31, 63, 94, 98, 98/A, 103, 104, 119 | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.193.pdf | 2026-10-31 |
| Damga Vergisi Kanunu no. 488, tables 1 (IV-1(b)) and 2 (IV-34) | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.488.pdf | 2026-10-31 |
| GİB, Beyanname verme ve ödeme süreleri | https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2FBeyannameVermeveOdemeSureleri.pdf | 2026-10-31 |
| Vergi Usul Kanunu no. 213 (arts. 344, 352, table 1) and Law 6183 (art. 51) | https://www.mevzuat.gov.tr/MevzuatMetin/1.5.213.pdf | 2026-10-31 |

Not yet confirmed: the official net minimum wage (TRY 28,075.50 here is computed from the gross and the 15% employee premiums, with no income or stamp tax); the SGK circular for 2026 (2026/2) and its figures, which were not read on sgk.gov.tr (floor and ceiling here are computed from art. 82 and the daily minimum wage); the minimum wage support of TRY 1,270 a month proposed in decision 2025/1 and its legal basis; the day SGK sets for premium payment (art. 88); the GİB communiqué on the cumulative withholding method; the severance pay (kıdem tazminatı) ceiling for 2026 (the old version gave TRY 46,655.43 for 2025 from a non-official site); the 4/1-b premium base rules and minimum base; sector incentives (manufacturing, youth, women, regional and others) and whether any reduce the employer rate further in 2026; the list of social security agreements; employer premiums on directors and partners.
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
