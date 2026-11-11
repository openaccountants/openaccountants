---
name: ecuador-social-contributions
description: "Ecuador social security contributions (IESS) for 2026 for people who pay their own: the self-employed (trabajadores autónomos), professionals in private practice, business owners and legal representatives, voluntary affiliates resident in Ecuador and Ecuadorians abroad, unpaid home workers, pensioners and the Seguro Social Campesino. Covers who must be affiliated (Ley de Seguridad Social art. 2), the self-declared materia gravada with its floor of one salario básico unificado (USD 482 for 2026), the 20.60% total rate for independent and voluntary affiliates (IESS Resolución C.D. 501), the 0.10% disability levy, the 13.25% home-work scale with state subsidy, payment within 15 days after the month, automatic exit after 30 days unpaid, mora interest and how employee and employer rates link to payroll. Trigger on: afiliación voluntaria IESS 2026, aporte IESS independiente, afiliado sin relación de dependencia, profesional en libre ejercicio IESS, trabajo no remunerado del hogar, cuánto pago al IESS, Ecuador self-employed social security. Out of scope: employees and employers (ecuador-payroll), income tax (ecuador-income-tax)."
version: 0.2
jurisdiction: EC
tax_year: 2026
last_updated: 2026-11-11
depends_on:
  - social-contributions-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Ecuador: IESS contributions for the self-employed and voluntary affiliates (2026) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill computes what a person who is not someone's employee pays to the Instituto Ecuatoriano de Seguridad Social (IESS) in 2026. It links to the other Ecuador skills and does not repeat them:

- [ecuador-payroll](ecuador-payroll.md): workers in relación de dependencia, the employee 9.45% and employer 11.15% rates, décimos, fondos de reserva and the monthly planilla.
- [ecuador-income-tax](ecuador-income-tax.md): the self-employed person's income tax, RIMPE and the gastos personales rebate.
- [ec-tax-overview](ec-tax-overview.md): Ecuador tax overview, including the position of non-residents.

**Quick reference (2026).** Salario básico unificado (SBU): USD 482. Self-employed, professionals, business owners and voluntary affiliates: 20.60% of the monthly income they declare, never on less than the SBU, so at least 482 × 20.60% = USD 99.29 a month. Paid within 15 days after the month; unpaid for 30 days after the month and the IESS records the affiliate's exit. Unpaid home work: 13.25% on 25% to 100% of the SBU depending on the household's income, with a state subsidy on the lower tiers.

**Which texts.** Ley de Seguridad Social (Ley 55, RO Supl. 465 of 30 Nov 2001, IESS copy with last reform 26 June 2025); IESS Consejo Directivo Resolución C.D. 467 (Reglamento de afiliación de las personas sin relación de dependencia o independientes y ecuatorianos domiciliados en el exterior) and C.D. 501 of 13 November 2015 (consolidated contribution tables); Acuerdo Ministerial MDT-2025-195 (SBU 2026).

## Who this applies to

- **Obliged to be affiliated** (LSS art. 2): everyone who earns income from work or services, with or without an employment relationship: the worker in relación de dependencia (see ecuador-payroll), the self-employed worker (trabajador autónomo), the professional in private practice, the administrator or owner (patrono) of a business, the owner of a sole-proprietor company (empresa unipersonal), the independent minor worker, people doing unpaid home work, and others obliged by special laws or decrees.
- **Voluntary affiliation** (C.D. 467 arts. 1, 7): people with income without an employment relationship domiciled in Ecuador, and Ecuadorians aged 18 or over domiciled abroad (or Ecuadorian scholarship holders abroad), from the day they apply through the IESS website. They need a cédula (a foreigner in Ecuador a cédula de identidad, a refugee the refugee card; abroad, a cédula or Ecuadorian passport) and no arrears with the IESS (arts. 2, 8).
- **Ecuadorians abroad** may contribute at the same time to their country of residence's social security (C.D. 467 art. 13).
- **Seguro Social Campesino**: artisanal fishers and rural dwellers who habitually work the land on their own account or for their community and employ nobody from outside it (LSS art. 2, second paragraph).
- **Out of scope**: employees and their employers (ecuador-payroll), the military and police schemes (ISSFA, ISSPOL), additional insurance for unhealthy work.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Salario básico unificado (SBU) | USD 482.00 a month from 1 January 2026 | 2026 | https://www.trabajo.gob.ec/wp-content/uploads/downloads/2026/01/ACUERDO-MINISTERIAL-MDT-2025-195.pdf (Acuerdo MDT-2025-195) |
| Self-employed, independent workers, voluntary affiliates resident in Ecuador, interns, scholarship holders, rotating interns and voluntary affiliates abroad: total rate, paid by the affiliate | 20.60% of materia gravada (pensions 10.46, disability law 0.10, health 5.16, work risks 0.38, cesantía 3.00, Seguro Social Campesino 0.70, administration 0.80 in the table for 2021 onwards) | 2026 | https://iess.gob.ec/documents/10162/33703/C.D.+501 (C.D. 501 art. 1, Sexta, and annex "año 2021 en adelante") |
| Materia gravada of an independent or voluntary affiliate | the monthly amount the affiliate declares as equivalent to their pay; never below the SBU; may be raised or lowered (to the minimum) at any time | 2026 | https://www.iess.gob.ec/documents/10162/33703/C.D.+467 (C.D. 467 arts. 4, 10) |
| Minimum base for every affiliate | the SBU; part-time affiliation uses the proportional SBU | 2026 | same (C.D. 467, Disposición General Primera) |
| Minimum monthly contribution, independent or voluntary affiliate | 482 × 20.60% = USD 99.29 | 2026 | same (computed from the C.D. 501 and C.D. 467 rows above) |
| Ley Orgánica de Discapacidades levy | 0.10% of materia gravada, paid by every affiliate (inside the 20.60%) | 2026 | same (Disposición General Segunda); https://www.iess.gob.ec/es/web/empleador/tasas-de-aportacion |
| Extra voluntary saving for cesantía | the affiliate may raise the cesantía contribution above the 3.00% minimum and lower it back at any time | 2026 | same (Disposición General Cuarta; Disposiciones Reformatorias, cesantía marked "valor mínimo") |
| Unpaid home work, household income below 50% of the SBU | 13.25% on 25% of the SBU: affiliate 2.26%, state subsidy 10.99% | 2026 | https://iess.gob.ec/documents/10162/33703/C.D.+501 (C.D. 501 art. 1, Séptima) |
| Unpaid home work, 50% to under 100% of the SBU | 13.25% on 50% of the SBU: affiliate 5.3%, subsidy 7.95% | 2026 | same |
| Unpaid home work, 100% to under 150% of the SBU | 13.25% on 75% of the SBU: affiliate 7.3%, subsidy 5.95% | 2026 | same |
| Unpaid home work, 150% of the SBU or more | 13.25% on 100% or more of the SBU, all paid by the affiliate | 2026 | same |
| IESS pensioners (jubilados) | 2.76% of the unified pension; widow(er) pensioners 4.15% for health cover; spouse cover 4.15%, children under 18 3.41% on request | 2026 | same (C.D. 501 art. 3) |
| Seguro Social Campesino family contribution | between 2% and 3% of the fraction of the dependent workers' minimum contribution salary, as the LSS General Regulation sets | 2026 | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social (LSS art. 15, last paragraph) |
| Late payment interest (mora) | Banco Central del Ecuador maximum conventional rate at the settlement date plus 4 points | 2026 | same (LSS art. 89) |

## The base

**The legal basis.** For an independent affiliate the contribution is calculated on the Base Presuntiva de Aportación (BPA) or the materia gravada, at the percentages set by the LSS and varied periodically on independent actuarial studies (LSS arts. 13, 15). Where income is hard to establish, the IESS defines a presumptive base each year for the main categories, as multiples of the minimum contribution salary (LSS art. 13). C.D. 467 lets the independent or voluntary affiliate declare the monthly amount, with the SBU as the floor (arts. 4, 10; Disposición General Primera).

**Not materia gravada** (LSS art. 14): meals, medical cover, life and accident premiums, work clothes and tools and social services paid by an employer (together at most 20% of contributable pay), profit sharing and the compensación para el salario digno. These matter mainly for employees.

**The computation, each month.**

1. Decide the affiliate's group: independent or voluntary (C.D. 501 Sexta), unpaid home work (Séptima), pensioner (art. 3), or employee (ecuador-payroll).
2. Independent or voluntary: base = the amount declared, at least USD 482 (or the proportional SBU if part time).
3. Contribution = base × 20.60%, plus any extra cesantía saving the affiliate chose.
4. Unpaid home work: find the household's tier against the SBU; the base is 25%, 50%, 75% or 100% of the SBU; the affiliate pays its share and the state pays the subsidy.
5. Pay within 15 days after the month (LSS art. 73). If no payment is recorded within 30 days after the month, the IESS records the exit automatically (C.D. 467 arts. 3, 9).

**Benefits follow the base.** Under the congruence principle every part of the income that enters the calculation and payment of benefits is materia gravada (LSS art. 12(a)). A higher declared base costs more each month and feeds the benefits computed on it.

## Deadlines and filing

| Item | Deadline | Source URL |
|---|---|---|
| Enrol (aviso de entrada) as a voluntary or independent affiliate | from the day of the application on the IESS website | https://www.iess.gob.ec/documents/10162/33703/C.D.+467 (C.D. 467 arts. 1, 7) |
| Pay contributions | within 15 days after the month the contributions relate to | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social (LSS art. 73) |
| Self-employed culture workers who chose four-monthly payment | within 15 days after each four-month period | same (LSS art. 73) |
| Automatic exit if unpaid | no payment recorded within 30 days after the month | https://www.iess.gob.ec/documents/10162/33703/C.D.+467 (C.D. 467 arts. 3, 9) |
| Leave voluntarily (aviso de salida) | any time, on the IESS website; re-enrol with a new aviso de entrada once there are no arrears | same (arts. 3, 9) |
| Due date on a Saturday, Sunday or rest day | the next business day | https://www.iess.gob.ec/es/web/empleador/mora-patronal |
| Unpaid home workers | affiliated from the date of their application; they keep their workplace and socio-economic data up to date | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social (LSS art. 73) |

**How to affiliate and pay, step by step.**

1. Get the IESS personal password (clave) through the IESS website; every affiliate has free access to their work history (C.D. 467, Disposición General Quinta).
2. In the IESS online services, file the aviso de entrada as an independent or voluntary affiliate and declare the monthly materia gravada (at least the SBU).
3. The system generates the monthly contribution. Pay it within 15 days after the month through the payment channels the IESS offers.
4. To change the base, update it online; it can go up at any time or down to the SBU (C.D. 467 art. 4).
5. Check the work history each year: unpaid months create mora and, after 30 days, an automatic exit.

## Penalties and interest

| Item | Rule | Source URL |
|---|---|---|
| Late contributions | interest at the Banco Central del Ecuador maximum conventional rate at the settlement date plus 4 points | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social (LSS art. 89) |
| Mora generally | the employer and the voluntary affiliate must pay within the deadlines; mora creates liability for benefits in health, pensions, work risks and cesantía | https://www.iess.gob.ec/es/web/empleador/mora-patronal |
| Unpaid for 30 days after the month | automatic exit from voluntary or independent affiliation | https://www.iess.gob.ec/documents/10162/33703/C.D.+467 (C.D. 467 arts. 3, 9) |
| Re-entering after an exit | only with no arrears or pending obligations with the IESS | same (arts. 2(b), 8(c)) |
| Paying arrears | partial-payment agreements up to 12 months, 13 to 24 months, and purga de mora agreements | https://www.iess.gob.ec/es/web/empleador/mora-patronal |

## Cross-border points

- **Ecuadorians domiciled abroad** may affiliate voluntarily and contribute on a declared base of at least the SBU, at the same time as contributing in their country of residence (C.D. 467 arts. 7 to 13). Benefits are paid by bank transfer abroad (art. 11). On moving back to Ecuador they file an exit or ask to be moved to the right scheme (art. 12).
- **Foreigners** in Ecuador with independent income can affiliate voluntarily with a cédula de identidad (C.D. 467 art. 2(a)); refugees with the refugee card.
- Social security agreements between Ecuador and other countries were not read for this skill.

## Two worked examples that recompute

### Example 1: professional in private practice, declared base USD 1,500

Lucía is an architect in private practice in Cuenca. She declares a monthly materia gravada of USD 1,500, which is above the SBU.

- Contribution: 1,500 × 20.60% = **USD 309.00** a month, due within 15 days after each month.
- Of which the disability levy: 1,500 × 0.10% = **USD 1.50**, and the cesantía minimum: 1,500 × 3.00% = **USD 45.00**.
- Year: 309 × 12 = **USD 3,708.00**.

```oa-check
name: EC IESS 2026, independent affiliate, declared base USD 1,500
inputs:
  declared: 1500
  sbu: 482
  rate: 0.206
steps:
  - base: max(declared, sbu)
  - monthly: base * rate
  - lod: base * 0.001
  - cesantia: base * 0.03
  - yearly: monthly * 12
expected:
  base: 1500
  monthly: 309.00
  lod: 1.50
  cesantia: 45.00
  yearly: 3708.00
```

### Example 2: declare the SBU or the real income? (a decision worked both ways)

Andrés is a freelance designer with about USD 1,000 a month of income. He is choosing between the minimum base and his real income.

- **Declare the SBU (USD 482):** 482 × 20.60% = **USD 99.29** a month, USD 1,191.48 a year.
- **Declare USD 1,000:** 1,000 × 20.60% = **USD 206.00** a month, USD 2,472.00 a year.
- Difference: **USD 106.71** a month, **USD 1,280.52** a year.

What decides it: the floor is the SBU (C.D. 467 art. 4), so declaring less than USD 482 is not an option, and anything above is his choice. The extra cost buys benefits computed on a higher base (LSS art. 12(a)). If he later hires staff or takes a job, those earnings follow ecuador-payroll instead.

```oa-check
name: EC IESS 2026, voluntary affiliate, SBU base vs USD 1,000 base
inputs:
  sbu: 482
  income: 1000
  rate: 0.206
steps:
  - min_monthly: round(sbu * rate, 2)
  - min_yearly: min_monthly * 12
  - real_monthly: round(income * rate, 2)
  - real_yearly: real_monthly * 12
  - diff_monthly: real_monthly - min_monthly
  - diff_yearly: real_yearly - min_yearly
expected:
  min_monthly: 99.29
  min_yearly: 1191.48
  real_monthly: 206.00
  real_yearly: 2472.00
  diff_monthly: 106.71
  diff_yearly: 1280.52
```

## Ask the client first

1. Is the person an employee of anyone (then ecuador-payroll), or self-employed, a professional, a business owner, a voluntary affiliate, an unpaid home worker or a pensioner?
2. Domiciled in Ecuador or abroad? Ecuadorian, foreign resident or refugee?
3. What monthly base will they declare (at least USD 482), and do they want extra cesantía saving?
4. For unpaid home work: the household's monthly income against the SBU.
5. Any unpaid months or arrears with the IESS (they block re-entry and create mora)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Acuerdo Ministerial MDT-2025-195 (15 Dec 2025): SBU USD 482 from 1 Jan 2026 | https://www.trabajo.gob.ec/wp-content/uploads/downloads/2026/01/ACUERDO-MINISTERIAL-MDT-2025-195.pdf | 2026-11-11 |
| IESS Resolución C.D. 467: arts. 1 to 15, Disposiciones Generales and Reformatorias read | https://www.iess.gob.ec/documents/10162/33703/C.D.+467 | 2026-11-11 |
| IESS Resolución C.D. 501 (13 Nov 2015): art. 1 Sexta and Séptima, art. 3, annexes read | https://iess.gob.ec/documents/10162/33703/C.D.+501 | 2026-11-11 |
| IESS, Tasas de aportación page (0.10% LOD note) | https://www.iess.gob.ec/es/web/empleador/tasas-de-aportacion | 2026-11-11 |
| Ley de Seguridad Social, IESS copy (last reform 26 Jun 2025): arts. 2, 11 to 15, 73, 89 read | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social | 2026-11-11 |
| IESS, Mora patronal page | https://www.iess.gob.ec/es/web/empleador/mora-patronal | 2026-11-11 |

Not yet confirmed: the 17.60% voluntary rate in the old version (it came from PwC and a university page; C.D. 501 Sexta gives 20.60% for independent and voluntary affiliates, and no later Consejo Directivo resolution changing it was read; the IESS voluntary-affiliation page returned "content no longer exists"); whether any Consejo Directivo resolution after 2015 changed C.D. 501's tables; the presumptive bases (BPA) under LSS art. 13 for 2026, if any are set; the IECE and SECAP 0.5% levies (old version, no primary source); the extra 0.1% disability-pension rate the old version doubted (C.D. 467 and C.D. 501 put the 0.10% inside the totals); the Seguro Social Campesino percentages actually set by the General Regulation; social security agreements.
