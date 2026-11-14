---
name: sx-wage-tax-tables
description: "Sint Maarten wage tax (loonbelasting) withholding for 2026 under Annex II to AB 2026 no. 11. Covers choosing the pay-period table, the column 13 wage-tax base, the nil-withholding thresholds per period (Cg 2,273.44 a month, Cg 27,281.28 a year), the basic credit already built into the tables, the 47.5% rate above the end of the table, the separate table for special payments (bijzondere beloningen), the official low-pay and high-pay examples, and the monthly return and payment within 15 days. Applies to Dutch Sint Maarten only. Trigger phrases include Sint Maarten wage tax, loonbelasting Sint Maarten, payroll St. Maarten 2026, maandtabel, bijzondere beloningen."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sx-wage-tax-tables"
  jurisdiction: "SX"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Sint Maarten: 2026 wage tax tables v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year: pay periods from 1 January 2026. Authority: Inspectorate of Taxes, Sint Maarten Tax Administration. Amounts in Caribbean guilders (Cg). Dutch Sint Maarten only, not French Saint-Martin.

## Who this applies to

- Employers (withholding agents) in Sint Maarten withholding wage tax from employees' pay. [AB 2026 no. 11, article 2](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Regeling%20vaststelling%20inkomsten-%20en%20loonbelastingtabellen%202026.pdf) adopts Annex II with the wage tax tables and the special-payments table.
- The input is the wage-tax base in **column 13 of the wage statement** (loonstaat), not the gross cash salary ([Annex II](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20II%20TABEL%20LOONBELASTING%202026.pdf)).
- Not covered: AOV/AWW and medical insurance premiums (their rates are not confirmed here), benefits in kind, registration, annual reporting.

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Nil withholding, half-day table | base not more than Cg 52.46 | Column 13 base | 2026 | [Annex II, Loonbelasting grondslagen 2026](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20II%20TABEL%20LOONBELASTING%202026.pdf) |
| Nil withholding, day table | Cg 104.93 | same | 2026 | same |
| Nil withholding, week table | Cg 524.64 | same | 2026 | same |
| Nil withholding, quincena table | Cg 1,049.28 | same | 2026 | same |
| Nil withholding, month table | Cg 2,273.44 | same | 2026 | same |
| Nil withholding, quarter table | Cg 6,820.32 | same | 2026 | same |
| Nil withholding, net full-year wage | Cg 27,281.28 | Annual equivalent | 2026 | same |
| Above the end of the table | 47.5% on the excess | Month table ends at Cg 14,162.33 (tax 3,933.16) | 2026 | same |
| Special payments, 0 to under 21,200 | 0% | Income measure for the special-payments table | 2026 | same |
| Special payments, 21,200 to under 40,700 | 12.5% | same | 2026 | same |
| Special payments, 40,700 to under 61,000 | 20% | same | 2026 | same |
| Special payments, 61,000 to under 84,700 | 26.25% | same | 2026 | same |
| Special payments, 84,700 to under 127,000 | 33.75% | same | 2026 | same |
| Special payments, 127,000 to under 179,500 | 40% | same | 2026 | same |
| Special payments, 179,500 and over | 47.5% | same | 2026 | same |
| Basic credit | 2,381 a year, already in the tables | Do not deduct again | 2026 | same |

## The base

1. **Pick the table for the actual pay period:** half-day, day, week, quincena, month or quarter ([Annex II](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20II%20TABEL%20LOONBELASTING%202026.pdf)).
2. **Compute the column 13 base.** The annex example: gross 2,473.16, less acquisition costs 41.67, less the employee AOV/AWW share 158.05 (stated at 6.5% "onder voorbehoud", subject to that being the 2026 rate) = 2,273.44 (same annex).
3. **Nil rule:** if the base is not more than the period threshold, withhold nothing; otherwise use the table normally. In the example the month table would show 85.62, but the nil rule controls (same annex). Use the published period figure, not a scaled annual amount.
4. **Above the table:** withhold 47.5% on the part above the last table amount only, not on the whole wage (same annex).
5. **Special payments** (bijzondere beloningen) use their own table, by income band. Classify the payment and establish the income measure before using it; the top 47.5% is not for every bonus (same annex).
6. **A nil wage tax result does not mean nil premiums.** Check AOV/AWW and medical insurance separately.

## Deadlines and filing

- Wage tax returns are monthly: file and pay within 15 days after the end of the period ([General Tax Ordinance (Algemene landsverordening landsbelastingen)](https://lokaleregelgeving.overheid.nl/CVDR671742)). The Tax Administration calendar lists 16 November 2026 for the October 2026 return and December dates for November ([Sint Maarten Tax Administration](https://www.tax.sx/)).
- The annual verzamelloonstaat and the Opgave Derden forms are on the Tax Administration's business documents page (same site); their 2026 due dates are not confirmed here.

## Penalties and interest

The penalty amounts for late wage tax returns and payments are not on the pages read. Refer to the General Tax Ordinance chapter on administrative penalties.

## Cross-border points

- Applies to Dutch Sint Maarten; an employee living on the French side may be taxed under the French rules too: refer.
- Treaty and Kingdom-arrangement relief: refer.

## Two worked examples that recompute

**Case 1: the annex's low-pay example.** Gross 2,473.16 a month; less costs 41.67 and employee AOV/AWW 158.05 = base 2,273.44. That is not more than the month threshold of 2,273.44, so wage tax is nil (the table alone would show 85.62).

```oa-check
name: Sint Maarten 2026 month, low pay at the nil threshold
inputs:
  gross: 2473.16
  costs: 41.67
  aov_aww_employee: 158.05
  month_nil_limit: 2273.44
steps:
  - base: gross - costs - aov_aww_employee
  - headroom: month_nil_limit - base
expected:
  base: 2273.44
  headroom: 0.00
```

**Case 2: the annex's high-pay example.** Base Cg 15,000 a month. Table ends at 14,162.33 with tax 3,933.16; excess 837.67 at 47.5% = 397.89; total 4,331.05. Applying 47.5% to the whole 15,000 would give 7,125, overstating wage tax by 2,793.95.

```oa-check
name: Sint Maarten 2026 month, base above the table
inputs:
  base: 15000
  table_end: 14162.33
  table_tax: 3933.16
steps:
  - excess: base - table_end
  - excess_tax: round(excess * 0.475, 2)
  - total: table_tax + excess_tax
  - wrong_flat: base * 0.475
  - overstatement: wrong_flat - total
expected:
  excess: 837.67
  excess_tax: 397.89
  total: 4331.05
  overstatement: 2793.95
```

## Ask the client first

1. The pay period (month, quincena, week, day, half-day, quarter).
2. The column 13 base: gross pay, acquisition costs, employee premiums.
3. Is any payment a special payment (bonus, 13th month)?
4. Residence of the employee (Dutch side or French side).
5. Is the employer registered, with a CRIB number?

## Sources

| Source | URL | Read on |
|---|---|---|
| AB 2026 no. 11, regulation: read for article 2 (Annex II) and the entry into force | https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Regeling%20vaststelling%20inkomsten-%20en%20loonbelastingtabellen%202026.pdf | 2026-11-14 |
| AB 2026 no. 11, Annex II (wage tax tables 2026): read for the general rules, column 13, the period nil thresholds, both examples, the 47.5% rule and the special-payments table | https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20II%20TABEL%20LOONBELASTING%202026.pdf | 2026-11-14 |
| General Tax Ordinance (CVDR671742): read for the 15-day return and payment periods for periodic returns | https://lokaleregelgeving.overheid.nl/CVDR671742 | 2026-11-14 |
| Sint Maarten Tax Administration: read for the 2026 tax calendar (16 November 2026 for October) and the business documents section | https://www.tax.sx/ | 2026-11-14 |

Not yet confirmed: the 2026 AOV/AWW and medical insurance premium rates and ceilings (the annex assumes a 6.5% employee AOV/AWW share "onder voorbehoud"); the income measure for the special-payments table; the 2026 verzamelloonstaat due date; wage tax penalty amounts.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sx-wage-tax-tables` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sx-wage-tax-tables. If neither is available, confirm every figure against the official source pages cited above before relying on it.
