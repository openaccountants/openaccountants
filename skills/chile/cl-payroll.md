---
name: cl-payroll
description: "Chile employer payroll for tax year 2026: the monthly contributions an employer withholds from a dependent employee and pays itself, and the Impuesto Único de Segunda Categoría (IUSC) withheld from wages. Covers the AFP pension contribution of 10% plus the AFP commission (DL 3.500 arts. 16 to 19), the 7% health contribution to Fonasa or an Isapre (art. 84), the taxable ceiling of 90 UF for 2026 and 135.2 UF for unemployment insurance (Superintendencia de Pensiones), seguro de cesantía under Ley 19.728 (0.6% employee, 2.4% or 3% employer, the 11-year rule), the new employer pension contribution of Ley 21.735 (1% from August 2025, 3.5% from August 2026, SIS included from August 2026), the SIS rate of 1.78%, work-accident insurance under Ley 16.744 (0.90% plus the risk rate) and the 0.03% SANNA contribution, the IUSC base and monthly table, Previred and F29 deadlines, DJ 1887 and penalties. Trigger on: liquidación de sueldo, cotizaciones previsionales empleador, Previred, tope imponible 2026, AFP comisión, seguro de cesantía, cotización empleador reforma previsional, SIS, Chile payroll. Out of scope: self-employed cotizaciones (cl-social-contributions) and the annual IGC (cl-income-tax)."
version: 1.1
jurisdiction: CL
tax_year: 2026
last_updated: 2026-11-14
category: payroll
type: computation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
---

# Chile: employer payroll and wage withholding (2026) v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill covers one month of payroll for a dependent employee in Chile in 2026: what the employer deducts from the gross pay, what it pays on top, the wage tax it withholds, and where and when each amount is declared and paid. Tax year: the calendar year 2026. Currency: Chilean peso (CLP); ceilings are set in Unidades de Fomento (UF).

Linked skills, not repeated here:

- [cl-income-tax](cl-income-tax.md): the IUSC and IGC scales, the UTM and UTA of each month of 2026, the two-employer reliquidation (LIR art. 47) and the penalties of CT art. 97 No. 11 for late payment of tax withheld.
- [cl-social-contributions](cl-social-contributions.md): contributions of independent workers who issue boletas de honorarios.
- [cl-vat-return](cl-vat-return.md): Form F29, which also carries the IUSC withheld, and its due dates.
- [cl-cross-border](cl-cross-border.md): pay to people who are not resident in Chile (Impuesto Adicional, LIR art. 60).

**Which text of the law.** DL 3.500 (pension system) and Ley 19.728 (unemployment insurance) as consolidated on LeyChile and read on 11 November 2026 in the version in force on that day (both have deferred changes from 1 April 2027 that are not used here); Ley 21.735 (pension reform, Diario Oficial 26 March 2025); Ley 16.744 (work accidents); Ley 21.063 (SANNA); DL 824, Ley sobre Impuesto a la Renta (LIR), version of 17 October 2026. Ceilings, AFP commissions and the SIS rate are set by the Superintendencia de Pensiones (SP) under DL 3.500 arts. 16, 17 and 29, and are read from spensiones.cl.

## Who this applies to

- **Employers of dependent workers** affiliated to an AFP (DL 3.500). The employer declares and pays the contributions of its workers, deducting the worker's share from pay (DL 3.500 art. 19).
- **Workers obliged to contribute 10%:** affiliates under 65 (men) and under 60 (women) (DL 3.500 art. 17). For older workers and pensioners who keep working, ask; the rules differ and are not set out here.
- **Unemployment insurance (seguro de cesantía):** dependent workers who start or restart work after the law came in. Not covered: apprentices, workers under 18 until they turn 18, and pensioners, except invalidity-partial pensioners and household workers (Ley 19.728 art. 2).
- **Out of scope:** independent workers (see cl-social-contributions), household workers (they have their own cesantía and indemnity rules), workers in the old IPS, Dipreca or Capredena systems, public-sector pay, heavy-work contributions in detail (DL 3.500 art. 17 bis: an extra 2% from worker and employer, or 1% each where the Comisión Ergonómica Nacional sets it), gratificaciones, minimum wage and severance.

## Rates, bands and thresholds

| Item | Rate or amount | Who pays | Year | Source URL |
|---|---|---|---|---|
| Taxable ceiling (tope imponible) for AFP, health and work-accident contributions | 90.0 UF a month, from February 2026 pay for the rest of 2026 (87.8 UF in 2025) | ceiling | 2026 | https://www.spensiones.cl/portal/institucional/594/w3-article-16921.html (DL 3.500 art. 16) |
| Taxable ceiling for unemployment insurance | 135.2 UF a month, from February 2026 pay (131.9 UF in 2025) | ceiling | 2026 | same (Ley 19.728 art. 6) |
| UF at 31 October 2026 (used in the examples) | CLP 41,247.63 | value | Oct 2026 | https://www.sii.cl/valores_y_fechas/uf/uf2026.htm |
| AFP pension contribution | 10% of taxable pay, up to the ceiling | worker | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=7147 (DL 3.500 art. 17) |
| AFP commission (cotización adicional), by AFP | Capital 1.44%; Cuprum 1.44%; Habitat 1.27%; Modelo 0.58%; PlanVital 1.16%; Provida 1.45%; Uno 0.46% | worker | 2026 | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9897.html (DL 3.500 arts. 17, 29) |
| Disability and survivors insurance (SIS), from August 2026 | 1.78% of taxable pay, women and men; part of the employer's 3.5% below | employer | Aug-Dec 2026 | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9917.html |
| Health contribution (Fonasa, or the Isapre plan with this as the minimum) | 7% of taxable pay, up to the ceiling | worker | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=7147 (DL 3.500 art. 84) |
| Employer pension contribution, Ley 21.735, 1 August 2025 to 31 July 2026 | 1.0% (0.1% to the worker's AFP account, 0.9% to the Fondo Autónomo de Protección Previsional) | employer | Jan-Jul 2026 | https://www.bcn.cl/leychile/navegar?idNorma=1212060 (Ley 21.735 art. 4 transitorio a)) |
| Employer pension contribution, Ley 21.735, from 1 August 2026 | 3.5% (0.1% AFP account, 0.9% Cotización con Rentabilidad Protegida, 2.5% Seguro Social Previsional, which includes the SIS and the life-expectancy compensation) | employer | Aug 2026-Jul 2027 | same, art. 4 transitorio b); https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-10906.html |
| Employer pension contribution, later steps | 4.25% from August 2027, then 5.0%, 5.7%, 6.4%, 7.1%, 7.8% and 8.5% in yearly steps (a lower path applies if Ministerio de Hacienda decrees that Ley 21.713 raised less than expected) | employer | 2027 on | https://www.bcn.cl/leychile/navegar?idNorma=1212060 (art. 4 transitorio c) to k)) |
| Unemployment insurance, indefinite contract | 0.6% worker; 2.4% employer | both | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=184979 (Ley 19.728 art. 5) |
| Unemployment insurance, fixed-term or per-job contract | 3% employer; nothing from the worker | employer | 2026 | same, art. 5 b) |
| Unemployment insurance after 11 years in one job | The individual-account part (worker 0.6%, employer 1.6%) stops; the employer keeps paying 0.8% to the Fondo de Cesantía Solidario | both | 2026 | same, arts. 9 and 23 |
| Work-accident insurance, basic rate | 0.90% | employer | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=28650 (Ley 16.744 art. 15 a)) |
| Work-accident insurance, additional rate | By activity and risk, set by decree; up to 3.4% | employer | 2026 | same, art. 15 b) |
| SANNA (insurance for parents of seriously ill children) | 0.03% | employer | 2026 | https://www.bcn.cl/leychile/navegar?idNorma=1113014 (Ley 21.063 art. 24 a)) |
| IUSC, monthly table for October 2026 (used in the examples) | Exempt to CLP 974,038.50; 4% to 2,164,530 (deduct 38,961.54); 8% to 3,607,550 (125,542.74); 13.5% to 5,050,570 (323,957.99); 23% to 6,493,590 (803,762.14); 30.4% to 8,658,120 (1,284,287.80); 35% to 22,366,810 (1,682,561.32); 40% above (2,800,901.82) | worker (withheld) | Oct 2026 | https://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/impuesto2026.htm (LIR art. 43 No. 1) |

For January to July 2026 pay, the SIS is paid by the employer on top of the 1% Ley 21.735 contribution (DL 3.500 art. 17; Ley 21.735 art. 8 transitorio). Its rate for those months is not confirmed: the SP pages read on 14 Nov 2026 give only the 1.78% from August 2026.

The IUSC tables for the other months of 2026, and the UTM behind each, are in [cl-income-tax](cl-income-tax.md); use the table of the month the pay is earned.

## The base

Work in this order each month, for each worker.

1. **Taxable pay (remuneración imponible).** Pay for the month that is remuneration in law. Allowances that are not remuneration stay out; which allowances those are is a labour-law question not set out here (ask, and see Not yet confirmed).
2. **Apply the ceilings.** Pension, commission, SIS, health, the Ley 21.735 contribution and work-accident insurance are computed on taxable pay up to 90 UF. Unemployment insurance is computed up to 135.2 UF, at the UF of the last day of the month before payment (Ley 19.728 art. 6). Previred's file uses one field (field 27) for the base of both the AFP and the Seguro Social Previsional (SP, employer contribution page). For the AFP ceiling, the SP page read does not say which day's UF is used; the examples use the UF of the last day of the month the pay is earned, which for October 2026 pay is also the last day of the month before payment.
3. **Worker deductions.** AFP 10% plus the AFP's commission; health 7% (an Isapre plan may cost more, and the worker pays the difference); unemployment 0.6% on an indefinite contract. Two jobs: unemployment insurance is paid on each job up to the ceiling in each (Ley 19.728 art. 7).
4. **IUSC base.** Taxable pay less the worker's mandatory pension contributions (including the commission), the health contribution computed on the ceiling, and the 0.6% unemployment contribution (LIR art. 42 No. 1; DL 3.500 art. 18). Then apply the month's table: tax = base x rate of the band - amount to deduct (LIR art. 43 No. 1). Voluntary pension saving (APV) through the employer can also come off the base; see cl-income-tax.
5. **Net pay.** Gross pay less the worker deductions and the IUSC.
6. **Employer cost on top.** From August 2026: the 3.5% Ley 21.735 contribution (which already includes the SIS), unemployment 2.4% (or 3%), work-accident 0.90% plus the company's additional rate, and SANNA 0.03%. For January to July 2026: 1% under Ley 21.735 plus the SIS at the rate then in force, paid separately.

The SP says the SIS keeps being reported in Previred field 29 even though from August 2026 it is collected by the Instituto de Previsión Social (IPS) for the Fondo Autónomo de Protección Previsional (FAPP); the life-expectancy compensation goes in field 94 and the Cotización con Rentabilidad Protegida in field 95.

## Deadlines and filing

| What | When | Rule |
|---|---|---|
| Declare and pay AFP, health and Ley 21.735 contributions | Within the first 10 days of the month after the pay is earned; next working day if the 10th is a weekend or holiday; to the 13th (even if a weekend or holiday) when declared and paid electronically, as through Previred | DL 3.500 art. 19 |
| Declare and pay unemployment insurance | Same days | Ley 19.728 art. 10 |
| Notify the start or end of a worker's service to the AFC (Sociedad Administradora) | Within 10 days of the start or end | Ley 19.728 art. 5 |
| IUSC withheld | Declared and paid in Form F29, code 48, for the month of payment; due dates in [cl-vat-return](cl-vat-return.md) | LIR arts. 74 No. 1, 79; SII F29 |
| Annual sworn statement of wages and IUSC, DJ 1887 (AT 2026 calendar) | 27 March; certificates to workers by 14 March | SII, declaraciones juradas 2026 table |

**How to pay.** Upload the payroll file (the 105-field Previred format) or key it in at previred.com, choose the payroll type (remuneraciones, gratificaciones, retroactive pay), check each worker's AFP, taxable pay, worker type, working day, staff movements, medical leave and the ceiling for the period, then pay. The employer contribution of Ley 21.735 is declared and paid through Previred on the same dates as the other contributions, and the IPS collects it for the FAPP (SP, employer contribution page). The 2026 ceilings apply from the February 2026 pay, paid by 10 March (13 March electronically) (SP, 10 February 2026). The IUSC goes on the company's monthly F29 on sii.cl.

## Penalties and interest

- **Not declaring in time, or an incomplete or wrong declaration:** a fine of 0.75 UF per worker affected. If the declaration was incomplete or wrong without malice and the contributions are paid in the next calendar month, there is no fine (DL 3.500 art. 19).
- **Late payment:** the unpaid contributions are adjusted by the UF from the last day they should have been paid to the day of payment, and bear monthly interest at the higher of the real return of the worker's pension fund and the CMF current rate for indexed peso operations under a year, capitalised monthly (DL 3.500 art. 19). The SP publishes the adjustments and interest each month.
- **Late payment of IUSC withheld:** CT art. 97 No. 11, in [cl-income-tax](cl-income-tax.md).
- **Collection:** the AFPs must pursue unpaid contributions through the Sistema Único de Cobranza de Cotizaciones, and the Dirección del Trabajo enforces the declaration duty (DL 3.500 art. 19).

## Cross-border points

- **A worker who is not resident in Chile** but works in Chile for a Chilean employer is still a dependent worker for IUSC purposes on Chilean-source pay; pay for scientific, cultural or sports activities of non-residents is taxed under LIR art. 60 instead. See [cl-cross-border](cl-cross-border.md).
- **Foreign technicians and social-security agreements.** Chile has rules that can exempt foreign professionals from AFP contributions and bilateral social-security agreements; neither was read for this skill. Refer.
- **Chilean employees seconded abroad:** out of scope.

## Two worked examples that recompute

Both use October 2026 pay, paid in November 2026. UF at 31 October 2026 = CLP 41,247.63, so the 90 UF ceiling is CLP 3,712,286.70 and the 135.2 UF unemployment ceiling CLP 5,576,679.58. October 2026 is after 1 August 2026, so the employer's Ley 21.735 contribution is 3.5% with the SIS inside it. The additional work-accident rate is taken as 0% to keep the arithmetic short; use the company's real rate. Rounding to whole pesos is left out.

### Example 1: indefinite contract, CLP 2,500,000, AFP Habitat, Fonasa

Camila earns CLP 2,500,000 of taxable pay, below both ceilings.

- Worker: AFP 10% = 250,000; Habitat commission 1.27% = 31,750; health 7% = 175,000; unemployment 0.6% = 15,000. Total CLP 471,750.
- IUSC base = 2,500,000 - 471,750 = CLP 2,028,250, in the 4% band of the October table. IUSC = 2,028,250 x 4% - 38,961.54 = CLP 42,168.46.
- Net pay = 2,500,000 - 471,750 - 42,168.46 = CLP 1,986,081.54.
- Employer on top: Ley 21.735 3.5% = 87,500; unemployment 2.4% = 60,000; work-accident basic 0.90% = 22,500; SANNA 0.03% = 750. Total CLP 170,750, paid through Previred by 13 November 2026.

```oa-check
name: CL payroll October 2026, CLP 2.5m, indefinite contract, Habitat
inputs:
  gross: 2500000
  commission: 0.0127
steps:
  - afp: gross * 0.10
  - afp_commission: gross * commission
  - health: gross * 0.07
  - cesantia_worker: gross * 0.006
  - worker_total: afp + afp_commission + health + cesantia_worker
  - iusc_base: gross - worker_total
  - iusc: round(iusc_base * 0.04 - 38961.54, 2)
  - net_pay: gross - worker_total - iusc
  - employer_total: gross * (0.035 + 0.024 + 0.009 + 0.0003)
expected:
  worker_total: 471750
  iusc_base: 2028250
  iusc: 42168.46
  net_pay: 1986081.54
  employer_total: 170750
```

### Example 2: CLP 6,000,000 above the ceiling, and which AFP to choose

Rodrigo earns CLP 6,000,000, above the 90 UF ceiling and above the 135.2 UF unemployment ceiling. He is with Provida (1.45%) and asks whether moving to Uno (0.46%) is worth it.

- **Ceilings:** AFP, commission and health on CLP 3,712,286.70; unemployment on CLP 5,576,679.58.
- **With Provida:** AFP 371,228.67; commission 53,828.16; health 259,860.07; unemployment 33,460.08; total 718,376.98. IUSC base 5,281,623.02, in the 23% band: IUSC = 5,281,623.02 x 23% - 803,762.14 = 411,011.15. Net pay CLP 4,870,611.87.
- **With Uno:** commission 17,076.52; total 681,625.34. IUSC base 5,318,374.66: IUSC 419,464.03. Net pay CLP 4,898,910.63.

The figure that decides is the commission saved less the extra tax: the commission is deductible for IUSC, so CLP 36,751.64 less commission raises his IUSC by 23% of it, CLP 8,452.88. Uno leaves him CLP 28,298.76 more a month. A worker under the exempt band keeps the whole commission saving. (Service, fund returns and the choice of fund are not compared here.) The employer's cost does not change with the AFP: 3.5% of 3,712,286.70 = 129,930.03, unemployment 2.4% of 5,576,679.58 = 133,840.31, work-accident 0.90% = 33,410.58 and SANNA 1,113.69 (on the 90 UF ceiling).

```oa-check
name: CL payroll October 2026, CLP 6m above the ceilings, Provida against Uno
inputs:
  gross: 6000000
  uf: 41247.63
steps:
  - cap: round(90 * uf, 2)
  - cap_cesantia: round(135.2 * uf, 2)
  - afp: round(cap * 0.10, 2)
  - health: round(cap * 0.07, 2)
  - cesantia_worker: round(min(gross, cap_cesantia) * 0.006, 2)
  - commission_provida: round(cap * 0.0145, 2)
  - commission_uno: round(cap * 0.0046, 2)
  - iusc_provida: round((gross - afp - commission_provida - health - cesantia_worker) * 0.23 - 803762.14, 2)
  - iusc_uno: round((gross - afp - commission_uno - health - cesantia_worker) * 0.23 - 803762.14, 2)
  - net_provida: gross - afp - commission_provida - health - cesantia_worker - iusc_provida
  - net_uno: gross - afp - commission_uno - health - cesantia_worker - iusc_uno
  - gain_uno: net_uno - net_provida
  - employer_pension: round(cap * 0.035, 2)
  - employer_cesantia: round(cap_cesantia * 0.024, 2)
expected:
  cap: 3712286.70
  cap_cesantia: 5576679.58
  iusc_provida: 411011.15
  iusc_uno: 419464.03
  net_provida: 4870611.87
  net_uno: 4898910.63
  gain_uno: 28298.76
  employer_pension: 129930.03
  employer_cesantia: 133840.31
```

## Ask the client first

1. Which month is the pay for? Before or from August 2026 changes the employer pension contribution (1% plus SIS, or 3.5% with SIS inside), and the month sets the IUSC table and the UF.
2. The contract type (indefinite, fixed-term, per job), the start date (the 11-year unemployment rule) and the worker's age, and whether the worker is a pensioner.
3. Gross pay and how it splits between taxable remuneration and allowances that are not remuneration.
4. The worker's AFP (commission), health institution (Fonasa or Isapre and the plan price), and any APV through the employer.
5. The company's work-accident insurer (mutual or ISL) and its additional rate, and whether any job is classed as heavy work.
6. Any second job, medical leave in the month, or a worker not resident in Chile.

## Sources

| Source | URL | Read on |
|---|---|---|
| DL 3.500, LeyChile consolidated text in force on 11 Nov 2026 (read in the XML export and the JSON text service): arts. 16, 17, 17 bis, 18, 19, 84 | https://www.bcn.cl/leychile/navegar?idNorma=7147 | 2026-11-11 |
| Ley 21.735 (DO 26 Mar 2025): art. 1, transitory arts. 4, 5 and 8 | https://www.bcn.cl/leychile/navegar?idNorma=1212060 | 2026-11-11 |
| Ley 19.728, seguro de desempleo, text in force on 11 Nov 2026: arts. 2, 5, 6, 7, 9, 10, 23 | https://www.bcn.cl/leychile/navegar?idNorma=184979 | 2026-11-11 |
| Ley 16.744: art. 15 | https://www.bcn.cl/leychile/navegar?idNorma=28650 | 2026-11-11 |
| Ley 21.063: art. 24 | https://www.bcn.cl/leychile/navegar?idNorma=1113014 | 2026-11-11 |
| DL 824, LIR, version of 17 Oct 2026: arts. 42 No. 1, 43 No. 1, 74 No. 1, 79 | https://www.bcn.cl/leychile/navegar?idNorma=6368 | 2026-11-11 |
| Read for the figures named: SP, final 2026 ceilings (90.0 UF and 135.2 UF from February 2026 pay; notice and PDF of 10 Feb 2026) | https://www.spensiones.cl/portal/institucional/594/w3-article-16921.html | 2026-11-11 |
| Read for the figures named: SP, Sistema de AFP page (commissions of the seven AFPs; SIS 1.78% from August 2026; split of the 3.5%) | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9897.html | 2026-11-11 |
| Read for the figures named: SP, SIS page (1.78% from August 2026) | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-9917.html | 2026-11-11 |
| Read for the figures named: SP, Cotización de cargo del empleador (1% Aug 2025 to Jul 2026; 3.5% Aug 2026 to Jul 2027; SIS inside the 2.5%; Previred fields 27, 29, 94, 95) | https://www.spensiones.cl/portal/institucional/594/w3-propertyvalue-10906.html | 2026-11-11 |
| Read for the figures named: SII, UF 2026 daily values (31 Oct 2026 CLP 41,247.63) | https://www.sii.cl/valores_y_fechas/uf/uf2026.htm | 2026-11-11 |
| Read for the figures named: SII, IUSC 2026 monthly tables (October and December read in full) | https://www.sii.cl/valores_y_fechas/impuesto_2da_categoria/impuesto2026.htm | 2026-11-11 |
| Read for the figures named: SII, declaraciones juradas 2026, forms and deadlines (F1887: 27 March, certificates by 14 March) | https://www.sii.cl/ayudas/ayudas_por_servicios/2120-formularios_y_plazos_2026-2171.html | 2026-11-11 |

Not yet confirmed: the SIS rate for January to July 2026 pay (the SP pages read give only the rate from August 2026); how the 2.5% Seguro Social Previsional part splits between the SIS (1.78%) and the life-expectancy compensation, and the CEV rate Previred applies; the January 2026 ceiling (the SP's preliminary 89.9 UF and 135.1 UF notice was not read); which day's UF the SP applies to the 90 UF ceiling; whether the Ley 21.735 contribution is due for workers over the legal age or for pensioners who keep working; whether the SANNA 0.03% is capped at 90 UF; whether an Isapre premium above 7% reduces the IUSC base; which allowances are not taxable remuneration (Código del Trabajo art. 41, not read); the additional work-accident rates (D.S. 110 and the insurer's notice); the AT 2027 DJ 1887 deadline; rounding of the IUSC to whole pesos; foreign technicians' exemption and social-security agreements.
