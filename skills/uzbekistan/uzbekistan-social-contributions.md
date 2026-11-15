---
name: uzbekistan-social-contributions
description: "Uzbekistan 2026 employer social-tax category, contribution-base, INPS and individual-contribution eligibility working papers. Trigger on ijtimoiy soliq, budget organisations, foreign staff, incentive rates, INPS and Soliq contributions. Detailed net pay is owned by uzbekistan-payroll."
version: 0.3
jurisdiction: UZ
tax_year: 2026
last_updated: 2026-11-15
checked_on: 2026-11-14
type: computation
depends_on:
  - social-contributions-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
---

# Uzbekistan social contributions v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Determines employer social-tax and INPS obligations, special cohorts and 408 individual contributions; `uzbekistan-payroll` owns integrated salary net pay and withholding register. Republic of Uzbekistan (Oʻzbekiston, Central Asia), UZ, UZS (Uzbek soʻm). Calendar 2026. These distinct jobs retain both existing slugs. This is an estimated working-paper method for review, not a live filing agent.

Quick answer: ordinary PIT 12%, employer social 12% or proven special category; INPS 0.1% and the 2026 social-insurance 0.2-point allocation are inside PIT. Do not use those headline rates without checking the conditions below.

## Ask the client first

1. Employer STIR/INN, legal status, budget/special-category proof, work and residence locations, foreign-personnel contracts and claimed incentive cohort/window.
2. Reporting month, actual pay date, gross cash/noncash salary, advances, bonus and leave pay, reimbursements, deductions and employer-funded benefits; currency conversion evidence where relevant.
3. Each worker's employment/civil-contract/IE status, tax residence and treaty evidence, Uzbek citizenship/permanent residence and INPS account; do not equate immigration and tax tests.
4. Documented 378/380 exemptions or relief and dates, vocational-training proof, disability category, poor-family eligibility and minimum-wage threshold evidence.
5. Prior employer certificate, year-to-date income/tax, prior Soliq reports/receipts, payment ledger and existing INPS allocations. Bank-only records and net-only salaries do not establish these inputs.

## The method, step by step

### Rates, bases and effective periods

| Item | Rate, base and conditions for 2026 | Official source |
|---|---|---|
| Resident employment PIT |12% of taxable employment income; apply documented exclusions/relief before the rate; special regimes can override | Tax Code 381,378,380,483, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Nonresident employment PIT |12% on Uzbek-source employment/civil-contract income and other income outside the specified investment/freight rows; treaty/source analysis first | Tax Code 382, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Commercial employer social tax |12% of the separate employment-cost base; not an employee deduction | Tax Code 403–405,407, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Budget employer |25%; budget status must be established, not inferred from state ownership alone | Tax Code 405, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| SOS Children's Villages of Uzbekistan |7% for the specifically named association | Tax Code 405, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Disability-workshop limb |4.7% for taxpayers using disabled persons' labour in specialised workshops, sections and enterprises; not every employer hiring a disabled person | Tax Code 405, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Mandatory INPS |0.1% of PIT-taxable income where funded-pension participation applies; allocated from calculated PIT, not added to employee deductions | PP 4086 para 5, https://lex.uz/docs/-4131684; Funded Pension Law 4,6,10, https://lex.uz/docs/-390573 |
| State social-insurance financing from 2026 |0.2 percentage points of PIT allocated to the State Social Insurance Fund; excludes declared rental PIT and source-withheld dividend/interest PIT; not an extra deduction | PP 388 para 5, https://lex.uz/docs/-7959569 |
| Minimum wage,1 Jan–31 Aug 2026 |UZS 1,271,000/month; historical commencement 1 August 2025 | PF 91 para 3(b), https://lex.uz/docs/-7553322 |
| BCV/BHM,1 Jan–31 Aug 2026 |UZS 412,000; a different measure from minimum wage | PF 91 para 3(b), https://lex.uz/docs/-7553322 |
| Minimum wage,from 1 Sep 2026 |UZS 1,360,000/month | PF 115 para 3(b), https://lex.uz/docs/-8283656 |
| BCV/BHM,from 1 Sep 2026 |UZS 440,000 | PF 115 para 3(b), https://lex.uz/docs/-8283656 |

Select the rate for each legally eligible base/employee cohort. Do not add category rates or assume every employee gets one organisation-wide incentive. The numerical amounts above are statutory numerals; multipliers below are derived arithmetic.

### Establish each base before applying rates

Employment income includes salary, incentives/bonus, compensation, nonworked-time pay and specified civil-contract work and board payments under 371. Keep gross cash and noncash components; identify legal exemptions under 378 and documented 380 relief before PIT. Social-tax base follows 371 employment costs under 404, not simply the PIT-taxable amount.403 excludes specified employment-injury compensation, seasonal cotton-harvest wages and qualifying Mahalla Service wages. Foreign-personnel supply and diplomatic postings have separate 404 bases. Sources: Tax Code 371,378,403–404, https://lex.uz/docs/4674902?ONDATE=21.10.2026.

### Restricted personal relief and residence

Article 380 does not grant a universal allowance or a 1×BCV deduction. For eligible categories it exempts monthly income equal to 1.41×minimum wage; clause 3(childhood disability or disability groups I/II, except specified Chernobyl cases) uses 3×minimum wage. Other categories are statutory heroes/decorated persons, war-disabled/veterans/equivalents, specified parents/unremarried surviving spouses of fallen service personnel, single mothers with at least 2 children under 16, qualifying widows/widowers with at least 2 children under 16 and no survivor pension, and one parent caring for a co-resident person disabled from childhood. Obtain the specific certificate/evidence. Apply one selected benefit where several grounds exist, from entitlement, normally at the main workplace; notify loss within 15 days. Source: Tax Code 380, https://lex.uz/docs/4674902?ONDATE=21.10.2026.

Tax residence under 30 normally requires MORE THAN 183 days in the relevant consecutive 12-month window beginning/ending in the tax year, not 183+. The separate under 183 days/more-than-any-other-country test, early application with long-term contract, short treatment/study absence rule and excluded diplomatic/international-organisation periods require full fact analysis; exactly 183 days is not resolved by the shorthand. Cross-border/treaty cases are referred to the income-tax Guide. Source: Tax Code 30, https://lex.uz/docs/4674902?ONDATE=21.10.2026.

### Restricted social-tax incentives

| Eligible facts | Rate and window | Official source |
|---|---|---|
| Poor-family member hired by a business; monthly salary at least 1.5×minimum wage |1% social tax on those employees' wages,1 Jan 2025 until 1 Jan 2028; equality qualifies. From 1 Sep 2026 the wage threshold is derived as 1.5×1,360,000=UZS 2,040,000 | Tax Code 483; PF 115, https://lex.uz/docs/4674902?ONDATE=21.10.2026; https://lex.uz/docs/-8283656 |
| School/college/technical-school student no older than 30, hired for vocational training |1% social tax on qualifying wages AND 1% employee PIT,1 Sep 2024 until 1 Sep 2027; age 30 is included | Tax Code 483, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Cotton-textile clusters; textile and garment/knitwear enterprises |1% social tax,1 Sep 2025 until 1 Sep 2028; establish actual qualifying activity | Tax Code 483, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Modern-packaged fruit/vegetable sellers meeting both conditions |1% social tax,1 May 2025 until 1 Jan 2028; every employee monthly wage at least 2×minimum wage AND qualifying sales at least 50% of total income for reporting/tax period; evidence includes phytosanitary certificate and customs declaration | Tax Code 483, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Legal entity with children's-content creation income at least 80% of annual total income; also the named Children's Content Development Centre |1% social tax,1 Jul 2025 until 1 Jan 2030, not July 2030 | Tax Code 483, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Greenhouse farms with greenhouse-activity income at least 60% of total income in the current reporting/tax period |1% social tax,1 Jan 2026 until 1 Jan 2029 | Tax Code 483, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |

Any overlapping special regime needs its own exact operative instrument before use; these are not generic 1% sectors. Student relief changes employee PIT as well as employer cost, so the ordinary net multiplier is inapplicable to that cohort. Retain employee eligibility documents and separately reconcile the affected wage base.

### Compute and reconcile

1. Identify statutory PIT base and cumulative annual tax. Under 388 compute monthly YTD tax at the applicable rates/relief, less tax already computed for prior months; carry corrections and employer-change certificates. A flat salary case with no relief reduces to monthly base ×12%.
2. Compute eligible INPS as 0.1% of PIT-taxable income and deduct it from PIT remitted, not from net a second time. Confirm Uzbek citizenship/permanent residence and mandatory employment participation under funded-pension law 4/6; non-permanent foreign staff do not automatically have INPS. Distinguish PIT residence.
3. For covered 2026 employment PIT allocate 0.2 percentage points to State Social Insurance Fund under PP 388 para 5. In an ordinary case with the same taxable base, remaining PIT is 12%−0.1%−0.2%=11.7% of that base. This allocation does not change net pay.
4. Net pay=gross−total employee PIT−other proven employee deductions, with separate tax relief and benefit treatment. Ordinary no-relief net=gross×0.88; reverse gross=net÷0.88 only under those conditions.
5. Social tax=separate statutory social base ×applicable rate for each cohort. Employer cost=gross + employer social tax+any additional actual employer-funded benefits/contributions. Simplified multipliers are derived:1.12/1.25/1.047/1.07/1.01 only when base equals gross and the corresponding 12/25/4.7/7/1% rate legally applies.
6. Reconcile total PIT=INPS+insurance allocation+remaining PIT and salary/net/advances to the bank. Total cash remittances across all recipients=PIT+social tax; do not describe the whole PIT as one budget transfer. Do not offset VAT supplies with payroll tax.

Sources: Tax Code 388,403–407, https://lex.uz/docs/4674902?ONDATE=21.10.2026; PP 4086 para 5, https://lex.uz/docs/-4131684; funded-pension law 10, https://lex.uz/docs/-390573; PP 388 para 5, https://lex.uz/docs/-7959569.

### Individual contributions are a different 408 job

IEs pay at least 1 BCV per month regardless of days worked; registered family-business member 1 BCV/month, other adult family members 50% BCV/month; family members under 18 are excluded from this family-business requirement. New registrations start payment from the following month; monthly due date 15th of activity month. Self-employed and the other voluntary 408(2) groups can pay at least 1 BCV annually for pension service.408(3) mandatory annual groups include Hunarmand artisans, Usta-shogird pupils until 25, dehkan heads and IE employees; the IE bears its employees' payment obligation. Annual 408(2)/(3) payments by 31 December use BCV on payment date. Pension-age/disability I–II cases have specified exemption/at-least 50%-minimum rules, subject to evidence; Hunarmand old-age pension/benefit recipients are exempt. Voluntary higher payment and notified suspension/employee-card conditions must be checked under 408, not guessed. Record surname/name/patronymic, ID and period per individual in the payment instruction. Source: Tax Code 408, https://lex.uz/docs/4674902?ONDATE=21.10.2026.

### Working paper and bank classification

Record period/payment date, employer STIR/INN and category proof, employee status, gross, each taxable base, rate, YTD tax and prior tax, INPS, insurance allocation, remaining PIT, net, social tax, total cost and remittances. Label estimates and unresolved flags. A spreadsheet may use B3 gross; B5 PIT; B6 INPS; B7 remaining PIT; add a separate insurance allocation row in 2026; B8 net; B9 social tax; B10 gross+B9; B11 PIT+B9. ROUND(...,2) was an old illustration, not a verified legal rounding rule. Gross-up estimates and ratios identify questions, never determine employer status.

The following legacy narrative keys and banks are retained as a recognition vocabulary, not a verified bank export schema or automatic tax classifier. Read actual direction, counterparty, period, payment reference, payroll register and acceptance ledger before assigning tax. Refunds/reversals need reconciliation; a tax remittance is not necessarily an outgoing amount.

```text
#### Legacy vocabulary: Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to social tax, PIT and pension. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Social tax and PIT remittances always EXCLUDE from any VAT return; they are statutory payroll obligations, not business supplies. Uzbek statements may be in Uzbek (Latin or Cyrillic) or Russian  -  both forms are listed.

#### Legacy vocabulary: 3.1 Employer social tax remittances

**Employer social tax remittances patterns**

Historical table row: Pattern ; Treatment ; Notes
Historical table row: --- ; --- ; ---
Historical table row: IJTIMOIY SOLIQ, IZHTIMOIY SOLIQ ; EXCLUDE -- employer social tax ; "Social tax" in Uzbek
Historical table row: СОЦИАЛЬНЫЙ НАЛОГ, СОЦНАЛОГ ; EXCLUDE -- employer social tax ; "Social tax" in Russian
Historical table row: SOCIAL TAX, SOC TAX ; EXCLUDE -- employer social tax ; English reference
Historical table row: SOLIQ QO'MITASI, GNK, ГНК ; EXCLUDE -- tax authority remittance ; State Tax Committee

#### Legacy vocabulary: 3.2 PIT (personal income tax) withholding remittances

**PIT withholding remittance patterns**

Historical table row: Pattern ; Treatment ; Notes
Historical table row: --- ; --- ; ---
Historical table row: JISMONIY SHAXSLAR DAROMAD SOLIG'I ; EXCLUDE -- PIT withholding ; "Personal income tax" in Uzbek
Historical table row: НДФЛ, НАЛОГ НА ДОХОДЫ ФИЗ ЛИЦ ; EXCLUDE -- PIT withholding ; PIT in Russian
Historical table row: PIT, INCOME TAX WITHHELD ; EXCLUDE -- PIT withholding ; English reference

#### Legacy vocabulary: 3.3 INPS / pension fund transfers

**INPS / pension fund transfer patterns**

Historical table row: Pattern ; Treatment ; Notes
Historical table row: --- ; --- ; ---
Historical table row: INPS, JAMG'ARMA PENSIYA ; EXCLUDE -- pension allocation ; Individual accumulated pension  -  funded from within PIT
Historical table row: ПЕНСИОННЫЙ ФОНД, ПЕНСИЯ ; EXCLUDE -- pension fund ; Russian reference

#### Legacy vocabulary: 3.4 Salary and payroll (exclude from social-tax classification)

**Salary and payroll patterns**

Historical table row: Pattern ; Treatment ; Notes
Historical table row: --- ; --- ; ---
Historical table row: OYLIK, ISH HAQI (outgoing) ; EXCLUDE -- payroll/wages expense ; Net salary to employees
Historical table row: ЗАРПЛАТА, ОКЛАД (outgoing) ; EXCLUDE -- payroll expense ; Russian reference
Historical table row: OYLIK, ЗАРПЛАТА (incoming) ; EXCLUDE -- employment income received ; Not a contribution payment

#### Legacy vocabulary: 3.5 Other tax payments (NOT social tax -- do not confuse)

**Other tax payment patterns**

Historical table row: Pattern ; Treatment ; Notes
Historical table row: --- ; --- ; ---
Historical table row: QQS, НДС, VAT ; EXCLUDE -- VAT, not social tax ; 12% VAT remittance
Historical table row: FOYDA SOLIG'I, НАЛОГ НА ПРИБЫЛЬ ; EXCLUDE -- corporate income tax ; CIT, not social tax
Historical table row: AYLANMA SOLIG'I, turnover tax ; EXCLUDE -- turnover tax ; Simplified regime, not social tax


#### Legacy vocabulary: Section 8 -- Bank statement reading guide

#### Legacy vocabulary: How social tax, PIT and pension remittances appear on Uzbek bank statements

Uzbek statements may be in Uzbek (Latin or Cyrillic) or Russian. Common banks: National Bank of Uzbekistan (NBU), Ipoteka Bank, Asaka Bank, Kapitalbank, Hamkorbank, Agrobank, Uzpromstroybank (SQB).

**Employer social tax:**
- Description: "IJTIMOIY SOLIQ", "СОЦИАЛЬНЫЙ НАЛОГ", "SOCIAL TAX", or to "SOLIQ QO'MITASI / ГНК"
- Timing: monthly, on or before the 15th of the following month
- Amount: employer rate (usually 12%) × gross payroll for the month

**PIT withholding:**
- Description: "JISMONIY SHAXSLAR DAROMAD SOLIG'I", "НДФЛ", "PIT"
- Timing: same monthly cycle, by the 15th
- Amount: 12% of monthly gross payroll (cumulative method)

**INPS / pension:**
- Description: "INPS", "JAMG'ARMA PENSIYA", "ПЕНСИОННЫЙ ФОНД"
- Note: the 0.1% is funded from within the PIT  -  it may appear as a sub-allocation, not a separate extra debit

**Key identification tips:**
1. Social tax and PIT remittances are always outgoing (DEBIT) to the tax authority.
2. They recur monthly with amounts proportional to payroll.
3. Do NOT confuse social tax with QQS/НДС (VAT 12%), FOYDA SOLIG'I (CIT 15%), or AYLANMA SOLIG'I (turnover tax).
4. Do NOT treat the 0.1% INPS as an additional 0.1% debit on top of the 12% PIT  -  it is inside the 12%.
5. Net salary debits (OYLIK / ЗАРПЛАТА) are payroll expense, not contribution remittances.

```

Bank-only onboarding: request payroll registers, category/status certificates and prior accepted reports; identify candidate tax/salary/INPS lines, reconcile them to recipients and periods, then reconstruct gross only as a scenario. Unknown worker type/category or missing certificates block finalisation.

## Boundary and exception table

| Situation | Required treatment |
|---|---|
| Missing employer category or incentive proof | Hold final computation. A12% scenario may be an estimate, never proof of category; do not infer budget status from a bank debit ratio |
| Foreign employee | Determine work location, tax residence, treaty, legal employer and permanent-residence status separately. INPS eligibility is not decided by 183-day tax residence alone |
| Very high or below-minimum salary | Use the actual statutory base under 403–404. The old universal minimum-wage social-tax floor is not established by those articles; do not invent a ceiling or substitute BCV |
| Foreign-personnel supply contract | Base is supplied personnel income but at least 90% of total contract costs under 404; ordinary local payroll is a different case |
| Tax-exempt income or restricted PIT relief | PIT base and social-tax base may differ. An employee PIT exemption is not automatically employer social-tax exemption |
| Advance, bonus, leave pay, benefit or reimbursement | Reconcile the legal character and accrual/payment dates; bank narration alone cannot determine its tax treatment |
| IE/self-employed or family business | Separate 408 contribution rules from ordinary employer percentage payroll. Their turnover/income tax goes to uzbekistan-income-tax |
| Non-employment investment/freight payment | Outside salary computation.381 resident dividends/interest 5%;382 nonresident dividends/interest 10%, international freight 6%, subject to specific exemption/treaty; do not call these salary rates: https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Annual or departure return | Employer withholding does not replace a required individual declaration; refer 397–398 and the income-tax Guide |

## Worked cases

A hypothetical qualifying poor-family employee earns exactly 1.5×November 2026 minimum wage=2,040,000. The inclusive boundary qualifies for social 1% if every other statutory condition is documented:20,400 social versus 244,800 ordinary. This is a decision on evidence, not a default rate selection. OrdinaryPIT remains 12% in this case.

```oa-check
name: Exact poor-family wage boundary and eligibility decision
inputs:
  minimum_wage: 1360000
  gross: 2040000
steps:
  - threshold: minimum_wage * 1.5
  - boundary_difference: gross - threshold
  - qualifying_social: gross * 0.01
  - ordinary_social: gross * 0.12
  - qualifying_cost: gross + qualifying_social
  - ordinary_cost: gross + ordinary_social
  - saving: ordinary_cost - qualifying_cost
expected:
  threshold: 2040000
  boundary_difference: 0
  qualifying_social: 20400
  ordinary_social: 244800
  qualifying_cost: 2060400
  ordinary_cost: 2284800
  saving: 224400
```

Foreign-personnel supply scenario: total contract cost 100,000,000, personnel income 60,000,000.404 requires a90,000,000 base; standard 12% social is 10,800,000, not 7,200,000. This floor belongs to personnel supply, not every employee's minimum wage.

```oa-check
name: Foreign personnel contract statutory 90 percent base floor
inputs:
  contract_cost: 100000000
  personnel_income: 60000000
steps:
  - minimum_base: contract_cost * 0.90
  - base: max(personnel_income, minimum_base)
  - social: base * 0.12
  - wrong_income_only: personnel_income * 0.12
  - difference: social - wrong_income_only
expected:
  minimum_base: 90000000
  base: 90000000
  social: 10800000
  wrong_income_only: 7200000
  difference: 3600000
```

### Historical case archive: original payloads, not current authority

Every original case below is retained in full. These are historical test inputs and old explanatory text, not current verified law or validated bank-file formats. The current method above controls. In 2026 ordinary PIT budget-only amounts must also subtract the 0.2-point insurance allocation;1,271,000 is the historical minimum from 1 Aug 2025 through 31 Aug 2026, not the current minimum; claimed 1% requires evidence and student PIT can also change. A debit 600,000 described as total PIT needs recipient-level reconciliation:5,000 INPS plus 595,000 remaining 2025 PIT were not automatically one budget transfer. Dates and amounts below remain unchanged; old period-specific legal claims are quarantined.

```text
## Section 4 -- Worked examples

Six bank-statement / payroll classifications for a hypothetical private (non-budget) Uzbek company employing resident staff. All figures in UZS. Employer social tax rate = 12% unless stated. PIT = 12% flat; INPS 0.1% is carved out of the PIT (no extra deduction).

### Example 1 -- Standard resident employee, gross UZS 5,000,000/month (private employer)

**Input line:**
`31.01.2025 ; OYLIK YANVAR ; DEBIT ; NET SALARY ; -4,400,000 ; UZS`

**Reasoning:**
Gross UZS 5,000,000. PIT = 12% × 5,000,000 = UZS 600,000. INPS = 0.1% × 5,000,000 = UZS 5,000, taken FROM WITHIN the 600,000 PIT (no extra deduction). Net pay = 5,000,000 − 600,000 = UZS 4,400,000. Separately, employer social tax = 12% × 5,000,000 = UZS 600,000 (employer cost, not deducted from the employee). Total employer cost = 5,000,000 + 600,000 = UZS 5,600,000.

**Classification:** Net salary debit EXCLUDE from VAT (payroll expense). PIT UZS 600,000 and social tax UZS 600,000 remitted to Soliq by 15 Feb 2025.

### Example 2 -- PIT withholding remittance (private employer)

**Input line:**
`14.02.2025 ; NDFL YANVAR ; DEBIT ; JISMONIY SHAXSLAR DAROMAD SOLIG'I ; -600,000 ; UZS`

**Reasoning:**
Matches PIT pattern (3.2). UZS 600,000 = 12% PIT on the UZS 5,000,000 gross from Example 1, withheld and remitted by the employer. Of this, UZS 5,000 (0.1%) is credited to the employee's INPS account; the remainder UZS 595,000 is general budget PIT. Paid before the 15 Feb deadline.

**Classification:** EXCLUDE from VAT. PIT withholding remittance.

### Example 3 -- Employer social tax remittance (private employer, 12%)

**Input line:**
`14.02.2025 ; IJTIMOIY SOLIQ YANVAR ; DEBIT ; SOCIAL TAX ; -600,000 ; UZS`

**Reasoning:**
Matches social tax pattern (3.1). UZS 600,000 = 12% × UZS 5,000,000 gross payroll. This is an employer cost, not withheld from the employee. Reported and paid monthly by the 15th.

**Classification:** EXCLUDE from VAT. Employer social tax (deductible business expense).

### Example 4 -- Budget (state-funded) organisation, gross UZS 4,000,000/month (25% social tax)

**Input line:**
`14.04.2025 ; СОЦНАЛОГ МАРТ ; DEBIT ; СОЦИАЛЬНЫЙ НАЛОГ ; -1,000,000 ; UZS`

**Reasoning:**
Budget organisation → social tax rate 25% (PwC). Gross UZS 4,000,000. Employer social tax = 25% × 4,000,000 = UZS 1,000,000. PIT on the employee = 12% × 4,000,000 = UZS 480,000; net pay = 4,000,000 − 480,000 = UZS 3,520,000. Total employer cost = 4,000,000 + 1,000,000 = UZS 5,000,000.

**Classification:** EXCLUDE from VAT. Budget-organisation social tax at 25%.

### Example 5 -- Cumulative year-to-date PIT (March remittance)

**Input lines (payroll YTD):**
`Jan–Feb cumulative gross: 10,000,000 ; Jan–Mar cumulative gross: 15,000,000 ; UZS`

**Reasoning:**
PIT is withheld cumulatively (LegalAct.uz): monthly PIT = YTD PIT to current month − YTD PIT to prior month. YTD PIT to March = 12% × 15,000,000 = UZS 1,800,000. YTD PIT to February = 12% × 10,000,000 = UZS 1,200,000. March PIT = 1,800,000 − 1,200,000 = UZS 600,000. (Here income is level UZS 5,000,000/month, so the cumulative method reconciles to a flat 12% per month.)

**Classification:** EXCLUDE from VAT. March PIT remittance UZS 600,000, due 15 Apr 2025.

### Example 6 -- Organisation employing persons with disabilities (4.7%), gross UZS 3,000,000/month

**Input line:**
`14.05.2025 ; IJTIMOIY SOLIQ APREL ; DEBIT ; SOCIAL TAX ; -141,000 ; UZS`

**Reasoning:**
Organisation employing persons with disabilities → social tax rate 4.7% (PwC). Gross UZS 3,000,000. Employer social tax = 4.7% × 3,000,000 = UZS 141,000. PIT on the employee = 12% × 3,000,000 = UZS 360,000; net pay = 3,000,000 − 360,000 = UZS 2,640,000.

**Classification:** EXCLUDE from VAT. Reduced 4.7% social tax. Confirm the organisation qualifies before applying the reduced rate (R-UZ-ST-2 logic).


### Computation examples (private employer, 12% social tax, resident employee)

**Computation examples table**  _(PwC; LegalAct.uz; WageCentre)_

Historical table row: Gross/month (UZS) ; PIT 12% (UZS) ; of which INPS 0.1% (UZS) ; Net pay (UZS) ; Employer social tax 12% (UZS) ; Total employer cost (UZS)
Historical table row: --- ; --- ; --- ; --- ; --- ; ---
Historical table row: 1,271,000 (min wage) ; 152,520 ; 1,271 ; 1,118,480 ; 152,520 ; 1,423,520
Historical table row: 3,000,000 ; 360,000 ; 3,000 ; 2,640,000 ; 360,000 ; 3,360,000
Historical table row: 5,000,000 ; 600,000 ; 5,000 ; 4,400,000 ; 600,000 ; 5,600,000
Historical table row: 10,000,000 ; 1,200,000 ; 10,000 ; 8,800,000 ; 1,200,000 ; 11,200,000

*All derived from the flat 12% PIT and 12% employer social tax (PwC); INPS 0.1% carve-out per LegalAct.uz. Minimum wage UZS 1,271,000 from 1 Aug 2025 (WageCentre).*

### Other employer categories (social tax on gross UZS 4,000,000)

**Other employer categories table**  _(PwC; EY)_

Historical table row: Category ; Rate ; Social tax (UZS) ; Source
Historical table row: --- ; --- ; --- ; ---
Historical table row: Private / other taxpayers ; 12% ; 480,000 ; PwC
Historical table row: Budget organisation ; 25% ; 1,000,000 ; PwC
Historical table row: SOS Children's Villages ; 7% ; 280,000 ; PwC
Historical table row: Disability-employing org ; 4.7% ; 188,000 ; PwC
Historical table row: Incentive (qualifying, time-limited) ; 1% ; 40,000 ; EY


### Test suite

**Test 1:** Private employer, resident, gross UZS 5,000,000. → PIT = 600,000; net pay = 4,400,000; employer social tax (12%) = 600,000; total employer cost = 5,600,000.

**Test 2:** Private employer, resident, gross UZS 10,000,000. → PIT = 1,200,000; net pay = 8,800,000; employer social tax (12%) = 1,200,000; total employer cost = 11,200,000.

**Test 3:** Budget organisation, resident, gross UZS 4,000,000. → PIT = 480,000; net pay = 3,520,000; employer social tax (25%) = 1,000,000; total employer cost = 5,000,000.

**Test 4:** Disability-employing organisation, gross UZS 3,000,000. → PIT = 360,000; net pay = 2,640,000; employer social tax (4.7%) = 141,000.

**Test 5:** SOS Children's Villages, gross UZS 4,000,000. → employer social tax (7%) = 280,000.

**Test 6:** Minimum-wage employee, gross UZS 1,271,000 (private). → PIT = 152,520; net pay = 1,118,480; employer social tax (12%) = 152,520; total employer cost = 1,423,520.

**Test 7:** Cumulative PIT  -  YTD gross to March 15,000,000, YTD gross to Feb 10,000,000. → YTD PIT to Mar = 1,800,000; YTD PIT to Feb = 1,200,000; March PIT = 600,000.

**Test 8:** INPS treatment  -  gross UZS 5,000,000. → Total employee deduction = 12% = 600,000 (NOT 12.1%); INPS 5,000 is inside the 600,000, not on top.

**Test 9:** Foreign employee without residence permit, gross UZS 8,000,000 (private). → PIT 12% = 960,000 still applies; INPS carve-out generally does not (flag T2-3); employer social tax (12%) = 960,000.

```

## When to refuse or refer

Stop for another jurisdiction (including Kazakhstan KZT, Azerbaijan AZN or Tajikistan TJS), missing gross/pay period/payment date, unknown employer category, unproved special relief, worker-type uncertainty or an unresolved base difference. Net-only gross-up is a labelled scenario: net÷0.88 only if ordinary 12% PIT, no relief and no other deductions. It is not a verified gross or filing position.

Retain the old social refusal IDs: R-UZ-ST-1 unknown category; R-UZ-ST-2 incentive qualification/window; R-UZ-ST-3 floor/ceiling request without applicable legal basis; R-UZ-ST-4 arrears/fines without rates and dates; R-UZ-ST-5 nonresident/cross-border work. Each requires a qualified Uzbek tax professional before finalising. Income changing to IE turnover, dividends, interest, freight or other non-employment income goes to the relevant income-tax work, not a salary formula. Do not use Venezuela-derived INCES, INPS 4%,0.5% unemployment or Housing Loan Regime text for Uzbekistan.

Never add INPS or the 0.2-point financing allocation on top of PIT; never deduct employer social tax from net salary; never apply ordinary 12% PIT to an evidenced special 1% student case; never apply a BCV-based personal allowance; never apply a sector incentive without its conditions; never present estimates as definitive. Sickness/maternity benefits, insurance eligibility and benefit calculations are a separate job: the 2026 reform cannot be reduced to the old assertion that there is no other social-insurance mechanism. Refer those benefit computations and voluntary-insurance elections; only the statutory PIT financing allocation is computed here.

## Filing and payment

For tax filing, payment and notice deadlines expressed in days, count working days unless the provision expressly says calendar days; counting starts on the day after the triggering date or event. If the last day of such a deadline falls on a statutory rest day or nonworking holiday, the following working day is the endpoint. Apply these deadline-counting rules to the 5-day and 15-day deadlines here; article 110 late interest expressly uses calendar days. Source: Tax Code 5,110, https://lex.uz/docs/4674902?ONDATE=21.10.2026.

Keep a payroll tax register per 388 identifying the employee, income type, exemptions, accrual/payment dates, status, tax withheld and remitted. When an employee changes their main job, obtain the prior employer income/withholding certificate before the first new payroll. Without it/required ID, withhold without the specified relief; recalculate after evidence arrives. This replaces the old assumption that a bank-statement gross-up establishes the annual base. Source: Tax Code 388, https://lex.uz/docs/4674902?ONDATE=21.10.2026.

| Obligation | Timing and conditions | Official source |
|---|---|---|
| PIT report |Monthly by 15th of following month; annual result by 15 February following year. Applicable branch reporting follows 389, including the more-than 25-worker branch rule | Tax Code 389, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| PIT payment |At the time income is paid, no later than the reporting deadline; in-kind income tax within 5 days after month-end | Tax Code 390, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Social-tax report/payment |Monthly report by 15th of following month; annual result by 15 February; monthly payment no later than reporting deadline | Tax Code 406–407, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Prepopulated 2026 reporting |Tax authority forms PIT/social reports using its records and personal-account inputs. Correct differences within 5 days, no later than the filing deadline; absence of a timely correction signifies acceptance. This is not an extra 5-day extension | Tax Code 81, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |
| Individual declaration, when required |File by 1 April following year; ordinary resident balance by 1 June. Applicable foreign-person departure declaration is due 1 month before departure, and tax within 15 days after filing; the before-1-February exception is held for review because the Uzbek original and Russian translation differ on residence status | Tax Code 393,397–398, https://lex.uz/docs/4674902?ONDATE=21.10.2026 |

Use the client's existing Soliq personal account (my.soliq.uz) and approved current PIT/social-tax calculation, reconcile prepopulated figures to the register, correct discrepancies, obtain the accepted-report receipt, then reconcile payment allocations to the tax ledger and INPS individual accounts at Xalq banki (People's Bank). The live account/form-field map and separate INPS transfer channel/due-date details were not inspected: unattended submission is held. Do not invent a form code, box number, electronic signature path or new account-registration procedure.

Late-payment interest under 110 is the unpaid tax ×the Central Bank refinancing rate applicable to each period ÷300 for each late calendar day from the day after the statutory due date, subject to statutory exclusions (including specified collection restraints, qualifying written-authority guidance and enforcement-register cases). It also applies to tax agents. Obtain the actual rate/date history; no current numeric Central Bank rate is supplied here. Missing withholding can make the agent liable for the unpaid tax and interest under 386. Fixed fines, late-report grace and limitation claims remain outside usable quantified guidance. Sources: Tax Code 110,386, https://lex.uz/docs/4674902?ONDATE=21.10.2026.

## Completion checklist

- [ ] Place/currency UZ/UZS and reporting 2026 confirmed; historical cases clearly labelled.
- [ ] Gross, PIT base, social-tax base and INPS participation reconciled independently.
- [ ] Rate/category, wage-date, relief and incentive evidence retained; exception cohort separated.
- [ ] Current and prior YTD tax, bank salary, payment dates and accepted reports match.
- [ ] PIT total equals INPS plus State Social Insurance Fund allocation plus remaining PIT; employer social tax separately reconciled.
- [ ] Review flags, missing form mapping, uncertain penalty inputs and cross-border issues held; working paper marked estimated, not reviewed.

## Sources

| Source | URL | Read on | Read for sections |
|---|---|---|---|
| Uzbek-original Tax Code, selected 21 October 2026 revision | https://lex.uz/docs/4674902?ONDATE=21.10.2026 | 2026-11-14 | Read for articles 5;30;81;110;364–365;371;378;380–382;386;388–390;393;397–398;402–408;483 employment incentives; Russian edition cross-check only |
| Mandatory funded-pension law 702-II | https://lex.uz/docs/-390573 | 2026-11-14 | Read for articles 4,6,10–11: citizenship/permanent residence, mandatory/voluntary scope, PIT-funded monthly contributions and Xalq banki |
| PP 4086,26 December 2018 | https://lex.uz/docs/-4131684 | 2026-11-14 | Read for para 5 and neighbours:0.1% taxable-income contribution deducted from PIT |
| PP 388,26 December 2025 | https://lex.uz/docs/-7959569 | 2026-11-14 | Read for paras 4–6:2026 fund allocations,0.2 percentage-point PIT financing and exclusions |
| PF 91,2 June 2025 | https://lex.uz/docs/-7553322 | 2026-11-14 | Read for para 3(b) and neighbours: historical 1 Aug 2025 wage/BCV values |
| PF 115,23 June 2026 | https://lex.uz/docs/-8283656 | 2026-11-14 | Read for para 3(b) and neighbours:1 Sep 2026 wage/BCV changes |

Not yet confirmed: a blanket social-tax minimum-wage floor or universal ceiling; blanket no-other-insurance/no-unemployment/health-contribution assertion; supposed 1×BCV personal deduction (corrected by 380); alleged proposed INPS 2% (excluded); full overriding/overlapping incentive decrees; historical pre-August-2025 minimum wage of UZS 1,155,000; permanent standalone 1% regime for every seller/content producer; historical stock-dividend exemption 1 April 2022–31 December 2028; IE/self-employed 1% turnover up to 1 billion, abolished 100 million threshold and fixed-PIT changes as an executable payroll computation (referred to income-tax); legacy e-commerce 15%/4%, standard CIT 15%/special 20%, VAT 12%, turnover 4% and generic 1 billion thresholds (not contribution guidance); exact bank export schemas/date formats and FX conversion tax-date rule; current form codes/boxes and account navigation, distinct INPS remittance due date/channel, statutory rounding; fixed fines, alleged 5-day late-report grace/prior 3 months rule, single consolidated fine and 3-year assessment limitation; broad 183+residence shorthand and every special residence regime (use 30/treaty analysis); detailed sickness/maternity benefits and voluntary insurance; Tax Code 397 before-1-February departure exception, where Uzbek original says nonresident and Russian translation says resident. Old assertions and raw case payloads below are retained as historical evidence only, never authority for these gaps.

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
