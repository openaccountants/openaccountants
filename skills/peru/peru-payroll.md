---
name: peru-payroll
description: >
  Prepare ordinary private-sector Peru payroll for 2026, from remuneration and
  time records to fifth-category withholding, pension deductions, employer health
  contributions, net pay and filing reconciliation. Use for planilla, nómina,
  sueldo neto, gross to net, T-Registro, PLAME Form 0601, ONP, AFP, EPS,
  overtime, minimum wage, gratificaciones, CTS and employment-tax adjustments.
  Covers the October minimum-wage change, month-specific AFP components, actual
  withholding allocation, multiple employers, variable remuneration and cessation.
  Distinguishes employee liabilities from employer costs and bank payments from
  accepted filings. Ask for period, affiliation, tax domicile, remuneration
  components and cumulative records before computing. Special labour regimes,
  foreign social-security exemptions and unresolved source periods require their
  own documented assessment.
version: 0.2
jurisdiction: PE
tax_year: 2026
last_updated: 2026-11-11
checked_on: 2026-11-11
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: computation
---

# Peru payroll, tax year 2026 v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Use this method with `payroll-workflow-base` to prepare ordinary Peru private-sector employee payroll in PEN, reconcile statutory liabilities and produce a working paper for professional review. Employment income is fifth category under LIR art. 34. A calendar-year tax projection and a monthly contribution computation are different jobs: neither a monthly salary nor a bank credit establishes the complete annual tax base.

**Quick reference:** the ordinary employer withholds employee ONP or AFP and employment income tax; it separately bears EsSalud and applicable benefit/insurance costs. Confirm pension membership, commission arrangement, insurance eligibility, tax domicile, remuneration components, service month and previous withholding before calculating. Do not deduct employer EsSalud from salary, charge both pension systems, give each employer a separate 7 UIT deduction, use annual tax divided by twelve all year, or omit ordinary gratificaciones from the tax projection.

**Required inputs:** employee identity and contract/regime; service and payment month; ordinary salary, variable pay and taxable benefits; days/hours worked, paid leave, subsidy and unpaid suspension; ONP/AFP membership dates, administrator/commission arrangement and retirement documentation; actual SBS devengue schedule; EPS-covered workers and invoices/payments; tax-domicile/source facts; other employers and year-to-date income/withholding; employer RUC/status and filing receipts. Missing facts that change the result are questions to resolve, not conservative defaults.

This is not an automatic computation for public-sector, agricultural, construction, domestic-worker, fishing, artistic or special MYPE labour regimes. Tax regime and labour regime are different classifications. High-risk work can require employer-funded SCTR under Law 26790 art. 19. A gross-up, tax-equalisation agreement or foreign certificate can change the employer's actual cost and requires explicit instructions. Do not call 9% health the employer's only possible payroll cost.

Fourth-category independent fees are outside employee payroll. Resolve the real employment relationship before accepting a contractor label; the annual work-income and independent contribution methods are different. Retirement, cross-border coverage, severance agreements, stock options, company-car valuation and disputed remuneration need the specific legal/factual assessment named below. Do not quietly classify an unsupported benefit as tax-free.

## Rates, bands and thresholds

All amounts are PEN. Read dates and exact document portions appear in Sources. An AFP row is a November snapshot, not evidence for the other months of 2026.

| Item | Figure, period and conditions | Official source / short original wording |
|---|---|---|
| 2026 UIT | 5,500 for 2026 tax bands; a fine uses the UIT for its legally relevant infringement/detection date | [SUNAT UIT register](https://www.sunat.gob.pe/indicestasas/uit.html), `2026` / `5,500`; [Tax Code art. 180](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf) |
| Historical 2025 UIT | 5,350; use for 2025 calculations and where the relief rule expressly refers to the preceding year's UIT | [SUNAT UIT register](https://www.sunat.gob.pe/indicestasas/uit.html), `2025` / `5,350`; [RS 078-2021 art. 3.1](https://www.sunat.gob.pe/legislacion/superin/2021/078-2021.pdf) |
| Ordinary fixed deduction | 7 UIT = 38,500 in 2026, once against combined fourth/fifth-category work income; historical 2025 equivalent 37,450 | [LIR art. 46](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), `monto fijo equivalente a siete (7)` |
| Additional annual deduction | Up to 3 UIT = 16,500 for qualifying documented expenses; employer withholding never applies it, even if documents are supplied | [LIR art. 46](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf), `no podrán exceder en conjunto de tres (3)`; [Regulation art. 40(b)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) uses the fixed deduction |
| Resident work band 1 | Annual taxable base through 5 UIT = 27,500: 8%; cumulative tax at top 2,200 | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf), `Hasta 5 UIT` / `8%` |
| Resident work band 2 | Excess over 5 through 20 UIT, up to 110,000: 14%; cumulative tax at top 13,750 | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf), `Más de 5 UIT hasta 20 UIT` / `14%` |
| Resident work band 3 | Excess over 20 through 35 UIT, up to 192,500: 17%; cumulative tax at top 27,775 | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf), `Más de 20 UIT hasta 35 UIT` / `17%` |
| Resident work band 4 | Excess over 35 through 45 UIT, up to 247,500: 20%; cumulative tax at top 38,775 | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf), `Más de 35 UIT hasta 45 UIT` / `20%` |
| Resident work band 5 | Excess above 247,500: 30%; do not apply this rate to the whole taxable base | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf), `Más de 45 UIT` / `30%` |
| Non-domiciled employment | Domestic-law 30% on gross Peruvian-source employment income; no resident deductions; source, domicile and treaty facts first | [LIR art. 54(g)](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf), `Rentas de trabajo` / `Treinta por ciento (30%)` |
| Ordinary RMV, January-September 2026 | 1,130 monthly; do not use this floor for October onward | [DS 015-2026-TR art. 1](https://busquedas.elperuano.pe/dispositivo/EX/2559163-1), `de S/ 1,130.00` |
| Ordinary RMV, from 1 October 2026 | 1,230 monthly. Further tranche requires a 2027 decree, not automatic 2026 application | [DS 015-2026-TR art. 1.2](https://busquedas.elperuano.pe/dispositivo/EX/2559163-1), `a partir del 1 de octubre de 2026` |
| Ordinary hours / hour value | Maximum 8 daily or 48 weekly, subject to lawful schedules/exclusions; monthly ordinary remuneration / 30 / ordinary daily hours | [DS 007-2002-TR arts. 1-5, 12; DS 003-97-TR art. 8, official MTPE compendium pp. 43, 265-271](https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495), `entre siete, quince o treinta` |
| Overtime minimum surcharge | First two hours beyond ordinary daily working time at least 25%, subsequent hours at least 35%; hourly fractions proportional, lawful compensatory rest agreement distinct | [DS 007-2002-TR arts. 9-12, compendium pp. 269-271](https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495), `veinticinco por ciento (25%)` / `treinta y cinco por ciento (35%)` |
| Night-work floor | 22:00-06:00 statutory night period; qualifying night remuneration not below RMV plus 35%. This is not automatically 35% on every salary | [DS 007-2002-TR art. 8, compendium pp. 269-270](https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495), `inferior a la remuneración mínima mensual` |
| Ordinary ONP/SNP | Employee 13% of insurable monthly remuneration, no cap; full-schedule minimum and proportional-work conditions below | [ONP regulation arts. 19, 22-25](https://repocdn.onp.gob.pe/Normativa/Base_normativa/NPT046.pdf), `trece por ciento (13%) de la remuneración asegurable` |
| AFP mandatory savings | Employee 10% of contributory remuneration, uncapped by the insurance ceiling, subject to retirement exceptions | [SBS November 2026 schedule](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx), `APORTE OBLIGATORIO` / `10,00%` |
| AFP insurance, November 2026 | 1.37% on the lesser of contributory remuneration and RMA 12,732.70, where insured; other months require their actual schedule | [SBS devengue 2026-11, note 3](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx), `1,37%` / `12 732,70` |
| Habitat, November 2026 | Salary-flow commission 1.47%, OR annual fund-balance fee 1.25% according to arrangement; ordinary below-RMA flow total 12.84% | [SBS HABITAT row](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx), `1,47% 1,25%` |
| Integra, November 2026 | Salary-flow commission 1.55%, OR annual balance fee 0.78%; ordinary below-RMA flow total 12.92% | [SBS INTEGRA row](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx), `1,55% 0,78%` |
| Prima, November 2026 | Salary-flow commission 1.60%, OR annual balance fee 1.25%; ordinary below-RMA flow total 12.97% | [SBS PRIMA row](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx), `1,60% 1,25%` |
| Profuturo, November 2026 | Salary-flow commission 1.69%, OR annual balance fee 0.68%; ordinary below-RMA flow total 13.06% | [SBS PROFUTURO row](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx), `1,69% 0,68%` |
| Mixed/balance salary-flow leg | Zero since February 2023; ordinary insured below-RMA November salary deduction 11.37%, annual balance fee separate | [SBS closing note](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx), `el componente de flujo de la Comisión Mixta es 0%` |
| Ordinary EsSalud | Employer 9% of contributory remuneration, no upper cap, ordinary RMV floor subject to subsidy/whole-unpaid-month exceptions | [Law 26790 art. 6](https://www.essalud.gob.pe/transparencia/pdf/publicacion/ley26790.pdf), `equivale al 9%`; [SUNAT 003-2007](https://www.sunat.gob.pe/legislacion/oficios/2007/oficios/i0032007.htm) reads amended minimum |
| EPS health credit | Least of 25% of qualifying covered-worker EsSalud, eligible actual EPS payments for the month, and 10% UIT per covered worker; indexed 2026 cap 550 each | [Law 26790 arts. 15-16](https://www.essalud.gob.pe/transparencia/pdf/publicacion/ley26790.pdf), `sin exceder de los`; [SUNAT 088-2004](https://www.sunat.gob.pe/legislacion/oficios/2004/oficios/i0882004.htm) |
| Statutory gratificaciones | July/December ordinary benefits, one computable monthly remuneration for a complete qualifying semester; service/base conditions below | [Law 27735/DS 005-2002-TR, compendium pp. 329-335](https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495), `dos gratificaciones en el año` |
| Health-replacement bonus | 9% of statutory gratificación in ordinary EsSalud case, 6.75% for qualifying EPS cover; not ordinary social-contribution remuneration, but employment tax remains | [Law 30334/DS 012-2016-TR art. 6, compendium pp. 338-346](https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495), `no remunerativo ni pensionable` |
| CTS time formula | Computable base times qualifying months/12 plus days/360; semestral gratificación received enters base by one sixth | [CTS TUO arts. 18, 21](https://cdn.www.gob.pe/uploads/document/file/229267/TUO_Compensacion_por_Tiempo_de_Servicios_-_D.S_001-97-TR.pdf), `un sexto de lo percibido` / `treintavos` |
| Weekly rest / holiday work | Ordinary qualifying work without replacement rest: pay for work plus 100% surcharge, distinct from the ordinary paid rest/holiday entitlement; do not assume every Sunday is a rest day | [DL 713 arts. 1-4, 8-9, compendium pp. 285-287](https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495), `sin descanso sustitutorio` / `sobretasa de 100%` |
| Ordinary annual vacation | 30 calendar days after complete year and qualifying service record; four-hour ordinary-day gate and service tests below | [DL 713 arts. 10-16 / DS 012-92-TR art. 11, compendium pp. 287-295](https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495), `treinta días calendario` |

## The base

### 1. Build remuneration from documents, not net bank deposits

Start with the contract, time records, boleta de pago and current employment/social-security registration. Identify ordinary salary, regular allowances, commissions, overtime, taxable in-kind compensation, ordinary gratificaciones, extraordinary bonuses, paid/unpaid leave and subsidies. Gross cash, gross taxable employment income and contributory remuneration need not be identical. A salary advance reduces a later cash balance but does not prove lower taxable earnings. A refund is not automatically taxable employment income or an employer expense reversal.

Under LIR art. 34 and Regulation art. 40(f), include taxable in-kind remuneration at the appropriate market value; do not assume company cars, stock awards or reimbursements have zero value because no cash was paid. Obtain the applicable valuation and any specific exemption before calculating. LIR art. 18 separately excludes statutory labour indemnities, statutory CTS and qualifying social-security subsidies; a voluntary termination payment or a payment merely labelled indemnización does not establish that exemption. Keep legal basis and any statutory limit with the payment.

Use the actual ordinary schedule to calculate hour values under DS 003-97-TR art. 8 and DS 007-2002-TR art. 12: monthly ordinary remuneration / 30 / that worker's ordinary daily hours. Do not use `(monthly wage / 30 × 7) / 48`. Record approved overtime/time evidence and contractual rates if better than statutory minima. DS 007-2002-TR arts. 1-5 permits lawful compensating/atypical schedules and excludes specified managerial, unsupervised and intermittent work from the ordinary maximum; identify the correct population before counting an automatic ninth-hour surcharge.

For ordinary overtime, apply at least 25% extra for the first two excess daily hours and 35% for the remaining hours, prorating a fraction of an hour. Night remuneration has a minimum based on RMV plus 35%, not necessarily a 35% addition to every higher salary; the statute defines night as 22:00-06:00. Obtain actual night/ordinary hours and any better collective arrangement. For work on the actual weekly rest day or statutory holiday without replacement rest, apply DL 713 arts. 3/9's additional work remuneration and surcharge; distinguish a Sunday that is a normal scheduled day and the separately paid rest entitlement. The cited historic compendium holiday list is not offered as the complete 2026 holiday calendar; confirm the current calendar and replacement-rest facts.

### 2. Determine tax domicile and employment source

Establish domicile under LIR arts. 6-8 and source under arts. 9-10 before selecting the resident computation. Foreign nationality, an overseas payer or an offshore bank account does not settle either question. Do not apply a domiciled default to avoid asking for the necessary status facts, or treat the personal-income-tax residence rules as the test for pension coverage.

For a domiciled employee use the ordinary work-income projection below. For a non-domiciled employee, domestic law applies 30% to Peruvian-source employment income under LIR art. 54(g), without the 7 UIT or additional annual deduction. A treaty/source/split-year claim requires its actual facts and text. The after-tax cash amount is not final net pay until any applicable pension and other lawful deductions are determined.

### 3. Compute resident fifth-category withholding in the statutory order

Under Regulation art. 40(a)-(c):

1. Multiply the ordinary monthly remuneration made available in the current month by the remaining months of the year **including that month**.
2. Add the ordinary gratificaciones due for the year and remuneration/other relevant amounts made available in earlier months of the same year. Reconcile prior pay to avoid double counting. A full-year ordinary employee can have two full statutory gratificaciones; a part-year or special-regime employee must use actual entitlement. Omitting ordinary bonuses and flagging the omission is not an acceptable payroll method.
3. Subtract the fixed 7 UIT once and floor the taxable base at zero. Pension deductions are not another deduction from this tax base. The same fixed deduction is shared with fourth-category work income at annual level, not renewed for each payer.
4. Apply marginal LIR art. 53 bands. Let B be taxable base. Tax before credits is `8%×min(B,27500) + 14%×min(max(B-27500,0),82500) + 17%×min(max(B-110000,0),82500) + 20%×min(max(B-192500,0),55000) + 30%×max(B-247500,0)`. All thresholds use 2026 UIT.
5. Deduct the applicable documented credits/saldo under art. 40(c), then use the correct monthly allocation below. Do not subtract the additional annual 3 UIT expense deduction, even when receipts are provided. Qualifying donations for a fifth-category-only employee have the specific December adjustment under art. 40(b), not a general monthly expense deduction.
6. In a month with extraordinary pay, art. 40(e) adds the difference between annual tax including that extra payment and the ordinary projected annual tax to the ordinary monthly withholding. Include a statutory health-replacement extraordinary bonus under the applicable employment-tax rule; its social-contribution exemption is not an income-tax exemption.
7. For weekly/fortnightly payroll, art. 40(f) distributes the monthly withholding proportionately across payments. A different pay frequency does not create a new annual deduction or change the underlying monthly test.

| Payroll month | Ordinary withholding allocation and cumulative period | Official source |
|---|---|---|
| January-March | Projected annual tax / 12 | [Regulation art. 40(d)(1)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf), `dividirá entre doce` |
| April | Annual tax less withholding January-March, divided by 9 | [Regulation art. 40(d)(2)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf), `dividirá entre nueve` |
| May-July | Annual tax less withholding January-April, divided by 8 | [Regulation art. 40(d)(3)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf), `dividirá entre ocho` |
| August | Annual tax less withholding January-July, divided by 5 | [Regulation art. 40(d)(4)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf), `dividirá entre cinco` |
| September-November | Annual tax less withholding January-August, divided by 4 | [Regulation art. 40(d)(5)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf), `dividirá entre cuatro` |
| December | Final annual adjustment less withholding January-November | [Regulation art. 40(d)(6)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf), `ajuste final` |

Keep ordinary withholding, current extraordinary increment and actual prior retentions as separate fields. Preserve the rounding/reconciliation evidence from the payroll system; do not multiply a rounded January amount by twelve and call it the final annual liability.

### 4. Variable remuneration, changes of employer and cessation

Regulation art. 41(a) permits an alternative for variable monthly remuneration: use the average paid in the current and immediately preceding two months for the projection, excluding ordinary gratificaciones from that average/projection as that provision directs, and adding the ordinary/extraordinary gratificaciones and profit participation actually made available in the month. The option is exercised in the first withholding month of the year and maintained throughout it. For the specified variable-pay worker joining after 1 January, the employer withholds only after three complete months have elapsed from incorporation, as that paragraph directs. Do not switch between current pay and an averaging method each month simply to reduce withholding.

For a later starter under art. 41(b), use the remuneration of the joining month and remaining period, not a fictitious full twelve months with that employer. Under art. 41(c) carry forward earlier employers' income and retentions using the evidence SUNAT requires. For simultaneous fifth-category jobs, art. 44(b) makes the highest-paying employer aggregate the others' remuneration after the worker's declaration; the worker supplies received copies to the other employers so they do not duplicate withholding. A failure to supply the declaration does not remove each employer's withholding duties under art. 44(c).

At cessation, art. 41(d) requires a final adjustment using actual taxable remuneration/gratificaciones and other amounts made available in the year, including taxable termination payments, less the fixed deduction and applicable credits/withholding. Do not keep forecasting a salary after termination as if the employee stayed all year. If that adjustment shows excess withholding before year-end, art. 42(a) requires repayment to the worker in that month; the employer offsets against other workers' withholding, carries the uncompensated amount to following periods or requests SUNAT refund as the rule permits. Post-year-end excess for persons without a return obligation follows the separate SUNAT procedure. Keep the repayment and offset/refund trail; it is not a salary expense or an additional tax deduction.

### 5. Employee pension deductions and employer health

**ONP:** 13% of monthly insurable remuneration under ONP regulation arts. 19, 22-25, uncapped. For the ordinary full legal/contractual schedule the minimum is RMV; less than the full schedule/month requires the lawful proportional minimum and actual accrued remuneration. Do not import EsSalud's full floor into every lawful part-time ONP case. Confirm effective membership periods. Do not add an ordinary employer matching pension charge or stack ONP and AFP on the same remuneration.

**AFP:** use the actual month, administrator and arrangement. Calculate savings `10%×contributory remuneration`; insurance `premium×min(contributory remuneration, month RMA)` if insured; and a salary-flow commission only where that arrangement applies. The mixed arrangement's flow component is zero under SBS's note; its annual balance fee is charged to the relevant fund balance, not as another percentage of monthly salary. Only insurance has the RMA cap. The November table verifies an ordinary insured worker's flow totals of 12.84/12.92/12.97/13.06%, or mixed salary deduction 11.37%, below the cap. Do not multiply those combined totals by high earnings or apply November's snapshot to January/June.

SBS Title V art. 87(a) allows a qualifying retired affiliate continuing work to refrain from mandatory SPP contributions after communicating and documenting pensioner status. Art. 87(b) separately exempts the insurance premium at retirement age, with identification/documentary conditions; it does not automatically eliminate savings contributions. Qualifying retirement withdrawals have the specified documentary route. Request the actual pension status and date. Mere tax non-domicile, an old pension credit in a bank statement, or age alone does not establish every exemption.

**EsSalud:** ordinary employer 9% of contributory remuneration, no upper cap. For an ordinary remunerated month without subsidy use `9%×max(actual contributory remuneration, month-end RMV)`. Part-time/partial-month work alone does not remove the full ordinary health floor. SUNAT report 003-2007 distinguishes a full month with no remuneration under unpaid suspension, where no ordinary wage contribution arises, from a subsidised month. Do not charge on social-security subsidies; in a mixed subsidised/remunerated month use the statutory proportional non-subsidised-days minimum and actual contributory pay. Do not force the full ordinary floor onto a whole subsidised/unpaid month.

**EPS:** confirm qualifying employer scheme, covered-worker selection, cover month, workers and actual eligible payment. Credit is the least of (a) 25% of the qualifying covered-worker EsSalud charge, (b) eligible actual EPS sums attributable to the source month and (c) 10% of that month's UIT times covered workers. A 6.75% residual health charge is only the result when the full 25% credit is available against a 9% wage charge; it is not a universal rate. SUNAT report 088-2004 defers late EPS credit to the payment period and succeeding periods, using each source month's own caps; it does not extinguish a correctly earned credit solely because EsSalud filing/payment is late. Keep current/prior credit and utilisation separate. The EPS cash payment can exceed the credit.

Use the detailed social-contribution method in the Peru pack for those bases and benefit interfaces, but do not rely on an older approved version that contradicts these current statutory rules. Special/high-risk insurance, contractual gross-ups and employer-sponsored contributions require separate cost rows.

### 6. Benefits, leave and termination payments

Ordinary **gratificaciones** follow Law 27735/DS 005-2002-TR: January-June and July-December qualifying semesters, reference remuneration at 30 June/30 November, complete qualifying semester one computable monthly remuneration. For complementary variable pay, receipt in at least three months of the semester meets regularity and sum/six enters the base; principal variable remuneration uses the specified CTS art. 17 average. Shorter service uses complete-calendar-month sixths with non-credited-day thirtieths of that monthly fraction. Paid vacation/leave and qualifying subsidised time have their statutory credited treatment. Truncated gratificación uses the immediately preceding month's computable pay, requires at least one complete qualifying month, and is due within 48 hours of cessation. Add the ordinary 9% or qualifying EPS 6.75% health-replacement bonus; statutory contribution exemptions do not remove employment income tax.

Ordinary **CTS** has its four-hour-average daily gate, computable regular remuneration, April/October reference bases, qualifying variable-pay average and one sixth of semestral gratificación actually received. CTS TUO arts. 16-18 distinguishes complementary variable pay (at least three months in six, sum/six, also for a shorter liquidation), principal imprecise pay (semester average or actual-period daily average if shorter), and periodic pay. Under art. 21 use base×months/12 + base×remaining days/360. Do not substitute an approximate annual employer-cost percentage. At cessation art. 3 uses cessation-date remuneration and direct payment within 48 hours, unlike the previous-month base of truncated gratificación. Obtain family-allowance/variable-pay and service records rather than using basic salary alone.

Ordinary **vacation** under DL 713 arts. 10-16 and DS 012-92-TR arts. 11-12 requires the applicable four-hour ordinary-day gate and service record: ordinarily 260 effective days for a six-day week, 210 for a five-day week. For a three/four-day plan or authorised temporary interruption, unjustified absences must not exceed ten in the period; absences not credited to the statutory record count as unjustified for this test. Credit common illness/work-accident/occupational-disease absence only within the first 60 days per service year. Count maternity, authorised absence and other credited categories separately under art. 12, not every absence as unpaid. Ordinary entitlement is 30 calendar days, remunerated as if the worker continued work and paid before leave starts. The current statutory conditions, consent and written agreement matter for advance, split, accumulation or reduction; do not replace actual leave with a generic extra monthly salary.

On termination, DL 713 art. 22 and regulatory art. 23 require at least a month for the truncated record and twelfths/thirtieths of the monthly fraction for completed months/days. Accrued complete entitlement not taken is separate. Where leave is not enjoyed within the year following the year in which the right was acquired, DL 713 art. 23 distinguishes remuneration for actual work, earned vacation pay and an additional indemnity equal to one remuneration. Only that indemnity is free of the article's tax/contribution charge. Regulatory art. 24 excludes managers/representatives who themselves decided not to take leave from that indemnity. Do not treat every manager as excluded regardless of who controlled the leave decision.

A statutory severance indemnity, CTS, vacation pay, late-vacation indemnity and voluntary settlement have different legal/tax classifications. Obtain the reason for termination, contract and statutory entitlement before quantifying a dismissal payment or exempting it under LIR art. 18(a)/(c). This method does not supply a universal severance rate or stock-option/company-car valuation.

### 7. Net pay, employer cost and bookkeeping reconciliation

`Employee cash net = cash remuneration and benefits payable - applicable employee pension - fifth-category withholding - other lawful deductions - advances already paid`, with non-cash remuneration traced separately. Do not label a tax-only subtotal final net where pension eligibility is unresolved. Employer EsSalud is an additional employer liability, not another employee withholding.

The ordinary wage-plus-health subtotal `salary + gross EsSalud - allowable EPS credit` excludes any separate EPS cash payment, additional insurance and benefit costs not already included. Add CTS, ordinary bonuses, the health-replacement bonus, leave provisions and any contractual employer obligations on their proper basis. Avoid double counting salary already covering ordinary paid leave when preparing an annual budget. A pension/tax withholding remains a liability until remitted; paying it later is not a second wage expense.

Reconcile each concept: opening liability + charge/withholding - valid credits - paid remittances = closing balance. Net salary payments tie to payroll cash control; PLAME debt and payments tie by tax code/period; AFP declarations/payments tie separately by employee and component. A filed return, a payment reference and an actual paid receipt are different evidence.

### 8. Bank reading, working paper and handoffs

The following are illustrative narration search strings, not verified proprietary bank dictionaries or deterministic legal classifications. Read the direction, account holder, counterparty, period and receipts. A bank statement alone cannot establish gross salary, tax domicile, pension affiliation or exact contribution split.

| Candidate string / direction | Provisional classification | Evidence and exception |
|---|---|---|
| Incoming `SUELDO`, `REMUNERACION`, `PLANILLA`, `PAGO PLANILLA`, `NOMINA`, `PAYROLL`, `SALARY`, `HABERES` | Possible employment cash received | Reconcile boleta and employer; not automatically gross remuneration |
| `ADELANTO`, `ADELANTO DE SUELDO` | Possible wage advance | Reconcile later settlement; not an additional full wage or proof of lower tax base |
| `GRATIFICACION`, `GRATI` | Possible bonus | Confirm statutory entitlement, extraordinary bonus and tax treatment |
| `CTS`, `DEPOSITO CTS` | Possible benefit deposit | Confirm employee CTS account, semester and actual computation |
| `DEVOLUCION RENTA`, `REINTEGRO SUNAT` | Possible tax refund | Verify refund decision and tax account; not automatically employment income |
| Outgoing `SUNAT`, `PLAME`, `FORM 601`, `RENTA QUINTA`, `RETENCION RENTA` | Possible payroll-tax remittance | Generic SUNAT may be any tax; obtain form, period and concept-level receipt |
| `ESSALUD`, `APORTE ESSALUD` | Possible employer health payment | Reconcile base, gross charge and current/prior EPS credits |
| `ONP`, `SNP`, `APORTE ONP` | Possible employee pension remittance | Confirm membership and accepted/paid return, not an employer pension match |
| `AFP`, `INTEGRA`, `PRIMA AFP`, `PROFUTURO`, `HABITAT`, `AFPNET` | Possible private pension remittance | Confirm components/period and paid status, separate from SUNAT |
| Outgoing `PAGO PLANILLA`, `NOMINA`, `PAYROLL RUN`, `PAGO HABERES` | Possible net wages disbursed | Reconcile employee bank list to payroll cash control |

The old working-paper columns remain useful but must implement the actual method. Use one employee-period row, not a single annual row that hides the changing allocation:

| Field group | Inputs / computation / control |
|---|---|
| Identity A-D | Employee; RUC/DNI; tax domicile/source; actual pension affiliation, AFP, arrangement and effective dates |
| Remuneration E-G | Current pay by component; period-specific UIT/RMV; earlier actual pay; remaining months; ordinary bonuses; additional current payments; projection method elected |
| Deductions H-J | Fixed 7 UIT once; annual 3 UIT tracked outside employer withholding; non-negative projected taxable base; taxable benefits and statutory exclusions recorded separately |
| Tax K-L | All five marginal bands; credits; statutory divisor/prior-retention cutoff; extraordinary increment; actual current withholding and rounding reconciliation |
| Pension M-Q | ONP base/minimum/13%, OR AFP savings/insured capped premium/applicable flow; annual balance fee not another salary deduction; retirement documents |
| Net R | Cash pay less employee pension, tax, other lawful deductions and advances; unresolved pension means no final net |
| Health S | Actual health base; full/proportional minimum or exemption; gross 9%; current/prior EPS caps/utilisation and net health |
| Cost T | Wage-plus-health subtotal clearly labelled; separate EPS cash, insurance and benefit provisions; no assumed complete 9% wedge |
| Filing/evidence controls | T-Registro receipts; PLAME field-by-field reconciliation/accepted return; AFP declaration/paid receipt; actual due dates/extensions; bank references/receipts; closing liability |
| Benefits/cessation | Qualifying service/base; CTS/grati/vacation records; final tax adjustment; refunded overwithholding/offset trail; review items |

For a non-domiciled employee, change the income-tax computation, not the entire pension columns M-Q. Footer controls sum fifth-category tax, EsSalud and ONP to their PLAME debt/payment concepts; AFP sums to the separate remittance and payroll cash sums to wage transfers. Trace every difference rather than forcing an amount to the bank total.

Spanish reading glossary: remuneración/sueldo = gross wage; sueldo neto = net cash; renta de quinta = employment income; renta neta imponible = taxable income; retención de quinta = employment tax withheld; UIT = indexing unit; EsSalud = health; ONP/SNP = public pension; AFP = private pension; prima = insurance; comisión sobre flujo = salary-based fee, distinct from balance arrangement; RMA = insurance ceiling; RMV = minimum wage; gratificación = statutory bonus when its conditions apply; CTS = service-time benefit; PLAME = monthly declaration; T-Registro = employment/social-security registry; SUNAT = tax administration; SBS = pension supervisor; RUC = taxpayer identifier; Sol/S/ = PEN currency.

Handoffs: `peru-igv` handles IGV, not payroll remittances as input invoices; `peru-income-tax` handles annual work/other-income reconciliation; the actual social-contribution slug is `peru-social-contributions`, not the old broken `peru-social-security` reference; `cross-border-payroll-coordination` is a workflow handoff requiring the actual agreement/certificate. A sibling's old tax year or inconsistent figure is not supporting evidence for a 2026 payroll. Payroll-to-bookkeeping records gross costs and withholding liabilities separately. Payroll-to-tax supplies year-to-date income, contributions, withholding/refund and annual-deduction records.

## Deadlines and filing

### Register and maintain the worker

The ordinary electronic-payroll obligation starts with one or more employees, not an income/salary threshold; SUNAT also lists other specified populations. Obtain employer RUC/SOL access. In **Empresas > Mi RUC y Otros Registros > T-Registro**, complete employer **Alta**, then worker **Registro Individual > Nuevo**, entering identity, employment, social-security and tax facts with consistent dates. Save worker CIR receipts **1604-1** for alta, **1604-2** for modifications and **1604-3** for baja, as in SUNAT's official presentation.

SUNAT's obligations table requires worker registration **within the day services begin**, not a rolling 24 hours. Update changes within five business days of the relevant event/knowledge under that rule and deregister by the day after termination. Deliver the alta receipt by the next business day, modification receipt within fifteen calendar days, and requested baja receipt within two calendar days of the request. A pensioner's first-payment registration rule is different. Preserve communications and evidence of delivery; a bank wage payment does not prove registration.

### Complete PLAME and the separate AFP payment

1. Use the period-appropriate PDT: **4.6** was introduced for January 2026 by RS 016-2026; **4.7** applies from the October 2026 period under RS 213-2026 art. 2, available **30 October**, with specified earlier original/rectifying-period use. Read the operative resolution instead of an old landing page/version number.
2. Validate the employer/SOL data and synchronise **T-Registro** in the employer/PDT module. In **Declaraciones Juradas**, select the service period and synchronise the workers. Use SUNAT's personalised T-Registro file route where online sync fails; fix inconsistent registration first.
3. In **Detalle de Declaración > Trabajadores**, complete **Jornada Laboral**, actual days/subsidies/hours, **Ingresos**, remuneration accrued/paid, deductions and **Tributos y Aportes**. Map taxable employment pay and each contribution base separately. Do not force taxable pay to equal contributory pay.
4. Review **Determinación de la Deuda**, including resulting charges, current/prior EPS credits, prior payments, applicable interest, balance and amount actually paid. SUNAT's public unpopulated PLAME Web receipt identifies ordinary EsSalud base/result **452/412**, ONP **451/411**, fifth-category **455/415**, EPS credits **602/612** and respective balances **712/711/715**. These are the read public receipt fields, not a claim that every historical PDT/special-regime screen is identical.
5. **Validar**, correct errors, **Guardar**, then **Declaraciones Registradas > Archivo de Envío**. In SOL's declarations/payment platform use **Presentación PDT / Receptor de Archivos PDT > Examinar**, upload and follow the submission checks. Save accepted **constancia de presentación**, form, period and order number. A locally generated file is not a filed declaration.
6. Pay by an enabled debit/card route or NPS where offered, saving the actual payment confirmation and bank receipt. SUNAT's NPS notice says `no es una constancia de pago`; a reference does not settle the liability or extend the legal due date. Reconcile actual payments and unpaid amounts per concept.
7. Separately declare/remit AFP contributions through the applicable AFP/AFPnet collection route. SBS requires employer contributions within the **first five business days of the next month**. Do not substitute the SUNAT RUC timetable or treat AFP as ONP in the SUNAT payment. Keep worker/component details and paid status.

**PLAME Web:** optional Form 601 for the private-sector employer meeting SUNAT's up-to-ten-workers and/or up-to-ten-service-providers conditions and exclusively the specified concepts: employee EsSalud, ONP, fourth/fifth-category withholding, fourth-category recipient information and eligible +Vida premiums. Check all conditions for that period. In **Mis declaraciones y pagos**, choose form/period, download T-Registro, complete and submit. A Web original may be corrected through Web or PDT; re-enter all concepts, including unchanged data. Specified identity/date-of-birth corrections use Form **1601**. If Web is unavailable or the concept/population test is not met, use the PDT.

**Monthly due date:** obtain the annual SUNAT calendar for the actual RUC ending, taxpayer status and period, including emergency extensions. The official Emprender calendar read gives January 2026 obligations for RUC ending 0 on **16 February 2026**; this example is not the date for other RUCs/months. A generic mid-month range, assumed first-business-day window or automatic rollover is not a substitute for the published date. Save the applicable calendar with the payment authorisation.

### Annual process and benefits

LIR art. 79 generally excludes persons with exclusively fifth-category income from an annual return, subject to the specific exceptions/SUNAT designation. Two employers alone do not impose a return obligation; aggregate withholding under art. 44 first. Annual expenses, other income, balances/refunds and special annual filing cases require the applicable resolution. SUNAT's [published 2025-income campaign instructions](https://renta.sunat.gob.pe/personas/como-realizar-la-declaracion-del-impuesto-la-renta) use Form 709 through SOL or App Personas; this is historical procedure, not a released 2026-income form. The released form, fields, population and 2027 timetable for **2026 income** must be confirmed, not copied from the 2025 campaign. Supply the taxpayer's records; do not promise all annual expense claims require the same filing route.

Ordinary CTS is deposited within the first fifteen calendar days of May/November under CTS TUO art. 22; a non-working final day moves to the next business day. In 2026 the ordinary dates are **15 May and 16 November**, the latter because 15 November is Sunday, subject to an applicable holiday/extension. Ordinary gratificaciones are paid in the first fortnight of July/December; do not apply the CTS rollover to a different benefit without legal authority. Truncated CTS and gratificación have the separate **48-hour** cessation rules and different bases described above. Ordinary vacation remuneration is due before leave begins. Keep actual credited service and payment/deposit evidence with every benefit.

## Penalties and interest

### Choose the correct infringement and population

Failure to file on time under Tax Code art. 176(1), incorrect bases/credits under art. 178, and failure to remit tax already withheld under art. 178(4) are different failures. Filing an omitted PLAME does not itself pay tax, pension, interest or a fine. Determine infringement date, return population, taxpayer table and any applicable current discretionary non-sanction decision before calculating. The rate tables below do not establish the outcome for an individual notice or a period with different UIT.

### First test the statutory preventive-training gate

[Tax Code arts. 165/180, amended by Law 32335](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf), require a preventive-training process for qualifying microenterprises before the corresponding fine/closure sanction. It is a separate gate from discretionary non-sanction and Annex II graduality, not automatic art. 13-B payroll relief.

1. Test a natural/legal person generating third-category income, any tax regime, annual sales up to 150 UIT and the first qualifying infringement punishable by fine or closure. Under [DS 288-2025-EF arts. 3-6](https://www.mef.gob.pe/es/por-instrumento/decreto-supremo/34781-decreto-supremo-n-288-2025-ef/file), each independently numbered conduct in arts. 173-178 is a type; do not combine all art. 172 categories or all filing failures. Check the proprietor/partner exclusion for a current final tax/customs criminal conviction. REMYPE labour registration is not the eligibility test.
2. Apply DS 288 art. 7 and first transitional provision(2): for 2026 onward, ordinarily sum prior-year declared income, including effective amendments presented by commission/detection date, using that year's UIT. General/RMT and RER use their specified net-income declarations; Nuevo RUS uses gross income. Where there was no prior-year activity, apply the prescribed current-year expired-period test. More than one omitted required monthly declaration in the relevant year prevents the computation/course unless a filing exemption applies. Do not substitute art. 13-B's 621-field test or automatically use 2026 UIT for 2025 declarations.
3. Establish first-type status from actual SUNAT history under DS 288 art. 5's alternatives: fine/closure notification, discretionary non-sanction, 100% reduction or Table III note-3 payment, recognition act and course communication. Do not reduce it to a generic 'first ever error'. Where qualifying same-type breaches already exist, the earliest is first. A natural person's own first/second/fourth/fifth-category income breaches are excluded from this count; employer withholding is not thereby that proprietor's own fifth-category income.
4. RUC deregistration/reactivation does not erase prior history. Under art. 11, simultaneous same-type first breaches receive the course for only one; where fine amounts differ, use the most onerous for the course and leave the others subject to sanction. The second transitional provision also preserves qualifying pre-17-May-2025 breaches without an applied sanction; the January 2026 operating resolution does not exclude them automatically.
5. Under [RS 010-2026 arts. 5-8](https://www.sunat.gob.pe/legislacion/superin/2026/000010-2026.pdf), SUNAT notifies the SOL buzón communication with platform URL, credentials and its nonextendable five-business-day access window. The taxpayer or entity's legal representative completes the course and final activity, obtains and saves the constancia within that window. Participation acknowledges the infringement; nonattendance or incomplete steps permits the applicable sanction. There is no independent self-elected course/payment deadline to invent.
6. Check the gate before recommending payment: DS 288 art. 10(f) prevents refund/compensation of relevant amounts paid before course completion. Training does not settle tax, pension or interest. Preserve the eligibility/history/notice/certificate evidence before treating a fine in the following table as payable.

| Statutory base or relief | Figure and required conditions | Official source / original wording |
|---|---|---|
| Late debt-determination return, Table I | Base fine 1 UIT; 5,500 if infringement's relevant UIT is 2026. Applies to the Table I population including General/RMT, before relief | [Table I, art. 176(1)](https://www.sunat.gob.pe/legislacion/codigo/tablaI.pdf), `Numeral 1 1 UIT` |
| Same infringement, Table II | Base fine 50% UIT; 2,750 on relevant 2026 UIT, including RER population where applicable | [Table II, art. 176(1)](https://www.sunat.gob.pe/legislacion/codigo/tablaII.pdf), `50% de la UIT` |
| Nuevo RUS, Table III | 0.6% of statutory **I** or closure, with table notes/minimum and payment timing; not 0.6% of actual monthly net income | [Table III, art. 176(1), notes](https://www.sunat.gob.pe/legislacion/codigo/tablaIII.pdf), `0.6% de los I o cierre`; [RS 063-2007 art. 1(f)](https://www.sunat.gob.pe/legislacion/superin/2007/063.htm) |
| Ordinary Annex II item 12, voluntary cure | 80% reduction without fine payment, 90% with payment; cure before the effective SUNAT infringement notice, for the applicable omitted-return case | [RS 063-2007 Annex II, item 12, original official XLS](https://www.sunat.gob.pe/legislacion/superin/2007/063_anexo_ii.xls), `SUBSANACION VOLUNTARIA`, `Sin Pago`, `Con Pago`; [RS 078-2021 art. 3.3](https://www.sunat.gob.pe/legislacion/superin/2021/078-2021.pdf) clarifies scope |
| Same Annex II item, induced cure | 50% without payment, 60% with payment; cure within the period SUNAT grants, starting when the specified notice takes effect | [Official Annex II item 12](https://www.sunat.gob.pe/legislacion/superin/2007/063_anexo_ii.xls), `dentro del plazo otorgado por la SUNAT` |
| Wrong RUC/period deemed unfiled case | Distinct item-12 correction route and 100% cure criterion; not a universal waiver for an actually omitted payroll return | [Annex II item 12/notes 3, 8](https://www.sunat.gob.pe/legislacion/superin/2007/063_anexo_ii.xls), `Solicitud de Modificación y/o Inclusión de Datos` |
| T-Registro nonregistration | Muy grave under RLGIT art. 25.20; ordinary No MYPE scale 2.63 to 52.53 UIT depending on affected count, not the grave 1.57-26.12 scale | [Official RLGIT arts. 25.20, 48.1](https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=47), `No registrar trabajadores` / `Muy grave`; actual employer/table conditions below |

For Nuevo RUS, I means four times the applicable category's maximum monthly **gross-income** limit, not the employer's monthly net profit. Table III's ordinary 5% UIT minimum is itself reduced when graduality produces a smaller fine under RS 063's second complementary final provision. Keep the separate Table III note-3 requirement to pay before notification of the closure resolution; do not substitute the notification's later effective date or promise fine-only treatment after a closure notice. For Tables I/II, reduced fines can fall below 5% UIT if paid before the fine-resolution notification takes effect; after that effective point the reduced fine cannot fall below 5% UIT unless a specific exception applies. Do not apply an art. 13-B enhanced-rate exception to PLAME contrary to the payroll exclusion below.

**Important payroll exclusion:** RS 078-2021 art. 3.4 inserted art. 13-B(2), which excludes annual/monthly declarations for income other than the taxpayer's **own third-category business income**. The more generous art. 13-B small-business bands are not an automatic PLAME relief scheme. RS 007-2025 changes its eligible <=19 and >19-to-150 UIT bands, but does not erase that exclusion. Thus the former skill's 100%, 98/99%, 96/97% and 90/95% own-business relief claims cannot be applied to payroll merely because the employer is small; nor does a seventh-business-day-after-enforcement window replace the ordinary Annex II notice-granted cure period.

For a **separate qualifying own-business return**, art. 13-B retains the prior-year UIT definition under RS 078-2021 art. 3.1 and the amended RS 007-2025 prior-year income tests. Exactly 19 UIT is in the lower band and exactly 150 UIT in the next band, not excluded by a strict-less-than sign. That comparison belongs in the business-return working paper, not the employee's payroll deduction. No individual payroll fine is reduced here by those rates. Ask for the actual notice and infringement before choosing either regime.

Under RLGIT art. 25.20, nonregistration is muy grave rather than the old skill's grave classification. In the cited No MYPE art. 48.1 table, 1-10 affected persons uses 2.63 UIT and 1,000 or more 52.53 UIT; multiplication by 2026 UIT gives 14,465 and 288,915 before case-specific rules. Other bands and micro/small-enterprise tables differ. Art. 48.1-A requires REMYPE evidence and governs the already-reduced small-business tables and applicable revenue cap/proof; do not halve an already reduced table again or apply No MYPE figures to everyone. The affected-person population in art. 25.20 includes the stated pensioners, providers, trainees, third parties and dependants, not just the payroll employee count by assumption. The obsolete 123,750 maximum is not a current universal cap.

Tax interest follows art. 33, with potential other liabilities for unremitted employee amounts; AFP collection has its own rules. This skill supplies no present TIM/AFP interest percentage or blanket discretionary exemption. Obtain the actual period rate and current operative relief decision before quantifying. Likewise, do not state one universal document-retention number: tax, labour, pension, benefit and any live dispute/prescription duties must be checked for the record concerned.

## Cross-border points

Determine work location/source, employer, payroll payer and domicile separately. Non-domiciled 30% employment tax does not automatically disapply EsSalud or pension. For a posted worker obtain the actual foreign social-security agreement, certificate, validity period and conditions before exempting a local contribution. Do not treat an income-tax treaty as a social-security exemption or the name of a cross-border workflow as legal evidence.

Home-country payroll, tax equalisation, split-year facts, PE/employer questions, foreign credits and treaty relief need the relevant country documents and specialist computation. Keep all Peruvian gross-to-net records and foreign adjustments rather than netting the two systems without a reconciliation. No foreign-covered-worker exemption, treaty percentage or gross-up factor is invented here.

## Two worked examples that recompute

All examples use stated hypothetical records. Tax and contribution periods are explicit. The old six example families and twelve tests are preserved with corrected legal inputs, rather than the old twelve-salary shortcut. AFP examples use the read November schedule; ONP January cases do not assume an unverified January AFP rate.

### Case 1: January low and middle earners, confirmed ONP

Ordinary full-year general-regime employees, fixed monthly salaries 3,000 and 8,000, two full ordinary gratificaciones due, no prior/current extraordinary pay or applicable credits, no other employers, ONP affiliation confirmed. January projections are 42,000 and 112,000, not 36,000 and 96,000. Projected taxes are 280 and 8,640; January withholding is 23.33 and 720 after stated cent rounding. January net is 2,586.67 and 6,240. EsSalud remains employer cost.

```oa-check
name: January ordinary salary and two-gratification projection, ONP
inputs:
  salary_low: 3000
  salary_mid: 8000
  uit: 5500
steps:
  fixed: uit * 7
  gross_low: salary_low * 14
  base_low: max(gross_low - fixed, 0)
  tax_low: base_low * 0.08
  withholding_low: round(tax_low / 12, 2)
  pension_low: salary_low * 0.13
  net_low: salary_low - pension_low - withholding_low
  health_low: salary_low * 0.09
  gross_mid: salary_mid * 14
  base_mid: gross_mid - fixed
  tax_mid: min(base_mid, 27500) * 0.08 + max(base_mid - 27500, 0) * 0.14
  withholding_mid: tax_mid / 12
  pension_mid: salary_mid * 0.13
  net_mid: salary_mid - pension_mid - withholding_mid
  health_mid: salary_mid * 0.09
expected:
  fixed: 38500.00
  gross_low: 42000.00
  base_low: 3500.00
  tax_low: 280.00
  withholding_low: 23.33
  pension_low: 390.00
  net_low: 2586.67
  health_low: 270.00
  gross_mid: 112000.00
  base_mid: 73500.00
  tax_mid: 8640.00
  withholding_mid: 720.00
  pension_mid: 1040.00
  net_mid: 6240.00
  health_mid: 720.00
```

The 14 multiplier is justified by these employees' stated full ordinary entitlement, not a universal rule for every new starter. Later actual extraordinary bonuses and rounding require the period adjustment.

### Case 2: November middle earner, Integra flow versus balance

Salary 8,000, ordinary annual salaries/gratificaciones total 112,000. The record includes the July ordinary health-replacement bonus 720 as a prior taxable receipt. The resulting November projection is 112,720, taxable base 74,220, annual projected tax 8,740.80; actual January-August withholding is 5,860.80. September-November allocation therefore gives 720. The worker's November Integra flow deduction is 1,033.60 and net 6,246.40. For an otherwise identical eligible mixed/balance member, salary pension is 909.60 and net 6,370.40; do not charge the annual fund fee on salary.

```oa-check
name: November Integra arrangements and actual cumulative withholding
inputs:
  salary: 8000
  ordinary_annual: 112000
  july_extraordinary_bonus: 720
  withheld_january_august: 5860.80
  rma: 12732.70
steps:
  projected: ordinary_annual + july_extraordinary_bonus
  base: projected - 38500
  annual_tax: 27500 * 0.08 + (base - 27500) * 0.14
  withholding: (annual_tax - withheld_january_august) / 4
  saving: salary * 0.10
  insurance: min(salary, rma) * 0.0137
  flow: salary * 0.0155
  flow_pension: saving + insurance + flow
  flow_net: salary - flow_pension - withholding
  mixed_pension: saving + insurance
  mixed_net: salary - mixed_pension - withholding
expected:
  projected: 112720.00
  base: 74220.00
  annual_tax: 8740.80
  withholding: 720.00
  saving: 800.00
  insurance: 109.60
  flow: 124.00
  flow_pension: 1033.60
  flow_net: 6246.40
  mixed_pension: 909.60
  mixed_net: 6370.40
```

The prior-withholding input must come from actual records in a real case; a missing record cannot be replaced with this example's amount. November insurance/commissions are not silently backdated to January.

### Case 3: November high earner, Profuturo flow and insurance cap

Salary 20,000, full ordinary annual remuneration 280,000 and July health-replacement bonus 1,800 already received; prior January-August withholding 25,410. November projected base 243,300 gives annual tax 37,935; current ordinary withholding is 3,131.25. Only insurance is capped at RMA 12,732.70: premium 174.44, savings 2,000 and flow commission 338, total 2,512.44. Net is 14,356.31, not the old 15,024.81 based on omitted gratificaciones and an unsupported quarter's RMA.

```oa-check
name: November Profuturo high earner with prior taxable bonus
inputs:
  salary: 20000
  ordinary_annual: 280000
  prior_bonus: 1800
  withheld_january_august: 25410
  rma: 12732.70
steps:
  projected: ordinary_annual + prior_bonus
  base: projected - 38500
  annual_tax: 27775 + (base - 192500) * 0.20
  withholding: (annual_tax - withheld_january_august) / 4
  saving: salary * 0.10
  insurance: round(min(salary, rma) * 0.0137, 2)
  flow: salary * 0.0169
  pension: saving + insurance + flow
  net: salary - pension - withholding
  health: salary * 0.09
expected:
  projected: 281800.00
  base: 243300.00
  annual_tax: 37935.00
  withholding: 3131.25
  saving: 2000.00
  insurance: 174.44
  flow: 338.00
  pension: 2512.44
  net: 14356.31
  health: 1800.00
```

### Case 4: non-domiciled tax is not a pension exemption

Confirmed Peruvian-source employment income 15,000, non-domiciled domestic-law rate and no applicable treaty change. Employment tax is 4,500 and the after-tax subtotal 10,500. Pension affiliation/coverage unknown means **no final net**. If the separate documented facts establish ordinary ONP on that full contributory remuneration, pension would be 1,950 and cash net 8,550 before any other valid deductions. This alternative is not an assumed non-resident affiliation.

```oa-check
name: Non-domiciled employment tax and separate confirmed-pension alternative
inputs:
  gross: 15000
steps:
  employment_tax: gross * 0.30
  after_tax_before_pension: gross - employment_tax
  onp_if_separately_confirmed: gross * 0.13
  net_if_onp_confirmed: after_tax_before_pension - onp_if_separately_confirmed
expected:
  employment_tax: 4500.00
  after_tax_before_pension: 10500.00
  onp_if_separately_confirmed: 1950.00
  net_if_onp_confirmed: 8550.00
```

### Case 5: employer subtotal, EPS cap and month-sensitive minimum

A normal 8,000 wage with no EPS/subsidy gives gross health 720 and wage-plus-health subtotal 8,720. That is not the complete employer budget. For one eligible EPS-covered worker with eligible paid invoice 100, the credit is 100 (less than the 180 health cap and 550 indexed cap), net EsSalud 620 and wage/net-health subtotal 8,620; separate EPS cash restores total wage/health/EPS cash to 8,720 in this particular payment-limited scenario. Actual benefit/insurance costs remain separate. A lawful part-time remunerated worker earning 900 without subsidy has ordinary health minimum 101.70 through September and 110.70 from October.

```oa-check
name: Employer wage-health subtotal, EPS and October floor
inputs:
  salary: 8000
  eligible_eps: 100
  covered_workers: 1
  uit: 5500
  part_time_pay: 900
steps:
  health: salary * 0.09
  gross_subtotal: salary + health
  eps_credit: min(health * 0.25, eligible_eps, uit * 0.10 * covered_workers)
  net_health: health - eps_credit
  net_health_subtotal: salary + net_health
  wage_health_eps_cash: net_health_subtotal + eligible_eps
  minimum_before_october: max(part_time_pay, 1130) * 0.09
  minimum_from_october: max(part_time_pay, 1230) * 0.09
expected:
  health: 720.00
  gross_subtotal: 8720.00
  eps_credit: 100.00
  net_health: 620.00
  net_health_subtotal: 8620.00
  wage_health_eps_cash: 8720.00
  minimum_before_october: 101.70
  minimum_from_october: 110.70
```

### Case 6: marginal-band checks, extraordinary pay and cessation refund

Band totals are computed marginally, not by a single top rate. A separate annual total of 36,000 taxable employment receipts before the fixed deduction gives zero tax; it is **not** the projection of an ordinary 3,000-monthly employee also entitled to bonuses. For a January 8,000 ordinary-salary employee with two 8,000 ordinary gratificaciones, an extraordinary current payment 2,000 raises annual tax by 280; add that to ordinary January withholding 720, giving 1,000. Separately, a departing worker's actual taxable receipts for the year are 30,000 with prior withholding 600 and no other credits: final tax is zero and excess 600 is repayable under the cessation rule.

```oa-check
name: Bands, current extraordinary increment and cessation excess
inputs:
  uit: 5500
  ordinary_base: 73500
  extra_payment: 2000
  actual_cessation_receipts: 30000
  prior_withholding: 600
steps:
  cumulative_one: 27500 * 0.08
  cumulative_two: cumulative_one + 82500 * 0.14
  cumulative_three: cumulative_two + 82500 * 0.17
  cumulative_four: cumulative_three + 55000 * 0.20
  annual_36000_tax: max(36000 - uit * 7, 0) * 0.08
  ordinary_tax: cumulative_one + (ordinary_base - 27500) * 0.14
  tax_with_extra: cumulative_one + (ordinary_base + extra_payment - 27500) * 0.14
  increment: tax_with_extra - ordinary_tax
  january_withholding: ordinary_tax / 12 + increment
  cessation_base: max(actual_cessation_receipts - uit * 7, 0)
  cessation_tax: cessation_base * 0.08
  excess_to_refund: max(prior_withholding - cessation_tax, 0)
expected:
  cumulative_one: 2200.00
  cumulative_two: 13750.00
  cumulative_three: 27775.00
  cumulative_four: 38775.00
  annual_36000_tax: 0.00
  ordinary_tax: 8640.00
  tax_with_extra: 8920.00
  increment: 280.00
  january_withholding: 1000.00
  cessation_base: 0.00
  cessation_tax: 0.00
  excess_to_refund: 600.00
```

### Case 7: hour value, ordinary overtime and a conditional filing fine

For an eight-hour ordinary day the monthly RMV hour value is 4.708333... before October and 5.125 from October, not 5.17. A distinct worker on monthly ordinary salary 3,000 has hour value 12.50; three evidenced excess daily hours at statutory minima give additional overtime 48.13 after final rounding. October's full night-work floor is 1,660.50. For a separate Table I employer outside the preventive-training population, assume an omitted payroll return with relevant 2026 UIT, voluntary Annex II cure before effective notice and full payment meeting the applicable rule: base fine 5,500 less 90% is 550 before applicable fine interest, not an assumed art. 13-B 100% waiver. These independent arithmetic cases do not establish a live penalty or entitlement without their stated facts.

```oa-check
name: Statutory hour method, overtime, night floor and conditional Annex-II relief
inputs:
  daily_hours: 8
  ordinary_salary: 3000
  uit: 5500
steps:
  old_period_hour: 1130 / 30 / daily_hours
  october_hour: 1230 / 30 / daily_hours
  ordinary_hour: ordinary_salary / 30 / daily_hours
  overtime: round(ordinary_hour * 2 * 1.25 + ordinary_hour * 1 * 1.35, 2)
  october_night_floor: 1230 * 1.35
  base_fine: uit
  fine_after_reduction: base_fine * (1 - 0.90)
  no_mype_lower: uit * 2.63
  no_mype_upper: uit * 52.53
expected:
  old_period_hour: 4.7083333333
  october_hour: 5.125
  ordinary_hour: 12.50
  overtime: 48.13
  october_night_floor: 1660.50
  base_fine: 5500.00
  fine_after_reduction: 550.00
  no_mype_lower: 14465.00
  no_mype_upper: 288915.00
```

**Refusal/regression guards:** unknown domicile means no resident/non-resident tax result; unknown ONP/AFP or AFP arrangement means no final pension/net; unknown period/RMA means no extrapolated premium; annual 3 UIT documents do not change employer withholding; high pay does not cap savings/flow commission; tax non-domicile does not switch off pension columns; employer health never reduces employee salary; benefit base/service gaps require the records, not a fixed percentage; generic bank narration does not settle a specific liability. These replace the old misleading defaults and preserve the old twelve-test topics with corrected inputs.

## Ask the client first

Use the existing records first, then ask only what is missing:

1. Contract/regime, employee identity, service and payment month, ordinary schedule, actual time/leave/subsidy records and remuneration components?
2. Tax domicile/source facts, other jobs, prior employers' income/retentions, actual year-to-date payments/credits, variable-pay method election, extraordinary pay and cessation events?
3. Pension affiliation/effective dates, AFP arrangement, period-specific official schedule and retirement/insurance-exemption documents? Never ask the client to supply a rate already in the official schedule.
4. EPS contract/covered-worker selection, actual population and payments, source-month limits and credits already used? Any SCTR/special-regime insurance?
5. Credited benefit service, variable-pay/family-allowance records, previous ordinary gratificación, CTS account, accrued/used vacation and termination documents?
6. Employer RUC/status, registration receipts/delivery, PLAME/AFP returns and payments, applicable due-date calendar/extensions and bank statements? If a fine/interest is requested, also obtain the exact failure/date, taxpayer table, turnover declarations, same-type infringement/training history and notifications, conviction-exclusion facts, cure/payment dates, current discretionary decision and applicable rate. Do not infer payroll relief from business turnover alone.

Complete the working paper only after inputs trace to evidence, bases and periods agree, exceptions are resolved, all bands/components recompute, filings/payments reconcile and unresolved matters are listed. Outputs remain informational/computational and require qualified professional review before implementation, preserving the existing professional-review requirement.

## Sources

Read dates mean actual operative portions read, not a response code or the whole contents of a compilation. The official XLS was downloaded and its actual cells/headers/notes read with an XLS reader; no unsupported web extraction was treated as a read.

| Source and portions actually read | URL | Read on |
|---|---|---|
| SUNAT UIT register, 2025/2026 rows and legal instruments | https://www.sunat.gob.pe/indicestasas/uit.html | 2026-11-11 |
| LIR chapter II, arts. 6-10 domicile/source | https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf | 2026-11-11 |
| LIR chapter IV, art. 18 statutory indemnities/CTS/subsidies and adjacent conditions | https://www.sunat.gob.pe/legislacion/renta/ley/capiv.pdf | 2026-11-11 |
| LIR chapter V, art. 34 employment income | https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf | 2026-11-11 |
| LIR chapter VI, arts. 45-46/49 work deductions and annual conditions | https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf | 2026-11-11 |
| LIR chapter VII, arts. 53 and 54(g) bands/non-domiciled employment | https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf | 2026-11-11 |
| LIR chapter XI, art. 79 fifth-category annual exclusion | https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf | 2026-11-11 |
| SUNAT annual campaign labelled Renta 2025, operative how-to paragraphs on FV 709, SOL and App Personas; historical procedure only, not a 2026-income form release | https://renta.sunat.gob.pe/personas/como-realizar-la-declaracion-del-impuesto-la-renta | 2026-11-11 |
| LIR Regulation X, arts. 40-44, current projection/divisors/extraordinary pay, variable option, cessation refund and multiple employers; historical text not used as current | https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf | 2026-11-11 |
| El Peruano DS 015-2026-TR, complete decree and future-tranche condition | https://busquedas.elperuano.pe/dispositivo/EX/2559163-1 | 2026-11-11 |
| Law 26790, arts. 5-6, 15-16 and 19; historical filing wording not used | https://www.essalud.gob.pe/transparencia/pdf/publicacion/ley26790.pdf | 2026-11-11 |
| SUNAT report 003-2007, operative analysis/conclusions on amended EsSalud floor, subsidies and unpaid months | https://www.sunat.gob.pe/legislacion/oficios/2007/oficios/i0032007.htm | 2026-11-11 |
| SUNAT report 088-2004, operative analysis/conclusions on EPS caps and timing | https://www.sunat.gob.pe/legislacion/oficios/2004/oficios/i0882004.htm | 2026-11-11 |
| ONP consolidated DS 354-2020-EF / DS 282-2021-EF, arts. 19, 22-26 minimum, withholding and collection | https://repocdn.onp.gob.pe/Normativa/Base_normativa/NPT046.pdf | 2026-11-11 |
| SBS November 2026 schedule, complete four-AFP table and notes, explicitly devengue 2026-11 | https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx | 2026-11-11 |
| SBS Title V, art. 2, 87(a)-(b), 87A/88, affiliation/retirement evidence and collection | https://www.sbs.gob.pe/Portals/0/jer/LEYES_SPP/2023/T%C3%ADtulo_V_SPP_15-11-2024.pdf | 2026-11-11 |
| SBS Aportes, operative employer remittance paragraphs and reform-update note | https://www.sbs.gob.pe/usuarios/aprende-con-la-sbs/aportes | 2026-11-11 |
| SUNAT T-Registro, employer-obligation and receipt-delivery tables | https://orientacion.sunat.gob.pe/03-obligaciones-del-empleador-t-registro | 2026-11-11 |
| SUNAT Emprender Planilla, obligations/SOL/PLAME Web/correction and displayed January 2026 calendar; superseded software version not used | https://emprender.sunat.gob.pe/principales-impuestos/planilla/planilla-electronica | 2026-11-11 |
| SUNAT presentation pp. 3-29, actual T-Registro/PDT fields, sync, validation, export, upload and payment process; current version supplied by 2026 resolutions | https://orientacion.sunat.gob.pe/sites/default/files/inline-files/PDF%20de%20T-Registro%20y%20PLAME.pdf | 2026-11-11 |
| RS 016-2026, complete two-page version 4.6 resolution | https://www.sunat.gob.pe/legislacion/superin/2026/000016-2026.pdf | 2026-11-11 |
| RS 213-2026, complete two-page version 4.7 resolution, affected periods and availability | https://www.sunat.gob.pe/legislacion/superin/2026/000213-2026.pdf | 2026-11-11 |
| SUNAT public receipt template, PLAME Web 0601 fields and NPS notice; no authenticated transaction | https://e-plataformaunica.sunat.gob.pe/app/recaudacion/tributaria/internet/html/carrito.html | 2026-11-11 |
| CTS TUO DS 001-97-TR, arts. 3-6, 9-18, 21-23, eligibility/base/variable pay/cessation/deposit dates | https://cdn.www.gob.pe/uploads/document/file/229267/TUO_Compensacion_por_Tiempo_de_Servicios_-_D.S_001-97-TR.pdf | 2026-11-11 |
| MTPE compendium, DS 003-97-TR art. 8 printed p. 43; DS 007-2002-TR arts. 1-12 pp. 265-271; DL 713 arts. 1-23 and DS 012-92-TR arts. 11-12/23-24 pp. 285-296; Law 27735/DS 005-2002-TR pp. 329-335; Law 30334/DS 012-2016-TR pp. 338-346 | https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495 | 2026-11-11 |
| Tax Code, arts. 33, 166, 176, 178 and 180, actual interest/infringement/base framework; current specific relief not presumed | https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf | 2026-11-11 |
| Tax Code arts. 165/180 as amended by Law 32335, mandatory preventive-training gate; DS 288-2025-EF regulation arts. 3-11 and both transitions, actual MEF web PDF read after direct download returned non-PDF HTML | https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf; https://www.mef.gob.pe/es/por-instrumento/decreto-supremo/34781-decreto-supremo-n-288-2025-ef/file | 2026-11-11 |
| RS 010-2026, complete four-page resolution, course notice/access/completion/final activity/constancia | https://www.sunat.gob.pe/legislacion/superin/2026/000010-2026.pdf | 2026-11-11 |
| Tax Code Table I, population/art. 176(1) and adjacent current/deleted rows | https://www.sunat.gob.pe/legislacion/codigo/tablaI.pdf | 2026-11-11 |
| Tax Code Table II, population/art. 176(1) and adjacent rows | https://www.sunat.gob.pe/legislacion/codigo/tablaII.pdf | 2026-11-11 |
| Tax Code Table III, art. 176(1), minimum/closure notes and adjacent withholding rule | https://www.sunat.gob.pe/legislacion/codigo/tablaIII.pdf | 2026-11-11 |
| RS 063-2007 original text, art. 1(f), art. 13 and second complementary final provision, read with amendments below | https://www.sunat.gob.pe/legislacion/superin/2007/063.htm | 2026-11-11 |
| RS 063-2007 Annex II original XLS, item 12 row, voluntary/induced column headers, cure method and notes 1-4/8; read actual worksheet cells | https://www.sunat.gob.pe/legislacion/superin/2007/063_anexo_ii.xls | 2026-11-11 |
| RS 078-2021, arts. 3.1-3.4 including prior-year UIT, payment definition, Annex II scope and unchanged art. 13-B(2) exclusion | https://www.sunat.gob.pe/legislacion/superin/2021/078-2021.pdf | 2026-11-11 |
| RS 007-2025, art. 3 amended 13-B(1)/(3)-(5), table and notes, commencement; older pending-penalty transitional application not supplied | https://www.sunat.gob.pe/legislacion/superin/2025/000007-2025.pdf | 2026-11-11 |
| Official RLGIT consolidation, art. 25.20 and arts. 47/48.1/48.1-A with adjacent special populations; table amendment DS 008-2020-TR in consolidation dated 26 February 2023 | https://diariooficial.elperuano.pe/Normas/obtenerDocumento?idNorma=47 | 2026-11-11 |

Not yet confirmed: other 2026 AFP devengue rates/RMA, including old Q2 estimate and claimed resolution attribution of an all-year premium; numeric current TIM/AFP interest, applicable individual sanction/relief/discretion and subsequent case-specific SUNAFIL changes; released 2026-income annual form/fields/population and 2027 calendar; current complete holiday calendar and special-sector/foreign social-security certificate outcomes; specific stock-option/company-car/severance valuation; exact record-specific retention/prescription period; proprietary live bank narration dictionaries. Do not infer missing affiliation, EPS eligibility, domicile, benefit service/base or prior withholding from defaults. The ordinary methods above do not establish the omitted figures.
