---
name: us-ma-payroll
description: Run Massachusetts employer payroll for 2026. Covers state income tax withholding under the January 2026 Circular M (5%, and 9% on annualized wages above $1,107,750), the $2,000 FICA deduction and exemption factors, supplemental wages, unemployment insurance (the $15,000 taxable wage base, 2.42% new employer rate, 6.08% new construction rate, Schedule E rates with the COVID-19 recovery assessment), the employer medical assistance contribution (EMAC), and Paid Family and Medical Leave (PFML) contributions of 0.88% for 2026, with quarterly reporting. Trigger on "Massachusetts payroll", "MA withholding", "Circular M", "M-4", "Massachusetts unemployment insurance", "DUA contribution rate", "EMAC", "PFML contribution", "Massachusetts paid leave". Federal payroll is in us-form-941-940-payroll.
version: "1.0"
jurisdiction: US-MA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Massachusetts payroll: withholding, unemployment insurance, EMAC and PFML, 2026

> **Source-cited draft.** Built from the DOR Circular M effective 1 January 2026, the DOR 4% surtax page, the Department of Unemployment Assistance (DUA) pages on employer contributions and EMAC, the DUA 2026 UI and COVID-19 Recovery Assessment rate schedule, the Department of Family and Medical Leave (DFML) contribution rates page, and M.G.L. c. 151A, s. 14, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** A Massachusetts employer withholds state income tax at **5%** of annualized wages after a deduction of up to **$2,000** a year for FICA and similar contributions and **$4,400** for one exemption (more per extra exemption), and **9%** on annualized wages above **$1,107,750**. It pays state unemployment insurance (UI) on the first **$15,000** of each employee's wages: **2.42%** for a new employer (6.08% in construction), or its DUA-assigned rate, plus the COVID-19 recovery assessment built into the effective rate. From the fourth year it also pays EMAC on the same $15,000 (0.12% to 0.34%). PFML contributions for 2026 are **0.88%** of eligible wages for employers with 25 or more covered individuals and **0.46%** for smaller employers, which can withhold all of the smaller-employer amount from wages.

## Scope

| Field | Value |
| --- | --- |
| Jurisdiction | Massachusetts (US-MA), [DOR](https://www.mass.gov/orgs/massachusetts-department-of-revenue) |
| Withholding | DOR, M.G.L. c. 62B, [Circular M 2026](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) |
| Unemployment insurance and EMAC | DUA, M.G.L. c. 151A, [UI Online for employers](https://unemployment.mass.gov/Employers/_/) |
| Paid Family and Medical Leave | DFML, M.G.L. c. 175M, [PFML contribution rates](https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator) |

Covers private employers with Massachusetts employees. Not covered: federal income tax withholding, FICA and FUTA (`us-form-941-940-payroll`), private PFML plan exemptions, domestic and agricultural employers beyond their thresholds, the employee's own return (`ma-income-tax`), and Massachusetts new hire reporting detail (`us-state-new-hire-reporting-matrix`).

## Ask the client first

1. When the business first became liable for Massachusetts UI (new employer under 3 years, or established), and whether it is in construction.
2. The 2026 DUA rate notice, if established (sent by 31 January).
3. Number of covered individuals for PFML (25 or more, or fewer).
4. Each employee's Form M-4 (exemptions, head of household, blindness) and pay frequency.
5. Any bonuses or other supplemental pay, and any employee likely to earn above $1,107,750.
6. Registrations in place: DOR withholding account on MassTaxConnect, DUA account, DFML account.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Condition | Source |
| --- | --- | --- | --- |
| Withholding rate | 5% | Annualized wages after deductions up to $1,107,750 | [Circular M 2026](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) |
| Withholding rate above the surtax threshold | 9% | Annualized wages after deductions above $1,107,750 | [Circular M 2026](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) |
| FICA, Medicare and public retirement deduction | Up to $2,000 a year | Stop once $2,000 has been deducted in the year | [Circular M 2026](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) |
| Exemption factor, 1 exemption | $4,400 a year ($85 weekly, $169 biweekly, $183 semimonthly, $367 monthly) | Employee claiming 1 | [Circular M 2026](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) |
| Exemption factor, more than 1 | $1,000 times the number claimed, plus $3,400 a year | A claimed spouse counts as 4 exemptions | [Circular M 2026](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) |
| Head of household tax value | $120 a year ($2.31 weekly) | Employee will file as head of household | [Circular M 2026](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) |
| Blindness tax value | $110 a year ($2.12 weekly) | Employee or spouse blind | [Circular M 2026](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) |
| No withholding floor | Wages under $8,000 a year ($154 weekly) | Employee claiming 1 or more exemptions | [Circular M 2026](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) |
| Supplemental wages | 5%, or 9% on the part where supplemental plus prior supplemental plus annualized regular wages exceed $1,107,750 | Bonuses and other supplemental pay | [DOR 4% surtax](https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000) |
| UI taxable wage base | $15,000 per employee per year | Calendar years from 2015 | [M.G.L. c. 151A, s. 14](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXI/Chapter151A/Section14) |
| UI new employer rate | 2.42% | Registered less than 3 years | [DUA employer contributions](https://www.mass.gov/info-details/employer-contributions-to-unemployment) |
| UI new construction employer rate | 6.08% | New construction industry employer | [DUA employer contributions](https://www.mass.gov/info-details/employer-contributions-to-unemployment) |
| UI experienced rates, Schedule E | 0.94% to 14.37% UI; effective rate with the COVID-19 recovery assessment 1.118% to 17.086% | Set by the reserve percentage on the DUA rate notice | [DUA 2026 rate schedule](https://www.mass.gov/doc/ui-and-covid-recovery-assessment-rates/download) |
| UI liability test | 1 or more employees for 13 weeks, or $1,500 of wages in a quarter | Most private employers; $200 in a quarter for out-of-state employers | [DUA employer contributions](https://www.mass.gov/info-details/employer-contributions-to-unemployment) |
| EMAC rate | Years 1 to 3 exempt; year 4 0.12%; year 5 0.24%; year 6 on 0.34% | First $15,000 of each employee's wages | [DUA EMAC](https://www.mass.gov/info-details/employer-medical-assistance-contribution-emac) |
| PFML, 25 or more covered individuals | 0.88% of eligible wages: family 0.18% (all may be withheld), medical 0.70% (up to 0.28% withheld, employer pays 0.42%) | 2026 | [DFML contribution rates](https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator) |
| PFML, fewer than 25 covered individuals | 0.46% of eligible wages, all of which may be withheld | 2026; no employer medical share | [DFML contribution rates](https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator) |
| PFML wage cap | Social Security taxable maximum (figure in `us-form-941-940-payroll`) | Per individual | [DFML contribution rates](https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator) |
| Late UI payment interest | 12% | Until paid | [DUA employer contributions](https://www.mass.gov/info-details/employer-contributions-to-unemployment) |

### Step 1. Register

Register for withholding on MassTaxConnect, with DUA once the UI liability test is met, and with DFML for PFML.

### Step 2. Withhold income tax each pay period (percentage method)

1. From the period's wages subtract FICA, Medicare and public retirement deductions until $2,000 has been subtracted in the year.
2. Subtract the exemption factor for the period (none if 0 claimed).
3. Annualize: times 52, 26 (or 27), 24 or 12.
4. Tax: 5% of the annualized amount up to $1,107,750, plus 9% of any excess.
5. Divide by the number of periods; subtract the head of household and blindness tax values where they apply. The wage-bracket tables in Circular M give the same result for ordinary wages.

### Step 3. Supplemental wages

Add the supplemental payment (after exemptions per Circular M), earlier supplemental payments this year, and annualized regular wages. If the sum is at or below $1,107,750, withhold 5%. If above, withhold the lesser of 9% of the payment, or 9% of the amount by which the sum exceeds the threshold plus 5% of the rest of the payment.

### Step 4. Unemployment insurance, COVID-19 recovery assessment and EMAC

Apply the UI rate (new employer, or the rate notice) to each employee's first $15,000 of wages. Established employers apply the 2026 effective rate (UI plus COVID-19 recovery assessment) from the Schedule E table. Add EMAC from the fourth year at the rate for the employer's year.

### Step 5. PFML

Apply 0.88% (25 or more covered individuals) or 0.46% (fewer) to eligible wages up to the Social Security maximum, split between employee withholding and employer share as the table allows.

### Step 6. Report and pay

Quarterly employment and wage detail report to DUA with UI, EMAC and PFML contributions; DOR withholding returns and payments on MassTaxConnect.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Children under 18 working for a parent, a spouse working for a spouse, a parent working for a child | Wages exempt from UI | [DUA employer contributions](https://www.mass.gov/info-details/employer-contributions-to-unemployment) |
| Real estate broker or insurance agent commissions | Exempt from UI | [DUA employer contributions](https://www.mass.gov/info-details/employer-contributions-to-unemployment) |
| Domestic employer | UI from $1,000 of cash wages in a quarter | [DUA employer contributions](https://www.mass.gov/info-details/employer-contributions-to-unemployment) |
| Agricultural employer | UI from $40,000 of wages in a quarter or 10 or more employees for 20 weeks | [DUA employer contributions](https://www.mass.gov/info-details/employer-contributions-to-unemployment) |
| Cash flow in the first half | Up to 34% of Q1 and Q2 UI contributions may be deferred, if eligible | [DUA employer contributions](https://www.mass.gov/info-details/employer-contributions-to-unemployment) |
| Wrong rate notice | Request a rate review before June 20 | [DUA employer contributions](https://www.mass.gov/info-details/employer-contributions-to-unemployment) |
| PFML for 2027 | Rate stays 0.88% but the split shifts from medical to family leave from 1 January 2027 (Chapter 101 of the Acts of 2026) | [DFML contribution rates](https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator) |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| No Form M-4 | Withhold as for 0 exemptions until one is filed |
| No DUA rate notice and under 3 years | 2.42% (6.08% in construction) |
| Covered individual count unknown | Use the 25 or more rates until counted |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Executive with annualized pay above $1,107,750 | 9% withholding applies above the threshold |
| Large bonus | Supplemental method may need 9% |
| Employer in its fourth year | EMAC starts |
| Headcount crossing 25 | PFML employer share starts |

## Worked cases

**Case 1, annual withholding for a high earner.** A single employee claiming 1 exemption is paid USD 1,200,000 a year in regular wages. FICA deductions far exceed USD 2,000, so USD 2,000 is subtracted, then USD 4,400. Annualized wages after deductions are USD 1,193,600. Withholding is 5% of USD 1,107,750 (USD 55,387.50) plus 9% of USD 85,850 (USD 7,726.50) = USD 63,114 for the year.

```oa-check
name: Circular M 2026 annual withholding above the threshold
inputs:
  annual_wages: 1200000
  fica_deduction: 2000
  exemption_factor: 4400
  threshold: 1107750
steps:
  - annualized: annual_wages - fica_deduction - exemption_factor
  - tax_at_5: min(annualized, threshold) * 0.05
  - tax_at_9: max(annualized - threshold, 0) * 0.09
  - annual_withholding: tax_at_5 + tax_at_9
expected:
  annualized: 1193600.00
  tax_at_5: 55387.50
  tax_at_9: 7726.50
  annual_withholding: 63114.00
```

**Case 2, decision: what a headcount above 25 costs an established employer.** An employer in its sixth year has 30 employees each paid USD 60,000, with a reserve percentage of 10.0 to 10.5 on its rate notice (2026 effective rate 3.044%). UI and COVID-19 assessment on USD 15,000 each: USD 13,698. EMAC at 0.34%: USD 1,530. PFML at 0.88% on USD 1,800,000 of eligible wages: USD 15,840, of which the employer must bear the 0.42% medical share, USD 7,560. With fewer than 25 covered individuals, the 0.46% could all be withheld from wages, so the employer share would be nil.

```oa-check
name: Employer UI, EMAC and PFML cost for 30 employees
inputs:
  employees: 30
  wage_each: 60000
  ui_base: 15000
  effective_ui_rate: 0.03044
  emac_rate: 0.0034
  pfml_rate: 0.0088
  employer_medical_share: 0.0042
steps:
  - ui_and_covid: employees * ui_base * effective_ui_rate
  - emac: employees * ui_base * emac_rate
  - pfml_total: employees * wage_each * pfml_rate
  - pfml_employer_minimum: employees * wage_each * employer_medical_share
  - employer_cost_minimum: ui_and_covid + emac + pfml_employer_minimum
expected:
  ui_and_covid: 13698.00
  emac: 1530.00
  pfml_total: 15840.00
  pfml_employer_minimum: 7560.00
  employer_cost_minimum: 22788.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| REF-MAPR-01 | Private PFML plan exemption | Refer: DFML exemption process |
| REF-MAPR-02 | Pensions, annuities and nonperiodic payments (Form M-4P) | Refer: Circular M payer rules |
| REF-MAPR-03 | Successor employer rate transfer or voluntary UI contributions | Flag for reviewer |
| REF-MAPR-04 | Employees working in more than one state | Flag for reviewer: withholding and UI localization |

## Filing and payment

- **DUA quarterly report and payment** (UI, COVID-19 recovery assessment, EMAC): Q1 by 3 p.m. April 30; Q2 by July 31; Q3 by October 31; Q4 by January 31, through UI Online.
- **DOR withholding:** returns and payments on MassTaxConnect; electronic filing applies to withholding liabilities.
- **PFML:** contributions sent to DFML with the quarterly wage reporting.
- **Rate notices:** DUA sends them by 31 January; review requests before June 20.

## Completion checklist

- [ ] DOR, DUA and DFML registrations in place.
- [ ] M-4 on file for each employee; withholding per Circular M 2026.
- [ ] $2,000 FICA deduction stopped once reached.
- [ ] 9% applied above $1,107,750 on regular and supplemental wages.
- [ ] UI on the first $15,000 at the right rate; COVID-19 recovery assessment included.
- [ ] EMAC from year 4.
- [ ] PFML rate by headcount; employee share not above the allowed split.
- [ ] Quarterly reports filed by the 3 p.m. deadlines.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR, Circular M effective 1 January 2026. Read for the percentage method, $2,000 deduction, exemption factors, $1,107,750 and 9%, head of household and blindness values, the $8,000 floor. | https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download | 2026-11-13 |
| DOR, Massachusetts 4% Surtax on Taxable Income. Read for the supplemental wage method. | https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000 | 2026-11-13 |
| DUA, Employer contributions to unemployment. Read for 2.42%, 6.08%, liability tests, exempt employment, deferral, rate review, due dates and 12% interest. | https://www.mass.gov/info-details/employer-contributions-to-unemployment | 2026-11-13 |
| DUA, 2026 UI and COVID-19 Recovery Assessment Rate Schedule (Schedule E). Read for 0.94% to 14.37% and the effective rates 1.118% to 17.086%, and the 10.0 to 10.5 row (2.56% plus 0.484% = 3.044%). | https://www.mass.gov/doc/ui-and-covid-recovery-assessment-rates/download | 2026-11-13 |
| DUA, Employer medical assistance contribution (EMAC). Read for the $15,000 base and the 0.12%, 0.24% and 0.34% rates. | https://www.mass.gov/info-details/employer-medical-assistance-contribution-emac | 2026-11-13 |
| DFML, PFML employer contribution rates and calculator (updated 1 Oct 2026). Read for 0.88%, 0.46%, the 2026 splits, the Social Security cap and the 2027 change. | https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator | 2026-11-13 |
| M.G.L. c. 151A, s. 14. Read for (a)(4) the $15,000 taxable wage base. | https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXXI/Chapter151A/Section14 | 2026-11-13 |

Not yet confirmed: the DOR withholding return filing frequencies and due dates (Form M-941 thresholds) were not on the pages read; the PFML definition of covered individuals for the 25 count was not read in full.
