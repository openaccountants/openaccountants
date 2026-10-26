---
name: armenia-payroll
description: "Use for Armenian ordinary 2026 salary payroll, distinct accrued salary and paid contract-income bases, PIT, pension participation and caps, stamp and health entry/continuation. Reconcile employee net pay, employer-funded exceptions, registration, the published monthly calculation and separate health obligations. Includes two conditional examples with supplementary controls preserved in the research record and the qualifying voluntary-pension deduction method. Trigger on Armenia payroll, salary tax, gross to net, SRC monthly calculation, employee registration or payroll corrections. Read alongside the individual and social-payment methods. Source-cited draft; ordinary labour entitlements and current statutory health timing are supplied, with the statutory benefit minimum and Service assessment/payment method supplied. The separate health payment-error implementation, specialist R&D branches, actual portal discrepancies, independent country review and accountant attestation remain open."
version: 0.3
jurisdiction: AM
tax_year: 2026
last_updated: 2026-10-26
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
sources:
  - https://www.arlis.am/hy/acts/215611/latest
  - https://www.arlis.am/hy/acts/224823
  - https://www.arlis.am/hy/acts/172160
  - https://www.arlis.am/hy/acts/230046
  - https://www.arlis.am/hy/acts/230432
  - https://www.arlis.am/hy/acts/223829
  - https://www.arlis.am/hy/acts/231489
---

# Armenia payroll: 2026 ordinary salary and statutory reconciliation

## Who this applies to

Source-cited draft for Armenian employers/agents preparing ordinary 2026 salary payroll, read 24 October 2026. Establish the employment relationship, tax-agent status, wage period, worker's residence/permit and each separate pension/stamp/health status. Read with `payroll-workflow-base`, [individual income tax](armenia-income-tax.md) and [social payments](armenia-social-contributions.md). Do not use a generic salary calculator to decide the legal classifications. Independent source review is recorded in the country research; named accountant attestation remains open.

Ordinary salary withholding does not replace the worker's annual declaration obligations. The current individual Guide distinguishes taxable, exempt and reportable income, the 2025-income November 2026 deadline and later general filing rules. Do not state that only income without withholding is reportable. [Tax Code 156/158][code]

## Rates, bands and thresholds

| Component | Ordinary 2026 branch | Source |
|---|---|---|
| Salary PIT | 20% of established taxable salary base | [Tax Code 143, 147, 150, 152][code] |
| Mandatory pre-retirement pension | 5% through 500,000 monthly base; above, 10% less 25,000; ordinary cap 87,500 | [Pension 5–6][pension] |
| Pre-1974 elected / continuing pension-age branch | Status-specific 5%, with statutory start/cessation rules | [Pension 5–6][pension] |
| Military stamp | Eligible monthly base through 1 million: 1,000; from 1,000,001: 15,000 | [Stamp 9–14][stamp] |
| Health, established eligible 2026 employee payer | 4,800 through 500,000 salary; 10,800 from 500,001; entry/continuation/funding conditions are separate | [Health 45–46][health] |
| Ordinary monthly PIT/social calculation and PIT payment | Following month's 20th, subject to applicable deadline rules | [Tax Code 156/158][code], [Pension 7][pension] |
| Statutory minimum monthly wage | 75,000, **excluding** the taxes/mandatory amounts and additions specified in wage Article 4 | [Minimum wage 1/4][wage] |

AMD amounts throughout. The wage law's 75,000 is not proof that a gross salary of 75,000 meets minimum-pay obligations. Check contractual base pay, working time, statutory exclusions, leave and applicable labour rules. The ordinary working-time, minimum-pay and entitlement method below supplies the calculation; specialist employment categories require their stated separate rules. [1–4][wage]

Obtain: employee identity/registration and start date; contract and hours; ordinary/bonus/benefit/leave/civil-contract categories; accrued and paid amounts by month; birth date, permits and pension elections/cessation/cap waiver; other employers/sources; health-register entry/notice, continuation, state-paid and social-package status; tax invoices/support for any exemption; prior payroll returns, corrections and treasury allocations.

## The base

1. **Classify and place the income.** Resident and non-resident source rules, employment versus contract/service/owner payment, and tax-agent obligations must be established. Salary/equivalents use the **accrual method** under 142(1)(1). Civil-contract work/services and specified temporary-incapacity/maternity benefits use the stated **cash method** under 142(1)(3)/(4). A late bank payment does not move ordinary earned salary to that later payroll month. [140–143, 151–153][code]
2. **Determine PIT base.** Ordinary eligible taxable salary less lawful Article 147 deductions/exclusions, then Article 150 rate. Do not automatically subtract mandatory pension, stamp or health from gross to obtain PIT base. Also do not claim there are no possible salary deductions: qualifying voluntary-pension contributions have Article 147(1)(3)'s five-percent-of-tax-base limit. The published monthly form provides its specific inverse-base formula below. Benefits, reimbursements, insurance and leave payments require their own provision. [143, 147, 150][code]
3. **Select the rate.** Ordinary salary is 20%. Article 150 contains conditional special branches, including approved R&D treatment; do not apply a reduced rate merely because an employer describes itself as IT or research. Use the actual approval/list, activity and employee evidence before that branch. This Guide's ordinary controls use 20%. [150][code]
4. **Compute pension independently.** Apply the current social Guide's participation, salary/contract base, ordinary/elected/pension-age limb, ceiling and waiver. Aggregate-source excess is not an automatic credit in one employer's payroll. [Pension 2/5–7][pension]
5. **Compute stamp independently.** Establish monthly population, each agent's base and residence-status exclusion. No-income, insufficient civil-contract income and military-family refund cases have specific rules. Do not treat a parent's refund eligibility as a current payroll exemption. [Stamp 9–15][stamp]
6. **Compute health independently.** Establish phase entry and payer status, then current salary branch, continuing twelve-month obligation, social-package/state-funding, no/insufficient salary, termination and multiple employers. The current month being below 200,001 does not prove zero for an already entered payer; salary reaching the threshold in January–November 2026 first triggers the following-month branch. Health contributions are not included as a new field in the specified 2026 monthly calculation. [Health 11–16, 45–46][health]
7. **Reconcile employee net and employer funding.** Start with gross cash salary due; subtract legally employee-borne PIT/pension/stamp/health and other authorised deductions. Keep employee self-payments and state financing separate. Employer-funded childcare pension, insufficient-income agent obligations, employer-paid benefits and voluntary employer coverage require separate cost/receivable treatment. Do not assert universal employer cost equals gross salary or universal zero employer social payment. [Pension 6(10)][pension], [Stamp 11(3.1)][stamp], [Health 14(9), 46(20)][health]

### Ordinary benefits need separate PIT and pension classification

| Component | PIT treatment and period | Pension salary-equivalent treatment |
|---|---|---|
| Salary, ordinary bonuses and paid annual leave | Ordinary taxable employment income; accrual method | Included in joint416-N/107-N/561-N list1(1)–(2), subject to participant/cap rules |
| Unused-leave compensation at termination | Expressly excluded from147(1)(12)'s reimbursement exemption | Expressly included in joint list1(2) |
| Statutory temporary-incapacity and employed/self-employed maternity benefits under the named Benefits Law | Exceptions to147(1)(1)'s benefit exemption; cash method under142(1)(4). Use distinct form1.10–1.12 fields and applicable event-date instructions | Excluded from joint list1(1)(e)'s wage-fund one-off limb; do not add to pensionable salary merely because PIT is due |
| Documented employment-expense reimbursement | Excluded only within147(1)(12)'s statutory limits, including117travel limits. Excess has no exemption under this limb | Apply the actual joint list compensation exclusion; an undocumented salary supplement is not established statutory compensation |
| Employer private health premiums |147(1)(29)'s exclusion is up to10,000 per worker per income month | Determine the actual benefit's classification under the list; the PIT limit is not a pension-base deduction |
| Statutory universal-health premium for a person/related person | Separate147(1)(29) statutory-health exclusion; do not impose the private-health10,000cap on it | Separate health obligation/benefit; no automatic reduction of pensionable cash salary |
| Qualifying voluntary-pension contribution |147(1)(3)'s five-percent-of-tax-base limit and field1.9 inverse formula below | Not the mandatory pension withholding; keep the salary base and this PIT exclusion separate |

[Tax Code142/147(1)(1)/(3)/(12)/(29)][code]; [joint salary list1][salarylist]. Insurance compensation has147(1)(4)'s separate exemption and voluntary-pension-funded exception. Taxability does not decide who funds or computes a statutory benefit: the ordinary labour/benefit entitlement and payment calculation is supplied separately below. This table does not certify a generic employer “aid” label as exempt. [147(1)(4)/(33)][code]

For the simple fully taxable cash-salary case only:

`employee_net_due = gross_salary − PIT − employee_pension − employee_stamp − employee_health`.

This is not a formula for every benefit, civil contract, recovery, unpaid period or employee self-payment.

### Establish the pay entitlement before withholding

Keep the actual work calendar and contract separate from the tax calendar. Ordinary working time is at most **40 hours/week and eight/day**; including overtime the ordinary maximum is **12/day (including the stated meal/rest break) and 48/week**. The Code has separate reduced-hours, summed-time and continuous-duty branches. Overtime outside Article 145's exceptional cases requires written consent under 144; protected categories have additional restrictions. A payroll calculation is not permission to schedule unlawful hours. [Labour Code 139–144][labour]

For ordinary overtime, pay the normal hourly rate **plus at least 50%**; night work attracts the normal rate **plus at least 30%**. If the normal-rate component is already in monthly pay, add the premium without duplicating that component. Under 185, unscheduled rest/holiday work uses the agreed statutory double-rate or paid-time alternative; scheduled statutory holiday work is at least double. The expressly listed martial-law/continuous-service exceptions need their actual conditions. [184–185][labour]

The Minimum Wage Law sets **AMD 75,000/month**, or the stated hourly minima **450 at 40 hours/week, 750 up to 24 hours/week, 500 at 36 hours/week**, with its special-sector calculation. Article 4 excludes wage taxes, social/other statutory mandatory payments and supplements/bonuses from those minima. For a full-time monthly worker, solve the basic-pay gross-up using that person's actual mandatory deductions so the qualifying basic pay after those deductions meets the statutory minimum; do not count a bonus or assume gross 75,000 suffices. Recheck the pension/stamp/health bands after gross-up rather than applying one universal percentage. Part-time remuneration follows actual time or output under 187, while reduced statutory working hours are a different classification. Ordinary salary is calculated monthly and paid on working days at least monthly by the **next month's 15th**; cashless-payment requirements remain applicable. [Minimum Wage Law 1–4][wagecurrent]; [187, 192][labour]

### Annual leave and final settlement

The statutory ordinary annual minimum is **20 working days for a five-day week or 24 for six days**; part-time hours do not reduce that duration. The working year starts on the employee's start date, not automatically 1 January. First-year leave is ordinarily after six continuous months, with the statutory exceptions and earlier leave by agreement. Track actual qualifying service under 165, including the specified retained-job/pay periods, temporary incapacity and paid leave; do not replace the service ledger with a universal monthly accrual assumption. A split leave must include one block of at least **10 working days (five-day week) or 12 (six-day week)**. Apply extended/additional-leave qualification separately. [159–165][labour]

For Labour Code benefits, Article **195** supplies a distinct average-pay method. Start with all remuneration under that employer/contract in the 12 months before the event month. Apply its exclusions for incapacity, leave, specified downtime/military periods and the hiring month. Where the remaining period is shorter, divide non-award remuneration by those months and include awards at **one twelfth**, including awards from excluded months under the stated rule. Apply the contract/statutory-rate fallback when the Article 195(2) fallback conditions apply, and its monthly/hourly minimum safeguard. Daily average is **monthly average/21** for a five-day week or **/25** for six days; for less than one month's employment, use remuneration for days actually worked divided by those days. Hourly average follows 195(4)'s actual-hour/fallback method. Do not reuse the separate statutory sickness-benefit average below. [195][labour]

Annual leave pay is daily average × granted working leave days. Pay ordinarily at least **three days before** leave; the independent-cause exception and employer-caused delay extension have their own rules. Leave cannot generally be replaced with cash while employment continues. On termination, compensate **all unused annual leave**, including the specific short-service/fixed-term cases, using the established unused days and average daily pay. [169–170][labour]

Classify the termination ground before calculating severance. Labour 113(1)(1)/(2)/(4) (the specified cessation, redundancy and reinstatement cases) gives **one average monthly salary** under 129. For 113(1)(3)/(7), 109(1)(9) and 124's stated grounds, the continuous-service scale is **10 average daily wages for under one year; 25 for one to under five; 30 for five to under ten; 35 for ten to under fifteen; 44 for fifteen or more**. A contract can provide more. This is not universal severance for every resignation. Notice and notice-delay compensation are separate under 115. Full settlement is due **on termination day**, subject to the stated legal/agreed exception; inability independent of the employer uses the five-working-day clock after the employee's demand. Retained employment on an internal/successor transfer is not automatically termination settlement. [113, 115, 129–130][labour]

Statutory severance and unused-leave compensation are different tax categories. Apply Code 147(1)(1)'s statutory-benefit exemption to the qualifying statutory severance; 147(1)(12) expressly **excludes unused-leave compensation from its compensation exemption**. Do not relabel contractual extras as statutory exempt benefits without their basis. The joint salary list includes paid leave and unused-leave compensation but excludes its stated statutory compensation/benefit amounts from the one-off wage-fund limb. Keep the corresponding pension base and withholding fields separate. [147(1)(1)/(12)][code]; [joint salary list 1(1)(e), (2)–(3)][salarylist]

### Temporary incapacity and maternity

Use the case's **first day** to choose the law. Actual **HO-73-N 11**, official clarification **1-2025**, and current Government **1024-N**, replaced by **1241-N**, apply the new method where incapacity starts **1 September 2025 or later**, including ordinary new 2026 cases. Do not import the older five-working-day employer model into these cases. Actual employment/self-employment, paid/calculated tax, residence registration for foreign/stateless persons, medical entitlement and the stated exclusions must be established. [Benefits Law 4–6][benefitlaw]; [HO-73-N 11][benefitchange]; [official clarification][benefitclarification]; [1024-N commencement/Annex 5][benefitprocedure]

For an employee's sickness, pay the certified **calendar days from the first day**. The tax-agent employer funds the **first seven calendar days** on the Unified Social Service's calculation; the Service/state funds **day eight onward**. Where the employer is exempt from tax-agent duties, the state payer branch applies. Maternity is state-funded except the permitted employer top-up. Benefits do not create duplicate ordinary salary for the same incapacity period. Ordinary illness, prosthetics, sanatorium and family-care cases have the different duration/medical conditions in Articles 8–12; do not assume an unrestricted annual day count. [6, 8–12, 24(15)][benefitlaw]

The benefit average is not Labour 195's leave average: under **Benefits Law 22**, use the preceding **12 consecutive calendar months**, divide the relevant earnings by **12**, include statutory benefits as specified and use the tax database at the first incapacity day. Apply the child-care-month substitution, earlier-employer rule where current service is under 12 months (one prior employer per month, the highest-income one), and separate multi-employer sickness versus combined maternity rules. Self-employed income uses the prior year's statutory business base with passive/freight exclusions and special turnover/micro periods; the Government procedure supplies its minimum-base branches. [22(7)–(14)][benefitlaw]; [1024-N Annex 5, 9–18][benefitprocedure]

Let **M** be the benefit-law minimum: the Minimum Wage Law Article 1 amount plus its income tax, under Benefits Law 22(1). **Article 4 excludes taxes from the 75,000 wage minimum.** Therefore the ordinary 20% PIT tax-inclusive benefit base solves **M − 20% × M = 75,000**, giving **M = AMD 93,750**. Adding 20% of the already tax-exclusive 75,000 would leave only 72,000 after PIT and fail that reconciliation. This is an income-tax-only gross-up for the benefit definition; pension, stamp, health and other contractual minimum-pay adjustments are separate. The amount is derived from the current statutory definition and exclusions, rather than an asserted Service quotation or the generic 1,000-dram multiplier. [Benefits Law 22(1)][benefitlaw]; [Minimum Wage Law 1/4][wagecurrent]; [Tax Code 150(1)][code]; [current Ministry minimum-wage explanation][minimumfaq]

For the ordinary 20% branch, **0.5M = 46,875**, **5M = 468,750**, **10M = 937,500** and **15M = 1,406,250** AMD. The Ministry's historical 2015 worked examples likewise used an income-tax-inclusive minimum above the tax-exclusive wage figure; those historical numbers are not 2026 rates or caps. Current 2026 assignment and calculation belong to the Unified Social Service under Article 24: use its notified employer-funded amount for payment and reconcile the underlying period, statutory base and population. Correct disputed underlying records/calculations through the Service process rather than silently replacing its notice with a private calculator. [22/24][benefitlaw]; [1024-N Annex 5, 3/9/17–20/29][benefitprocedure]; [Ministry 2015 explanation, historical context only][historicalbenefit]


Let **A** be the statutory average monthly salary/income computed above. Apply these tests before daily conversion. [22(1)–(6)][benefitlaw]

| Population / benefit | Monthly calculation base |
|---|---|
| Employee sickness | If **A < 0.5M**, use **0.5M** under 22(6). Otherwise use **min(80% × A, 10M)** under 22(2)–(3). The floor test compares A itself, not the amount after the 80% reduction. |
| Employee maternity | If **A < 0.5M**, use **0.5M**; otherwise **min(A, 15M)**, subject also to the separate Government minimum-total rule below. |
| Self-employed | Apply the same statutory average-income floor test and the separate **5M** ceiling to the sickness percentage or maternity average under 22(4); the 4(3.1) special maternity branch instead uses the expressly prescribed 0.5M. |

**Self-employed overrides come first.** Under current **1024-N Annex 5(17)(2)**, a person in the turnover-tax system when incapacity arises has the benefit calculated from **0.5M**, regardless of a higher prior-year general-system average. Paragraph **17(3)** likewise uses 0.5M where the prescribed preceding-year profit-tax base is absent; apply 17(1) for its separate below-minimum preceding-year case. These rules override the ordinary average/percentage/cap row; they are not permission to invent a prior-year base. Ordinary self-employed maternity also requires activity suspension for the entitlement period under **12(2)**, except the expressly stated Benefits Law **4(3.1)(2)–(3)** cases. Paragraphs 13–15 separately govern those maternity exceptions and combined employee/self-employed income; do not deny every maternity case merely because no profit tax was paid. Confirm the tax regime, prior-year base, dates and reported suspension before calculating. [1024-N Annex 5(12)–(18)][benefitprocedure]; [4(3.1)–(3.2), 22][benefitlaw]

For an algebraic illustration, A = **0.55M** gives employee sickness base **0.44M**, while A = **0.4M** triggers base **0.5M**. Do not impose a floor on every result after applying 80%. Divide the applicable monthly base by **30.4**, then multiply by eligible calendar days, splitting employer/state days for sickness. This differs from leave's /21 or /25. The Service's actual calculation must reconcile to the statutory inputs and the relevant tax-inclusive M. [22(1)–(6), (15)–(20)][benefitlaw]


Ordinary maternity leave is **140 calendar days**, **155** for the specified complicated birth and **180** for multiple birth, with the adoption/early-birth/surrogacy branches. Government Annex 5(20) sets the minimum **total** maternity amount at **(50% × M) / 30.4 × 140 days**, or **70 days for its premature-birth case**. At ordinary M = 93,750, the 140-day minimum is **215,871.710526… AMD before payment rounding and PIT**, not a rounded net payment. Compare the calculated maternity total with the applicable minimum; do not use 140 days to replace the actual 155/180-day entitlement. Sick leave during unpaid or child-care leave and the self-employed suspended/micro/border-exempt cases have their specified denial/exception rules; maternity's self-employed exception is separate. [Labour 172][labour]; [Benefits Law 4, 11, 22][benefitlaw]; [1024-N Annex 5, 12–20, 25–26][benefitprocedure]

The current ordinary process is electronic: the e-health certificate opening/closing reaches the Service, then SRC/employer, using Article 24's separate **one-working-day** data steps. After the required SRC income data arrives, the Service has **five working days** for calculation; SRC transmits the employer-funded amount within its following **one working day**. The employee ordinarily files no separate application/documents under Annex 5(4); protected data, court/death and foreign-certificate cases have their own paths. Employer-funded sickness is paid by the salary deadline for the calculation/award month; state benefits by the specified upcoming salary deadline through the chosen bank. Appointment/payment/refusal notification has its separate **three-working-day** clock. E-social or individual Azdarar notice is not evidence the bank has already settled. [24(1)–(9), (16)][benefitlaw]; [1024-N Annex 5, 3–8, 27–31][benefitprocedure]

PIT is calculated from these statutory incapacity/maternity benefits under Code 147(1)(1)'s exceptions and the applicable cash/benefit form instructions; do not add them to pensionable salary just because PIT is due. Reconcile the employer's payment with the Service's state portion and the actual period; a benefit certificate is not a generic salary accrual or an automatic employer tax credit. [142, 147][code]; [1024-N Annex 5(24)][benefitprocedure]

[labour]: https://www.arlis.am/hy/acts/51/latest
[wagecurrent]: https://www.arlis.am/hy/acts/172160/latest
[benefitlaw]: https://www.arlis.am/hy/acts/205733/latest
[benefitchange]: https://www.arlis.am/hy/acts/205729/latest
[benefitclarification]: https://www.arlis.am/hy/acts/206406/latest
[minimumfaq]: https://welfare.gov.am/labor-legislation-faq
[historicalbenefit]: https://old.mlsa.am/?p=4879
[benefitprocedure]: https://www.arlis.am/hy/acts/196905/latest


## Deadlines and filing

Tax Code 156(2) requires the specified new-employee registration no later than the end of the day before actual work begins; same-day hiring/start has its **14:00** rule. Residence-status foreign-worker and limited-information exceptions require their actual branch. Do not treat company registration on e-register as the employee payroll registration filing. [156][code]

Published **Order 300-N**, consolidation applicable from **15 April 2026**, Annex 1 is the monthly calculation; Annex 2 the qualifying simplified calculation; Annex 3 annual calculation/declaration; Annexes 4/5 income information/certificates. This is actual published mapping, not a verified live SRC session. [300-N][form]

| Annex 1 field | Published purpose / reconciliation |
|---|---|
| 1.1–1.4 | Identity, public-service identifier and occupation code |
| 1.5 | Pension-participation code: 1 nonpayer; 2 payer; 3 application-based payer |
| 1.6 | Salary and equivalents accrued for the reporting month |
| 1.7 | Civil-contract work/services actually paid in the month |
| 1.8 | Other specified taxable base, excluding the benefit columns |
| 1.9 | Qualifying voluntary-pension deduction under the specified cap |
| 1.10–1.12 | Distinct employer/state benefit amounts and recovery; instructions include the pre-1 September 2025 incapacity-event gate |
| 1.13 / 1.13.1 | PIT / specified foreign tax under applicable treaty branch |
| 1.14 / 1.14.1 | Social / stamp payment |
| 1.15 | Actual hours worked |

The instructions provide one row per specified employee even without income in the reporting month. Pension code 3 is not code 1. A restricted/no-residence-status population can require summary or special reporting rather than the ordinary individual row. Check the operative instructions and actual identity/status, not a guessed code. [Annex 1 instructions 2–6; Tax Code 156][form] [Code][code]

For field 1.9 the published instruction uses, for its stated included-income total **S**, maximum `S − S/1.05`, as well as actual qualifying contributions. This is not simply 5% of an unadjusted gross amount; confirm every included component and qualification before using it. Statutory mandatory pension deductions are a different item and do not populate 1.9. [Tax Code 147(1)(3)][code], [Annex 1 instruction 5][form]

Ordinary tax-agent monthly return and PIT payment are due through the following month's20th; reconcile social deadlines via Pension7 and stamp via14. **Health:**46(14) excludes the specified premiums from the2026monthly tax calculations. Under46(13), amended salary reductions do not reduce the health calculation basis. Maintain a separate ledger and use the [social Guide's payment/register/refund workflow](armenia-social-contributions.md#separate-health-payment-and-register-workflow), including the three published account populations. For its specified December 2025/2026 transitional population, current 46(11) supplies the **20th inclusive of the payer-status month**. Apply that statutory transition to that population; general 14(3) and an older leaflet do not replace it. Retain the actual Fund status/payment notice for reconciliation. The entrepreneur/notary2026deadline is separately20July2026. [Tax Code151/156/158][code], [Pension7][pension], [Stamp14][stamp], [Health14/46][health], [Fund accounts][healthaccounts]

**Form date gate:** September **1003-N** is not an October 2026 form rewrite. Its crypto-related specified changes start **1 December 2026**, ordinary bank-dividend changes **1 February 2027**, and the specified managed-property changes **1 June 2027**, under paragraphs 2–3. It does not create a current ordinary salary health column. Earlier/historical rates in form tables also do not override current Code categories and dates. [1003-N][form-amend]

## Penalties and interest

Reconcile original and amended personal rows, periods, taxable base, employee withholding and authority accounts. **Tax Code152(2) has different look-backs:** an agent can recover late/unwithheld or under-withheld PIT from the individual under the applicable legal procedure for **no more than the last three months**. Over-withheld PIT is offset against future withholding or refunded **within one month after discovery**, for **no more than the last three years**. A three-month refund limit is wrong. These employee-recovery/refund rules do not excuse the agent's liability to the tax authority or authorize unrestricted employment-law deductions. [152(1)–(3)][code]

Prepare an amended calculation for the **original income period**, retaining the original and amended worker rows and bridge by tax, pension, stamp and net pay. Pension8(2) records additional liabilities/reductions arising from an amended calculation on its submission date. If the worker's employment/civil contract has ended by then and the amended return changes that person's social liability,8(4) records the resulting difference as the filing employer's additional amended-return liability. Do not debit an invented former-worker payroll account or use the PIT recovery window as a pension rule. Health46(13)'s disregard of downward salary amendments and46(14)'s separate2026reporting remain in force. [Pension8(2)/(4)][pension]; [Health46(13)–(14)][health]

PIT arrears: Tax Code 401 provides 0.075% daily with its 730-day limit, and 402 prescribes 5% per completed fifteen-day late-filing period capped at calculated tax, subject to actual event/population. Health Article 16’s import of tax-law late-payment terms starts **1 January 2027** under Article 45(1)(8). Do not use it as a 2026 health-interest authority; any other operative 2026 sanction/collection basis must be established separately. **Stamp Article 13(4) excludes tax-law late-payment interest** while preserving enforcement. Do not apply the PIT rate to all contribution debts or treat filing as payment. [401–403][code], [Health 16, 45(1)(8)][health], [Stamp 13][stamp]

## Cross-border points

Foreign-resident status, Armenian tax residence, Armenian-source pay, pension residence permit and health eligibility are separate tests. A no-agent foreign-employer case, posting, treaty credit or social-security agreement requires its own evidence and route. The form's foreign-tax column does not itself prove treaty entitlement. No actual residence certificate, agreement relief or foreign tax credit is verified by these salary examples. [Tax Code 25/141/156][code], [Pension 5][pension], [Health 11/45][health]

## Two worked examples that recompute

Hypothetical AMD inputs. Each assumes fully taxable ordinary cash salary, known participation and current health payer status unless expressly stated otherwise; no other deductions, exemptions or employer-funded benefits. These controls do not prove minimum-pay compliance, health entry or accepted filing.

### 1. Established ordinary payer, salary 300,000

PIT 60,000, mandatory pension 15,000, stamp 1,000, employee health 4,800; net due 219,200. Ordinary non-social-package status and applicable funding established. [Tax Code 150][code], [Pension 6][pension], [Stamp 12][stamp], [Health 46][health]

```oa-check
name: Armenia ordinary salary 300000 net due
inputs:
  gross_salary: 300000
steps:
  - pit: gross_salary * 0.20
  - pension: gross_salary * 0.05
  - stamp: 1000
  - health: 4800
  - net_due: gross_salary - pit - pension - stamp - health
expected:
  pit: 60000
  pension: 15000
  net_due: 219200
```

### 5. New health threshold trigger versus following month

No prior entry/other covered-payer branch; salary first reaches 250,000 in January 2026 and is unchanged in February. Under the established Article 45(1)(4) facts, compare January without this health contribution to February after entry: net 186,500 versus 181,700. Mandatory pension and stamp apply in both. Register and commencement evidence are assumed established, not derived by arithmetic. [Health 45–46][health] [Pension][pension] [Stamp][stamp] [PIT][code]

```oa-check
name: Armenia health entry following month salary comparison
inputs:
  monthly_salary: 250000
steps:
  - pit: monthly_salary * 0.20
  - pension: monthly_salary * 0.05
  - net_before_entry: monthly_salary - pit - pension - 1000
  - net_after_entry: net_before_entry - 4800
expected:
  net_before_entry: 186500
  net_after_entry: 181700
```

## Ask the client first

- Which salary month, actual work dates, contract type, gross components, paid/accrued amounts and hours apply?
- Which residence/permit, pension election/cessation/cap waiver, childcare leave and other employers are documented?
- Which health entry month/continuation, social-package/state-paid status and Fund notices apply?
- What benefits, reimbursements, qualifying voluntary contributions, R&D approval and earlier-period corrections exist?
- Which returns, registration confirmations, payment allocations, net-pay balances and assessments reconcile?

## Sources

| Official source and actual read scope | URL | Read on |
|---|---|---|
| Current Ministry minimum-wage FAQ, 75,000 and exclusion of taxes; historical 2015 Ministry benefit examples read from search-retained primary text, original URL now opens the ministry homepage | https://welfare.gov.am/labor-legislation-faq ; https://old.mlsa.am/?p=4879 | 2026-10-26 |
| [Current Armenian Tax Code][code], targeted Articles 142, 147(1)(3), 150–158, 401–403; actual current Armenian accrual, deduction, monthly and registration provisions checked against supporting [official English](https://www.arlis.am/en/acts/231892). | https://www.arlis.am/hy/acts/215611/latest | 2026-10-24 |
| [Funded Pensions law][pension], targeted Articles 2, 5–8 and current metadata; distinct payment populations and employer-funded childcare rule. | https://www.arlis.am/hy/acts/224823 | 2026-10-24 |
| [Stamp law][stamp], targeted Articles 9–15; [HO-477-N](https://www.arlis.am/hy/acts/218648) date gate. No universal PIT interest import. | https://www.arlis.am/hy/acts/230046 | 2026-10-24 |
| [Universal Health Insurance law][health], current September consolidation, targeted 11–16 and 45–46; salary entry, continuation, funding, separate 2026 reporting/payment. | https://www.arlis.am/hy/acts/230432 | 2026-10-24 |
| [Minimum Monthly Wage law][wage], Articles 1–4 and statutory exclusions. | https://www.arlis.am/hy/acts/172160 | 2026-10-24 |
| [Actual 300-N form/instructions][form], Annex 1 identity, pension status, bases/deduction, benefits and tax/social/stamp fields; current metadata. This does not establish a live portal session. | https://www.arlis.am/hy/acts/223829 | 2026-10-24 |
| [Actual 1003-N][form-amend], paragraphs 1–3 and 29 September 2026 publication; December 2026 / February and June 2027 branches kept separate. | https://www.arlis.am/hy/acts/231489 | 2026-10-24 |

| Fresh current native Tax Code142,147(1)(1)/(3)/(4)/(12)/(29)/(33),152(1)–(3): benefit bases/accrual, health/voluntary-pension distinctions, three-month recovery versus three-year refund and one-month remedy | https://www.arlis.am/hy/acts/215611/latest | 2026-10-26 |
| Complete joint416-N/107-N/561-N salary-equivalent list1 and current metadata | https://www.arlis.am/hy/acts/126230/latest | 2026-10-26 |
| Fresh nativePension8(2)/(4) and Health46(11)–(16): amended liabilities/former workers and separate health calculation/reporting | https://www.arlis.am/hy/acts/224823/latest ; https://www.arlis.am/hy/acts/230432/latest | 2026-10-26 |
| Current native Labour Code, targeted 113/115/129/130, 139/140/144, 158–165/169/170/172, 184/185/187/192/195 | https://www.arlis.am/hy/acts/51/latest | 2026-10-26 |
| Current Minimum Wage Law 1–4, ordinary monthly/hourly and exclusions | https://www.arlis.am/hy/acts/172160/latest | 2026-10-26 |
| Current Benefits Law, targeted 4–12/22/24, ordinary bases/payer/day/clock method | https://www.arlis.am/hy/acts/205733/latest | 2026-10-26 |
| Actual HO-73-N 11 and official clarification 1-2025, September 2025 first-day gate | https://www.arlis.am/hy/acts/205729/latest ; https://www.arlis.am/hy/acts/206406/latest | 2026-10-26 |
| Current Government 1024-N, operative 1241-N replacement, Annex 5 1–31 and targeted Annex 2/data/commencement | https://www.arlis.am/hy/acts/196905/latest | 2026-10-26 |
| Current Fund native payment instructions, all three routes; full implementation/source record in companion social Guide | https://www.uhif.am/am/requisites | 2026-10-26 |

Read/reused 24 October 2026:


[code]: https://www.arlis.am/hy/acts/215611/latest
[pension]: https://www.arlis.am/hy/acts/224823
[stamp]: https://www.arlis.am/hy/acts/230046
[health]: https://www.arlis.am/hy/acts/230432
[wage]: https://www.arlis.am/hy/acts/172160
[form]: https://www.arlis.am/hy/acts/223829
[form-amend]: https://www.arlis.am/hy/acts/231489


[salarylist]: https://www.arlis.am/hy/acts/126230/latest
[healthaccounts]: https://www.uhif.am/am/requisites

Targeted commencement recheck, **25 October 2026**: [current Health Law arts. 16 and 45(1)(8)](https://www.arlis.am/hy/acts/230432/latest) expressly defer article 16 until 1 January 2027. Other source read dates remain as recorded.

**Not yet confirmed:** operative Government procedure/commencement for Health 14(12) mistaken/no-liability payments and the specified suspended/age-65 entrepreneur refund implementation. Ordinary working-time, minimum-pay, leave and termination methods and the current statutory health transition are supplied; the ordinary benefit method now states the explicit statutory tax-inclusive calculation and uses the Service notice for payment, with the statutory inputs reconciled separately. Specialist employment/R&D/foreign-status branches, actual portal signatures/rounding/acceptance and enforcement/remedies remain separate boundaries. These are conditional exceptional-payment/refund boundaries, distinct from the ordinary contribution/payroll method and supplied participant-excess procedure. No country approval or professional attestation is claimed.

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
