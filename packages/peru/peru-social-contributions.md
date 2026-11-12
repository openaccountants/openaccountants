---
name: peru-social-contributions
description: >
  Compute ordinary Peruvian employer health contributions and employee pension
  deductions for 2026, distinguishing EsSalud, ONP and each AFP commission regime.
  Use for EsSalud minimum bases, EPS credits, AFP insurance ceilings, ONP versus
  AFP, PLAME Form 0601, T-Registro, payroll bank reconciliation, CTS and
  gratificaciones. Covers the October minimum-wage change, November SBS snapshot,
  fifth-category withholding interface, employer versus employee costs, independent
  pension contributions and documentary exceptions. Produces a source-linked
  working paper and a reconciliation to filings and payments. Ask for the service
  period, pension affiliation, remuneration components and supporting records before
  calculating. Foreign assignments, special labour regimes and missing period-specific
  insurance rates require a separate documented assessment.
version: 0.2
jurisdiction: PE
tax_year: 2026
last_updated: 2026-11-11
checked_on: 2026-11-11
depends_on:
  - social-contributions-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: computation
---

# Peru social contributions and payroll reconciliation v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Use this skill for ordinary private-sector employment in Peru during 2026: compute employer EsSalud, employee ONP or AFP deductions, and reconcile the working paper to PLAME, AFP remittances and bank payments. It also covers the common independent pension-contribution route and the interface with fifth-category income tax, CTS and statutory gratificaciones. Load `social-contributions-workflow-base` for the output workflow. Tax domicile, pension membership and labour-benefit eligibility are separate decisions.

**Quick reference:** EsSalud is an employer cost. Ordinary ONP or AFP deductions are withheld from the employee. ONP and AFP are alternative affiliations for the period, not two deductions to stack. An AFP salary percentage is not enough: identify the administrator, commission arrangement, insurance eligibility and the SBS schedule for the actual month. Benefits and fifth-category tax use different bases from pension contributions. Sources: Law 26790 arts. 6, 15-16; ONP regulation arts. 19, 22-25; SBS contribution guidance and Title V art. 87, listed below.

**Required inputs before any calculation:** service/payroll month; days worked, subsidised and unpaid; ordinary and variable remuneration; statutory bonuses and other non-remunerative payments; ONP or AFP affiliation and effective changes; AFP commission arrangement; retirement or insurance-exemption evidence; EPS-covered workers and payments; employee tax domicile and year-to-date income/withholding; employer RUC and filing status. If any input changes the result and is missing, ask for it. Do not assume resident status, choose the highest AFP rate or infer every worker's affiliation from one bank debit.

**Scope boundaries:** this is the ordinary employment method. Agricultural, construction, domestic-worker, fishing, artistic, public-sector, MYPE-specific labour benefits and high-risk SCTR cases need their applicable regime before using an ordinary base or benefit formula. Law 26790 art. 19 separately requires employer-financed SCTR for qualifying high-risk work. Do not present ordinary EsSalud as the employer's entire insurance or labour-cost budget. Pensioner health deductions are also distinct from employer health contributions on wages. Pension transfers, withdrawals and entitlement calculations are outside this job.

For an independent person, do not invent an employer or automatically impose employee payroll contributions on professional fees. The voluntary SNP/SPP routes below depend on affiliation and the current implementation rules. A worker labelled a contractor may still have an employment relationship; resolve the underlying facts before selecting a route.

## Rates, bands and thresholds

Amounts are PEN. Each percentage is conditional on the population and period in its row. All sources were read on 2026-11-11 in the portions recorded in Sources.

| Item | Amount and conditions | Official source and short original wording |
|---|---|---|
| UIT, 2026 | 5,500; indexing unit for the 2026 income-tax bands and EPS limit | [SUNAT UIT table, DS 301-2025-EF](https://www.sunat.gob.pe/indicestasas/uit.html): `2026` / `5,500` |
| Historical UIT, 2025 | 5,350, only for a 2025 computation; historical 7 UIT = 37,450 | [SUNAT UIT table, DS 260-2024-EF](https://www.sunat.gob.pe/indicestasas/uit.html): `2025` / `5,350` |
| RMV, January to September 2026 | 1,130 monthly ordinary minimum; do not use it for October onward | [DS 015-2026-TR art. 1](https://busquedas.elperuano.pe/dispositivo/EX/2559163-1): `de S/ 1,130.00` |
| RMV, from 1 October 2026 | 1,230; the further tranche requires a 2027 decree, not automatic application in 2026 | [DS 015-2026-TR art. 1.2](https://busquedas.elperuano.pe/dispositivo/EX/2559163-1): `a partir del 1 de octubre de 2026` |
| Ordinary EsSalud | Employer 9% of contributory remuneration, no upper cap; ordinary minimum base is the RMV applicable at month end, subject to unpaid-month and subsidy rules below | [Law 26790 art. 6](https://www.essalud.gob.pe/transparencia/pdf/publicacion/ley26790.pdf): `equivale al 9%`; [SUNAT report 003-2007](https://www.sunat.gob.pe/legislacion/oficios/2007/oficios/i0032007.htm) reads the amendments |
| Ordinary ONP/SNP | Employee 13% of monthly insurable remuneration, uncapped; minimum and proportional-work conditions below | [ONP regulation arts. 22.3, 23-24](https://repocdn.onp.gob.pe/Normativa/Base_normativa/NPT046.pdf): `trece por ciento (13%) de la remuneración asegurable` |
| AFP mandatory savings | Employee 10% of contributory gross monthly remuneration, no insurance ceiling on this component; retirement exceptions below | [SBS November 2026 schedule](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx): `APORTE OBLIGATORIO AL FONDO DE PENSIONES` / `10,00%` |
| AFP insurance, November 2026 snapshot | 1.37% on the lesser of contributory remuneration and RMA 12,732.70 for an insured member; do not carry this snapshot into another month without that month's schedule | [SBS devengue 2026-11 and note 3](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx): `Al mes de devengue 2026-11` / `1,37%` / `12 732,70` |
| Habitat, November 2026 | Salary-flow commission 1.47%, or annual balance commission 1.25%, according to the member's arrangement; ordinary below-RMA flow total 12.84% | [SBS schedule, HABITAT row](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx): `1,47% 1,25% 1,37% 10,00%` |
| Integra, November 2026 | Salary-flow commission 1.55%, or annual balance commission 0.78%; ordinary below-RMA flow total 12.92% | [SBS schedule, INTEGRA row](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx): `1,55% 0,78% 1,37% 10,00%` |
| Prima, November 2026 | Salary-flow commission 1.60%, or annual balance commission 1.25%; ordinary below-RMA flow total 12.97% | [SBS schedule, PRIMA row](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx): `1,60% 1,25% 1,37% 10,00%` |
| Profuturo, November 2026 | Salary-flow commission 1.69%, or annual balance commission 0.68%; ordinary below-RMA flow total 13.06% | [SBS schedule, PROFUTURO row](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx): `1,69% 0,68% 1,37% 10,00%` |
| Mixed/balance arrangement | Salary-flow component zero since February 2023. For an ordinary insured member below RMA in the November snapshot, salary deduction is 10% + 1.37% = 11.37%; annual balance charge is not another salary deduction | [SBS schedule, closing note](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx): `el componente de flujo de la Comisión Mixta es 0%` |
| EPS health credit | Least of 25% of qualifying covered-worker EsSalud, eligible amounts actually paid for that month's EPS cover, and 10% of UIT times covered workers; 2026 indexed cap 550 per covered worker | [Law 26790 arts. 15-16](https://www.essalud.gob.pe/transparencia/pdf/publicacion/ley26790.pdf): `sin exceder de los`; [SUNAT report 088-2004, analysis 4.4](https://www.sunat.gob.pe/legislacion/oficios/2004/oficios/i0882004.htm) |
| Resident employment fixed deduction | 7 UIT = 38,500 for 2026, once against combined fourth/fifth-category work income; not a deduction per employer | [LIR art. 46](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf): `monto fijo equivalente a siete (7)` |
| Additional annual expense deduction | Up to 3 UIT = 16,500 for qualifying documented expenses; never subtract it in employer fifth-category withholding | [LIR art. 46](https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf): `no podrán exceder en conjunto de tres (3)`; [Regulation art. 40(b)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) uses the fixed 7 UIT |
| Resident work band 1 | Taxable annual income through 5 UIT = 27,500 at 8% | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Hasta 5 UIT` / `8%` |
| Resident work band 2 | Excess over 5 through 20 UIT, 27,500 to 110,000 at 14% | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Más de 5 UIT hasta 20 UIT` / `14%` |
| Resident work band 3 | Excess over 20 through 35 UIT, 110,000 to 192,500 at 17% | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Más de 20 UIT hasta 35 UIT` / `17%` |
| Resident work band 4 | Excess over 35 through 45 UIT, 192,500 to 247,500 at 20% | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Más de 35 UIT hasta 45 UIT` / `20%` |
| Resident work band 5 | Excess over 45 UIT = 247,500 at 30% | [LIR art. 53](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Más de 45 UIT` / `30%` |
| Non-domiciled employment | Domestic-law 30% on Peruvian-source employment income, no resident 7 UIT or 3 UIT deduction; first test source, domicile and any applicable treaty | [LIR art. 54(g)](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf): `Rentas de trabajo` / `Treinta por ciento (30%)` |
| Ordinary statutory gratificaciones | July and December; complete qualifying semester gives one computable monthly remuneration, shorter service prorated under the rules below | [Law 27735 arts. 1-7, MTPE compendium pp. 329-335](https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495): `dos gratificaciones en el año` |
| Additional bonus accompanying gratificación | Ordinary EsSalud case 9% of statutory gratificación; EPS-covered case 6.75%; non-remunerative/non-pensionable, but income-tax treatment remains | [Law 30334 art. 3; DS 012-2016-TR art. 6, compendium pp. 338-346](https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495): `bonificación extraordinaria de carácter temporal no remunerativo ni pensionable` |
| Ordinary CTS | Computable remuneration times qualifying months/12 plus qualifying days/360; semestral gratificación enters the base at one sixth, subject to actual entitlement | [CTS TUO DS 001-97-TR arts. 18, 21](https://cdn.www.gob.pe/uploads/document/file/229267/TUO_Compensacion_por_Tiempo_de_Servicios_-_D.S_001-97-TR.pdf): `un sexto de lo percibido` / `treintavos` |

## The base

### 1. Establish the period and the legal relationship

Keep a separate row for each employee and payroll month. Reconcile the employment contract, boleta de pago, time records, taxable earnings and T-Registro membership dates. The October RMV change is period-sensitive: an October payroll or minimum contribution cannot use September's floor merely because the contract or software was set up earlier. The later proposed wage tranche is not a 2026 amount.

A payroll total is not automatically the base of every contribution. Identify cash and in-kind remuneration, regular variable pay, periods of subsidy or unpaid leave, statutory gratificaciones, CTS and other exclusions before calculating. ONP regulation art. 23 includes freely available remuneration unless a legal exclusion applies. Law 30334 and DS 012-2016-TR exempt the statutory gratificación and its qualifying extraordinary bonus from the ordinary social contributions, while preserving income tax and legally authorised deductions. Do not exempt a payment merely because its narration says "bono" or "aguinaldo".

### 2. Compute EsSalud and keep its minimum separate from ONP

For an ordinary remunerated month without subsidy, employer EsSalud is `9% × max(contributory remuneration, month-end RMV)`. No upper cap applies. A worker joining/leaving partway through the month, or working part-time, does not by itself permit prorating the ordinary EsSalud minimum. SUNAT report 003-2007 reads art. 6 of Law 26790 as amended by Law 28791, and regulatory art. 33 as amended by DS 020-2006-TR: `independientemente de las horas y días laborados`.

Apply the adjacent exceptions before using that formula:

- For a whole month with no remuneration because of an unpaid suspension, no ordinary wage contribution arises: SUNAT's conclusion is `no corresponde abonar el aporte a ESSALUD respecto de dicho mes`.
- A subsidy is not ordinary contributory remuneration. In a mixed remunerated/subsidised month, the minimum is proportional to the non-subsidised days under the cited regulatory rule. Keep actual contributory pay and the adjusted minimum separate; do not charge on the subsidy or force the ordinary full floor onto an entirely subsidised month.
- Special insured populations and regimes require their own base. An employer's EPS plan does not remove EsSalud registration or the gross calculation.

Working-paper order: show gross health base, gross 9% charge, qualifying EPS credit, prior-period credit where valid, and net EsSalud separately. The employee's net salary does not bear employer EsSalud.

### 3. Compute the EPS credit with all three limits

Confirm that the employer and workers meet Law 26790 arts. 15-16 and the eligible coverage conditions, including the selection of an EPS through the statutory process. Obtain covered-worker lists, cover periods, contract and actual EPS payment evidence. Calculate the credit for the covered population, not every employee merely because one has an EPS policy:

`current source-month credit = min(25% × covered workers' gross EsSalud contributions, eligible EPS payments attributable to that month, 10% × that month's UIT × number of covered workers)`.

Subtract the allowable credit from the gross EsSalud obligation. A 6.75% residual only results where the full 25% credit is available against a 9% wage contribution. It is not a universal replacement rate and the credit is not 25% of the EPS invoice. The EPS invoice can exceed the allowable credit and remains a separate cash payment.

SUNAT report 088-2004, following binding Tribunal Fiscal decisions, distinguishes late payment from loss of credit. A late EPS payment defers use to the contribution period in which it is paid, with any balance applied in the immediately following periods under the legal limits. Determine each source month's limits using its own covered workers, remuneration and UIT, rather than the payment month's population. Late filing or late payment of EsSalud alone does not extinguish a credit correctly earned. Keep a source-month/payment-month/utilisation rollforward; do not apply the same credit twice.

### 4. Compute ONP where that is the evidenced affiliation

Under ONP regulation arts. 19 and 22-25, `ONP = 13% × monthly insurable remuneration`. The contribution is employee-borne, withheld and remitted by the employer through SUNAT. The insurable remuneration has no upper cap. For an ordinary full legal or contractual work schedule the base cannot be below RMV; where the worker does not perform the full daily/weekly/monthly schedule, use accrued remuneration subject to the lawful proportional minimum. The regulation says `siempre que se mantenga la proporcionalidad`. Do not import the full EsSalud floor indiscriminately into a lawful part-time ONP calculation.

Separate an actual lawful part-time/partial-month case from an employer simply paying less than the lawful wage. Obtain the employment schedule and days before applying a reduced minimum. Changes between SNP and SPP follow the effective affiliation/disaffiliation period; the same ordinary employment remuneration is not charged to both systems. No general matching employer pension contribution is added to the ordinary ONP calculation here.

### 5. Compute AFP components rather than applying an uncapped total

For an ordinary insured member subject to mandatory contributions, using the actual month's SBS schedule:

1. Savings contribution: `10% × contributory remuneration`.
2. Insurance: `premium rate × min(contributory remuneration, that month's RMA)`.
3. Salary-flow arrangement: add `AFP flow commission × contributory remuneration`.
4. Mixed/balance arrangement: the salary-flow component is zero under the published note; record the annual fund-balance charge separately. Do not subtract that annual percentage from the salary or apply it to the entire salary each month.
5. Add only the components applicable to that member. For November 2026, below RMA and without an insurance exemption, the flow totals are 12.84%, 12.92%, 12.97% or 13.06%, and the mixed salary deduction is 11.37%. Above RMA those flat totals overstate insurance.

The 10% savings and salary-flow commission do not inherit the insurance ceiling. The old early-2026 and second-quarter RMA estimates are not established for use here; obtain the actual SBS devengue schedule before computing an earlier or later month. Retain a copy of that month's schedule in the working paper.

**Retirement conditions matter.** SBS Title V art. 87(a) allows an affiliated pensioner continuing work not to make mandatory SPP contributions after communicating and documenting pensioner status. Art. 87(b) separately excludes the insurance premium for a member who has reached retirement age and continues paid work, subject to informing the employer with identification showing date of birth. Qualifying retirement withdrawals have the documentary treatment specified in that article. These are not all the same exemption: do not automatically stop the 10% contribution merely because someone reaches retirement age, or continue insurance without checking eligibility. Request the required documents and effective date; do not infer status from a bank pension credit alone.

### 6. Independent and voluntary pension routes

ONP regulation arts. 28-31 distinguishes voluntary contribution for a person without compulsory employment contributions from extra amounts added to existing contributions. Declared voluntary insurable monthly income is at least one RMV and has no upper cap. A credited contribution month requires accumulated payments reaching 13% of that declared income; a smaller payment is not automatically a full contribution month. On a declared minimum base, the arithmetic is 146.90 for January-September and 159.90 from October 2026. The ordinary maximum payment deadline in art. 30 is the following month, with late-payment surcharge; request the applicable ONP collection record and channel. Do not report voluntary payments as employer payroll withholding.

SBS's current [Aportes guidance](https://www.sbs.gob.pe/usuarios/aprende-con-la-sbs/aportes) describes independent SPP contributions as voluntary: the member declares chosen contributory income not below RMV and makes the payment, with savings, insurance and commission components as applicable. Insurance continuity and eligibility must be checked. That guidance says it will be updated as complementary regulations to Law 32123 are approved. Do not infer a new compulsory independent-worker payment schedule or future reform commencement from the employee table. Multiple jobs do not create separate AFP individual accounts.

### 7. Fifth-category withholding interface

First establish domicile and Peruvian source under LIR arts. 6-10, 34 and 54. For an ordinary domiciled employee, Regulation art. 40 requires the following monthly projection, rather than simply annualising twelve salaries and dividing by twelve all year:

1. Multiply the current ordinary monthly remuneration by the months remaining including the current month. Add ordinary gratificaciones for the year and previous months' ordinary and other remuneration, taking care not to count a payment twice.
2. Deduct the fixed 7 UIT once. Apply the LIR art. 53 marginal bands to the non-negative projected taxable base, then applicable documented credits. Do not deduct employee ONP/AFP as if these were the statutory 7 UIT deduction.
3. Do not use the additional 3 UIT annual expense deduction in employer withholding. It is assessed through the taxpayer's annual process under LIR art. 46. Qualifying donations for a fifth-category-only worker have the specific December adjustment in Regulation art. 40(b); do not silently insert them into every monthly projection.
4. Use the period-specific allocation below. If extraordinary pay is made in the current month, Regulation art. 40(e) additionally withholds the difference between the annual tax including that additional amount and the ordinary projected annual tax. This is additional to ordinary monthly withholding, not a reason to spread the whole extra payment over twelve months.
5. For multiple fifth-category employers, Regulation art. 44(b) requires the worker to inform the highest-paying employer of other remuneration so it aggregates and withholds, and supply received copies to the others. Multiple employers alone do not create a mandatory annual-return rule. Carry forward the prior employer's income/withholding evidence when employment changes; special cessation and variable-pay methods need Regulation arts. 41-42.

| Month of ordinary withholding | Allocation under Regulation art. 40(d) | Official source |
|---|---|---|
| January-March | Projected annual tax divided by 12 | [Regulation art. 40(d)(1)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |
| April | Annual tax less January-March withholding, divided by 9 | [Regulation art. 40(d)(2)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |
| May-July | Annual tax less January-April withholding, divided by 8 | [Regulation art. 40(d)(3)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |
| August | Annual tax less January-July withholding, divided by 5 | [Regulation art. 40(d)(4)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |
| September-November | Annual tax less January-August withholding, divided by 4 | [Regulation art. 40(d)(5)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |
| December | Final annual adjustment less January-November withholding | [Regulation art. 40(d)(6)](https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf) |

Non-domiciled employment uses the domestic-law 30% rate on Peruvian-source work income without resident deductions, subject to source and treaty analysis. This tax treatment does not itself determine whether EsSalud or pension contributions apply. Never default a foreign worker to resident or exempt social contributions just because employment tax is non-resident.

### 8. CTS and gratificaciones are benefits, not interchangeable contributions

For ordinary CTS, first test the private-sector four-hour average daily service gate in CTS TUO art. 4, the worker's regime and credited time. Arts. 9-18 identify regular computable pay, the April/October reference remuneration, qualifying variable-pay averages and the one-sixth inclusion of semestral gratificación actually received. Art. 21 uses monthly twelfths and daily thirtieths of a twelfth: `CTS = base × complete months / 12 + base × remaining credited days / 360`. Do not treat an approximate annual cost percentage as the deposit formula. Obtain regular family allowance and variable-pay records rather than using basic salary alone. For complementary variable/imprecise pay, CTS TUO art. 16 requires receipts in at least three months of the six-month period, then adds the sum received divided by six to the computable base; the same regularity gate applies to a shorter liquidation period. For principal imprecise remuneration such as commissions or piecework, art. 17 uses the semester average, or the daily average over the actual period if shorter than six months. Periodic pay has the distinct art. 18 rules: semestral pay enters by sixths, longer periods by twelfths of the amount received in the semester, and periods exceeding a year are excluded; fixed pay with periods above a month but below a semester uses art. 16 incorporation without the three-month receipt gate. The extraordinary non-remunerative health-replacement bonus is not simply added as another sixth of gratificación.

For gratificaciones, Law 27735 and DS 005-2002-TR distinguish the January-June and July-December semesters; use the computable remuneration at 30 June or 30 November, respectively. Complete qualifying semesters give one computable monthly remuneration; shorter service is calculated by complete calendar months with the regulatory treatment of non-credited days. Paid vacation/leave and qualifying subsidised time have the statutory service treatment, so absence is not automatically an exclusion. For complementary variable pay, Law 27735 art. 3 requires receipt in at least three months of the semester and adds the sum divided by six. For principal variable remuneration, apply DS 005-2002-TR art. 3.1 with the CTS art. 17 average rule and the specified service period. For a shorter ordinary entitlement, calculate one sixth of the computable remuneration per complete calendar month and deduct non-credited days at one thirtieth of that monthly fraction; do not remove credited paid leave or subsidy days. Under DS 005-2002-TR art. 5, truncated gratificación requires at least one complete service month, uses the computable remuneration of the month immediately before cessation and complete calendar months in the relevant semester, and is paid with the social benefits within 48 hours of cessation. Truncated CTS instead uses cessation-date remuneration under CTS TUO art. 3 and is paid directly by the employer within 48 hours. Add the health-replacement extraordinary bonus at 9%, or 6.75% for qualifying EPS coverage, as provided by Law 30334 and DS 012-2016-TR. Do not deduct ordinary ONP/AFP/EsSalud from the exempt statutory gratificación; retain employment income tax and permitted deductions.

### 9. Reconcile the bank and produce the working paper

Bank narrations are clues, not statutory proof or a deterministic tax classifier. The following are illustrative search strings for BCP, BBVA, Interbank and Scotiabank extracts; their proprietary current vocabulary has not been independently established. Request the actual receipts and bank documentation. Direction, counterparty, payroll period and the employee/employer role decide the posting.

| Illustrative narration to investigate | Provisional route | Evidence before final posting |
|---|---|---|
| `SUNAT`, `PAGO SUNAT`, `TRIBUTOS SUNAT`, `SUNAT TRIBUTOS` | Could be many taxes, not automatically PLAME | Form number, period, tax codes and payment receipt; do not split a generic debit into EsSalud/ONP/tax by guess |
| `PLAME`, `PLANILLA ELECTRONICA`, `FORMULARIO 0601`, `FORM 0601` | Payroll declaration/payment reconciliation | PLAME debt determination and paid amounts; filing alone does not prove remittance |
| `RENTA QUINTA`, `RENTA 5TA`, `5TA CATEGORIA` | Employment tax withholding liability | Worker calculation, declaration, payment |
| `ESSALUD`, `ES SALUD` | Employer health liability | Gross charge, EPS credit and payment, not an employee salary deduction |
| `ONP`, `SNP` | Public pension withheld if an outgoing contribution | Affiliation, relevant employee bases, PLAME and receipt |
| `AFPNET`, `AFP NET`, `AFP HABITAT`, `AFP INTEGRA`, `AFP PRIMA`, `AFP PROFUTURO`, `SPP` | Private pension remittance | AFP period, worker components and paid status; ordinarily separate from the SUNAT PLAME payment |
| `APORTE OBLIGATORIO`, `COMISION AFP`, `PRIMA SEGURO` | Potential pension components | Savings/insurance/commission breakdown; insurance or commission narration alone does not prove an AFP payroll payment |
| `CTS`, `COMP TIEMPO SERVICIOS`, `CTS DEPOSITO` | Potential employer severance deposit | Named worker's CTS account, qualifying semester, deposit calculation and proof |
| `GRATIFICACION`, `GRATI`, `FIESTAS PATRIAS`, `AGUINALDO` | Potential bonus | Distinguish statutory gratificación, extraordinary bonus and any public/special-regime payment |
| Outgoing `ABONO HABERES`, `PAGO PLANILLA`, `TELECREDITO`, `PAGO DE HABERES`, `PAGO HABERES` | Net wage/payroll batch, not an additional contribution expense | Payroll net-pay control and employee bank list |
| Incoming `SUELDO`, `REMUNERACION`, `HABERES` | Wage received by the account holder | Confirm holder and employer, not a contribution paid |
| Incoming `PENSION ONP`, `PENSION SNP`, `PENSION AFP`, `RETIRO AFP`, `JUBILACION` | Pension/withdrawal received, not a payroll contribution | Pension statement or withdrawal decision; different from an outgoing remittance |

A tax, social-contribution, wage or CTS payment is not an IGV purchase invoice. Do not claim IGV input credit from the bank debit itself. The underlying invoice and substantive IGV requirements, where a separate taxable supply exists, require their own analysis; see LIR/IGV separation and [IGV Law art. 18](https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf).

If only a bank statement is supplied, list candidate transactions and missing evidence. The existence of an AFPnet payment suggests a private-pension remittance to investigate; its absence does not prove ONP affiliation or payment compliance. A client may have employees in different systems. Do not compute employee-level deductions or final contribution splits from bank labels alone.

Working-paper fields:

```text
PERU 2026 CONTRIBUTIONS AND PAYROLL RECONCILIATION
Employer/RUC; worker identity; preparation date; service and payment periods
Evidence index: contract, time records, payslip, affiliation, returns, bank receipts
Period-specific UIT/RMV; actual SBS devengue and saved schedule
Gross pay by component; contributory/non-contributory classification and source
Days/hours worked; subsidised/unpaid days; applicable labour regime
EsSalud actual base; ordinary/adjusted floor; gross 9%; EPS current/prior credit; net
ONP base/minimum adjustment and 13%, OR AFP savings/insurance/commission separately
Retirement/premium exemption evidence and effective date; no double pension charge
EPS covered population, eligible paid invoice, three caps and utilisation rollforward
Tax domicile/source; current projection; 7 UIT; bands; credits; allocation divisor
Prior employers/pay/withholding; extraordinary-payment increment; final withholding
Employee net pay = cash remuneration minus employee pension minus tax/other valid deductions
Employer costs: remuneration, EsSalud, additional insurance, benefits, separate EPS cash
CTS base/semester/months/days; gratificación base/service; health-replacement bonus
PLAME base/result/credit/balance/payment fields; AFP declaration and payment status
Return order number; tax/payment period; payment reference AND bank receipt
Reconciliation by liability: opening + accrued/withheld - payments = closing balance
Missing inputs, unconfirmed source periods and professional review items
```

Glossary retained for reading Spanish records: remuneración/haberes = wages; boleta de pago = payslip; planilla = payroll; descuentos = deductions; aporte obligatorio = mandatory pension saving; comisión = administration fee; prima de seguro = insurance premium; renta de quinta categoría = employment income tax; gratificación = statutory bonus where its legal conditions apply; CTS = severance-time benefit; RMV = minimum wage; UIT = tax indexing unit. An aguinaldo label is not conclusive evidence of the ordinary private-sector gratificación regime.

## Deadlines and filing

### Registration and T-Registro

The ordinary electronic-payroll obligation arises with one or more employees, not a wage threshold. SUNAT also lists pension payers, specified service/third-party personnel, withholding obligations and other populations. Obtain the employer's RUC/SOL access and register the employer before the worker entries. In SOL, go to **Empresas > Mi RUC y Otros Registros > T-Registro**; use employer **Alta**, then worker **Registro Individual > Nuevo**. Enter identification, employment, social-security and tax data with consistent effective dates. Save the CIR registration receipts. SUNAT's official presentation identifies worker receipts 1604-1 (alta), 1604-2 (modification) and 1604-3 (baja).

Under [SUNAT's employer-obligations table](https://orientacion.sunat.gob.pe/03-obligaciones-del-empleador-t-registro), register an employee within the day services begin, not within a rolling 24-hour period. Update changes within five business days of the event/knowledge under the stated rule; deregister by the day after the relationship ends. Deliver the alta receipt by the following business day; modification receipt within fifteen calendar days; a requested baja receipt within two calendar days of the request. Pensioner registration has a different first-payment rule. Keep employee communication and receipt-delivery evidence.

### Monthly computation, declaration and payment

1. **Prepare the right software and period.** RS 016-2026 introduced PDT PLAME 4.6 for January 2026 obligations. RS 213-2026 art. 2 introduces 4.7 from the October 2026 period, available 30 October, and specifies use for qualifying earlier original/rectifying returns. Do not follow an old landing page saying version 4.3 or the old skill's 4.5. Current legal resolution controls; confirm the installation/update route on [SUNAT PDT PLAME](https://orientacion.sunat.gob.pe/pdt-plame).
2. **Synchronise T-Registro.** In the PDT employer module validate the employer with SOL and synchronise. In **Declaraciones Juradas** choose the period and synchronise the relevant workers. Use the official personalised T-Registro file route if online sync fails; correct registration errors before filing.
3. **Enter actual payroll inputs.** In **Detalle de Declaración > Trabajadores**, record the actual days worked/subsidised, hours, **Jornada Laboral**, **Ingresos**, deductions and **Tributos y Aportes**. Distinguish remuneration accrued and paid. Reconcile employee pensions and employer health to the calculations above. Fifth-category withholding is a separate tax liability, not an employer pension contribution.
4. **Review Determinación de la Deuda.** Check the bases, resulting charges, EPS current/prior credits, prior payments, interest if applicable, balances and amounts to pay against the period control. The public PLAME Web receipt template identifies ordinary EsSalud base/result **452/412**, ONP **451/411**, fifth-category **455/415**, current/prior EPS credits **602/612**, and balances **712/711/715** respectively. These are the read public receipt fields, not a claim that every historical PDT screen or special regime uses identical boxes. Do not overwrite a calculated field simply to make a bank debit reconcile.
5. **Validate and submit.** In the PDT select **Validar**, correct inconsistencies, **Guardar**, then **Declaraciones Registradas** to generate **Archivo de Envío**. In SOL's declarations/payment platform choose **Presentación PDT / Receptor de Archivos PDT**, **Examinar**, upload and follow the submission checks. Retain the accepted **constancia de presentación**, form, period and order number. A saved file is not an accepted return.
6. **Pay and reconcile.** Use the enabled debit/card payment route or NPS where offered. Retain the actual payment confirmation and bank debit. SUNAT's template expressly says an NPS document `no es una constancia de pago`; generating a reference does not settle the liability or extend the legal deadline. Reconcile each concept and closing unpaid balance.
7. **AFP is separate.** Declare/remit AFP contributions through the applicable AFP/AFPnet collection route, not as an ONP payment. The SBS schedule note requires the relevant month's commissions and premiums within the first five business days of the following month; SBS contribution guidance gives that remittance deadline for employer contributions. Preserve worker breakdown, declaration status and paid receipt. Do not use the SUNAT RUC deadline as the AFP deadline.

**PLAME Web alternative:** SUNAT describes Form 601 PLAME Web as optional for private-sector employers with up to ten workers and/or up to ten service providers, provided the declaration exclusively covers the listed concepts: employee EsSalud, ONP, fourth/fifth-category withholding, fourth-category recipient information and eligible +Vida accident premiums. Check every condition for that month. In **Mis declaraciones y pagos**, select the form/period, download T-Registro data, complete and submit; otherwise use PDT PLAME. Correct a Web original with Web or PDT, re-entering all concepts, including unchanged ones. For specified worker identity/date-of-birth corrections SUNAT names Form 1601. Do not assume Web is available simply because employee headcount is small.

**Monthly deadline:** use the employer's last RUC digit, status, period and applicable SUNAT emergency extensions. Do not substitute an approximate mid-month range. As a source-read example only, the official Emprender 2026 calendar gives January obligations for RUC ending 0 on **16 February 2026**, with other digits/statuses later. Record the actual due date before authorising payment; that one example is not the timetable for every payroll month.

### Annual employment-tax process and benefit dates

LIR art. 79 generally excludes persons receiving exclusively fifth-category income from an annual return, unless a specific exception or SUNAT designation applies. Additional annual deductions, other income, balances and refund/regularisation conditions need the applicable annual-return rules. Do not tell every person with two employers to file just for that reason. For 2026 income, obtain the 2027 annual timetable and form when published; no 2027 deadline is established here. The old 2025-return timetable is historical and is not a 2026-income deadline.

CTS TUO art. 22 requires the deposit in the first fifteen calendar days of May and November and moves a non-working last day to the next business day. For ordinary 2026 deposits this gives **15 May** and **16 November**, the latter because 15 November is Sunday. Verify any applicable holiday/extension and worker facts. Truncated CTS has its separate cessation payment rule. Gratificaciones are paid in the first fortnight of July and December under Law 27735 art. 5, with truncated-benefit payment governed by DS 005-2002-TR; do not apply the CTS deadline exception to every labour payment without authority.

## Penalties and interest

A missing declaration, a wrong base/credit, and failure to remit money already withheld are different infringements. Identify the obligation, period, taxpayer table and actual conduct before choosing a sanction. The [Código Tributario](https://www.sunat.gob.pe/legislacion/codigo/codigotributario.pdf) separates filing infringements in art. 176 and substantive tax/withholding infringements in art. 178, with interest under art. 33 and discretionary/graduality powers under art. 166. Correcting the filing does not by itself prove that interest or a sanction has been extinguished.

ONP regulation arts. 24-26 specifically addresses employer liability for unremitted compulsory contributions. AFP arrears require the SPP collection rules, not an assumed SUNAT rate. Labour-inspection consequences for non-registration, unpaid benefits or missing CTS follow the labour inspection legislation and the applicable worker-count/employer category; they are not interchangeable with SUNAT tax penalties.

This skill does not publish a current late-interest percentage, individual fine, closure sanction or relief percentage. Obtain the current official rate and exact infringement/graduality instrument before quantifying. The old file's generic references to DL 1524, DS 008-2020-TR and RS 007-2025 do not establish a universal payroll sanction or automatic reduction. Keep the missing current quantification in the review brief rather than filling it from a secondary summary.

## Cross-border points

Keep the contribution analysis separate from income-tax residence and sourcing. Under LIR arts. 6-10 a foreign nationality or overseas bank payment does not establish non-domicile or foreign-source income. Domestic-law non-domiciled employment tax is 30% on Peruvian-source work income under art. 54(g), subject to the relevant treaty facts; it is not a 30% social contribution.

For an inbound/outbound assignment, identify the legal employer, services location, payroll payer, existing pension affiliation, duration and any documented social-security agreement/certificate or exemption. Do not apply a tax treaty as if it automatically displaced EsSalud or ONP/AFP. Obtain the actual agreement and certificate before exempting a contribution or claiming continued foreign coverage. No blanket expatriate contribution exemption or treaty rate is established here.

A cross-border employee may still need both a Peruvian payroll computation and a separate home-country reconciliation. Do not deduct foreign social contributions in the Peruvian fifth-category computation without a specific applicable legal basis. Foreign income, foreign-tax credits, fourth-category fees and capital income are outside the employment withholding computation and need the relevant LIR method.

## Two worked examples that recompute

These computations illustrate stated facts and periods, not amounts inferred from bank narrations. Use the actual month's official AFP schedule for a real filing. They preserve the old six example families and ten tests while correcting period and projection assumptions.

### Case 1: ordinary employer health and alternative pension affiliations

November 2026; ordinary contributory remuneration 5,000, no subsidy, EPS or retirement exemption; compare confirmed ONP with confirmed Habitat salary-flow affiliation, not both together. Health is 450 employer cost. ONP is 650; Habitat components are 500 savings + 68.50 insurance + 73.50 commission = 642. Income tax has not yet been calculated, so no final net-pay figure follows from this case alone.

```oa-check
name: November 2026 ordinary health and pension alternatives
inputs:
  pay: 5000
  rmv: 1230
  rma: 12732.70
steps:
  essalud: max(pay, rmv) * 0.09
  onp: pay * 0.13
  saving: pay * 0.10
  insurance: min(pay, rma) * 0.0137
  habitat_flow: pay * 0.0147
  habitat_total: saving + insurance + habitat_flow
expected:
  essalud: 450.00
  onp: 650.00
  saving: 500.00
  insurance: 68.50
  habitat_flow: 73.50
  habitat_total: 642.00
```

### Case 2: minimum-base period change and pension regression cases

A lawful part-time worker has contributory remuneration 900 in a month with no subsidy. The ordinary EsSalud floor still applies: 101.70 through September, 110.70 from October. This does not assert that 900 is lawful full-time pay or that ONP always has the full-month health floor. The other inputs retain the old 6,000 health and 4,000 pension test cases, with AFP rates specifically from November.

```oa-check
name: 2026 health minimum change and November pension regressions
inputs:
  low_pay: 900
  health_pay: 6000
  pension_pay: 4000
steps:
  health_before_october: max(low_pay, 1130) * 0.09
  health_from_october: max(low_pay, 1230) * 0.09
  health_regular: health_pay * 0.09
  onp_regular: pension_pay * 0.13
  habitat_regular: pension_pay * (0.10 + 0.0137 + 0.0147)
  profuturo_regular: pension_pay * (0.10 + 0.0137 + 0.0169)
  voluntary_snp_before_october: 1130 * 0.13
  voluntary_snp_from_october: 1230 * 0.13
expected:
  health_before_october: 101.70
  health_from_october: 110.70
  health_regular: 540.00
  onp_regular: 520.00
  habitat_regular: 513.60
  profuturo_regular: 522.40
  voluntary_snp_before_october: 146.90
  voluntary_snp_from_october: 159.90
```

### Case 3: AFP insurance ceiling and balance arrangement

November 2026 ordinary insured member, contributory pay 20,000. Only insurance is capped at 12,732.70. Round the insurance component to cents for this working paper. Habitat salary-flow commission remains on full remuneration; the mixed/balance member has no salary-flow commission. The annual balance fee is not calculated from salary here.

```oa-check
name: November AFP above the insurance ceiling
inputs:
  pay: 20000
  rma: 12732.70
steps:
  saving: pay * 0.10
  insurance: round(min(pay, rma) * 0.0137, 2)
  flow: pay * 0.0147
  habitat_total: saving + insurance + flow
  mixed_salary_total: saving + insurance
  uncapped_flat_error: pay * 0.1284 - habitat_total
expected:
  saving: 2000.00
  insurance: 174.44
  flow: 294.00
  habitat_total: 2468.44
  mixed_salary_total: 2174.44
  uncapped_flat_error: 99.56
```

### Case 4: EPS is a bounded credit, not a universal split

One eligible covered worker, normal November contributory pay 5,000 and eligible EPS payment 100 for that month. The 25% health limit is 112.50 but actual EPS paid limits the credit to 100, leaving EsSalud 350. A second independent scenario has one covered worker on 90,000 and eligible EPS paid 3,000: the 550 indexed per-worker cap binds, not the 25% health limit. These scenarios are not added into one employer's population calculation.

```oa-check
name: EPS actual payment and per-covered-worker limits
inputs:
  pay_a: 5000
  eps_a: 100
  pay_b: 90000
  eps_b: 3000
  uit: 5500
steps:
  health_a: pay_a * 0.09
  credit_a: min(health_a * 0.25, eps_a, uit * 0.10)
  remaining_a: health_a - credit_a
  health_b: pay_b * 0.09
  credit_b: min(health_b * 0.25, eps_b, uit * 0.10)
  remaining_b: health_b - credit_b
expected:
  health_a: 450.00
  credit_a: 100.00
  remaining_a: 350.00
  health_b: 8100.00
  credit_b: 550.00
  remaining_b: 7550.00
```

### Case 5: annual work-tax regression and a corrected monthly net-pay projection

For the annual-only tests, 38,500, 60,000 and 150,000 are **total annual taxable employment receipts before the fixed deduction**, not monthly salary times twelve with bonuses omitted. No additional annual deductions or credits are assumed. For the separate January payroll case, ordinary monthly salary is 5,000, with twelve salaries and two ordinary 5,000 gratificaciones in the projection, no other known amounts or credits, and confirmed ONP. The ordinary annual projection is 70,000, tax 2,760, January withholding 230 and January net 4,120. Any extraordinary health-replacement bonus or other extra payment when actually paid requires the art. 40(e) increment; this case does not exempt it from annual employment tax. Later-month withholding must use actual cumulative facts and that month's divisor.

```oa-check
name: Annual tax totals and January ordinary withholding with gratificaciones
inputs:
  uit: 5500
  salary: 5000
steps:
  fixed_deduction: uit * 7
  tax_at_fixed: max(38500 - fixed_deduction, 0) * 0.08
  base_60000: max(60000 - fixed_deduction, 0)
  tax_60000: min(base_60000, 27500) * 0.08
  base_150000: 150000 - fixed_deduction
  tax_150000: 27500 * 0.08 + 82500 * 0.14 + (base_150000 - 110000) * 0.17
  january_projected_gross: salary * 12 + salary * 2
  january_base: january_projected_gross - fixed_deduction
  january_annual_tax: min(january_base, 27500) * 0.08 + max(january_base - 27500, 0) * 0.14
  january_withholding: january_annual_tax / 12
  onp: salary * 0.13
  january_net: salary - onp - january_withholding
  non_domiciled_tax: 10000 * 0.30
expected:
  fixed_deduction: 38500.00
  tax_at_fixed: 0.00
  tax_60000: 1720.00
  tax_150000: 14005.00
  january_projected_gross: 70000.00
  january_base: 31500.00
  january_annual_tax: 2760.00
  january_withholding: 230.00
  onp: 650.00
  january_net: 4120.00
  non_domiciled_tax: 3000.00
```

The non-domiciled 3,000 result assumes 10,000 of Peruvian-source employment income with no applicable treaty modification. It is not the treatment for every non-resident receipt.

### Case 6: ordinary benefit bases and the old CTS bank amount

Ordinary worker meets the CTS gate, has constant computable salary 5,000, received a qualifying semestral gratificación 5,000, and has six complete credited months with no variable pay or other base changes. Base is 5,833.333..., and the half-year CTS is 2,916.67. A full ordinary gratificación of 5,000 also generates health-replacement bonus 450, or 337.50 in the qualifying EPS case. These alternatives are not both paid for the same entitlement.

```oa-check
name: Ordinary CTS sixth and statutory bonus alternatives
inputs:
  salary: 5000
  received_gratificacion: 5000
  months: 6
steps:
  cts_base: salary + received_gratificacion / 6
  cts_deposit: round(cts_base * months / 12, 2)
  ordinary_bonus: salary * 0.09
  eps_bonus: salary * 0.0675
expected:
  cts_deposit: 2916.67
  ordinary_bonus: 450.00
  eps_bonus: 337.50
```

The old illustrative bank line `14.05.2026; CTS DEPOSITO; DEBIT; -2500.00 PEN` remains a candidate CTS deposit, not proof the legal amount is 2,500. Obtain that worker's actual computation. The bank date is consistent with payment before the ordinary May deadline, but does not establish eligibility, base or full settlement.

### Case 7: variable-pay benefits and cessation are ordinary cases

Ordinary eligible worker has fixed computable salary 5,000 and complementary variable payments 300, 600 and 900 in three separate months of the six-month period, zero in the other months. The three-month gate is met; the computable average is 300. With a qualifying received semestral gratificación of 5,000, six credited months produce CTS 3,066.67. A complete ordinary gratificación based on salary plus this average is 5,300, with ordinary health-replacement bonus 477. In a separate cessation scenario, computable remuneration in the immediately preceding month is 5,300 and the worker has three complete credited calendar months in the relevant semester: truncated gratificación is 2,650, plus ordinary bonus 238.50, payable under the 48-hour rule. There are no non-credited days or EPS cover in these hypothetical cases; do not substitute the cessation-month salary for the previous-month gratificación base.

```oa-check
name: Complementary variable pay and truncated ordinary gratification
inputs:
  salary: 5000
  variable_one: 300
  variable_two: 600
  variable_three: 900
  received_gratificacion: 5000
  previous_month_base: 5300
  complete_credited_months: 3
steps:
  variable_average: (variable_one + variable_two + variable_three) / 6
  cts_base: salary + variable_average + received_gratificacion / 6
  cts: round(cts_base * 6 / 12, 2)
  ordinary_gratificacion: salary + variable_average
  ordinary_bonus: ordinary_gratificacion * 0.09
  truncated_gratificacion: previous_month_base * complete_credited_months / 6
  truncated_bonus: truncated_gratificacion * 0.09
expected:
  variable_average: 300.00
  cts: 3066.67
  ordinary_gratificacion: 5300.00
  ordinary_bonus: 477.00
  truncated_gratificacion: 2650.00
  truncated_bonus: 238.50
```

### Bank-only and refusal regression cases

- `16.02.2026; SUNAT PAGO PLAME 0601; PERIODO ENE-2026; DEBIT -3250.00 PEN`: reconcile to January PLAME and its payment detail. For the RUC-0 example the date matches the read official calendar. The debit alone cannot establish which portion was EsSalud, ONP or withholding, or the due date for a different RUC/status.
- `05.02.2026; AFPNET AFP INTEGRA; APORTES ENE-2026; DEBIT -1940.00 PEN`: request the AFP contribution schedule and paid receipt for January. Do not apply November's commission/insurance snapshot backwards or reclassify it as an employer pension match.
- Pension affiliation unknown: stop the pension and net-pay calculation, request actual affiliation/period. Show only independently determinable components with their limitations.
- AFP administrator, commission arrangement, insurance eligibility or month-specific ceiling unknown: obtain the missing fact; do not use a highest-rate default or a stale RMA.
- EPS payment/population or subsidised-day evidence missing: do not claim the maximum credit or ordinary full-month minimum by assumption.
- CTS/gratificación base, credited time or special regime missing: explain the method and request the records before producing an amount for payment.
- Non-domicile, split-year or treaty claim uncertain: resolve source and status before selecting employment tax deductions or any foreign social-security exemption.
- Current sanction/interest requested: identify the law, date and applicable relief before quantifying; no invented penalty figure.

## Ask the client first

Ask only for facts not already present in the records:

1. Which employee, service month and actual payment period? Contract, ordinary/special regime, days/hours worked, subsidised and unpaid periods?
2. What remuneration components were accrued and paid, including in-kind pay, variable pay, allowances, ordinary gratificaciones and extraordinary bonuses?
3. Which pension system applied in that month? For AFP, which administrator, commission arrangement, actual devengue schedule and insurance eligibility? Any pensioner/retirement exemption documents or effective affiliation change?
4. Which workers had qualifying EPS cover, what source months were paid, and what current/prior credits have already been used?
5. Tax domicile/source evidence, other employers, prior income/withholding, credits, extraordinary pay and cessation events? Do not ask the employee to certify a rate that the official schedule supplies.
6. RUC ending/status, accepted T-Registro and PLAME receipts, applicable due date/extension, AFP declaration and payment receipt, bank statement and reconciliations?
7. For benefits: credited service, April/October or June/November reference remuneration, actual semestral bonus received, regular variable pay/family allowance, and the nominated CTS deposit account?
8. For an independent person: actual legal relationship, affiliation, declared contribution income, contribution months and payment history? For a foreign assignment: employer/location, actual agreement and certificate, not a presumed treaty exemption?

Before completing, reconcile the total to employee payslips and contribution returns, distinguish the employer charge from employee deductions, confirm the source period of every rate and credit, and list unresolved differences. Outputs remain informational/computational and require qualified professional review against the actual facts before filing or payment; this preserves the existing skill's professional-review requirement.

## Sources

Read dates refer to the actual portions below, not the whole contents of a long compilation. Exact short original-language wording appears beside the relevant figures and methods.

| Source and portion actually read | URL | Read on |
|---|---|---|
| El Peruano, DS 015-2026-TR, complete decree including art. 1.2 and future-tranche condition | https://busquedas.elperuano.pe/dispositivo/EX/2559163-1 | 2026-11-11 |
| SUNAT UIT table, 2025/2026 rows and legal bases | https://www.sunat.gob.pe/indicestasas/uit.html | 2026-11-11 |
| Law 26790, arts. 5-6, 15-16, 19; original compilation, amended health minimum read through current SUNAT interpretation below, not its old filing deadline | https://www.essalud.gob.pe/transparencia/pdf/publicacion/ley26790.pdf | 2026-11-11 |
| SUNAT report 003-2007, complete operative analysis/conclusions on amended art. 6 and regulatory art. 33, minimum, subsidy and unpaid months | https://www.sunat.gob.pe/legislacion/oficios/2007/oficios/i0032007.htm | 2026-11-11 |
| SUNAT report 088-2004, analysis 1-4/conclusions on EPS conditions, three limits, late payment and carryforward | https://www.sunat.gob.pe/legislacion/oficios/2004/oficios/i0882004.htm | 2026-11-11 |
| ONP consolidated regulation DS 354-2020-EF/DS 282-2021-EF, arts. 18-31, mandatory/voluntary bases, withholding and collection | https://repocdn.onp.gob.pe/Normativa/Base_normativa/NPT046.pdf | 2026-11-11 |
| SBS commission/premium schedule, complete November 2026 table and notes; not evidence for other devengue months | https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/paginas/comision_prima.aspx | 2026-11-11 |
| SBS Title V, arts. 2, 87(a)-(b), 87A, 88 on affiliation, retirement exceptions and collection registration | https://www.sbs.gob.pe/Portals/0/jer/LEYES_SPP/2023/T%C3%ADtulo_V_SPP_15-11-2024.pdf | 2026-11-11 |
| SBS Aportes, operative employer and independent contribution paragraphs and reform-update note | https://www.sbs.gob.pe/usuarios/aprende-con-la-sbs/aportes | 2026-11-11 |
| LIR chapter II, arts. 6-10, domicile and Peruvian source | https://www.sunat.gob.pe/legislacion/renta/ley/capii.pdf | 2026-11-11 |
| LIR chapter V, art. 34, employment-income definition | https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf | 2026-11-11 |
| LIR chapter VI, arts. 45-46 and 49, work deductions and annual conditions | https://www.sunat.gob.pe/legislacion/renta/ley/capvi.pdf | 2026-11-11 |
| LIR chapter VII, arts. 53 and 54(g), resident marginal bands/non-domiciled work | https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf | 2026-11-11 |
| LIR chapter XI, art. 79, annual return and fifth-category exclusion | https://www.sunat.gob.pe/legislacion/renta/ley/capxi.pdf | 2026-11-11 |
| LIR regulation chapter X, arts. 40-44, projection, allocation, special cases and multiple employers | https://www.sunat.gob.pe/legislacion/renta/regla/cap10.pdf | 2026-11-11 |
| SUNAT T-Registro, employer-obligations table, registration/update/baja and receipt delivery | https://orientacion.sunat.gob.pe/03-obligaciones-del-empleador-t-registro | 2026-11-11 |
| SUNAT Emprender Planilla Electrónica, operative obligation/procedure/PLAME Web/correction paragraphs and displayed January 2026 calendar; superseded 4.3 version not used | https://emprender.sunat.gob.pe/principales-impuestos/planilla/planilla-electronica | 2026-11-11 |
| SUNAT official January 2024 presentation, pp. 3-29, T-Registro data/CIR, PDT fields, sync/validation/export/upload, Web eligibility/payment; current version supplied by 2026 resolutions | https://orientacion.sunat.gob.pe/sites/default/files/inline-files/PDF%20de%20T-Registro%20y%20PLAME.pdf | 2026-11-11 |
| SUNAT RS 016-2026, complete two-page resolution on version 4.6 | https://www.sunat.gob.pe/legislacion/superin/2026/000016-2026.pdf | 2026-11-11 |
| SUNAT RS 213-2026, complete two-page resolution, art. 2 on version 4.7 and affected periods | https://www.sunat.gob.pe/legislacion/superin/2026/000213-2026.pdf | 2026-11-11 |
| SUNAT public unpopulated receipt template, PLAME Web 0601 fields and NPS notice only; no authenticated submission made | https://e-plataformaunica.sunat.gob.pe/app/recaudacion/tributaria/internet/html/carrito.html | 2026-11-11 |
| CTS TUO DS 001-97-TR, arts. 3-6, 9-18 and 21-23 on eligibility, base, time and deposit dates | https://cdn.www.gob.pe/uploads/document/file/229267/TUO_Compensacion_por_Tiempo_de_Servicios_-_D.S_001-97-TR.pdf | 2026-11-11 |
| MTPE official labour compendium, Law 27735/DS 005-2002-TR pp. 329-335; Law 30334 arts. 1/3 pp. 338-339; DS 012-2016-TR arts. 2-7 pp. 344-346 | https://cdn.www.gob.pe/uploads/document/file/289875/Compendio_normas_laborales_29-01-19.pdf?v=1549987495 | 2026-11-11 |
| Código Tributario, arts. 33, 166, 176 and 178, interest/infringement structure, not a current individual relief computation | https://www.sunat.gob.pe/legislacion/codigo/codigotributario.pdf | 2026-11-11 |
| IGV Law chapter VI, art. 18 on input-credit substantive requirements; payroll remittance itself is not a purchase invoice | https://www.sunat.gob.pe/legislacion/igv/ley/capitul6.pdf | 2026-11-11 |

Not yet confirmed: SBS rates and insurance ceilings for devengue months other than the read November 2026 snapshot, including the old early-year/second-quarter estimates; current AFP/SUNAT late-interest percentages, particular SUNAFIL/SUNAT fines and exact graduality relief; a 2027 annual timetable for 2026 income and the old historical 2025-return deadline range; proprietary live narration dictionaries of BCP, BBVA, Interbank and Scotiabank; assignment-specific social-security agreements/certificates and exemption eligibility; numerical schedules for special labour/insurance regimes; pension-reform commencement and contribution schedules beyond the current SBS guidance. Obtain these primary texts before applying those cases. No unknown pension affiliation, EPS eligibility, benefit base, tax domicile or client fact is resolved by a default.
