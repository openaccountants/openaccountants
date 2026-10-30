---
name: ad-income-tax
description: "Compute Andorra resident personal income tax for calendar 2026, including employment, pensions, direct or objective sole-trader income, rental income, investments and capital gains. Use for fiscal residence, IRPF allowances and proportional bonus, family and housing reductions, loss pools, property sale and reinvestment, foreign-tax credits, advances and annual return reconciliation. This Guide distinguishes employment expense relief from business deductions, general income from savings and resident property taxation from IRNR. Read the payroll and social Guide for the actual 2026 CASS category and wage period, the IGI Guide for indirect tax, and the corporate and cross-border Guides for their separate computations. Figures require the cited facts and documents. Source-cited draft, without accountant attestation."
version: 0.3
jurisdiction: AD
tax_year: 2026
last_updated: 2026-10-29
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Andorra individual income tax (IRPF), 2026 v0.3

## Who this applies to

Resident individuals, including employees, pensioners, sole traders and landlords, for calendar 2026; amounts in EUR. Resident income is worldwide. Residence requires more than 183 days, counting sporadic absences unless foreign residence is evidenced, or the principal activity/economic-interest base in Andorra. A resident spouse and minor children create a rebuttable presumption; daily frontier workers commuting from Spain/France have the specific exclusion. Record days, economic facts and any operative treaty before choosing IRPF or IRNR. [Law 5/2014 arts. 4, 8][law].

Compute the general and savings bases separately. Use the combined payroll/social Guide for CASS, the IGI Guide for indirect tax, the corporate Guide for imported business-base rules, and the non-resident Guide for IRNR/PE and corporate departure. These are source-cited drafts, without accountant attestation.

## Rates, bands and thresholds

| Item | 2026 rule | Primary authority |
|---|---|---|
| Statutory rate | 10% on positive general and savings liquidation bases | [Arts. 43–44][law] |
| Personal reduction | 24,000; 30,000 for qualifying incapacity; conditional household/spouse rule up to 40,000 | [Art. 35(1)][law] |
| Family reduction | 1,000 per qualifying descendant under 25, ascendant over 65, or ward/foster dependant who lives with or depends on the taxpayer and whose annual income is not above the minimum wage (salari mínim interprofessional); circumstances are taken at accrual (31 December, or the date of death if the taxpayer dies during the year) | [Art. 35(2)][law]; [arts. 36(2), 40–41][law] |
| Minimum wage for the dependant-income test, 2026 | Monthly 1,525.33 from 1 January 2026 (Decret 8/2026, BOPA núm. 3, 14 January 2026); monthly 1,568.67 from 1 July 2026 (Decret 253/2026, BOPA núm. 77, 8 July 2026). Annual test: 18,564.00 or less qualifies; above 18,824.04 fails; 18,564.01 to 18,824.04 is not settled (method below) | [Labour Inspection circular, January 2026][smi1]; [Labour Inspection circular, July 2026][smi7] |
| Annual figure the Govern used in earlier years | 17,367.96 for 2025 and 16,515.24 for 2024 (monthly minimum wage × 12) | [Guia IRPF 2025][g25]; [Guia IRPF 2024][g24] |
| Disability/dependency and tuition | Family amount multiplied by 1.5 for the specified recognised cases, without the ordinary age test; actual qualifying higher-education tuition up to 300 per descendant | [Art. 35(2)–(3)][law] |
| Employment expenses | Employee public social-security contributions plus 3% of eligible gross employment receipts, capped at 2,500; specified receipt classes excluded | [Arts. 12–13][law] |
| General-income bonus | 50% of 10% of general income after the first-paragraph personal reduction, maximum 800 | [Art. 46][law] |
| Savings reduction | 3,000; liquidation base cannot become negative | [Arts. 34, 37][law] |
| Home acquisition | 50% of qualifying payments, maximum 5,000/year; conditions and reinvestment coordination below | [Art. 38][law] |
| Affordable-rental acquisition | 50% of qualifying payments, maximum 5,000/year, for the specified affordable permanent-home rental | [Art. 38 bis][law] |
| Pension contributions | Lesser of 30% of net employment/business income and 5,000/year; qualifying instrument required | [Art. 39(1)][law]; [regulation art. 18][reg] |
| Objective business option | Prior-year turnover at most 300,000, or 150,000 for professionals; estimated expenses 80% strictly commercial, 3% directors, 40% other | [Art. 17][law] |
| Ordinary tax late interest | 4.05% annually for 2026 under the statutory period/base rules; distinct from the 3.24% legal rate | [General Tax Law art. 23][general]; [Budget Law 1/2026 art. 17][budget] |

The 24,000 amount is a base reduction. The bonus is proportional before its cap: do not deduct a flat 800 whenever income enters the next band. Eligibility for an enhanced household reduction depends on general-base income, not an unsupported requirement that the partner receives no income of any kind. [Arts. 35, 43–46][law].

## The base

1. **Reconcile source income and timing.** Employment and capital receipts are recognised when due or, if earlier, collected; business income follows the accounting accrual rules; gains arise on the relevant asset alteration. Retain invoices, payslips, contracts, asset and CASS records, not only bank descriptions. Own-account transfers, loan principal and refundable deposits are not automatically sales or operating expenses. Output IGI collected and recoverable input IGI must be reconciled separately from net business revenue/cost. [Arts. 4, 12, 14–16, 42][law]; [corporate arts. 9, 19][cit].
2. **Employment and pensions.** Include covered salary, bonuses, taxable benefits, notice/termination amounts and the article 12 pension/benefit classes. Article 5 separately exempts mandatory termination compensation, qualifying personal-injury compensation, specified disability/widow/orphan/social benefits, scholarships and qualifying prizes. Medical-cost reimbursements described in article 12(2)(g) are not income. Check each legal condition. Deduct employee public social contributions and 3% only on article 13's eligible employment receipts, capped at 2,500. The 3% excludes the listed unemployment, representation, travel, option, termination, public-office and pension/other receipt categories. For non-CASS private pension receipts, article 12(3) prevents taxing qualifying contributions already taxed and not previously deducted; annuities use its contribution/provision ratio and cumulative limit. [Arts. 5, 12–13, 29][law].
3. **Direct business method.** Reconcile accounting profit to tax using corporate articles 9–19, with the IRPF article 16 exceptions. Capital expenditure follows effective depreciation and the corporate Annex I lives; interest, impairments, provisions, grants, related payments and timing require their own adjustments. Add back income tax, fines, disallowed donations/private expenditure and communal taxes treated through the credit. Family wages/rent require contracts, actual work/rights, social registration where required and evidenced market value. Own pension-plan contributions use the personal reduction route. Client meals/representation are classified under the actual law, including corporate article 13's limits, rather than the former blanket prohibition. [Arts. 16, 18, 47][law]; [corporate arts. 9–14, 19 and Annex I][cit].
4. **Registered sole-trader special expenses.** Article 16(3) supplies separate rules: qualifying home rent, insurance/utilities/community/security costs use 35% of cost multiplied by the business-area ratio, unless a different percentage is evidenced; home depreciation uses the statutory area and 40%-of-acquisition-cost constraint, and qualifying Andorran-bank financing uses the business-area ratio. Evidence occasional work-related away-from-usual-place meals and electronic payment: cap at 1% of net turnover and 1,500/year. Actual public transport needs invoices; own-vehicle work travel uses 0.31/km plus evidenced tolls/parking, and 20% of compulsory vehicle insurance qualifies under its separate rule. Avoid claiming the same cost twice. For a contribution base above 100%, the statute additionally specifies 1.18% of the self-employed CASS contribution; retain that calculation separately from ordinary contribution expense. A generic floor-area or mileage estimate does not replace these rules. [Art. 16(3)][law].
5. **Objective business method.** Verify prior-year turnover, annualising a start-year, and the timely all-activity election. Elect before the preceding year ends, or within one month of starting; the method binds for at least three years and renunciation precedes the year of effect. Apply the relevant 80%/3%/40% expense percentage to activity revenue, with asset-disposal results added separately. Compute each activity then integrate; do not additionally deduct actual costs or an employment 3% allowance. Apply market value to free/self-use or materially underpriced supplies under article 15(3). Keep business/private asset allocation under article 18, including its three-year sale rule and cessation exception. [Arts. 15, 17–18][law].
6. **Rental income.** First test article 14(2): rental is business income if, at any time in the preceding period, at least six properties were let/offered or gross rent exceeded EUR 100,000; the statutory combined-property counting rule includes jointly acquired accessories and at most two parking spaces. Return to capital-income treatment only after both triggers cease for two consecutive periods, effective in the next period; a business-treatment option also exists. For rental that remains capital income, use documented direct-method costs or the elected 40% gross-rent expense method, with its prior-year notice and minimum three-year binding period. Article 21 permits an additional ten percentage points for qualifying Andorran permanent-home rents below 9/m² and no more than 1,250/month; verify both limits and the contract before the enhanced deduction. Keep this rental-expense election separate from the acquisition reduction in article 38 bis. [Arts. 14(2), 20–21][law]; [Law 5/2025 art. 79(1)][housing]; [Government explanation of the ten-percentage-point rental increase](https://www.govern.ad/ca/w/canvis-en-reglaments-alguns-impostos-derivats-llei-per-al-creixement-sostenible-dret-habitatge).
7. **Savings and exemptions.** Include taxable interest, foreign dividends and other article 22 receipts, deducting evidenced custody/administration/intermediation costs under article 23. Article 5(j) exempts the specified distributions by Andorran-resident entities/Andorran collective investments subject to corporate tax. Share/collective-investment disposals use article 5(k): aggregate related/family holdings, test the preceding twelve months and 25% boundary, or the specified ten-year holding alternative. Interests backed at least 50% by Andorran property are excluded. The foreign-property ten-year exemption is a separate rule. Gifts/inheritances received are outside IRPF under article 4(4); the donor's gain exemptions and carryover values/dates require article 5(l)–(m), not an inference that every gift or property filing is exempt. [Arts. 4–5, 22–27][law].
8. **Gains, losses and reductions.** For ordinary taxable disposals reconcile transfer and acquisition values, qualifying costs/improvements, market-value safeguards and the statutory homogeneous-share cost method. Unproved/private/gift/gambling losses are disallowed; repurchase loss rules use one year for assets/unlisted shares and two months for listed homogeneous securities. General income and savings each have their own ten-year negative-base carryforward; do not cross-net the two pools. Apply personal/family reductions first, then qualifying home/pension/maintenance reductions without creating a negative liquidation base. Share family relief equally where entitlement is equal, with the nearest-relative rule; short periods/deceased dependants use article 36. Deduct qualifying civil/judicial/notarial spouse maintenance, excluding child support. [Arts. 24–27, 30–39][law].
9. **Liquidate and settle.** Tax positive general and savings liquidation bases at 10%, deduct the article 46 bonus first, then qualifying communal, foreign and incentive credits without a negative settlement liability. Article 47 communal-tax and article 48 foreign-credit balances have a three-year insufficiency carryforward; retain origin/expiry/evidence. Donations and business incentives use articles 48 bis/49 and their actual conditions. Finally deduct withholding, advances and the property payment on account; an excess is a refund, not a negative tax charge. [Arts. 44–49, 52, 58][law].

For CASS pensions and similar benefits, obtain the contribution history before fixing gross taxable employment income. If contributions began before 1 January 2015 and the recipient had at least fifteen total CASS contribution years when the benefit began, reduce each year’s receipt by 1% for each pre-2015 contribution year, rounding a fraction of a year up to a whole year. Cap the reduction at 30% of that year’s pension or benefit. This reduces the receipt used in the ordinary net-employment calculation; it does not make pensions eligible for the 3% employment-expense allowance. [Additional provision 5 and final provision 5; arts. 12–13][law].

**Personal and investment reductions.** The household EUR 40,000 rule requires the qualifying cohabiting spouse/partner facts and unused general-base personal reduction, capped jointly as article 35 provides. Family relief uses age/status at accrual, the annual-income test set out in the next paragraph, CONAVA disability or COVASS dependency recognition and equal-sharing/nearest-relative rules. The EUR 300 tuition amount is actual qualifying higher-education tuition, not a flat additional allowance. Home acquisition includes qualifying acquisition costs and, for third-party borrowing, principal, interest and associated loan costs; register in the parish census within twelve months of acquisition or restore relief plus interest in the failure period. The same 50%-of-paid-cost, EUR 5,000 annual maximum structure applies to article 38 bis's acquired home let for another individual's habitual/permanent residence at a legally affordable price. Obtain the actual regulated affordable classification; the under-EUR-9 rental-income incentive is a different test. Pension contributions must meet regulation article 18's instrument, provider, irrevocable rights and permitted-access requirements, including the specified unemployment/illness/departure exceptions; an ordinary savings product is not enough. [Arts. 35–39][law]; [regulation art. 18][reg].

**Dependant-income test.** Article 35(2) allows the 1,000 family reduction (and the 300 tuition amount) only when the descendant, ascendant or ward has annual income not above the minimum wage. Article 36(2) takes family circumstances at accrual, which is 31 December, or the date of death if the taxpayer dies during the year (arts. 40(2) and 41). If a qualifying descendant dies during the year, the amount is pro-rated by the days on which the conditions were met (art. 36(2), second paragraph). The law does not say how to annualise a minimum wage that changes during the year. The Govern's IRPF guides use the monthly minimum wage × 12: 17,367.96 for 2025 (1,447.33 × 12) and 16,515.24 for 2024, and both write the test as income equal to or below that figure. In 2026 the monthly minimum wage was 1,525.33 from 1 January and 1,568.67 from 1 July, which gives two readings. Months in force: 6 × 1,525.33 + 6 × 1,568.67 = 18,564.00. Rate in force at accrual × 12: 1,568.67 × 12 = 18,824.04. Apply it this way: a dependant with 2026 annual income of 18,564.00 or less meets the test under either reading; one above 18,824.04 fails under either reading. **Audit flash point:** income from 18,564.01 to 18,824.04 is not settled until the Govern's 2026 IRPF guide states the annual figure or the Departament de Tributs i de Fronteres answers a written tax consultation. Under General Tax Law article 65 the consultation is filed before the return deadline, the answer is binding on the tax administration and is due within two months, and no answer in that time means the taxpayer's proposed treatment is accepted. Do not claim the reduction for a dependant in that band on a guess; get the guide or the consultation first. [Arts. 35(2), 36(2), 40–41][law]; [Guia IRPF 2025][g25]; [Guia IRPF 2024][g24]; [Labour Inspection circulars][smi1], [July 2026][smi7]; [General Tax Law art. 65][general]. The 18,564.00 and 18,824.04 figures assume a full calendar-year period.

**Andorran property disposals.** Article 27 bis has a separate real-value base, also covering its property-rich interests/rights, judicial awards and debt-settlement acts. Add lawful, invoiced improvements and qualifying direct acquisition/development costs; subtract prior tax-deductible depreciation. The gain is reduced by coefficients 0.8 for more than six through seven years, 0.6 for more than seven through eight, 0.4 for more than eight through nine, and 0.2 for more than nine through ten; after more than ten years it is excluded from the base. Calculate dates exactly. Additional provision 9 separately charges 10% of the defined gain below two years and 5% from two to under five years, before the annual savings-base calculation. The non-resident 25%/20%/15%/10% schedule is a different regime. [Art. 27 bis and additional provision 9][law]; [Law 5/2025 art. 79 and fifth transition][housing].

For principal-home reinvestment, verify the article 5(r) nationality/effective-residence or five-year legal-residence condition, qualifying habitual home, no outstanding general-administration debt and prior approval. Full relief requires reinvestment of the sale proceeds, with proportional relief for less. The statutory reinvestment period is one year; the regulation also addresses a new home bought within six months before sale. Obtain approval before the transfer and execute within three months of approval. Submit the sale/new deed within one month, census proof within six months of reinvestment, and annual residence/utility evidence. Article 5(r) states the four-year habitual-home condition; comply with the approval's actual conditions and preserve evidence. Loss of relief requires the prescribed self-assessment and interest within one month. Coordinate exempt gain with the new-home reduction under article 38(2). [Arts. 5(r), 38(2)][law]; [regulation art. 14][reg].

## Deadlines and filing

| Duty | Statutory method/deadline | Source |
|---|---|---|
| Annual IRPF | File and pay between 1 April and 30 September following the tax year: 2026 income in 2027 | [Arts. 55–56][law] |
| Filing exclusions | Sole employment, movable-capital and exempt sources have article 55(2)'s exclusion; article 55(3) overrides where the covered income was not subject to required payments on account | [Art. 55][law] |
| Business advance | September; 50% prior settlement liability or elected 5% prior business net income; first activity period excluded; short-period rules apply | [Art. 51(8)][law]; [regulation art. 19][reg] |
| Resident property payment on account | 10% of the income determined under the property rules; private contract within 30 days, public deed simultaneously; exempt-income and deferred-price conditions apply | [Arts. 51 bis–ter][law] |
| Ordinary negative annual settlement | Provisional assessment/refund within the statutory three-month framework from filing; interest for authority-attributable delay | [Art. 58][law] |
| Objective business/rental option | Before preceding year-end; business start option within one month; minimum three years | [Arts. 17, 21][law] |

Obtain the NRT, reconcile the approved return to the source-level workpapers and retain submission, payment, withholding and property-notary evidence. Employment withholding follows the payroll Guide's personalised ministerial percentage and CASS/non-CASS filing distinction; the old illustrative salary bands are not a filing instruction. A return exclusion is not an exemption from the underlying tax. [Arts. 50–55][law]; [regulation arts. 24–36][reg].

**Resident investment-income withholding.** The ordinary rate is 10% of gross taxable movable-capital income. Article 51(4) permits the taxpayer to request the EUR 3,000 savings reduction at source without duplicating it across payers. Use the regulation article 38 official communication, based on a reasonable estimate of all movable-capital income for the year, identifying the relevant account, deposit, instrument or contract. A valid election prevents withholding on the receipts covered by that election under article 37(3); promptly notify the payer on the official model if the all-payer estimate no longer supports the reduction, so withholding resumes on subsequent receipts. Retain the original communications. Capitalisation operations have article 37(2)’s separate gain-base and derived-rate calculation rather than an automatic 10% of returned capital. [Law arts. 51(4), 51(6)–(7)][law]; [regulation arts. 37–38][reg].

For foreign securities within article 50(9), the responsible custodian/intermediary reduces withholding by the qualifying foreign-tax credit: the lesser of evidenced actual comparable foreign income tax and 10% of the gross receipt. Compute this limit receipt by receipt for withholding; do not substitute it for the annual article 48 credit calculation. Article 5 exempt income has no withholding and no declaration obligation under article 51(7). [Arts. 50(2), 50(6), 50(9), 51(5)–(7)][law]; [regulation art. 37(4)][reg].

Declare and remit movable-capital withholding during April, July, October and January for the preceding quarter. The January annual summary identifies recipients, NRT, income and withholding. Authorised financial/insurance entities instead submit the signed original external-auditor report during the following first calendar semester; using their existing external auditors requires prior ministry approval. The separate January declaration for article 38 elections still reports the relevant receipts and any withholding. [Regulation art. 39][reg].

## Penalties and interest

Under General Tax Law article 24, voluntary late filing with tax payable attracts 2% when less than two months late, 5% between two and twelve, and 10% after twelve; filing following a formal request uses 15% if its deadline is met. Article 24(4)–(5) controls interaction: after six months, or with a prior request, interest and applicable sanctions are not automatically excluded. Identify the actual period and whether the administration requested filing before calculating. [General Tax Law art. 24][general].

Executive-recovery charges are mutually exclusive: 2% before the enforcement notice, 10% within the reduced enforcement-payment conditions, otherwise 20%. The ordinary 20% charge is compatible with interest; the 2% and 10% charges exclude it. Apply article 23's overdue base/period and the 2026 tax late-interest rate of 4.05%; CASS has separate rules. [Arts. 23–25][general]; [Budget art. 17][budget].

IRPF articles 59–61 specify simple-offence fines of EUR 150–3,000 and defraudation sanctions of 50%–150% of evaded tax, with the general-law graduation rules. The specific statute controls over an assumed universal EUR 200/250 general documentary fine. Article 60 separately identifies the property-value discrepancy offence; it is not a valuation safe harbour. Article 62 permits thirteen working days for representations on the proposed sanction and sets the guarantee requirement for suspension on appeal. General Tax Law article 132 has conditional 30% agreement/payment and further 25% timely-sanction-payment reductions; the actual offence, appeal and payment facts govern. Do not automatically equate every error with evasion or add all charges together. [IRPF arts. 59–62][law]; [General Tax Law arts. 125–132][general].

## Cross-border points

Aggregate worldwide receipts by their correct general/savings category and apply an operative treaty only after residence, income article and evidence checks. Article 48's credit is the lower of actual qualifying foreign income tax (within the treaty limit) and Andorran tax attributable to the same income under Andorran expense rules. Include foreign tax in gross income; group by country, with each PE separate. Retain tax/payment proof and the three-year insufficiency-credit ledger; foreign tax above the substantive cap is not automatically a transferable credit. [Arts. 3, 4, 48][law].

On loss of taxpayer status through fiscal-residence change, include all income pending imputation in the last resident period under article 42(3). Record departure facts and outstanding accrual/deferred-income schedules. Immigration authorisation and deposits are separate from the fiscal-residence test. Non-resident wages, treaty employment cases, PE profits and company migration use the companion cross-border Guide. [Arts. 8, 40–42][law].

## Two worked examples that recompute

### 1. Direct-method sole trader, without the employment allowance

Assume a full-year resident's revenue is 55,000 net of IGI, evidenced ordinary deductible business expenses 9,000 and actual deductible self-employed CASS 7,055.40. The correctly established prior-year category supports a 100% CASS base throughout the year; no reduction, additional contribution deduction, family/home/pension relief, other income, credit or payment on account applies. General income is 38,944.60. After 24,000 personal reduction, gross tax is 1,494.46 and the proportional bonus 747.23, leaving 747.23. [Arts. 16, 35, 43–46][law].

```oa-check
name: Andorra 2026 direct business income and proportional bonus
inputs:
  net_revenue: 55000
  evidenced_business_expenses: 9000
  deductible_cass_paid: 7055.40
  personal_reduction: 24000
steps:
  general_income: net_revenue - evidenced_business_expenses - deductible_cass_paid
  liquidation_base: max(0, general_income - personal_reduction)
  gross_tax: liquidation_base * 0.10
  bonus: min(800, liquidation_base * 0.10 * 0.50)
  settlement_tax: max(0, gross_tax - bonus)
expected:
  general_income: 38944.60
  liquidation_base: 14944.60
  gross_tax: 1494.46
  bonus: 747.23
  settlement_tax: 747.23
```

### 2. Ordinary wages, foreign dividends and a capped credit

Assume ordinary salary 60,000, employee CASS 3,900, and all salary qualifies for the 3% expense deduction. No family/home/pension relief or losses. Foreign dividends are 8,000 gross, with 800 qualifying actual foreign tax permitted by the operative treaty and no other savings income/cost. Employment expense is 1,800, general income 54,300, general tax after the 800 bonus is 2,230. Savings tax is 500 after its 3,000 reduction. The allowable foreign credit is 500, fully usable; the above-cap 300 is not an insufficiency carryforward. Actual resident withholding of 2,000 leaves 230 payable. The withholding is an evidenced input, not a salary-table rate. [Arts. 13, 35, 37, 43–48, 52][law].

```oa-check
name: Andorra 2026 employment savings and capped foreign credit
inputs:
  ordinary_salary: 60000
  employee_cass: 3900
  foreign_dividends_gross: 8000
  qualifying_foreign_tax: 800
  actual_resident_withholding: 2000
steps:
  employment_expense: min(2500, ordinary_salary * 0.03)
  general_income: ordinary_salary - employee_cass - employment_expense
  general_base: max(0, general_income - 24000)
  general_tax: max(0, general_base * 0.10 - min(800, general_base * 0.10 * 0.50))
  savings_base: max(0, foreign_dividends_gross - 3000)
  savings_tax: savings_base * 0.10
  foreign_credit: min(qualifying_foreign_tax, savings_tax)
  settlement_tax: general_tax + savings_tax - foreign_credit
  final_payment: settlement_tax - actual_resident_withholding
expected:
  employment_expense: 1800
  general_income: 54300
  general_base: 30300
  general_tax: 2230
  savings_base: 5000
  savings_tax: 500
  foreign_credit: 500
  settlement_tax: 2230
  final_payment: 230
```

## Ask the client first

- What are the year's presence, economic-interest, family and foreign-residence facts?
- Which receipts are wages, business, rent, investments, benefits, grants or disposals, and when were they due/paid?
- Which costs, CASS category/payments, assets, actual-use and prior-year elections are evidenced?
- What establish spouse/dependant income, recognition, cohabitation, tuition, home and pension eligibility?
- What was each claimed dependant's total 2026 annual income? If it is between 18,564.01 and 18,824.04, the family reduction waits for the Govern's 2026 IRPF guide or a binding consultation.
- Which tax losses, communal/foreign credits, treaty documents, withholding and advance payments remain available?
- For property, what establish ownership dates, tax basis/depreciation, improvements, deed/contract and reinvestment approval?

## Sources

| Source and read scope | URL | Read on |
|---|---|---|
| Law 5/2014, current consolidation: cited residence, income classes, expense/base, exemption, property, reduction, credit, withholding and return articles, additional provision 5 and final provision 5 | https://www.portaljuridicandorra.ad/L2014005 | 2026-10-27 |
| Law 5/2014 version register, current thirteenth consolidation and application-date qualification | https://www.portaljuridicandorra.ad/L2014005_F | 2026-10-27 |
| IRPF regulation of 29 December 2023, arts. 14, 18–19, 24–39 cited procedures | https://www.portaljuridicandorra.ad/R20231229D | 2026-10-27 |
| Law 5/2025 art. 79 and fifth transition, property, rental and family amendments | https://www.portaljuridicandorra.ad/L2025005 | 2026-10-27 |
| Corporate Law 95/2010 arts. 9–14, 18–19 and Annex I, imported business-base method | https://www.portaljuridicandorra.ad/L2010095 | 2026-10-27 |
| General Tax Law 21/2014, arts. 23–25 and 125–132, interest/charges and sanctions | https://www.portaljuridicandorra.ad/L2014021 | 2026-10-27 |
| Government explanation, qualifying rental reduction | https://www.govern.ad/ca/w/canvis-en-reglaments-alguns-impostos-derivats-llei-per-al-creixement-sostenible-dret-habitatge | 2026-10-27 |
| Budget Law 1/2026 art. 17, annual legal and tax late-interest rates | https://www.portaljuridicandorra.ad/L2026001 | 2026-10-27 |
| Law 5/2014 arts. 35(2), 36(2) and 40–41, dependant-income test and accrual date | https://www.portaljuridicandorra.ad/L2014005 | 2026-10-29 |
| Labour Inspection circular (published by CASS), minimum wage from 1 January 2026 (Decret 8/2026) | https://www.cass.ad/sites/default/files/arxius/Circular%20informativa%20Salari%20m%C3%ADnim%202026.pdf | 2026-10-29 |
| Labour Inspection circular, minimum wage from 1 July 2026 (Decret 253/2026) | https://www.cass.ad/sites/default/files/arxius/Circular%20informativa%20salari%20m%C3%ADnim%20a%20partir%20de%20l%271%20de%20juliol%20del%202026_0.pdf | 2026-10-29 |
| Govern, Guia IRPF 2025, family minimum and annual minimum-wage figure | https://www.govern.ad/documents/d/guest/guia_irpf | 2026-10-29 |
| Govern, Guia IRPF 2024, family minimum and annual minimum-wage figure | https://www.govern.ad/documents/d/guest/Guia_IRPF_2024 | 2026-10-29 |
| Labour Inspection circular, minimum wage 2025 (Decret 4/2025), monthly 1,447.33 | https://www.cass.ad/sites/default/files/arxius/Circular%20informativa%20Salari%20m%C3%ADnim%202025.pdf | 2026-10-29 |
| Labour Inspection circular, minimum wage 2024 (Decret 577/2023), monthly 1,376.27 | https://www.cass.ad/sites/default/files/documents/Circular-informativa-del-salari-minim-de-l-any-2024.pdf | 2026-10-29 |
| General Tax Law 21/2014, art. 65, written tax consultations | https://www.portaljuridicandorra.ad/L2014021 | 2026-10-29 |

The legal portal consolidations expressly lack official legal status; their current/historical text is provided through the BOPA service. The cited amendment is separately checked. Exact retrievals and article-read limits are in the country research record. The independent source and preservation review, including its repair closure, is recorded in [country research](../../research/andorra-2026/research.md). This remains a source-cited draft without licensed-accountant attestation. Only the 18,564.01 to 18,824.04 band of the 2026 dependant-income test remains open, as stated below.

Not yet confirmed: The old share-gain 50% relief for five-to-ten-year holdings is not established by current article 5(k); use its actual ownership/holding exemption instead. The 2026 dependant-income test is settled except for annual income between 18,564.01 and 18,824.04: the Govern has not yet said whether 2026 uses months in force (18,564.00) or the rate in force at accrual × 12 (18,824.04). That band waits for the Govern's 2026 IRPF guide or a binding consultation from the Departament de Tributs i de Fronteres; do not claim the family reduction in that band on a guess. Where the taxpayer dies during 2026, the period ends at death (arts. 40(2) and 41) and the annual figure for that shorter period is not settled either. The old fixed 12.45/m² affordable-rent qualification, the separate immigration/deposit and wealth/other-property-tax claims, including the old fixed 50,000 deposit statement, are not established here. Verify the actual regulated affordable-home classification before article 38 bis relief. The old criminal-fraud claims (EUR 75,000/EUR 150,000 plus 5% tests, three-month-to-three-year or one-to-five-year imprisonment, one-to-four-times fines and automatic voluntary-regularisation immunity) have not been verified against the current Criminal Code and are not applied. Blanket absence of inheritance/gift/wealth/branch-remittance tax and no-filing claims are not established by this IRPF scope. The legacy simplified-IGI EUR 100,000 threshold is outside the ordinary IGI method and requires its actual special-regime conditions. Historic dividend and optional special-regime transitions, and case-specific treaty results are outside the ordinary computations. The ordinary CASS pension contribution-history reduction is supplied above. Article 5(r)'s closing reference to two years does not reconcile its stated four-year habitual-home condition; follow the actual prior approval and obtain clarification for a disputed period. No blanket no-filing or no-tax conclusion is made for those separate regimes.

[law]: https://www.portaljuridicandorra.ad/L2014005
[reg]: https://www.portaljuridicandorra.ad/R20231229D
[cit]: https://www.portaljuridicandorra.ad/L2010095
[general]: https://www.portaljuridicandorra.ad/L2014021
[budget]: https://www.portaljuridicandorra.ad/L2026001
[housing]: https://www.portaljuridicandorra.ad/L2025005
[smi1]: https://www.cass.ad/sites/default/files/arxius/Circular%20informativa%20Salari%20m%C3%ADnim%202026.pdf
[smi7]: https://www.cass.ad/sites/default/files/arxius/Circular%20informativa%20salari%20m%C3%ADnim%20a%20partir%20de%20l%271%20de%20juliol%20del%202026_0.pdf
[g25]: https://www.govern.ad/documents/d/guest/guia_irpf
[g24]: https://www.govern.ad/documents/d/guest/Guia_IRPF_2024

> Contributed by Michael Cutajar.

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
