---
name: costa-rica-income-tax
description: "Use this skill for Costa Rica income tax of individuals for fiscal period 2026: the self-employed and other persons with lucrative activities (annual table, exempt to CRC 6,244,000, then 10%, 15%, 20% and 25%), salaried workers and pensioners (monthly table, exempt to CRC 918,000, then 10% to 25%), the family credits (child CRC 1,710 a month or CRC 20,520 a year, spouse CRC 2,590 or CRC 31,080), the small legal-person table (5% to 20% when gross income does not exceed CRC 119,174,000), the annual return (form 101 in TRIBU-CR, due 16 March 2026 for 2025) and penalties. Trigger phrases include impuesto sobre la renta Costa Rica, tramos 2026, Decreto 45333-H, actividad lucrativa, D-101, TRIBU-CR and Hacienda."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/costa-rica-income-tax"
  jurisdiction: "CR"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Costa Rica income tax, individuals and small companies, fiscal period 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed by a Costa Rican accountant. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Costa Rica.

## Who this applies to

Individuals with lucrative activities (self-employed, professionals, traders), salaried workers and pensioners, and small legal persons, for the fiscal period 2026 (1 January to 31 December). The tax authority is the Direccion General de Tributacion of the Ministerio de Hacienda; returns are filed in TRIBU-CR. Costa Rica taxes Costa Rican-source income.

Refer: the Regimen de Tributacion Simplificada, free zone companies, capital income and gains (separate 15% regime, not read in this pass), non-residents (remittances abroad), large companies at the general rate, and any audit. Employer withholding mechanics: [costa-rica-payroll](costa-rica-payroll.md). IVA: [costa-rica-iva](costa-rica-iva.md).

Conservative defaults:

| Ambiguity | Default |
| --- | --- |
| Expense without an authorised electronic receipt | Not deductible |
| Business share of home, car or phone unknown | Not deductible |
| Spouse or children credit claimed by both spouses | Only one may claim it |
| Gross income of a company near CRC 119,174,000 | Check the full year's gross; above it the small table does not apply |

## Rates, bands and thresholds

**Persons with lucrative activities, annual renta neta, 2026 (Decreto Ejecutivo 45333-H).**

| From (CRC) | To (CRC) | Rate | Source |
| --- | --- | --- | --- |
| 0 | 6,244,000 | Not subject | Hacienda, Tramos del impuesto sobre la renta 2026: https://www.hacienda.go.cr/docs/TramosRenta2026.pdf |
| 6,244,000 | 8,329,000 | 10% | same |
| 8,329,000 | 10,414,000 | 15% | same |
| 10,414,000 | 20,872,000 | 20% | same |
| Over 20,872,000 | | 25% | same |
| Credit per child | CRC 20,520 a year | Against the tax | same |
| Credit for spouse | CRC 31,080 a year | Against the tax | same |

**Salaried workers, retirees and pensioners, monthly gross salary, 2026.**

| From (CRC) | To (CRC) | Rate | Source |
| --- | --- | --- | --- |
| 0 | 918,000 | Not subject | Hacienda, Tramos del impuesto sobre la renta 2026: https://www.hacienda.go.cr/docs/TramosRenta2026.pdf |
| 918,000 | 1,347,000 | 10% | same |
| 1,347,000 | 2,364,000 | 15% | same |
| 2,364,000 | 4,727,000 | 20% | same |
| Over 4,727,000 | | 25% | same |
| Credit per child | CRC 1,710 a month | Against the tax | same |
| Credit for spouse | CRC 2,590 a month | Against the tax | same |

**Legal persons with gross income not above CRC 119,174,000 in the period, annual renta neta.**

| From (CRC) | To (CRC) | Rate | Source |
| --- | --- | --- | --- |
| 0 | 5,621,000 | 5% | Hacienda, Tramos del impuesto sobre la renta 2026: https://www.hacienda.go.cr/docs/TramosRenta2026.pdf |
| 5,621,000 | 8,433,000 | 10% | same |
| 8,433,000 | 11,243,000 | 15% | same |
| Over 11,243,000 | | 20% | same |
| Gross income ceiling for this table | CRC 119,174,000 | Above it the general corporate rate applies | same |

**Other figures.**

| Item | Amount | Source |
| --- | --- | --- |
| Salario base 2026 (unit for fines) | CRC 462,200 | Hacienda salario base table: https://www.hacienda.go.cr/docs/SalariosBaseActualEHistorico.pdf |
| Late filing fine (art. 79) | Half a salario base, CRC 231,100 | Hacienda, Infracciones y sanciones 2026: https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf |
| Late payment fine (art. 80) | 1% a month or part, up to 20% | same |

## The base

1. **Lucrative activities:** gross income from the activity less necessary, documented costs and expenses; renta neta goes on the annual table. Income reported in the IVA returns must match the income tax return (Hacienda CP-11-2026).
2. **Salaries:** the monthly gross salary goes on the monthly table; the employer withholds, and withholding is final for a salaried worker without other income.
3. **Credits** for children and spouse reduce the tax computed.
4. **Small companies:** renta neta on the 5% to 20% table if gross income does not exceed CRC 119,174,000.
5. **Partial payments (pagos parciales)** made during the year and retentions are credited on the return; missing them causes interest (CP-11-2026).

## Deadlines and filing

| Obligation | Deadline | Form |
| --- | --- | --- |
| Annual return, 2025 period | 16 March 2026 (Hacienda CP-11-2026) | 101 (individuals), 102 (legal persons), 103 (public), TRIBU-CR OVi |
| Annual return, 2026 period | Expected in March 2027 on the same rule; date not yet announced | Same |
| Payment | With the return, online with an IBAN or at BCR or BAC | |
| Pagos parciales | During the period | See Not yet confirmed |

## Penalties and interest

Hacienda's 2026 sanctions summary: late filing, half a salario base (CRC 231,100), cut by 75% (CRC 57,775) if filed before any Hacienda action and by 80% (CRC 46,220) if the fine is also self-assessed and paid; late payment, 1% a month or part on the unpaid tax, up to 20%, no reduction; failure to register, half a salario base a month up to 3 salarios base (CRC 1,386,600). Interest on late tax also applies (rate not confirmed here).

## Cross-border points

Costa Rica taxes income from Costa Rican sources. Payments abroad bear the remittance tax (impuesto sobre remesas al exterior); its rates were not read in this pass. No treaty analysis is given here.

## Two worked examples that recompute

### Example 1: self-employed designer, 2026

Renta neta CRC 12,000,000; married, one child. Tax on the table CRC 838,450; less spouse credit CRC 31,080 and child credit CRC 20,520: CRC 786,850.

```oa-check
name: CR 2026 lucrative activity, renta neta 12 million
inputs:
  net: 12000000
steps:
  - b10: (8329000 - 6244000) * 0.10
  - b15: (10414000 - 8329000) * 0.15
  - b20: (net - 10414000) * 0.20
  - gross_tax: b10 + b15 + b20
  - tax: gross_tax - 31080 - 20520
expected:
  b10: 208500
  b15: 312750
  b20: 317200
  gross_tax: 838450
  tax: 786850
```

### Example 2: own name or a small company at CRC 15,000,000 (decision)

As an individual: CRC 1,438,450. Through a company with gross income under CRC 119,174,000: CRC 281,050 + 281,200 + 421,500 + 751,400 = CRC 1,735,150, before any tax on distributing the profit. At this level the individual table is CRC 296,700 cheaper, because it exempts the first CRC 6,244,000 while the company table starts at 5%.

```oa-check
name: CR 2026 individual against small company at 15 million
inputs:
  net: 15000000
steps:
  - individual: (8329000 - 6244000) * 0.10 + (10414000 - 8329000) * 0.15 + (net - 10414000) * 0.20
  - company: 5621000 * 0.05 + (8433000 - 5621000) * 0.10 + (11243000 - 8433000) * 0.15 + (net - 11243000) * 0.20
  - difference: company - individual
expected:
  individual: 1438450
  company: 1735150
  difference: 296700
```

## Ask the client first

1. Salaried, self-employed, or both? A company?
2. Renta neta for 2026, or monthly gross salary.
3. Spouse and children who qualify for credits (and who claims them).
4. For a company: gross income for the period (CRC 119,174,000 test).
5. Partial payments made and retentions suffered.
6. Any income from abroad or capital income.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for Hacienda, Tramos del impuesto sobre la renta para el periodo fiscal 2026: salaried, lucrative activity and small legal person tables and credits | https://www.hacienda.go.cr/docs/TramosRenta2026.pdf | 2026-11-14 |
| Read for Hacienda salario base table, 2026 value | https://www.hacienda.go.cr/docs/SalariosBaseActualEHistorico.pdf | 2026-11-14 |
| Read for Hacienda, Infracciones y sanciones administrativas mas relevantes (2026): arts. 78, 79, 80 and reductions | https://www.hacienda.go.cr/docs/InfraccionesYSancionesAdministrativasMasRelevantes.pdf | 2026-11-14 |
| Read for Hacienda notice CP-11-2026: forms 101, 102, 103, deadline 16 March 2026 for period 2025, payment channels, pagos parciales | https://www.hacienda.go.cr/docs/CP11-2026.pdf | 2026-11-14 |

Not yet confirmed: the general corporate rate (30% in the old file) on an official page read today; the Ley 10667 25% standard deduction for professionals that the old file reported from 2026; capital income and gains rates; remittance tax rates; pagos parciales rules and dates; the 2027 filing date for period 2026; late payment interest.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `costa-rica-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/costa-rica-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
