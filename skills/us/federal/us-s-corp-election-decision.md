---
name: us-s-corp-election-decision
description: Compare a US sole proprietorship or single-member LLC with an S corporation for 2026, and check the 2027 election deadline. Covers entity eligibility, evidence for reasonable compensation, employment tax with other wages, QBI, quoted costs, Form 2553 timing, late-election relief and revocation. Produces a conditional decision brief; state, conversion and uncommon ownership issues require partner review. Trigger on S corp election, Form 2553, reasonable salary or saving self-employment tax.
version: "1.2"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: decision
---

# US S corporation election decision, tax year 2026

Compare total after-tax cost at a salary supported by evidence; a distribution gap alone does not establish a saving.

## Scope

This is a federal decision brief for a Schedule C sole proprietor or disregarded single-member LLC considering an election, or an existing S corporation considering whether to continue. The calculations are for 2026; only the election deadline is supplied for 2027. Do not reuse 2026 indexed amounts for 2027.

## Ask the client first

Read the available records before requesting missing facts. Obtain entity and ownership documents (including community interests and classification-election history), intended effective date, existing election notices, expected profit in both a normal and a low year, duties/hours/comparable pay, each owner's Social Security and Medicare wages, filing status and the joint spouse's Medicare income, other income/deductions and QBI facts, business locations, and actual recurring cost quotes. Missing salary evidence or cost quotes means a conditional comparison, not an invented salary or cost.

## The method, step by step

### 1. Eligibility and compensation

Form 2553 is for a corporation or an entity eligible to elect corporate treatment. An individual sole proprietor cannot file it for an unincorporated business. An eligible LLC meeting the tests and making a timely S election generally has a deemed corporate-classification election; a separate Form 8832 is unnecessary. Previous classification changes can restrict another change: do not assume a fresh LLC election is available without reviewing its history. [Form 2553 instructions, Purpose/Who May Elect](https://www.irs.gov/instructions/i2553); [26 CFR 301.7701-3(c)(1)(iv)-(v)](https://www.ecfr.gov/current/title-26/section-301.7701-3).

Eligibility requires a domestic eligible entity, no ineligible financial institution using the section 585 reserve method, subchapter L insurance company, DISC or former DISC; no more than 100 shareholders after the statutory spouse/family counting rules; eligible individual, estate, qualifying trust or section 401(a)/501(c)(3) owners; no direct nonresident-alien shareholder; one class of stock with identical distribution/liquidation rights (voting differences alone are permitted); an allowed tax year; and required shareholder consents. The nonresident-alien restriction has an ESBT-beneficiary exception. This Guide's calculation scope is one individual owner; estates, trusts, exempt owners, family counting, spouses/community property and multiple owners need partner review rather than an automatic rejection. [26 U.S.C. 1361(b)-(c)](https://uscode.house.gov/us/usc/t26/s1361/); [Form 2553 instructions, tests 1–8](https://www.irs.gov/instructions/i2553).

**AUDIT FLASH POINT.** Pay reasonable compensation for shareholder-employee services before non-wage distributions. IRS may reclassify distributions as wages; the reasonable-compensation amount cannot exceed what the shareholder receives directly or indirectly. Assess services, staff and capital generating receipts, including the owner's administrative work. Document training, duties, time, dividend history, staff pay, bonuses, comparable pay, agreements and compensation formula. No salary percentage or “close to profit” default is supplied here. Without evidence, leave salary unresolved and show only explicitly hypothetical calculations. [IRS compensation guidance](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues).

The IRS guidance lists Joly v. Commissioner, T.C. Memo. 1998-361, aff'd 211 F.3d 1269 (6th Cir. 2000); Veterinary Surgical Consultants, P.C. v. Commissioner, 117 T.C. 141 (2001); Joseph M. Grey Public Accountant, P.C. v. Commissioner, 119 T.C. 121 (2002); and David E. Watson, P.C. v. United States, 668 F.3d 1008 (8th Cir. 2012). These are references to its compensation discussion, not salary safe harbours.

### 2. Compare payroll tax

| Figure and operative condition | 2026 amount | Official source |
| --- | --- | --- |
| Regular SE tax: Social Security part subject to the owner's remaining annual base; Medicare part uncapped | 12.4% plus 2.9% | [26 U.S.C. 1401(a)-(b)](https://uscode.house.gov/us/usc/t26/s1401/) |
| Positive ordinary Schedule C profit: net-earnings factor, before the Schedule SE filing/coverage tests | 92.35% | [Schedule SE line 4a](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf) |
| Social Security base, each individual, coordinating that individual's covered wages and SE earnings | USD 184,500 | [2026 Schedule SE instructions](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf) |
| Covered S corporation salary: employer and employee each pay Social Security to the employer's wage base, plus uncapped Medicare | 6.2% plus 1.45% each | [Pub. 15, section 9](https://www.irs.gov/publications/p15) |
| Additional Medicare liability: excess Medicare wages and positive SE income; joint return combines spouses, separate Social Security bases remain | 0.9%; thresholds USD 250,000 joint, USD 125,000 married separate, USD 200,000 other filing statuses | [Form 8959 instructions](https://www.irs.gov/instructions/i8959) |
| Additional Medicare withholding by each employer, irrespective of filing status; employee only | 0.9% above USD 200,000 paid by that employer | [Pub. 15, section 9](https://www.irs.gov/publications/p15) |

For ordinary positive Schedule C profit P, use Schedule SE: E = P × 0.9235; regular SE = 0.124 × min(E, remaining Social Security base) + 0.029 × E. The remaining base cannot be negative. Use the owner's wages/tips and prescribed other line 8 amounts, not the spouse's wages. Generally net SE earnings of at least USD 400 trigger SE tax; other activities, losses and coverage exceptions require the full `us-schedule-c-and-se-computation`. Farm, minister, church, railroad, statutory-employee, totalization and exempt coverage cases are outside this simplified formula. [Schedule SE and instructions](https://www.irs.gov/instructions/i1040sse).

For covered salary W at one S corporation, combined regular FICA is 0.124 × min(W, USD 184,500) + 0.029 × W before any employee multi-employer credit. Genuine non-wage distributions are outside employment tax; they are not thereby free of income tax. Do not confuse cash distributed with K-1 taxable profit. [IRS compensation guidance](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues); [S corporation income treatment](https://www.irs.gov/instructions/i2553).

An unrelated second employer generally withholds and pays its own full employer share even when another job has used the employee's Social Security base. Excess employee Social Security tax from multiple employers can qualify for a credit/refund under section 6413(c); that provision does not refund the S corporation's employer share. Successor-employer/common-paymaster arrangements need separate analysis. Thus other wages can make the election more costly. [Pub. 15, section 9, Part-Time Workers/Successor employer](https://www.irs.gov/publications/p15); [26 U.S.C. 6413(c)](https://uscode.house.gov/us/usc/t26/s6413/).

Calculate Additional Medicare separately in both structures: combine Medicare wages as required, reduce the SE threshold by those wages (not below zero), and apply the tax to positive SE earnings above the remainder. Do not use gross profit or subtract SE losses from wages. The employer's withholding threshold differs from final household liability. [Form 8959 instructions](https://www.irs.gov/instructions/i8959).

### 3. Count costs and income tax

Obtain recurring quotes for payroll, Form 1120-S/K-1 preparation, bookkeeping, FUTA and state unemployment, workers' compensation where applicable, annual reports, registration and entity taxes. Deduct only costs that legally qualify and compare incremental costs over the existing structure; no national average or automatic break-even profit is supplied. Send payroll filing/deposit requirements to `us-form-941-940-payroll` and `us-state-payroll-matrix`; formation to `us-state-formation-matrix`. [26 U.S.C. 162(a)](https://uscode.house.gov/us/usc/t26/s162/).

Deduct one-half of regular SE tax (excluding Additional Medicare) in the sole-proprietor column. In the corporation column, account for deductible salary, employer payroll tax and deductible costs. These income-tax differences must always be calculated, not only on request. [26 U.S.C. 164(f)](https://uscode.house.gov/us/usc/t26/s164/); [26 U.S.C. 162(a)](https://uscode.house.gov/us/usc/t26/s162/).

QBI is the net of qualifying domestic business items after attributable deductions; salary/reasonable compensation is not the owner's QBI. The usual deduction is up to 20% of QBI, with the taxable-income-minus-net-capital-gain cap and the other section 199A components/limits. For 2026 the minimum is USD 400 if aggregate QBI from active qualified businesses is at least USD 1,000; “active” requires material participation under section 469(h). It can override the usual cap; do not state the cap as absolute. Below the threshold there is no W-2/property limitation; above it, the limitation phases in, and a fully phased-in SSTB cannot qualify. For other qualifying businesses the wage/property limit is the greater of 50% of qualifying W-2 wages or 25% of those wages plus 2.5% of qualified-property UBIA. Owner salary can supply qualifying W-2 wages only subject to allocation and timely SSA reporting requirements. Property can support a sole proprietor's limit too. Run both complete computations in `us-qbi-deduction`, including aggregation, losses, REIT/PTP or cooperative items where relevant; refer uncommon cases. [26 U.S.C. 199A(a)-(f), (i)](https://uscode.house.gov/us/usc/t26/s199A/); [IRS QBI guidance](https://www.irs.gov/newsroom/qualified-business-income-deduction).

| Case 1 figure, subject to the stated facts | 2026 amount | Official source |
| --- | --- | --- |
| Ordinary single standard deduction; extra age/blindness/dependent rules not part of the case | USD 16,100 | [Rev. Proc. 2025-32, section 4.15](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| Single ordinary-income bracket containing both Case 1 taxable incomes | 22% above USD 50,400 through USD 105,700 | [Rev. Proc. 2025-32, section 4.01 table 3](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |
| QBI wage/property threshold, before QBI deduction: Case 1 single / Case 2 joint | USD 201,750 / USD 403,500 | [Rev. Proc. 2025-32, section 4.26](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf) |

Net annual benefit = regular SE and Additional Medicare avoided − net corporation/employee payroll taxes − incremental costs − increase in total income tax (or plus a decrease). Compare the actual returns, not a guessed marginal rate when brackets, credits or other limits change. Show the conditions, confidence, low-year sensitivity and what would change the result. Do not guarantee savings or recommend a salary.

### 4. Election, relief and revocation

For an existing calendar-year entity, the ordinary election deadlines were 17 March 2025 for 2025, 16 March 2026 for 2026, and are 15 March 2027 for 2027 (weekend adjustment). Form 2553 may also be filed during the preceding tax year. A new entity uses no more than 2 months and 15 days after the first tax year starts, not a universal 75-day rule: first-year item E is the earliest of first owners, first assets or beginning business. The instructions' 7 January start gives a 21 March deadline. Earlier-year eligibility or consent failures can push a timely filing to the following year under section 1362(b)(2); an ordinary late filing takes effect the following year unless relief applies. [26 U.S.C. 1362(b)](https://uscode.house.gov/us/usc/t26/s1362/); [26 U.S.C. 7503](https://uscode.house.gov/us/usc/t26/s7503/); [Form 2553 instructions, When/Item E](https://www.irs.gov/instructions/i2553).

Rev. Proc. 2013-30 simplified late-election relief requires intended status from the requested effective date, failure solely from untimely election, reasonable cause and diligent correction, and generally a request within 3 years and 75 days. Complete Form 2553 with the authorized officer and all required current/former shareholder signatures, consistent-reporting statements for every affected shareholder/year, the reasonable-cause/diligence statement and dated penalties-of-perjury declarations; mark it “FILED PURSUANT TO REV. PROC. 2013-30.” A late LLC corporate-classification election additionally requires eligibility, intent for the same date, classification failure solely from the missing/deemed Form 8832, and all required federal tax AND information returns timely filed consistently with no inconsistent returns, or the first year's return not yet due. Meeting the time limit alone does not establish relief. [Rev. Proc. 2013-30, sections 4.02–5.03](https://www.irs.gov/irb/2013-36_IRB#RP-2013-30).

The procedure permits a standalone election or attachment to a return only through its specified filing routes and headings; return extensions do not extend the relief window. Section 5.04 has a beyond-window exception for a corporation not concurrently seeking late classification relief, with failure solely from Form 2553 lateness, consistent corporation/shareholder reporting for all affected years, at least 6 months since the first return was filed, no IRS status notice within 6 months of the timely first Form 1120-S, and the required shareholder statements. Letter-ruling relief may be available when the simplified route fails. For this exception, ruling requests/fees, uncertain intent or correction of inconsistent returns: Check this point with one of our partner accountants. Do not invent retroactive intent, salary or a reasonable-cause declaration. [Rev. Proc. 2013-30, sections 3.02, 4.03, 5.04](https://www.irs.gov/irb/2013-36_IRB#RP-2013-30).

An election continues until termination/revocation. Revocation needs consent of holders of more than half the shares; by the 15th day of the third month it generally takes effect from that year's first day, otherwise next year, unless a permissible prospective date is specified. Without IRS consent, another S election cannot precede the fifth tax year beginning after the first year the termination took effect. Revocation does not itself turn an LLC back into a disregarded entity: the corporate classification generally continues. Check this point with one of our partner accountants before acting. [26 U.S.C. 1362(c), (d)(1), (g)](https://uscode.house.gov/us/usc/t26/s1362/); [26 CFR 301.7701-3(c)(1)(v)(C)](https://www.ecfr.gov/current/title-26/section-301.7701-3).

## Worked cases

**Case 1, a decision: a single consultant with USD 120,000 profit and a USD 70,000 salary.** A single filer, no other income, standard deduction, a non-SSTB business in a state with no entity-level tax on S corporations. 2026 profit before any owner pay is USD 120,000. Market data supports a salary of USD 70,000. Quotes for the added costs (payroll service, Form 1120-S, FUTA and state unemployment) total USD 3,000.

Sole proprietor: net earnings USD 120,000 x 92.35% = USD 110,820, all under the USD 184,500 base; self-employment tax 15.3% = USD 16,955.46; deductible half USD 8,477.73. QBI = USD 111,522.27. Taxable income before QBI: USD 120,000 less USD 8,477.73 less USD 16,100 = USD 95,422.27. QBI deduction: the smaller of 20% of QBI (USD 22,304.45) and 20% of taxable income (USD 19,084.45), so USD 19,084.45. Taxable income USD 76,337.82.

S corporation: FICA on salary USD 70,000 x 15.3% = USD 10,710 (employer half USD 5,355 deducted by the corporation). K-1 income USD 120,000 less 70,000 less 5,355 less 3,000 = USD 41,645, which is the QBI. Taxable income before QBI USD 70,000 plus 41,645 less 16,100 = USD 95,545; QBI deduction 20% of USD 41,645 = USD 8,329. Taxable income USD 87,216.

For planning, the following uses a continuous rate-schedule estimate of ordinary income tax; it is not a completed Form 1040 tax-table calculation. Use the applicable annual Form 1040 instructions and Tax Table for filing; that result can differ from this estimate. [IRS filing method](https://www.irs.gov/instructions/i1040gi).

The estimated decision: payroll tax saved USD 16,955.46 less USD 10,710 = USD 6,245.46. Less added costs USD 3,000. Taxable income is USD 10,878.18 higher with the S corporation, mostly because the salary left QBI; both figures sit in the 22% band (under USD 105,700), so income tax rises USD 2,393.20. Estimated net saving on that rate-schedule basis: **USD 852.26 a year**. The result is marginal and conditional on the stated salary evidence, eligibility, fully deductible costs and unchanged case facts. Growth or a different supported salary requires a fresh comparison. Without the QBI step the saving would have looked like USD 3,245.46, which is the common mistake.

```oa-check
name: S corporation decision, single, profit 120,000, salary 70,000 (2026)
inputs:
  profit: 120000
  salary: 70000
  added_costs: 3000
  standard_deduction: 16100
  marginal_rate: 0.22
steps:
  - se_tax: profit * 0.9235 * 0.153
  - half_se: se_tax * 0.5
  - ti_before_qbi_sp: profit - half_se - standard_deduction
  - qbi_sp: min((profit - half_se) * 0.2, ti_before_qbi_sp * 0.2)
  - taxable_sp: ti_before_qbi_sp - qbi_sp
  - fica: salary * 0.153
  - k1_income: profit - salary - salary * 0.0765 - added_costs
  - ti_before_qbi_s: salary + k1_income - standard_deduction
  - qbi_s: min(k1_income * 0.2, ti_before_qbi_s * 0.2)
  - taxable_s: ti_before_qbi_s - qbi_s
  - payroll_tax_saved: se_tax - fica
  - extra_income_tax: (taxable_s - taxable_sp) * marginal_rate
  - net_saving: payroll_tax_saved - added_costs - extra_income_tax
expected:
  se_tax: 16955.46
  qbi_sp: 19084.45
  taxable_sp: 76337.82
  fica: 10710.00
  k1_income: 41645.00
  qbi_s: 8329.00
  taxable_s: 87216.00
  payroll_tax_saved: 6245.46
  extra_income_tax: 2393.20
  net_saving: 852.26
```

**Case 2, a decision: a side business on top of a job above the wage base.** A married couple filing jointly. One spouse earns USD 190,000 of wages from an employer (Medicare wages in box 5; Social Security wages in box 3 are capped at USD 184,500 for this fully covered job) and has a side LLC with 2026 profit of USD 60,000; the other spouse has no income. A reasonable salary for the side work is USD 35,000; added costs are quoted at USD 2,500.

Sole proprietor: net earnings USD 60,000 x 92.35% = USD 55,410. Schedule SE line 9: USD 184,500 less USD 190,000 is below zero, so zero; no 12.4%. Self-employment tax is 2.9% only: USD 1,606.89. Additional Medicare Tax: the USD 250,000 joint threshold less USD 190,000 of wages leaves USD 60,000, above USD 55,410, so none.

S corporation on a USD 35,000 salary: employer 6.2% plus 1.45% = USD 2,677.50; employee Medicare 1.45% = USD 507.50; employee social security 6.2% = USD 2,170 is withheld but comes back as the excess social security credit on Form 1040, because the job already withheld on the full USD 184,500 (26 U.S.C. 6413(c)). Payroll tax borne USD 3,185. Wages total USD 225,000, under USD 250,000, so no Additional Medicare Tax either. With the added costs: USD 5,685.

The decision: the S corporation costs **USD 4,078.11 more each year** in payroll tax and costs. This is a payroll-tax-and-cost comparison, before income tax. Do not conclude that income tax cannot offset it merely because QBI is smaller: recompute the deductible half of SE tax, employer tax, deductible costs, QBI and the complete household return before an overall recommendation. Eligibility and the stated reasonable salary remain conditions.

```oa-check
name: S corporation decision, other wages above the wage base, joint (2026)
inputs:
  profit: 60000
  salary: 35000
  other_wages: 190000
  wage_base: 184500
  added_costs: 2500
steps:
  - line_4a: profit * 0.9235
  - line_9: max(wage_base - other_wages, 0)
  - se_tax: min(line_4a, line_9) * 0.124 + line_4a * 0.029
  - employer_tax: salary * 0.0765
  - employee_medicare: salary * 0.0145
  - employee_ss_withheld: salary * 0.062
  - employee_ss_credited: min(employee_ss_withheld, max(other_wages + salary - wage_base, 0) * 0.062)
  - scorp_payroll_tax: employer_tax + employee_medicare + employee_ss_withheld - employee_ss_credited
  - scorp_total: scorp_payroll_tax + added_costs
  - extra_cost_of_election: scorp_total - se_tax
expected:
  line_4a: 55410.00
  se_tax: 1606.89
  employer_tax: 2677.50
  employee_ss_credited: 2170.00
  scorp_payroll_tax: 3185.00
  scorp_total: 5685.00
  extra_cost_of_election: 4078.11
```

### Historical cases retained from the 2025 version

These preserve the original test inputs and years, not its old recommendations. Salary figures and costs below are hypothetical case inputs, not verified market compensation or official fees. The old USD 42 FUTA input is conditional on full credit and sufficient taxable wages; a credit-reduction state or other failed credit condition changes it. It is not added again where costs already include it. [Pub. 15, section 14](https://www.irs.gov/publications/p15). The historical Social Security base is USD 176,100 for 2025. [SSA](https://www.ssa.gov/oact/cola/cbb.html). Dollar outputs use full precision until rounding.

| Original case / year and unchanged facts | Recomputed limited result and decision boundary |
| --- | --- |
| Section 7 worked example, 2025: single freelance software developer, profit USD 120,000, salary USD 65,000, FUTA input USD 42, other incremental costs USD 3,500 | E = USD 110,820; regular SE USD 16,955.46; each FICA share USD 4,972.50, total USD 9,945; employer FICA, FUTA and costs leave USD 46,485.50 of corporation profit, not the old USD 55,000 “distribution.” Payroll/cost benefit USD 3,468.46 **before income/state tax**; a complete return and salary evidence are still required. |
| Test 1, 2025: single freelance developer, profit USD 150,000, no employees/other W-2 wages, Texas resident, salary input USD 80,000, FUTA USD 42 and other costs USD 3,500 | E = USD 138,525; SE USD 21,194.33; FICA USD 12,240; payroll/cost benefit USD 5,412.33 before income/state tax. “No state income tax” does not establish zero entity costs; no final election recommendation. |
| Test 2, 2025: single freelance writer, profit USD 35,000, no employees, no state income tax, salary input USD 25,000, FUTA USD 42 and costs USD 3,500 | E = USD 32,322.50; SE USD 4,945.34; FICA USD 3,825; payroll/cost result **negative USD 2,421.66**, before income/state tax. |
| Test 3, 2025: single California freelance consultant, profit USD 120,000, no employees, salary input USD 65,000, FUTA USD 42 and federal costs USD 3,500 | Federal payroll/cost benefit USD 3,468.46 before income/state tax. Withdraw the old USD 2,600 California total: a minimum is not automatically added to income-based tax, and gross pre-salary profit is not established California taxable income. Check this point with one of our partner accountants. |
| Test 4, 2025: joint couple, consultant profit USD 80,000, spouse's job wages USD 200,000, salary input USD 50,000, FUTA USD 42 and costs USD 3,500 | The spouse's wages do not consume the consultant's own base: SE USD 11,303.64; FICA USD 7,650; payroll/cost benefit USD 111.64. If the stated job wages are Medicare wages, joint Additional Medicare is USD 214.92 as sole proprietor (USD 200,000 + 73,880 − 250,000) × 0.009, versus zero on USD 250,000 joint salary; combined benefit USD 326.56 **before income/state tax**. |
| Test 5, 2025: single designer, LLC formed/intended election 15 January 2025, filing 15 July 2025, expected profit USD 100,000, stated consistent S returns | If 15 January is the first-year start, the ordinary deadline is **31 March 2025** (29 March is Saturday), and 15 July is **106 days** later. Formation does not establish eligibility, reasonable cause, diligent correction or payroll. The statement “filed TY2025 returns” in July needs reconciliation with the actual return/period. Check this point with one of our partner accountants. |
| Test 6, 2025: single non-SSTB freelance app developer, profit USD 280,000, no employees, UBIA USD 0, salary input USD 140,000; old illustrative marginal rate 32% | E = USD 258,580; regular SE USD 29,335.22 and Additional Medicare USD 527.22 if no other Medicare wages. FICA USD 21,420; employer part USD 10,710. If all residual profit qualifies and before **unknown further costs/deductions**, corporation QBI is USD 129,290, so 20% is USD 25,858, not USD 28,000. Qualifying wage limit would be USD 70,000. Sole-proprietor wage/property limit is zero only if actual taxable income is fully above the 2025 range (USD 197,300 + 50,000 = USD 247,300); USD 280,000 profit is not taxable income. Do not multiply the provisional deduction by the old 32% assumption or recommend until both actual returns are computed. |

California case correction: [FTB filing requirements](https://www.ftb.ca.gov/file/business/types/corporations/s-corporations.html) and [2025 Form 100S instructions, line 21](https://www.ftb.ca.gov/forms/2025/2025-100s-booklet.html). Historical QBI threshold: [Rev. Proc. 2024-40, section 2.27](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf); the 2026 wider phase-in/minimum must not be backdated to 2025. [Section 199A effective-date notes](https://uscode.house.gov/us/usc/t26/s199A/).

```oa-check
name: Historical 2025 cases, conditional payroll comparisons only
inputs:
  factor: 0.9235
  rate: 0.153
  futa_input: 42
  other_costs: 3500
  base_2025: 176100
steps:
  - se_worked: 120000 * factor * rate
  - employer_worked: 65000 * 0.0765
  - residual_worked: 120000 - 65000 - employer_worked - futa_input - other_costs
  - benefit_worked_and_test3: se_worked - 65000 * rate - futa_input - other_costs
  - se_test1: 150000 * factor * rate
  - benefit_test1: se_test1 - 80000 * rate - futa_input - other_costs
  - se_test2: 35000 * factor * rate
  - benefit_test2: se_test2 - 25000 * rate - futa_input - other_costs
  - se_test4: 80000 * factor * rate
  - benefit_test4_regular: se_test4 - 50000 * rate - futa_input - other_costs
  - additional_test4_sp: max(200000 + 80000 * factor - 250000, 0) * 0.009
  - additional_test4_s: max(200000 + 50000 - 250000, 0) * 0.009
  - benefit_test4_with_additional: benefit_test4_regular + additional_test4_sp - additional_test4_s
  - days_test5: 30 + 31 + 30 + 15
  - earnings_test6: 280000 * factor
  - se_test6: min(earnings_test6, base_2025) * 0.124 + earnings_test6 * 0.029
  - additional_test6: max(earnings_test6 - 200000, 0) * 0.009
  - employer_test6: 140000 * 0.0765
  - qbi_test6_before_other_costs: 280000 - 140000 - employer_test6
  - deduction_test6_conditional: qbi_test6_before_other_costs * 0.2
  - wage_limit_test6_conditional: max(140000 * 0.5, 140000 * 0.25)
expected:
  se_worked: 16955.46
  employer_worked: 4972.50
  residual_worked: 46485.50
  benefit_worked_and_test3: 3468.46
  se_test1: 21194.33
  benefit_test1: 5412.33
  se_test2: 4945.34
  benefit_test2: -2421.66
  se_test4: 11303.64
  benefit_test4_regular: 111.64
  additional_test4_sp: 214.92
  additional_test4_s: 0
  benefit_test4_with_additional: 326.56
  days_test5: 106
  se_test6: 29335.22
  additional_test6: 527.22
  deduction_test6_conditional: 25858
  wage_limit_test6_conditional: 70000
```

Historical edge inputs also remain separate: the freelancer's USD 150,000 in TY2024 and expected USD 40,000 in TY2025; a new LLC on 1 July 2025 (ordinary 15 September deadline, not “within 75 days”); California USD 300,000 versus USD 150,000 pre-salary income; and an existing election with income falling from USD 200,000 to USD 50,000. The first pair gives regular SE tax of USD 21,194.33 for TY2024 and USD 5,651.82 for TY2025 under ordinary coverage with no other covered wages; without that condition it must be recomputed. These cases lack supported salaries, complete costs/returns or conversion facts, so no net saving can be derived. The old rough USD 3,000–5,000 costs and USD 10,000–15,000 savings are withdrawn estimates. Check this point with one of our partner accountants. The separate spouse/QJV, staff/capital, high-UBIA, retirement, sale, losses, multiple-business and nonresident-spouse topics are routed in the boundary table below.

## When to refuse or refer

For each situation in this table: **Check this point with one of our partner accountants.** Do not fill an unknown fact with a favourable assumption.

| Code / original topic | Boundary or next step |
| --- | --- |
| R-SC-INELIG; R-SC-MULTI | Ownership/eligibility failing or unclear, trusts/ESBTs, nonresident-alien spouse/community interests, spouses' qualified joint venture, multi-member LLC or partnership conversion: establish the actual owners and structure; `us-form-1065-partnership`. |
| R-SC-ZEROSAL | No/token salary while performing services, missing comparable-pay evidence, or receipts dependent on staff/equipment: resolve compensation before recommending a distribution split. |
| R-SC-CCORP; R-SC-SALE | Existing C corporation, built-in-gain/earnings-and-profits issues, planned business sale, asset transfers/debt on incorporation, mid-year change or multiple businesses: obtain a conversion/sale analysis and correct short-period filings. |
| R-SC-LATE; R-SC-REVOKE | Late election, uncertain intent, classification-election history, inconsistent reporting, termination or proposed revocation: apply the legal conditions above before any filing. |
| R-SC-STATE | California, New York State, New York City, New Hampshire, New Jersey, Texas, Tennessee and every other relevant state/locality: separate state election/recognition, entity tax, existing LLC charges, payroll and workers' compensation analysis; no state outcome is assumed. Routes: `ca-llc-fee-and-tax`, `ny-corporate-franchise-article-9a`, `nyc-ubt`, `nh-bpt-bet`, `nj-cbt-and-bait`, `tx-franchise-tax`, `us-state-payroll-matrix`; Tennessee needs a partner. |
| R-SC-SSA | Social Security benefit projections and reduced covered earnings: obtain an individual benefits comparison; do not compute benefits here. |
| Losses; retirement; health insurance | Loss limitations and stock/debt basis, at-risk/passive/excess-business-loss rules in either structure; solo 401(k)/SEP contribution room (`us-self-employed-retirement`); more-than-2% shareholder health insurance (`us-self-employed-health-insurance`): obtain the separate calculation. |
| QBI; variable profit | SSTB classification, phase-in, qualified property, multiple-business aggregation or unknown income tax; low/volatile profits and recurring costs: recompute both structures; no fixed profit or salary-percentage cut-off. |

## Filing and payment

The output is a decision brief, not a filed election, payroll run or return. Form 2553 must be signed by an authorized officer and consented to by all required shareholders: for a pre-effective-date filing, owners on filing day; on/after that date, also required former owners in the intervening period. Community-interest spouses both consent. Use the current IRS address/fax for the principal business location, retain the original if faxed and proof of filing, and check the acceptance notice/effective date. The usual determination is within 60 days; follow up after 2 months, or 5 months when box Q1 is checked (the tax-year ruling adds time). [Form 2553 instructions, Signature/Columns J–K/Where/Acceptance](https://www.irs.gov/instructions/i2553); [current filing destinations](https://www.irs.gov/filing/where-to-file-your-taxes-for-form-2553).

After the decision, route payroll and employment-tax filing/deposits to `us-form-941-940-payroll`; the S return to `us-form-1120-s-s-corporation-return` and `us-corporate-extension-form-7004-and-the`; owner estimates/withholding to `us-quarterly-estimated-tax`; QBI to `us-qbi-deduction`; C corporation comparison to `us-form-1120-c-corp`. Do not wait for acceptance to consider effective-date payroll obligations or state requirements. Resolve the salary, quoted costs, both tax columns, state analysis and correct election date before recommending action.

Circular 230 section 10.37: this general decision framework does not establish the facts or determine a taxpayer's filing position; a qualified professional must review the actual facts, applicable law and assumptions before action.

## Sources

| Official source and exact material read/reused | Read date |
| --- | --- |
| [Form 2553 instructions](https://www.irs.gov/instructions/i2553): Purpose, all eligibility tests, timing examples, late-election branches, item E, signatures/consents, destinations and acceptance follow-up. | 2026-11-26 |
| [26 U.S.C. 1361](https://uscode.house.gov/us/usc/t26/s1361/): (b) eligibility and (c) counting/owner exceptions; [1362](https://uscode.house.gov/us/usc/t26/s1362/): election timing, continuing effect, revocation and (g) re-election; [7503](https://uscode.house.gov/us/usc/t26/s7503/): weekends/holidays. | 2026-11-26 |
| [26 CFR 301.7701-3](https://www.ecfr.gov/current/title-26/section-301.7701-3): (a), (c)(1)(iv) classification history and (v)(C) deemed S election/continuing association status. | 2026-11-26 |
| [IRS compensation guidance](https://www.irs.gov/businesses/small-businesses-self-employed/s-corporation-compensation-and-medical-insurance-issues): reasonable compensation, cited cases, receipt sources and factors. | 2026-11-26 |
| [Pub. 15 (2026)](https://www.irs.gov/publications/p15): section 9 rates, multi-employer/successor rules, withholding; section 14 FUTA credit conditions. | 2026-11-26 |
| [Schedule SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf), [instructions](https://www.irs.gov/instructions/i1040sse), [26 U.S.C. 1401](https://uscode.house.gov/us/usc/t26/s1401/) and [164(f)](https://uscode.house.gov/us/usc/t26/s164/): reuse proven USCSE rows 006–007, 011–014, 023–025, 061–075, 2026 coverage/SE calculation and deductible half; [Form 8959 instructions](https://www.irs.gov/instructions/i8959): joint coordination/positive SE. | 2026-11-22; applicability and joint-income correction confirmed 2026-11-26 |
| [26 U.S.C. 6413(c)](https://uscode.house.gov/us/usc/t26/s6413/): multi-employer employee credit; [162(a)](https://uscode.house.gov/us/usc/t26/s162/): qualifying business expenses/salary. | 2026-11-26 |
| [26 U.S.C. 199A](https://uscode.house.gov/us/usc/t26/s199A/): (a)–(f), (i), exclusions, thresholds/phase-in and minimum; [IRS QBI guidance](https://www.irs.gov/newsroom/qualified-business-income-deduction): attributable deductions and minimum. | 2026-11-26 |
| [Rev. Proc. 2025-32](https://www.irs.gov/pub/irs-drop/rp-25-32.pdf): sections 4.01, 4.15, 4.26, 2026 case figures; [Rev. Proc. 2024-40](https://www.irs.gov/pub/irs-drop/rp-24-40.pdf): section 2.27 historical 2025 QBI threshold. | 2026-11-26 |
| [Rev. Proc. 2013-30](https://www.irs.gov/irb/2013-36_IRB#RP-2013-30): sections 3.02, 4.02–4.03 and 5.01–5.04, all relief conditions and filing routes. | 2026-11-26 |
| [SSA contribution base](https://www.ssa.gov/oact/cola/cbb.html): historical 2025 base and annual indexing; [California FTB](https://www.ftb.ca.gov/file/business/types/corporations/s-corporations.html) and [2025 Form 100S booklet, line 21](https://www.ftb.ca.gov/forms/2025/2025-100s-booklet.html): historic case minimum-tax error, filing conditions/first-year exception; [Form 1040 instructions, line 16](https://www.irs.gov/instructions/i1040gi): filing tax-table method, not a 2026 tax-table amount. | 2026-11-26 |

Not yet confirmed: no usable state/local calculation, individualized salary, retirement/health/benefits projection, conversion/sale/loss result or ruling-fee amount is supplied. Those topics require the explicit partner referral above. Historical tests preserve their original years and inputs; their conditional arithmetic is not an election recommendation.
