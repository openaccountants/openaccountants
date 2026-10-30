---
name: moldova-social-contributions
description: "Compute Moldova social contributions and compulsory medical insurance for 2026. Distinguish ordinary private and public employers, special aviation roles, agricultural relief, IT-park insured income, independent physicians and justice professions, fixed-contribution categories, patents, taxi transitions, day workers and independent service entrepreneurs. Apply the social minimum base and separate part-time contribution floor, and distinguish salary accrual from medical-premium payment timing. Use for CNAS, CNAM, IPC21, fixed social insurance, health premiums, payroll contribution reconciliation, status overlaps, payment deadlines and arrears. This source-cited writer draft preserves predecessor subjects through explicit destinations and gaps, requires whole-country independent review and does not claim comprehensive coverage or accountant attestation."
version: 0.2
jurisdiction: MD
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Moldova social contributions and medical insurance, 2026 v0.2

## Who this applies to

Determine the actual payer category, insured person, remuneration, work period and payment date before calculating Moldova's 2026 social contributions or mandatory medical insurance. These are different systems with different bases and timing. This source-cited writer draft replaces the earlier mixed-year summary. It is not independently reviewed or accountant-attested; the country remains partial. [Law 489/1999 arts. 17–23][social]; [Law 1593/2002][health].

Social insurance covers the ordinary private and public employer categories, specified special-condition work, IT-park employment, independent family physicians, qualifying agriculture, individual/farm founders, independent retail and plant-product purchasing, justice professions, patents, day workers and the new independent service entrepreneurs. A sole trader, patent holder and independent service entrepreneur are not interchangeable categories. Obtain actual registration and overlapping employment/pension/disability records. Insured benefits also differ by category; payment of a fixed amount does not establish entitlement to every benefit. [Law 489 art. 17 and annex 1; CNAS instructions points 2–3, 10–20][instructions].

Mandatory health insurance separately distinguishes percentage payers in Law 1593 annex 1 and fixed-premium categories in annex 2. Current annex 1 identifies employees as percentage payers and includes the covered civil-contract remuneration route. Do not recreate an employer/employee percentage split from an older summary. For IT-park salary, use the special single-tax route; civil-contract payments remain a separate classification. State-insured status, concurrent categories, residence and the dates a status starts or ends matter. [Law 1593 arts. 4–6 and annexes 1–2][health]; [2026 medical budget art. 4][medicalbudget].

Foreign citizenship alone does not exempt a worker from social insurance. Law 489 art. 19(6) applies the charging rule to the stated national/foreign/stateless groups and contains a specific exception for foreigners meeting Law 200/2010 art. 43^17 conditions. Establish those conditions or the operative international agreement before claiming an exemption. Tax residence and social-insurance coverage require separate legal tests. [Law 489 art. 19(6)][social].

Use [payroll](moldova-payroll.md) for wage withholding and net pay and [individual income tax](moldova-income-tax.md) for annual residence, allowances, investment income and returns. Their existing dates and gaps remain explicit until their own rewrites. Bank descriptions, the old Guide's “Tier 1/Tier 2” rule headings and a matching payment amount do not establish legal eligibility or review status.

## Rates, bands and thresholds

All amounts are MDL. Classify first; the same percentage does not make two categories equivalent. CNAS instructions below are the authority's 2026 operating instructions, Order 31-A of 18 February 2026, with their cited statutory provisions. Direct retention of annex 1's attached tariff document is still open; the law-register link returned 403 during this writer pass.

| Category or measure | 2026 rate/amount and limits | Primary authority |
|---|---|---|
| Ordinary commercial private/state/municipal employers; specified higher-education and medical institutions | Employer social contribution 24% of the applicable base | [CNAS point 9.2; Law 489 annex 1, 1.1][instructions] |
| Specified budgetary/public authorities and institutions | Employer social contribution 29%; check the higher-education/medical exceptions | [CNAS point 9.1; annex 1, 1.1][instructions] |
| Listed civil-aviation special-condition roles | 39% in the specified public category; 32% in the specified private category. A general “hazardous” description does not establish either category | [CNAS points 10–10.2; annex 1, 1.2; Law 489 annex 2][instructions] |
| Independent family physician | 24% of the defined professional income; employees follow their own employer category | [CNAS point 11; annex 1, 1.3][instructions] |
| Qualifying agriculture | Total social tariff 24%: employer 18%, state-budget transfer 6%; qualifying CAEM 01.1–01.6 income must be at least 70% of operating income | [Law 489 art. 17(3^1)–(3^2)][social]; [CNAS points 13–13.4][instructions] |
| Employee social withholding in ordinary employment | The listed ordinary employer tariff is the employer's liability; do not deduct an additional old 6% employee social tariff | [CNAS points 9–10; annex 1, 1.1–1.2][instructions] |
| Ordinary employee/covered civil-contract health premium | 9% of covered salary/other remuneration; ordinary employee premium is withheld by the payer | [Medical budget art. 4(1)][medicalbudget]; [Law 1593 arts. 4, 6, 12, 20 and annex 1][health] |
| National minimum monthly wage used in the contribution floor | 6,300 from 1 January; contribution base at least the minimum proportionate to time worked; part-time/reduced-work social contribution at least 25% of the full-minimum contribution | [CNAS point 19.1][instructions]; [Law 489 art. 22(1), January version][socialjan] |
| Forecast monthly average salary | 17,400 | [CNAS point 12.1 citing Government Decision 773/2025][instructions] |
| IT-park insured employment income | 68% of forecast average salary = 11,832 a month for the specified insured-income purpose; this is not the worker's actual cash salary | [CNAS point 12.1][instructions] |
| IT-park single-tax allocation to social budget | 54.7% of the single tax; distinct from the new service entrepreneur's allocation | [CNAS point 12.2][instructions] |
| Specified founders, independent retailers, plant-product purchasers and patents | Annual fixed social amount 22,878; monthly amount 1,906.50, subject to the category/period/exemption rules | [Social budget art. 3(1)][socialbudget]; [CNAS points 15, 17][instructions] |
| Justice professions | Annual fixed social amount 30,966; monthly 2,580.50, subject to the category, overlap and suspension rules | [Social budget art. 3(2)][socialbudget]; [CNAS point 16][instructions] |
| Taxi-driver fixed social category | 1,906.50 monthly only January–June; from 1 July ordinary employer treatment and IPC21 replace this special category | [CNAS points 2.2, 18–18.3][instructions] |
| Covered day worker | Social 6% of daily remuneration; the stated 169-hour monthly norm gives 37.28 hourly and 298.24 for eight hours in the 2026 instruction | [CNAS point 19.1][instructions] |
| New independent service entrepreneur | Single tax 15% up to annual income 1.2 million and 35% on excess; 53.3% of that tax allocated to social budget. Do not impose the ordinary employer tariff on the same single-tax receipt | [CNAS points 2.1, 20; Law 489 annex 1, 1.10][instructions] |
| Voluntary social contract | 22,878 annual; qualifying individually working agricultural landholder/tenant 5,827 annual; at least one twelfth monthly | [Social budget art. 3(3)][socialbudget]; [CNAS points 22–22.4][instructions] |
| Fixed annual health premium | 12,636 for covered fixed categories, subject to the category and entry-date rules | [Medical budget art. 4(2)][medicalbudget] |
| Eligible early-payment health amount | 2,527 for the stated annex-2 groups 1, 3 and 4 paid within the statutory deadline; exclude digital nomads and concurrent groups 2/2^1 | [Medical budget art. 4(3)][medicalbudget]; [Law 1593 art. 22][health] |
| Fixed health groups 2/2^1 and digital nomads | 12,636 under the separate statutory conditions; no automatic early-payment reduction | [Medical budget art. 4(4), (6)][medicalbudget] |

The medical-budget statute says **2,527**, whereas the Finance Ministry's January 2026 overview says 2,572. The statute controls. For the new service-entrepreneur top-up, Fiscal Code art. 69^26(2) refers to the annual fixed amount granted for timely payment to Law 1593 annex 2 point 1(b). The linked 2026 statutory benchmark is 2,527, not the overview's 2,572. Apply the separate allocation/difference method below; this reference does not reclassify the entrepreneur as an ordinary fixed-premium payer. [Fiscal Code art. 69^26(2)][code]. [Medical budget art. 4][medicalbudget]; [Finance Ministry overview][mfchanges].

## The base

### Ordinary social contribution and the minimum

1. Establish the statutory employer and worker category. Do not choose 24%, 29%, 32% or 39% from the bank reference or assume that all difficult/hazardous jobs are civil-aviation special-condition jobs. Annex 2 lists navigant, air-traffic and technical aviation roles; apply the actual category and documented conditions. The ordinary employer contribution is an employer cost, separate from the employee health deduction and PIT. [Law 489 arts. 17–18, annex 2][social]; [CNAS points 9–10][instructions].
2. Reconcile accrued gross salary and other covered remuneration for every employee to the payroll and nominal insured record. Social contributions follow accrual/calculation, not merely the date cash leaves the bank. A wage bank debit often represents net cash after withholding and does not identify the social base. [Law 489 art. 20(1), (5)][social]; [CNAS points 5–9][instructions].
3. Apply Law 489 art. 22(1)'s minimum: the employee's monthly base cannot be lower than the national minimum in proportion to time worked. For part-time or reduced work, the calculated social contribution cannot be below 25% of the contribution on the full national monthly minimum. Compare the actual contribution, the time-proportionate minimum contribution and that separate floor. Obtain the actual time/work-status record; do not impose an ordinary-salary calculation on an IT-park insured-income entry or a fixed-tax category. The minimum wording is present in both the January and current selected statute. [Art. 22][social]; [January art. 22][socialjan].
4. For amounts calculated now for other service periods, preserve both the calculation/reporting month and the actual insured service periods. CNAS points 7–8.3 apply the calculation-period tariff and current reporting method; their December/January holiday-pay and employer/state-funded sickness examples require distinct nominal categories. Do not shift every prior-year correction into a fictional current service period. Historical declaration corrections have their own rules below. [CNAS points 7–8.3, 33][instructions].
5. Test every excluded payment against Law 489 annex 3. Exclusion from PIT or a corporate deduction is not automatically exclusion from social insurance. Excluded remuneration also does not enter the insured-benefit calculation under art. 23(2). [Law 489 art. 23 and annex 3][social].

The following statutory exclusion groups preserve ordinary remuneration distinctions. Apply the exact facts and any cited Government procedure; the label alone is insufficient. Annex 3 covers Government-organised transport/food/training and student-trainee transport/food; duty-travel and specified injury compensation; statutory redundancy amounts; specified public/military service compensation; protection equipment, therapeutic food and the stated treatment/rest facilities; qualifying gifts and Fiscal Code art. 24(19^3)/(20) payments; scholarships and specified student work; duty-transfer travel/removal/housing; the stated young-specialist payments; temporary-incapacity benefits and public-budget social benefits; property-management income including dividends/interest; state-bond proceeds; qualifying grants; copyright and civil-agreement amounts **except work/service contracts**; inventions; qualifying union/employer-organisation material aid; specified injury/death compensation; sport/competition awards; survey participation rewards; damage compensation **except salary for forced absence**; patent activity receipts; specified state first-home/teacher payments; SARS-CoV-2 testing/vaccination; alternative childcare up to 2,500 monthly per employee's child under 3; and the stated electoral-worker indemnity. Public/medical staff commuting/housing and strategic-industry young-worker payments have their own exact conditions. This is a classification map, not a universal exemption for every payment with one of these names. [Law 489 annex 3 points 1–43][social].

Employee gifts/benefits tied to Fiscal Code art. 24(19^3)/(20) require the actual deductible-limit tests. In 2026 the rural-tourism/vacation-voucher and sports benefit route shares the 50%-of-forecast-salary cap; do not apply a second independent cap to the same combined route. Obtain provider activity, benefit type, period and per-employee records. See the [corporate draft](md-corporate-income-tax.md) for the underlying expense tests and its remaining Government-procedure gaps. [CNAS points 4.1–4.2][instructions]; [Fiscal Code art. 24][code].

### Agriculture, IT parks and other professional categories

For agriculture, compute qualifying CAEM 01.1–01.6 income divided by recorded operating income for the reporting period. Preserve the pre-1-January accounting-policy election and reconcile the actual annual ratio before the final monthly declaration. If the ordinary ratio conditions are satisfied despite a missing policy statement, CNAS describes corrected declarations; if 18% was used and the actual ratio fails, correct and settle the ordinary difference. The state 6% is not an employee deduction. [Law 489 art. 17(3^1)–(3^2)][social]; [CNAS points 13–13.4][instructions].

For IT-park employment, report the specified 11,832 monthly insured income for each employer independently. Multiple jobs within the same employer do not create multiple insured-income bases. Keep the 54.7% allocation of the park's single tax distinct from insured income and actual salary; covered civil work/service contracts remain under the ordinary social law. The previous Guide's 7%-of-turnover and 30%-of-average-salary minimum assertions require the full current park-tax eligibility/base and headcount rules, which this social draft does not certify. [Law 489 art. 19(7), 20(4)][social]; [CNAS points 12.1–12.3][instructions].

For an independent family physician, use the legally determined professional income base; employees are not converted into self-payers because their employer is a physician. For justice professions, distinguish lawyer, notary, bailiff, authorised administrator and mediator; check statutory overlapping categories, pension/disability and officially recorded professional suspension. Notify CNAS of a qualifying suspension. Sickness reporting distinguishes self-funded from social-budget periods rather than cancelling every month automatically. [Law 489 art. 22(4)][social]; [CNAS points 11, 16–16.6][instructions].

### Fixed contributions, patents, taxis, day work and voluntary insurance

For individual/farm founders, independent retailers and plant-product purchasers, the fixed contribution runs from state registration to deletion, subject to the actual exclusions. Pensioner/disability/insured-employment exemptions require the statutory evidence. An old-age social allowance without pension entitlement is not the pensioner exemption. Zero insured employment income, suspended contracts, the stated maternity/childcare/unpaid leave situations and sickness periods have different effects under the CNAS instructions. Do not extend an employment exemption to every month without insured pay. Founders who also retail/purchase plants and concurrent retail/plant purchasers follow the specified single-capacity assessment rules, avoiding duplicate identical fixed charges. [CNAS point 15 and subpoints][instructions].

For plant-product purchasers and independent retailers, CNAS makes the specified monthly assessment from its received registration data; this is not a demand that every person file CAS18-AN. Check the individual's CNAS account and category. [Law 489 art. 20(1^1)][social]; [CNAS points 2.3, 15.5–15.6, 25.2][instructions].

A patent holder pays for the patent period at application/renewal, with at least a full monthly twelfth for every touched month; do not prorate a partial month like a new taxi hire. A patent spanning year-end follows the CNAS tariff rule depending on whether the next budget was enacted when the application was made. [CNAS points 17.3–17.4][instructions].

Only January–June 2026 uses the taxi driver's fixed contribution. A new hire during a month has the stated remaining-calendar-days proration; termination during a month retains the full monthly charge, without automatic refund/reallocation. Other employment/functions are separately subject to ordinary contributions. From 1 July, use the general salary category and IPC21 rather than continuing the old fixed/TAXI18 method. [CNAS points 2.2, 18–18.3][instructions].

For covered day workers, establish eligibility under Law 22/2018, the remuneration and overlap exclusions before applying 6%. The 2026 instruction's daily wage illustration uses the specified minimum and hours; do not assume every day worker works an eight-hour day. [CNAS point 19.1][instructions].

For the new independent service entrepreneur, social contributions form 53.3% of the single tax, whose annual income bands are 15% up to 1.2 million and 35% above. SFS calculates the tax and issues the next-month notice; CNAS records the transmitted social component. Do not confuse this with independent retail, a justice profession or IT-park taxation. The fiscal period is the calendar year, with the stated registration-to-cessation/year-end or year-start-to-cessation periods. Article 69^26(3) taxes actual service income for a person starting or ceasing during the period. The registration/activity tests and monthly cumulative-band adjustments still need their implementing procedures; use the [individual-income draft](moldova-income-tax.md) for the separate regime and reclassification tests. [Fiscal Code arts. 69^20–69^26][code]. [CNAS points 2.1, 20.2][instructions]; [Law 489 art. 20(4^1)][social].

A qualifying voluntary contract covers at least one month; the general monthly amount is 1,906.50. For qualifying individually working agricultural landholders/tenants the CNAS 2026 schedule gives 485.59 for January–November and 485.51 for December, totalling 5,827. Retrospective coverage is available only for the stated periods from 1999, or 2009 for the stated agricultural group, at the applicable contract-date tariff. Payment in 2026 does not lock a tariff for a contract made later. Termination normally gives no refund; documented overlap with actual insured income has the specific request/refund route. [Social budget art. 3(3)][socialbudget]; [CNAS points 22–22.4][instructions].

A legally state-registered business suspension can suspend the specified categories' social calculation/reporting/payment duties. Obtain the actual registration and affected category; a quiet bank account is not a registered suspension. [CNAS point 21][instructions].

### Medical insurance is a separate computation

For percentage premiums, start with covered gross remuneration **before income tax or other deductions**. Withhold/remit the ordinary employee's premium as the law requires. Salary and covered civil contracts must be classified under annex 1; other receipts are not automatically wages. Law 1593's IT-park salary exception does not exempt every payment by an IT-park resident. [Law 1593 arts. 4–6, 12, 20 and annex 1][health].

For fixed-premium liability, establish the actual annex-2 category at 1 January and all later status changes. Categories include the statute's specified land/property/patent/independent-business groups, justice professions, independent medical practice, other non-employed non-state-insured persons and digital-nomad conditions. Do not charge every non-salaried resident 12,636 without testing State coverage, percentage status, residence and category overlap. The full State-insurance statute and international cases remain open below. [Law 1593 annex 2][health]; [medical budget art. 4][medicalbudget].

For eligible annex-2 groups 1, 3 and 4, timely payment under art. 22 gives the 2,527 amount only if the person is not a digital nomad and does not concurrently fall within groups 2/2^1. Groups 2/2^1 pay 12,636 under the annual law's stated rule. Digital nomads obtain insured status after paying the full amount. A Moldovan citizen outside the payer categories who establishes more than 183 calendar days abroad after the statutory deadline has the separate full-premium/status route; it is not a blanket exemption for every resident working abroad. [Medical budget art. 4(3)–(6)][medicalbudget].

For a person entering a fixed category after the annual deadline, Law 1593 art. 23 gives a 30-calendar-day payment deadline and its prescribed proportional calculation. The relevant uninsured days can include uninsured days before entry as well as the remaining year; do not assume liability starts only on registration. Refund/reallocation on overlapping salary premiums, newly acquired exempt status or other changes has the statute's own conditions, including the stated comparison with the full fixed amount. Late acquisition of insured status requires the applicable premium and late charge. Obtain CNAM's category/day record before calculating. [Law 1593 arts. 23–23^1][health].

### Independent service entrepreneur: annual medical difference

The single tax includes medical insurance. Article 69^25(4)(c) allocates **15.4% of the single tax**, not 15.4% of gross receipts, to the medical fund; the social allocation is separately 53.3%. Reconcile the actual annual medical allocation from the single tax against the **2,527** 2026 benchmark identified above. If the allocation is lower, the art. 69^26(2) additional medical amount is the positive difference; if it covers the benchmark, that paragraph does not create a negative top-up/refund. Keep the notice and allocation evidence, rather than charging the ordinary 9% payroll premium again on the same single-tax receipts. [Fiscal Code arts. 69^25(3)–(4), 69^26(2)][code]; [medical budget art. 4(3)][medicalbudget].

SFS sends the additional notice by **25 January following the reporting year**, and the difference is payable by **25 February of the year the notice is sent**. Thus the statutory dates for a 2026 annual difference are 25 January and 25 February 2027, before applying any separately verified non-working-day rule. Do not import the ordinary fixed-payer 31 March deadline or uninsured-day proration into this distinct Code mechanism. Partial-year calculation, status overlap, actual allocation/rounding and correction procedures beyond the stated statute remain explicit implementation gaps. [Fiscal Code art. 69^26(2)–(3)][code].

### Reconcile the bank and working paper

Keep separate schedules for employer social cost, employee health withholding, PIT, fixed social contributions and fixed health premiums. “CNAS”, “CASA NATIONALA DE ASIGURARI SOCIALE”, “ASIGURARI SOCIALE”, “CONTRIBUTII SOCIALE”, “BASS” and “CONTRIBUTIE SOCIALA FIXA” are search hints for social movements. “CNAM”, “COMPANIA NATIONALA DE ASIGURARI IN MEDICINA”, “ASIGURARE MEDICALA”, “ASIGURARI MEDICALE”, “PRIMA ASIGURARE MEDICALA” and “FAOAM” are health hints. “SFS”, “SERVICIUL FISCAL DE STAT”, “IMPOZIT PE VENIT”, “IPC21” and “IPC” require allocation to the actual liability; IPC21 is a declaration, not proof that a single bank payment settled every component. “SALARIU”, “SALARIZARE” and “AVANS” identify possible wage/advance movements; “PENSIE”, “CNAS PENSIE”, “INDEMNIZATIE” and “AJUTOR SOCIAL” can identify benefits. These are reconciliation cues, not statutory classification or VAT conclusions. A refund can be a credit; do not reject it because the old rule expected only debits.

For a bank-only file, collect matching debits and credits, reconcile each to its treasury account, period, notice, declaration and payment receipt, and ask for payroll/registration evidence before calculating. Do not reverse-engineer gross salary from a combined tax payment or average all payments to infer a legal rate. Keep transfers and refunds separate to avoid double counting. The old Maib/MICB/OTP/Victoriabank names are possible statement-source labels, not evidence of a payer's legal status.

The working paper records employer/person identity; tax year; each payer category and effective dates; registration/overlap evidence; hours and accrued gross; excluded remuneration with the precise legal basis; actual pay date and covered health base; social minimum-floor comparison; employer social cost; employee health; PIT as a separately verified input/output; payment/return deadlines; amounts assessed/paid/refunded; and unresolved questions. Preserve fixed and single-tax schedules separately. Report employer cost and cash to the worker only after all applicable payroll components have been established.

## Deadlines and filing

| Obligation | Method/deadline | Authority |
|---|---|---|
| Ordinary social calculation/payment and IPC21/IU17 where applicable | Generally by the 25th after the reporting month for the specified categories; distinguish the form, category and insured periods | [Law 489 arts. 20, 26][social]; [CNAS points 23–30, 40][instructions] |
| Non-working payment due date | Social contribution payment moves to the next working day under the instruction; do not silently apply this to every unrelated tax deadline | [CNAS point 41][instructions] |
| Ordinary percentage medical premium | Withhold/remit by the 25th after the month covered remuneration is actually paid; keep this separate from social accrual | [Law 1593 arts. 12, 20][health] |
| Medical percentage declaration/correction | Electronic monthly reporting under art. 26; reconcile payment timing and actual approved form | [Law 1593 art. 26][health] |
| Fixed medical status present at 1 January | Pay by 31 March for the statutory annual deadline and eligible reduced amount | [Law 1593 art. 22][health]; [medical budget art. 4][medicalbudget] |
| Fixed medical status arising later | 30 calendar days under the applicable art. 23 route; prescribed uninsured-day calculation | [Law 1593 art. 23][health] |
| Founder without employees | CAS18-AN under the specified category; generally by 15 January following the year. Founder with employees uses IPC21 for the relevant combined nominal reporting | [CNAS points 25, 29][instructions] |
| Independent retail/plant purchaser | CNAS monthly assessment under the stated route, rather than the person's own contribution declaration | [Law 489 art. 20(1^1)][social]; [CNAS point 25.2][instructions] |
| New service entrepreneur | SFS notice by the 10th of the next month; single tax paid by the 25th of that month. Annual medical-difference notice by following-year 25 January; payment by 25 February of that notice year | [Fiscal Code art. 69^26(2)][code]; [CNAS point 2.1][instructions] |
| Patent | On application/renewal for the covered period, with the minimum monthly rule | [CNAS points 17.3–17.4][instructions] |
| Taxi fixed route January–June only | TAXI18 and payment by the 25th of the preceding month, with the special late-hire rules; from July ordinary IPC21 route | [CNAS points 18–18.3, 30, 40][instructions] |
| Employment relationship changes | IRM19 within 10 working days for the prescribed start/change/termination events | [CNAS point 32][instructions] |
| Registration outside the general State-registration law | Register as a contribution payer with the territorial CNAS office within 10 working days of obtaining the right to the relevant activity | [Law 489 art. 26(1)][social] |

IT-park reporting uses IU17 for the single tax and IPC21 nominal insured-income information; ordinary civil-contract contributions remain separate. The specified employer, physician, agriculture and justice groups use IPC21 table 2. When no employee and no social contribution is calculated, the instruction gives the stated no-monthly-return exception; check whether any other liability/reporting duty remains. Submit electronically with the appropriate signature and retain SFS-to-CNAS reconciliation. [CNAS points 23–25.2, 31][instructions].

Liquidation IPC21/IU17 filing has the instruction's maximum 10 days after approval of the liquidation balance; CAS18-AN liquidation uses its separate 3-day period from initiating deletion. Pension-request and other termination cases have their own stated reporting timing. Historical corrections preserve the relevant form: IPC18 for January 2018–December 2020, earlier BASS/REV5 material to CNAS. Full current approved annex/codes and reorganisation procedures remain open below. [CNAS points 28–29, 33][instructions].

Payment is considered made when received into the Ministry of Finance Treasury account, not merely when a bank instruction is prepared. Part payments allocate to insured accounts under the statutory proportional rule. Match the actual account, liability period, receipt and payment allocation; incorrect/overpaid social payments require the separate CNAS request/correction/refund procedure. [Law 489 art. 20(6)–(7), 24][social]; [CNAS point 45][instructions].

The old annual CET18/PIT deadlines are not interchangeable with these social and medical returns. Annual individual filing and foreign-citizen departure cases require the individual Guide's own current-law check. Do not certify that an IPC21 alone discharges every person's annual income-tax obligation.

## Penalties and interest

For late social contributions, the 2026 annual budget sets 0.1% of outstanding contribution debt per delayed day through actual payment inclusive. Apply the debt movements and statutory non-accrual cases; do not compound by adding accrued late charges to the contribution principal. CNAS normally calculates monthly without a special decision, while amounts arising from fiscal control have the stated SFS route. [Law 489 art. 28(1)–(4)][social]; [social budget art. 4][socialbudget]; [CNAS point 34][instructions].

Article 28(1^1) excludes the specified periods for inter-account transfer documents, VAT/excise-refund set-off requests, specially recorded discharged obligations and the stated transfers from another budget. Each exclusion has its own start date and amount limit. Qualifying agricultural employers' current-year social-contribution arrears begin the specified late-charge treatment from 1 November; distinguish opening arrears and the actual covered obligation. The due date itself is not erased. [Law 489 art. 28(1^1)–(1^2)][social]; [CNAS points 35–36][instructions].

A payer with no outstanding principal contributions/fines can request a budget-year late-charge instalment agreement while paying current obligations fully and on time. Obtain the actual CNAS agreement; this is not automatic forgiveness. [Law 489 art. 28(5)–(6)][social]; [CNAS points 37–39][instructions].

For medical premiums, the retained current Law 1593 art. 30 refers to the Fiscal Code art. 228 calculation. Do not apply the social 0.1% to medical premiums or repeat the old assertion that all arrears compound. The exact 2026 published daily tax/medical rate and complete intra-year commencement comparison remain to be retained and checked; use the actual CNAM/SFS assessment and applicable statutory periods. [Law 1593 art. 30][health]; [Fiscal Code art. 228][code].

False/missing returns and under-calculation can have sanctions distinct from daily late charges. Fiscal Code arts. 260–261 contain category-dependent filing fines and 20%–30% understatement/80%–100% evasion provisions, with the self-correction exception and other statutory conditions. This draft does not certify every administrative/offence or individual-payer category penalty; identify the actual notice and legal provision. [Fiscal Code arts. 232, 260–261][code].

## Cross-border points

Apply the governing social-insurance legislation and actual treaty before using a foreign-coverage exception. Foreign nationality, a foreign payer, travel, a residence certificate for income tax or a foreign insurance card alone does not establish the Moldovan contribution result. Obtain the employment/posting contract, work locations and dates, applicable social-security agreement, coverage certificate and competent-authority decision. Law 489 recognises international-agreement administration; exact partner-country allocation, certificate periods and aggregation rules remain unconfirmed here. [Law 489 art. 19][social]; [art. 49(1)(m), January version][socialjan].

For technical-assistance receipts, annex 3 point 6 requires an international agreement that actually exempts the specified contributions; “foreign-funded” alone is insufficient. For current foreign workers, separately test the narrow Law 200 art. 43^17 route referenced by Law 489 art. 19(6). For non-salaried health coverage and the more-than-183-days-abroad case, apply the medical-budget category/status rule above, not an income-tax residence shortcut. [Law 489 annex 3 point 6 and art. 19][social]; [medical budget art. 4(5)–(6)][medicalbudget].

## Two worked examples that recompute

### 1. Ordinary private employer: social cost and separate medical withholding

Assume an ordinary private employer and a fully worked month. An employee has covered accrued and paid salary plus bonus totalling 12,000, no excluded benefits, no special regime, and no minimum-base adjustment. Employer social contribution is 12,000 × 24% = 2,880. Employee medical premium is 12,000 × 9% = 1,080. Employer salary-plus-social cost is 14,880; remuneration after medical withholding but **before separately computed PIT or other deductions** is 10,920. It is not certified net pay. Both salary accrual and actual payment occur in the same month in this example. [CNAS point 9.2][instructions]; [medical budget art. 4(1)][medicalbudget]; [Law 1593 arts. 6, 20][health].

```oa-check
name: Moldova 2026 ordinary employer social and employee medical components
inputs:
  covered_gross_accrued_and_paid: 12000
  employer_social_rate: 0.24
  employee_medical_rate: 0.09
steps:
  employer_social: covered_gross_accrued_and_paid * employer_social_rate
  employee_medical: covered_gross_accrued_and_paid * employee_medical_rate
  employer_cost: covered_gross_accrued_and_paid + employer_social
  amount_before_pit_and_other_deductions: covered_gross_accrued_and_paid - employee_medical
expected:
  employer_social: 2880
  employee_medical: 1080
  employer_cost: 14880
  amount_before_pit_and_other_deductions: 10920
```

### 2. Part-time employee: the separate social minimum is not a health base

Assume the same ordinary 24% employer category, a complete month with a documented 10% working-time arrangement, accrued and paid remuneration 630 and no excluded benefits or special regime. The time-proportionate minimum is 6,300 × 10% = 630. Social on the actual/time-proportionate base is 151.20, but art. 22's separate floor is 25% × 6,300 × 24% = 378; employer social is therefore 378. Medical is 9% of actual covered remuneration, 56.70, with no assumed importation of the social floor. Employer cost is 1,008 and remuneration after medical but before PIT/other deductions is 573.30. If salary is paid in a later month, the percentage-medical payment timing changes; the social accrual record is preserved. [Law 489 art. 22][social]; [CNAS point 19.1, minimum-wage input][instructions]; [Law 1593 arts. 6, 20][health]; [medical budget art. 4(1)][medicalbudget].

```oa-check
name: Moldova 2026 part-time social floor and actual-remuneration medical base
inputs:
  national_minimum: 6300
  documented_work_fraction: 0.10
  actual_covered_remuneration: 630
  employer_social_rate: 0.24
  employee_medical_rate: 0.09
  minimum_contribution_fraction: 0.25
steps:
  time_proportionate_minimum: national_minimum * documented_work_fraction
  social_base_before_separate_floor: max(actual_covered_remuneration, time_proportionate_minimum)
  social_before_separate_floor: social_base_before_separate_floor * employer_social_rate
  separate_minimum_contribution: national_minimum * employer_social_rate * minimum_contribution_fraction
  employer_social: max(social_before_separate_floor, separate_minimum_contribution)
  employee_medical: actual_covered_remuneration * employee_medical_rate
  employer_cost: actual_covered_remuneration + employer_social
  amount_before_pit_and_other_deductions: actual_covered_remuneration - employee_medical
expected:
  time_proportionate_minimum: 630
  social_before_separate_floor: 151.20
  separate_minimum_contribution: 378
  employer_social: 378
  employee_medical: 56.70
  employer_cost: 1008
  amount_before_pit_and_other_deductions: 573.30
```

The predecessor's eight payroll/self-employment tests and six bank classifications remain in the archived original with their 2025 facts and arithmetic. They are not silently passed off as current 2026 examples. Current social-category calculations also have separate writer controls for agriculture, aviation, justice/founder amounts, patent months, the taxi transition, day work, IT-park insured income, independent-service allocation, voluntary agricultural rounding and arrears. Those controls are not independent legal review. The country ledger identifies which old tests still need the current individual/payroll/IT-park rules reconciled.

## Ask the client first

- Which payer/person category applies, with registration, activity, pension/disability, overlapping jobs and actual start/suspension/deletion dates? Supply the supporting records.
- What are the accrued gross, remuneration components, worked hours/fraction and actual payment dates? Supply contracts, payroll, nominal insured records, benefits and any statutory exclusion evidence.
- Does agriculture, special aviation, IT-park, taxi, day-work, patent, independent physician/justice practice or independent service activity apply, and for which months?
- For fixed health coverage, what annex-2 and State-insurance statuses apply, on which dates, with what salary-premium overlap, days uninsured/abroad and previous payments?
- Supply filed declarations, current CNAS/CNAM/SFS account statements, payment notices/receipts, corrections, refunds and arrears movements. A bank-only file does not establish the legal liability.
- For work across countries, supply exact locations/dates, the applicable agreement and competent-authority coverage certificate. PIT allowances, residence and net pay require their own verified facts.

## Sources

Read 30 October 2026. The retained source bodies, incomplete writer ledger and predecessor destinations are in [the social ledger](../../../ledgers/moldova-social-contributions.md) and country evidence. This is a local writer draft. No whole-country independent review or accountant attestation is claimed. Platform metadata and CTA are preserved.

| Primary source | Read scope and limit | Read on |
|---|---|---|
| [Law 489/1999, 2 October 2026 consolidation][social] | Selected charging/base/arrears provisions and annexes 2–3 read; annex 1 is an attached DOCX whose direct retrieval returned 403. CNAS 2026 instructions supply the stated tariff/category operating source | 2026-10-30 |
| [Law 489, January version][socialjan] | Art. 22 minimum wording checked against the current selected text | 2026-10-30 |
| [CNAS Order 31-A/2026 instructions][instructions] | Complete 2026 instruction PDF retained and read; 67 initial rule groups, with operating categories, deadlines and transitions | 2026-10-30 |
| [Law 320/2025, original annual social budget][socialbudget] | Arts. 3–4 fixed contributions and daily late charge; later budget amendment charging comparison remains open | 2026-10-30 |
| [Law 1593/2002, 1 July 2026 consolidation][health] | Premium framework, bases, categories, deadlines/status and penalty reference; complete 2026 version comparison remains open | 2026-10-30 |
| [Law 321/2025, medical budget, September consolidation][medicalbudget] | Art. 4 percentage/fixed/reduced amounts and category conditions read and retained; other annual-law interactions remain open | 2026-10-30 |
| [Current Fiscal Code][code] | Selected expense-benefit/enforcement provisions and independent-service period, single-tax allocation and medical-difference rules in arts. 69^23–69^26; no complete tax-code or payroll audit claimed | 2026-10-30 |
| [Finance Ministry 2026 overview][mfchanges] | Corroboration only; the 2,572 medical figure conflicts with the 2,527 statute and is not adopted | 2026-10-30 |

Not yet confirmed: directly retained operative Law 489 annex 1 tariff DOCX and full 2026 amendment/effective-date comparison; all Government benefit/travel/food/training and special-condition implementing procedures; complete current IPC21/IU17/IRM19/CAS18-AN annex/code and liquidation/reorganisation instructions; full State-insured health groups under Law 1585/1998 and every salary/fixed overlap or refund case; medical-penalty commencement and the actual published 2026 tax/medical daily rate; new service-entrepreneur eligibility/registration, monthly cumulative-band adjustments and medical-allocation rounding, partial-year/status-overlap and correction implementation beyond the sourced annual-difference method; full IT-park eligibility, 7%-turnover/30%-minimum/headcount and entry/exit methods; bilateral social-security agreements/certificates; full benefit-entitlement and labour-law computation. The old 2025 social amount 20,518 and monthly 1,709.84, minimum 5,500, average salary 16,100, net-pay test fixtures, personal allowance 29,700/2,475 and 360,000 gate, major 34,620, spouse/disability-dependent 21,780 and ordinary-dependent 9,900 figures, annual CET18/30-April and three-day foreign-citizen departure-return claims, and other-tax context (corporate/entrepreneur 12%, statutory farming 7%, SME 4%, VAT 20%/8%/6%, old VAT-registration 1.2/1.5/1.7-million thresholds and their asserted dates, and withholding) are archived predecessor subjects pending their own period/source reconciliation or companion Guide. They are not certified current rules here. The earlier defaults of assuming 24%, applying percentage rates to every self-payer, treating every ambiguous bank debit as a settled contribution, and compounding all arrears are replaced by explicit classification, evidence and debt-movement checks. All ordinary gaps keep the domain partial.

[social]: https://www.legis.md/cautare/getResults?doc_id=156677&lang=ro
[socialjan]: https://www.legis.md/cautare/getResults?doc_id=151170&lang=ro
[instructions]: https://cnas.gov.md/sites/default/files/2026-10/Particularitati2026.pdf
[socialbudget]: https://www.legis.md/cautare/getResults?doc_id=152321&lang=ro
[health]: https://www.legis.md/cautare/getResults?doc_id=152955&lang=ro
[medicalbudget]: https://www.legis.md/cautare/getResults?doc_id=156542&lang=ro
[code]: https://www.legis.md/cautare/getResults?doc_id=157050&lang=ro
[mfchanges]: https://mf.gov.md/ro/content/modific%C4%83rile-efectuate-%C3%AEn-codul-fiscal-pentru-anul-2026-privind-impozitul-pe-venit-tva

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
