---
name: ecuador-payroll
description: "Ecuador employer payroll for tax year 2026: gross to net and employer cost for a worker in relación de dependencia. Covers the IESS contributions (aporte personal 9.45% and aporte patronal 11.15% for the private sector, set by IESS Resolución C.D. 501 under Ley de Seguridad Social arts. 11 to 15), the materia gravada and its exclusions, the 2026 salario básico unificado of USD 482 (Acuerdo Ministerial MDT-2025-195), the décimo tercero and décimo cuarto (Código del Trabajo arts. 111 to 114), fondos de reserva at 8.33% from the second year (arts. 196 to 202), overtime, profit sharing (15% utilidades), monthly income tax withholding by annual projection divided by 11 (RLRTI art. 104), the IESS and SRI deadlines and the penalties. Trigger on: rol de pagos, nómina Ecuador, aporte IESS 9.45%, aporte patronal 11.15%, décimo tercero, décimo cuarto, fondos de reserva, salario básico 2026, retención en relación de dependencia, gross to net Ecuador, employer cost Ecuador. Out of scope: the employ"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ecuador-payroll"
  jurisdiction: "EC"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Ecuador: employer payroll (2026) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill runs a monthly payroll in Ecuador for employees in relación de dependencia in 2026: what the employer withholds, what it adds, and where each amount goes. It links to the other Ecuador skills and does not repeat them:

- [ecuador-income-tax](ecuador-income-tax.md): the 2026 income tax table, the gastos personales rebate and its caps, exempt income and the employee's own annual return.
- [ecuador-social-contributions](ecuador-social-contributions.md): IESS for the self-employed, voluntary affiliates and other non-employee affiliates.
- [ec-corporate-income-tax](ec-corporate-income-tax.md): deductibility of payroll in the company's return.
- [ec-cross-border](ec-cross-border.md): payments to people and companies abroad.

**Quick reference (2026).** Currency: US dollar. Salario básico unificado (SBU): USD 482 a month from 1 January 2026. IESS, private sector: employee 9.45%, employer 11.15%, total 20.60% of the materia gravada, paid within 15 days after the month. Décimo tercero: one twelfth of the month's pay, paid monthly unless the worker asks in writing to have it by 24 December. Décimo cuarto: one twelfth of the SBU (USD 40.17) a month, or USD 482 accumulated by 15 March (Costa and Galápagos) or 15 August (Sierra and Amazonía). Fondos de reserva: 8.33% from the 13th month of service. Income tax: projected annual pay less IESS, table, less rebate, divided by 11, withheld from February; nothing withheld from January pay.

**Which texts.** Ley de Seguridad Social (Ley 55, RO Supl. 465 of 30 Nov 2001, IESS copy with last reform 26 June 2025); IESS Consejo Directivo Resolución C.D. 501 of 13 November 2015 (consolidated contribution tables); Código del Trabajo (Codificación 2005-017, Ministerio del Trabajo copy with last reform RO Supl. 309 of 12 May 2023); Acuerdo Ministerial MDT-2025-195 of 15 December 2025 (SBU 2026); the LRTI (SRI codification, last reform 1 April 2026) and its Reglamento (RLRTI, last reform 18 November 2025).

## Who this applies to

- **Employers** of any worker in relación de dependencia, whether a company or an individual. The employer must enrol the worker with the IESS from the first day of work and send the aviso de entrada within the first 15 days (LSS art. 73). It withholds the employee's share and pays both shares (LSS art. 73) and withholds income tax monthly (LRTI art. 43; RLRTI art. 104).
- **Who must be affiliated.** Everyone who earns income from work or services, with or without an employment relationship, starting with the worker in relación de dependencia (LSS art. 2(a)). The self-employed, professionals, business owners and unpaid home workers are also obliged (art. 2(b) to (h)); their contributions are in [ecuador-social-contributions](ecuador-social-contributions.md).
- **Which rate table.** C.D. 501 art. 1 sets one table per group. This skill computes the first: private-sector workers in relación de dependencia and secular clergy (9.45% / 11.15%). The other groups are in the rates table below with their own split.
- **Agricultural employers** are exempt from sending avisos de entrada and de salida; service time is credited to the workers (LSS art. 73).
- **Out of scope**: the military and police schemes (ISSFA, ISSPOL), public-sector pay scales, the Seguro Social Campesino regime, and the employee's annual income tax return (ecuador-income-tax).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Salario básico unificado (SBU), workers in general, including small industry, farm, maquila, paid home workers, craft operatives and microenterprise workers | USD 482.00 a month from 1 January 2026 | 2026 | https://www.trabajo.gob.ec/wp-content/uploads/downloads/2026/01/ACUERDO-MINISTERIAL-MDT-2025-195.pdf (Acuerdo MDT-2025-195, artículo único) |
| IESS aporte personal, private sector in relación de dependencia | 9.45% of materia gravada, withheld from pay | 2026 | https://iess.gob.ec/documents/10162/33703/C.D.+501 (C.D. 501 art. 1, Primera); https://www.iess.gob.ec/documents/13718/54965/Tasasdeaportacion.pdf |
| IESS aporte patronal, private sector in relación de dependencia | 11.15% of materia gravada, on top of pay | 2026 | same |
| Total, private sector | 20.60% | 2026 | same |
| Of the 9.45%: Ley Orgánica de Discapacidades | 0.10% (all affiliates pay it) | 2026 | same; https://www.iess.gob.ec/es/web/empleador/tasas-de-aportacion (C.D. 464, Disposición General Segunda) |
| Bank employees, decentralised local governments and public entities, property and commercial registrars | personal 11.45%, patronal 11.15%, total 22.60% | 2026 | https://iess.gob.ec/documents/10162/33703/C.D.+501 (C.D. 501 art. 1, Segunda) |
| Public servants including teachers and the judiciary, and notaries | personal 11.45%, patronal 9.15%, total 20.60% | 2026 | same (Tercera) |
| Foreign-service officials resident abroad | personal 9.45%, patronal 9.15%, total 18.60% | 2026 | same (Cuarta) |
| Temporary sugar-industry workers | personal 18.90%, patronal 22.30%, total 41.20% | 2026 | same (Quinta) |
| Minimum contribution base, full-time worker | the monthly base pay may never be below the SBU, the sectoral minimum, the minimum under a professional-defence law or the public pay scale, whichever applies to the activity | 2026 | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social (LSS art. 11, third paragraph); https://www.iess.gob.ec/es/web/empleador/salarios-de-aportacion |
| Part-time worker | base by days worked, never below the proportional part of the SBU; the 4.41% health premium is paid on at least the full SBU | 2026 | https://www.iess.gob.ec/es/web/empleador/obligaciones |
| Exclusions from materia gravada (meals, medical, life and accident premiums, work clothes and tools, social services) | not contributable; together capped at 20% of the worker's contributable pay | 2026 | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social (LSS art. 14(1) to (5) and last paragraph) |
| Utilidades (profit share) and the compensación para el salario digno | not materia gravada, with no cap | 2026 | same (LSS art. 14(6), (7); art. 11) |
| Décimo tercero (decimotercera remuneración) | one twelfth of the remuneration received, paid monthly; on the worker's written request, accumulated and paid by 24 December | 2026 | https://www.trabajo.gob.ec/wp-content/uploads/2024/01/CODIGO_DEL_TRABAJO-CT.pdf (CT art. 111) |
| Décimo cuarto (decimocuarta remuneración) | one twelfth of the SBU a month (482 / 12 = USD 40.17); on written request, accumulated and paid by 15 March (Costa and Insular regions) or 15 August (Sierra and Amazonía); proportional part on leaving | 2026 | same (CT art. 113); SBU from the first row |
| Décimo tercero and décimo cuarto: IESS, fondos de reserva, income tax | not part of pay for IESS contributions, fondos de reserva, jubilación, indemnities, holidays or income tax on employment | 2026 | same (CT arts. 112, 114); https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 9) |
| Fondos de reserva | one month's pay for each full year after the first; paid monthly with pay at 8.33% of the remuneración de aportación, or deposited monthly with the IESS if the worker applies for accumulation | 2026 | https://www.trabajo.gob.ec/wp-content/uploads/2024/01/CODIGO_DEL_TRABAJO-CT.pdf (CT arts. 196, 201); https://www.iess.gob.ec/es/web/empleador/fondos-de-reserva |
| Overtime (horas suplementarias), up to 4 a day and 12 a week, with written agreement and inspector authorisation | +50% up to 24:00; +100% between 24:00 and 06:00; +100% on Saturday or Sunday | 2026 | https://www.trabajo.gob.ec/wp-content/uploads/2024/01/CODIGO_DEL_TRABAJO-CT.pdf (CT art. 55) |
| Utilidades (participación laboral) | 15% of net profits: 10% split equally among workers, 5% in proportion to family dependants (cargas familiares) | 2026 | same (CT art. 97) |
| Utilidades: liquidation and payment | liquidated by 31 March; each worker's share paid within 15 days of the liquidation | 2026 | same (CT art. 105) |
| Income tax on pay | Tabla No. 1 of LRTI art. 36(a), 2026 version (exempt band USD 12,208; 0% to 37%); applied by annual projection, see The base | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf (Res. NAC-DGERCGC25-00000043 art. 2); full table in ecuador-income-tax |

## The base

**Materia gravada (LSS art. 11).** Every income with a money value received by the affiliate. For a worker in relación de dependencia it includes the basic monthly pay plus overtime (extraordinary and supplementary hours), piece work, commissions, sobresueldos, bonuses (gratificaciones), fees, profit-related payments, rights of use and housing, and any other accessory pay that is normal in the industry or service. It excludes the items in LSS art. 14 (meals, medical cover, life and accident premiums, work clothes and tools, social services; together at most 20% of the contributable pay), the utilidades and the compensación para el salario digno. It also excludes the décimo tercero and décimo cuarto (CT arts. 112, 114). Fondos de reserva are not part of remuneration (CT art. 95) and payments to the IESS are not subject to income tax withholding (RLRTI art. 105(1)).

**The IESS computation, each month.**

1. Materia gravada for the month, at least the SBU (or the sectoral minimum) for a full-time worker (LSS art. 11).
2. Aporte personal = materia gravada × 9.45%, withheld from pay.
3. Aporte patronal = materia gravada × 11.15%, paid by the employer.
4. Fondos de reserva, from the 13th month of service with the same employer (CT art. 196): materia gravada × 8.33%. Paid to the worker with the pay, or to the IESS with the planilla where the worker asked for accumulation (IESS fondos de reserva page; CT art. 201). A worker who leaves before completing the first year has no right to fondos; one who returns to the same employer adds the earlier service (CT art. 197). A change of owner does not interrupt service (CT art. 198).

**Remuneration for the décimo tercero, fondos and indemnities (CT art. 95).** Everything the worker receives in money, services or kind, including overtime, piece work, commissions, profit participation and the employee's IESS share where the employer bears it. It excludes the legal utilidades, the monthly fondos de reserva payment, occasional travel allowances or subsidies, the décimo tercero and décimo cuarto, the compensación para el salario digno and social services.

**Income tax withholding (LRTI art. 43; RLRTI art. 104).** The employer withholds every month:

1. Add up all pay due to the worker projected for the whole year, except the décimo tercero and décimo cuarto.
2. Subtract the worker's aporte personal to the IESS (LRTI art. 17), and the over-65 or disability exemptions where they apply.
3. Apply Tabla No. 1 (2026) to get the projected tax (see ecuador-income-tax for the table).
4. Subtract the rebate on the gastos personales the worker projected for the year, within the legal caps, using the January 2026 canasta familiar básica (or the last known value until it is published).
5. Divide by 11. That is the monthly withholding from February pay onwards. **January pay is not withheld.**
6. Re-project when pay changes.

The worker hands the employer a projection of gastos personales, with the number of cargas familiares, during February (RLRTI art. 104). The rebate rate, the canasta (USD 821.80 for 2026) and the caps by number of dependants are in [ecuador-income-tax](ecuador-income-tax.md).

**What is and is not taxed pay for withholding.**

| Item | IESS | Income tax withholding | Rule |
|---|---|---|---|
| Base pay, overtime, commissions, habitual bonuses | yes | yes | LSS art. 11; RLRTI art. 104 |
| Voluntary individual bonuses, agasajos and subsidies | yes if habitual | yes (agasajos with no personal income excluded) | RLRTI art. 106 |
| Décimo tercero, décimo cuarto | no | no | CT arts. 112, 114; LRTI art. 9; RLRTI art. 104 |
| Fondos de reserva | no | no | CT art. 95; RLRTI art. 105(1) |
| Utilidades | no (LSS art. 14(6)) | RLRTI art. 104 excludes only the 13th and 14th from the projection | LSS art. 14; RLRTI art. 104 |
| Meals, medical cover, work clothes (within the 20% cap) | no | see ecuador-income-tax for exempt income | LSS art. 14 |
| Travel, lodging and meals for the job, documented | not pay | no withholding | RLRTI art. 105(4); LRTI art. 9(11) |
| Lodging and meals while working away from home; relocation and return costs of a worker hired to work away from home | not pay | not income, no withholding | RLRTI art. 107 |
| Employer pays the employee's IESS share or income tax | the assumed IESS share is remuneration (CT art. 95) | the tax borne by the employer is added once to the base | LRTI art. 17 |

## Deadlines and filing

| Item | Deadline | Source URL |
|---|---|---|
| Enrol a new worker with the IESS | from the first day of work; aviso de entrada within the first 15 days | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social (LSS art. 73); https://www.iess.gob.ec/es/web/empleador/avisos-de-entrada-y-salida |
| Report a change of pay, illness, departure (aviso de salida) or other event | within 3 days of the event | same |
| Pay the IESS planilla (aporte personal + aporte patronal) | within 15 days after the month the contributions relate to; a due date on a Saturday, Sunday or rest day moves to the next business day | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social (LSS art. 73); https://www.iess.gob.ec/es/web/empleador/mora-patronal |
| Fondos de reserva deposited with the IESS | within the first 15 days of the following month | https://www.iess.gob.ec/es/web/empleador/fondos-de-reserva |
| Declare and pay income tax withheld in a month | next month by the ninth digit of the RUC: 1 = 10th, 2 = 12th, 3 = 14th, 4 = 16th, 5 = 18th, 6 = 20th, 7 = 22nd, 8 = 24th, 9 = 26th, 0 = 28th; Galápagos up to the 28th; holiday rule as below | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 102) |
| Due date on a rest day or holiday | moves to the next business day, unless that falls in the next month; then to the last business day of the due month | same |
| Withholding receipt (comprobante de retención) for employment income | delivered to the worker during January for the previous year's pay | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 50) |
| Worker's projection of gastos personales to the employer | during February | RLRTI art. 104, same URL as the withholding row |
| Décimo tercero, accumulated | by 24 December | https://www.trabajo.gob.ec/wp-content/uploads/2024/01/CODIGO_DEL_TRABAJO-CT.pdf (CT art. 111) |
| Décimo cuarto, accumulated | by 15 March (Costa, Insular) or 15 August (Sierra, Amazonía) | same (CT art. 113) |
| Utilidades | liquidation by 31 March; payment within 15 days after | same (CT art. 105) |

**How to run the month, step by step.**

1. Log in to the IESS employer system (www.iess.gob.ec, empleadores, servicios en línea) with the employer's cédula or RUC and password. Send the aviso de entrada for each new worker and any novedades (pay changes, departures) within the deadlines above.
2. Compute each worker's materia gravada, aporte personal, aporte patronal and, from the 13th month, fondos de reserva.
3. Compute the income tax withholding by the projection method (from February).
4. Pay net pay plus, unless the worker asked for accumulation, the monthly décimo tercero, décimo cuarto and fondos de reserva.
5. Pay the IESS planilla generated by the system within 15 days after the month, with the fondos de reserva of workers who chose accumulation.
6. Declare and pay the income tax withheld through SRI en línea by the ninth-digit date of the next month.
7. In January, give each worker the comprobante de retención for the previous year's pay.

## Penalties and interest

| Item | Rule | Source URL |
|---|---|---|
| Late IESS contributions, fondos de reserva or IESS loan deductions (mora patronal) | interest at the Banco Central del Ecuador's maximum conventional rate at the settlement date, plus 4 points | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social (LSS art. 89) |
| Mora patronal on benefits | the employer is liable (responsabilidad patronal) for the benefits the worker claims in health, pensions, work risks and cesantía | https://www.iess.gob.ec/es/web/empleador/mora-patronal |
| Aviso de entrada not sent | fine of 4% of the contribution on the last contributable pay of each worker concerned, borne by the employer; collected if unpaid within 15 days of the month after the planilla | https://www.iess.gob.ec/es/web/empleador/insentivos-y-sanciones (C.D. 516 arts. 19, 20) |
| Payment arrangements for arrears | partial-payment agreements up to 12 months, agreements from 13 to 24 months, and purga de mora agreements | https://www.iess.gob.ec/es/web/empleador/mora-patronal |
| Income tax not withheld, or withheld in part | fine equal to the tax that should have been withheld, plus interest; the employer stays jointly liable | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI art. 50(1)) |
| Late withholding return | as for any late return under LRTI art. 100 (3% of the tax a month, capped at 100%; see ecuador-income-tax) | same (art. 50(2)) |
| Comprobante de retención not given to the worker | fine of 5% of the amount withheld | same (art. 50(3)) |
| Late payment of tax withheld | the tax with late interest, plus the Código Tributario sanctions | same (art. 50, last paragraph) |
| Breach of the Código del Trabajo with no specific penalty (for example, décimos or utilidades not paid) | fines up to USD 200 by the Director Regional del Trabajo; up to USD 50 by judges and labour inspectors | https://www.trabajo.gob.ec/wp-content/uploads/2024/01/CODIGO_DEL_TRABAJO-CT.pdf (CT art. 628) |
| Fondos de reserva recovered through the courts from a worker not affiliated | the amount plus 50%; unaffiliated workers also receive 6% a year interest on fondos paid on departure | same (CT art. 202) |

## Cross-border points

- **Foreign workers employed in Ecuador** are affiliated like anyone else: LSS art. 2 covers all persons who earn income from work or services. Their pay for work in Ecuador is Ecuadorian-source income (LRTI art. 8(1)).
- **Occasional services by a non-resident.** Pay received by a non-resident individual for services occasionally provided in Ecuador (a stay of less than six months, consecutive or not, in a calendar year) is not Ecuadorian-source income where a foreign company pays it as part of its own income subject to withholding or exempt, or pays it abroad without charging it to an Ecuadorian company or permanent establishment (LRTI art. 8(1)). Otherwise it is taxed as in [ec-cross-border](ec-cross-border.md).
- **Residence** decides whether the projection method applies to all income or a non-resident rate does: see [ecuador-income-tax](ecuador-income-tax.md) (183 days, centre of interests).
- Social security agreements and posted-worker rules were not read for this skill.

## Two worked examples that recompute

### Example 1: worker on the SBU, second year, décimos and fondos paid monthly

María works full time in Quito (Sierra) for a private company. Her pay is the SBU, USD 482 a month. She joined in 2024, so fondos de reserva are due. She has not asked for accumulation, so the décimos and fondos are paid with her monthly pay.

- Aporte personal: 482 × 9.45% = 45.549, **USD 45.55**. Aporte patronal: 482 × 11.15% = 53.743, **USD 53.74**. IESS planilla: **USD 99.29**.
- Décimo tercero: 482 / 12 = **USD 40.17**. Décimo cuarto: 482 / 12 = **USD 40.17**. Fondos de reserva: 482 × 8.33% = **USD 40.15**.
- Income tax: projected base (482 − 45.55) × 12 = USD 5,237.40, below USD 12,208: **no withholding**.
- Net pay: 482 − 45.55 + 40.17 + 40.17 + 40.15 = **USD 556.94**.
- Employer cost: 482 + 53.74 + 40.17 + 40.17 + 40.15 = **USD 656.23**.

```oa-check
name: EC payroll 2026, SBU worker, second year, décimos and fondos monthly
inputs:
  pay: 482
  sbu: 482
  exempt_band: 12208
steps:
  - ee_iess: round(pay * 0.0945, 2)
  - er_iess: round(pay * 0.1115, 2)
  - planilla: ee_iess + er_iess
  - d13: round(pay / 12, 2)
  - d14: round(sbu / 12, 2)
  - fondos: round(pay * 0.0833, 2)
  - tax_base: (pay - ee_iess) * 12
  - below_band: max(exempt_band - tax_base, 0)
  - net_pay: pay - ee_iess + d13 + d14 + fondos
  - employer_cost: pay + er_iess + d13 + d14 + fondos
expected:
  ee_iess: 45.55
  er_iess: 53.74
  planilla: 99.29
  d13: 40.17
  d14: 40.17
  fondos: 40.15
  tax_base: 5237.40
  below_band: 6970.60
  net_pay: 556.94
  employer_cost: 656.23
```

### Example 2: USD 3,000 a month, one dependant, and monthly or accumulated décimos (a decision worked both ways)

Diego earns USD 3,000 a month in Guayaquil (Costa) and has worked for the employer since 2023. In February 2026 he hands in a projection of USD 5,000 of gastos personales with one carga familiar. He asks whether to take his décimos monthly or accumulated.

**Withholding.** Projected pay 3,000 × 12 = 36,000 (no décimos). Less aporte personal 9.45% × 36,000 = 3,402: base **USD 32,598**. The 2026 table band from 26,700 to 35,136 gives 1,412 + 15% × (32,598 − 26,700) = 1,412 + 884.70 = **USD 2,296.70**. Rebate: 18% of the lower of 5,000 and the one-dependant cap of 9 canastas (9 × 821.80 = 7,396.20) = **USD 900.00** (caps in ecuador-income-tax). Tax **USD 1,396.70**; withholding 1,396.70 / 11 = **USD 126.97** a month from February to December. January: nothing withheld.

**Monthly pay from February.** Aporte personal USD 283.50; aporte patronal 3,000 × 11.15% = USD 334.50; fondos 3,000 × 8.33% = USD 249.90. Before the décimos, he receives 3,000 − 283.50 − 126.97 + 249.90 = **USD 2,839.43**.

**The decision.** Taken monthly, each month adds 3,000 / 12 = USD 250.00 (décimo tercero) and USD 40.17 (décimo cuarto). Accumulated (written request), he receives the décimo tercero in one sum by 24 December and USD 482.00 of décimo cuarto by 15 March, the Costa date. Over a full year the totals are the same (USD 3,000 and one SBU), and neither choice changes the IESS base, the fondos or the income tax (CT arts. 112, 114; RLRTI art. 104). What decides it is cash timing only. Leaving before the payment date, he receives the proportional part either way (CT art. 113).

```oa-check
name: EC payroll 2026, USD 3,000, one dependant, projection divided by 11
inputs:
  pay: 3000
  gastos: 5000
  canasta: 821.80
  canastas_one_dependant: 9
  sbu: 482
steps:
  - annual_pay: pay * 12
  - ee_iess_year: annual_pay * 0.0945
  - base: annual_pay - ee_iess_year
  - tax_table: 1412 + (base - 26700) * 0.15
  - rebate: min(gastos, canastas_one_dependant * canasta) * 0.18
  - tax_year: tax_table - rebate
  - monthly_withholding: round(tax_year / 11, 2)
  - ee_iess: pay * 0.0945
  - er_iess: pay * 0.1115
  - fondos: round(pay * 0.0833, 2)
  - net_feb_before_decimos: pay - ee_iess - monthly_withholding + fondos
  - d13_monthly_total: round(pay / 12, 2) * 12
  - d14_monthly_total: round(sbu / 12, 2) * 12
expected:
  base: 32598
  tax_table: 2296.70
  rebate: 900.00
  tax_year: 1396.70
  monthly_withholding: 126.97
  ee_iess: 283.50
  er_iess: 334.50
  fondos: 249.90
  net_feb_before_decimos: 2839.43
  d13_monthly_total: 3000.00
  d14_monthly_total: 482.04
```

The monthly décimo cuarto of USD 40.17 adds up to USD 482.04 over 12 months; the law sets the accumulated amount at one SBU (USD 482.00), so the last monthly payment is the one to adjust.

## Ask the client first

1. Which group is the worker in (private sector, bank or local-government employee, public servant, other)? It sets the IESS rates.
2. Monthly materia gravada: base pay plus overtime, commissions and habitual bonuses; any meals, medical or clothing benefits (and are they within the 20% cap)?
3. Start date with this employer, including earlier service with the same employer (fondos de reserva from the 13th month).
4. Region of work (Costa and Galápagos, or Sierra and Amazonía) and whether the worker asked in writing to accumulate the décimos or the fondos.
5. The worker's February projection of gastos personales and number of cargas familiares; over 65 or disability.
6. The ninth digit of the employer's RUC (withholding due date), and whether the employer is in Galápagos.

## Sources

| Source | URL | Read on |
|---|---|---|
| Acuerdo Ministerial MDT-2025-195 (15 Dec 2025): SBU USD 482 from 1 Jan 2026, whole document read | https://www.trabajo.gob.ec/wp-content/uploads/downloads/2026/01/ACUERDO-MINISTERIAL-MDT-2025-195.pdf | 2026-11-11 |
| IESS Consejo Directivo, Resolución C.D. 501 (13 Nov 2015): art. 1 tables Primera to Sexta, art. 2, Disposiciones and annexes read | https://iess.gob.ec/documents/10162/33703/C.D.+501 | 2026-11-11 |
| IESS, Tasas de aportación table (PDF linked from the IESS employer page) | https://www.iess.gob.ec/documents/13718/54965/Tasasdeaportacion.pdf | 2026-11-11 |
| IESS, Tasas de aportación page (0.10% LOD note, C.D. 464) | https://www.iess.gob.ec/es/web/empleador/tasas-de-aportacion | 2026-11-11 |
| Ley de Seguridad Social, IESS copy (last reform 26 Jun 2025): arts. 2, 11 to 15, 73, 89 read | https://www.iess.gob.ec/documents/10162/34738848/12.+Ley+de+Seguridad+Social | 2026-11-11 |
| IESS employer pages: obligaciones, salarios de aportación, avisos de entrada y salida, fondos de reserva, mora patronal, incentivos y sanciones | https://www.iess.gob.ec/es/web/empleador/obligaciones ; https://www.iess.gob.ec/es/web/empleador/salarios-de-aportacion ; https://www.iess.gob.ec/es/web/empleador/avisos-de-entrada-y-salida ; https://www.iess.gob.ec/es/web/empleador/fondos-de-reserva ; https://www.iess.gob.ec/es/web/empleador/mora-patronal ; https://www.iess.gob.ec/es/web/empleador/insentivos-y-sanciones | 2026-11-11 |
| Código del Trabajo, Ministerio del Trabajo copy (Codificación 2005-017, last reform RO Supl. 309 of 12 May 2023): arts. 55, 95, 97, 97.1, 105, 111 to 114, 196 to 204, 628 read | https://www.trabajo.gob.ec/wp-content/uploads/2024/01/CODIGO_DEL_TRABAJO-CT.pdf | 2026-11-11 |
| LRTI, SRI codification (last reform 1 Apr 2026): arts. 8, 9, 17, 43, 50 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| RLRTI, SRI codification (last reform 18 Nov 2025): arts. 102 to 107 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| SRI Resolution NAC-DGERCGC25-00000043 (29 Dec 2025): 2026 table, art. 2 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf | 2026-11-11 |

Not yet confirmed: the split of the 11.15% employer rate by fund in 2026 (C.D. 501's annex "año 2021 en adelante" prints a private-sector patronal total of 10.97% with work-risk 0.20%, while its own bank-employee table and the IESS Tasas de aportación PDF give 11.15%; the totals used here are the 9.45% / 11.15% of C.D. 501 art. 1 and the IESS table, and no fund split is given); whether any later Consejo Directivo resolution changed C.D. 501's tables; the 0.5% IECE and 0.5% SECAP employer levies that the old version added (no primary text read); whether any upper limit on materia gravada applies to dependent workers (LSS art. 12(c) refers to maximum limits in the Law; none was found for them); the SRI form numbers for the monthly withholding return and the annual employee certificate (Formularios 103 and 107 in the old version) and the RDEP annex with its 2027 dates; the Ministerio del Trabajo (SUT) registration deadlines for the décimos and utilidades; Código del Trabajo reforms after 12 May 2023; the status of the 24-SBU cap on utilidades in CT art. 97.1 after Corte Constitucional ruling 002-18-SIN-CC; social security agreements for foreign workers.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ecuador-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ecuador-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
