---
name: honduras-payroll
description: >
  Use this skill to run Honduras payroll for employees in 2026. It covers the employer's
  monthly ISR withholding on the SAR 2026 progressive scale (exempt to L228,324.32 a year),
  the remittance of retentions within 10 calendar days of the following month, the 13th
  month (aguinaldo) and 14th month salaries with their ISR exemption of 10 average minimum
  wages each (L149,172.00 in 2026), the 2026 minimum wage table of Acuerdo SETRASS-233-2026
  (average L14,917.20 a month) and the employee's annual position. IHSS and RAP rates live
  in honduras-social-contributions. Trigger phrases include planilla Honduras, retencion
  ISR asalariados codigo 111, aguinaldo, decimo cuarto mes, salario minimo 2026 Honduras
  and net salary Honduras.
version: "1.0"
jurisdiction: HN
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Honduras payroll, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Honduran accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Honduras.

## Who this applies to

Employers in Honduras paying salaries to employees in 2026: the monthly ISR withholding, the 13th and 14th month salaries, minimum wage checks and the monthly retention return. Contribution rates and ceilings for IHSS and RAP are in [honduras-social-contributions](honduras-social-contributions.md); the employee's own annual return is in [honduras-income-tax](honduras-income-tax.md).

Refer to a Honduran accountant: employees of free zone companies with special agreements, expatriates who are not domiciled (art. 5 flat 25% on salaries), severance and termination settlements (prestaciones laborales), and employers with arrears at SAR, IHSS or RAP.

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Gross monthly salary unknown | Stop; do not compute |
| Domicile of the employee unknown | Stop; a non-domiciled employee is withheld 25% on gross (art. 5) |
| Sector or size for the minimum wage unknown | Check against the highest band of the sector |
| 13th or 14th month above the exempt cap | Tax the excess with the regular salary |
| Employee has other income | Withhold on salary only; the employee files Form 102 |

Wages are paid in lempiras.

## Rates, bands and thresholds

**ISR withholding scale for 2026 (annual renta neta gravable).** The same scale as the annual return; SAR orders retention agents to use it from 1 January 2026.

| Band | From (L) | To (L) | Rate | Source |
| --- | --- | --- | --- | --- |
| 1 | 0.01 | 228,324.32 | Exempt | SAR Acuerdo SAR-01-2026: https://www.sar.gob.hn/download/acuerdo-numero-sar-01-2026-publicado-en-fecha-23-de-enero-del-2026-en-la-gaceta-no-37051/?wpdmdl=22954 |
| 2 | 228,324.33 | 348,154.10 | 15% | same |
| 3 | 348,154.11 | 809,660.75 | 20% | same |
| 4 | 809,660.76 | and above | 25% | same |

**Other payroll figures.**

| Item | Amount | Condition | Source |
| --- | --- | --- | --- |
| Remittance of ISR retentions | Within the first 10 calendar days of the following month | Declaracion jurada of retentions (Codigo 111 for salaries) | SAR Ayuda retencion asalariados Codigo 111: https://www.sar.gob.hn/download/ayuda-rentencion-asalariados-art-22-ley-isr-codigo-111/?wpdmdl=20533 |
| Flat deduction for education and medical fees | L40,000 a year (L80,000 over 65) | Deducted from the annual projection | SAR Ayuda Form 102 (2026): https://www.sar.gob.hn/download/ayuda-declaracion-jurada-impuesto-sobre-la-renta-102/?wpdmdl=22532 |
| ISR exemption of the 13th and 14th month | 10 average minimum wages each | Excess is taxable | same |
| Average minimum wage 2026 | L14,917.20 a month | Acuerdo SETRASS-233-2026, La Gaceta 37,129 of 29 April 2026, in force from 1 January 2026 | Secretaria de Trabajo, Tabla 2026: https://www.trabajo.gob.hn/wp-content/uploads/2026/05/TABLA-SALARIO-MINIMO-2026-.pdf |
| So, exempt cap for each of the 13th and 14th month in 2026 | L149,172.00 | 10 x L14,917.20 | same |
| Lowest minimum wage 2026 | L9,596.64 a month | Agriculture, forestry, hunting and fishing, 1 to 10 workers | same |
| Highest minimum wage 2026 | L19,298.72 a month | Financial establishments, real estate and business services, 151 or more workers | same |
| Commerce, 1 to 10 workers | L13,292.06 a month | Wholesale and retail trade | same |
| Commerce, 151 or more workers | L18,786.37 a month | Wholesale and retail trade | same |
| Manufacturing, 1 to 10 workers | L12,869.14 a month | Industria manufacturera | same |
| Free zone companies | L12,930.07 a month | Acuerdo SETRASS-109-2024 | same |

## The base

1. **Project the year.** Annual taxable salary = 12 regular months plus the 13th and 14th month above their caps, less the L40,000 flat deduction (or L80,000), less contributions deductible under LISR art. 10 h (pension contributions; SAR's Form 102 guide names the RAP 1.5%).
2. **Apply the 2026 scale** to the projected renta neta gravable; divide the annual tax by 12 for the monthly retention, and re-project when pay changes.
3. **13th month (aguinaldo)** is paid in December and the **14th month** mid-year; each is exempt from ISR up to L149,172.00 in 2026 (LISR art. 10 h).
4. **Withhold and remit** by the 10th of the following month through the Oficina Virtual; the retention is a credit for the employee.
5. **Contributions** (IHSS IVM, RAP) are computed separately; see the social contributions skill.

An employee with one employer whose ISR was fully withheld need not file Form 102 (LISR art. 28).

## Deadlines and filing

| Obligation | Deadline | Channel |
| --- | --- | --- |
| ISR retention on salaries, monthly | Within 10 calendar days of the following month | Declaracion jurada of retentions, Codigo 111, Oficina Virtual (OVI); payment by boletin de pago |
| Declaracion Mensual de Retenciones (DMR) | Monthly | OVI |
| 13th month | December | Paid to employee |
| 14th month | Mid-year; exact legal date not confirmed | Paid to employee |
| IHSS and RAP | Monthly | See honduras-social-contributions |
| Employee annual return, if any | 30 April 2027 | Form 102 |

## Penalties and interest

Retained ISR not remitted on time: 5% interest a month or part month, up to 60% (Codigo Tributario art. 163.2), and the employer is jointly liable for tax it failed to retain (LISR art. 51). Late retention returns are formal faults fined by the employer's gross income band (CT art. 160.1). Voluntary correction reduces the fine (art. 162).

## Cross-border points

A non-domiciled employee or a person paid for services from abroad bears a final 25% on Honduran-source pay (LISR art. 5(3)), withheld by the payer. Temporary residents may file before leaving (art. 4). Treaty relief was not confirmed.

## Two worked examples that recompute

### Example 1: monthly retention for a L40,000 salary, 2026

Regular salary L40,000 a month (L480,000 a year); 13th and 14th month L40,000 each, both inside the L149,172.00 cap. Projected renta neta gravable L440,000 after the L40,000 deduction. Annual ISR L36,343.65; monthly retention L3,028.64.

```oa-check
name: HN 2026 payroll, L40,000 monthly salary
inputs:
  monthly: 40000
  flat_deduction: 40000
  cap_13_14: 149172
  top1: 228324.32
  top2: 348154.10
steps:
  - bonus_taxable: max(monthly - cap_13_14, 0) * 2
  - annual_taxable: monthly * 12 + bonus_taxable - flat_deduction
  - annual_tax: round((top2 - top1) * 0.15 + (annual_taxable - top2) * 0.20, 2)
  - monthly_retention: round(annual_tax / 12, 2)
expected:
  bonus_taxable: 0
  annual_taxable: 440000
  annual_tax: 36343.65
  monthly_retention: 3028.64
```

### Example 2: a senior manager's aguinaldo, taxed or not (decision)

A manager earns L160,000 a month. The aguinaldo of L160,000 exceeds the 2026 cap of L149,172.00 by L10,828.00, so L10,828.00 joins the taxable base, and so does L10,828.00 of the 14th month. A manager earning L149,000 a month would have no taxable excess. The cap of 10 average minimum wages decides it; the old version of this skill treated both salaries as fully exempt, which was wrong.

```oa-check
name: HN 2026 13th month above the cap
inputs:
  salary_a: 160000
  salary_b: 149000
  min_wage_avg: 14917.20
steps:
  - cap: min_wage_avg * 10
  - excess_a: max(salary_a - cap, 0)
  - excess_b: max(salary_b - cap, 0)
  - taxable_added_a: excess_a * 2
expected:
  cap: 149172
  excess_a: 10828
  excess_b: 0
  taxable_added_a: 21656
```

## Ask the client first

1. Each employee's gross monthly salary, start date and domicile.
2. Economic sector and number of workers (for the minimum wage band).
3. 13th and 14th month amounts and payment dates.
4. Other deductions the employee claims (over 65, pension contributions).
5. RTN of the employer and whether it already files the monthly retention return.
6. Any employee paid from abroad or in a free zone.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the 2026 ISR scale and the order to retention agents, Acuerdo SAR-01-2026 arts. primero and segundo | https://www.sar.gob.hn/download/acuerdo-numero-sar-01-2026-publicado-en-fecha-23-de-enero-del-2026-en-la-gaceta-no-37051/?wpdmdl=22954 | 2026-11-14 |
| Read for SAR Ayuda retencion asalariados art. 22 (Codigo 111): monthly remittance within 10 calendar days, boletin de pago | https://www.sar.gob.hn/download/ayuda-rentencion-asalariados-art-22-ley-isr-codigo-111/?wpdmdl=20533 | 2026-11-14 |
| Read for SAR Ayuda Form 102 (2026): art. 13 deductions, the 13th and 14th month cap, RAP 1.5% deduction | https://www.sar.gob.hn/download/ayuda-declaracion-jurada-impuesto-sobre-la-renta-102/?wpdmdl=22532 | 2026-11-14 |
| Read for the 2026 minimum wage table, all 12 sectors and the average, Acuerdo SETRASS-233-2026 | https://www.trabajo.gob.hn/wp-content/uploads/2026/05/TABLA-SALARIO-MINIMO-2026-.pdf | 2026-11-14 |
| Read for LISR consolidated text, arts. 4, 5, 10 h, 28 and 51 | https://www.sar.gob.hn/download/ley-isr-texto-consolidado-hasta-el-acuerdo-no-sar-014-2023/?wpdmdl=17388 | 2026-11-14 |
| Read for Codigo Tributario consolidated, arts. 160, 162 and 163 | https://www.sar.gob.hn/download/texto-consolidado-codigo-tributario-decreto-170-2016-segun-fe-de-errata-publicada-en-la-gaceta-de-fecha-25-de-mayo-del-2017-y-los-decretos-25-2017-7-2017-32-2017-93-2017-98-2018-55-2019-170-2/?wpdmdl=6987 | 2026-11-14 |

Not yet confirmed: the legal payment dates of the 13th and 14th month (Codigo de Trabajo and the 14th month law not read); whether IHSS contributions are deductible in the ISR projection; the INFOP training levy rate and threshold (no official page read; see honduras-social-contributions); the municipal personal tax withheld by employers (Ley de Municipalidades not read); overtime and vacation rules.
