---
name: uruguay-payroll
description: "Uruguay payroll for employers, tax year 2026: the monthly gross-to-net for a private-sector employee and the employer's cost. Covers BPS contributions (jubilatorio 15% employee and 7.5% employer, FONASA 3% to 8% employee by income and family and 5% employer, FRL 0.10% each side, FGCL 0.025% employer), the 2026 contribution ceilings (UYU 288,836 from February 2026) under Ley 16.713 and the Ley 20.130 pension reform, the employer's monthly IRPF withholding under Decreto 148/007 (monthly scale in BPC at UYU 6,864, the 6% gross-up above 10 BPC, the 14% or 8% deduction credit, form 3100), aguinaldo and salario vacacional, the year-end ajuste anual, the BPS nómina calendar, the 2026 minimum wage and BPS late-payment fines. Trigger on: nómina Uruguay, sueldo líquido, aportes BPS, montepío, FONASA, FRL, retención IRPF, formulario 3100, ajuste anual, aguinaldo, tope de cotización, Uruguay payroll 2026. Out of scope: domestic, rural and construction workers, public bodies, the employee's own IRP"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/uruguay-payroll"
  jurisdiction: "UY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Uruguay payroll for 2026 v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill runs a monthly payroll for an employee of a private-sector employer in Uruguay ("Industria y Comercio" affiliation at BPS) in 2026: the employee's BPS contributions, the IRPF the employer withholds, net pay, and the employer's own contributions. It links to the other Uruguay skills and does not repeat them:

- [uruguay-income-tax](uruguay-income-tax.md): the employee's annual IRPF, the annual scale, who must file forms 1102 and 1103, DGI penalties.
- [uruguay-social-contributions](uruguay-social-contributions.md): the BPS contribution rules beyond the private-sector employee, including the self-employed (unipersonales) and partners.
- [uy-cross-border](uy-cross-border.md): non-resident employees (IRNR) and the IRNR option for foreign staff.

**Which text of the law.** Ley 16.713 (pension system, 1995), Ley 20.130 (pension reform, Sistema Previsional Común, 2023), Ley 18.211 (FONASA rates), Decreto 148/007 (IRPF regulation, withholding on wages in arts. 60 to 65), as consolidated on IMPO; the 2026 values as published by BPS, which sets and collects them, and by DGI.

**Quick reference, 2026**

| Item | Figure |
|---|---|
| Tax year | Calendar year 2026; pay is declared and paid to BPS the month after the work month |
| BPC 2026 | UYU 6,864 a month from 1 January 2026 (Decreto 11/026) |
| Employee BPS | Jubilatorio 15% + FONASA 3% to 8% + FRL 0.10% |
| Employer BPS | Jubilatorio 7.5% + FONASA 5% (plus the cuota mutual top-up where due) + FRL 0.10% + FGCL 0.025% |
| Jubilatorio ceiling, mixed (AFAP) regime | UYU 288,836 a month from February 2026 (UYU 272,564 for January 2026) |
| IRPF withholding | Monthly scale 0% up to 7 BPC (UYU 48,048), then 10% to 36%; pay over 10 BPC is grossed up by 6%; credit of 14% (pay up to 15 BPC, UYU 102,960) or 8% of deductions |
| Minimum wage | UYU 24,572 a month from 1 January 2026; UYU 25,383 from 1 July 2026 |

## Who this applies to

- **Employers.** Any employer of dependent workers must register each worker with BPS (alta), report changes and leavers (baja) through the GAFI service, and send the monthly nómina of all staff through the declaración nominada ([BPS, declarar al personal](https://www.bps.gub.uy/818/declarar-al-personal.html)). All persons doing paid work in Uruguay, dependent or not, fall under BPS unless another fund covers the activity (Ley 20.130 art. 3(1)).
- **Employer as IRPF withholder.** Employers of active BPS affiliates are responsables sustitutos and withhold IRPF on wages every month (Decreto 148/007 arts. 61 to 63). BPS receives the withholding data with the nómina, calculates the amount and bills it (art. 65).
- **Employees covered here.** Private-sector employees affiliated to BPS under "Industria y Comercio". Employees affiliated to the bank, notarial, professional, military and police funds are withheld under DGI rules instead (arts. 67 and 68).
- **Which pension regime.** Three groups pay the same 15% and 7.5% but split them differently and meet the ceiling differently:
  1. Workers whose first job began on or after the start of the Sistema Previsional Común (1 December 2023, per [BPS values note 5](https://www.bps.gub.uy/5478/valores-actuales.html)): Ley 20.130 arts. 21 and 22.
  2. Workers already in the mixed regime of Ley 16.713 (BPS plus an AFAP) before that date: Ley 16.713 arts. 7 and 8, kept for them by Ley 20.130 art. 22.
  3. Workers outside the mixed regime: BPS states the contribution ceiling only for workers "incorporados al nuevo régimen jubilatorio (AFAP)" ([BPS, topes](https://www.bps.gub.uy/10306/topes-de-cotizacion.html)); confirm their position with BPS.
- **Out of scope.** Domestic work, rural employers (they pay every four months), construction under the aporte unificado, public bodies (their employer rate differs, per [BPS, tasas](https://www.bps.gub.uy/835/tasas.html)), servicios bonificados, the self-employed, and the employee's own annual return.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| BPC from 1 January 2026 | UYU 6,864 a month | 2026 | https://www.impo.com.uy/bases/decretos/11-2026 (art. 1) |
| Jubilatorio, employee (montepío), on all pay subject to contributions | 15% | 2026 | https://www.bps.gub.uy/835/tasas.html; Ley 16.713 art. 181, https://www.impo.com.uy/bases/leyes/16713-1995; for new entrants Ley 20.130 art. 21(1), https://www.impo.com.uy/bases/leyes/20130-2023 |
| Jubilatorio, employer (patronal), Industria y Comercio, since 1 July 2007 | 7.5% | 2026 | https://www.bps.gub.uy/835/tasas.html |
| Mixed regime (Ley 16.713) levels: tope A, B and C | UYU 96,279 / 144,418 / 288,836 a month (values for October and November 2026; A and B shown in force from January 2026, C from February 2026) | 2026 | https://www.bps.gub.uy/5478/valores-actuales.html; history at https://www.bps.gub.uy/5479/valores-historicos.html |
| Tope C in January 2026 (value in force from February 2025 until the February 2026 change) | UYU 272,564 | 2026 | https://www.bps.gub.uy/5479/valores-historicos.html |
| Ley 20.130 levels for the Sistema Previsional Común: nivel A and nivel B | UYU 144,418 (from January 2026) and UYU 288,836 (from February 2026) | 2026 | https://www.bps.gub.uy/5478/valores-actuales.html; Ley 20.130 arts. 22 and 25 |
| FONASA employee, pay up to 2.5 BPC (UYU 17,160), no spouse, with or without children | 3% | 2026 | https://www.bps.gub.uy/10314/tasas-fonasa.html |
| FONASA employee, pay up to 2.5 BPC, spouse or partner without SNIS cover of their own | 5% (3% + 2%) | 2026 | same |
| FONASA employee, pay over 2.5 BPC, no spouse, no children | 4.5% | 2026 | same; Ley 18.211 art. 61 B), https://www.impo.com.uy/bases/leyes/18211-2007 |
| FONASA employee, pay over 2.5 BPC, no spouse, with children | 6% | 2026 | same; Ley 18.211 art. 61 A) |
| FONASA employee, pay over 2.5 BPC, spouse without own SNIS cover, no children | 6.5% | 2026 | https://www.bps.gub.uy/10314/tasas-fonasa.html |
| FONASA employee, pay over 2.5 BPC, spouse without own SNIS cover, with children | 8% | 2026 | same |
| FONASA employer | 5% of pay subject to montepío, plus the Complemento de Cuota Mutual (CCM) where due | 2026 | same; Ley 18.211 art. 61 |
| Cuota mutual (value used for the CCM) | UYU 1,820 (January to June 2026); UYU 1,880 from July 2026 | 2026 | https://www.bps.gub.uy/5479/valores-historicos.html |
| FRL (Fondo de Reconversión Laboral), employee and employer, since 1 January 2019 | 0.10% each (0.125% until 31 December 2018) | 2026 | https://www.bps.gub.uy/10322/fondo-reconversion-laboral-frl.html |
| FGCL (Fondo de Garantía de Créditos Laborales), employer, private-sector dependants | 0.025% | 2026 | https://www.bps.gub.uy/15668/fondo-de-garantia-de-creditos-laborales.html (Ley 19.690) |
| IRPF monthly scale, up to 7 BPC (UYU 48,048) | 0% | 2026 | https://www.bps.gub.uy/23860/2026---comunicado-r-5---valores-escalas-irpf-2026.html (part 1); Decreto 148/007 art. 63, https://www.impo.com.uy/bases/decretos/148-2007 |
| Over 7 to 10 BPC (to UYU 68,640) | 10% | 2026 | same |
| Over 10 to 15 BPC (to UYU 102,960) | 15% | 2026 | same |
| Over 15 to 30 BPC (to UYU 205,920) | 24% | 2026 | same |
| Over 30 to 50 BPC (to UYU 343,200) | 25% | 2026 | same |
| Over 50 to 75 BPC (to UYU 514,800) | 27% | 2026 | same |
| Over 75 to 115 BPC (to UYU 789,360) | 31% | 2026 | same |
| Over 115 BPC | 36% | 2026 | same |
| Gross-up of monthly computable pay over 10 BPC (UYU 68,640), on the part subject to personal contributions, ignoring the AFAP ceiling | +6% | 2026 | https://www.impo.com.uy/bases/decretos/148-2007 (arts. 60 and 63(1)) |
| Deduction credit rate, monthly nominal pay (without aguinaldo and salario vacacional) up to 15 BPC (UYU 102,960) | 14% | 2026 | https://www.bps.gub.uy/23860/2026---comunicado-r-5---valores-escalas-irpf-2026.html (part 3); Decreto 148/007 art. 63(2) |
| Deduction credit rate, monthly nominal pay over 15 BPC | 8% | 2026 | same |
| Monthly deduction per minor child (20 BPC a year) | UYU 11,440 | 2026 | https://www.bps.gub.uy/23860/2026---comunicado-r-5---valores-escalas-irpf-2026.html (part 4) |
| Monthly deduction per dependant with a disability (40 BPC a year) | UYU 22,880 | 2026 | same |
| Fondo de Solidaridad, monthly deduction by category 1 to 5 | UYU 286 / 572 / 1,144 / 1,049 / 1,621 | 2026 | same |
| Monthly limit for exclusion from withholding (art. 64 bis) | UYU 68,300 | 2026 | same (part 2) |
| Reduction of withholding for an employee who meets DGI's conditions and asks for it | 5% of the computed withholding; the December ajuste is then capped at 20% of December pay | 2026 | https://www.impo.com.uy/bases/decretos/148-2007 (arts. 63 and 64) |
| Salario mínimo nacional | UYU 24,572 a month from 1 January 2026; UYU 25,383 from 1 July 2026 (divide by 25 for a day, by 200 for an hour) | 2026 | https://www.impo.com.uy/bases/decretos/319-2025 (arts. 1 and 2) |
| FONASA user threshold: a worker is a Seguro Nacional de Salud user from 13 days worked in the month or pay of 1.25 BPC | 1.25 BPC (UYU 8,580) | 2026 | https://www.impo.com.uy/bases/leyes/18211-2007 (art. 62) |
| FONASA year-end refund: personal contributions above 1.25 times the Costo Promedio Equivalente (CPE) of the worker and covered family are refunded | CPE UYU 6,858 a month (October and November 2026 value) | 2026 | Ley 18.211 art. 61; https://www.bps.gub.uy/5478/valores-actuales.html |

## The base

**What is pay.** Labour income from employment: regular or extraordinary pay, in money or in kind, including allowances and per diems paid without accounting; dismissal pay is taxed only above the legal minimum (Decreto 148/007 art. 48). The IRPF base cannot be lower than the pay subject to BPS contributions (art. 63).

**Step by step, one employee, one month.**

1. **Pay subject to contributions** for the month. Aguinaldo is subject to the same legal regime as salary (Ley 12.840 art. 4) and pays contributions; it is left out when choosing the FONASA band ([BPS, tasas FONASA](https://www.bps.gub.uy/10314/tasas-fonasa.html)), and under Ley 20.130 it counts as a separate income for the pillar split (art. 24). The salario vacacional (suma para el mejor goce de la licencia, Ley 16.101 art. 4) is free of social charges (Ley 12.590 art. 27) but is taxed in IRPF (Decreto 148/007 art. 48).
2. **Jubilatorio.** 15% employee and 7.5% employer, on pay up to the ceiling that fits the worker's regime:
   - Sistema Previsional Común (first job from 1 December 2023): of the 15%, 10% on pay up to nivel A goes to BPS, and 5% up to nivel A plus 15% between nivel A and nivel B goes to the AFAP; above nivel B the personal contribution is voluntary (Ley 20.130 art. 22). Art. 28 A counts the employer's contribution on pay up to the same amount (UYU 215,179 at 2022 values, adjusted under art. 25).
   - Ley 16.713 mixed regime: pay up to tope A is in the solidarity pillar (BPS), between A and C in the individual savings pillar (AFAP); above C saving is voluntary (Ley 16.713 art. 7). A worker who opted under art. 8 sends 50% of the first-level pay to the AFAP.
   - The ceiling bites the jubilatorio only. FONASA is on the total pay subject to montepío (Ley 18.211 art. 61), and FRL and FGCL are on full pay.
3. **FONASA employee** at 3% to 8%: choose the band by all pay subject to contributions in the month without aguinaldo (above or below 2.5 BPC, UYU 17,160), then the family line. The spouse lines apply only when the spouse or partner has no SNIS cover of their own. A child counts if under 18, or of any age with a disability, including the spouse's or partner's children (Ley 18.211 art. 61).
4. **FRL** 0.10% employee.
5. **IRPF to withhold** (Decreto 148/007 art. 63):
   - a. Take the month's computable pay without aguinaldo. If it exceeds 10 BPC (UYU 68,640), increase the part subject to personal contributions by 6%, measured before any AFAP ceiling.
   - b. Run that figure through the monthly scale.
   - c. Add the deductions: the employee's own jubilatorio, FONASA and FRL for the month, the Fondo de Solidaridad if any, UYU 11,440 per minor child or UYU 22,880 per dependant with a disability, and the other items of Título 7 art. 49 declared on form 3100. Deductions tied to the aguinaldo are left out of this step.
   - d. Multiply the deductions by 14% if monthly nominal pay (without aguinaldo and salario vacacional) is up to 15 BPC (UYU 102,960), otherwise by 8%.
   - e. Withholding = b minus d. Where the credit exceeds the tax, nothing is withheld that month.
   - f. If the employee meets DGI's conditions and asked for the 5% reduction, reduce the result by 5%.
6. **Aguinaldo and salario vacacional.** Taxed apart from the scale, at the highest marginal rate the employee's other labour income reaches; if that income and its deductions give no tax, the rate is zero (Decreto 148/007 art. 55 bis; Título 7 arts. 47 and 48). Only the legally required amounts get this treatment; amounts owed under collective agreements do not.
7. **Net pay** = gross pay minus employee jubilatorio, FONASA, FRL and IRPF.
8. **Employer cost** = gross pay plus 7.5% jubilatorio (to the ceiling), 5% FONASA plus any CCM, 0.10% FRL and 0.025% FGCL.

**Form 3100 and deductions.** The employee declares family circumstances and deductions to the employer on form 3100; the employer loads them into the BPS declaration. Without a form, the employer withholds with no deductions and the employee can claim them in the annual return. A new or changed form counts from the month after it is handed in; for the ajuste anual the date the deduction started counts ([BPS, IRPF](https://www.bps.gub.uy/10323/impuesto-a-la-renta-de-las-personas-fisicas-irpf.html); Decreto 148/007 art. 63).

**Exclusion from withholding.** An employee whose total employment income stays within the monthly limit set by the Executive (UYU 68,300 for 2026) can give the employer a sworn statement and be excluded from monthly withholding and from the ajuste anual, from the following month (or from the start of employment). If pay in a month exceeds the limit, the employer withholds anyway (Decreto 148/007 arts. 64 bis and 78 ter). The option is barred for a family-unit filer and for anyone with independent income (art. 78 ter).

**Ajuste anual.** At 31 December the employer recomputes the year with the information in force at that date, compares it with the withholdings made and withholds any balance due. A balance in the employee's favour is refunded by DGI. If the employee had only this employer all year, the withholding is final and the employee need not file; a family-unit filer, or one who took the 5% reduction, must file (Decreto 148/007 art. 64). BPS closes the year's IRPF information on 30 April of the next year; after that, corrections go to DGI ([BPS, IRPF](https://www.bps.gub.uy/10323/impuesto-a-la-renta-de-las-personas-fisicas-irpf.html)).

## Deadlines and filing

| Step | What | When | Where |
|---|---|---|---|
| Before the first hire | Register the company's wage-council group and subgroup; register each worker (alta) | Alta from 10 days before the start date up to the start date itself ([BPS guide, Industria y Comercio](https://www.bps.gub.uy/bps/file/10291/13/guia---industria-y-comercio.pdf)) | BPS online services, GAFI, or the BPS Empresas app ([BPS](https://www.bps.gub.uy/818/declarar-al-personal.html)) |
| Monthly | Nómina (declaración nominada) of all staff and pay for the work month, with the IRPF data from form 3100 | Month after the work month, by the BPS calendar date | BPS online services, declaración nominada |
| Monthly | Pay the BPS bill (jubilatorio, FONASA, FRL, FGCL) and the IRPF bill | Same calendar; the IRPF bill carries the DGI due date ([BPS, pago](https://www.bps.gub.uy/10357/pago-de-aportes.html)) | BPS service "Emitir facturas, declaración jurada de no pago y pagar aportes", or the collection network |
| If you cannot pay | File the nómina with a declaración jurada de no pago (DJNP) and pay at least the personal contributions withheld | By the due date | Same service |
| Leavers and changes | Register the baja or the change; a worker returning early from unemployment benefit within 5 working days | When it happens | GAFI |
| Year end | Ajuste anual of IRPF | December 2026 pay | December nómina |

**2026 calendar for most private employers** ("todos los demás contribuyentes", by the last digit of the BPS company number), [Resolución de Directorio 37-15/2025](https://www.bps.gub.uy/bps/file/23709/1/calendario-de-vencimientos-2026.pdf): in the month of payment, digits 0 to 4 / 5 to 9 are due on January 19 / 20, February 18 / 19, March 16 / 17, April 20 / 21, May 19 / 20, June 15 / 16, July 15 / 16, August 17 / 18, September 15 / 16, October 16 / 19, November 17 / 18, December 15 / 16. Paying by internet extends the payment date (not the nómina date) to January 23, February 24, March 20, April 24, May 25, June 22, July 21, August 21, September 21, October 22, November 23 and December 21. Seasonal companies are due on the fifth working day of the month. Large taxpayers ("mayores contribuyentes") and public bodies have earlier dates in the same calendar (for example November 12 for large taxpayers).

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| BPS late-payment fine, nómina filed on time with the DJNP | 2.5% if paid within 5 working days after the due date; 5% up to 90 calendar days; 10% after that | [BPS, multas y recargos](https://www.bps.gub.uy/18132/multas-y-recargos-por-mora.html) |
| BPS late-payment fine, nómina not filed on time with the DJNP | 5% / 10% / 20% for the same periods | same |
| BPS recargo (monthly surcharge on the unpaid amount, capitalised every four months) | 0.90% a month from January 2026; 0.80% a month from May 2026 | [BPS, valores históricos](https://www.bps.gub.uy/5479/valores-historicos.html) |
| Late or missing nómina | First time in the calendar year: 0.1 UR per worker not declared if paid or DJNP filed within the due month, 0.25 UR after; repeat: 0.2 UR and 0.5 UR; capped at 5 UR when the nómina was on time and only the payment or DJNP was late (UR UYU 1,948.97 in November 2026) | [BPS, multa por nómina](https://www.bps.gub.uy/10366/multa-por-nomina.html) (Ley 18.834 art. 281); UR at [BPS, valores actuales](https://www.bps.gub.uy/5478/valores-actuales.html) |
| Withheld contributions not paid over | Exposure to a criminal complaint for apropiación indebida | [BPS, pago de aportes](https://www.bps.gub.uy/10357/pago-de-aportes.html) |
| Good payer | Pay without fine or surcharge from the day after the due date to the end of that month (Código Tributario art. 94, RD 1-13/2008); December discount on employer contributions for micro (up to 4 people) and small (up to 19) firms with 12 regular payments (Ley 17.963) | [BPS, buenos pagadores](https://www.bps.gub.uy/10362/beneficios-buenos-pagadores.html) |
| IRPF withholding paid late | DGI fines and surcharges under Código Tributario art. 94 (see [uruguay-income-tax](uruguay-income-tax.md)); BPS bills it with the DGI due date and DGI's fine procedure applies | [BPS, IRPF](https://www.bps.gub.uy/10323/impuesto-a-la-renta-de-las-personas-fisicas-irpf.html) |

## Cross-border points

- **Posted abroad.** A dependent worker sent abroad for less than 183 days keeps Uruguayan affiliation, unless a social security agreement's posting rule applies; for longer periods worker and employer may agree to keep it for up to five years (Ley 20.130 art. 3(6)).
- **Working in Uruguay for a foreign employer with no permanent establishment.** The worker is covered by BPS as non-dependent, on the pay actually received, unless a dependent worker proves cover in the employer's country under an agreement in force (Ley 20.130 art. 3(7)).
- **Free-zone staff and foreign specialists.** Foreign staff in a free zone who are outside BPS can opt for IRNR on their wages; foreign IT specialists under contracts started up to 28 February 2025 could opt for IRNR for five years. Their employer withholds IRNR instead of IRPF. See [uy-cross-border](uy-cross-border.md).
- **Non-resident employees** are not in IRPF; their wages are IRNR income, withheld by the employer. See [uy-cross-border](uy-cross-border.md).

## Two worked examples that recompute

### Example 1: employee on UYU 120,000 a month, single, no children

Martina works full time for a Montevideo software firm in March 2026. Her monthly salary is UYU 120,000. She has no spouse or partner and no children, handed in form 3100 with no deductions, and is in the AFAP mixed regime. She pays no Fondo de Solidaridad.

BPS. Her pay is below the UYU 288,836 ceiling, so the jubilatorio is on all of it: 15% = UYU 18,000. Pay is above 2.5 BPC, single without children: FONASA 4.5% = UYU 5,400. FRL 0.10% = UYU 120. Employee contributions total UYU 23,520.

IRPF. Pay exceeds 10 BPC (UYU 68,640), so it is grossed up by 6% to UYU 127,200. On the scale: 10% of (68,640 - 48,048) = 2,059.20; 15% of (102,960 - 68,640) = 5,148.00; 24% of (127,200 - 102,960) = 5,817.60; tax UYU 13,024.80. Her nominal pay exceeds 15 BPC (UYU 102,960), so the credit is 8% of her deductions of UYU 23,520 = UYU 1,881.60. Withholding: UYU 11,143.20.

Net pay: 120,000 - 23,520 - 11,143.20 = UYU 85,336.80. The employer adds 7.5% jubilatorio (9,000), 5% FONASA (6,000), 0.10% FRL (120) and 0.025% FGCL (30): UYU 15,150, so the cost is UYU 135,150. The April BPS bill for March carries UYU 38,670 of contributions plus the IRPF of UYU 11,143.20.

```oa-check
name: Martina, UYU 120,000 a month, single, no children, March 2026
inputs:
  gross: 120000
  bpc: 6864
  ceiling: 288836
  fonasa_rate: 0.045
steps:
  - jub_ee: min(gross, ceiling) * 0.15
  - fonasa_ee: gross * fonasa_rate
  - frl_ee: gross * 0.001
  - ee_total: jub_ee + fonasa_ee + frl_ee
  - irpf_base: gross * 1.06
  - tax: (10 * bpc - 7 * bpc) * 0.10 + (15 * bpc - 10 * bpc) * 0.15 + (irpf_base - 15 * bpc) * 0.24
  - credit: ee_total * 0.08
  - irpf: tax - credit
  - net_pay: gross - ee_total - irpf
  - er_total: min(gross, ceiling) * 0.075 + gross * 0.05 + gross * 0.001 + gross * 0.00025
  - employer_cost: gross + er_total
  - to_bps: ee_total + er_total
expected:
  ee_total: 23520.00
  irpf_base: 127200.00
  tax: 13024.80
  credit: 1881.60
  irpf: 11143.20
  net_pay: 85336.80
  er_total: 15150.00
  employer_cost: 135150.00
  to_bps: 38670.00
```

### Example 2: pay above the ceiling, one child, and whether to declare the child on form 3100

Diego earns UYU 350,000 a month in March 2026 in the mixed regime. He has a son aged 9 and no spouse. Should he hand in a new form 3100 declaring the child, or leave the deduction to an annual return?

BPS. The jubilatorio stops at the ceiling: 15% of 288,836 = UYU 43,325.40. FONASA, above 2.5 BPC with a child: 6% of the full 350,000 = UYU 21,000. FRL 0.10% = UYU 350. Employee contributions: UYU 64,675.40.

IRPF. The 6% gross-up is on the full pay, ignoring the AFAP ceiling: UYU 371,000. On the scale: 2,059.20 + 5,148.00 + 24% of (205,920 - 102,960) = 24,710.40 + 25% of (343,200 - 205,920) = 34,320.00 + 27% of (371,000 - 343,200) = 7,506.00; tax UYU 73,743.60. Nominal pay is over 15 BPC, so the credit rate is 8%.

- **Child declared on form 3100:** deductions 64,675.40 + 11,440 = UYU 76,115.40; credit UYU 6,089.23; withholding UYU 67,654.37; net pay UYU 217,670.23.
- **Child not declared:** credit 8% of 64,675.40 = UYU 5,174.03; withholding UYU 68,569.57.

The decision: declaring the child cuts each month's withholding by UYU 915.20 (8% of UYU 11,440), from the month after he hands in the form. Not declaring it does not lose the deduction, but the excess comes back only through an annual return; with one employer settling his year in the ajuste anual, declaring it on form 3100 is the better route unless the other parent claims the child.

The employer pays 7.5% of 288,836 = 21,662.70, plus 5% FONASA (17,500), FRL (350) and FGCL (87.50) on full pay: UYU 39,600.20.

```oa-check
name: Diego, UYU 350,000 above the ceiling, one child, form 3100 both ways
inputs:
  gross: 350000
  bpc: 6864
  ceiling: 288836
  child: 11440
steps:
  - ee_total: min(gross, ceiling) * 0.15 + gross * 0.06 + gross * 0.001
  - irpf_base: gross * 1.06
  - tax: (10 * bpc - 7 * bpc) * 0.10 + (15 * bpc - 10 * bpc) * 0.15 + (30 * bpc - 15 * bpc) * 0.24 + (50 * bpc - 30 * bpc) * 0.25 + (irpf_base - 50 * bpc) * 0.27
  - credit_declared: round((ee_total + child) * 0.08, 2)
  - irpf_declared: tax - credit_declared
  - credit_not_declared: round(ee_total * 0.08, 2)
  - irpf_not_declared: tax - credit_not_declared
  - monthly_saving: irpf_not_declared - irpf_declared
  - net_pay_declared: gross - ee_total - irpf_declared
  - er_total: min(gross, ceiling) * 0.075 + gross * 0.05 + gross * 0.001 + gross * 0.00025
expected:
  ee_total: 64675.40
  tax: 73743.60
  irpf_declared: 67654.37
  irpf_not_declared: 68569.57
  monthly_saving: 915.20
  net_pay_declared: 217670.23
  er_total: 39600.20
```

## Ask the client first

1. Which month: the ceiling (January 2026 against February onward) and the minimum wage (before or from 1 July 2026) change within the year.
2. The employee's pension regime: first job before or after 1 December 2023, AFAP mixed regime or not, and any art. 8 option.
3. Family situation for FONASA: spouse or partner and whether they have their own SNIS cover; children under 18 or with a disability.
4. Form 3100: what the employee declared and when, other employers, Fondo de Solidaridad or Caja Profesional payments, and any request for the 5% reduction or for exclusion from withholding.
5. Gross pay for the month split into salary, aguinaldo, salario vacacional, benefits in kind, dismissal pay and amounts under collective agreements.
6. The employer's BPS affiliation (Industria y Comercio or another), company number (its last digit fixes the due date) and wage-council group.

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley 16.713, IMPO consolidated text: arts. 7, 8 (levels and option) and 181 to 183 (15% personal rate, employer rate cut) read | https://www.impo.com.uy/bases/leyes/16713-1995 | 2026-11-11 |
| Ley 20.130, IMPO consolidated text: arts. 1 to 9 and 18 to 28 read (inclusion, posting, new entrants' rate, pillar split, adjustment, solidarity resources) | https://www.impo.com.uy/bases/leyes/20130-2023 | 2026-11-11 |
| Ley 18.211, IMPO consolidated text: arts. 61 to 63 read (FONASA employer 5%, employee rates, user threshold, year-end refund) | https://www.impo.com.uy/bases/leyes/18211-2007 | 2026-11-11 |
| Ley 12.840, arts. 1 to 4 read (aguinaldo) | https://www.impo.com.uy/bases/leyes/12840-1960 | 2026-11-11 |
| Ley 16.101 art. 4 read (salario vacacional) | https://www.impo.com.uy/bases/leyes/16101-1989/4 | 2026-11-11 |
| Ley 12.590 art. 27 read (vacation sums free of social charges) | https://www.impo.com.uy/bases/leyes/12590-1958/27 | 2026-11-11 |
| Decreto 148/007, IMPO consolidated text: arts. 47, 48, 55, 55 bis, 56, 60 to 68 and 78 ter read (withholding on wages, gross-up, deductions, ajuste anual, exclusion) | https://www.impo.com.uy/bases/decretos/148-2007 | 2026-11-11 |
| Decreto 11/026, art. 1 read: BPC UYU 6,864 from 1 January 2026 | https://www.impo.com.uy/bases/decretos/11-2026 | 2026-11-11 |
| Decreto 319/025, arts. 1 and 2 read: minimum wage from 1 January and 1 July 2026 | https://www.impo.com.uy/bases/decretos/319-2025 | 2026-11-11 |
| BPS ATYR, Comunicado R 5/2026 (February 2026), both pages read: monthly scale, exclusion limit, deduction rates, child and Fondo de Solidaridad values | https://www.bps.gub.uy/23860/2026---comunicado-r-5---valores-escalas-irpf-2026.html | 2026-11-11 |
| DGI, IRPF categoría 2 escalas y alícuotas (page of 2 February 2026 and its workbook, monthly 2026 sheet read) | https://www.gub.uy/direccion-general-impositiva/politicas-y-gestion/irpf-categoria-2-escalas-alicuotas | 2026-11-11 |
| BPS, tasas de aporte jubilatorio (15% and 7.5%), page updated 6 July 2023, read in full | https://www.bps.gub.uy/835/tasas.html | 2026-11-11 |
| BPS, tasas FONASA (employee bands, socio vitalicio, employer 5% and CCM), page updated 23 October 2026, read in full | https://www.bps.gub.uy/10314/tasas-fonasa.html | 2026-11-11 |
| BPS, FRL page (0.10% since 2019), updated 21 October 2026, read in full | https://www.bps.gub.uy/10322/fondo-reconversion-laboral-frl.html | 2026-11-11 |
| BPS, FGCL page (0.025% employer), read in full | https://www.bps.gub.uy/15668/fondo-de-garantia-de-creditos-laborales.html | 2026-11-11 |
| BPS, topes de cotización page (who the ceiling applies to), read in full | https://www.bps.gub.uy/10306/topes-de-cotizacion.html | 2026-11-11 |
| BPS, valores actuales (October and November 2026 columns: BPC, minimum wage, cuota mutual, CPE, topes A to C, niveles A and B, UR, recargo) | https://www.bps.gub.uy/5478/valores-actuales.html | 2026-11-11 |
| BPS, valores históricos, 2025 and 2026 entries read for tope C, nivel B, minimum wage, cuota mutual and recargo | https://www.bps.gub.uy/5479/valores-historicos.html | 2026-11-11 |
| BPS, IRPF page read (form 3100 timing, BPS collection, 30 April closing) | https://www.bps.gub.uy/10323/impuesto-a-la-renta-de-las-personas-fisicas-irpf.html | 2026-11-11 |
| BPS, declarar al personal page read (GAFI, nómina) | https://www.bps.gub.uy/818/declarar-al-personal.html | 2026-11-11 |
| BPS, Guía de obligaciones Industria y Comercio (January 2025 edition, page updated 21 May 2026), all pages read: alta deadline, nómina, payment | https://www.bps.gub.uy/bps/file/10291/13/guia---industria-y-comercio.pdf | 2026-11-11 |
| BPS, pago de aportes page read (monthly payment, DJNP, minimum payment, IRPF bills) | https://www.bps.gub.uy/10357/pago-de-aportes.html | 2026-11-11 |
| BPS, calendario de vencimientos 2026 (Resolución de Directorio 37-15/2025), full table read | https://www.bps.gub.uy/bps/file/23709/1/calendario-de-vencimientos-2026.pdf | 2026-11-11 |
| BPS, multas y recargos por mora page read (fine percentages) | https://www.bps.gub.uy/18132/multas-y-recargos-por-mora.html | 2026-11-11 |
| BPS, multa por nómina page read (UR amounts) | https://www.bps.gub.uy/10366/multa-por-nomina.html | 2026-11-11 |
| BPS, beneficios buenos pagadores page read | https://www.bps.gub.uy/10362/beneficios-buenos-pagadores.html | 2026-11-11 |

Not yet confirmed: the two-instalment payment dates of the aguinaldo (June and December), which sit in a later law not read; whether the 6% gross-up also applies in the December ajuste anual; how deductions attached to the aguinaldo are credited; the CCM amount per worker; the BSE work-accident insurance premium, which BPS does not collect and which varies by activity; the employer rates of public bodies and of servicios bonificados; whether a worker outside the AFAP regime has any contribution ceiling; the socio vitalicio FONASA rates (the BPS table shows an inconsistent row for "sin cónyuge con hijos"); the annual limit for the art. 64 bis exclusion; the DGI form used by employers outside BPS (art. 68); the 2027 BPS calendar.

> Contributed by OpenAccountants.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `uruguay-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/uruguay-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
