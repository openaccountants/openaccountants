---
name: guatemala-social-contributions
description: >
  Use this Guatemala reference for IGSS contributions in 2026: cuota laboral,
  cuota patronal, the salario total base, the contribución mínima, the INTECAP
  tasa and IRTRA impuesto collected with them, registration, the Planilla de
  Seguridad Social, recargos and the voluntary routes. Match requests such as
  how much IGSS do I pay, IGSS employee rate, IGSS employer rate, INTECAP IRTRA,
  Guatemala payroll deductions, salario minimo Guatemala, bonificacion incentivo,
  Q250 bono, ISR retencion empleados, ISR planilla, constancia de retencion,
  SAT-1331, crédito por IVA planilla and IGSS bank statement transactions. It
  ties each rate to its instrument, holds the IRTRA rate, and sends ISR
  computation to guatemala-payroll. This Tier 2 draft supports source checking
  and reviewer questions; it does not authorise filing, payment or a tax
  position.
version: 0.3
jurisdiction: GT
tax_year: 2026
tax_year_notes: "Calendar 2026. IGSS percentages are as read in the Junta Directiva acuerdos on the IGSS site on 5 November 2026. Minimum wages are as reported by Diario de Centro América for Acuerdo Gubernativo 256-2025, in force 1 January 2026. The IRTRA rate and the SAT rules are held."
last_updated: 2026-11-05
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: payroll
---

# Guatemala Social Contributions v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

This reference covers contributions to the Instituto Guatemalteco de Seguridad Social (IGSS) by employers (patronos) and workers in Guatemala, the INTECAP tasa and the IRTRA impuesto that IGSS collects with them, and the voluntary IGSS routes. Amounts are in quetzales (Q, GTQ only). Tax year: calendar 2026. Payroll ISR, owed to the Superintendencia de Administración Tributaria (SAT), appears only as a held item: `guatemala-payroll` and `guatemala-income-tax` own it.

| Person | Position | Basis and limit |
| --- | --- | --- |
| Employer | 'Todo patrono está obligado a inscribirse' and to register its workers, without prejudice to exceptions in other institutional reglamentos. A patrono is a natural person who owns a business, or a legal person, using 1 or more workers under a contract or labour relationship. No acuerdo read sets a different number by department or activity | Acuerdo 1529 Art 6; Gerencia 06/2023 Art 2. Acuerdo 1529 Art 38 repealed Acuerdo 1123, which legacy gives as the former 3-worker rule; Acuerdo 1123 itself was not read. IGSS's undated registration guide still says 3 or more, or 1 or more in land transport, and cites Acuerdo 1123, so it appears to predate Art 6: this draft follows the acuerdo. The exceptions in the other reglamentos were not all read: see the rows below for those found |
| Who is the patrono | A natural or legal person. In construction: the owner, where a professional, maestro de obra or construction firm's agent carries out the work with no construction contract, or the contractor where the work is under contract. Owners or co-owners of unincorporated businesses who exercise general administrative direction of the common assets. Lessees of a mercantile business or agricultural unit, for the term of the lease | Acuerdo 1529 Art 8 |
| Employer with fewer than 3 workers | The duty is the same, but the date obligations start follows the inscription resolution. Gerencia 06/2023 Art 1 numeral 2 ties it to the resolution taking effect within 30 calendar days of notification; numeral 4, on inscription de oficio, ties it to the notification date | Needs Input: ask for the resolution. The legacy date of 17 January 2023 is when Acuerdo 1529 took effect, not when each such employer's obligations began |
| Legal representatives, shareholders and spouses of the patrono who have worker status | Incorporated by resolution; the notification date fixes the obligations | Gerencia 06/2023 Art 1 numeral 5 |
| Worker | A natural person providing material or intellectual services, or both, under a contract or labour relationship. Permanent, temporary and part-time workers all contribute | Acuerdo 1529 Art 10; Res 08-SGF/2026 para 1 |
| Registered part-time worker | Shorter than the ordinary working-day limits with the same employer, and so defined in a contract that meets the registration and authorisation requirements. Separate calculation in the Rates table | Acuerdo 1522 with AG 258-2022. Employer must register or update on form DRPT-59 and identify the worker in the planilla: Res 876-SGF/2023, OCR read in part |
| State | As employer and as such, at separate rows and under 1421 Art 37. Army personnel are outside Acuerdo 410 (Art 83). Officials under Acuerdo 522 are outside the IVS afiliado definition. IGSS's registration guide reproduces Acuerdo 522 Arts 1 and 2: listed office-holders, including the President, ministers, deputies, mayors and diplomatic agents, are not affiliated and owe no contributions | Worked figures here are for private employers. Acuerdo 522 itself was not read, so check the list against it |
| Universities | Gerencia 31/2022 Art 1(d) lists them as a proportional case for the contribución mínima, on the exemption in Constitution Arts 88 and 100. Res 08-SGF/2026 says that status is respected | Needs Input: the Constitution and the extent of the exemption were not read |
| Domestic workers (PRECAPI) | Special programme, administered at flat figures in the capital and the municipalities of the Department of Guatemala | IGSS leaflet, administrative. Reglamento number not found; the leaflet cites Acuerdo 1235 Art 37, not read |
| Eventual agricultural workers | Special Enfermedad y Maternidad cover under Acuerdo 1292, where IGSS has implemented it | Acuerdo 1292 Arts 2, 5, 8, 12. No special rate read. Gerencia 02/2024 not read |
| Self-employed person | Not a 'trabajador' under the definitions above. Decreto 295 Art 27 lets IGSS include all active inhabitants gradually, and no independent-worker regime was found in the instruments read. Treat that as held, not as a rule that none exists. Decreto 295 Art 72 a) allows a seguro facultativo simple, a voluntary contract with IGSS for a person or group not obliged to the regime; its terms for a self-employed person were not read. Employer and employee rates do not apply to the person's own income | The routes are voluntary: Rates table and Example 4 |

### What this file is

This is a Tier 2 source-cited draft. It has no accountant sign-off, and no accountant has reviewed this version. Treat every working it produces as a working paper only: an estimate for a reviewer, never an exact amount. IGSS's planilla validation and receipt settle what a client pays.

IGSS's own instruments were read on its site. Many are scans: they were read through local OCR, which is not qualified for Spanish. Only 3 passages were checked by eye on the page image: Acuerdo 1520 Arts 1 to 4, Acuerdo 1522 Arts 5 and 6, and Acuerdo 1002 Art 46 c). Every other figure from a scan rests on OCR alone, including the unreformed articles of Acuerdo 1421 and Res 08-SGF/2026. A plain curl request with its default user agent to congreso.gob.gt, portal.sat.gob.gt and irtra.org.gt returned 403, and one further diagnostic request showed a Cloudflare challenge on the last 2. Logged fetches of mintrabajo.gob.gt's decree and minimum wage pages and of gae.gob.gt returned 403. None was retried around the block. The Organismo Judicial and FONDETEL hosts did not connect. No archive copy was used. What depended on those sources is held below.

**Status against `social-contributions-workflow-base` Section 6.** Slots filled: 5 (registration), 8 (income tax interaction, as held), 9 (patterns), 10 (refusals and defaults), 12 (examples). Partly filled: 1 (the IRTRA rate is held), 2 (Bono 14 and pay in kind are Needs Input), 3 (the floor figure for an employer outside the Department of Guatemala, the pro-ration formula and the multiple-employment rule are held), 4 (IVS status is Needs Input and the self-employed regime is held), 6 (period calendars and bank reference formats unread), 7 (recargo rate unread), 11 (Res 08-SGF/2026 para 93 gives a tolerance, not a rounding rule). A figure that rests on a partly filled slot is Needs Input. For a payroll run, `payroll-workflow-base` and `guatemala-payroll` own the payslip figures.

### Refusals and boundaries

A refusal is a full stop: give the message and classify nothing further.

- **R-GT-1, salario total unknown.** Trigger: the worker's pay for the period is not given by component. Message: 'The pay for the period, by component, is mandatory. IGSS cuotas run on salario total, which includes overtime and bonuses except those the law excludes. I cannot compute IGSS without it.'
- **R-GT-2, arrears.** Trigger: the employer has unpaid IGSS contributions and wants an amount. Message: 'Recargos use the last maximum annual simple rate set by the Junta Monetaria, capped at the contributions in mora, and a Nota de Cargo adds 5% capped at Q3,000. I do not have that rate. Get an IGSS statement and escalate to a licensed Guatemalan accountant. I can show the Nota de Cargo charge only.'
- **R-GT-3, pension projection.** Trigger: the client wants a projected IVS pension or a statement of the pension they will get. Message: 'IVS sets a Remuneración Base limit of Q9,000 and a pension limit of 80% of it, but a personal projection needs IGSS's contribution record. Confirm with IGSS.' State those 2 limits and go no further.
- **R-GT-4, minimum wage ISR.** Trigger: a request to apply the Decreto 13-2026 treatment to a worker's ISR. Message: 'The decree text was not read here. The official gazette reports the 2026 exemption and a Q3,024 extraordinary deduction. Confirm the text and the worker's pay with a licensed accountant and use guatemala-payroll.'
- **R-GT-5, department rate.** Trigger: a client says a department has a different rate, or wants a rate certified for a department. Message: 'The texts read show no rate that differs by department, and only one extension acuerdo was read in full. I cannot certify a department outside it. Confirm with IGSS.'
- **R-GT-6, self-employed with no route.** Trigger: a self-employed person has no contribution history or does not meet the Art 35 test, and no other voluntary route with a stated rate in the Rates table fits. Message: 'I found no IGSS contribution rate for this person in the texts read. Decreto 295 allows a voluntary seguro facultativo simple by contract with IGSS, but I have not read its terms. I will not apply employee or employer rates to their income. Ask IGSS directly.'
- **R-GT-7, disguised employment.** Trigger: a question whether a contractor or 'servicios profesionales' arrangement is a labour relationship. Message: 'Whether this is a labour relationship is a legal question on the facts. Escalate to a licensed Guatemalan adviser.'
- **R-GT-8, exoneration.** Trigger: a client wants to rely on an exoneration of recargos. Message: 'The 2026 programme read ran from 25 March to 24 September 2026 and its acuerdo text was not obtained. Ask IGSS in writing whether any programme is open.'

### Missing facts

| Missing fact | Action |
| --- | --- |
| Pay by component | R-GT-1 |
| Character of a bonus | Needs Input: ask its name, the law it rests on and the justification. Art 4 puts a bonus in the base unless its creating law excludes it |
| Whether a worker is outside IVS | Needs Input. 1421 Art 12 recognises workers 'afectos y no afectos'. Acuerdo 1124 Art 31 covers an employed pensioner, by the health programmes; it does not use those words, and no text read gives a general list. Do not apply 3% and 7% without evidence |
| Economic activity, department or circunscripción | Needs Input where pay is at or near the floor. Do not assume C1 or C2 |
| Employer's number of workers | Registration is required at 1 or more, so an employer with workers is treated as obliged. The start date is Needs Input where there are fewer than 3 |
| Registration status | Treat as required, on Acuerdo 1529 Art 6. Whether arrears exist is Needs Input |
| Start or end date, or an IGSS medical suspension, in the month | Needs Input where the floor applies. Gerencia 31/2022 makes the floor proportional, and Res 08-SGF/2026 para 1 says proportional to time worked, with no formula |
| INTECAP position | Needs Input: entity type, activity, permanent workers if agricultural, and any convenio |
| Unmatched or bundled IGSS receipt | Credit nothing to a period until the receipt or planilla splits it |
| Tier 2 question threshold | GTQ 0: no row is filtered on amount, as no Guatemalan floor was set |

### Rules for using this file

- Compute cuotas on salario total, not 'ordinary salary'.
- Never deduct INTECAP or IRTRA from a worker. Art 28 of Decreto 17-72 calls INTECAP a tasa patronal. IRTRA's text was not read; IGSS's instrument treats both as charged to 'patronos afectos'.
- Do not use a rate from a commentary as law. Each confirmed rate below has its instrument.
- Do not add IRTRA into a confirmed total. Show it apart and labelled.
- A floor applies only where salario total is below the monto base.
- Do not call any figure final. Present every figure as an estimate and point the client to IGSS and SAT records.
- Do not confuse SAT debits with IGSS debits.
- Do not use the Decreto 13-2026 treatment for an earlier year, or in any year without its text.

## Rates, bands and thresholds

Percentages apply to salario total as defined under 'The base'. No IGSS rate below varies by employer size. Acuerdo 410 Art 85 says its rates are those for the Department of Guatemala, and the extension acuerdos set them elsewhere; its footnote 21 lists Acuerdos 475, 616, 621, 849, 1024, 1095, 1121 and 1243, and only 1243 (Santa Rosa, El Progreso, Petén) was read, at the same 4% and 2%. IGSS's 2022 notice and Acuerdo 1520 Art 2 state uniform shares and no department variation, so this draft uses the rows below everywhere, with R-GT-5 for a contrary claim. That covers employer and worker rates only: the State's own share has a narrower scope, stated in its row.

| Item | Figure | Applies to | Source and limit |
| --- | --- | --- | --- |
| Enfermedad y Maternidad | Employer 4.00%, worker 2.00%, together 6.00% | Private employers and the State as employer | [Acuerdo 410, rev 2018, Art 62](https://www.igssgt.org/wp-content/uploads/2026/10/Acuerdo-410-Junta-Directiva-IGSS-1967-rev-2018.pdf). Acuerdo 1243 Art 5 agrees for its departments |
| Accidentes | Employer 3.00%, worker 1.00%, together 4.00% | Patronos and afiliados, on total monthly salaries | [Acuerdo 1002 Art 46](https://www.igssgt.org/wp-content/uploads/2026/10/Acuerdo-No-1002-de-Junta-Directiva-IGSS.pdf). Acuerdos 1023, 1031, 1097 and 1157 checked: none changes it |
| Invalidez, Vejez y Sobrevivencia (IVS) | Employer 3.67%, worker 1.83%, together 5.50% | Private employers and the State as employer; affiliated workers | [Acuerdo 1124, rev 2021, Art 40](https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-1124-Junta-Directiva-IGSS-Rev-2021.pdf). Art 40 d) struck out by the Corte de Constitucionalidad, file 732-2003 |
| IGSS total | Employer 10.67%, worker 4.83%, together 15.50% | Workers in all 3 programmes | [IGSS notice, 3 October 2022](https://www.igssgt.org/noticias/2022/10/03/el-igss-fija-cuota-minima-de-contribuciones-a-la-seguridad-social/). The sum of the 3 rows above. Acuerdo 1520 Art 2 uses the same shares. Legacy cited Acuerdo 1118, repealed by Acuerdo 1421 Art 47 |
| Workers not obliged to IVS | Employer 7.00%, worker 3.00%, together 10.00% | Only with evidence of the status | [Acuerdo 1520 Art 2](https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-Gubernativo-239-2022-y-Acuerdo-1520-de-Junta-Directiva-IGSS.pdf) gives the split proportions; the 7%, 3% and 10% are derived from the first 2 rows |
| State as such | Enfermedad y Maternidad: 1% of total salaries of private employers' workers and of its own, in the Department of Guatemala only. In Acuerdo 1243's departments, the proportion the State budget sets: figure not read. Elsewhere held. Accidentes: 1½% of those total salaries. IVS: 25% of benefits paid | The State, not an employer rate | [Acuerdo 410 Art 62](https://www.igssgt.org/wp-content/uploads/2026/10/Acuerdo-410-Junta-Directiva-IGSS-1967-rev-2018.pdf); Acuerdo 1002 Art 46 c), read on the page image; Acuerdo 1124 Art 40 c); [Acuerdo 1243 Art 5 c)](https://www.igssgt.org/wp-content/uploads/2026/10/acdo1243_2010ger.pdf). Art 85 confines Art 62 to the Department of Guatemala, and footnote 23 points to the same clause of each extension acuerdo |
| Contribution ceiling | None found in the texts read: held | Cuotas. Treat figures at high pay as conditional on no ceiling: Needs Input, confirm with IGSS | [Acuerdo 1421 as reformed](https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-Gubernativo-239-2022-y-Acuerdo-1520-de-Junta-Directiva-IGSS.pdf) has none, and Art 4 uses salario total. An absence in the texts read, held. The Q9,000 limit below is a benefit limit |
| Contribution floor | Contribución mínima = percentages in force x monto base: 15.50% for a worker in all 3 programmes, or 10.00% for a worker not obliged to IVS. Monto base = diurnal minimum wage for the economic activity, on at least 8 hours, x 243.3333 if fixed by hour, x 30.4167 by day, x 1 by month | Applies only where salario total is below the monto base, whatever the contract, jornada, days worked or circunscripción | same; 1421 Art 5, read on the page image. Art 5 says 'los porcentajes fijados por la normativa institucional vigente'. IGSS's published minimums use 15.50% only, so the 10.00% floor is this draft's reading: confirm with IGSS |
| Who pays at the floor | Worker on actual pay at 4.83%, or 3.00% if not obliged to IVS; employer max(minimum - worker share, 0) | Same. Examples 2 and 6 | same; [IGSS notice](https://www.igssgt.org/noticias/2022/10/03/el-igss-fija-cuota-minima-de-contribuciones-a-la-seguridad-social/) |
| Registered part-time worker below 1 minimum wage | Employer Cp = (RMV x Fa x 0.155) - (RR x 0.0483), worker RR x 0.0483, Fa initially 1. Where pay reaches 1 minimum wage, the normal percentages apply | Workers under Acuerdo 1522, with cover conditional on Art 3 | [Acuerdo 1522 Art 5](https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-Gubernativo-258-2022-y-Acuerdo-1522-de-Junta-Directiva-IGSS.pdf), read on the page image. RMV = monthly minimum wage, RR = real pay. The acuerdo also sets State shares of 3.5% and 1.83% of the base mínima. The 0.155 and 0.0483 are the all-3-programme rates. Neither the acuerdo nor Res 876-SGF/2023 gives a variant for a part-time worker outside IVS: Needs Input |
| Minimum wage 2026, Circunscripción 1 | Non-agricultural Q131.58 daily, Q4,002.28 monthly; agricultural Q124.64, Q3,791.20; export and maquila Q112.10, Q3,409.73 | In force 1 January 2026 | [DCA, AG 256-2025](https://dca.gob.gt/noticias-guatemala-diario-centro-america/gobierno-fija-nuevos-salarios-minimos-para-2026/), a gazette news item; AG text not read. IGSS's PRECAPI leaflet prints the Q4,002.28. DCA and legacy say C1 is the Department of Guatemala; the AG was not read |
| Minimum wage 2026, Circunscripción 2 | Non-agricultural Q125.49, Q3,816.90; agricultural Q119.21, Q3,625.89; export and maquila Q105.90, with Q3,321.10 in the DCA note | Same | same. The export figure is in conflict: a search digest says Q3,221.10 and Q105.90 x 30.4167 = Q3,221.13. Held |
| Bonificación incentivo amount | unverified: Q250 monthly | Private sector workers | Decreto 37-2001 not read: OJ did not connect. Q250 appears here only from a search digest of that decree. DCA confirms the employer's duty under Decreto 78-89 without the amount |
| INTECAP tasa, non-agricultural | Steps to 0.75%, with a maximum of 1.00% from 1 January 1974 | Monthly, on all sueldos y salarios of private companies and entities, and public entities with for-profit activity, except pay not subject to IGSS | [Decreto 17-72 Art 28](https://www.intecap.edu.gt/informacionpublica/pdf/Ley%20Organica%20INTECAP.pdf), INTECAP's copy. 1.00% is 'su límite máximo'; Art 28(3) needs a Junta Directiva finding and its acta was not read. This draft uses 1.00% as that maximum, labelled |
| INTECAP tasa, agricultural | Steps to 0.75%, with a maximum of 1.00% from 1 January 1975, on permanent workers only. Exonerated with fewer than 10 permanent workers; permanent means over 1 year without interruption | Agricultural and livestock companies | same, Art 28(2). The text does not say how workers are counted across sites: Needs Input |
| INTECAP, not charged or reduced | Universities and private entities not pursuing profit are excepted. A convenio can reduce the rate by up to 80%, with quarterly reimbursement | As stated | same, Arts 29, 30. Legacy 'all employers' corrected |
| IRTRA impuesto | unverified: 1% | Reported: ordinary and extraordinary salary of workers of private for-profit companies under the Código de Comercio | Decreto 1528, Decreto 43-92 and Decreto 9-2024 not read: congreso.gob.gt and irtra.org.gt blocked the fetch. Only a search digest of iniciativa 6314 gives the rate. Res 08-SGF/2026 para 76 confirms IGSS collects it from 'patronos afectos', and no rate |
| Benefit limit, IVS | Remuneración Base at most Q9,000; pension at most 80% of it, so Q7,200 derived; minimum Q340 for invalidez total or vejez | Benefits, not contributions | [Acuerdo 1124](https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-1124-Junta-Directiva-IGSS-Rev-2021.pdf) Art 29 (Q9,000), Art 3 definition and Art 9 (80%), Art 30 (Q340). Legacy 'never state' replaced |
| Contribuyente Voluntario | 3.67% + 1.83% = 5.50% of the salary of the last month of obligatory contribution, or the month before if work was interrupted, monthly. IVS only | Former contributors with at least 12 months in the last 36. Written request: see 'Deadlines and filing'. Lost after 3 consecutive months in mora (Art 36). A voluntary contributor who returns to obligatory employment stops being voluntary from that date, and needs at least 9 months of obligatory contribution to become voluntary again, with earlier voluntary contributions counting towards the 12 (Art 37). Return after an Art 36 lapse with no new employment is not addressed in the text read: Needs Input | same, Arts 35 to 37; [IGSS 2026 notice](https://www.igssgt.org/noticias/2026/03/02/como-ser-contribuyente-voluntario-en-el-igss-respondemos-las-dudas-mas-frecuentes/) says it suits independents, professionals and merchants who meet the requirements |
| Cuotas Faltantes | Up to 12 contributions at Art 40 a) and b) rates, on the salary of the last obligatory month, or the non-agricultural minimum wage if higher at request | Age 60 or over, vejez pension applied for, IGSS has determined the missing contributions | [Acuerdo 1521](https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-Gubernativo-257-2022-y-Acuerdo-1521-de-Junta-Directiva-IGSS.pdf) |
| Migrante Guatemalteco | Q1,000.00 monthly, updated yearly, payable monthly, quarterly, half-yearly or yearly in advance | Voluntary, for Guatemalan migrants who register | [Acuerdo 1543 Arts 11, 12](https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-Gubernativo-No-215-2023-y-Acuerdo-No-1543-de-Junta-Directiva-del-IGSS.pdf); [IGSS page](https://www.igssgt.org/trabajador-migrante-guatemalteco/) still shows Q1,000.00 |
| PRECAPI | Worker Q151.83, employer Q303.66, total Q455.49, paid quarterly, first quarter in advance | Domestic workers, capital and Department of Guatemala municipalities | [IGSS leaflet, rev 2026](https://www.igssgt.org/wp-content/uploads/2026/08/Trifoliar-Programa-PRECAPI-IGSS-rev-2026.pdf). Administrative. Whether the figures are per month or per quarter is not clear from the leaflet: confirm with IGSS |
| Seguro facultativo simple | No rate read | A person or group not obliged to the regime, by voluntary contract with IGSS, for the same benefits as obligatory affiliates | [Decreto 295 Art 72 a)](https://www.igssgt.org/wp-content/uploads/2026/09/Decreto-No-295-y-sus-reformas-Decreto-No-11-04-Ley-Organica-del-IGSS-Guatemala.pdf), OCR scrambled here, with the wording checked against the copy in IGSS's registration guide. Acuerdo 410 Art 79 and Acuerdo 1002 Art 63 give the Gerencia power to contract it. Art 79's conditions speak of a patrono, so its reach to a self-employed person is open. Held: terms and cost not read |
| Closed window | Acuerdo 1429: age 55, 180 contributions by 31 December 2010 | Closed, listed so nobody offers it | [AG 200-2019](https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-1429-de-Junta-Directiva-IGSS-y-Acuerdo-Gubernativo-200-2019.pdf) |
| ISR rates | unverified: 5% to Q300,000 of annual taxable income, then Q15,000 + 7% of the excess | Payroll ISR | Decreto 10-2012 not read: SAT and Congreso blocked. Owned by `guatemala-payroll` |
| ISR personal deduction 2026 | Q48,000 limit plus Q3,024 extraordinary deduction without proof, for 2026 | Payroll ISR | [DCA, 18 May 2026](https://dca.gob.gt/noticias-guatemala-diario-centro-america/oficializan-que-salario-minimo-esta-exento-de-isr/), a gazette news item; Decreto 13-2026 text not read |
| ISR other deductions | unverified: IVA credit capped at Q12,000 yearly, on a filed planilla; donations to non-profits capped at 5% of gross income; life insurance, non-dotal | Payroll ISR, with documents | Legacy figures, no primary read. Owned by `guatemala-income-tax` |
| Legacy derived figure | unverified: Q51,027.36, being 12 x (Q4,002.28 + Q250) | Derived, never published | Rests on the Q250 row and on the Decreto 13-2026 rule in the hold list under Sources |

Legacy's 'totals' of 12.67% and 17.50% are not used: they add an unverified IRTRA rate and INTECAP's maximum to a confirmed rate.

## The base

Acuerdo 1421 Art 4, as reformed by Acuerdo 1520 (AG 239-2022, DCA 28 September 2022, read on the page image), defines salary as the pay 'sea cual fuere su denominación o método de cálculo' if it can be valued in legal tender. Cuotas are computed on 'el salario total del trabajador, que comprende el devengado durante las jornadas ordinarias, extraordinarias y bonificaciones, excepto aquellas cuyas leyes de creación las excluyan', provided it is not below the monto base. Legacy's 'ordinary salary' was wrong.

| Component | Treatment | Basis and limit |
| --- | --- | --- |
| Ordinary pay and overtime | In | Art 4 |
| Commission or other pay under any name | In | Art 4 definition, by its words. No IGSS text on commissions read |
| Pay in kind | Needs Input | In if it can be valued in legal tender. Valuation method not read |
| Aguinaldo | Out | Art 4 exception |
| Indemnización and compensación de vacaciones en dinero on termination | Out | Art 4 exception. Limited to payments at the end of the contract |
| Bonuses whose creating law excludes them | Out | Art 4 exception. Name the law |
| Salary paid as a complement to an IGSS temporary incapacity subsidy, for accident or illness | Out | Art 4, last sentence |
| Bonificación incentivo under Decretos 78-89, 7-2000 or 37-2001 | Out, conditionally | IGSS notice of 23 November 2018 alone. See below |
| Bono 14 | Needs Input; reading is in | See below |
| Any other bonus | In unless a law expressly excludes it | IGSS notice of 23 November 2018 |

**Bonificación incentivo.** A footnote to repealed Acuerdo 1118 Art 4 records that the Corte de Constitucionalidad on 8 October 2003 (files 580, 613 and 649-2003) struck the phrase 'así como la bonificación incentivo hasta por la cantidad que fija la ley', which sat in that article's list of exceptions. The ruling was not read, so its effect is not stated here, and the footnote gives no support for the treatment in the table. Acuerdo 1421 replaced 1118, and its Art 4 does not name the bonus. 'Out, conditionally' rests on the IGSS notice of 23 November 2018 alone, where an IGSS official explains the rule: administrative, not law. It says Art 4 'no modifica en lo absoluto la bonificación otorgada por el Decreto 78-89 y sus modificaciones, incluida su interpretación constitucional', which applies 'exactamente como hasta antes de la derogatoria del Acuerdo 1118', provided the bonus is justified and fits the concept under Decretos 78-89, 7-2000 or 37-2001. Any other bonus not expressly excluded by law counts as salary. That the bonificación is outside the base is this draft's inference from those sentences. The decrees were not read, so 2 points are held: the text of any exclusion and whether an amount above the Q250 is also out. The condition matters: a bonus that does not fit the concept is salary, as Example 1 shows. IGSS's 2022 minimum contribution figures show a monto base with no bonus in it, which concerns the floor, not salario total.

**Bono 14.** Decreto 42-92, read in an ONSEC compendium copy, contains no clause excluding Bono 14 from IGSS: it excludes it from the aguinaldo (Art 6), and counts it for indemnización (Art 4). On Art 4 of 1421 and the IGSS 2018 notice it therefore falls in the base. This is this draft's reading. No IGSS statement on Bono 14 was found and later amendments to Decreto 42-92 were not checked, so show both figures and ask the reviewer before a planilla relies on either.

**Employer and undeducted cuotas.** Employer cuotas cannot be deducted from workers, and worker cuotas not deducted fall on the employer (1421 Art 6). The employer deducts when it pays, and records the deduction in its accounts and its register of workers and salaries (Art 4).

**Multiple employers.** No text read says how the floor or the planilla works for a worker with 2 employers. Needs Input. Two benefit-side rules exist: Res 876-SGF/2023 treats part-time contributions with 2 or more employers in one month as a complete contribution, and Acuerdo 1292 Art 7 recognises an eventual agricultural worker's subsidy through one employer only.

**Construction.** Where work was done with no registration, IGSS can register de oficio and estimate salaries at 35% of the value of the work, from the licence, valuation or contract (Acuerdo 1529 Art 9).

| Salario total | Worker 4.83% | Employer 10.67% | INTECAP at 1.00% maximum |
| --- | --- | --- | --- |
| Q4,002.28 | Q193.31 | Q427.04 | Q40.02 |
| Q5,000.00 | Q241.50 | Q533.50 | Q50.00 |
| Q10,000.00 | Q483.00 | Q1,067.00 | Q100.00 |
| Q25,000.00 | Q1,207.50 | Q2,667.50 | Q250.00 |

The rows are for a worker in all 3 programmes and assume no ceiling applies: see the rates table.

### Income tax interaction

Decreto 10-2012 was not read. Legacy quoted its Art 72(c) from an ICEFI analysis, which was not reread here, as allowing IGSS cuotas as a deduction: treat that as conditioned. `guatemala-payroll` uses the full 4.83%. Decreto 17-72 Art 33 makes INTECAP contributions deductible for ISR. The Diario de Centro América note of 18 May 2026 reports that Decreto 13-2026 makes minimum wage earners exempt from ISR through a Q3,024 extraordinary deduction for 2026 under its transitional Art 4, in force 8 days after publication. Legacy's 'exempt from 2026 onward' is therefore conditional on the decree text. Legacy ISR examples and tests are not repeated here, as their figures rest on an unread statute.

### Bank narrations

These patterns are unsourced classifier hints, not law. Banks seen in earlier versions were Banco Industrial, Banrural, BAM, G&T Continental and BAC. One IGSS receipt, the 'Recibo Electrónico de Cuotas de Patronos y de Trabajadores Impuesto IRTRA y Tasa INTECAP', can carry cuotas, IRTRA and INTECAP together, so separate lines cannot be assumed. IGSS and ISR payments are outside IVA: they are payroll obligations, not taxable supplies. Match on the bank's counterparty or reference text. Where a narration matches 2 rows, the row naming the tax wins over bare SAT: SAT IVA is VAT and SAT RETENISR is ISR.

| Narration | Meaning | Treatment |
| --- | --- | --- |
| IGSS, I.G.S.S., INSTITUTO GUATEMALTECO DE SEGURIDAD SOCIAL, SEGURIDAD SOCIAL, PLANILLA IGSS, IGSS CUOTA | IGSS payment; may be bundled | Split only from the receipt or planilla |
| CUOTA PATRONAL, CUOTA LABORAL, DESCUENTO IGSS | Employer or worker share | Label as stated; check against the planilla |
| INTECAP, IRTRA | May be a separate line, or inside an IGSS receipt | Rate check only for INTECAP; never treat as a worker deduction |
| SAT, SUPERINTENDENCIA DE ADMINISTRACION TRIBUTARIA, with no tax named | Tax payment, not IGSS; tax not stated | Needs Input: ask which tax, from the SAT receipt |
| ISR, RETENCION ISR, RETENISR, SAT RETENISR, SAT ISR, SAT-1331, FORMULARIO 1331 | ISR, not IGSS | Send to `guatemala-payroll` |
| IVA, FEL, SAT IVA | VAT, not payroll | Not this file |
| SALARIO, SUELDO, NOMINA, PLANILLA (outgoing) | Pay | Payroll expense, not a contribution |
| BONIFICACION INCENTIVO, BONO 250 | Bonus | Not a contribution. Base test above |
| SALARIO, SUELDO (incoming) | Income received | Not a contribution |
| IGSS PENSION, JUBILACION, PENSION | Pension received | Inbound benefit, not a contribution |
| IGSS SUBSIDIO, INCAPACIDAD | Subsidy received | Inbound benefit, not a contribution |
| MORA, RECARGO, NOTA DE CARGO, AVISO DE COBRO, RECONOCIMIENTO | Arrears, possibly with charges | Needs Input: split principal and charges from IGSS's statement |

If a client gives a bank statement but cannot answer yet, this is intake only: identify the IGSS debits and ask the questions in 'Ask the client first' before any output. Do not back-solve salary from a debit, because the debit may be bundled, cover several workers, or include a floor top-up. Unanswered items stay Needs Input.

## Deadlines and filing

Filing runs through the Portal de Servicios Electrónicos del IGSS (https://servicios.igssgt.org), reached from the IGSS site. An employer asks for access on form DRPT-53 and generates, transmits, validates and pays the electronic Planilla de Seguridad Social. Payment is through a bank's virtual banking, against the electronic receipt. One file covers several sites, workers in and out of IVS, activities, regions and weekly, fortnightly or monthly pay (1421 Art 12).

| Item | Deadline | Basis and limit |
| --- | --- | --- |
| Planilla and cuotas, ordinary | By the 20th of each calendar month, for salaries paid in the previous calendar month, unless IGSS sets its own calendar | 1421 Art 9. A deadline on a day IGSS is closed moves to its next working day (Art 42) |
| Weekly and catorcenal periods | IGSS's 2026 calendar has separate tables | [IGSS calendar page](https://www.igssgt.org/patronos/calendario-de-pagos-2026/) read; its PDF tables were not. Needs Input |
| Employer registration | 30 working days from the start of the obligation | Acuerdo 1529 Art 34 |
| First payment without recargos, after timely registration | 30 calendar days after inscription | Acuerdo 1529 Art 34. IGSS's undated registration guide says 30 working days from notification of the resolution: confirm with IGSS before relying on the longer period |
| Updating employer or worker data | 10 working days | Acuerdo 1529 Art 32 |
| Paying or challenging a Nota de Cargo | 15 working days from the day after notification | 1421 Art 21 |
| IGSS account statement | Issued within 10 working days from the day after the request | Res 91-SGF/2026 Procedimiento 11 norm 5, an internal manual. IGSS's undated collection guide says 15 working days |
| Claim for an amount paid in error | One year from the payment | IGSS's undated collection guide, citing Acuerdo 36 de Gerencia Art 53, not read. Confirm with IGSS |
| Contribuyente Voluntario request | 'En el curso del año calendario siguiente' to the last contributed month or last subsidy day | 1124 Art 35 a), reformed by Acuerdo 1437. IGSS's notice adds 'un mes después de haber terminado la relación laboral': confirm with IGSS |
| SAT-1331 (RetenISR2 Web) monthly ISR withholding | unverified: monthly | SAT not read. Owned by `guatemala-payroll` |
| SAT-1431 employee deduction declaration | unverified: yearly, January to March window | SAT not read |
| Constancia de retención | unverified: 10 working days from final or yearly payment | Legacy secondary source only |
| Yearly ISR liquidation or refund | unverified: 28 February of the following year | Legacy secondary source only |
| IVA-FEL planilla | unverified: first working days of January, commonly 10 January | Legacy secondary source only |

Documents for registration are listed in Acuerdo 1529 Arts 17 and 18. Rectification and complementary planillas are in Res 08-SGF/2026 para 6, and they generate recargos automatically.

### Working paper

```text
GUATEMALA IGSS WORKING PAPER (working paper only)
Employer: ____________  IGSS patronal no.: ________  Worker: ____________  Period: ________  Date: ________

A. Status: number of workers; inscription date and resolution; contract type; IVS status
B. Salario total: ordinary pay; overtime; other pay; each bonus with the law relied on
   Excluded: aguinaldo; termination payments; subsidy complement; bonificación incentivo if it meets the condition
C. Floor: activity; circunscripción; monto base; salario total below it? yes / no
D. Cuotas: worker 4.83% (3.00% if not obliged to IVS); employer 10.67% (7.00% if not obliged to IVS); floor top-up; IGSS total
E. Apart from the total: INTECAP (position and rate); IRTRA (unverified)
F. Due date; planilla no.; receipt no.; bank debit matched
G. ISR: not computed here. Send to guatemala-payroll

REVIEWER FLAGS
[ ] Every bonus tested against Art 4; Bono 14 position stated with both figures
[ ] Overtime included
[ ] Floor tested, and the C1 or C2 figure justified
[ ] IRTRA and INTECAP rates checked against their law and the IGSS receipt
[ ] Registration start date confirmed where fewer than 3 workers
[ ] No Needs Input item converted into a figure
```

## Penalties and interest

| Item | Amount or rule | Basis and limit |
| --- | --- | --- |
| Failure to file or pay on time | Administrative collection. A refusal lasting over 3 months goes to the Art 14 procedure. IGSS still receives cuotas if IRTRA or INTECAP are not paid voluntarily, and reports that to those bodies | 1421 Arts 11, 14; Res 08-SGF/2026 para 76 |
| Recargos por mora | 'la última tasa de interés simple máxima anual, determinada por la Junta Monetaria, tomando como base la tasa ponderada bancaria para operaciones activas', applied to the contribution owed: cuotas x rate x days late / 365 (366 in a leap year). Runs from the day after the due date until payment. Never above the contributions in mora. Employer alone bears it, and it cannot be passed to workers | 1421 Art 38; Res 08-SGF/2026 paras 51, 79. The rate figure was not found. Do not quantify: R-GT-2 |
| Late planilla accepted without recargos | Four cases: an interrupted relationship resumed by direct agreement, requested within 6 months of resumption; a retroactive raise from collective bargaining, within 6 months of paying it; a court order to reinstate or adjust salary, within 6 months of reinstatement unless the judge sets a term; a cause attributable to IGSS. Payment within the term stated in the request, up to 45 working days from the day after notice of IGSS's oficio, or recargos apply. On a request made before that term ends, the term can be extended once by another of equal or shorter length. Missing the extended term brings recargos and a collection document | Res 08-SGF/2026 paras 80 to 83, on written request to the Director de Recaudación with the listed documents. An instructivo, not a reglamento |
| Nota de Cargo administrative charge | 5% of unpaid cuotas, at most Q3,000, on top of recargos and interest. Employer alone | 1421 Art 22; Res 08-SGF/2026 paras 54, 67. Legacy 'aviso de cobro' corrected |
| Reconocimiento de deuda | Up to 60 months in level instalments, interest at the Banguat weighted average active rate, not where a judgment has been issued. Default on 2 instalments sends the case to court within 15 working days. Current cuotas continue | 1421 Arts 31, 33, 34. Art 31 f) says 2 of the agreed instalments; Res 08-SGF/2026 para 70 and Res 91-SGF/2026 say 2 consecutive: confirm with IGSS. IRTRA, INTECAP and their recargos are paid with the first instalment. An employer who does not pay them voluntarily tells those bodies in writing and gives IGSS the stamped copies before signing: Res 08-SGF/2026 para 76 |
| Late registration or payment after registration | Recargos, interest and a Q500 multa | Acuerdo 1529 Art 34. This fine is for that Acuerdo's duties only |
| Late data update | Q500 | Acuerdo 1529 Art 32 |
| Breach of the IVS reglamento | Q500 to Q1,000. Q10,000 for fraudulently seeking a benefit. Doubled on repeat | Acuerdo 1124 Arts 57 to 61. Reaches only that reglamento |
| Breach of the Enfermedad y Maternidad reglamento | Q20 to Q500, by article. Doubled on repeat | Acuerdo 410 Arts 64 to 69. Reaches only that reglamento |
| Breach of the Accidentes reglamento | Q100 to Q500 for the listed articles. Doubled on repeat | Acuerdo 1002 Art 50. Reaches only those articles |
| Eventual agricultural workers | Q500 for each breach of that reglamento | Acuerdo 1292 Art 9 |
| Ley Orgánica ordinary penalty | Q1 to Q500 by gravity | Decreto 295, OCR damaged at this point; confirm the article before citing |
| INTECAP failure to pay | A labour and social welfare fault, with economic-coactive collection and a reglamento on multas and recargos | Decreto 17-72 Art 32. That reglamento was not read, so its amounts are held |
| Exoneration of recargos | 100% from 25 March to 24 September 2026, by cash or reconocimiento up to 60 months, not where a final judgment exists | Acuerdo 1556 text not obtained: IGSS's site serves a different acuerdo at that link. Read in the IGSS comunicado, leaflet and Res 67-SGF/2026, and that window has closed. Res 67 point 23 leaves IRTRA and INTECAP to their own terms. Legacy's repealed 50% benefit is confirmed in the IGSS 2018 notice |
| ISR omission | unverified: 100% of tax omitted, less 50% if paid before a SAT requirement | Código Tributario Art 89, not read |
| ISR mora | unverified: tax x 0.005 x days late | Código Tributario Art 92, not read |

Certifications by IGSS are enforceable through economic-coactive collection under Decreto 295. A collection file begun under Acuerdo 1087 keeps intereses resarcitorios (Res 08-SGF/2026 para 56). Do not compute a penalty without escalating to a licensed Guatemalan accountant.

## Cross-border points

The Migrante Guatemalteco route (Acuerdo 1543) lets a Guatemalan abroad contribute voluntarily: a pension at 60 with 240 contributions (Art 5), health cover for family in Guatemala, being a spouse or partner and children under 7 (Arts 4, 6), to age 15 for congenital conditions (Art 8), on 4 contributions in the last 6 months (Art 7). A resident can pay on the migrant's behalf (Art 12), and prior contributions link in (Art 15).

No social security treaty, posted worker rule or foreign employer rule was read. Needs Input: do not assume cover or exemption either way. The definitions read do not turn on nationality.

## Two worked examples that recompute

Each block below was recomputed separately in exact decimal arithmetic. All examples assume a private employer and a worker in all 3 programmes, except where stated. Figures are estimates for a reviewer. Slot 12 of the workflow base maps to Example 1 (within limits), Example 2 (below the floor), Example 3 (high salary, conditional on no ceiling) and Example 4 (self-employed). Example 6 shows the floor for a worker not obliged to IVS.

### Example 1: employee within limits

A for-profit commerce company in the Department of Guatemala pays a worker for all of March 2026: salary Q6,000.00, overtime Q800.00 and a Q250.00 bonus that the employer can justify under Decreto 78-89. Salario total is Q6,800.00, which is above the monto base.

```oa-check
name: Salario total with overtime, bonus outside the base
inputs:
  salary: 6000
  overtime: 800
  bonus_if_salary: 250
  worker_rate: 0.0483
  employer_rate: 0.1067
  intecap_max: 0.01
  irtra_unverified: 0.01
steps:
  - base: salary + overtime
  - laboral: round(base * worker_rate, 2)
  - patronal: round(base * employer_rate, 2)
  - igss_total: laboral + patronal
  - intecap_at_max: round(base * intecap_max, 2)
  - irtra_held: round(base * irtra_unverified, 2)
  - base_if_salary: base + bonus_if_salary
  - total_if_salary: round(base_if_salary * (worker_rate + employer_rate), 2)
expected:
  base: 6800
  laboral: 328.44
  patronal: 725.56
  igss_total: 1054.00
  intecap_at_max: 68.00
  irtra_held: 68.00
  total_if_salary: 1092.75
```

The worker bears Q328.44 and the employer Q725.56, so the confirmed IGSS amount is Q1,054.00, due by 20 April 2026 under Art 9. INTECAP at its Q68.00 maximum and the unverified Q68.00 for IRTRA stay outside that total, and the employer alone bears them. If the bonus fails the condition under 'The base', or a reviewer does not accept the 2018 notice as its basis, it is salary and IGSS becomes Q1,092.75.

### Example 2: below the floor

A worker in a non-agricultural activity is paid a salario total of Q3,500.00 for a full month. Art 5 uses the monto base because Q3,500.00 is below it. The same arithmetic results under Acuerdo 1522 for a registered part-time worker. The employer's premises are outside the Department of Guatemala and it is unclear which minimum wage figure IGSS applies, so both are shown.

```oa-check
name: Contribución mínima on 2 candidate minimum wages
inputs:
  pay: 3500
  floor_c1: 4002.28
  floor_c2: 3816.90
  total_rate: 0.155
  worker_rate: 0.0483
  employer_rate: 0.1067
steps:
  - laboral: round(pay * worker_rate, 2)
  - total_c1: round(floor_c1 * total_rate, 2)
  - employer_c1: max(total_c1 - laboral, 0)
  - total_c2: round(floor_c2 * total_rate, 2)
  - employer_c2: max(total_c2 - laboral, 0)
  - ordinary_patronal: round(pay * employer_rate, 2)
  - top_up_c1: employer_c1 - ordinary_patronal
  - top_up_c2: employer_c2 - ordinary_patronal
expected:
  laboral: 169.05
  total_c1: 620.35
  employer_c1: 451.30
  total_c2: 591.62
  employer_c2: 422.57
  top_up_c1: 77.85
  top_up_c2: 49.12
```

The worker pays Q169.05 either way. The employer pays Q451.30 on the Q4,002.28 figure or Q422.57 on the Q3,816.90 figure. Which applies is Needs Input, since Art 5 follows the economic activity and is independent of circunscripción, whilst the minimum wage has 2 circunscripciones. Ask IGSS or read the planilla validation. Do not choose.

### Example 3: high salary, if no ceiling applies

A manager has a salario total of Q60,000.00 for a month. No ceiling was found in the texts read, and Art 4 uses salario total, so the figures below run on the whole amount only if no ceiling applies. That is Needs Input: confirm with IGSS. The Q9,000 limit bears on benefits only.

```oa-check
name: High salary if no ceiling applies, contribution base against benefit limit
inputs:
  pay: 60000
  worker_rate: 0.0483
  employer_rate: 0.1067
  benefit_limit: 9000
  pension_share: 0.80
steps:
  - laboral: round(pay * worker_rate, 2)
  - patronal: round(pay * employer_rate, 2)
  - igss_total: laboral + patronal
  - remuneration_base_max: min(pay, benefit_limit)
  - pension_max: remuneration_base_max * pension_share
expected:
  laboral: 2898.00
  patronal: 6402.00
  igss_total: 9300.00
  remuneration_base_max: 9000
  pension_max: 7200
```

If no ceiling applies, IGSS comes to Q9,300.00 for the month. The pension cannot exceed Q7,200.00 a month however high the salary: R-GT-3 applies to any projection below that limit.

### Example 4: decision, self-employed after employment

Worker A left employment on 30 June 2026 with 18 months of contributions in the last 36 and last full-month salary of Q8,000.00, and now freelances. Worker B is 40, lives in Guatemala and has 9 months. Neither has an employer, so 4.83% and 10.67% do not apply to their freelance income. The test is Acuerdo 1124 Art 35.

```oa-check
name: Contribuyente Voluntario gate and monthly cost
inputs:
  months_a: 18
  months_b: 9
  salary: 8000
  employer_share: 0.0367
  worker_share: 0.0183
steps:
  - gate_a: min(max(months_a - 11, 0), 1)
  - gate_b: min(max(months_b - 11, 0), 1)
  - rate: employer_share + worker_share
  - monthly_a: round(gate_a * salary * rate, 2)
  - monthly_b: round(gate_b * salary * rate, 2)
  - yearly_a: monthly_a * 12
expected:
  gate_a: 1
  gate_b: 0
  monthly_a: 440.00
  monthly_b: 0
  yearly_a: 5280.00
```

A meets the 12-month test and, once accepted, pays Q440.00 a month, Q5,280.00 for 12 months, for IVS only, with no medical cover, on the salary of the last obligatory month whatever the freelance income. A loses the option after 3 unpaid months in a row. Timing is the open limb: Art 35 a) says the calendar year following the last contributed month, whilst IGSS's notice adds 'un mes después de haber terminado la relación laboral'. A should confirm the date with IGSS before relying on 2027. B fails the 12-month test, so this route is closed. Cuotas Faltantes needs age 60 and Migrante Guatemalteco a Guatemalan migrant abroad, so neither fits and R-GT-6 applies.

### Example 5: Nota de Cargo charge

Two employers receive a Nota de Cargo, one for unpaid cuotas of Q10,000.00 and one for Q80,000.00. The rate for recargos is held, so only the Art 22 charge and the Art 38 cap can be computed.

```oa-check
name: Administrative charge and recargo cap
inputs:
  cuotas_a: 10000
  cuotas_b: 80000
  charge_rate: 0.05
  charge_cap: 3000
steps:
  - charge_a: min(cuotas_a * charge_rate, charge_cap)
  - charge_b: min(cuotas_b * charge_rate, charge_cap)
  - known_a: cuotas_a + charge_a
  - known_b: cuotas_b + charge_b
  - recargo_cap_a: cuotas_a
  - recargo_cap_b: cuotas_b
expected:
  charge_a: 500
  charge_b: 3000
  known_a: 10500
  known_b: 83000
  recargo_cap_a: 10000
  recargo_cap_b: 80000
```

The amounts before recargos and interest are Q10,500.00 and Q83,000.00. Recargos come on top, up to Q10,000.00 and Q80,000.00. They are not quantified: R-GT-2 applies.

### Example 6: below the floor, worker not obliged to IVS

A worker in a non-agricultural activity, with evidence of not being obliged to IVS, is paid a salario total of Q3,500.00 for a full month. Art 5 applies 'los porcentajes fijados por la normativa institucional vigente' to the monto base, so this example uses 10.00% and the worker's 3.00%, not 15.50% and 4.83%. Both candidate minimum wages are shown, as in Example 2. This is a full-time worker: Acuerdo 1522 gives no variant outside IVS.

```oa-check
name: Contribución mínima outside IVS on 2 candidate minimum wages
inputs:
  pay: 3500
  floor_c1: 4002.28
  floor_c2: 3816.90
  total_rate: 0.10
  worker_rate: 0.03
  employer_rate: 0.07
steps:
  - laboral: round(pay * worker_rate, 2)
  - total_c1: round(floor_c1 * total_rate, 2)
  - employer_c1: max(total_c1 - laboral, 0)
  - total_c2: round(floor_c2 * total_rate, 2)
  - employer_c2: max(total_c2 - laboral, 0)
  - ordinary_patronal: round(pay * employer_rate, 2)
  - top_up_c1: employer_c1 - ordinary_patronal
  - top_up_c2: employer_c2 - ordinary_patronal
expected:
  laboral: 105.00
  total_c1: 400.23
  employer_c1: 295.23
  total_c2: 381.69
  employer_c2: 276.69
  ordinary_patronal: 245.00
  top_up_c1: 50.23
  top_up_c2: 31.69
```

The worker pays Q105.00 either way. The employer pays Q295.23 on the Q4,002.28 figure or Q276.69 on the Q3,816.90 figure, which is the ordinary Q245.00 plus a top-up of Q50.23 or Q31.69. IGSS's published minimums use 15.50% only, so the 10.00% floor is this draft's reading of Art 5: confirm it with IGSS. Which minimum wage applies stays Needs Input, as in Example 2.

## Ask the client first

1. Who are you in this: an employer, a worker, a former worker, self-employed, a domestic worker or employer, or a Guatemalan abroad? If an employer: how many workers, what is your IGSS patronal number, and when did you register, under which resolution?
2. For each worker: activity, department, contract type (permanent, temporary, registered part-time, agricultural eventual), start and end dates, any IGSS suspension, and whether the worker is outside IVS, with the evidence.
3. For each pay period: pay date and every component by name: ordinary pay, overtime, commissions, each bonus with the law relied on, Bono 14, aguinaldo, pay in kind, termination payments and any subsidy complement.
4. For the employer: legal form, whether it pursues profit, whether it is a company under the Código de Comercio, its activity, any permanent agricultural worker count, and any INTECAP convenio.
5. What has been filed and paid: planillas, receipts, any Nota de Cargo, reconocimiento de deuda or exoneration request, and which months are open?
6. For a self-employed or former worker: months contributed, last month of obligatory contribution and its salary, last subsidy day, and age. Is ISR also needed? If so it goes to `guatemala-payroll`.

Also useful, not required: bank statements, prior constancia de retención and the IGSS account statement.

Reviewer questions: which minimum wage figure IGSS applies under Art 5, Example 2; whether IGSS computes the floor at 10.00% for a worker outside IVS, Example 6; whether any ceiling applies to cuotas, Example 3; whether the bonificación incentivo is outside salario total, as that rests on the 2018 notice alone; Bono 14 in or out; the character of any bonus above the legal amount; INTECAP at 1.00% for this employer; and the IRTRA rate and base from its law.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Decreto 295, Ley Orgánica del IGSS, with Decreto 11-04, IGSS copy, OCR. Read in part: Arts 27, 39, 40, 50 to 54, 72 and the financial rules; OCR damaged in places | https://www.igssgt.org/wp-content/uploads/2026/09/Decreto-No-295-y-sus-reformas-Decreto-No-11-04-Ley-Organica-del-IGSS-Guatemala.pdf | 2026-11-05 |
| Acuerdo 1421, Reglamento sobre Recaudación, OCR. Read in full | https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo_No_1421_2018.pdf | 2026-11-05 |
| AG 239-2022 and Acuerdo 1520, OCR, read in full, Arts 1 to 4 of Acuerdo 1520 checked on the page image. Art 3 concerns confidentiality, not deadlines | https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-Gubernativo-239-2022-y-Acuerdo-1520-de-Junta-Directiva-IGSS.pdf | 2026-11-05 |
| Gerencia 31/2022, proportional floor, OCR, read in full | https://www.igssgt.org/wp-content/uploads/2026/09/1-acuerdo-31-2022-gerencia-IGSS.pdf | 2026-11-05 |
| Res 08-SGF/2026, instructivo to Acuerdo 1421, OCR. Read in part: paras 1, 3 to 6, 10, 13, 18, 22, 51 to 56, 67, 70, 76, 78 to 83, 93 | https://www.igssgt.org/wp-content/uploads/2026/10/Resolucion-08-SGF-2026-de-la-Subgerencia-Financiera-IGSS_compressed.pdf | 2026-11-05 |
| AG 9-2023 and Acuerdo 1529, Reglamento de Inscripción, OCR, read in full | https://www.igssgt.org/wp-content/uploads/2026/09/Informacion.pdf | 2026-11-05 |
| Gerencia 06/2023, OCR, read in full | https://www.igssgt.org/wp-content/uploads/2026/09/1-acuerdo-06-2023-gerencia-IGSS.pdf | 2026-11-05 |
| Acuerdo 410, Enfermedad y Maternidad, rev 2018. Read in part: Arts 62 to 69, 79, 83, 85, footnotes 21 and 23 | https://www.igssgt.org/wp-content/uploads/2026/10/Acuerdo-410-Junta-Directiva-IGSS-1967-rev-2018.pdf | 2026-11-05 |
| Acuerdo 1002, Accidentes. Read in part: opening articles, Arts 46, 50, 63; Art 46 c) on the page image, as the text layer garbles it | https://www.igssgt.org/wp-content/uploads/2026/10/Acuerdo-No-1002-de-Junta-Directiva-IGSS.pdf | 2026-11-05 |
| Acuerdo 1097, read in full for amendments to 410 and 1002 | https://www.igssgt.org/wp-content/uploads/2026/10/Acuerdo-No-1097-de-Junta-Directiva-IGSS.pdf | 2026-11-05 |
| Acuerdo 1157, read in full for amendments to 1002 | https://www.igssgt.org/wp-content/uploads/2026/10/Acuerdo-No-1157-de-Junta-Directiva-IGSS.pdf | 2026-11-05 |
| Acuerdo 1023, read in full for amendments | https://www.igssgt.org/wp-content/uploads/2026/10/Acuerdo-No-1023-de-Junta-Directiva-IGSS.pdf | 2026-11-05 |
| Acuerdo 1031, read in full for amendments | https://www.igssgt.org/wp-content/uploads/2026/10/Acuerdo-No-1031-de-Junta-Directiva-IGSS.pdf | 2026-11-05 |
| Acuerdo 1243, extension to Santa Rosa, El Progreso and Petén, OCR. Read in part: Art 5 and the territory clause | https://www.igssgt.org/wp-content/uploads/2026/10/acdo1243_2010ger.pdf | 2026-11-05 |
| Acuerdo 1124, IVS, rev 2021. Read in part: definitions, Arts 3, 9, 15, 16, 29 to 31, 35 to 40, 56 to 62 | https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-1124-Junta-Directiva-IGSS-Rev-2021.pdf | 2026-11-05 |
| Acuerdo 1118, repealed. Read in part: Art 4 and its footnote on the Court ruling | https://www.igssgt.org/wp-content/uploads/2026/10/acuerdo1118jd.pdf | 2026-11-05 |
| AG 258-2022 and Acuerdo 1522, part-time, OCR, read in full, Art 5 and Art 6 checked on the page image; commencement clause of the AG not confirmed | https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-Gubernativo-258-2022-y-Acuerdo-1522-de-Junta-Directiva-IGSS.pdf | 2026-11-05 |
| Res 876-SGF/2023, part-time planilla rules, OCR, read in full | https://www.igssgt.org/wp-content/uploads/2026/09/Resolucion-876-SGF-2023-Subgerencia-Financiera-IGSS.pdf | 2026-11-05 |
| Acuerdo 1292, eventual agricultural workers, OCR, read in full | https://www.igssgt.org/wp-content/uploads/2026/10/acdo_1292jd_2012.pdf | 2026-11-05 |
| AG 257-2022 and Acuerdo 1521, Cuotas Faltantes, OCR, read in full | https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-Gubernativo-257-2022-y-Acuerdo-1521-de-Junta-Directiva-IGSS.pdf | 2026-11-05 |
| AG 215-2023 and Acuerdo 1543, Migrante Guatemalteco, OCR, read in full | https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-Gubernativo-No-215-2023-y-Acuerdo-No-1543-de-Junta-Directiva-del-IGSS.pdf | 2026-11-05 |
| AG 200-2019 and Acuerdo 1429, closed window, OCR, read in full | https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-1429-de-Junta-Directiva-IGSS-y-Acuerdo-Gubernativo-200-2019.pdf | 2026-11-05 |
| Res 67-SGF/2026, exoneration instructions, OCR, read in full | https://www.igssgt.org/wp-content/uploads/2026/09/Resolucion-67-SGF-2026-de-la-Subgerencia-Financiera-IGSS.pdf | 2026-11-05 |
| IGSS comunicado on Acuerdo 1556, read in full. Administrative | https://www.igssgt.org/noticias/2026/02/24/comunicado-igss-implementara-100-de-exoneracion-de-recargos-segun-acuerdo-1556-de-junta-directiva/ | 2026-11-05 |
| IGSS link labelled AG 17-2026 and Acuerdo 1556, read in part: enough to identify it, as it serves Acuerdo 1564, a budget acuerdo, so nothing rests on it | https://www.igssgt.org/wp-content/uploads/2026/09/Acuerdo-No-1564-de-Junta-Directiva-IGSS-1.pdf | 2026-11-05 |
| IGSS exoneration leaflet 2026, read in full. Administrative | https://www.igssgt.org/wp-content/uploads/sites/2/2026/03/Trifoliar-imprimible-Exoneracion-IGSS-2026.pdf | 2026-11-05 |
| IGSS notice on the contribución mínima, 3 October 2022, read in full. Administrative | https://www.igssgt.org/noticias/2022/10/03/el-igss-fija-cuota-minima-de-contribuciones-a-la-seguridad-social/ | 2026-11-05 |
| IGSS notice on the Reglamento, 23 November 2018, read in full. Administrative | https://www.igssgt.org/noticias/2018/11/23/igss-este-es-el-nuevo-reglamento-sobre-recaudacion-de-contribuciones-al-regimen-de-seguridad-social/ | 2026-11-05 |
| IGSS notice on Contribuyente Voluntario, 2 March 2026, read in full. Administrative | https://www.igssgt.org/noticias/2026/03/02/como-ser-contribuyente-voluntario-en-el-igss-respondemos-las-dudas-mas-frecuentes/ | 2026-11-05 |
| IGSS Contribuyente Voluntario page, read in full. Administrative | https://www.igssgt.org/afiliados/contribuyente-voluntario/ | 2026-11-05 |
| IGSS acuerdos index, read in full to find instruments and amendments | https://www.igssgt.org/acuerdos-y-resoluciones/ | 2026-11-05 |
| IGSS planilla page, read in full for the portal, form DRPT-53 and steps | https://www.igssgt.org/servicios-electronicos/planilla-electronica/ | 2026-11-05 |
| IGSS 2026 payment calendar page, read in part: page only; its PDF tables not read | https://www.igssgt.org/patronos/calendario-de-pagos-2026/ | 2026-11-05 |
| IGSS PRECAPI leaflet, rev 2026, read in full. Administrative | https://www.igssgt.org/wp-content/uploads/2026/08/Trifoliar-Programa-PRECAPI-IGSS-rev-2026.pdf | 2026-11-05 |
| IGSS PRECAPI page, read in full. Administrative | https://www.igssgt.org/programa-especial-de-proteccion-para-trabajadoras-de-casa-particular/ | 2026-11-05 |
| IGSS migrant page, read in full. Administrative | https://www.igssgt.org/trabajador-migrante-guatemalteco/ | 2026-11-05 |
| Decreto 17-72, Ley Orgánica de INTECAP, INTECAP copy annotated with Decreto-Ley 7-83. Read in part: Arts 28 to 33, 38 | https://www.intecap.edu.gt/informacionpublica/pdf/Ley%20Organica%20INTECAP.pdf | 2026-11-05 |
| Decreto 42-92, Bono 14, ONSEC compendium copy on the Ministerio de Cultura site, read in full; later amendments not checked | https://mcd.gob.gt/wp-content/uploads/2013/07/bono-14-decreto-42-92.pdf | 2026-11-05 |
| Diario de Centro América, minimum wages 2026, news item on AG 256-2025, read in full; the AG itself not read | https://dca.gob.gt/noticias-guatemala-diario-centro-america/gobierno-fija-nuevos-salarios-minimos-para-2026/ | 2026-11-05 |
| Diario de Centro América, 18 May 2026, news item on Decreto 13-2026, read in full; the decree itself not read | https://dca.gob.gt/noticias-guatemala-diario-centro-america/oficializan-que-salario-minimo-esta-exento-de-isr/ | 2026-11-05 |
| Diario de Centro América, opinion column of 19 May 2026 on planillas, read in full. Commentary, not law | https://dca.gob.gt/noticias-guatemala-diario-centro-america/ajustes-para-planillas-y-retenciones/ | 2026-11-05 |
| Acuerdo 1154, OCR, read in full: amends Arts 6, 7, 23 and 24 of Acuerdo 410 and adds Art 84 Bis, with no rate | https://www.igssgt.org/wp-content/uploads/2026/10/Acuerdo_No_1154m.pdf | 2026-11-05 |
| Res 91-SGF/2026, Cobro Administrativo manual, an internal manual, OCR. Read in part: Procedimientos 3, 4 and 11 and a keyword search for rates and charges, which found no recargo rate; low OCR confidence on pages 3, 10, 43, 45 and 63, and page 71 rotated | https://www.igssgt.org/wp-content/uploads/2026/09/Resolucion-91-SGF-2026-de-la-Subgerencia-Financiera-IGSS.pdf | 2026-11-05 |
| Res 358-SGF/2025, Inspección Patronal manual, OCR. Read in part: keyword search for rates, charges, bonuses and deadlines, which found none relied on here | https://www.igssgt.org/wp-content/uploads/2026/09/Resolucion-358-SGF-2025-de-la-Subgerencia-Financiera-IGSS.pdf | 2026-11-05 |
| IGSS guide, Departamento de Registro de Patronos y Trabajadores, undated, OCR. Read in part: welcome letter, rates page, seguros facultativos, Acuerdo 522, inscription requirements; the portal walkthrough pages are garbled. Administrative | https://www.igssgt.org/wp-content/uploads/2026/09/Departamento-de-REGISTRO-DE-PATRONOS-Y-TRABAJADORES-IGSS.pdf | 2026-11-05 |
| IGSS guide, Departamento de Cobro Administrativo, undated, OCR. Read in part: each section's requirements and notes. Administrative | https://www.igssgt.org/wp-content/uploads/2026/09/Departamento-de-COBRO-ADMINISTRATIVO-IGSS.pdf | 2026-11-05 |
| IGSS guide, Dirección de Recaudación, undated, OCR, read in full; nothing relied on | https://www.igssgt.org/wp-content/uploads/2026/09/Direccion-de-RECAUDACION-IGSS.pdf | 2026-11-05 |
| IGSS home page, read in part: keyword search; nothing relied on | https://www.igssgt.org/ | 2026-11-05 |
| IGSS patronos page, read in part: keyword search; nothing relied on | https://www.igssgt.org/patronos/ | 2026-11-05 |
| IGSS requisitos de inscripción page, read in part: keyword search; nothing relied on | https://www.igssgt.org/patronos/requisitos-de-inscripcion/ | 2026-11-05 |
| IGSS información pública page, read in part: keyword search; nothing relied on | https://www.igssgt.org/informacion-publica/ | 2026-11-05 |
| IGSS preguntas frecuentes page, read in part: keyword search; nothing relied on | https://www.igssgt.org/preguntas-frecuentes/ | 2026-11-05 |
| IGSS preguntas frecuentes for patronos, read in part: keyword search; nothing relied on | https://www.igssgt.org/preguntas-frecuentes/patronos/ | 2026-11-05 |

Not yet confirmed: the text of the IRTRA law (Decreto 1528, Decreto 43-92, Decreto 9-2024), its rate and its base, for which the 1% is a digest of iniciativa 6314; the Junta Directiva acta that took INTECAP to its 1.00% maximum, and INTECAP's reglamento on multas and recargos; Decretos 78-89, 7-2000 and 37-2001, the Q250 figure, whether an amount above it is excluded, and the Corte de Constitucionalidad ruling of 8 October 2003 and its effect, as the exclusion rests on the 2018 notice alone; Bono 14 in the base; who is 'no afecto' to IVS beyond Acuerdo 1124 Art 31, as no text read gives a general list; whether IGSS computes the floor at 10.00% for a worker outside IVS, and how Acuerdo 1522 treats a part-time worker outside IVS; any ceiling on cuotas, as no text read sets one; the terms of a seguro facultativo simple; Acuerdo 522 itself; the extension acuerdos 475, 616, 621, 849, 1024, 1095 and 1121, and whether every department is covered; the State's Enfermedad y Maternidad share outside the Department of Guatemala, including the budget proportion under Acuerdo 1243 Art 5 c); AG 256-2025 itself, whether it fixes the wage by day or month (Q131.58 x 30.4167 = Q4,002.23 against the published Q4,002.28, and each monthly figure differs slightly), whether C1 is the Department of Guatemala, the Q3,321.10 or Q3,221.10 conflict, and which figure sets the monto base outside C1; the formula for a proportional floor; whether INTECAP and IRTRA run on the actual pay or the monto base at the floor; the floor and planilla for multiple employers; the Junta Monetaria rate; whether 2 instalments in default must be consecutive; the undated IGSS guides' 3-worker text and 30 working days for a first payment, and Acuerdo 36 de Gerencia Art 53; Res 91-SGF/2026 and Res 358-SGF/2025, read by keyword search and named procedures only, with low-confidence OCR on several pages; Acuerdo 1556 and any extension of its window, as the IGSS link serves Acuerdo 1564 instead; the 2026 period calendars; the reglamento behind PRECAPI, including Acuerdo 1235 Art 37, which its leaflet cites, and whether its figures are monthly or quarterly; commencement conflicts, where AG 239-2022 says on publication and Acuerdo 1520 Art 4 the day after, and AG 9-2023 says on publication and Acuerdo 1529 Art 39 the day after, giving 17 January 2023; AG 258-2022's commencement; Decreto 10-2012, the Código Tributario and every SAT form and deadline; Decreto 13-2026, approved on 28 April 2026 per legacy and published on 15 May 2026 per a search digest, whose remaining provisions the DCA note says apply from 1 January 2027 with a deduction of 12 monthly non-agricultural minimum wages including bonificación incentivo at the highest circunscripción figure, which `guatemala-payroll` and `guatemala-income-tax` need to reflect; any conflict with those sibling guides on the IGSS base; the request date for Contribuyente Voluntario, as Art 35 a) says the calendar year following and IGSS's notice adds 'un mes después de haber terminado la relación laboral'; return to voluntary status after an Acuerdo 1124 Art 36 lapse with no new employment; social security treaties; and Acuerdo 1432, read only as a footnote to Art 29.

## Changelog

| Version | Date | Change |
| --- | --- | --- |
| 0.3 | 2026-11-05 | Converted to the upstream template. Corrected the base to salario total, the INTECAP scope and the sources of rates; stated the Q9,000 benefit limit; added the floor, part-time, voluntary and Nota de Cargo rules; held IRTRA, ISR, the Q250 figure and Bono 14; replaced the bank fallback with intake only. After an independent check: corrected the Court footnote, so the bonificación incentivo rests on the 2018 notice alone; added the recargo day count, the late planilla cases, the seguro facultativo simple and the State's Accidentes share; read the remaining IGSS scans. After a second-opinion review: limited the 4.83% and 15.50% floor to workers in all 3 programmes and added Example 6 outside IVS; limited the State's 1% to the Department of Guatemala; split bare SAT from ISR; added the one-off extension for a late planilla; made Example 3 conditional on no ceiling; narrowed the image check statement to its 3 passages and matched Sources to the read log; confined the 9-month return rule to Art 37. |
| 0.2 | 2026-11-01 | Legacy version. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador público, perito contador, or equivalent licensed practitioner in Guatemala) before filing or acting upon.
