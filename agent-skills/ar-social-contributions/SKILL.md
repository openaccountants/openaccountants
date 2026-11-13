---
name: ar-social-contributions
description: "Compute ordinary Argentina social contributions in 2026: aportes autonomos, categorias I a V, SIPA, PAMI, obra social, employer contributions, F.931, Libro de Sueldos Digital, Declaracion en linea and Fondo de Asistencia Laboral. Covers activity/income categorisation, dated autonomous tables, employee and employer bases, caps and detractions, registration, May recategorisation, payment reconciliation and the December 2026 FAL change. Establish the accrued period, pension status, activity and payroll facts before computing. It prepares a source-cited working paper for local professional review. Special industries, pension-benefit calculations, professional provincial funds, moratoria and incentive regimes require their own review. Monotributo personal components belong to its Guide."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ar-social-contributions"
  jurisdiction: "AR"
  tax_year: "2026"
  last_updated: "2026-11-12"
---

# Argentina: social contributions 2026 v 2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Ordinary national-regime self-employed contributors and employers/employees within Ley 24.241, Ley 19.032, Ley 23.660 and Ley 27.541. This revision is **Not yet approved**. The [earlier version approved by Maria Valeria Benvenuti on 3 November 2026](https://github.com/openaccountants/openaccountants/blob/157f7d8be741c4c7347a88c8a2970b529d175741/skills/argentina/ar-social-contributions.md) remains preserved; that approval does not cover this text. It extends the former autonomous-only Guide to ordinary staff social contributions; [argentina-payroll](argentina-payroll.md) owns employee income-tax withholding, and [ar-monotributo](ar-monotributo.md) owns simplified-regime personal components.

**Quick answer:** autónomo category depends on activity and prior-year gross income, not a university degree or employee-count floor. Use the published table for the applicable period/status. Staff contributions require separate employee and employer bases: the employee cap does not cap employer contributions. From December 2026 FAL reallocates specified employer contributions; do not simply add it to an unchanged SUSS total.

Get the accrued month, all activities and prior-year income, Código de Registro Autónomo (CRA) and category, pension law/status, concurrent employment/funds, and for staff each CUIL, age, pay components, days/hours, SAC, health coverage, employer sector/size certificate, headcount and benefits. Missing classification or period-specific figures prevent finalising the affected line.

Out of scope: pension-entitlement/benefit promises, debt moratoria, hazardous/special-regime qualification, provincial professional-fund rules, domestic service, rural/construction/sport specifics, incentive/regularisation regimes and public-employer special treatment. ART and collective/union amounts need their actual policy/agreement, not a guessed national percentage.

## Rates, bands and thresholds

### Autónomo category, ordinary activity

The small nominal income cutoffs below are the actual current published classification amounts, not Monotributo limits. Source: Decreto 1866/2006 Annex II, RG 2217 and ARCA's current definition/category page.

| Activity and prior-calendar-year gross income, ARS | Minimum category | Official source |
|---|---|---|
| Company direction/administration/conduction and applicable partners: up to 15,000 inclusive | III | https://www.arca.gob.ar/autonomos/que-es/que-es.asp |
| Same, over 15,000 up to 30,000 inclusive | IV | same |
| Same, over 30,000 | V | same |
| Other leases/services up to 20,000 inclusive | I | same |
| Other leases/services over 20,000 | II | same |
| Other activities up to 25,000 inclusive | I | same |
| Other activities over 25,000 | II | same |
| Ordinary startup | Lowest category in the activity's table; III if simultaneous startup includes table I | RG 2217 art. 12; https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A2217%7Co%3A3%7Ca%3A2007%7Cf%3A21%2F02%2F2007 |
| Unremunerated director, only autonomous activity, no income/utilities | III, not zero | RG 2217 art. 14; https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A2217%7Co%3A3%7Ca%3A2007%7Cf%3A21%2F02%2F2007 |
| Age 18 to under 21; specified voluntary contributors; working Ley 24.241 retiree | I, status conditions apply | RG 2217 arts. 3-4, 15; https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A2217%7Co%3A3%7Ca%3A2007%7Cf%3A21%2F02%2F2007 |

### Published autonomous amounts from 15 October 2026

This is the latest original ARCA PDF read, not an assertion that these apply to every month or remain the November/December values. Use the period-specific table before payment; later tables remain unconfirmed here. Currency ARS/month. Ordinary contribution comprises 27% SIPA plus 5% PAMI on the category reference income; there is no ordinary current-health obra-social component in this autónomo payment (Ley 24.241 art. 11; Ley 19.032 art. 8(c)). Use printed cents instead of recomputing rounded reference amounts.

| Category | Ordinary monthly contribution | Official source |
|---|---|---|
| I | 78,271.56 | https://www.arca.gob.ar/autonomos/documentos/Valores-autonomos-desde-octubre-2026.pdf |
| II | 109,578.51 | same |
| III | 156,541.75 | same |
| IV | 250,466.70 | same |
| V | 344,390.34 | same |
| Working Ley 24.241 retiree, category I | 66,041.63; 27% pension contribution, without ordinary 5% PAMI | same |
| Voluntary affiliate / age 18-under 21, category I | 78,271.56 | same |
| Qualifying Ley 24.828 reduced homemaker category I | 26,905.85; specialist eligibility must be established | same |

Differential I'-V' in the same PDF are respectively 85,609.52; 119,851.50; 171,217.53; 273,947.95; 376,676.94. RG 2217 art. 5 adds 3% of reference income for legally qualifying hazardous/arduous activity. Do not choose a primed category just because work is physically demanding. Legacy pre-March-2007 A-J categories in the PDF need their own history and are not mapped by letter resemblance.

### Ordinary staff, 2026

| Item | Rate / amount and condition | Official source |
|---|---|---|
| Employee SIPA | 11% on applicable employee pension base | Ley 24.241 art. 11; https://biblioteca.arca.gob.ar/dcp/LEY_C_024241_1993_09_23 |
| Employee PAMI | 3% on applicable employee base | Ley 19.032 art. 8(d); https://biblioteca.arca.gob.ar/dcp/LEY_C_019032_1971_05_13 |
| Employee health | 3%, plus 1.5% for each eligible additional adherent under art. 9 final paragraph; ordinary family/status and higher collective-agreement rules must be distinguished | Ley 23.660 arts. 16(b), 18; https://biblioteca.arca.gob.ar/dcp/LEY_C_023660_1988_12_29 |
| Employer ordinary SUSS aggregate | 20.40% for qualifying private services/commerce above medium-tranche-2 sales ceiling; 18% for remaining covered employers, with required size evidence | Ley 27.541 art. 19; https://biblioteca.arca.gob.ar/dcp/LEY_C_027541_2019_12_21 |
| Employer health | 6% for 2026; the enacted 5% change applies from 1 January 2027, not retroactively | Ley 23.660 art. 16, Ley 25.565 art. 80 and Ley 27.802 art. 165 note; https://biblioteca.arca.gob.ar/dcp/LEY_C_023660_1988_12_29 |
| Ordinary per-worker SUSS base detraction | 7,003.68 monthly, prorated for part-month/part-time; SAC has 50% and its own proportional rules; remaining base cannot fall below statutory minimum | Ley 27.541 art. 22; https://biblioteca.arca.gob.ar/dcp/LEY_C_027541_2019_12_21 |
| Certain statutory sectors/public concessionaires | 17,509.20 instead, only where art. 22's conditions apply | same |
| Employer-wide extra detraction, up to 25 employees | 10,000 monthly from remaining total SUSS base, to exhaustion without future carry; not 10,000 for every employee | Art. 23 and Decreto 99 art. 4; https://biblioteca.arca.gob.ar/dcp/DEC_C_000099_2019_12_27 |
| FAL, from accrued December 2026 | 2.5% for qualifying characterised MiPyME/nonprofits; 1% for remaining covered private employers, on specified employer SIPA base | RG 5907 art. 8, current text under RG 5915; https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5907%7Co%3A9%7Ca%3A2026%7Cf%3A30%2F09%2F2026 |

### Employee base parameters read for January-October

| Accrued month 2026 | Minimum ARS | Maximum ARS | Official source |
|---|---|---|---|
| January | 117,643.93 | 3,823,372.95 | https://www.arca.gob.ar/declaracionenlinea/actualizacion-versiones/version47-5-actualizacion.asp |
| February | 120,996.78 | 3,932,339.08 | same |
| March | 124,481.49 | 4,045,590.45 | same |
| April | 128,091.45 | 4,162,912.57 | https://www.arca.gob.ar/declaracionenlinea/actualizacion-versiones/version47-6.asp |
| May | 132,420.94 | 4,303,619.01 | https://www.arca.gob.ar/declaracionenlinea/actualizacion-versiones/version47-6-actualizacion.asp |
| June | 135,837.40 | 4,414,652.38 | https://www.arca.gob.ar/declaracionenlinea/actualizacion-versiones/version47-7-actualizacion.asp |
| July | 138,757.90 | 4,509,567.41 | https://www.arca.gob.ar/declaracionenlinea/actualizacion-versiones/version47-8-actualizacion.asp |
| August | 141,380.42 | 4,594,798.23 | same |
| September | 144,363.55 | 4,691,748.47 | same |
| October | 146,759.98 | 4,769,631.49 | same |

ARCA attributes these to ANSES arts. 3 of resolutions 381/2025, 21/2026, 38/2026, 74/2026, 110/2026, 139/2026, 186/2026, 232/2026, 257/2026 and 284/2026 respectively. November/December are unconfirmed. Current ANSES monthly minimum/maximum bases must be matched to the accrued month. Do not use the autonomous category reference income as an employee cap or apply employee caps to employer bases. The examples use October amounts within its confirmed minimum and maximum.

## The base

### Autónomo computation and changes

1. Test compulsory affiliation and any specific exception under Ley 24.241 arts. 2-5. Concurrent employee coverage does not automatically exempt separate autonomous activity: art. 5 requires contributions for each covered activity unless a specific exception applies. Under art. 3(b)(4), national incorporation is voluntary for the same covered university-professional activity with compulsory provincial professional-fund affiliation; this does not exempt a separate compulsory director/business activity or erase provincial obligations. A degree alone sets no category-II minimum.
2. Under RG 2217 arts. 7-8, reconcile cash/in-kind gross income, net of returns/discounts, including specified advances, activity fixed-asset sales and compulsory-affiliated partnership interests. Exclude national indirect taxes where the contributor is their taxpayer. Apply income-tax attribution rules; total gross income cannot be below total income used for taxable, exempt and non-taxable Ganancias gross income for that year (art. 7). Value in-kind receipts at market on receipt. Net benefit is gross income less necessary expenses under income-tax timing rules and cannot be below the Ganancias net income computed under that law (art. 8).
3. Choose the activity table and prior-calendar-year category. For an earlier year shorter than twelve months, art. 11 uses actual total income for category selection, not a guessed full-year projection. For multiple tables, Decreto 1866 Annex II selects the table for the activity or activities with greatest annual gross income, then applies that table to the sum of all activity gross income; do not add two fixed payments or choose by staff numbers. A new activity uses the statutory startup category; document actual start/cessation dates. Ordinary category modifications under art. 10 take effect from the accrued month of the change; corrections of inaccurate self-declared data are retroactive to when those data should have determined the minimum category. Keep those separate from annual May recategorisation.
4. Test statutory status: RG 2217 art. 2 exempts the specified old-law retiree class who obtained or met the conditions for the qualifying benefit by 15 July 1994; it is not a blanket exemption for every retiree. Ley 24.241 working retirees use the special minimum payment. Age 18-under 21 uses I and changes in the month of turning 21 (art.15). A benefit application while continuing work changes category in the application month (art.16).
5. Higher category is optional under art. 6, except working Ley 24.241 retirees and age 18-under 21. It creates the chosen payment obligation; this Guide promises no particular future pension increase. An annual net-benefit/gross-income ratio below 30% can permit the immediately lower category within the applicable table under art.18; document eligibility at recategorisation.
6. Zero monthly revenue does not cancel registration or its fixed obligation. Arts.19-22 instead provide a June application to carry qualifying already-paid contributions to following-year monthly obligations where the prior-year income test is met; short-year income is annualised for this distinct credit test, all simultaneous income counted and category changes recalculate the credit. The OctoberPDF prints 1,761,574.72 for the updated arts 19/20 income reference; do not backdate it to a different application period. Under Decreto 1866 art. 1 point 4, periods shifted out by this mechanism do not count as service periods for benefits. This is no automatic unpaid-month waiver.
7. Deduct eligible actual personal retirement contributions in Ganancias under LIG art.85(d), subject to its payment and attribution rules, not an unpaid expected bill. Keep receipts/year of payment. The ordinary autonomous payment does not buy current obra-social cover; health eligibility/unification must be checked separately.

### Staff computation

Use ARCA Libro de Sueldos Digital Guides 18/31 for base construction and limits, alongside the applicable laws and actual month parameters.

1. Classify remuneration and each non-remunerative item by whether it actually bears each subsystem; a labour label alone is insufficient. Check CUIL, age, days, ordinary pay, SAC and vacation concepts, health and differential bases. Under 18 employees do not simply enter the full adult SIPA/PAMI calculation; health and other employer systems remain separate.
2. Build employee pension base 1, PAMI base 5 and health base 4 independently, including any applicable differential bases. Apply the correct month minimum/maximum and health minimum rules. Health reduced-hours minima can require full-category remuneration under Ley 23.660 art.18; do not reduce every health base mechanically with hours.
3. For employee maxima compare ordinary monthly components to their monthly cap; compare SAC separately to 50% of monthly cap, with proportional SAC days where relevant. Vacation advances can have a separate days/30 cap; ordinary plus-vacation concepts can instead remain within the monthly base. Sum the separately limited bases. A single comparison of total monthlypay+SAC with 1.5×cap can be wrong. Guide 31's historical quarterly-index introduction is stale for current monthly parameters; its examples are historical, not 2026 amounts.
4. Compute employee 11%SIPA,3%PAMI and 3%health only on their respective eligible bases; include actual extra health/collective deductions separately. These are not automatically 17% of every gross payment.
5. Build employer bases 2/3 for SUSS and 8 for health without the employee maximum. Choose 18%/20.40% using sector/sales/certificate, not headcount alone. Apply art 22's eligible base detraction, prorating on a 30-day basis and subject to minimum; Decreto 99 art 3 limits the part-time detraction to 2/3 of full-time. Apply the 10,000 employer-wide art 23 base reduction if eligible, after per-worker amounts, to exhaustion without carry. Do not reduce health or special/additional bases with an ordinary SUSS detraction. Add 6%health on its own base and policy/collective obligations. Special sector/incentive rules need separate calculations.
6. From accrued December 2026, RG 5907 arts 8-9 reallocates the applicable FAL amount out of SIPA/PAMI/FNE/family-allowance employer contributions. Declaración en línea computes the distribution and separately shows FAL in **Totales Generales / Resultado del cálculo**. The reduction is capped by applicable employer contributions; excess in reduced-rate cases is not carried. Art 15 says incentive reductions do not reduce the FAL calculation. Use characterised employer status and valid IDFAL; do not add FAL to an otherwise unchanged SUSS bill.
7. Reconcile individual bases/deductions, employer subsystem totals, payment credits and final F.931. A payroll income-tax withholding credit or an autonomous payment is not a staff contribution payment.

**Boundary and correction table**

| Fact pattern from the earlier Guide | Current treatment |
|---|---|
| Lawyer/accountant assumes minimumII solely from degree | Use actual service-table income/startup facts; no degree-only floor in official table |
| Employer has 5 employees, assumes autonomousIV | Employee count does not set autonomous category; activity/income does; staff obligations computed separately |
| CategoryI has a zero-revenue month | Registration remains; full applicable fixed amount unless a proved statutory procedure/exception applies |
| Employed person also freelances | Separate affiliation/contributions under art 5 unless specific exception, not automatic exemption |
| Monotributo to general regime mid-year | Establish lawful effective transition date, then activity-table startup/affiliation; not an invented projected-income category |
| Working retiree | Identify actual retirement law and special payment/exemption, not an unspecified PAMI discount |
| Staff decreases from 5 to 3 | No automatic autonomousIV-toIII change; assess real activity/income and separate employer-headcount effects |
| Differential/moratoria/years of debt | Record periods/status/evidence and refer specific law/procedure; do not promise pension credit or a debt waiver |

## Deadlines and filing

### Autónomos

ARCA's current **Sistema Registral → Registro tributario → Empadronamiento autónomos** route requires CUIT/ClaveFiscal and produces the category code/payment credential. RG 2217 art 9 identifies receiptF.940 and credentialF.1101 (F.1104 for qualifying reduced homemakers). The old F.885 assertion is not established as this current registration form. Save the actual acknowledgement, category, start date and credential; do not claim an unverified grace period for late registration.

Annual recategorisation is **May**, using prior-calendar-year facts; the payment category applies **June to following May** (currentarts 24-27). First annual recategorisation is the year after starting. WorkingLey 24.241 retirees, voluntary contributors and specified otherart 25 groups are excepted. The June low-income credit request is different from May recategorisation.

Monthly payment uses the applicable category code/period through VEP/electronic transfer or permitted debit under currentart 29, and is checked in **CCMA** with capital/interest and receipts. Reconcile the period billed with the table's stated effective date. The old “last business day of following month” is not a valid universal deadline: use the current ARCA CUIT calendar/RG 4186, including business-day/exception adjustments. Current live VEP field/code details beyond category code are not confirmed here.

### Employers and December FAL transition

Register actual employment through **Simplificación Registral** and prepare the required payroll records. Where Libro de Sueldos Digital applies, reconcile its concepts/bases to F.931 in **Declaración en línea**; keep acknowledgement and separately pay via the applicable VEP route by the CUIT calendar. Exact current non-FAL payment codes and universal LSD enrolment are not asserted.

Current RG 5907 as amended by 5915 requires **version 48** from **1 December 2026**, for accruedDecember and later and earlier-period original/amended returns filed from that date. Before the December return, declare private/public employer condition in Simplificación Registral; before first FAL contribution, validate the assigned **IDFAL**, entity, investment vehicle and CBU. MiPyME treatment needs a current certificate/characterisation; nonprofits use the specified codes. Missing valid ID prompts the statutory default-assignment route, not permission to skip payment.

FAL forms part of F.931 balance and shares its due date; pay by VEP **266/019/019** (art 10). Excess FAL payments can be reimputed only against another FAL period. Authorised suspension/interruption only operates from the month after ARCA receives the labour authority communication and restores unreduced SUSS treatment; it does not cancel earlier accruals (arts 13-14). FAL grace for use of the fund does not postpone contribution payment.

## Penalties and interest

Late payment, missing registration, omitted remuneration and underpayment are distinct. RG 5907 art 12 routes sanctions to Ley 11.683/Ley 17.250 and RG 1566. Current 2026 penalty amounts and interest rates are not confirmed here; do not apply a stale “daily resolutory rate”. Save notices, principal, period, legal basis and actual payment history. Compulsory collection, retroactive assessments and pension recognition need current procedural/ANSES review; nonpayment is not a universal promise of lost-or-restored retirement credit. Refer moratoria before proposing a plan.

## Cross-border points

Foreign employment/assignments and international social-security agreements need their own official coordination rules; an income-tax treaty does not automatically exempt contributions. Use [argentina-cross-border](argentina-cross-border.md) for income residence/source and keep social-security coverage separate. Foreign currency remuneration must be converted under its own applicable payroll rule; no universal exchange rate is guessed here.

## Two worked examples that recompute

### 1. Degree or activity and income?

Assume an ordinary self-employed professional, prior-calendar-year service receiptsARS 100,000, no special fund/retiree/age exception, and the publishedOctober table applies. Receipts exceed 20,000, so minimumII,109,578.51, because of income, not degree. A genuine new service activity initially falls inI,78,271.56, subject to proper startup facts. Difference 31,306.95. If the first person also has employee contributions 20,000 that month, combined personal cash contributions 129,578.51; do not erase the autonomous obligation just because employment exists.

```oa-check
name: Autonomous category and dual status
inputs:
  category_one: 78271.56
  category_two: 109578.51
  employee_contributions: 20000
steps:
  - category_difference: category_two - category_one
  - dual_status_total: category_two + employee_contributions
expected:
  category_difference: 31306.95
  dual_status_total: 129578.51
```

### 2. Ordinary employee and employer, pre-FAL

Assume October 2026, one full-month adult employee, each contribution baseARS 1,000,000 before ordinary detractions, noSAC/vacation/extras, verified minimum/cap conditions met,18%employer status and eligibility for both ordinary detractions. EmployeeSIPA 110,000+PAMI 30,000+health 30,000=170,000. EmployerSUSSbase=1,000,000-7,003.68-10,000=982,996.32; SUSS 176,939.34; health 60,000; total 236,939.34 beforeART/collective charges. Total employer cash cost including gross salary is 1,236,939.34 before those extras. This does not use employee 17%as employer rate or apply an employee cap to employerhealth.

```oa-check
name: Employee and employer separate bases
inputs:
  remuneration: 1000000
  worker_detraction: 7003.68
  employer_detraction: 10000
steps:
  - employee_contributions: remuneration * (0.11 + 0.03 + 0.03)
  - employer_suss_base: remuneration - worker_detraction - employer_detraction
  - employer_suss: round(employer_suss_base * 0.18, 2)
  - employer_health: remuneration * 0.06
  - employer_contributions: employer_suss + employer_health
  - employer_cost: remuneration + employer_contributions
expected:
  employee_contributions: 170000
  employer_suss_base: 982996.32
  employer_suss: 176939.34
  employer_health: 60000
  employer_contributions: 236939.34
  employer_cost: 1236939.34
```

## Ask the client first

1. Accrued period, actual start/cessation, all activities, gross-income/net-benefit evidence and prior category/category code.
2. Pension status/law/application date, age, other employment and actual contributions, provincial professional-fund facts.
3. CCMA/payment/registration/recategorisation history, arrears, notices, any higher-category or credit election.
4. For staff: CUIL, age, days/hours, pay concepts, SAC/vacation, health/collective coverage and actual policies.
5. Employer sector/sales/certificate, headcount, special regimes, credits/LSD/F.931 history and payment calendar.
6. DecemberFAL private/public characterisation, MiPyME/nonprofitcodes, IDFALvalidation and suspension notifications.

Retain a category/source-period sheet, autonomous payment reconciliation, employee-by-subsystem base schedule, detraction eligibility/order and F.931/payment bridge. Flag the exact unresolved component/evidence and professional needed; do not finalise an unsupported number.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| Read for compulsory/concurrent affiliation and employee/autonomous rates: Ley 24.241 arts 2-5,11; quotation:"El aporte personal de los trabajadores autónomos será del veintisiete por ciento" | https://biblioteca.arca.gob.ar/dcp/LEY_C_024241_1993_09_23 | 2026-11-11 |
| Read forPAMIcomponents: Ley 19.032 art 8(c)-(d); quotation:"del cinco por ciento" | https://biblioteca.arca.gob.ar/dcp/LEY_C_019032_1971_05_13 | 2026-11-11 |
| Read forhealthrates,2027 effective-note andminima: Ley 23.660 arts 16,18; quotation:"a partir del 1º de enero de 2027" | https://biblioteca.arca.gob.ar/dcp/LEY_C_023660_1988_12_29 | 2026-11-11 |
| Read forcategoryactivity/income/startup table: ARCAQué es; quotation:"ingresos brutos obtenidos en el año calendario inmediato anterior" | https://www.arca.gob.ar/autonomos/que-es/que-es.asp | 2026-11-11 |
| Read originalOctoberPDFallpages, currentI-V/specialstatus/differential tables andincome-reference: quotation:"15/10/2026" | https://www.arca.gob.ar/autonomos/documentos/Valores-autonomos-desde-octubre-2026.pdf | 2026-11-11 |
| Read forcategory/payments/Mayreview/Junecredit: RG 2217 current arts. 1-32; quotations:"mes de mayo de cada año","mes de junio de cada año" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A2217%7Co%3A3%7Ca%3A2007%7Cf%3A21%2F02%2F2007 | 2026-11-11 |
| Read forcurrentregistrationroute: ARCAinscripciónpage; quotation:"Empadronamiento autónomos" | https://www.arca.gob.ar/autonomos/inscripcion/inscripcion.asp | 2026-11-11 |
| Read foremployerSUSSclassification/detraction: Law 27.541 arts 19-24; quotation:"siete mil tres con sesenta y ocho centavos" | https://biblioteca.arca.gob.ar/dcp/LEY_C_027541_2019_12_21 | 2026-11-11 |
| Read forcertificate, parttime andorderedbase reductions: Decreto 99 arts 1-4; quotation:"sin que el excedente pueda trasladarse a períodos futuros" | https://biblioteca.arca.gob.ar/dcp/DEC_C_000099_2019_12_27 | 2026-11-11 |
| Read forbaseconstruction: ARCA LSDGuide 18, wholemethod/basesections; quotation:"no se aplica tope máximo"; oldillustrativeamountsnotused | https://www.arca.gob.ar/LibrodeSueldosDigital/documentos/nuevos/G18-Armado-bases-imponibles-LSD.pdf | 2026-11-11 |
| Read forcapseparation: ARCA LSDGuide 31, wholemethod/examples; quotation:"cada tope se calcula por separado"; historicalamountsnotused | https://www.arca.gob.ar/LibrodeSueldosDigital/documentos/nuevos/G31-Topes-LSD.pdf | 2026-11-11 |
| Read forFALscope/rates/base/reallocation/ID/payment/version 48/Decemberstart: RG 5907 currentarts 1-19 under 5915; quotation:"período devengado diciembre de 2026" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A5907%7Co%3A9%7Ca%3A2026%7Cf%3A30%2F09%2F2026 | 2026-11-11 |
| Read foractualpersonalretirementdeduction: LIGart 85(d); quotation:"contribuciones o descuentos para fondos de jubilaciones" | https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 | 2026-11-11 |
| Read for January-March employee base table, each row; quotation: "01/03/2026" | https://www.arca.gob.ar/declaracionenlinea/actualizacion-versiones/version47-5-actualizacion.asp | 2026-11-11 |
| Read for April employee base table; quotation: "$ 4.162.912,57" | https://www.arca.gob.ar/declaracionenlinea/actualizacion-versiones/version47-6.asp | 2026-11-11 |
| Read for May employee base table; quotation: "$ 4.303.619,01" | https://www.arca.gob.ar/declaracionenlinea/actualizacion-versiones/version47-6-actualizacion.asp | 2026-11-11 |
| Read for June employee base table; quotation: "$ 4.414.652,38" | https://www.arca.gob.ar/declaracionenlinea/actualizacion-versiones/version47-7-actualizacion.asp | 2026-11-11 |
| Read for July-October employee base table, each row; quotation: "$ 4.769.631,49" | https://www.arca.gob.ar/declaracionenlinea/actualizacion-versiones/version47-8-actualizacion.asp | 2026-11-11 |
| Read for simultaneous-activity classification and low-income credit conditions: Decreto 1866 Annex II and art. 1; quotation: "COMPATIBILIZACION ENTRE LAS TABLAS I, II Y III" | https://biblioteca.arca.gob.ar/dcp/DEC_C_001866_2006_12_12 | 2026-11-11 |
| Read for the restoration of the 6% employer health contribution: Ley 25.565 art. 80; quotation: "Restitúyese la alícuota" | https://biblioteca.arca.gob.ar/dcp/LEY_C_025565_2002_03_06 | 2026-11-11 |
| Read for ordinary CUIT calendar grids, RG 4186 art. 1(2), read with actual month shifts; quotation: "PRESENTACIÓN DDJJ F. 931 y PAGO" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t%3ARAG%7Cn%3A4186%7Co%3A3%7Ca%3A2018%7Cf%3A05%2F01%2F2018 | 2026-11-11 |

Not yet confirmed: November/December 2026 employee minimum/maximum and post-October autonomous tables; CUIT-specificfuturecalendars/liveVEPnon-FALcodes; currentpenalties/interest; registrationgraceperiod/oldF.885 claim; professional-fundandforeigncoordinationrules; pensionbenefit/retirementcredit/collectionprocedure; exactMonotributotransitioneffective-date facts. Legacydegree/employee-countfloors, September 2025 approximations, ordinaryobra-socialcomponent andCPI-plus-RIPTEmobilityclaim are superseded by the verifiedclassification/components andoriginalperiodtables, not repeated as facts.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-12. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ar-social-contributions` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ar-social-contributions. If neither is available, confirm every figure against the official source pages cited above before relying on it.
