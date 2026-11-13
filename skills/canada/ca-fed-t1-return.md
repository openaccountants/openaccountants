---
name: ca-fed-t1-return
description: >
  Prepare the Canadian federal T1 income-tax computation and return working
  paper for a resident individual with self-employment income, including
  common employment and investment slips. Covers 2026 estimates with a
  separately dated 2025 filing and amendment bridge: marginal brackets,
  net versus taxable income, basic personal amount, CPP/CPP2 deduction and
  credit, voluntary EI, RRSP room, medical and donation credits, dividends,
  the top-up credit, instalments and filing/payment. Use for T1 return,
  federal personal tax, self-employed Canada, BPA, Schedule 8, RC381 and
  Schedule 13. Read with ca-fed-t2125 and ca-fed-cpp-ei; provincial tax is
  calculated in the applicable provincial skill.
version: 2.2
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-13
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Canadian federal T1 return for self-employed individuals v2.2

## Scope

Prepare a federal T1 working paper for a Canadian resident individual with a sole-proprietor business or professional activity, and common employment/investment slips. Currency is CAD; the income year is the calendar year. Use **2026** amounts for 2026 estimates and the explicitly dated **2025** bridge for a 2025 return or amendment. A 2025 calculation is not wrong simply because it is being prepared in 2026. This skill is **Built from the law** and **Not yet approved**. [2026 rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html); [2025 rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html).

Read [income-tax-workflow-base](../global/methods/income-tax-workflow-base.md), [ca-fed-t2125](ca-fed-t2125.md) for the business-income computation and [ca-fed-cpp-ei](ca-fed-cpp-ei.md) for contributions, coverage and elections. This method consumes their supported results; it does not classify bank deposits afresh or use an old companion figure merely because a cross-link exists. Use the applicable provincial/territorial method for its tax and credits, with the federal Quebec/other adjustments described below. [Actual T1 package](https://www.canada.ca/en/revenue-agency/services/forms-publications/tax-packages-years/general-income-tax-benefit-package.html).

**Answer layer:** calculate total income, deductions, net income, taxable income, federal tax and credits in that order. Add actual CPP/EI payable, provincial tax and other applicable return items, then subtract payments and refundable credits. A basic federal-tax subtotal is not the person's final balance. Prepare the proposed return for an authorized accountant to approve, not a filing or payment instruction to execute automatically.

## Ask the client first

1. Which income year, original return/estimate/amendment, residence periods and province/territory on December 31? Did any business have a PE in another province or country? A non-resident, part-year resident, deceased or bankrupt return needs the relevant specialist method and actual event dates, not the full-year resident assumptions here. [T1 identification/residence fields](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf).
2. Obtain legal identity, date of birth, marital/dependant facts and required tax identification through the authorized secure intake. Do not request a SIN, tax-account password or full slip package in a public working paper. Marital/dependant income can affect credits and benefits; record what is missing rather than inventing it.
3. Obtain a reconciled statement for each business/profession, its tax adjustments and the applicable T2125 outputs, plus all T4/T4A, T5, T3 and relevant rental, partnership and other income records/slips. Obtain actual withholding, amended slips and foreign-income facts. T2125 line **9946** feeds the appropriate T1 net-income line; it is not itself a T2125 line 13500. [T2125, net income](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf).
4. Obtain RRSP deduction notices/NOAs, actual contribution receipts and dates, unused contributions, deduction choice, loss/carryforward balances and any other deduction support. The annual RRSP new-room ceiling is not the individual's total available deduction room. [RRSP limit calculation](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html).
5. Obtain CPP/CPP2/QPP/QPP2 and EI earnings/contributions from all slips, pension/disability dates, contributory-month facts and elections/revocations. Obtain the actual self-employed EI agreement, its date, withdrawal history and any benefits already received. Unknown agreement status does not prove no EI. [CRA line 22200](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html); [EI agreement](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/eligibility.html).
6. Obtain medical receipts/reimbursements and the proposed claim period, donation receipts/carryforwards and the actual claimant, employment-credit facts, and notices concerning other credits or benefits. Identify any AMT, split-income, foreign-tax, trust-allocation or special deduction question before calling the calculation complete.
7. Obtain the two prior years' assessments/net tax owing, current estimate, instalment reminders, actual instalments paid and withholding/refundable credits. Separate an instalment **trigger** from its payment **amount**. For an amendment, obtain the filed return, NOA and any pending change request first. [Instalment test](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html); [amendments](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html).

Missing province, RRSP room, EI agreement or net-income facts remain open items. A conditional calculation with and without an unconfirmed deduction is useful; asserting zero legal room, an invented election or maximum BPA clawback is not.

## The method, step by step

### 1. Select the year and actual filing package

As read on November 13, 2026, CRA's annual return catalogue and the actual T1/worksheet/Schedule 8/Schedule 13 packages below are labelled **2025**. They establish the current observed line functions, not a claim that the final 2026 layout has been inspected. Use published 2026 parameters and enacted law for a 2026 estimate; confirm the final 2026 package/certified software before filing it. Keep 2025 figures when amending or late-filing 2025. [T1 catalogue](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5006-r.html); [Schedule 13 catalogue](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5000-s13.html).

Federal tax is in **T1 Step 5, Parts A, B and C** on the actual 2025 return. Do not tell a filer to attach an obsolete separate “Schedule 1 (Federal Tax)”. Supporting Schedule 8/RC381, Schedule 13, Schedule 9, Federal Worksheet and other applicable schedules still have their own jobs. Select the province-specific package; the Ontario PDF used to inspect the federal flow is not the correct package for every Canadian resident. [Actual 2025 T1, Steps 3-6](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf).

### 2. Reconcile business income, other income and deductions

Use a separate supported T2125 for each applicable business/profession. Map final net income from **T2125 line 9946** to T1 **13500 business**, **13700 professional** or **13900 commission**, as applicable. Other types such as farming/fishing and limited/non-active partnership income need their own return inputs and methods. The net business income, not gross deposits or sales before expenses, enters the T1 income flow. [T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf).

Reconcile employment, interest, taxable dividends, relevant T3/partnership and other income to the slips and tax workpapers. Ordinary supported T3 amounts are return inputs; an unresolved trust allocation is a specialist question, not a reason to omit every T3 slip. Preserve the business-use-of-home rule: those expenses cannot create or increase a business loss; the T2125 method owns eligibility and any permissible carryforward. [Business-use-of-home expenses](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-5.html).

Build the sequence explicitly:

- **15000:** total income from the supported component schedules/slips.
- **23600:** net income after applicable deductions, including the properly computed **22200** self-employed contribution deduction, RRSP and other supported deductions, with the return's intervening adjustments.
- **26000:** taxable income after applicable Division C deductions, such as supported loss carryovers. Do not treat every loss balance as usable against every kind of income.

A deduction changes income; a tax credit changes tax. BPA uses **net income at 23600**, not taxable income at 26000. Do not run the brackets until both amounts are established. [T1 Steps 3-5](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf); [BPA worksheet](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf).

For RRSP, verify the person's actual room/unused contributions, prior-year earned income, PA/PSPA/PAR adjustments and receipts. The annual new-room dollar ceiling is **33,810 for 2026**, versus **32,490 for 2025**; it is not a universal personal deduction maximum. Carryforward or eligible transfers can change the actual amount. Confirm the applicable contribution period and deduction choice rather than assuming every receipt is deductible in this year. [Annual RRSP limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html); [room calculation](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html).

### 3. Calculate CPP/QPP and EI before finalizing net income

Use the contribution companion and actual applicable CPP or Quebec Schedule 8/RC381. Age, pension/disability status, elections, months, Quebec/mixed employment and foreign coverage can change the result. A self-employment loss does not simply refund CPP correctly paid through employment. Do not subtract one undifferentiated T4 CPP amount from twice an employee maximum. Employment base/enhancement and self-employed contributions have different credit/deduction destinations. [CRA line 22200](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html); [actual CPP Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf).

For an ordinary **full-year CPP-only self-employed person**, with no employment earnings, election, disability-month or other coverage adjustment, let E be supported pensionable net earnings, P = max(0, min(E, YMPE) − 3,500), and U = max(0, min(E, YAMPE) − YMPE). Compute base CPP **P × 9.9%**, first additional **P × 2%**, and CPP2 **U × 8%**. Below or at 3,500, that ordinary first-band amount is zero. These are combined employer/employee contributions; CPP2 is CPP2, not QPP2. [Schedule 8, Part 4](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf); [2026 CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html); [CPP2](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html).

For that bounded case, half of **base** CPP is the **31000 credit base**; the other half of base plus **all first and second additional contributions** is the **22200 income deduction**. The full self-employed contribution payable goes to **42100**. Do not deduct half of the combined total and credit the other half. Employment base credit **30800** and employment enhanced deduction **22215** are separate. Mixed CPP/QPP selection belongs to the companion and the actual forms. [Schedule 8, Parts 3-5](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf); [line 31000](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31000-cpp-qpp-contributions-on-self-employment-other-earnings.html).

Self-employed EI is voluntary through an actual agreement, covering qualifying **special benefits**, not ordinary unemployment coverage. An agreement active for at least **12 months** is a benefit-eligibility condition, not a universal twelve-month benefit waiting period. Verify the specific benefit's conditions and Quebec's QPIP interaction. Premiums ordinarily cover the entire joining calendar year; withdrawal within **60 days** avoids premiums, later withdrawal generally requires them through December 31. Once benefits have been received, participation continues while self-employed. Use Schedule 13, including actual employment-insurable earnings interaction, for **31217 credit base** and **42120 payable**. Do not charge EI by default or assume a missing agreement means no premium. [Eligibility](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/eligibility.html); [premiums](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html); [withdrawal](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/withdraw.html); [Schedule 13](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5000-s13.html).

The special-benefit categories include maternity, parental, sickness, family caregiver for children, family caregiver for adults and compassionate care. For Quebec residents, maternity, paternity, parental and adoption benefits are provided through QPIP; do not promise EI maternity/parental benefits from a self-employed EI agreement there. Verify the actual benefit and plan before advising a claim. [Service Canada benefit types and Quebec routing](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers.html).

### 4. Apply marginal brackets and the correct BPA

Use the year-specific tables below. Tax each slice within its band, then add the slices; do not apply the highest reached rate to all income. Keep cents at the return's prescribed intermediate steps. The exact 2025 return constants are **8,319.38 / 20,081.25 / 36,495.57 / 58,399.85**, not the old whole-dollar quick-table approximations. Derived 2026 cumulative totals are **8,193.22 / 20,190.23 / 36,932.93 / 59,275.11**. Do not independently round every complete band and accidentally change an official cumulative constant. [2025 return Step 5A](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf); [2026 marginal table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html).

For a full-year resident under the ordinary BPA rule, use actual net income NI from 23600. The enhanced BPA is reduced only within the specified range, not below the minimum or above the maximum:

**BPA = maximum − enhanced amount × min(1, max(0, (NI − lower boundary) / (upper boundary − lower boundary))).**

2026: **16,452 − 1,623 × clamp((NI − 181,440) / 77,042, 0, 1)**; minimum **14,829**. 2025: **16,129 − 1,591 × clamp((NI − 177,882) / 75,532, 0, 1)**; minimum **14,538**. Apply the year's general credit percentage to the supported BPA amount. Partial residency and other special limitations require the appropriate rule; unknown NI is not a maximum-clawback election. [ITA 118(1), (1.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html); [indexed amounts](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html); [2025 BPA worksheet](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf).

### 5. Calculate each credit in its own form

The ordinary federal percentage for the relevant credit amounts here is **14% for 2026** and **14.5% for 2025**. This is not a command to multiply every credit by that percentage: donation, dividend and top-up computations are separate, and an already calculated credit must not be multiplied again. [ITA 118](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html); [actual T1 Step 5B](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf).

**Canada employment amount, 31260.** No amount arises from self-employment income itself. For qualifying office/employment income use the lesser of that income and **1,501 in 2026 / 1,471 in 2025**, then the applicable credit percentage. A person with both a business and qualifying employment is not automatically disqualified from the employment component. The current CRA webpage's simplified “not self-employed” condition is broader than ITA 118(10) and the actual T1 line, which tests employment income. Follow the enacted/form calculation; refer an unusual employment-income classification. [ITA 118(10)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html); [indexed caps](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html); [CRA page, stated simplification](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31260-canada-employment-amount.html).

**Medical expenses, 33099/33199/33200.** Establish eligible paid expenses, the claimant/family relationship, the permitted 12-month period ending in the relevant year, no duplicate claim and reimbursement treatment. For the ordinary self/spouse/dependent-child-under-18 pool, subtract the lesser of **3% of the claimant's net income** and **2,890 for 2026 / 2,834 for 2025**, with a zero floor, then apply the credit percentage. Other eligible dependants have their own net-income threshold calculation; do not combine every adult dependant under the claimant's one threshold. Check the actual worksheet and related refundable supplement separately. [Medical claim conditions](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/lines-33099-33199-eligible-medical-expenses-you-claim-on-your-tax-return.html); [ITA 118.2](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.2.html); [indexed ceiling](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html).

**Donations, 34900.** Establish a qualified donee, eligible receipted gift, chosen claimant, unused-year records and applicable income limit. Ordinary gifts are generally subject to a **75% net-income** limit; property/cultural/ecological/death rules and carryforwards need the actual schedule. For ordinary supported current gifts, first **200** uses **14% in 2026 / 14.5% in 2025**. Excess generally uses **29%**; **33%** applies only to the eligible part supported by taxable income above the year's top-bracket threshold, with the schedule's special-gift restrictions. A high **net** income does not itself prove the 33% calculation. Do not claim the same gift twice or omit a valid dated carryforward. [ITA 118.1(1), (3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.1.html); [2025 Schedule 9](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s9/5000-s9-25e.pdf).

**Canadian dividends, 12000/12010 and 40425.** Where an actual cash amount must be grossed up, eligible dividends use **138%** and other-than-eligible dividends **115%**. Do not gross up an already taxable slip amount again. 12000 includes both taxable types; 12010 identifies other-than-eligible taxable dividends. The federal credit is **15.0198% of taxable eligible dividends** and **9.0301% of taxable other-than-eligible dividends**. Use slip credit amounts/the actual worksheet, and do not apply the Canadian credit to foreign dividends. [Dividend inclusion](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12000-taxable-amount-dividends-eligible-other-than-eligible-taxable-canadian-corporations.html); [ITA 82](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-82.html), [121](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-121.html); [Federal Worksheet 40425](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf).

**Top-up credit, observed 2025 line 34990.** ITA 118(11) applies to **2025-2030**. Let A be the actual eligible **credit-dollar** sum under the enumerated provisions in 118(11), including only the capped first-200 donation-credit component specified there; do not add all donation credits or dividend credits. Let B be the appropriate percentage, C the year's first bracket threshold and D **3.45% for 2025 / 7.14% for 2026-2030**. The computation is **max(0, A − B × C) × D**. This is a separate tax credit, not an income deduction and not 0.5%/1% of credit dollars. The actual 2025 worksheet uses 33800 plus Schedule 9 line 22, less **8,319.38**, with the zero floor and 3.45%. For 2026 the threshold product is **58,523 × 14% = 8,193.22**; confirm the final 2026 field presentation when published. [Enacted ITA 118(11)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html); [2025 top-up worksheet](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf); [CRA 34990](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-34990-top-up-tax-credit.html).

### 6. Complete the federal result and the return balance separately

Keep a basic federal-tax computation separate from net federal tax and the total payable. The actual 2025 T1 distinguishes **42900 basic federal tax**, additional adjustments leading to **42000 net federal tax**, then **42100 CPP payable**, **42120 voluntary EI payable**, **42200 social-benefit repayment** and **42800 provincial/territorial tax**, leading to **43500 total payable**. Screen actual TOSI, AMT/carryover, foreign-tax credit/surtax, investment-credit and special-tax facts and route the affected computation rather than silently setting every extra item to zero. [T1 Parts C and Step 6](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf).

Provincial tax is a separate computation, but the federal return can still require the **44000 Quebec abatement** and **T2203** where business PE/residence spans relevant jurisdictions. Do not omit a federal adjustment because the provincial calculation is referred elsewhere. Use the Quebec package/applicable T2203, not an Ontario template for every resident. [Quebec abatement and T2203 conditions](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44000-refundable-quebec-abatement.html).

Reconcile **43700 withholding**, **47600 instalments actually paid**, overpayment/refundable-credit claims and **47900 provincial credits** into total credits **48200**. The difference from total payable is **48400 refund** or **48500 balance owing** on the observed form. Do not subtract only instalments while ignoring withholding or benefits, and do not treat zero basic federal tax as proof of zero CWB or other refund. Every amount needs its actual eligibility, slip, notice or receipt. [Actual T1 Step 6](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf).

### 7. Determine instalments from net tax owing, not CPP alone

For ordinary **2026** instalments, net tax owing must exceed **3,000**, or **1,800 for a Quebec resident**, in **2026 and either 2025 or 2024**. Exactly the threshold does not exceed it. Obtain the actual reminder and residence/current/prior assessments; an untested federal-tax subtotal is not the net-tax-owing figure. [CRA current 2026 test](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html); [ITA 156-156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html).

Use the actual **2026 calculation chart** to reconcile net federal/provincial or territorial tax, repayments, withholding, abatements and the listed refundable credits. **CPP and voluntary EI are excluded from net tax owing for this trigger**, then their amounts at **42100/42120 are added to the instalment payment total**. A person owing CPP with little income tax does not automatically cross the income-tax instalment threshold. [2026 chart, both pages](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf).

Choose the supported **no-calculation reminder, prior-year or current-year** option; retain the comparison and assumptions. A current-year estimate that is too low is not automatically interest-safe. Ordinary dates are March 15, June 15, September 15 and December 15; in **2026 March 15 is Sunday, so March 16 is the next-business-day payment date**. The other three 2026 dates are business days. Where the current chart's August-only reminder route applies, it uses **75% September / 25% December**, not four fictional payments already made. Farming/fishing has a different statutory/reminder route; refer it rather than applying the ordinary current-plus-one-prior test mechanically. [Calculation options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html); [due dates](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html); [actual chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf).

## Rates, bands and thresholds

### Federal marginal rates, by income year

| 2026 taxable-income slice | Rate | Source |
|---|---|---|
| 0-58,523.00 | 14% | [CRA 2026](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html) |
| 58,523.01-117,045.00 | 20.5% | [CRA 2026](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html) |
| 117,045.01-181,440.00 | 26% | [CRA 2026](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html) |
| 181,440.01-258,482.00 | 29% | [CRA 2026](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html) |
| Over 258,482.00 | 33% | [CRA 2026](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html) |

| 2025 taxable-income slice, retained for 2025 filings | Rate | Source |
|---|---|---|
| 0-57,375.00 | 14.5% annual blended rate | [CRA 2025](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| 57,375.01-114,750.00 | 20.5% | [CRA 2025](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| 114,750.01-177,882.00 | 26% | [CRA 2025](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| 177,882.01-253,414.00 | 29% | [CRA 2025](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |
| Over 253,414.00 | 33% | [CRA 2025](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html) |

The 2025 annual 14.5% rate reflects the July 1 reduction from 15% to 14%; it does not split an annual T1's income by payment date. ITA section 117 gives the structure and section 117.1 indexes amounts. Use the published year-specific thresholds, not an unindexed base amount in the statute. [ITA 117](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-117.html); [CRA 2025 explanation](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html).

### Ordinary full-year CPP and voluntary EI parameters

| Item and conditions | 2026 | Dated 2025 bridge | Source |
|---|---|---|---|
| CPP YMPE / YAMPE | 74,600 / 85,000 | 71,300 / 81,200 | [CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html), [CPP2](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html) |
| CPP basic exemption / first-band combined rate | 3,500 / 11.9% | 3,500 / 11.9% | [CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html) |
| First-band combined maximum / CPP2 combined maximum at 8% | 8,460.90 / 832.00 | 8,068.20 / 792.00 | [CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html), [CPP2](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html) |
| Full-year self-employed CPP total maximum | 9,292.90 | 8,860.20 | Derived from the preceding two sourced maxima; assumes CPP-only full-year liability: [CRA CPP2](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html) |
| EI maximum insurable earnings | 68,900 | 65,700 | [CRA EI annual table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html) |
| Non-Quebec voluntary EI rate / maximum, before employment interaction | 1.63% / 1,123.07 | 1.64% / 1,077.48 | [Service Canada 2026](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html), [CRA annual table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html) |
| Quebec voluntary EI rate / maximum, before employment interaction | 1.30% / 895.70 | 1.31% / 860.67 | [Service Canada 2026](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html), [CRA annual table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html) |

Quebec QPP/QPIP is not computed with CPP's rates. Use [ca-fed-cpp-ei](ca-fed-cpp-ei.md) for the correct QPP-only/mixed-form selection and [qc-individual-return](quebec/qc-individual-return.md) for the Quebec return. The final 2026 annual contribution forms must be checked when available; these tables do not relabel the 2025 PDFs as 2026.

## Deadlines and filing

For **2026 income**, the ordinary qualifying self-employed filing date is **June 15, 2027** and the balance payment date is **April 30, 2027**. A qualifying spouse/common-law partner can also have the June date; the tax-shelter-expenditure exception can restore the April filing date. These dates are Tuesday and Friday respectively. For a **2025** return the corresponding dates were **June 15, 2026** and **April 30, 2026**. Confirm special deceased/bankruptcy/residency facts before using an ordinary deadline. [ITA 150(1)(d)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html); [current CRA 2027 deadlines for 2026 income](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html).

Use the actual certified **NETFILE** software route for an eligible individual's own return or authorized **EFILE** preparer route, with the correct package and authority; CRA account/representative access serves its own notices and adjustment functions. A completed workpaper is not proof that the CRA accepted a return. Retain the authorized sign-off, submitted version, confirmation number and actual payment receipt. The user must approve any proposed posting/import where the ledger is read-only. [CRA filing options](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file.html).

For an assessed return, wait for the **NOA** and any pending change request response before further corrections. Use **Change my return**, eligible **ReFILE** software or **T1-ADJ** as applicable; do not simply file another original return. Check eligible years, exclusions and representative authority. A normal adjustment request is not automatically a valid new or revised election. [CRA changing a return](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html).

Late-return penalty under ITA **162(1)** is **5%** of the relevant tax unpaid at the filing deadline plus **1% per complete month**, maximum **12 months**. The **162(2)** replacement penalty is **10% plus 2% per complete month**, maximum **20 months**, only with a demand to file and the specified penalty history in one of the **three prior taxation years**. Do not stack the two or charge them without unpaid tax. The relevant unpaid tax for this rule is not necessarily total tax before payments. [ITA 162(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html).

Balance interest is **compounded daily** from the day after the payment due date, not from the later June filing deadline. For an unpaid ordinary 2026 balance that means from **May 1, 2027**, subject to actual extensions/payment facts and applicable law. Obtain actual quarterly prescribed rates and dates received; do not freeze a rate or invent an interest assessment. Instalment interest/penalty has a separate test and calculation; do not reuse the late-return percentage on every missed instalment. File on time even when unable to pay. [CRA interest and penalties](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html).

Do not implement a future Budget proposal as a current deadline, instalment threshold or RRSP rule. This method uses current enacted law and the cited CRA year-specific guidance as read on the date below.

## Worked cases

### Case 1. 2026 standard self-employed estimate

Fictional full-year Ontario resident, ordinary CPP liability throughout, no employment earnings, no EI agreement/benefits, no other income/credits, and a supported RRSP deduction of 10,000. Net business income is 85,000. First-band earnings 71,100 yield base CPP 7,038.90 and first additional 1,422; CPP2 on 10,400 is 832. Total CPP is **9,292.90**, deduction **5,773.45**, credit base **3,519.45**. Net/taxable income is **69,226.55**. Federal tax before credits is **10,387.45**, ordinary credits **2,796.00**, basic federal tax **7,591.45**. Basic federal tax plus CPP subtotal **16,884.35** excludes provincial tax, other adjustments and payments; it is not a final balance. No CEA arises from these pure-business facts and no top-up arises on these credit amounts. [2026 rates](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html); [CPP](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html); [indexed BPA](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html).

```oa-check
name: 2026 T1 standard full-year CPP-only self-employed estimate
inputs:
  earnings: 85000
  rrsp: 10000
steps:
  - p: max(0, min(earnings, 74600) - 3500)
  - u: max(0, min(earnings, 85000) - 74600)
  - base_cpp: round(p * 0.099, 2)
  - additional_cpp: round(p * 0.02, 2)
  - cpp2: round(u * 0.08, 2)
  - cpp_payable: base_cpp + additional_cpp + cpp2
  - cpp_credit_base: round(base_cpp / 2, 2)
  - cpp_deduction: cpp_credit_base + additional_cpp + cpp2
  - net_income: earnings - rrsp - cpp_deduction
  - gross_tax: round(8193.22 + (net_income - 58523) * 0.205, 2)
  - ordinary_credits: round((16452 + cpp_credit_base) * 0.14, 2)
  - basic_federal: max(0, gross_tax - ordinary_credits)
  - federal_cpp_subtotal: basic_federal + cpp_payable
expected:
  base_cpp: 7038.90
  additional_cpp: 1422
  cpp2: 832
  cpp_payable: 9292.90
  cpp_credit_base: 3519.45
  cpp_deduction: 5773.45
  net_income: 69226.55
  gross_tax: 10387.45
  ordinary_credits: 2796
  basic_federal: 7591.45
  federal_cpp_subtotal: 16884.35
```

### Case 2. 2026 low-income and high-income estimates

Use the same full-year CPP-only/no-other-items assumptions. At business income **14,000**, with no RRSP deduction, CPP is **1,249.50**, deduction **729.75**, net income **13,270.25** and gross tax **1,857.84**; ordinary BPA/base-CPP credits exceed that tax, so basic federal tax is **zero**. This does not decide refundable benefits or the final return balance. [CPP Schedule 8 method](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf); [2026 table](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html).

At business income **300,000** and an actually supported chosen RRSP deduction **33,810**, full CPP is 9,292.90 and the deduction 5,773.45. Net/taxable income is **260,416.55**, above the BPA upper boundary; BPA is the 14,829 minimum. Gross tax is **59,913.51**, ordinary credits **2,568.78**, basic federal tax **57,344.73** and the federal/CPP subtotal **66,637.63**. The annual RRSP limit is not proof that this person has that deduction room; it is an express example assumption. [2026 amounts](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html); [RRSP limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html).

```oa-check
name: 2026 T1 low and high income with supported assumptions
inputs:
  low_income: 14000
  high_income: 300000
  high_rrsp: 33810
steps:
  - low_p: max(0, low_income - 3500)
  - low_cpp: round(low_p * 0.119, 2)
  - low_deduction: round(low_p * (0.0495 + 0.02), 2)
  - low_credit_base: round(low_p * 0.0495, 2)
  - low_net: low_income - low_deduction
  - low_tax: round(low_net * 0.14, 2)
  - low_credits: round((16452 + low_credit_base) * 0.14, 2)
  - low_basic_federal: max(0, low_tax - low_credits)
  - high_net: high_income - high_rrsp - 5773.45
  - high_tax: round(59275.11 + (high_net - 258482) * 0.33, 2)
  - high_credits: round((14829 + 3519.45) * 0.14, 2)
  - high_basic_federal: high_tax - high_credits
  - high_federal_cpp_subtotal: high_basic_federal + 9292.90
expected:
  low_cpp: 1249.50
  low_deduction: 729.75
  low_credit_base: 519.75
  low_net: 13270.25
  low_tax: 1857.84
  low_credits: 2376.05
  low_basic_federal: 0
  high_net: 260416.55
  high_tax: 59913.51
  high_credits: 2568.78
  high_basic_federal: 57344.73
  high_federal_cpp_subtotal: 66637.63
```

### Case 3. Preserve all three valid 2025 example families

These are **2025**, not 2026, using the same ordinary full-year CPP-only/no-EI/no-other-items assumptions and actual supported RRSP deductions. The old 85,000/10,000 example remains **7,978.82** basic federal tax and **16,839.02** federal/CPP subtotal. The 14,000 example remains zero basic federal tax and **1,249.50** CPP. The 300,000/32,490 example remains **58,640.54** basic federal tax. The high RRSP deduction is a supported assumption, not a universal personal maximum. None establishes the final provincial/benefit/payment result. [2025 T1 and exact bracket constants](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf); [2025 Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf).

```oa-check
name: 2025 T1 retained standard low and high cases
inputs:
  standard_income: 85000
  standard_rrsp: 10000
  low_income: 14000
  high_income: 300000
  high_rrsp: 32490
steps:
  - full_cpp: round(67800 * 0.119, 2) + round(9900 * 0.08, 2)
  - full_credit_base: round(67800 * 0.0495, 2)
  - full_deduction: full_credit_base + round(67800 * 0.02, 2) + round(9900 * 0.08, 2)
  - standard_net: standard_income - standard_rrsp - full_deduction
  - standard_tax: round(8319.38 + (standard_net - 57375) * 0.205, 2)
  - standard_credits: round((16129 + full_credit_base) * 0.145, 2)
  - standard_basic_federal: standard_tax - standard_credits
  - standard_federal_cpp_subtotal: standard_basic_federal + full_cpp
  - low_cpp: round((low_income - 3500) * 0.119, 2)
  - low_credit_base: round((low_income - 3500) * 0.0495, 2)
  - low_deduction: low_credit_base + round((low_income - 3500) * 0.02, 2)
  - low_net: low_income - low_deduction
  - low_tax: round(low_net * 0.145, 2)
  - low_basic_federal: max(0, low_tax - round((16129 + low_credit_base) * 0.145, 2))
  - high_net: high_income - high_rrsp - full_deduction
  - high_tax: round(58399.85 + (high_net - 253414) * 0.33, 2)
  - high_credits: round((14538 + full_credit_base) * 0.145, 2)
  - high_basic_federal: high_tax - high_credits
  - high_federal_cpp_subtotal: high_basic_federal + full_cpp
expected:
  full_cpp: 8860.20
  full_credit_base: 3356.10
  full_deduction: 5504.10
  standard_net: 69495.90
  standard_tax: 10804.16
  standard_credits: 2825.34
  standard_basic_federal: 7978.82
  standard_federal_cpp_subtotal: 16839.02
  low_cpp: 1249.50
  low_credit_base: 519.75
  low_deduction: 729.75
  low_net: 13270.25
  low_tax: 1924.19
  low_basic_federal: 0
  high_net: 262005.90
  high_tax: 61235.18
  high_credits: 2594.64
  high_basic_federal: 58640.54
  high_federal_cpp_subtotal: 67500.74
```

### Case 4. BPA midpoint and bounded phase-out

A full-year resident's 2026 net income is **219,961**, exactly halfway between 181,440 and 258,482; taxable income after a separate supported deduction may be different. BPA is **15,640.50**, with a **2,189.67** ordinary credit. At NI 181,440 it remains 16,452; at 258,482 and above it is 14,829. Use NI, not a lower taxable-income figure, and do not extrapolate below the minimum. This is a BPA component example, not a complete return. [ITA 118(1.1)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html); [indexed amounts](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html).

```oa-check
name: 2026 T1 BPA exact boundaries and midpoint
inputs:
  midpoint_ni: 219961
steps:
  - midpoint_bpa: round(16452 - 1623 * clamp((midpoint_ni - 181440) / 77042, 0, 1), 2)
  - midpoint_credit: round(midpoint_bpa * 0.14, 2)
  - at_lower: 16452 - 1623 * clamp((181440 - 181440) / 77042, 0, 1)
  - at_upper: 16452 - 1623 * clamp((258482 - 181440) / 77042, 0, 1)
  - above_upper: 16452 - 1623 * clamp((400000 - 181440) / 77042, 0, 1)
expected:
  midpoint_bpa: 15640.50
  midpoint_credit: 2189.67
  at_lower: 16452
  at_upper: 14829
  above_upper: 14829
```

### Case 5. Separate credit components, not one multiplier

Assume actual eligible facts: 2026 claimant NI 60,000, eligible unreimbursed medical expenses 5,000 within the permitted period; an ordinary receipted donation 1,000 within its income limit and below the 33% taxable-income band; actual Canadian eligible dividends 1,000 and other dividends 1,000 requiring gross-up; and a separate mixed-income worker with qualifying employment income 1,000 plus business income. Medical threshold is 1,800, base 3,200, credit **448**. Donation credit is **260**. Taxable dividends are 1,380 and 1,150, with illustrative calculated federal credits **207.27** and **103.85**; actual slip/worksheet amounts govern. The mixed worker's CEA amount is **1,000**, credit **140**; no business-income CEA is added. These are isolated components, not one taxpayer's reconciled return or a mixed-CPP calculation. [Medical law](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.2.html); [donation law](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.1.html); [dividend worksheet](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf); [CEA law](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html).

```oa-check
name: 2026 T1 medical donation dividend and employment-credit components
inputs:
  ni: 60000
  medical: 5000
  donation: 1000
  eligible_cash: 1000
  other_cash: 1000
  qualifying_employment: 1000
steps:
  - medical_threshold: min(ni * 0.03, 2890)
  - medical_base: max(0, medical - medical_threshold)
  - medical_credit: round(medical_base * 0.14, 2)
  - donation_credit: round(min(donation, 200) * 0.14 + max(0, donation - 200) * 0.29, 2)
  - eligible_taxable: eligible_cash * 1.38
  - other_taxable: other_cash * 1.15
  - eligible_dtc: round(eligible_taxable * 0.150198, 2)
  - other_dtc: round(other_taxable * 0.090301, 2)
  - cea_amount: min(qualifying_employment, 1501)
  - cea_credit: round(cea_amount * 0.14, 2)
expected:
  medical_threshold: 1800
  medical_base: 3200
  medical_credit: 448
  donation_credit: 260
  eligible_taxable: 1380
  other_taxable: 1150
  eligible_dtc: 207.27
  other_dtc: 103.85
  cea_amount: 1000
  cea_credit: 140
```

### Case 6. Top-up uses eligible credit dollars and the statutory multiplier

Assume the precisely defined eligible credit-dollar sum A is **9,000**, with sufficient tax and supported eligible claims. For 2026, subtract 8,193.22 and multiply 806.78 by **7.14%**: **57.60**. For a separate 2025 return, the actual worksheet subtracts 8,319.38 and multiplies the excess by **3.45%**: **23.48**. A 2026 eligible sum of 8,000 produces zero. These are credit components; they do not assume all donation or dividend credits qualify. [ITA 118(11)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html); [2025 worksheet 34990](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf).

```oa-check
name: T1 top-up actual multipliers and zero floor by year
inputs:
  eligible_credit_dollars: 9000
steps:
  - threshold2026: 58523 * 0.14
  - topup2026: round(max(0, eligible_credit_dollars - threshold2026) * 0.0714, 2)
  - topup2025: round(max(0, eligible_credit_dollars - 8319.38) * 0.0345, 2)
  - below_threshold: round(max(0, 8000 - threshold2026) * 0.0714, 2)
expected:
  threshold2026: 8193.22
  topup2026: 57.60
  topup2025: 23.48
  below_threshold: 0
```

### Case 7. Instalment threshold and payment amount are different

Assume a non-Quebec ordinary instalment case with actual 2026 net tax owing **4,000** and a qualifying prior year's net tax owing over 3,000; current-year estimated CPP payable 9,292.90 and voluntary EI payable 1,123.07 are already independently established. The threshold figure stays **4,000**, not 14,415.97. If using the supported current-year option, total instalment amount is **14,415.97**. Equal-quarter arithmetic displays **3,603.99** to cents, so the four displayed quarters fall short by one cent. Under this working paper's cent-allocation convention, three payments of 3,603.99 leave a final quarter of **3,604.00**. In the actual August-only route, 75% and 25% display **10,811.98 / 3,603.99**, whose displayed sum equals the total. Retaining September at 10,811.98 leaves **3,603.99** for December under that same convention. Reconcile to the actual reminder/payment instructions rather than imposing this presentation convention as a statutory rounding rule. If net tax owing were exactly 3,000, CPP/EI alone would not make this ordinary trigger exceed 3,000. [Current test](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html); [actual 2026 chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf).

```oa-check
name: 2026 T1 instalment trigger separated from CPP and EI payment amount
inputs:
  net_tax_owing: 4000
  cpp: 9292.90
  ei: 1123.07
steps:
  - threshold_figure: net_tax_owing
  - payment_total: net_tax_owing + cpp + ei
  - quarter_display: round(payment_total / 4, 2)
  - four_displayed: quarter_display * 4
  - rounding_excess: four_displayed - payment_total
  - september_display: round(payment_total * 0.75, 2)
  - december_display: round(payment_total * 0.25, 2)
  - last_quarter_reconciled: payment_total - quarter_display * 3
  - quarters_reconciled_total: quarter_display * 3 + last_quarter_reconciled
  - december_reconciled: payment_total - september_display
  - august_route_total: september_display + december_reconciled
expected:
  threshold_figure: 4000
  payment_total: 14415.97
  quarter_display: 3603.99
  four_displayed: 14415.96
  rounding_excess: -0.01
  september_display: 10811.98
  december_display: 3603.99
  last_quarter_reconciled: 3604.00
  quarters_reconciled_total: 14415.97
  december_reconciled: 3603.99
  august_route_total: 14415.97
```

### Case 8. Conditional filing penalties

Assume unpaid tax at the relevant filing deadline is 10,000 and three complete months pass. Ordinary penalty is **800**; if the separate demand/prior-three-year conditions are met, replacement repeated-failure penalty is **1,600**. Do not add them together. Interest from the payment deadline is a separate computation and requires actual rates/receipts. [ITA 162(1)-(2)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html).

```oa-check
name: T1 ordinary and qualifying repeat filing penalty
inputs:
  unpaid: 10000
  months: 3
steps:
  - ordinary: round(unpaid * (0.05 + min(months, 12) * 0.01), 2)
  - qualifying_repeat: round(unpaid * (0.10 + min(months, 20) * 0.02), 2)
expected:
  ordinary: 800
  qualifying_repeat: 1600
```

## Boundary checks

- Confirm income year, residence/province and actual component inputs before using a bracket, credit or contribution ceiling. A 2025 form is not evidence of final 2026 field presentation.
- Keep 15000, 23600 and 26000 distinct. Use 23600 for BPA and the applicable medical threshold; use taxable income for marginal tax and the donation high-rate limit.
- Apply CPP/CPP2 only where coverage and earnings require it. Keep base credit, enhanced deduction and payable separate; route QPP/QPIP and mixed earnings correctly.
- Treat EI as voluntary on actual agreement facts; verify benefit/withdrawal history. Do not confuse twelve-month eligibility with a waiting period.
- No CEA on business income; a mixed worker's actual qualifying employment component is a separate legal input. No double gross-up of dividend slips or multiplication of already computed credits.
- Preserve business-use-of-home loss limits and actual carryforward restrictions. Do not invent RRSP room or default unknown NI to full BPA clawback.
- Reconcile all federal adjustments, provincial result, refundable credits, withholding and instalments before calling an amount the final balance. A basic-tax example is only its stated subtotal.
- A current method's approval must belong to its actual version. This version remains Not yet approved; historical Git credit and an AI source review are not a new accountant approval.

### Return working paper and handoff

Keep one row per supported input/result with year, source/slip, computation, destination and open item:

| Working-paper section | Required output |
|---|---|
| Identity and scope | Income year, residence/province, business PEs, original/amendment/estimate and specialist flags |
| Income | Reconciled business/professional/commission output, employment, taxable investment and other income; 15000 |
| Deductions | Actual RRSP choice/room, 22200, 22215 and other supported deductions; 23600 |
| Taxable income | Supported Division C deductions and carryforwards; 26000 |
| Federal calculation | Marginal tax; BPA/base CPP/EI/CEA/medical credit bases; separate donation/top-up/dividend credits; basic and net federal outputs |
| Total payable | Actual 42100/42120, repayments, provincial computation and other applicable items; total payable |
| Payments and refundable credits | Actual withholding, instalment receipts, overpayments/abatements and supported refundable claims; total credits |
| Balance or refund | Reconciled proposed result, payment deadline, open items and authorized review |

Review flags: province/residency, year, CPP/QPP form and elections, actual RRSP support, BPA phase-out, credit eligibility, instalment trigger/option/interest, April payment versus June filing, unresolved adjustments and submission authority. This preserves the original spreadsheet-style working paper without a blanket credit multiplier. Provide a file or proposed posting list for human approval where the ledger is read-only; do not claim a journal was posted.

## When to refuse or refer

Refer the affected calculation for non-resident/part-year treatment, death, bankruptcy, unresolved trust or partnership allocation, multi-jurisdiction business/foreign-tax allocation, AMT/split-income or unusual donation/property rules, disputed pension/coverage/election facts and complex benefit claims. Provincial tax stays with its provincial method, without dropping a federal abatement or T2203 issue. Identify what is known, the exact missing record, applicable source and deadline; do not substitute a guessed liability.

For ordinary work, give the authorized accountant the reconciled return working paper, source year/version, income statements, contribution calculations, supported credits/deductions, payment history, draft filing result and open items. Only the authorized person decides whether to approve, sign, file, pay or post. No professional approval is claimed from this source review.

## Sources

Read **November 13, 2026**. Justice displays the Act current to October 19, 2026, last amended June 18, 2026. Indexed annual dollar amounts are read from the year-specific CRA tables, not guessed from the statute's base figures. Actual 2025 annual PDFs remain dated 2025; published 2026 rates, enacted credits and the actual 2026 instalment chart support the 2026 estimate. Official forms were downloaded for offline text/visual checks. The instalment PDF's metadata title says 2024, but its actual pages say 2026; content year governs.

| Source family | Official sources and use | Read on | What was read |
|---|---|---|---|
| Enacted income-tax structure | [ITA 117 rates](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-117.html), [118 BPA/CEA/top-up](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.html), [118.1 gifts](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.1.html), [118.2 medical](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-118.2.html), [82 dividends](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-82.html), [121 dividend credit](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-121.html) | 2026-11-13 | Read for sections 117, 118(1)/(1.1)/(10)/(11), 118.1(1)/(3), 118.2, 82 and 121: year structure, conditions and distinct credit formulas. |
| Year amounts | [2026 brackets](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/current-year.html), [2025 brackets](https://www.canada.ca/en/revenue-agency/services/tax/individuals/tax-rates-brackets/last-year.html), [indexed BPA/CEA/medical amounts](https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/adjustment-personal-income-tax-benefit-amounts.html), [RRSP annual limits](https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html) | 2026-11-13 | Read for 2026 and 2025 federal band rows, indexed BPA/CEA/medical rows and RRSP annual ceiling rows; exclude unrelated benefit tables. |
| Observed filing fields | [2025 T1, Ontario package](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-r/5006-r-25e.pdf), [2025 Federal Worksheet](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-d1/5000-d1-25e.pdf), [2025 T2125](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/t2125/t2125-25e.pdf), [T1 catalogue](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5006-r.html) | 2026-11-13 | Read for 2025 T1 Steps 3-6, worksheet BPA/34990/40425, T2125 9946 and catalogue year labels; visual checks of T1 page 6 and worksheet page 7. |
| Contribution methods | [CPP annual table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/canada-pension-plan-cpp/cpp-contribution-rates-maximums-exemptions.html), [CPP2 table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/calculating-deductions/making-deductions/second-additional-cpp-contribution-rates-maximums.html), [2025 Schedule 8](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s8/5000-s8-25e.pdf), [22200](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-22200-deduction-cpp-qpp-contributions-on-self-employment-other-earnings.html), [31000](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31000-cpp-qpp-contributions-on-self-employment-other-earnings.html) | 2026-11-13 | Read for CPP annual 2026/2025 rows, CPP2 maxima and Schedule 8 Parts 3-5, plus actual 22200/31000 form-selection instructions. |
| Voluntary EI | [Benefit types and Quebec routing](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers.html), [Premiums](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/premiums.html), [eligibility](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/eligibility.html), [withdrawal](https://www.canada.ca/en/services/benefits/ei/ei-self-employed-workers/withdraw.html), [annual EI table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll/payroll-deductions-contributions/employment-insurance-ei/ei-premium-rates-maximums.html), [actual Schedule 13 catalogue](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/5000-s13.html) | 2026-11-13 | Read for benefit categories and Quebec routing, premiums, twelve-month agreement condition, withdrawal rules, annual rate rows and both pages of actual 2025 Schedule 13; the first web PDF request failed but offline extraction succeeded. |
| Credits and conditions | [CEA page with simplification noted](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-31260-canada-employment-amount.html), [medical conditions](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/lines-33099-33199-eligible-medical-expenses-you-claim-on-your-tax-return.html), [2025 Schedule 9](https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5000-s9/5000-s9-25e.pdf), [dividend inclusion](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/personal-income/line-12000-taxable-amount-dividends-eligible-other-than-eligible-taxable-canadian-corporations.html), [34990](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-34990-top-up-tax-credit.html) | 2026-11-13 | Read for CEA eligibility/form discrepancy, medical claimant/period/threshold, Schedule 9 gift limits/rates, dividend taxable-slip mapping and top-up worksheet route. |
| Deductions and overlays | [RRSP room](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/rrsps-related-plans/contributing-a-rrsp-prpp/contributions-affect-your-rrsp-prpp-deduction-limit.html), [business-use-of-home](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/t4002/t4002-5.html), [Quebec abatement/T2203](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-44000-refundable-quebec-abatement.html) | 2026-11-13 | Read for RRSP room components, business-use-of-home loss limit and Quebec business-PE/T2203 abatement conditions. |
| Instalments | [Current test](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/who-pays-instalments.html), [2026 chart](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/ndvdls/tpcs/ncm-tx/pymnts/nstlmnts/Instalment-chart-fill-26e.pdf), [options](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/options-calculate.html), [due dates](https://www.canada.ca/en/revenue-agency/services/payments/payments-cra/individual-payments/income-tax-instalments/due-dates.html), [ITA 156.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-156.1.html) | 2026-11-13 | Read for current/prior-year threshold conditions, both actual 2026 chart pages, three options and due-date rules; visually checked chart page 2. |
| Filing, payment, correction | [ITA 150](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-150.html), [162](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-162.html), [CRA deadlines](https://www.canada.ca/en/services/taxes/resources-for-small-and-medium-businesses/2026-tax-deadlines-canadian-businesses-self-employed-individuals.html), [interest/penalties](https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/interest-penalties/late-filing-penalty.html), [filing options](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/how-file.html), [changing a return](https://www.canada.ca/en/services/taxes/income-tax/personal-income-tax/after-you-file/change-return.html) | 2026-11-13 | Read for 150(1)(d), 162(1)-(2), 2027 self-employed deadlines, daily interest/payment receipt, certified filing and assessed-return change routes. |

**Not yet confirmed:** final 2026 annual T1/worksheet/Schedule 8/Schedule 13 layouts and internal line presentation, a particular person's unknown eligibility/room/elections, case-specific benefits or interest, and any accountant approval of this replacement version. Current-year estimates are not a claim that a return has been professionally approved, accepted or filed.
