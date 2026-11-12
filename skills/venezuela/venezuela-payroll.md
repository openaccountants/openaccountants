---
name: venezuela-payroll
description: >
  Compute and reconcile Venezuela employee payroll for 2026, including employment
  classification, ordinary and exceptional pay, income-tax withholding, separate
  contribution bases, receipts and employer cost. Use for Venezuela payroll,
  retención ISLR, Unidad Tributaria, AR-I, AR-C, salario normal, IVSS, Paro Forzoso,
  Régimen Prestacional de Empleo, FAOV, INCES, LOPCYMAT, utilidades, vacaciones,
  prestaciones sociales, cestaticket, bono de guerra económica, Ingreso Mínimo
  Integral, gross-to-net pay and bolívares or foreign-currency payroll. Covers
  resident percentage estimates, multiple employers, missing employee information,
  recalculations and nonresident employees. Distinguishes employment from independent
  professional fees. Produces a working paper and filing packet; current monetary
  units, unresolved bonus tax treatment, contribution assessments and portal
  instructions must be supported before a payroll can be released.
version: 0.2
jurisdiction: VE
tax_year: 2026
last_updated: 2026-11-12
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: computation
---

# Venezuela payroll, 2026 v0.2

> **Not yet approved.** This revision is a source-cited draft. The [earlier version approved by Jose Padilla on 3 November 2026](https://github.com/openaccountants/openaccountants/blob/157f7d8be741c4c7347a88c8a2970b529d175741/skills/venezuela/venezuela-payroll.md) is preserved with its original attribution; that approval does not cover this text.

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare the gross pay, deductions, net payment, employer charges and supporting records for a Venezuelan employment relationship in 2026. Load `payroll-workflow-base` for the common payroll controls. The output is a traceable working paper, payslip, withholding calculation, contribution schedule and submission packet, with unresolved matters held for review. It is not a bank-description classifier that turns an unexplained transfer into taxable salary.

Start with these answers:

| Question | Working rule | Primary source |
|---|---|---|
| Which resident employees enter the withholding mechanism? | Estimated total annual remuneration from one or more payers **exceeding 1,000 UT**; test remuneration before the annual desgravamen. Exactly 1,000 UT is not “exceeding”. | Decreto 1.808 art. 2, “un total anual que exceda de mil unidades tributarias”; [original Gaceta 36.203, public-university archive](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf) |
| What percentage goes on each payment? | A resident's annual estimate produces a percentage of remuneration, subsequently revised for changed circumstances. It is not automatically annual tax divided by twelve. | Decreto 1.808 arts. 4-8, “porcentaje de retención”; [original gazette](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf) |
| When does withholding arise? | On payment or accounting credit, whichever happens first. A bank date alone cannot establish the period. | LISLR art. 84, “lo que ocurra primero”; [Gaceta 6.210](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf) |
| Is there one salary base for everything? | No. Record labour salary, normal salary, income-tax remuneration and each contribution base separately. Apply the specific statute to each. | LOTTT arts. 104-107; [INCRET statutory text](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf); LISLR art. 31, [Gaceta 6.210](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf) |
| Can an employer charge be deducted from the worker? | Separate employer liability from employee deductions. INCES expressly prohibits passing its employer contribution to workers. | INCES Law art. 49, “Queda prohibido el descuento”; [INCES statutory publication](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf) |
| Does a bank label prove an exemption? | No. Obtain the contract, legal basis, payment conditions and source document. A label does not resolve the salary or tax classification. | LOTTT arts. 18, 104-106; [INCRET statutory text](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |

The ordinary private-sector employment workflow is covered. LOTTT art. 3 applies territorially; art. 6 distinguishes public officials governed by their special rules from contracted public-sector workers; art. 7 addresses professional services in the presence of an employment relationship. Do not apply an ordinary private-sector result to public officials, directors, autonomous professionals or a special collective agreement without classification. Sources: [LOTTT arts. 3, 6-7, 18 and 55](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf).

The annual personal-tax return is owned by [Venezuela income tax](venezuela-income-tax.md). Detailed fund coverage and contribution computations belong to [Venezuela social contributions](venezuela-social-contributions.md). Those links are routing instructions, not confirmation of their current figures: if a sibling still covers an earlier year or lacks the necessary primary source, use the opened statute and a separate current working paper or hold that calculation. Never promote an old sibling's monetary unit, rate, cap or deadline into a verified 2026 input.

**AUDIT FLASH POINT**: the current employment ISLR base is not resolved merely by reading the printed 2015 LISLR art. 31. That text uses a broad regular/accidental-remuneration definition with named exclusions, while LOTTT art. 107 refers to normal salary. The current judicial and administrative interpretation must be established before disputed bonuses are included or excluded. This Guide does not adopt either “all bonuses exempt” or “all pay taxable” as a default. The unresolved current interpretation is listed at the end.

## Ask the client first

Obtain these documents before calculating. Ask only for facts not already in the employment and payroll records.

1. **Employer and period:** legal name, RIF, establishment, private/public status, special-taxpayer qualification and its notice, payroll period, accounting-credit dates, payment dates, payroll frequency and who approves payroll.
2. **Worker and relationship:** identity, RIF, actual duties and dependency, signed contract or evidence of oral terms, start/end dates, residence facts and day counts, prior-year residence, other employers, working place, collective agreement, ordinary hours and risk classification. Citizenship does not substitute for tax residence.
3. **Earnings:** contractual gross salary by currency, commissions, overtime, night/holiday work, absences, paid leave, food scheme, allowances, reimbursements, utilidades, bonuses, termination items and benefits in kind. Obtain receipts and the legal basis for each classification; a bank's net amount is not gross salary.
4. **Annual withholding estimate:** each payer's expected fixed, variable and occasional remuneration; employee's signed declaration and percentage; actual-desgravamen evidence or standard-deduction election; qualifying family and shared-support facts; prior excess withholding and its refund, offset, assignment and limitation status; tax already withheld and remuneration already received.
5. **Contributions and benefits:** registrations, current assessment notices, each fund's covered workers, base, cap, rate, risk, period, employee/employer split, payments and credits. Obtain prior reconciliations and the accruals for vacation, profit participation and prestaciones sociales.
6. **Current authority evidence:** applicable UT value and effective date, minimum wage and benefit instruments, currency-conversion rule and rate date, remittance calendar for this taxpayer class, current portal instructions, submission permission and bank payment authority. A previous payroll is a reconciliation input, not proof that the law is unchanged.

Sources for the employment and pay records: [LOTTT arts. 55-59 and 106](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf). Sources for residence, annual declaration and timing: [LISLR arts. 51, 57-60 and 84](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf), [COT art. 30](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf), [Decreto 1.808 arts. 4-8](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf).

## The method, step by step

### 1. Establish the employment and pay terms [LOTTT arts. 55-62](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf)

Identify personal services under dependency. A professional title, contractor invoice or foreign payer does not by itself remove an employment relationship. Article 55 describes services under dependency for remuneration. Under art. 58, a contract is preferably written but the absence of writing does not erase the relationship: proven services engage the statutory presumption about the worker's asserted terms, subject to contrary proof.

For a written contract, reconcile the two originals and acknowledgement of delivery with the actual terms. Article 59 requires identification, start date, relationship type, services, place, hours, salary and payment method and frequency, other benefits and collective terms, among its particulars. Do not invent a fixed term to match a payroll-system field: arts. 60-62 establish the indefinite-term starting point and limits on fixed-term contracts.

Use contractual gross pay, attendance and approved changes. Reconcile opening payroll liabilities and the last completed payroll, but correct an unsupported prior treatment. Salary must satisfy the applicable legal minimum under arts. 99 and 129-130; the current monetary minimum has not been confirmed here. Do not certify compliance from an old minimum-wage amount or a combined USD benefit announcement. A higher contractual or collective entitlement remains relevant; the statute is not authority to reduce it.

### 2. Give each earning a base decision [LOTTT arts. 104-107](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf)

Create a component register before summing anything. For each line record gross amount, currency, earned period, payment/credit date, contract clause, supporting receipt, labour-salary status, normal-salary status, annual ISLR treatment and each contribution treatment. A disputed component stays visible with an unresolved decision; it must not disappear from gross cash.

| Component | Labour/payroll decision | Tax and contribution control |
|---|---|---|
| Fixed salary and recurring commissions or premiums | Art. 104 salary includes remuneration for services regardless of label; normal salary is regular and permanent, subject to the article's exclusions. | Establish ISLR and fund treatment under their specific texts; do not equate gross labour salary with every other base. |
| Overtime, night and holiday pay | Calculate the statutory pay and applicable higher agreement; identify whether a component meets the normal-salary definition. | Do not exclude from tax because it is occasional, or include in every contribution merely because it is labour salary. |
| Qualifying food benefit | Art. 105 includes qualifying food services, coupons, cards and money among listed nonremunerative benefits. The facts must fit the legally provided benefit. | “Cestaticket” in a transfer description does not prove the scheme or determine every tax consequence. |
| Medical/pharmaceutical/dental reimbursements; work clothes; school supplies/toys; scholarships/training; funeral benefits | Art. 105 lists these benefits with their statutory conditions. A contract or collective agreement can stipulate salary character. | Keep receipts, purpose and any agreement changing salary treatment. Do not turn an unsupported allowance into reimbursement. |
| Utilidades, aguinaldo and vacation bonus | Apply the specific labour entitlement. Art. 192 expressly gives the vacation bonus salary character. | Keep their own tax and fund decisions; INCES employee liability specifically addresses year-end benefits. |
| “Bono de guerra”, IMI, discretionary or indexed bonus | Obtain the applicable instrument, worker group, effective date, entitlement and actual terms. Neither denomination nor foreign currency decides salary character. | Hold disputed current ISLR interpretation; do not create a general non-salary/non-taxable bucket. |
| Indemnity, prestaciones sociales, pension or retirement product | Identify the legal cause and distinguish earned salary from compensation. | LISLR art. 14(4),(6) contains particular exemptions; LOTTT art. 143 expressly exempts prestaciones sociales and their interest from ISLR. Apply only to qualifying items. |

The first two columns apply [LOTTT arts. 104-107, 143 and 192](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf). The last row also applies [LISLR art. 14](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf). The current interpretation of employment art. 31 remains unresolved. Do not infer that every termination payment is exempt or that all ordinary bonuses are indemnities.

Keep the labour definition and the tax timing separate. LISLR art. 5 addresses availability of employment enrichment when paid, whereas art. 84 expressly imposes withholding at payment or credit, whichever is first. Record both dates and the withholding event rather than postponing an accrued-and-credited payment to its bank settlement. Source: [LISLR arts. 5 and 84](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf).

### 3. Calculate labour earnings before deductions [LOTTT arts. 113-143, 173-183 and 190-197](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf)

### Rates, bands and thresholds

These statutory rules are not current currency amounts. Verify actual wage compliance and any higher contract or collective benefit separately.

| Item | Rate, threshold or amount and adjacent condition | Source and exact anchor |
|---|---|---|
| Ordinary daily wage from a monthly wage | Divide monthly wage by 30. Hourly wage divides the daily wage by the actual ordinary hours of that shift; do not use eight hours for every shift. | LOTTT art. 113, “la treintava parte de la remuneración mensual”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Ordinary day, night and mixed schedules | General day: 8 hours/day and 40/week; night: 7/day and 35/week; mixed: 7.5/day and 37.5/week. Day is 05:00-19:00, night 19:00-05:00; a mixed shift with more than 4 night hours is wholly night. General week includes 2 continuous paid rest days. Special schedules require the specific exception. | LOTTT art. 173, “dos días de descanso, continuos y remunerados”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Night premium | At least 30% above the agreed ordinary daytime wage, on the normal wage for the relevant shift. | LOTTT art. 117, “treinta por ciento”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Authorized overtime | At least 50% above the agreed ordinary-hour wage, using normal wage for the relevant shift. Preserve the authorization and record. Unauthorized overtime engages art. 182's doubled surcharge, not the ordinary premium. | LOTTT arts. 118 and 182-183, “cincuenta por ciento”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Paid rest and ordinary holidays | Monthly salary already includes ordinary paid rest and holidays. Apply the period-average normal wage for the entitlement. Do not automatically strip paid weekly rest because of one missed day. | LOTTT art. 119, “comprendidos en la remuneración”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Work on a holiday | In addition to the ordinary holiday entitlement, pay actual work with at least a 50% surcharge on normal wage. If monthly pay already contains the ordinary holiday, the extra for one full holiday worked is 1.5 daily wages, not another 2.5 daily wages. | LOTTT art. 120, “además del salario correspondiente a ese día”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Payment interval | Agreed interval cannot exceed a quincena; monthly payment is allowed where the employer provides food **and** accommodation. Quincenal is half-monthly, not a fourteen-day payroll. Pay on a working day; a nonworking payday moves to the preceding working day under art. 127. | LOTTT arts. 126-127, “alimentación y vivienda”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Annual vacation duration | After one uninterrupted service year, 15 working days; subsequent years add one paid day per year, up to 15 additional days. Food benefit and social contributions continue under art. 190. | LOTTT art. 190, “quince días hábiles”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Vacation wage and payment | Normal wage in the effective month before vacation; piecework/commission workers use the preceding 3-month average. Pay vacation wages at commencement. Preserve ordinary food/accommodation or its agreed value under art. 193. | LOTTT arts. 121 and 193-194, “tres meses”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Vacation bonus | At least 15 normal-salary days plus one day per service year, up to 30 days. It has salary character. | LOTTT art. 192, “hasta un total de treinta días”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Profit participation | At least 15% of liquid profits; individual floor 30 salary days, ceiling 4 salary months, proportionate to complete service months for a partial year. Compute the common pool and allocate by each worker's share of total annual wages. | LOTTT arts. 131 and 133-136, “quince por ciento de los beneficios líquidos”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Year-end advance and final profits | Profit-making entities advance at least 30 salary days in the first 15 days of December or collective-agreement date. It is not recoverable if there are no profits. Final participation is payable within 2 months of year-end; an additional distribution follows art. 133 where profits exceed the declared amount. | LOTTT arts. 132-133 and 137, “no estará sujeta a repetición”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Nonprofit employer | Not subject to profit participation but owes a year-end bonus of at least 30 salary days. | LOTTT art. 140, “por lo menos treinta días”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |
| Termination and benefits | Reconcile accrued guarantees with the final statutory benefit calculation and pay the greater entitlement, not a flat employer contribution on every payroll. | LOTTT arts. 122 and 141-143, “el monto que resulte mayor”; [INCRET](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf) |

Special hours are not an invitation to ignore limits. Articles 175-177 describe particular categories, continuous shifts and health restrictions. Article 178's general overtime limits are 10 total effective hours/day, 10 overtime hours/week and 100/year, subject to legally established exceptions. Article 182 requires Labour Inspector permission, with notice on the next working day for a duly proven unforeseen urgent case; unapproved overtime carries double the statutory surcharge. Keep art. 183's worker, work, hours and remuneration record. Source: [LOTTT arts. 175-183](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf).

Termination needs its own reconciliation. Article 122's benefit wage includes the statutory salary components and aliquots of vacation bonus and utilidades; variable wages use the preceding six-month average. Article 142 requires a guarantee of 15 salary days each quarter, with the right arising at the quarter's start; after the first year, add two days per year cumulatively up to 30. At termination compare that guarantee with 30 days per service year or fraction exceeding six months. Service under three months engages the five-days-per-month-or-fraction branch. Pay within five days after termination or the statutory interest follows. Article 143 governs the worker's chosen deposit or authorized book credit and interest treatment; it is not simply a monthly cash deduction from the worker. Sources: [LOTTT arts. 122 and 142-143](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf).

Unused vacation at termination uses normal wage at termination under art. 195; art. 196 prorates vacation and vacation bonus by complete service months where the year is incomplete. While employment continues, paying instead of granting actual vacation does not discharge the obligation to grant the leave and pay it under art. 197. Source: [LOTTT arts. 195-197](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf).

### 4. Build one annual resident ISLR estimate [LISLR arts. 50-60](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf)

First resolve residence using LISLR art. 51 together with COT art. 30, including the latter's domicile rules and the prior-year provision. LISLR uses more than 183 days, not Decreto 1.808's historical 180-day wording. Presence alone is not the only statutory test. The individual's worldwide-income and Venezuelan-source positions also require LISLR art. 1. Obtain treaty and overseas-work facts for cross-border cases; do not infer a treaty exemption from nationality. Sources: [LISLR arts. 1 and 51](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf), [COT art. 30](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf).

For a resident, test Decreto 1.808 art. 2's combined remuneration threshold before the desgravamen. Distinguish it from LISLR art. 77's annual-return test on net enrichment or gross receipts. Crossing either annual-return threshold does not prove that a particular payroll should use a flat percentage. Sources: [Decreto 1.808 art. 2](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf), [LISLR art. 77](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf).

Do the annual working in UT and preserve the currency conversion separately. COT art. 3 gives the unit rule for national-tax periods: year-end unit for annual taxes and start-of-period unit for other periods. It expressly prevents applying the national tax unit to obligations administered by other bodies; never mechanically convert all labour benefits or contributions with the ISLR UT. The current currency value and any applicable authority implementation for the withholding estimate have not been confirmed here. Do not substitute the old Guide's monetary unit. Source: [COT art. 3](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf).

Use the annual PIT working paper for the complete art. 50 Tarifa No. 1 table and arts. 57-60 deductions and rebates. Do not duplicate and maintain another complete annual tax table inside payroll. Where the income Guide remains stale, verify those opened articles directly and record the annual calculation; the worked cases below use their applicable first bracket and expressly elected deduction. The later LISLR art. 58 supersedes the old deduction amount printed in the 1997 decree. Apply actual desgravámenes or the elected standard alternative, never both. Family rebates require the spouse, residence, age/study/incapacity, shared support and separate-return conditions in art. 59, not merely a count of names in the personnel file.

A desgravamen reduces the annual base; a rebaja reduces the calculated annual tax. Prior excess withholding is a separate qualifying credit, not another salary deduction. Neither employee fund payments nor every reimbursement can be deducted from the annual ISLR base without its own primary authority. Document which relief is claimed, by whom, and why. Sources: [LISLR arts. 57-60](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf) and [Decreto 1.808 arts. 4-5](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf).

### 5. Turn that estimate into the payment percentage [Decreto 1.808 arts. 4-8](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf)

For an employee supplying the declaration:

1. Aggregate estimated annual fixed, variable and occasional remuneration from **every payer**. Keep one annual personal calculation and send the resulting percentage to each payer. Do not allocate the full personal deduction independently to each job.
2. Subtract the corresponding desgravamen from annual remuneration in UT and apply the annual tariff. Then subtract the legally allowed personal/family rebates and qualifying prior excess withheld, as prescribed by art. 5. Retain the annual worksheet and its supporting declaration.
3. Divide the resulting annual tax by **total estimated annual remuneration**, using consistent units, then multiply by 100. That is the percentage to apply to each relevant payment or credit. The denominator is not remuneration after the personal deduction.
4. Present the information before expiry of the first fortnight of the tax year and in all cases before the first effective remuneration. The employer may review errors and notify the worker under art. 4. Preserve the signed version and date used for each payroll.

Source and wording: art. 4 requires remuneration “de cada uno de sus deudores o pagadores”; art. 5 divides by “el total de la remuneración anual estimada”. [Original Decreto 1.808, PDF page 2](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf).

**Missing declaration does not mean no withholding.** Article 6 requires the employer to determine the percentage under art. 5 using remuneration it expects to pay and the expressly stated personal tax rebate, and to inform the worker in writing of the inputs. The text does not expressly establish automatic standard-deduction election or additional family rebates when the employee has supplied nothing. Obtain the election or current primary administrative authority before inserting those assumptions. Do not assert that silence is an election, or that this wording conclusively prohibits every later-authorized default. Source: [Decreto 1.808 arts. 4-6](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf).

**Changed estimate:** under art. 7, recompute annual estimated tax under art. 5(1)-(2), subtract tax already withheld, and divide by annual remuneration still to be received, then multiply by 100. Preserve a positive **or negative** result: the article says “sea positivo o negativo”. Present the revised percentage before the first fortnight of March, June, September and December. If actual pay exceeds an employee's estimate and the worker has not notified the change, the employer recalculates using prior information except the annual remuneration estimate and gives written inputs. Under art. 8, the worker's subsequently supplied percentage replaces the employer's calculation within the statutory presentation schedule. Source: [Decreto 1.808 arts. 7-8, PDF page 3](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf).

Do not clamp a negative result to zero in the worksheet. The quoted rule does not by itself authorize a particular employer cash refund, portal credit or offset process. Keep the overwithholding visible and resolve its authorized implementation before releasing an adjustment. A zero denominator, ceased employment, a wholly exhausted annual remuneration estimate or an unsupported credit needs review, not division by zero or an invented refund.

For a nonresident **employee**, Decreto 1.808 art. 3 prescribes 34% of total paid or credited remuneration regardless of amount; LISLR art. 50 also states the nonresident rate. Do not apply the independent-professional presumed base to an employment relationship. LISLR art. 39's nonresident noncommercial professional-services branch uses presumed net income of 90% of gross, subject to the distinct technical-assistance/services rules in art. 41. This is a classification comparison, not an employee payroll discount. Source: [Decreto 1.808 art. 3](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf); [LISLR arts. 39, 41 and 50](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf).

### 6. Compute each contribution separately [INCES arts. 49-52](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf)

Maintain a separate row per scheme, with legal coverage, base definition, cap, rate, period, employee deduction, employer charge, due date and settlement reference. Distinguish IVSS social insurance, Régimen Prestacional de Empleo/Paro Forzoso, FAOV housing, INCES training and LOPCYMAT workplace-risk obligations. These names describe distinct obligations; a combined payroll percentage hides their different rules.

Current IVSS, employment-regime, housing and workplace-risk assessments require the current, sourced social-contributions working. This Guide does not adopt an unverified rate, ceiling or payment calendar from the earlier version. A disputed item is **held**, not zero. Do not select the lowest IVSS risk class because no assessment was supplied, invent a housing cap by copying another scheme, or equate an unresolved LOPCYMAT cash contribution with absence of health-and-safety duties. Obtain registration and assessment evidence and reconcile to the respective authority's statement before release.

The INCES authority's published law does establish the following controls; these are not a substitute for the other schemes:

| INCES item | Rule, covered group and payment condition | Exact primary anchor |
|---|---|---|
| Employer contribution | Private-sector entities and state enterprises with their own self-managed income occupying 5 or more workers: 2% of **normal monthly salary paid**. Pay within 5 days after each quarter ends. The taxable event arises from salary payment; do not deduct this employer liability from workers. | Law art. 49, “dos por ciento del salario normal mensual pagado”; [INCES](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf) |
| Worker contribution | Workers in entities occupying 5 or more workers: 0.5% of annual utilidades, aguinaldos or year-end bonuses. Employer withholds and remits within 10 days after payment, indicating origin. It is not an automatic deduction on every ordinary monthly salary. | Law art. 50, “cero coma cinco por ciento”; [INCES](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf) |
| Registration | Entities subject to these contributions register within 45 working days following constitution and provide required information. | Law art. 51, “cuarenta y cinco días hábiles”; [INCES](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf) |
| Solvency | The certificate records compliance with training, apprentices and tax obligations at issue date; do not treat it as proof that a later payroll has been paid. | Law art. 52, “a la fecha de su expedición”; [INCES](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf) |

For normal salary used by INCES, keep the LOTTT art. 104 regular/permanent definition and statutory exclusions in the component register. Do not casually replace the law's “normal salary paid” with all gross payroll. The employee year-end base and employer normal-salary base are different, and their deadlines are different. Do not reuse ISLR withholding periods as INCES deadlines. Sources: [INCES arts. 49-50](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf), [LOTTT art. 104](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf).

### 7. Reconcile gross, net and employer cost [LOTTT arts. 106 and 123-127](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf)

For each currency, start with approved gross cash earnings. Subtract supported employee ISLR withholding, supported employee fund contributions and other legally authorized worker deductions. Add separately documented reimbursements or benefits paid outside salary without hiding them in the wage base. Employer-only charges increase employer cost and the liability to the fund; they do not reduce net pay. Keep noncash benefits and provisions visible but separate from cash transferred.

A working reconciliation is:

- Net worker payment = gross cash earnings + separately payable supported reimbursements/benefits - employee ISLR - employee contributions - other authorized deductions.
- Period employer cost = gross employment cost + employer-only contributions + separately recognized benefit/provision expense. Identify what is paid now and what is accrued; do not add a cash settlement of an opening liability to current expense again.
- Closing liability for each authority = opening liability + this period's employee amounts withheld + this period's employer liability - supported remittances - legally supported credits.

Salary must be paid in legal currency; art. 123 permits cheque or bank payment by agreement and prohibits substituting goods or vouchers for salary. The recipient is the worker or their written, revocably authorized recipient under art. 124. Foreign-currency clauses and actual foreign-currency settlements need their own legal and conversion evidence. Never silently treat a bank USD amount as bolívares, sum currencies without conversion, or choose a convenient exchange date.

Screen foreign-currency/crypto payments for applicable transaction-tax issues and the employer's special-taxpayer status, and screen the individual's separate wealth-tax position when relevant. IGTF and wealth tax are not automatic employee payroll deductions. Current rates, thresholds, payment-channel exemptions and scope have not been confirmed here, so the old Guide's figures must not be embedded in a net-pay formula. The routing issue is retained; the unsupported numerical rules are listed at the end.

## Boundary and exception table

| Facts | Decision and boundary | Evidence needed |
|---|---|---|
| Two employers; each annual payment below the resident trigger | Aggregate all payers for the annual test and percentage. A separate personal deduction at every job is wrong. | Employee declaration and both payer estimates; Decreto 1.808 arts. 2, 4-5. |
| Exactly the resident trigger, not above it | Do not change “exceeds” into “at least”. Keep any separate annual-return obligation distinct. | Annual remuneration and LISLR art. 77 test. |
| No worker estimate | Use art. 6 employer procedure and written notification; do not waive withholding or silently elect relief. | Expected annual remuneration, calculation inputs, notification and current authority if a default relief is proposed. |
| Reduced annual tax after withholding | Preserve the negative art. 7 percentage and overwithheld amount; resolve its authorized implementation. | Revised estimate, paid-to-date figures and refund/offset authority. |
| Consultant who works under dependency | Classify actual employment before applying a professional fee presumed base. | Contract and actual working facts; LOTTT arts. 7 and 55. |
| Regular bonus with “non-salary” label | Test facts and applicable instrument; hold disputed current tax interpretation. | Terms, payment pattern and current primary judicial/administrative authority. |
| Food benefit or expense reimbursement | Test statutory benefit and receipts, including any contractual salary stipulation. Do not classify by narration alone. | LOTTT art. 105 evidence and current tax treatment. |
| Salary earned, accounting credit and bank settlement in different periods | Preserve all dates; apply the specific withholding event and contribution event separately. | General ledger credit, payroll ledger, payment and fund rules. |
| Missing risk notice, cap or current monetary instrument | Hold the affected amount; do not insert lowest risk, zero risk cost, an old minimum or an invented cap. | Current authority assessment and applicable period. |
| Public official, continuous shift, collective or special regime | Establish the applicable special rules before applying ordinary limits. | LOTTT arts. 6 and 175-177 plus the actual governing instrument. |
| Termination or partial service year | Reconcile benefits, vacation, bonus and profit participation separately from regular monthly net. | Service dates, accrued guarantees, final wage bases, amounts previously paid and statutory comparison. |

Legal bases for the table: [LOTTT](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf), [LISLR](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf) and [Decreto 1.808](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf), at the articles identified in the preceding method.

## Worked cases

All amounts below are explicit test inputs. A number expressed in UT remains UT; it is not a claim that a particular bolívar value applies in 2026. The cash examples test payroll mechanics using already-supported assessments and an already-established base; they do not resolve the current monetary or bonus-law gaps.

### Case 1: net pay and employer cost use different deductions

Assume gross cash earnings of Bs 3,000, a valid resident withholding percentage of 2%, separately assessed employee contributions of Bs 20, 10 and 30, another authorized deduction of Bs 5, and employer-only contributions of Bs 120. These are hypothetical assessment amounts, not statutory fund rates or cap calculations. There are no other cash benefits or accruals in this example.

ISLR is Bs 60, employee contributions Bs 60 and net cash Bs 2,875. Employer cost is Bs 3,120. The combined employee/employer fund liability is Bs 180. ISLR remains a separate tax liability; the other authorized deduction has its own creditor. The arithmetic implements method step 7 and [LOTTT art. 106's separate deduction receipt](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf).

```oa-check
name: ve-payroll-cash-reconciliation
inputs:
  gross: 3000
  declared_percentage: 0.02
  employee_fund_a: 20
  employee_fund_b: 10
  employee_fund_c: 30
  other_authorized: 5
  employer_only: 120
steps:
  - islr: gross * declared_percentage
  - employee_funds: employee_fund_a + employee_fund_b + employee_fund_c
  - net: gross - gross * declared_percentage - employee_fund_a - employee_fund_b - employee_fund_c - other_authorized
  - employer_cost: gross + employer_only
  - fund_liability: employee_fund_a + employee_fund_b + employee_fund_c + employer_only
expected:
  islr: 60
  employee_funds: 60
  net: 2875
  employer_cost: 3120
  fund_liability: 180
tolerance: 1e-06
```

### Case 2: resident annual estimate becomes a percentage of gross remuneration

Assume agreed taxable remuneration of 1,200 UT for the year, the worker's express election of the art. 58 standard deduction of 774 UT, no dependants or prior credits, and the personal rebate of 10 UT under art. 59. The art. 50 first bracket applies at 6% up to 1,000 UT of taxable enrichment: the source says “Por la fracción comprendida hasta 1.000,00”. Taxable enrichment is 426 UT, tax before rebate 25.56 UT and annual estimated tax 15.56 UT. The percentage is 15.56 / **1,200**, or 1.2966666667%. A subsequent payment of 100 UT attracts 1.2966666667 UT withholding.

These specific figures come from [LISLR arts. 50, 58-59, including the original tariff on printed page 13](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf); the threshold and percentage method come from [Decreto 1.808 arts. 2 and 4-5](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf). This elected-deduction example does not establish an automatic election under art. 6.

```oa-check
name: ve-payroll-resident-percentage
inputs:
  annual_remuneration_ut: 1200
  elected_deduction_ut: 774
  first_band_rate: 0.06
  personal_rebate_ut: 10
  next_payment_ut: 100
steps:
  - taxable_ut: annual_remuneration_ut - elected_deduction_ut
  - tax_before_rebate_ut: (annual_remuneration_ut - elected_deduction_ut) * first_band_rate
  - annual_tax_ut: (annual_remuneration_ut - elected_deduction_ut) * first_band_rate - personal_rebate_ut
  - percentage: ((annual_remuneration_ut - elected_deduction_ut) * first_band_rate - personal_rebate_ut) / annual_remuneration_ut * 100
  - next_withholding_ut: next_payment_ut * ((annual_remuneration_ut - elected_deduction_ut) * first_band_rate - personal_rebate_ut) / annual_remuneration_ut
expected:
  taxable_ut: 426
  tax_before_rebate_ut: 25.56
  annual_tax_ut: 15.56
  percentage: 1.2966666667
  next_withholding_ut: 1.2966666667
tolerance: 1e-06
```

### Case 3: two payers do not each grant a complete annual deduction

Assume the same worker and annual tax of 15.56 UT from case 2, but two employers each estimate 600 UT annually and each pays 50 UT in the current period. Combined remuneration is 1,200 UT, exceeding the art. 2 trigger even though neither employer alone pays that much. Each receives the same valid 1.2966666667% declaration. Each withholds approximately 0.6483333333 UT before currency/rounding implementation, for a combined 1.2966666667 UT. Splitting the annual deduction into two complete claims would distort the result. Source: [Decreto 1.808 arts. 2, 4-5](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf).

```oa-check
name: ve-payroll-two-employers
inputs:
  payer_a_annual_ut: 600
  payer_b_annual_ut: 600
  annual_tax_ut: 15.56
  payer_a_current_ut: 50
  payer_b_current_ut: 50
steps:
  - combined_annual_ut: payer_a_annual_ut + payer_b_annual_ut
  - payer_a_withholding_ut: payer_a_current_ut * annual_tax_ut / (payer_a_annual_ut + payer_b_annual_ut)
  - payer_b_withholding_ut: payer_b_current_ut * annual_tax_ut / (payer_a_annual_ut + payer_b_annual_ut)
  - combined_current_withholding_ut: (payer_a_current_ut + payer_b_current_ut) * annual_tax_ut / (payer_a_annual_ut + payer_b_annual_ut)
expected:
  combined_annual_ut: 1200
  payer_a_withholding_ut: 0.6483333333
  payer_b_withholding_ut: 0.6483333333
  combined_current_withholding_ut: 1.2966666667
tolerance: 1e-06
```

### Case 4: annual revision subtracts actual withholding and remuneration to date

Assume revised annual tax is 300 UT, withholding already made is 120 UT, annual remuneration is now estimated at 3,600 UT and 1,800 UT has been received. Tax remaining is 180 UT and remuneration remaining 1,800 UT, so the revised percentage is 10%; a further payment of 200 UT attracts 20 UT. If instead the revised annual tax were 100 UT, the same history produces overwithholding of 20 UT and a **negative** percentage of -1.1111111111%. Preserve that sign in the working paper; do not infer an immediate cash-refund authorization. Source: [Decreto 1.808 art. 7](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf).

```oa-check
name: ve-payroll-revised-estimate
inputs:
  new_annual_tax_ut: 300
  already_withheld_ut: 120
  annual_remuneration_ut: 3600
  already_received_ut: 1800
  next_payment_ut: 200
  alternative_annual_tax_ut: 100
steps:
  - remaining_tax_ut: new_annual_tax_ut - already_withheld_ut
  - remaining_remuneration_ut: annual_remuneration_ut - already_received_ut
  - revised_percentage: (new_annual_tax_ut - already_withheld_ut) / (annual_remuneration_ut - already_received_ut) * 100
  - next_withholding_ut: next_payment_ut * (new_annual_tax_ut - already_withheld_ut) / (annual_remuneration_ut - already_received_ut)
  - alternative_excess_ut: already_withheld_ut - alternative_annual_tax_ut
  - alternative_percentage: (alternative_annual_tax_ut - already_withheld_ut) / (annual_remuneration_ut - already_received_ut) * 100
expected:
  remaining_tax_ut: 180
  remaining_remuneration_ut: 1800
  revised_percentage: 10
  next_withholding_ut: 20
  alternative_excess_ut: 20
  alternative_percentage: -1.1111111111
tolerance: 1e-06
```

### Case 5: nonresident employee versus genuine independent professional

Assume Venezuelan-source gross payment of Bs 50,000 and established nonresident status, with no applicable treaty override. Employment withholding is 34% of the full payment: Bs 17,000 and net Bs 33,000. A genuinely independent, noncommercial professional within LISLR art. 39's presumed-base branch would instead have presumed income of 90%, or Bs 45,000, and tax at 34% of Bs 15,300, leaving Bs 34,700 before other obligations. The technical-assistance/services branch in art. 41 requires separate classification. Misapplying the professional branch to this employee underwithholds Bs 1,700. Sources: [Decreto 1.808 art. 3](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf); [LISLR arts. 39, 41 and 50](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf).

```oa-check
name: ve-payroll-nonresident-classification
inputs:
  gross: 50000
  nonresident_rate: 0.34
  professional_presumed_fraction: 0.9
steps:
  - employee_tax: gross * nonresident_rate
  - employee_net: gross - gross * nonresident_rate
  - professional_base: gross * professional_presumed_fraction
  - professional_tax: gross * professional_presumed_fraction * nonresident_rate
  - professional_net: gross - gross * professional_presumed_fraction * nonresident_rate
  - employee_shortfall_if_misclassified: gross * nonresident_rate - gross * professional_presumed_fraction * nonresident_rate
expected:
  employee_tax: 17000
  employee_net: 33000
  professional_base: 45000
  professional_tax: 15300
  professional_net: 34700
  employee_shortfall_if_misclassified: 1700
tolerance: 1e-06
```

### Case 6: monthly salary already contains the ordinary holiday

Assume a lawful ordinary daytime monthly salary of Bs 6,000, an eight-hour ordinary shift, four authorized overtime hours on separate ordinary working days and one distinct full holiday worked. There is no night work or higher contractual premium, and all statutory scheduling conditions are met. The example assumes minimum-wage compliance has been checked; it does not establish the current minimum. Daily wage is Bs 200, hourly Bs 25, overtime Bs 150 and extra holiday-work pay Bs 300. Gross is Bs 6,450. The monthly Bs 6,000 already contains the ordinary holiday entitlement; adding another Bs 500 for that holiday would count its ordinary Bs 200 twice. Sources: [LOTTT arts. 113 and 118-120, with arts. 178 and 182 authorization conditions](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf).

```oa-check
name: ve-payroll-time-premiums
inputs:
  monthly_wage: 6000
  monthly_divisor: 30
  ordinary_daily_hours: 8
  authorized_overtime_hours: 4
  overtime_multiplier: 1.5
  holiday_days_worked: 1
  additional_holiday_multiplier: 1.5
steps:
  - daily_wage: monthly_wage / monthly_divisor
  - hourly_wage: monthly_wage / monthly_divisor / ordinary_daily_hours
  - overtime_pay: monthly_wage / monthly_divisor / ordinary_daily_hours * authorized_overtime_hours * overtime_multiplier
  - holiday_addition: monthly_wage / monthly_divisor * holiday_days_worked * additional_holiday_multiplier
  - gross: monthly_wage + monthly_wage / monthly_divisor / ordinary_daily_hours * authorized_overtime_hours * overtime_multiplier + monthly_wage / monthly_divisor * holiday_days_worked * additional_holiday_multiplier
expected:
  daily_wage: 200
  hourly_wage: 25
  overtime_pay: 150
  holiday_addition: 300
  gross: 6450
tolerance: 1e-06
```

Retain the old regression families as controls, without importing their unsupported inputs: low salary plus separately paid benefits; medium salary and capped contributions; annual income crossing a tariff boundary; family rebates; employer cost; nonresident fees. The current first-bracket, two-payer, recalculation and classification cases show the correct method. Rebuild any higher-bracket calculation from the current annual PIT working, and compute each contribution under its own cap. A higher gross amount cannot justify applying a percentage to uncapped gross. Test exactly-at/just-above thresholds, tariff continuity, a changed UT instrument, an unresolved benefit, a stale unit and a mixed-currency payment before release. Stale or missing authority must block the affected result.

## When to refuse or refer

Stop the affected calculation, state the missing evidence and produce a partial working paper with a visible unresolved item when:

- Gross pay, employment classification, worker identity, tax residence, applicable period or currency is missing. Do not reverse-engineer a statutory gross wage solely from the bank net.
- The applicable UT, minimum-wage/benefit instrument, FX rule, fund assessment, cap or calendar cannot be established. Do not default to the prior year, the lowest risk rate or zero.
- A bonus's current tax treatment depends on inaccessible judicial or administrative authority. Document the competing statutory texts and obtain the controlling current primary source; do not settle it by repeating a secondary summary.
- A purported independent professional actually works under dependency, or a nonresident/treaty position is unsupported. Hold the classification and explain its calculation effect.
- The proposed withholding relief lacks an employee election, qualifying family evidence or valid prior-credit support. Explain the art. 6 procedure rather than inventing a favourable election.
- A revised estimate is negative, the remaining-remuneration denominator is zero, the worker has left, or an employer cash refund/offset is proposed without the governing procedure. Preserve the arithmetic and refer the implementation.
- A payment, return or amendment has not been approved by the responsible employer. A prepared packet and a calculation are not authorization to submit or transfer funds.

Do not submit fabricated nil returns, omit a known worker or fund, hide a disputed earning, describe an unresolved contribution as paid, or certify a filing from a screenshot without an authority acknowledgement. Do not describe this source-cited draft as accountant-approved; the earlier approval covers only the archived version.

## Filing and payment

### Employee information, payslip and annual certificate [Decreto 1.808 arts. 4, 24-25](https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf)

“AR-I” is a useful legacy search label for the employee's estimate and percentage; “AR-C”, “ARC” and “comprobante de retención” are useful search labels for the employee's withholding record. The opened decree requires information and receipts but does not itself establish those current form names, numbers or field versions. Preserve the authorized form actually used; do not manufacture a current portal form from the label.

1. Collect the annual employee declaration, all-payer estimate, election, family and prior-credit evidence. Check the presentation timing and document each replacement percentage.
2. Produce an itemized pay receipt separating each salary/benefit item and deduction under LOTTT art. 106; retain delivery evidence. This is distinct from an income-tax certificate.
3. For each withholding, provide the art. 24 receipt showing the paid/credited amount and amount retained. Link it to the same worker, event and payroll entry.
4. The last withholding receipt of the worker's fiscal year includes the sum paid and total withheld; reconcile it to the cumulative payroll ledger and annual-return handoff. Do not confuse the separate Chapter III cessation rule with the employment Chapter II certificate.
5. Preserve the authorized processing media and programs while the tax remains unprescribed under art. 25. Do not invent a fixed universal retention period.

LOTTT art. 106 also addresses the evidential consequence of missing pay receipts. Source: [INCRET text](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf). Keep salary receipts, employee declarations, withholding certificates, tax remittances and fund receipts as distinct documents with matching totals.

### Employer tax remittance packet [LISLR arts. 83-84 and 196](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf)

SENIAT administers ISLR. Current Portal Fiscal access, form number, field schema, upload format, nil-reporting implementation, ordinary/special taxpayer deadlines and authorized payment route must be established from the current authority instructions before submission. Direct authority access and ordinary-browser/archive attempts did not establish those current instructions in this review. An old hard-coded “XML” or numbered planilla is not a verified interface.

Decreto 1.808 art. 21 expressly permits the Administration to change deadlines. Do not present its printed 1997 ordinary remittance period as a verified 2026 deadline, or its art. 23 annual relation as the complete current electronic reporting regime. Likewise, do not turn a historical transition date into a recurring annual filing duty. The current administrative source gap is retained at the end; prepare the packet without inventing a due date.

Once the applicable authority instructions are obtained, work in this order:

1. Match the employer RIF, taxpayer classification and withholding period to the current calendar and notice. Identify payment/credit events, not just bank withdrawals.
2. Reconcile the payroll export by worker identity, gross paid/credited, agreed tax base, percentage, tax retained, reversals and certificate. Include every operation the actual reporting rule requires, including zero-withholding operations or nil periods if required; do not infer their exclusion from a zero tax total.
3. Map that reconciliation to the current authority's form/field specification. Save the schema/version and confirm period and totals in the portal preview. A local spreadsheet column is not a portal box number.
4. Obtain employer approval, submit through the authorized portal and retain its acknowledgement, reference, period, timestamps and declared totals. A successful local file export is not submission.
5. Remit through the authority's authorized collection route by the applicable deadline, using the generated reference. Match bank settlement to the authority receipt and correct an unpaid or rejected submission.
6. Reconcile remitted amounts to the tax liability, issue any corrected worker certificate through the proper procedure and retain the evidence packet. Distinguish declared, accepted, paid and allocated status.

Annual employment withholding is an advance against annual tax under LISLR art. 83, not necessarily final settlement. The resident annual-return rule in art. 77 and nonresident return duty in art. 79 are separate from employer withholding. Do not promise a universal March deadline, nonextendability or a fixed instalment schedule without the current implementing rule and taxpayer classification. Source: [LISLR arts. 77, 79 and 83](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf).

### Penalties and interest: identify the breach first [COT arts. 27, 66, 103, 108, 110-115 and 121](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf)

An employer holding workers' withheld taxes is not in the same position as an ordinary taxpayer paying its own tax late. Start with the agent-specific provision; do not use the ordinary late-tax formula as a universal payroll remittance penalty. Article 27 distinguishes liability after withholding from failure to withhold and unauthorized withholding.

| Breach | Statutory branch and conditions | Exact anchor and source |
|---|---|---|
| Failure to withhold | Art. 115(1): 500% of tax not withheld. Apply the agent-specific facts, not a generic underpayment range. | “quinientos por ciento”; [COT art. 115](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Withholding less than required | Art. 115(2): 100% of the shortfall. Identify correct tax and actual withholding separately. | “cien por ciento”; [COT art. 115](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Late remittance by withholding agent | Art. 115(3): 5% per day up to 100 days; beyond that or during verification/fiscalisation, the provision routes to item 4 and art. 121. The named public bodies have their own statutory exceptions. | “por cada día de retraso en su enteramiento”; [COT art. 115](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Nonremittance | Art. 115(4): 1,000% of retained amounts not remitted; read its public-body exceptions and art. 121's criminal branch. Do not describe a payment after enforcement as ordinary timely correction. | “un mil por ciento”; [COT arts. 115 and 121](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| No return or delay exceeding a year | Art. 103 specifies a 10-continuous-day closure where there is an establishment and a 150-times penalty using the highest official BCV currency reference. Different formal communications have different branches. | “ciento cincuenta (150) veces”; [COT art. 103](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Incomplete return or delay not exceeding a year | Art. 103's 100-times branch applies to its specified return breaches; do not apply it to every record or communication. | “cien (100) veces”; [COT art. 103](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Formal offence by special taxpayer | Art. 108 increases the **formal pecuniary penalties** by 200%. It is not a blanket multiplier on every material tax penalty or fund liability. | “ilícitos formales”; [COT art. 108](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Ordinary own-tax late payment | Art. 110: 0.28% per day within the first year, capped at 100%; additional 50% after a year and 150% after two years, subject to its stated timing and enforcement conditions. Do not substitute this for art. 115. | “cero coma veintiocho por ciento”; [COT art. 110](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Other omitted tax | Art. 112's general 100%-300% omitted-tax sanction has its own conditions and reductions; it is not the automatic withholding-agent sanction. | “cien por ciento ... trescientos por ciento”; [COT art. 112](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |
| Tax interest | Art. 66 uses 1.2 times the applicable BCV active rate and its monthly publication/fallback rule. The actual rate for the late period must be obtained; a fixed remembered percentage is insufficient. | “1.2 veces la tasa activa bancaria”; [COT art. 66](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf) |

A potential art. 121 criminal withholding offence needs legal advice; do not present paying a computed fine as resolving criminal exposure. Apply any relief only after verifying its conditions. For unpaid labour salary/benefits, LOTTT art. 128 has its own BCV-based interest rule; art. 130 addresses below-minimum wage differences, their incidences and interest. Do not replace those with the COT calculation. Likewise each social fund's own penalty and interest law must be checked before applying COT categories. Source: [LOTTT arts. 128 and 130](https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf).

### Working-paper columns and bank evidence

Keep the old spreadsheet workflow's traceability while separating bases and liabilities. A reproducible working paper should contain:

| Working-paper group | Required fields and control |
|---|---|
| Identity and period | Employer RIF, worker ID/RIF, residence decision, service dates, pay period, credit/payment dates and taxpayer class. |
| Gross components | Contract salary, each premium/commission/bonus/benefit, quantity, rate, currency and supporting source document. |
| Base decisions | Labour salary, normal salary, ISLR remuneration and each contribution base, with inclusion/exclusion reason and controlling source. |
| Annual tax | All-payer annual remuneration, actual/elected desgravamen, applicable tariff calculation, personal/family rebates, prior eligible credit and annual estimated tax. |
| Resident percentage | Annual tax / gross annual remuneration; latest declaration date; revisions showing tax withheld and remuneration received to date. |
| Current withholding | Current relevant payment/credit, percentage, tax retained, UT/currency conversion and rounding evidence. |
| Employee funds | Separate assessed IVSS, employment-regime, FAOV, INCES year-end and any other supported employee deductions. Do not use one aggregate gross percentage. |
| Employer funds | Separate employer liabilities, assessed base/cap/risk, current-period charge and payment period. Never subtract from worker net. |
| Benefits and provisions | Vacation, vacation bonus, utilidades, prestaciones guarantee/final comparison, deposits, interest and already-settled balances. |
| Net and cost | Gross cash, other cash benefits/reimbursements, employee deductions, net per currency, noncash benefit and employer cost. |
| Reconciliation | Opening payable + current liability - remittances - lawful credits = closing payable, by creditor. |
| Submission evidence | Portal schema/form version, current due date/source, approval, acknowledgement, generated payment reference, bank settlement and authority allocation. |
| Worker documents | Pay receipt, employee declaration, withholding certificate and year-end cumulative reconciliation, with delivery evidence. |

Bank narration is a retrieval clue, not deterministic legal classification. Preserve the old matching vocabulary and require supporting evidence:

| Bank text or document label | Search for | Do not infer |
|---|---|---|
| Sueldo, salario, nómina, payroll, dispersión | Payroll batch, contract, approved gross/net register and beneficiary list. | That the debit is gross salary or one worker's entire pay. |
| Quincena, anticipo | Applicable half-month payroll or documented advance and later settlement. | A fourteen-day interval or an extra wage expense when settling an advance. |
| Bono de guerra económica, IMI | Applicable instrument, covered worker group, date and actual bonus terms. | Universal private-sector entitlement, amount or tax exemption. |
| Cestaticket, alimentación, bono alimentario | Food-benefit scheme and statutory conditions, with actual benefit paid. | That any cash transfer with this label is outside all bases. |
| Utilidades, aguinaldo | Year-end participation calculation, advance/final reconciliation and INCES worker contribution. | A regular monthly INCES employee deduction. |
| Bono vacacional, vacaciones | Leave dates, normal-wage basis, bonus entitlement and prior leave records. | That paying cash discharges the duty to grant leave. |
| Prestaciones, liquidación, finiquito | Termination calculation, guarantee, final comparison, previous deposits and legal cause. | That every termination line is tax-exempt indemnity. |
| IVSS, TIUNA, Seguro Social | Official assessment, worker roster, covered period, payment receipt and liability reconciliation. | The risk class, a current cap or that a bank debit alone proves allocation. |
| Paro Forzoso, RPE | Employment-regime assessment and the legally applicable base and ceiling. | That its base/cap necessarily matches IVSS. |
| FAOV, BANAVIH, vivienda | Housing-fund roster, assessment, covered salary and receipt. | A housing cap copied from another scheme. |
| INCES | Employer quarterly and worker year-end schedules distinguished by legal base and payment event. | That the same percentage and deadline apply to both. |
| INPSASEL, LOPCYMAT, seguridad laboral | Actual registration, risk/prevention obligations and any assessed contribution, penalty or other payment. | Zero obligations or a routine contribution from a label alone. |
| SENIAT, ISLR, retención, AR-C | Return/withholding packet, tax period, certificates, remittance receipt and authority reference. | That the employer's own annual tax is an employee withholding payment. |
| IGTF, divisas, cripto | Underlying transaction, taxpayer/channel status and current tax instrument. | A universal worker deduction or a universal rate on every FX payment. |
| Reintegro, devolución, ajuste IVSS | Original deduction/payment, reason for correction and authority credit/refund evidence. | Current salary income or permission for an unsupported net adjustment. |

For ambiguous entries use a review status and preserve the full narration, amount, currency, counterparty and linked evidence. Do not “solve” unmatched bank items by changing the worker's gross pay or classifying every credit as salary. Reconcile the payroll batch and individual payslips to the bank, then reconcile statutory liabilities to authority receipts separately.

## Completion checklist

- Employment classification, current period, contract, hours, gross components and legal wage compliance are supported; absence of writing has not been treated as absence of employment.
- Each earning has separate labour, normal-salary, ISLR and fund decisions. Unresolved bonus interpretation remains visible and blocks the affected result.
- The resident threshold uses all-payer annual remuneration and strict “exceeds”; the annual tax working uses a current source, supported elections and qualifying family/credit facts.
- Initial/revised percentages follow the correct denominator; actual amounts to date reconcile; negative results are preserved without inventing a cash-refund process.
- Each contribution has its own current coverage, base, cap, assessment and employee/employer split. Missing assessments have not become zero or lowest-risk defaults.
- Gross-to-net, employer cost, benefit accruals and every authority liability reconcile by currency and period. There is no double counting of ordinary holiday pay, advances or opening-liability payments.
- Payslips, certificates, current filing instructions, employer approval, submission acknowledgements, payment references and allocation receipts are complete before marking the payroll released or paid. This revised Guide remains Not yet approved.

## Talk to a verified accountant

Have the responsible Venezuelan professional review the unresolved classifications, current authority inputs and employer packet before release. This revision is published as an unapproved draft; professional approval remains outstanding.

## Sources

The read dates below mean the specified law passages were actually read. Historical statutes are cited as legal instruments, not as evidence that a current portal, monetary value or calendar has been checked. The full original gazette containing LISLR has an unrelated municipal filename; the cited pages contain the actual LISLR text. The COT host's filename mentions IVA because the same complete gazette contains multiple statutes.

| Source and passages read | URL | Read on |
|---|---|---|
| LOTTT, Gaceta 6.076 Extraordinario, 7 May 2012, INCRET government publication: arts. 1-22, 55-62, 97-143, 172-183 and 190-198; employment, salary definitions, receipts, premiums, profits, benefits, hours and vacation. Exact anchors are quoted beside the relevant rules. | https://incret.gob.ve/documentos/LEY_ORGANICA_DEL_TRABAJO_LOS_TRABAJADORES_Y_LAS_TRABAJADORAS.pdf | 2026-11-11 |
| LISLR, Decreto 2.163, original Gaceta 6.210 Extraordinario, 30 December 2015, government-hosted complete gazette: arts. 1, 5, 14, 31, 39, 41, 50-60, 77, 79, 83-84 and 196. Original tariff page 13 visually checked, including first brackets omitted by text extraction. The printed art. 31 is not asserted to resolve the current judicial interpretation. | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf | 2026-11-11 |
| Decreto 1.808, original Gaceta 36.203, 12 May 1997: arts. 1-8, professional-service branch and arts. 20-25, original PDF pages 2, 3 and 6. Archived original hosted by the public University of Carabobo, not a SENIAT-hosted current manual. Historical deduction and residence wording reconciled with later LISLR. | https://www.cidtct.uc.edu.ve/wp-content/uploads/2025/05/Decreto-1808-ISLR.pdf | 2026-11-11 |
| COT, original Gaceta 6.507 Extraordinario, 29 January 2020, government-hosted complete gazette: arts. 3, 9, 27, 30, 36, 66, 103, 108, 110, 112, 115 and 121 and neighbouring provisions. Read through the web-rendered original; separate direct download returned 403. | https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf | 2026-11-11 |
| INCES Law, official INCES publication, Decreto 1.414, Gaceta 6.155 Extraordinario, 19 November 2014: arts. 47-55, especially normal-salary employer contribution, worker year-end contribution, deadlines, registration and solvency. | https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf | 2026-11-11 |

Not yet confirmed: the current currency value/effective dates of UT and its current withholding-estimate implementation; the current minimum wage, Ingreso Mínimo Integral, bono de guerra económica and cestaticket amounts, effective dates and any private-sector mandate; current judicial/administrative interpretation of employment ISLR, including regular/accidental bonuses, food benefits, exclusions and LOTTT art. 107/LISLR art. 31 interaction; current authority treatment of a missing-declaration standard-deduction election and of negative-percentage refunds/offsets; current AR-I/AR-C form versions, numbers and fields, Portal Fiscal access, upload/XML/schema specifications, electronic monthly and nil-reporting requirements, ordinary/special-taxpayer calendars, authorized receivers and payment references; annual-return due dates, extensions and instalment dates for the relevant 2026/2027 obligation; current IVSS employee/employer rates, risk classes, bases, ceilings, coverage and deadlines, RPE/Paro Forzoso rates and cap, FAOV/BANAVIH rates and alleged ceiling, workplace-risk/LOPCYMAT contribution implementation and assessments, and any pension-related employer levy; purported IVSS restructuring and its effective consequences; contribution deductibility against annual ISLR; current FX/crypto payroll conversion and IGTF scope/rates/exemptions, wealth-tax rate/threshold/scope; current numerical BCV interest rates, relief/reduction conditions and each social fund's applicable penalty/interest regime; special public-sector, industry, cross-border and collective-agreement computations beyond the cited ordinary rules. None of these unresolved figures may be filled from the earlier Guide or secondary summaries.
