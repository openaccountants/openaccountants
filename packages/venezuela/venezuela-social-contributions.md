---
name: venezuela-social-contributions
description: >
  Reconcile Venezuelan employer and worker social and parafiscal contributions
  for 2026. Provides the ordinary INCES employer and worker calculations,
  eligibility, bases and payment periods from the institution's law; IVSS
  statutory remittance, retention, arrears and specific penalties; LOPCYMAT
  employer financing, risk formula and transition limits; separate IVSS,
  unemployment and FAOV workpapers where current primary parameters remain
  unconfirmed. Covers IVSS, TIUNA, RPE, paro forzoso, BANAVIH, FAOV, INCES,
  INPSASEL, LOPCYMAT, pension contributions, salary classification, bank-payment
  matching and the distinction from ISLR and IVA. Use when reviewing payroll
  deductions, employer costs, contribution statements or ambiguous statutory
  debits. Never infer a legal base, occupational risk class, current minimum
  wage, rate, cap or payment deadline from a bank label or the prior Guide.
version: 0.2
jurisdiction: VE
tax_year: 2026
last_updated: 2026-11-11
depends_on:
  - social-contributions-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Venezuela: social and parafiscal contributions, 2026 v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Answer layer.** Compute each Venezuelan contribution separately, using its own covered persons, legal pay definition, period, ceiling and allocation between employer and worker. For an eligible INCES employer with five or more workers, the opened law supplies the ordinary method: employer contribution of 2% of normal monthly salary actually paid, remitted within five days after each quarter; workers in an entity employing five or more contribute 0.5% of annual utilidades, aguinaldos or year-end bonuses, withheld and remitted within ten days after payment. The employer contribution cannot be deducted from workers. [INCES law arts. 49-50](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=52).

**Essential limit.** Current primary IVSS general-regulation parameters, unemployment/RPE parameters, FAOV contribution parameters and the pensions-protection contribution's current operative rate/base/calendar could not all be confirmed. Keep those liabilities open rather than substitute historical defaults. The IVSS law's explicitly initial rates are not a sufficient basis to certify the current rate. LOPCYMAT supplies a statutory financing framework and transition, not evidence of a particular employer's currently payable assessed rate. This is a source-based tier-2 rewrite without an accountant approval. It retains the prior Guide's contribution, bank-classification, workpaper, onboarding and income-tax-reference topics while correcting unsupported defaults.

## Who this applies to

Use this Guide to reconcile an employer's payroll, contributions payable, worker deductions and statutory bank payments, or a worker's deductions and contribution records. Establish the employer's legal form, sector, activity, worker count, actual employment relationship, registration and assessment before calculating. A company and an independent worker do not automatically follow the same contribution route. A payment called social security is not enough to identify the regime or period.

The 2012 consolidated IVSS law covers permanent dependent workers in urban or rural employment regardless of salary, with the stated extensions for home, domestic, temporary and occasional workers and a facultative route for independent workers. Its public-person/employer coverage in art. 3 has specific benefit conditions; do not apply a private-employer table to every public worker. Art. 6 allows continuation after compulsory coverage ends, with the insured bearing both shares, reverting to the worker's share when dependent employment resumes. [IVSS law arts. 1-3, 6, Gaceta 39.912](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=4).

INCES arts. 49 and 50 have separate wording. Art. 49 covers private-sector work entities and state enterprises with their own self-managed income employing at least five workers. Art. 50 describes workers of entities employing at least five. Do not silently import an employer-sector exception into the worker paragraph, or assume that a small payroll is exempt from every registration, training, occupational-safety or other contribution duty. Other INCES obligations, including training and apprentices, require their own analysis; the contribution headcount is not an all-purpose labor-law exemption. [INCES law arts. 49-52](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=52).

LOPCYMAT applies to dependent work, public or private, profit-making or otherwise, including domestic/home/conserjería work and the stated cooperative/associative situations; its Armed Forces exception and compatible prevention provisions for independent workers must be respected. The employer-only financing rule is in art. 7. Enrollment, risk assessment, workplace prevention and money contributions are related duties but are not interchangeable transactions. [LOPCYMAT arts. 4, 6-7](https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=2).

## Rates, bands and thresholds

### Confirmed statutory parameters

Amounts in the examples below are invented workpaper inputs, not the current minimum wage or the current value of a tax unit. Each row must be read with its eligibility and operative conditions.

| Item | Rate, amount or threshold and conditions | Official source |
|---|---|---|
| INCES employer eligibility | Art. 49 private-sector work entity or state enterprise with own self-managed income, employing five or more workers | https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=52 (art. 49) |
| INCES employer contribution | 2% of normal monthly salary paid; taxable event is payment; employer bears it, no worker deduction | https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=52 (art. 49) |
| INCES employer remittance | Within five days following each quarter's end; apply governing legal time-computation rules, not an invented calendar date | https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=53 (art. 49 continuation) |
| INCES worker eligibility and contribution | Workers in entities employing five or more; 0.5% of annual utilidades, aguinaldos or year-end bonuses, withheld by entity | https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=53 (art. 50) |
| INCES worker remittance | Within ten days after payment of the covered annual remuneration | https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=53 (art. 50) |
| INCES registration | Within 45 business days following constitution; supply required information | https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=54 (art. 51) |
| LOPCYMAT financing range | Employer/cooperative/other specified organization exclusively; 0.75% to 10% of each worker's salary or associate's income/rent, subject to actual risk/implementation | https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=4 (art. 7) |
| LOPCYMAT risk classes and degree framework | Classes I-V; degrees range 14-186; no automatic lowest-class assumption | https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=65 (art. 94) |
| LOPCYMAT statutory premium formula | Total salaries × assigned risk degree × 5.375 ÷ 10,000; assessment/operative requirements still apply | https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=67 (art. 95) |
| LOPCYMAT monthly payment provision | Accrues for completed months from worker entry; first five business days of each month, subject to transition/actual implementation | https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=68 (art. 98) |
| IVSS registration infringement | Law identifies failure to enroll workers within three business days after entry as serious; employer-registration wording separately concerns before activity begins | https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=11 (art. 86) |
| IVSS classified formal fines | Minor 25 U.T.; serious 50 U.T.; very serious 100 U.T., within arts. 85-87 conditions and case procedure | https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=11 (arts. 85-87) |
| IVSS late-contribution special fine | Five U.T. per week per affected worker, maximum 52 weeks; recidivism closure five days | https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=11 (art. 88) |
| IVSS recidivism under art. 87 | Minor/serious fine plus 50%; very serious closure three days; distinct from art. 88 | https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=11 (arts. 85, 87-88) |

The previous table's monetary ceilings derived from an alleged current minimum wage are not confirmed here. Neither an old statutory minimum nor a food/bonus “economic floor” is an interchangeable contribution base. The apparent smallness of a nominal bolívar payment cannot establish compliance. An institution's valid assessment and payroll records must be reconciled even where a statutory rate appears familiar.

### Risk degree table: what the LOPCYMAT statute actually supplies

The table below is the statutory framework, not an individualized assessment. Art. 94 requires a motivated resolution based on the listed actuarial/statistical/financial/demographic/epidemiological criteria and consultation. Art. 96 requires the special regulation and placement by the Treasury following INPSASEL qualification; first enrollment or the stated activity changes use the average of the **correct class**, not automatically class I. Art. 97 generally follows the principal activity; separate centers may seek separate placement only on its conditions. [LOPCYMAT arts. 94-97](https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=65).

| Risk class | Minimum degree | Weighted average degree | Maximum degree | Official source |
|---|---|---|---|---|
| I, minimum | 14 | 21 | 28 | https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=66 (art. 94) |
| II, low | 21 | 35 | 49 | https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=66 (art. 94) |
| III, medium | 35 | 64 | 93 | https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=66 (art. 94) |
| IV, high | 64 | 93 | 122 | https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=66 (art. 94) |
| V, maximum | 93 | 102 | 186 | https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=66 (art. 94) |

Art. 97's annual qualification adjustment is limited to its printed “veinticinco décimas (0,25)” of the company's current rate and to art. 7's outer limits. Retain that wording with an actual assessment; do not repair or reinterpret its terminology into an invented percentage-point rule. The current implementing risk resolution, Treasury operation and actual employer rate are not yet confirmed. [LOPCYMAT arts. 96-99](https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=67).

## The base

### The method, step by step

1. **Identify each obligation.** Create separate accounts for IVSS compulsory/facultative coverage, unemployment/RPE, FAOV housing, INCES employer, INCES worker, occupational-safety contributions and a pensions-protection contribution where legally applicable. Separately identify ISLR withholding, own ISLR, IVA and other taxes. Do not collapse every payment to a government recipient into a social contribution.
2. **Establish the persons and period.** Reconcile the actual employer, work relationships, hires/leavers, sector, activity, worker count and pay dates against contracts and official records. A worker's independent invoice is not proof that employment rules do not apply, and a worker count on one bank-payment day is not proof of every period's eligibility. The current administrative headcount method for changing/irregular staffing is not established here; obtain the actual primary instruction rather than average or round without authority.
3. **Classify compensation by obligation.** Build a pay-component matrix with normal recurring salary, variable remuneration, overtime/commissions, in-kind remuneration, vacation pay/bonus, utilidades, aguinaldo/year-end bonus, food benefit, travel reimbursements, Guerra Económica and other bonuses separately. For each contribution identify the legal base, evidence, exclusions and any current interpretation. INCES employer normal monthly salary and INCES worker annual-remuneration bases are distinct. IVSS law art. 60 permits institution determination of variable/in-kind remuneration. [INCES arts. 49-50](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=52); [IVSS law arts. 58-60](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=8).
4. **Apply only established ceilings and periods.** Record each regime's actual cap, statutory reference wage, effective dates, weekly/monthly convention and assessment. Never borrow one regime's cap for another. A constant monthly salary does not prove each monthly invoice has an identical contribution amount. The IVSS general regulation and RPE/FAOV texts needed to confirm current numerical parameters remain unavailable through the permitted routes; do not finalize those amounts from the old Guide.
5. **Calculate ordinary INCES.** For an art. 49 employer, sum legally classified normal monthly salaries actually paid in the quarter and multiply by 0.02. Do not deduct that sum from workers. For an art. 50 worker contribution, multiply legally identified annual utilidades/aguinaldo/year-end bonus actually paid by 0.005; deduct the worker share and record the employer's remittance payable. Determine all covered workers and amounts, rather than applying the rate only to a single bonus line that happens to match a bank description. [INCES arts. 49-50](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=52).
6. **Keep INCES relief separate.** Arts. 57-61 concern deductions for training/collective self-formation programs, subject to regulation, qualifying costs, prior Board approval, self-assessment and presentation in the first six months, with programmes to be executed in the year following presentation. Do not net all training expenditure against the contribution or invent a relief percentage. Current permitted percentage, regulation, application and approval details are not yet confirmed. [INCES arts. 57-61](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=59).
7. **Reconcile IVSS retention/remittance.** The employer must remit its own and workers' contributions on the law/regulation's conditions. Art. 63 allows withholding the worker part when salary is paid and prohibits later recovery if not withheld then; payment of salary creates the stated presumption of withholding. Do not treat a missed withholding as authority to deduct an arbitrary arrears lump sum from the next wage. [IVSS law arts. 61-64](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=9).
8. **Apply the occupational-safety limit.** Keep art. 95's mathematical risk formula with the actual assigned degree and established salary base, but first determine operative implementation/transition and whether the charge is already in another social-insurance assessment. The old assertion that LOPCYMAT always means no regular monetary obligation is not established; neither is an automatic additional payment at the statutory minimum. [LOPCYMAT arts. 7, 94-99, transitional fifth, final second](https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=4).
9. **Match the payment, not just its label.** Reconcile beneficiary/account, official payment order, contribution period, salary/worker detail, principal, interest, fine and bank reference. Split a combined remittance into its legal components. A bank payment proves a cash movement; the institution's account allocation proves the period credited. Keep refunds/reversals and employee reimbursement receipts distinct from original expense and payable movements.
10. **Close the liabilities with an exception list.** Compare opening payable plus employer expense plus worker amounts withheld plus separately assessed charges less payments actually allocated and valid credits. Document all unresolved differences, payroll adjustments and official rectification steps. Do not label the employer solvent solely because the bank balance reconciles or all visible government debits have a classification.

### Salary, integral salary and benefits: do not reuse a single base

The old Guide correctly treated salary payments as a different cash-flow category from contributions paid, but went further and automatically excluded Cestaticket and Guerra Económica from every base. That result cannot follow from a bank label. A legally nonsalary benefit under one enactment does not settle the definition in every contribution statute. The current pensions-protection regime also needs its own primary-text analysis before assuming the same exclusions. Record the legal pay category and the specific inclusion/exclusion for **each** obligation.

For INCES employer contributions, the law expressly says **salario normal mensual pagado**; it does not say every gross cash payment. For its worker contribution it identifies utilidades, aguinaldos and year-end bonuses. A vacation bonus should not be moved into the annual-bonus base merely because both are called BONO; first establish its actual legal category. The law's opened arts. 49-50 give no numeric salary ceiling in those paragraphs. Do not import a minimum-wage multiplier into their formulas. That observation does not certify the absence of every subsequent administrative or judicial rule. [INCES arts. 49-50](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=52).

For IVSS, art. 58 uses the insured's earned salary or the limit set in the regulation for contributions and cash benefits. Art. 59 delegates the percentage and allows the stated category/regional distinction; art. 60 permits institution determination for variable and in-kind pay. The 2012 Gazette's arts. 65-67 explicitly describe **initial** contributions and possible changes. They do not resolve today's risk-class rates, ceiling, week convention or the claimed February-2025 change. Current general-regulation and later administrative text are needed for those parameters. [IVSS law arts. 58-67, 78](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=8).

FAOV's old text contains two inconsistent claims: a minimum-wage-multiplier cap in its table/rule/workpaper and an uncapped integral base in an example. Neither is adopted here without the actual current law. Preserve the workpaper's housing section and component-by-component base analysis, but leave the operative rate, cap/no-cap, integral-salary composition and remittance calendar **not yet confirmed**. The same applies to RPE's exact rate split, salary ceiling, period and remittance instruction. A consistent-looking calculation is not corroboration of its legal parameters.

### Payment pattern library

Use these as search clues and provisional coding only. They are not legal conclusions or guaranteed bank formats. Retain original unnormalized text alongside any accent/case normalization, account identifier and matching evidence.

| Bank description clue | Provisional route | Evidence needed before final coding |
|---|---|---|
| IVSS, SEGURO SOCIAL, SEGUROS SOCIALES, SSO, TIUNA | Social-insurance remittance candidate | Official order/account, employer registration, period, workers, principal/interest/fine split |
| PARO FORZOSO, RPE, REGIMEN PRESTACIONAL DE EMPLEO | Unemployment regime candidate | Agency allocation and return; establish whether included in a combined payment |
| FAOV, BANAVIH, LEY POLITICA HABITACIONAL, LPH | Housing contribution candidate | Distinguish contribution from mortgage payment, loan disbursement, refund, arrears or fine |
| INCES, INCE | Training contribution candidate | Employer quarter vs worker annual remuneration; payment date and covered entity/workers |
| LOPCYMAT, INPSASEL | Occupational-safety related candidate | Assessment and reason; contribution, sanction, training/service charge or another transaction |
| SENIAT, ISLR, IMPUESTO SOBRE LA RENTA | Income tax/withholding candidate | Return/certificate and actual tax account; may also be a separately identified pension-related tax |
| IVA, IMPUESTO AL VALOR AGREGADO | VAT candidate | VAT return/assessment; never count automatically as a payroll contribution |
| RETENCION, RETENCION ISLR | Withholding candidate | Recipient, legal tax, period, certificate and remittance; word alone does not identify a rate |
| NOMINA, SUELDO, SALARIO outgoing | Salary cash payment candidate | Payroll gross-to-net bridge; contribution/withholding deductions occur in separate liabilities |
| CESTATICKET, CESTA TICKET, CESTATICKET SOCIALISTA | Food-benefit payment candidate | Governing benefit documents and each regime's actual base rule; no universal exclusion |
| BONO DE GUERRA, BONO CONTRA LA GUERRA ECONOMICA | Named bonus candidate | Payer, entitlement, legal classification and contribution-specific rule |
| UTILIDADES, AGUINALDO, BONIFICACION FIN DE AÑO outgoing | Annual-remuneration candidate | INCES art. 50 eligibility/base, actual annual payment and retention records |
| IVSS PENSION, PENSION DE VEJEZ incoming | Pension/benefit receipt candidate | Award/payment record; not an employer contribution payment solely because IVSS appears |
| PARO FORZOSO PAGO, PRESTACION DESEMPLEO incoming | Unemployment-benefit receipt candidate | Benefit record; do not net against employer contribution expense without legal/accounting basis |

A refund or returned transfer may appear as a credit from the institution. The old “always debits, never credits” assertion is removed: check direction and substance. A tiny debit may be a real contribution, bank fee, test transfer or erroneous short payment. A large debit may combine arrears, more workers, periods or assessed sanctions. Size is not a safe classifier. Exact bank export layouts and automated description reliability have not been confirmed for Banco de Venezuela, Banesco, Mercantil or BBVA Provincial.

### Working paper and onboarding fallback

Maintain a workbook with raw statement, payroll by worker, pay-component/legal-base matrix, assessments/returns, liability rollforward and unresolved-items tabs. Minimum fields are employer/RIF/registration, worker ID in the protected workpaper, hire/leaving dates, period, actual pay date, gross component, normal-pay classification, each regime's established base, cap/reference and effective date, actual risk class, employer/worker rates and amounts, withholding, institution reference, payment date, cash amount, credited amount, interest, fine and remaining balance. Keep private payroll identifiers out of public review evidence.

| Workpaper column or equation | Purpose |
|---|---|
| `regime`, `employer`, `worker_or_group`, `period`, `paid_date` | Establish which duty/period is being reconciled |
| `gross_component`, `legal_character`, `base_rule_source`, `included_amount` | Explain each contribution base; a bonus label is not an exclusion |
| `validated_reference_wage`, `cap_rule`, `cap_effective_date` | Store only a confirmed cap for the specific regime; FAOV cap status remains open |
| `normal_salary_paid_quarter` | Sum qualifying INCES employer monthly salaries actually paid in that quarter |
| `inces_employer = normal_salary_paid_quarter * 0.02` | Art. 49 qualifying employer's liability; employer bears it |
| `covered_annual_bonus_paid`, `inces_worker = covered_annual_bonus_paid * 0.005` | Art. 50 qualifying worker retention and remittance liability |
| `ivss_assessed_base`, `ivss_assessed_period`, `ivss_assessed_employer_rate`, `ivss_assessed_worker_rate` | Inputs await current primary verification; do not reverse-engineer from net pay |
| `rpe_assessed_base`, `rpe_rates`, `rpe_period` | Separate unemployment inputs, pending source verification |
| `faov_established_integral_base`, `faov_rates`, `faov_cap_status` | Separate housing computation, pending current primary law |
| `lopcymat_assigned_degree`, `implementation_evidence`, `assessed_base` | Mathematical statutory scenario is not evidence of an actually due charge |
| `opening + employer_expense + worker_withheld + assessed_charges - allocated_payments - valid_credits = closing` | Reconcile liability; refunds/reclassifications require their own entries |

Where onboarding documents are incomplete, assemble employer registration, official latest account/payment orders, recent payroll and pay-component evidence, worker register, annual-bonus records, prior return/assessment, bank statements and posted allocations. Produce a provisional exception report. Do not divide the latest IVSS debit by a presumed combined percentage to “infer salary”, choose the lowest risk class, or classify every unrecognized statutory payment as employer expense. A combined payment includes workers' withheld liabilities as well as employer costs. Posting the full payment again as employer expense double counts the worker share and may duplicate an expense already accrued.

## Deadlines and filing

The INCES employer quarter and worker-bonus clocks differ. Determine the actual pay date and applicable contribution before choosing a deadline. Art. 49 says five days following the quarter's expiry; art. 50 says ten days following annual-remuneration payment. The registration paragraph explicitly says 45 **business** days following constitution. For national tax duties, COT arts. 1/10 supply the general counting rule: day periods are business days unless the law says continuous days; a deadline falling on an administrative nonbusiness day extends to the next business day. The business calendar is that of the tax administration, including the stated closed-office and collection-bank conditions. Keep the actual official calendar and any specific contrary provision; the contribution paragraphs do not by themselves establish a calendar-date deadline. [INCES arts. 49-51](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=52); [COT arts. 1, 10](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=3).

An INCES solvency certificate states compliance as of its issue date with training/self-formation, apprentices and tax duties; the law makes it indispensable for state contracting and labor solvency. Verify actual certificate status and underlying duties rather than treating the latest contribution receipt as the certificate. The current RNCP portal and procedural forms, account numbers, actual holiday calendar and electronic correction workflow are not confirmed by reading the statute alone. [INCES art. 52](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=54).

IVSS law arts. 61-62 require employer/worker shares to be remitted on the law/regulation's timetable. Current IVSS assessment frequency, weekly conversion convention, monthly remittance date and later instructions remain not yet confirmed. The current IVSS institutional employer page states a registration instruction, but its wording is not a substitute for the actual regulation; where it differs from the opened statute's employer-registration infringement, retain the statute and refer the procedural point for primary confirmation. Do not infer an extension, grace period or solvency from a successful bank transfer. [IVSS law arts. 61-62, 85-90](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=9); [IVSS employer information](https://www.ivss.gov.ve/empleador/informacion-general).

LOPCYMAT art. 6 sets enrollment and hire/leaving notifications within three business days in its Treasury framework. Art. 98 sets the monthly completed-period/first-five-business-day provision. Transitional fifth says employers continue IVSS contributions on the existing laws' conditions until the Treasury is created; final second defers specified cash benefits until its operation. Neither clause proves the Treasury's actual current operation or this employer's current assessed contribution. Confirm operative implementation and authority before paying a second occupational charge or asserting no payment exists. [LOPCYMAT art. 6, art. 98, transitional fifth, final second](https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=3).

The RPE/FAOV return and payment timetables, current payroll-withholding remittance calendar, special-taxpayer advance calendar, pensions-protection contribution and current portal/forms are separate open items. A SENIAT special-taxpayer designation does not, without the governing primary rule, prove an uplift or a different calendar for every institution. Preserve the designation and actual relevant notices in the case workpaper.

## Penalties and interest

### IVSS has specific statutory rules

IVSS law art. 62 requires arrears interest without prior demand, based on the BCV active average rate valid when the breach occurs; it still accrues where effects of the act are suspended administratively or judicially. Do not substitute an old fixed monthly percentage or today's exchange rate. Separate the unpaid contribution, governing interest periods/rates and any assessed fine. Current BCV figures, detailed accrual method and actual collection order are not yet confirmed here. [IVSS law art. 62](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=9).

Arts. 85-87 classify infringements and specify fines: minor 25 U.T., serious 50 U.T. and very serious 100 U.T. The statute provides a separate infringement for each affected insured/worker except documentary duties that can be treated as collective; art. 85 states valuation by the UT at the offense and defines recidivism within three years following the firm resolution/judgment for the same classification. For recidivism, art. 87 adds 50% to minor/serious fines and gives three-day closure for very serious cases. Preserve actual offense, affected-person count, dates and procedure; no current currency fine is supplied without the legally applicable official unit/valuation analysis. [IVSS law arts. 85-87](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=10).

Art. 86 distinguishes employer registration before activity, worker enrollment within three business days of entry, employment/salary information, personnel records, excess retentions, obstruction and altered documents. Do not label every mismatch the same offense. Art. 88 separately treats failure to remit contributions: five U.T. per week per affected worker, capped at 52 weeks, without prejudice to arts. 86-87; recidivism carries five-day closure. Art. 89 says sanctions do not discharge contribution/other arrears and interest. [IVSS law arts. 86-89](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=11).

Art. 90 refers collection/sanction procedure to the COT only insofar as it does not contradict the social-insurance law/regulation and supplies special procedure. Therefore the old blanket “IVSS arrears receive all COT formal fines plus a special-taxpayer increase” is not a completed legal conclusion. Identify the specific applicable offense and controlling special rule, not only the entity's tax designation. Current judicial application, subsequent amendments and actual authority assessment need confirmation where not established by the opened texts. [IVSS law arts. 85-90](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=10).

### INCES and LOPCYMAT must be analyzed separately

INCES art. 55 subjects breach of its tax duties to the COT; art. 56 addresses liquidation/payment under its law and COT. Arts. 53-54 concern training/apprentice duties and their separate sanctions/enforcement. Do not use an apprentice sanction as a flat contribution penalty, or net a sanction against a worker's wages. The COT's duty, offense, amount, special-taxpayer application and procedural conditions must be established for the actual case. [INCES arts. 53-56](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=56).

LOPCYMAT art. 128 provides, within its contribution/affiliation framework, fines up to 100 U.T. per worker for nonaffiliation, late affiliation or inaccurate information according to gravity, without prejudice to other responsibility. It also requires unpaid contributions and interest based on the average active rate of the six principal universal banks, and full reimbursement of the specified benefits/expenses where the employer fails to affiliate or maintain contributions and the covered occupational event occurs. The Treasury applies the stated sanction. Its framework is not proof of current operational assessment, and the current UT/bank inputs remain unconfirmed. [LOPCYMAT art. 128](https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=84).

### Preserved COT tax-reference boundary

The old reference to income-tax underassessment, nonfiling, late/incomplete filing and special-taxpayer formal sanctions belongs to the relevant tax duty, not automatically every social-security arrear. In the opened 2020 COT, art. 103 distinguishes failure to file from late/incomplete returns and includes the stated closure/fine consequences; art. 108's 200% increase concerns the listed formal offenses by designated special taxpayers, not an invented universal addition to every principal/interest charge. Art. 112's omitted-tax penalty is subject to its actual conditions; arts. 110 and 115 distinguish delayed payment and retention/remittance misconduct. Apply them only after determining the offense, person, timing and governing special law. [COT arts. 103, 108, 110, 112, 115](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf).

For the retained tax-duty comparison, the following are the opened COT's actual figures. Their presence does not establish that a particular IVSS, INCES or other contribution assessment falls under that offense. In particular, special-taxpayer status does not independently turn every interest, substantive fine or institution-specific sanction into an art. 108 formal penalty.

| Tax-duty offense or condition | Statutory amount and boundary | Official source |
|---|---|---|
| No declaration or delay exceeding one year, art. 103(1) | 150 times the official highest-value-currency exchange reference; ten continuous days of establishment closure if an establishment exists; statutory branch rule applies | https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=13 (art. 103) |
| Incomplete declaration or delay no longer than one year, art. 103(3) | 100 times that exchange reference; distinguish from nonfiling beyond one year and other communication offenses | https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=13 (art. 103) |
| Chapter's formal offenses committed by designated special taxpayer | Applicable monetary sanctions increased by 200%; does not say every substantive/interest charge receives this increase | https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=14 (art. 108) |
| Illegitimate reduction of tax revenue by action/omission, including improperly enjoyed benefits | 100%-300% of omitted tax; art. 112's valuation and art. 196 exceptions remain applicable; not a flat fine on every bank difference | https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=15 (art. 112) |

Where a COT fine is expressed using the highest-value currency published by BCV, art. 91's currency rule is distinct from the IVSS statute's printed U.T. sanctions and from minimum-wage references in contribution caps. Establish the actual law and valuation before converting. A current exchange-rate/UT figure and an administrative fine schedule have not been confirmed here. A spreadsheet should show the governing unit and unresolved conversion rather than substitute one of those three reference systems for another. [COT art. 91](https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf#page=11); [IVSS law art. 85](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=10).

## Cross-border points

Determine the actual employment relationship and where services are performed before assuming foreign payroll or an offshore payer eliminates domestic coverage. IVSS law art. 2 covers dependent workers in urban/rural service irrespective of salary; LOPCYMAT art. 4 defines its territorial/work-relationship scope. The current treatment of posted workers, foreign employers, remote work, international social-security coordination, bilateral agreements, detached-worker certificates and refunds has not been confirmed here. A tax treaty or residence certificate is not itself a social-security exemption. Do not transplant another country's contribution rate or assume every foreign worker is outside local payroll. [IVSS law art. 2](https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf#page=4); [LOPCYMAT art. 4](https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=2).

Foreign-currency pay needs both documented remuneration and the specific legally applicable conversion rule. No BCV exchange-rate number, bonus dollar equivalent, minimum wage or “economic floor” is supplied here as a current parameter. Keep original currency, actual dates, legally established contribution currency/base and source alongside every conversion. A card settlement or foreign bank transfer label does not establish either salary character or the official conversion date.

### Income-tax reference retained from the old Guide

Social contributions are separate from ISLR on the worker or employer. LISLR art. 1 provides residents/domiciliaries' worldwide-income rule and nonresidents' territorial rule, with attributable-income treatment for a PE/fixed base. Art. 31's printed employment wording, and the current controlling interpretation of bonuses, need the individual income-tax analysis; do not calculate ISLR on net cash after all payroll deductions merely because it reconciles to the bank. The current individual Guide/review process must resolve the legally taxable employment amount. No generalized bonus exemption follows from this contribution Guide. [LISLR arts. 1, 31](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=4).

For an already established ordinary resident annual taxable enrichment in U.T., art. 50's Tarifa 1 is marginal. The following subtraction amounts are arithmetic derived from those bands, not contribution allowances. This retains the old reference/test topic without supplying an unsupported bolívar UT conversion. [LISLR art. 50](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13).

| Annual taxable enrichment U.T. | Marginal rate | Derived subtraction U.T. | Official source |
|---|---|---|---|
| Through 1,000 | 6% | 0 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (art. 50, visual Tarifa 1) |
| Over 1,000 through 1,500 | 9% | 30 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (art. 50) |
| Over 1,500 through 2,000 | 12% | 75 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (art. 50) |
| Over 2,000 through 2,500 | 16% | 155 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (art. 50) |
| Over 2,500 through 3,000 | 20% | 255 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (art. 50) |
| Over 3,000 through 4,000 | 24% | 375 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (art. 50) |
| Over 4,000 through 6,000 | 29% | 575 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (art. 50) |
| Over 6,000 | 34% | 875 | https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13 (art. 50) |

Resident taxable income uses the proper net-enrichment computation and the permitted personal-deduction route; art. 58's optional standard is 774 U.T., alternative to art. 57 itemization, and art. 59 personal/family reductions are applied to tax on their conditions. The old 5,000-U.T. **taxable** test gives `5000 × 0.29 - 575 = 875 U.T.`; taxable 1,000 gives `1000 × 0.06 = 60 U.T.` before personal tax reductions. Neither test says that a gross salary of the same amount has that tax. [LISLR arts. 50, 57-60](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=13).

A nonresident individual's art. 50 general proportional rate is 34% on the applicable statutory net base, subject to special categories and actual treaty rights. Art. 39 supplies a 90% presumed base for the specified noncommercial professional income, without prejudice to its technical-services rule; it is not a 90% base for every worker or foreign payment. The old 100,000-unit fee example therefore computes `100000 × 0.90 × 0.34 = 30600` only with that exact classification established. [LISLR arts. 39, 50](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=12).

The old company-tax context is also distinct from payroll: arts. 9 and 52's ordinary company Tarifa 2 applies 15% through 2,000 U.T., 22% to the next fraction through 3,000 and 34% above, on the proper net tax base. Art. 52 separately addresses net banking, financial, insurance or reinsurance enrichment obtained by domestically domiciled juridical persons/entities at 40% and arts. 11-12/53 distinguish the specified hydrocarbon regime at 50% from the specified mining royalties/participations at 60%, with detailed scope/exceptions. There is no blanket “all joint ventures pay the oil rate” rule. Use the reviewed corporate-tax Guide and actual legal entity/activity rather than calculating company tax from a statutory payroll debit. [LISLR arts. 9, 11-12, 52-53](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=6).

Annual filing, estimates, spouses, tax registrations and IVA were present in the old social Guide and remain separate checks. LISLR art. 77's annual natural-person tests use net enrichment above 1,000 U.T. or gross above 1,500 U.T., with the stated exceptions and primary-activity rule. Art. 80 authorizes the Executive to require estimated declarations for specified taxpayers exceeding the prior-year 1,500-U.T. **net** threshold and delegates the relevant regulatory bases, conditions and procedures; it does not supply a confirmed advance percentage or every administrative schedule. Art. 54's marital-community rule has its actual exceptions; do not require both property separation and a particular income category where the statute does not. Current annual calendar, extensions, instalments, special advances, RIF/forms, withholding and IVA rate/exemption details are not yet confirmed by this Guide. [LISLR arts. 54, 77-81](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=14).

## Two worked examples that recompute

### Example 1: complete ordinary INCES employer quarter and annual worker contribution

Assume a private employer continuously employing six workers satisfies art. 49, has no approved training deduction, and paid legally established normal monthly salaries totaling 30,000, 32,000 and 34,000 currency units in the three months of the quarter. The employer contribution is `96000 × 0.02 = 1920`. This is employer expense/payable, not an additional worker deduction. Separately, the same entity pays 24,000 of legally covered annual utilidades; art. 50 worker retentions total `24000 × 0.005 = 120`, giving net utilidades paid of 23,880 if no other deductions. The employer remits both liabilities on their **different** clocks; a coincident payment date does not combine the periods. [INCES arts. 49-50](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=52).

```oa-check
name: Eligible INCES employer quarter and separate annual worker contribution
inputs:
  month_one_normal_paid: 30000
  month_two_normal_paid: 32000
  month_three_normal_paid: 34000
  annual_utilidades_paid: 24000
steps:
  - quarter_normal_paid: month_one_normal_paid + month_two_normal_paid + month_three_normal_paid
  - employer_contribution: quarter_normal_paid * 0.02
  - worker_retained: annual_utilidades_paid * 0.005
  - utilidades_cash_after_inces: annual_utilidades_paid - worker_retained
  - combined_inces_payables: employer_contribution + worker_retained
expected:
  quarter_normal_paid: 96000
  employer_contribution: 1920
  worker_retained: 120
  utilidades_cash_after_inces: 23880
  combined_inces_payables: 2040
```

### Example 2: no salary cap imported into INCES, and bank allocation is reconciled

Assume the same eligible employer paid normal monthly salaries totaling 200,000 in each of three months, with no approved deduction. Annual covered year-end bonuses are separately 40,000. Employer INCES is `600000 × 0.02 = 12000`; worker retention is `40000 × 0.005 = 200`. An opening INCES liability of 500 and total cash remittances of 12,400 leave 300 payable if the institution credits the whole cash to these liabilities and there are no separately assessed interest/fines. Do not cap INCES using an unconfirmed IVSS/RPE/FAOV minimum-wage multiple; do not book the whole 12,400 as new employer expense. [INCES arts. 49-50](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=52).

```oa-check
name: INCES separate bases and liability allocation
inputs:
  monthly_normal_paid: 200000
  months: 3
  annual_covered_bonus: 40000
  opening_liability: 500
  allocated_cash: 12400
steps:
  - quarter_normal_paid: monthly_normal_paid * months
  - employer_expense: quarter_normal_paid * 0.02
  - worker_retention: annual_covered_bonus * 0.005
  - closing_liability: opening_liability + employer_expense + worker_retention - allocated_cash
expected:
  quarter_normal_paid: 600000
  employer_expense: 12000
  worker_retention: 200
  closing_liability: 300
```

### Preserved legacy bank examples with the source limit made explicit

1. **IVSS payment for a worker paid 130.** The amount 130 is only the old hypothetical pay input, not a confirmed current minimum. Match salary classification, period, official risk/rate/base/cap and order first. Because those current general-regulation parameters remain unconfirmed, no old combined-percentage answer is certified here. Preserve the calculation as `confirmed contribution base for the assessed period × confirmed employer/worker shares`, recording each share separately and the current source.
2. **FAOV for the same hypothetical pay input.** Identify housing contribution versus loan/fine; establish legally integral base and current rate/cap status before computing. The old example's uncapped answer and rule's capped answer cannot both establish current law. Leave the liability unresolved until its primary parameters are available; do not let one “successful” arithmetic result choose the law.
3. **RPE/Paro Forzoso for the same pay input.** Reconcile separate unemployment return, actual worker/employer shares, ceiling, period and any combined IVSS allocation. The old split and derived answer remain unconfirmed, not a default.
4. **Cestaticket payment of 2,080.** Code as a benefit-payment candidate, not a remittance merely because it is payroll-related. Do not automatically remove it from every contribution base; complete the component/rule matrix first. The same caution applies to Guerra Económica and another bonus with a different legal basis.
5. **SENIAT payment of 45,000.** If return/payment order identifies annual ISLR, it is income tax, not IVSS/FAOV/RPE/INCES. If a different SENIAT-administered duty is actually identified, use that duty. The recipient's name alone cannot exclude every pension-related contribution.
6. **Irregular IVSS debit of 1,250.** Do not reverse-engineer wages from a presumed percentage or apply an automatic penalty multiplier. Request/match the order/account allocation: workers, periods, principal, interest, fine and any reversal. Preserve the cash amount and unresolved classification; a large payment is not proof of arrears or an illegal deduction.

The prior test for a pay input of 2,000 with an assumed IVSS cap is preserved as an input-validation case: the actual current reference wage, cap multiplier, rate, period and legal salary base must all be sourced before computing. The old estimate using income of 70,000 divided by an unconfirmed currency value of the U.T. is replaced by `net prior-year enrichment ÷ confirmed applicable U.T.` and the actual art. 80 trigger/implementing instruction, not a guessed “required” verdict. [LISLR art. 80](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=17).

The retained small annual-bonus INCES test assumes an entity employing at least five and a covered utilidades payment of 4,000: worker retention is 20. The tax-reference tests use already established taxable enrichment, not gross salary; they do not apply personal reductions or deductions a second time. [INCES art. 50](https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf#page=53); [LISLR arts. 39, 50](https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf#page=12).

```oa-check
name: Retained annual utilidades and separate ISLR reference arithmetic
inputs:
  covered_utilidades: 4000
  resident_taxable_ut: 5000
  bottom_band_taxable_ut: 1000
  classified_nonresident_professional_gross: 100000
steps:
  - inces_worker_retention: covered_utilidades * 0.005
  - resident_tariff_ut: resident_taxable_ut * 0.29 - 575
  - bottom_band_tariff_ut: bottom_band_taxable_ut * 0.06
  - nonresident_presumed_base: classified_nonresident_professional_gross * 0.90
  - nonresident_professional_tax: nonresident_presumed_base * 0.34
expected:
  inces_worker_retention: 20
  resident_tariff_ut: 875
  bottom_band_tariff_ut: 60
  nonresident_presumed_base: 90000
  nonresident_professional_tax: 30600
```

### Statutory occupational-risk formula: a conditional scenario

Assume an actual operative assessment has already legally established the LOPCYMAT art. 95 formula, a degree of 21 and total relevant salaries of 100,000. Pure multiplication gives `100000 × 21 × 5.375 ÷ 10000 = 1128.75`. This is a conditional statutory arithmetic example, not proof of Treasury implementation, the correct class, a separate currently due charge or the proper base for a real employer. Do not select degree 21 automatically merely because it is class I's average. [LOPCYMAT arts. 94-97](https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf#page=65).

```oa-check
name: LOPCYMAT conditional assessed-degree statutory formula
inputs:
  legally_assessed_salary_total: 100000
  actual_assigned_degree: 21
steps:
  - statutory_premium: legally_assessed_salary_total * actual_assigned_degree * 5.375 / 10000
expected:
  statutory_premium: 1128.75
```

## Ask the client first

Read the existing payroll/case record before asking for missing information. Obtain only what is absent: employer/RIF/registration and sector; principal activity and actual risk assessment; worker list, employment relationships, hires/leavers and headcount by relevant period; normal and variable salary components; annual utilidades/aguinaldo/bonus payments; food/travel/other benefit legal documents; all institution payment orders, returns, statements, assessed rates/bases/caps, principal/interest/fine splits and credited periods; actual bank statements and payment references; any training deduction approval; relevant special-taxpayer notice; foreign service/work facts and claimed agreement certificate. A payroll net-cash total cannot replace these inputs.

Ask separately for actual tax returns and withholding certificates only when reconciling the retained ISLR context. Do not request personal/family residence facts merely to classify an unambiguous employer INCES payment; those facts matter when individual income tax or cross-border coverage is actually being computed. Keep confidentiality and the case's existing records in mind when collecting worker information.

### When to refuse or refer

Stop the affected numerical conclusion when a current rate/cap/base/period is unconfirmed, risk class is missing, pay classification is contested, staffing changes require an unconfirmed headcount rule, the institution's allocation disagrees with the bank, foreign coverage is claimed without primary support, or a sanction/arrears assessment cannot be mapped to the actual law. Continue the independent bookkeeping/reconciliation work that does not depend on that missing fact. Say which amount is unresolved and why; do not describe the whole payroll as compliant or solvent.

**Prohibitions retained:** no foreign-jurisdiction contribution defaults; no blanket total-pay or nonsalary-bonus base; no “lowest risk is conservative” assumption; no reverse calculation from a contribution debit to legally established salary; no automatic FAOV cap/no-cap; no tax-unit/minimum-wage/FX substitution; no double counting worker deductions as employer expense; no bank-label-only final classification; no presumed current nominal minimum or dollar “economic floor”; no automatic use of all COT tax penalties for IVSS; no certificate of solvency inferred from payment. Provisional coding must remain distinguishable from a completed legal calculation.

## Sources

Primary texts below were actually opened/read on 2026-11-11. The official INCES law book is linked from its current institutional laws page. CEBM's current regulation index links the **July** path of the IVSS Gazette, not the stale August search path. Its 14-page file contains the consolidated 2012 law and the amendment of regulation arts. 7-8, but **not** the complete current general regulation. The INCRET PDF contains LOPCYMAT; its enacted framework and transitional wording do not prove current implementing events.

| Source | Act/articles and material actually read | Exact native-language anchor | Read on | Status/limit |
|---|---|---|---|---|
| https://inces.gob.ve/documents/24/Ley_Inces_webm.pdf | Decree 1.414, INCES law arts. 49-61 | “el dos por ciento del salario normal mensual pagado”; “dentro de los diez días siguientes al pago” | 2026-11-11 | Official institutional law book; arts. 49/50 eligibility and distinct bases retained |
| https://www.cebm.gob.ve/wp-content/uploads/2025/07/LEY-SEGURO-SOCIAL.pdf | Gaceta 39.912, 30 Apr 2012; IVSS law arts. 1-3, 6, 58-67, 78, 85-90; regulation reform arts. 7-8 | “con base en la tasa activa promedio establecida por el Banco Central de Venezuela”; “cinco Unidades tributarias (5 U.T) por semana” | 2026-11-11 | Official Gazette facsimile; visual readings where OCR is noisy; general regulation absent |
| https://www.incret.gob.ve/public/documentos/LEY_ORGANICA_DE_PREVENCION_CONDICIONES_Y_MEDIO_AMBIENTE_DE_TRABAJO.pdf | LOPCYMAT arts. 4, 6-7, 94-99, 128; transitional fifth; final second | “estarán a cargo exclusivo del empleador o empleadora”; “Hasta tanto sea creada la Tesorería de Seguridad Social” | 2026-11-11 | Statutory framework; current implementing/assessment state not established |
| https://contraloriadebarquisimeto.gob.ve/images/baselegal/LOAFSP.pdf | Gaceta 6.210 Extraordinario, consolidated LISLR, arts. 1, 9, 11-12, 31, 39, 50, 52-54, 57-60, 77-81 | “Por la fracción comprendida entre 4.000,00 y 6.000,00 29,00%”; “noventa por ciento (90%) de los ingresos brutos” | 2026-11-11 | Retained tax-reference topics; first Tarifa 1 rates visually read; no current UT conversion |
| https://www.cmchacao.gob.ve/wp-content/uploads/2025/08/Decreto-con-Rango-Valor-y-Fuerza-de-Ley-que-Reforma-la-Ley-que-Establece-el-Impuesto-al-Valor-Agregado.pdf | Gaceta 6.507 Extraordinario; actual PDF is COT 2020; arts. 1, 10, 91, 103, 108, 110, 112, 115 | “serán aumentadas en un doscientos por ciento (200%)”; apply only its listed formal offenses | 2026-11-11 | Filename differs from actual law; COT is not a universal replacement for IVSS special provisions |
| https://www.ivss.gov.ve/marco-normativo | Current official law index, links to general regulation and RPE law | “Reglamento General de la Ley del Seguro Social” | 2026-11-11 | Index opened; linked law files returned 404, so their figures unconfirmed |
| https://www.ivss.gov.ve/empleador/informacion-general | Current employer information | “dentro de los tres días hábiles” | 2026-11-11 | Administrative page read; statute governs conflicting registration wording |
| https://web.archive.org/web/20261027165300/https://banavih.gob.ve/ | Archived official BANAVIH systems landing page, capture 2026-10-27 | “Seleccione la plataforma a la que desea ingresar” | 2026-11-11 | Archived, current-year capture; contains systems access only, not contribution parameters |

### Not yet confirmed

- Current IVSS general-regulation employer/worker rate splits, risk mapping, salary cap/reference wage, week-count/conversion and payment periods, any February-2025 administrative change, continuation/independent-worker current parameters and employer-specific assessment. The law's initial rates are not substituted for those missing parameters.
- Current RPE/unemployment contribution rate split, base, ceiling, covered-person detail, accrual period and return/remittance instructions. The live official law download failed; an older archived text does not satisfy this Guide's current-year archive condition.
- Current FAOV housing law/rates, integral-pay definition, cap/no-cap, effective amendments and filing/payment procedure. The conflicting legacy assertions remain unresolved; the opened current-year archived landing page supplies no rate or cap.
- Pensions-protection contribution's current rate, legal base (including nonsalary payments and any minimum integral income), exemptions, effective year, declaration/payment calendar and interaction with other contributions. No absent figure is filled from a secondary summary.
- Current statutory minimum wage, food benefit, Guerra Económica, combined “economic floor”, current tax-unit currency value, BCV rates and precise FX conversion rules for each contribution. All associated nominal bolívar ceilings and the old derived economic-floor table are excluded from confirmed parameters.
- LOPCYMAT implementing risk resolution/regulation, actual Treasury creation/operation and employer assessment, applicable current salary-base interpretation, current occupational-safety interest inputs and administrative sanctions practice. The statutory range/table/formula is conditional on those operative facts.
- Current INCES administrative staffing-count method, actual holiday calendar and any specific operative procedural departure, RNCP and payment/correction workflow, approved training-deduction percentage/regulation and an actual Board approval. Neither a failed search nor a missing approval is treated as a statutory exemption.
- Current individual employment/bonus income-tax interpretation, annual/estimated/special advance and withholding calendars, instalments, RIF/forms/portals, specific IVA rate/exemption and actual international agreements. The preserved statutory tax references do not certify those administrative questions.
- Exact Banco de Venezuela, Banesco, Mercantil and BBVA Provincial statement layouts, automated description accuracy, institution allocation of an ambiguous payment, actual arrears interest/fine and legal classification of any named bonus in a real case.

### Talk to a verified accountant

Use a qualified Venezuelan professional to review the actual payroll classification, assessment and disputed/source-gap items before filing, payment, amendment or reliance. Provide the source-linked workpaper and precise unresolved inputs, rather than asking the professional to reconstruct a bank-label assumption. This Guide is general reference material and is not a legal opinion or a solvency certificate.
