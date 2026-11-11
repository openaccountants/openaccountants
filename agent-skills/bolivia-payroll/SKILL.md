---
name: bolivia-payroll
description: "Bolivia payroll for dependent employees in 2026: the monthly run from total ganado to net pay, and the labour payments around it. Covers the 2026 minimum wage of Bs 3,300 (DS 5516) and the April 2026 adjustment payroll, the bono de antigüedad base of three minimum wages, the employee's social-security deductions and the employer's charges (rates in bolivia-social-contributions), the employer's RC-IVA withholding with Forms 110 and 608 (method in bolivia-income-tax), the aguinaldo de Navidad (one month's pay, three-month minimum, twelfths, 20 December, double if late, OVT payroll filing), the segundo aguinaldo when GDP growth exceeds 4.5% (DS 1802), severance (indemnización, one month per year after 90 days, DS 110), desahucio, vacations taken in parts (DS 4709), the RC-IVA exemption of the aguinaldo and severance, a worked gross-to-net and a final settlement, and bank-statement patterns. Trigger on: Bolivia payroll, planilla de sueldos, total ganado, salario mínimo 2026, aguinaldo, seg"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bolivia-payroll"
  jurisdiction: "BO"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Bolivia payroll for 2026: gross to net, aguinaldo, severance and the minimum wage v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

The 2026 minimum wage is set by DS 5516 (13 January 2026). Severance is in DS 0110 of 1 May 2009, the segundo aguinaldo in DS 1802 of 20 November 2013, the bono de antigüedad base in DS 23474 of 20 April 1993, and split vacations in DS 4709 of 1 May 2022, all read in the Gaceta Oficial de Bolivia. The aguinaldo rules are those the Ministerio de Trabajo, Empleo y Previsión Social applies in its yearly instruction under the Ley of 18 December 1944 and DS 229 of 1944; the latest one read is Instructivo DGTHSO 0119/2025. The RC-IVA exemptions are in DS 21531 art. 1, read in the SIN's consolidated Ley 843 to 30 September 2026. All amounts are in bolivianos (Bs). Tax year 2026, pay monthly.

This skill is the payroll run. It links to the skills that own the figures it uses: contribution rates in [bolivia-social-contributions](bolivia-social-contributions.md); the RC-IVA computation (non-taxable minimum, presumed credit, Forms 110 and 608 and their deadlines) in [bolivia-income-tax](bolivia-income-tax.md); the employer's deduction of pay for the IUE in [bolivia-corporate-income-tax](bolivia-corporate-income-tax.md).

## Who this applies to

- **Employers of dependent workers** under the Ley General del Trabajo in the private sector, and the dependent workers themselves: anyone working for another under subordination and dependence for pay, whatever the contract (Instructivo 0119/2025, point I.2).
- **Foreign employees** working for a Bolivian employer are on the same payroll, contributions and RC-IVA as nationals ([bolivia-social-contributions](bolivia-social-contributions.md)).
- **Out of scope:** public servants under the Estatuto del Funcionario Público (their aguinaldo follows the Ministry of Economy's instruction), independent professionals and consultants (RC-IVA Form 610, [bolivia-income-tax](bolivia-income-tax.md)), directors' fees, domestic workers' special rules, and mining cooperatives.

**When to refer.** Refer for: dismissals and disputes over desahucio; the bono de antigüedad percentage for a given seniority (the scale was not read); collective agreements that add pay items; benefits in kind and share plans; workers posted abroad; the segundo aguinaldo in a year it is declared.

## Rates, bands and thresholds

Quick answer: the employee's take-home pay is total ganado less 12.71% contributions, less any Aporte Nacional Solidario, less the RC-IVA the employer withholds. The employer adds 17.21% on top. The minimum wage for 2026 is Bs 3,300 a month.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| National minimum wage (SMN), public and private sectors, retroactive to 1 January 2026 (DS 5516 art. 23) | Bs 3,300 a month | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281033 |
| Adjustment payroll for workers raised to the 2026 SMN in basic pay or bono de antigüedad, on the OVT (Comunicado DGTHSO-014/2026, RM 088/26) | Due by 15 April 2026; no fee | 2026 | https://mintrabajo.gob.bo/wp-content/uploads/2026/04/COMUNICADO-DGTHSO-0014-26.pdf |
| Bono de antigüedad: calculation base for workers of productive companies, public and private (DS 23474) | 3 SMN = Bs 9,900 | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/17419 |
| Employee contributions and ANS; employer charges | 12.71% plus ANS; 17.21% (19.51% mining): see [bolivia-social-contributions](bolivia-social-contributions.md) | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/280468 |
| RC-IVA withheld by the employer: rate, non-taxable minimum and presumed credit | 13%; see [bolivia-income-tax](bolivia-income-tax.md) | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Aguinaldo de Navidad: amount (Instructivo 0119/2025 III.1) | One month's pay; twelfths if the year is not complete | 2026 | https://mintrabajo.gob.bo/wp-content/uploads/2025/12/INSTRUCTIVO-DGTHSO-No0119-2025.pdf |
| Aguinaldo: minimum service (DS 1802 Disposición Adicional Única; Instructivo I.2) | 3 months uninterrupted with the same employer in the year (1 calendar month for obreros); employees hired up to 1 October count | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/143786 |
| Aguinaldo: base (Instructivo I.3) | Average total ganado of the 3 months before payment, or before the job ended | 2026 | https://mintrabajo.gob.bo/wp-content/uploads/2025/12/INSTRUCTIVO-DGTHSO-No0119-2025.pdf |
| Aguinaldo: private-sector payment date, sanction (Instructivo IV.1) | By 20 December (the 2025 instruction: Saturday 20 December 2025); late payment is paid double | 2026 | same |
| Aguinaldo: deductions (Instructivo III.2; DS 21531 art. 1 b) | None: no tax, no contributions, no attachment, not in kind | 2026 | same |
| Segundo aguinaldo "Esfuerzo por Bolivia" (DS 1802 arts. 1, 3 and 5) | One more aguinaldo, only in a year the GDP growth for the 12 months to September exceeds 4.5% | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/143786 |
| Indemnización por tiempo de servicios (DS 0110 arts. 1 and 2) | One month's pay per year of continuous work, pro rata for months; due after more than 90 days, on dismissal or resignation | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/27513 |
| Indemnización: base (DS 0110 art. 2 III) | Average total ganado of the last 3 months (last 30 days for day workers) | 2026 | same |
| Desahucio (DS 0110 art. 3) | Due only on sudden dismissal (retiro intempestivo), never on resignation | 2026 | same |
| Indemnización and desahucio under RC-IVA (DS 21531 art. 1 c) | Not income; extra gratuities on leaving are taxed | 2026 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf |
| Vacations in parts (DS 224 art. 33, text of DS 4709) | At most 3 periods a year, and half days up to 5 days a year; not paid in money except when the job ends | 2026 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/168762 |

## The base

**Total ganado** is the month's gross pay: basic pay (haber básico), bono de antigüedad, overtime, night-work and holiday surcharges, commissions and the other regular pay items. The Ministry's aguinaldo instruction lists these as the "remuneración total" (Instructivo I.3). Contributions and RC-IVA both start from it.

**Gross to net, each month, in this order:**

1. **Total ganado.** Check the basic pay is at least the SMN of Bs 3,300 for a full month. Since January 2026 the SMN also moves the bono de antigüedad, whose base is three SMN (Bs 9,900); apply the seniority percentage from the employer's scale (refer if unsure).
2. **Employee contributions.** Deduct 12.71% of total ganado, and the Aporte Nacional Solidario if total ganado is above Bs 13,000 (rates in [bolivia-social-contributions](bolivia-social-contributions.md)).
3. **RC-IVA.** Total ganado less the contributions, less the non-taxable minimum of two SMN; 13% of the rest; less 13% of the invoices the employee hands in on Form 110 by the 20th, less the presumed credit, less any balance brought forward. Withhold what is left (method and 2026 figures in [bolivia-income-tax](bolivia-income-tax.md)).
4. **Net pay** = total ganado less steps 2 and 3, less any other deduction the worker has authorised.
5. **Employer charges.** 17.21% of total ganado (19.51% for mining productive-area workers), not deducted from the worker.

**Aguinaldo de Navidad.** One month's pay, on the average total ganado of the three months before payment. A worker with fewer than twelve months in the year gets twelfths for the months worked, if they worked at least three months in a row for the same employer (one calendar month for obreros). Employees hired up to 1 October count. It is paid in full, in money: no tax, no contributions, no set-off (Instructivo III.1 and III.2; DS 21531 art. 1 b). It is also due, pro rata, in the final settlement of a worker who leaves during the year, on the three months before the job ended (Instructivo I.3).

**Segundo aguinaldo.** DS 1802 creates a second aguinaldo for the public and private sectors in a year when GDP growth in the 12 months to September exceeds 4.5%. The INE reports the figure in October, and the Government then declares it. It follows the aguinaldo rules (three-month minimum, twelfths). Whether it is due for 2026 was not known on 11 November 2026.

**Leaving: the final settlement (finiquito).**

- **Indemnización:** one month's pay for each year of continuous work, and twelfths for months short of a year, once the worker has completed more than 90 days. It is due on dismissal and on resignation alike. The base is the average total ganado of the last three months (DS 0110 arts. 1 and 2).
- **Desahucio:** only when the employer dismisses the worker suddenly; never on resignation (DS 0110 art. 3). Its amount was not read here: refer.
- **Quinquenio:** rights earned every five years are kept even if a later cause under art. 16 of the Ley General del Trabajo forfeits the benefits of the current five years (DS 11478 art. 2, text of DS 0110 art. 4).
- **Plus:** pay to the last day, the aguinaldo twelfths, and untaken vacation, the one case where vacation is paid in money (DS 224 art. 33).
- **RC-IVA:** indemnización and desahucio are not income for RC-IVA; extra gratuities paid on leaving are (DS 21531 art. 1 c).

**Vacations.** Taken by the employer's rota. They cannot be paid in money except when the job ends, and cannot be carried over unless agreed in writing, the employer made no rota, or the employer did not let the worker take them. The worker can ask in writing to split them into at most three periods a year, and to take half days adding up to no more than five days a year (DS 224 art. 33, text of DS 4709). The number of days by seniority was not read here.

## Deadlines and filing

**The monthly cycle, in the order the employer meets it:**

1. **By the 20th:** collect the employees' Form 110 with their purchase invoices ([bolivia-income-tax](bolivia-income-tax.md)).
2. **Pay day:** pay net wages; keep the payroll (planilla de sueldos) signed by the workers.
3. **NIT-digit day 13 to 22 of the next month:** file Form 608 from the SIN's Planillas Tributarias application and pay the RC-IVA withheld ([bolivia-income-tax](bolivia-income-tax.md)).
4. **Last working day of the next month:** declare and pay the Gestora on the FPC; pay the health fund ([bolivia-social-contributions](bolivia-social-contributions.md)).

**Yearly and one-off items:**

| What | When | Where |
|---|---|---|
| 2026 SMN adjustment payroll, for workers whose basic pay or bono de antigüedad rose to the Bs 3,300 SMN (Comunicado DGTHSO-014/2026) | By 15 April 2026 | Ministry of Labour Oficina Virtual de Trámites (OVT) |
| Aguinaldo de Navidad, private sector (Instructivo 0119/2025) | By 20 December; the 2026 instruction had not been issued on 11 November 2026 | Paid to each worker |
| Aguinaldo payroll filed with the Ministry (RM 212/18 art. 2 II, as applied in Instructivo 0119/2025) | By the date in the yearly instruction (30 December in 2025), after paying the service fee (RM 462/22) | OVT |
| Segundo aguinaldo, if declared | By the date in the decree that declares it | Paid to each worker |
| Final settlement | When the job ends | Paid to the worker |

## Penalties and interest

- **Aguinaldo paid late:** paid double, plus a fine for breach of social law where it applies (Instructivo IV.1).
- **Aguinaldo payroll not filed with the Ministry:** sanctions under the Ministry's rules (Instructivo IV.1; amounts not read).
- **RC-IVA not withheld or paid late:** omission of payment, 60% of the updated tax, plus interest ([bolivia-income-tax](bolivia-income-tax.md)).
- **Contributions paid late:** the Gestora's interest and surcharges; never charged to the worker ([bolivia-social-contributions](bolivia-social-contributions.md)).

## Cross-border points

- **Foreign employees** of a Bolivian employer are paid, taxed and insured like nationals: RC-IVA through Form 608 and full contributions ([bolivia-income-tax](bolivia-income-tax.md), [bolivia-social-contributions](bolivia-social-contributions.md)).
- **People working in Bolivia under a contract with a foreign entity** are not on a Bolivian payroll: they declare RC-IVA themselves as non-domiciled individuals ([bolivia-income-tax](bolivia-income-tax.md)).
- **Pay for services from abroad** (a foreign consultant, not an employee) bears IUE-BE withholding ([bolivia-cross-border](bolivia-cross-border.md)).

## Two worked examples that recompute

### Example 1: gross to net, March 2026, employee on Bs 12,000

An employee's total ganado for March 2026 is Bs 12,000. No ANS (below Bs 13,000). The employee hands in no invoices on Form 110 and has no balance brought forward. RC-IVA figures from [bolivia-income-tax](bolivia-income-tax.md): non-taxable minimum two SMN (Bs 6,600), presumed credit 13% of one SMN (Bs 429).

- Contributions: 12.71% x 12,000 = Bs 1,525.20.
- RC-IVA base: 12,000 - 1,525.20 - 6,600 = Bs 3,874.80. Tax 13% = Bs 503.72. Less presumed credit Bs 429: withheld Bs 74.72.
- Net pay: 12,000 - 1,525.20 - 74.72 = Bs 10,400.08.
- Employer cost: 12,000 + 17.21% (Bs 2,065.20) = Bs 14,065.20.
- The edge: with Bs 1,000 of invoices on Form 110 (credit Bs 130), nothing is withheld and Bs 55.28 carries forward to April, updated by the UFV. Net pay Bs 10,474.80.

```oa-check
name: Gross to net, Bs 12,000, March 2026, with and without Form 110 invoices
inputs:
  total_ganado: 12000
  smn: 3300
  invoices: 1000
steps:
  - contributions: total_ganado * 0.1271
  - rc_iva_base: max(total_ganado - contributions - 2 * smn, 0)
  - rc_iva_gross: rc_iva_base * 0.13
  - presumed_credit: smn * 0.13
  - withheld_no_invoices: max(rc_iva_gross - presumed_credit, 0)
  - net_no_invoices: total_ganado - contributions - withheld_no_invoices
  - employer_cost: total_ganado * 1.1721
  - invoice_credit: invoices * 0.13
  - withheld_with_invoices: max(rc_iva_gross - invoice_credit - presumed_credit, 0)
  - balance_forward: invoice_credit + presumed_credit - rc_iva_gross
  - net_with_invoices: total_ganado - contributions - withheld_with_invoices
expected:
  contributions: 1525.20
  rc_iva_base: 3874.80
  rc_iva_gross: 503.72
  presumed_credit: 429.00
  withheld_no_invoices: 74.72
  net_no_invoices: 10400.08
  employer_cost: 14065.20
  invoice_credit: 130.00
  withheld_with_invoices: 0
  balance_forward: 55.28
  net_with_invoices: 10474.80
```

### Example 2: final settlement after nine months, resignation, and the 90-day line

A worker hired on 1 March 2026 resigns with effect from 30 November 2026: nine full months. Total ganado was Bs 6,000 in each of September, October and November.

- Indemnización: more than 90 days, so due even on resignation. 6,000 x 9 / 12 = Bs 4,500.
- Aguinaldo twelfths: three or more months in a row, hired before 1 October. 6,000 x 9 / 12 = Bs 4,500.
- Desahucio: none, because the worker resigned.
- Neither is subject to contributions or RC-IVA. Settlement Bs 9,000, plus November pay and any untaken vacation.
- The edge: had the worker left after 80 days (hired 1 March, gone 19 May), neither the indemnización (needs more than 90 days) nor the aguinaldo (needs three months in a row) would be due.

```oa-check
name: Final settlement, 9 months, resignation, average total ganado Bs 6,000 (2026)
inputs:
  average_total_ganado: 6000
  months: 9
steps:
  - indemnizacion: average_total_ganado * months / 12
  - aguinaldo_twelfths: average_total_ganado * months / 12
  - desahucio: 0
  - settlement: indemnizacion + aguinaldo_twelfths + desahucio
expected:
  indemnizacion: 4500
  aguinaldo_twelfths: 4500
  desahucio: 0
  settlement: 9000
```

### Bank-statement patterns

| Pattern in the narrative | What it is |
|---|---|
| SUELDO, SALARIO, HABER, HABERES, REMUNERACION, PAGO PLANILLA, ABONO SUELDO, NOMINA | Net pay to a worker |
| AGUINALDO, AGUINALDO NAVIDAD | Aguinaldo de Navidad, normally December |
| SEGUNDO AGUINALDO, ESFUERZO POR BOLIVIA | Segundo aguinaldo, only in a year it is declared |
| INDEMNIZACION, DESAHUCIO, FINIQUITO, BENEFICIOS SOCIALES | Final settlement |
| HORAS EXTRAS, RECARGO, BONO ANTIGUEDAD, PRIMA | Pay items inside total ganado |
| IMPUESTOS NACIONALES, SIN, SIAT, F608, RC-IVA, RETENCION | RC-IVA withheld, paid to the SIN |
| GESTORA, FPC, APORTES, CNS, CAJA NACIONAL DE SALUD, VIVIENDA | Contributions ([bolivia-social-contributions](bolivia-social-contributions.md)) |
| MINISTERIO DE TRABAJO, OVT | Ministry fee for filing a payroll |
| PRESTAMO, ANTICIPO, TRASPASO PROPIO, DIVIDENDO, INTERESES | Not payroll: loans and advances, own transfers, dividends, interest |

Bookkeeping: gross pay and the employer's charges are expenses; the employee contributions and the RC-IVA withheld are liabilities until paid to the Gestora and the SIN.

## Ask the client first

1. Each worker's basic pay, seniority and other regular pay items for the month (to build total ganado and check the SMN).
2. Start date, and for anyone leaving: end date, and whether they resigned or were dismissed.
3. The Form 110 invoices each worker handed in this month and any RC-IVA balance carried forward.
4. The employer's NIT last digit, sector (mining or not) and health fund.
5. Whether a collective agreement adds pay items or a seniority scale.
6. Any month of 2026 not yet filed: the April SMN adjustment payroll, Form 608, the Gestora FPC.

## Sources

| Source | URL | Read on |
|---|---|---|
| Gaceta Oficial, Decreto Supremo N° 5516 (HTML text): read arts. 21 and 23 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/281033 | 2026-11-11 |
| Ministerio de Trabajo, Comunicado DGTHSO-014/2026 of 2 April 2026: SMN adjustment payroll on the OVT by 15 April 2026 | https://mintrabajo.gob.bo/wp-content/uploads/2026/04/COMUNICADO-DGTHSO-0014-26.pdf | 2026-11-11 |
| Ministerio de Trabajo, Instructivo DGTHSO 0119/2025 of 1 December 2025, payment of the aguinaldo de Navidad: read in full (points I to IV) | https://mintrabajo.gob.bo/wp-content/uploads/2025/12/INSTRUCTIVO-DGTHSO-No0119-2025.pdf | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 1802 of 20 November 2013 (HTML text): read arts. 1 to 5 and Disposición Adicional Única | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/143786 | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 0110 of 1 May 2009 (HTML text): read arts. 1 to 5 | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/27513 | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 23474 of 20 April 1993 (HTML text): read the single article (bono de antigüedad base of three SMN) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/17419 | 2026-11-11 |
| Gaceta Oficial, Decreto Supremo N° 4709 of 1 May 2022 (HTML text): read art. 2 (new DS 224 art. 33) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/168762 | 2026-11-11 |
| Gaceta Oficial, Ley N° 1582 of 1 October 2024 (HTML text): contribution rates, as used in [bolivia-social-contributions](bolivia-social-contributions.md) | http://gacetaoficialdebolivia.gob.bo/normas/verGratis_gob/280468 | 2026-11-11 |
| SIN, Ley N° 843 y Decretos Reglamentarios, Texto Ordenado, actualizado al 30/09/2026: read DS 21531 art. 1 b) and c) (aguinaldo, indemnización and desahucio not income), PDF p. 84 | https://www.impuestos.gob.bo/wp-content/uploads/2026/10/1.-LEY-N%C2%B0-843-09-26-1.pdf | 2026-11-11 |

Not yet confirmed: the 2026 aguinaldo instruction (payment date and OVT filing date for 2026; the dates above are from the 2025 instruction); whether the segundo aguinaldo is due for 2026; the bono de antigüedad percentages by years of service for the private sector; the amount of the desahucio (Ley General del Trabajo art. 12, not read); the number of vacation days by seniority and the overtime surcharge (Ley General del Trabajo and DS 224, not read); the prima anual (profit bonus) rules; any quarterly payroll filing with the Ministry of Labour (RM 212/18 was not read in full); the bank-statement patterns, which are practice, not law.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bolivia-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bolivia-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
