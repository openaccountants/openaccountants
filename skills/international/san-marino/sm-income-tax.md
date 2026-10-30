---
name: sm-income-tax
description: >
  San Marino personal income tax (IGR, imposta generale sui redditi) for individuals in tax year 2026, under Law 166/2013 as reformed by Law 141/2025 and Delegated Decree 156/2026. Covers residence, worldwide and domestic-source scope, the eight progressive bands from 9% to 35%, the 18% separate rate on business and professional income for 2026 to 2030, the employee 7% forfait capped at EUR 2,800, pension forfaits, rental income, family, medical and rent credits, the SMaC card tax credit for wages, pensions and business income, loss relief, foreign tax credit, payroll withholding, the 31 July return deadline and late-filing charges. Use for San Marino income tax, IGR bands, SMaC credit, resident and frontier employee tax, self-employed tax in San Marino and personal return questions. Special residence regimes and mixed-income ordering need their own facts.
jurisdiction: SM
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.3
---

# San Marino personal income tax v0.3

Tax year: calendar year 2026 (1 January to 31 December), return filed in 2027. Currency EUR. Authority: UO Ufficio Tributario (Tax Office), Dipartimento Finanze e Bilancio.

Law 141/2025 rewrote the IGR law (Law 166/2013) with effect from tax year 2026; earlier years keep the old rules ([Law 141/2025, art 54(1)-(2)][l141]). Delegated Decree 156/2026 of 12 October 2026 amended the reformed law again from tax year 2026 ([DD 156/2026, art 19][dd156]). The official coordinated IGR text (updated to 22 December 2025) includes Law 141/2025 but not DD 156/2026, so read both.

## 1. Who this applies to

- **Residents** pay IGR on worldwide income. An individual is resident for the tax year if any one of these holds: (a) registered residence (residenza anagrafica) in San Marino for most of the tax period; (b) actually living in San Marino for most of the tax period; (c) centre of vital interests in San Marino ([IGR art 10(2)][igr]). Article 2 defines the centre of vital interests by economic, property, social and family ties. A plain 183-day count is not the test.
- **Non-residents** pay IGR only on income produced in San Marino as listed in article 5: San Marino land and buildings, specified capital income, employment paid by resident persons, professional work and business carried on through a San Marino permanent establishment ([IGR arts 1, 5][igr]).
- Partnerships (società di persone) and professional associations are not taxpayers: their income is attributed to each partner by profit share whether or not distributed ([IGR art 10(3)-(4)][igr]).
- Where a treaty applies, the domestic rule still applies if it is more favourable ([IGR art 9][igr]). Use `sm-cross-border` for non-resident payments and treaties.

Out of scope here: corporate IGR (`sm-corporate-income-tax`), payroll mechanics and social contributions (`sm-payroll-social`), special residence regimes.

## 2. Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Band 1: taxable income up to 10,000 | 9% | 2026 | [IGR Annex C, art C1(1)][igr] |
| Band 2: 10,000.01 to 18,000 | 13% | 2026 | [IGR Annex C, art C1(1)][igr] |
| Band 3: 18,000.01 to 28,000 | 17% | 2026 | [IGR Annex C, art C1(1)][igr] |
| Band 4: 28,000.01 to 38,000 | 21% | 2026 | [IGR Annex C, art C1(1)][igr] |
| Band 5: 38,000.01 to 50,000 | 25% | 2026 | [IGR Annex C, art C1(1)][igr] |
| Band 6: 50,000.01 to 65,000 | 28% | 2026 | [IGR Annex C, art C1(1)][igr] |
| Band 7: 65,000.01 to 80,000 | 31% | 2026 | [IGR Annex C, art C1(1)][igr] |
| Band 8: over 80,000 | 35% | 2026 | [IGR Annex C, art C1(1)][igr] |
| Band indexation | Every two years by cost of living, capped at 6 points; first adjustment in tax year 2028, none in 2026 | 2026 | [IGR Annex C, art C1(2)][igr] |
| Business and self-employed income (separate taxation, art 13(1)(a)) and directors' end-of-mandate pay (13(1)(l)) | 18% for tax years 2026 to 2030 (statutory rate 17%) | 2026 | [Law 141/2025, art 54(6)][l141]; [IGR art 13(2)(a)][igr] |
| Capital gains (13(1)(b)) and qualifying national-athlete sponsorship (13(1)(o)) | 10% separate | 2026 | [IGR art 13(2)(b)][igr] |
| Arrears and employment termination payments (13(1)(c)) | 2.5% on the first 5,000, 5% above | 2026 | [IGR art 13(2)(c)][igr] |
| Agency and collaboration termination payments, specified public-office pay (13(1)(d)-(f)) | 12% separate | 2026 | [IGR art 13(2)(d)][igr] |
| Optional separate taxation of foreign dividends (13(1)(g)) | 3% of the amount received net of foreign tax | 2026 | [IGR art 13(2)(e), (3)][igr] |
| Optional separate taxation of foreign bond interest and qualifying insurance income (13(1)(h), (m)) | 10% of the amount received net of foreign tax | 2026 | [IGR art 13(2)(f), (3)][igr] |
| Optional separate taxation of interest on foreign bank accounts (13(1)(i)) | 13% of the amount received net of foreign tax | 2026 | [IGR art 13(2)(g), (3)][igr] |
| Optional separate taxation of supplementary pension benefits (13(1)(n)) | 5% | 2026 | [IGR art 13(2)(h)][igr] |
| Employee forfait deduction | 7% of gross employment income, capped at 2,800 | 2026 | [IGR art 24(4)][igr] |
| Employee travel costs paid without receipts | Excluded up to 15 a day (San Marino and Italy) or 30 a day (abroad excluding Italy), if paid by traceable means | 2026 | [IGR art 24(3), replaced by DD 156/2026, art 8][dd156] |
| Pension forfait (marginal slices) | 20% of the first 13,000; 12% of 13,000.01 to 19,500; 9% of 19,500.01 to 26,000; 7% above 26,000 | 2026 | [IGR art 26][igr] |
| Let San Marino home, rent at or below the controlled rent | Income = 20% of rent (never below the cadastral income) | 2026 | [IGR art 22(2)(a), (3)][igr] |
| Let San Marino home, rent above the controlled rent | Income = 60% of rent (never below the cadastral income) | 2026 | [IGR art 22(2)(b), (3)][igr] |
| Let home outside San Marino | Income = 60% of rent | 2026 | [IGR art 22(2-quater), added by DD 156/2026, art 6][dd156] |
| Let business premises, lessor without bookkeeping duty | Income = rent less 25% (never below the cadastral income) | 2026 | [IGR art 23(3)(a), (4)][igr] |
| Own business premises used as the seat of activity (art 23(2)) | Cadastral rent still counts: 100% in 2026, 75% in 2027, 50% in 2028, 25% in 2029 | 2026 | [Law 141/2025, art 54(5)][l141] |
| Family credit: dependent spouse | 250 a year | 2026 | [IGR art 16(1)(a)][igr] |
| Family credit: each dependent child | 250 a year | 2026 | [IGR art 16(1)(b)][igr] |
| Family credit: dependent parents and parents-in-law, other cohabiting dependants, relatives owed maintenance | 125 a year each | 2026 | [IGR art 16(1)(c)-(e)][igr] |
| Family credit uplift | +20% where dependants exceed two, or a dependant is disabled or permanently ill | 2026 | [IGR art 16(7)][igr] |
| Medical and dental credit | 18% of documented, traceably paid costs up to 1,600 per person (taxpayer and each dependant) | 2026 | [IGR art 16(7-bis)(a)][igr] |
| Residential rent credit | 15% of 50% of rent (80% of rent if the tenant is under 35), rent counted up to 6,000 | 2026 | [IGR art 16(7-bis)(b)][igr] |
| SMaC credit, no-documentation portion | Up to 752.40 at taxable income up to 8,360, falling to zero at 16,720 | 2026 | [IGR Annex E, art E3(2) and Table 1][igr] |
| SMaC credit maximum | 1,900 at taxable income of 42,500 and above, on documented SMaC spend up to 10,000 | 2026 | [IGR Annex E, art E3(2) and Table 1][igr] |
| SMaC eligible fuel | Fuel counts only up to 1,500 a year | 2026 | [IGR Annex E, art E1(1)(a)][igr] |
| SMaC home utilities and insurance (residents) | Count up to 1,000 at taxable income up to 15,000, tapering to nil at 50,000 | 2026 | [IGR Annex E, art E1(2)][igr] |
| Business SMaC credit (separately taxed income) | 18% of spend up to 5,000 (income up to 25,000); cap 900 (25,000 to 50,000); 9% of spend up to 10,000 (over 50,000) | 2026 | [IGR art 17(1-ter)][igr] |
| Business and self-employed loss carryforward | No time limit; use capped at 70% of taxable business income each year | 2026 | [IGR art 30(4), replaced by DD 156/2026, art 10][dd156] |
| Return and balance payment deadline | 31 July following the tax year (31 July 2027 for 2026) | 2026 | [IGR arts 93(1), 124(1)][igr] |
| Employer income certification (IGR G) | Transmitted by 15 April | 2026 | [IGR art 85(2)][igr] |

### SMaC credit table (Annex E, Table 1)

The credit is limited to tax due and can be claimed in part. Between rows, the credit and the spend limit are interpolated on actual taxable income; the credit percentage (credit divided by the spend limit) is rounded down to two decimals ([IGR Annex E, art E3][igr]).

| Taxable income up to | Total maximum credit | No-SMaC portion | Documented SMaC portion | SMaC spend limit |
|---:|---:|---:|---:|---:|
| 8,360 | 752.40 | 752.40 | 0 | 0 |
| 10,450 | 925.00 | 564.30 | 360.70 | 500 to 1,125 |
| 12,540 | 1,000.00 | 376.20 | 623.80 | 1,750 |
| 14,630 | 1,075.00 | 188.10 | 886.90 | 2,375 |
| 16,720 | 1,150.00 | 0 | 1,150.00 | 3,000 |
| 20,900 | 1,300.00 | 0 | 1,300.00 | 4,250 |
| 25,080 | 1,450.00 | 0 | 1,450.00 | 5,500 |
| 29,260 | 1,600.00 | 0 | 1,600.00 | 6,750 |
| 33,440 | 1,700.00 | 0 | 1,700.00 | 8,000 |
| 37,970 | 1,800.00 | 0 | 1,800.00 | 9,250 |
| 42,500 and above | 1,900.00 | 0 | 1,900.00 | 10,000 |

## 3. The base

### Separate the baskets first

The ordinary progressive base is total income less deductible charges, excluding income taxed separately, income under final withholding and exempt income ([IGR art 12(1)][igr]). Non-residents' base is their article 5 San Marino-source income only ([IGR art 12(2)][igr]). Income of cohabiting minor children (other than their work income) is attributed to the parent ([IGR art 12(3)][igr]).

Article 13 income is taxed separately at the section 2 rates: business and self-employed income (net of article 14 deductible charges and compulsory social contributions), capital gains, arrears and termination payments, and the optional foreign dividend, interest and pension routes. The foreign dividend and foreign interest routes apply only if the taxpayer opts in; foreign capital gains and arrears can be taxed progressively instead, on election ([IGR art 13(1), (5)][igr]).

Where a person has separately taxed business or self-employed income plus other income, the other income is taxed at the bands that apply after stacking it on top of the business income ([IGR art 17(1-bis)][igr]).

### Employment income

Taxable employment income = gross cash and benefits (articles 24 and 25) less compulsory employee social contributions less the 7% forfait capped at 2,800 ([IGR art 24(4)][igr]). Compute the 7% on gross pay, not on pay already reduced by contributions. The Tax Office's 2026 calculator deducts 9.9% default contributions (pension 6.9%, FONDISS 2.5%, unemployment and solidarity 0.5%) and tells users to remove any component not on the payslip ([Tax Office IGR calculator][calc]). At gross 50,000 the forfait is capped at 2,800 (not 3,500) and taxable wage is 50,000 - 2,800 - 4,950 = 42,250.

Foreign-service allowances count as income at 75%; allowances for foreign trips count above the public-sector daily maximum; a foreign trip allowance and a same-day commuting reimbursement cannot be combined ([IGR art 24(3), (3-ter), replaced and added by DD 156/2026, art 8][dd156]).

### Pensions

Resident pensions are reduced by a marginal forfait: 20% of the first 13,000, 12% of the next 6,500, 9% of the next 6,500 and 7% above 26,000 ([IGR art 26][igr]). Apply each percentage only to its slice.

### Business and self-employed income

Use actual accounts: income, deductible costs, timing, depreciation (Annex D) and related-party normal value ([IGR arts 27-30][igr]). Compulsory social contributions of the self-employed, sole traders and separate-management members are fully deductible from that income ([IGR art 15][igr]). Documented losses carry forward without time limit but can absorb at most 70% of the year's taxable business income ([IGR art 30(4), replaced by DD 156/2026, art 10][dd156]). The 18% separate rate then applies.

### Property

San Marino homes count at their cadastral income; when let, income is 20% or 60% of rent depending on whether the rent is at or above the controlled rent, never less than the cadastral income; homes let to atypical residents count at 100% of rent ([IGR art 22(1)-(3)][igr]). Rent is income of the year the contract covers, whether or not received; a lessor with a documented bad debt can file a corrective return within the assessment period ([IGR art 22(6)][igr]; [DD 156/2026, art 7][dd156]). A let foreign home produces income of 60% of rent ([DD 156/2026, art 6][dd156]). Business premises let by a person without bookkeeping duties produce rent less 25% ([IGR art 23(3)][igr]). For own business premises used as the seat of activity, the cadastral rent is phased out of income: 100% in 2026, 75% in 2027, 50% in 2028, 25% in 2029 ([Law 141/2025, art 54(5)][l141]).

### Deductible charges

Article 14 and Annexes A and B allow listed expenses actually paid and documented for the taxpayer and dependants. DD 156/2026 article 17 changes the Annex A family-care and voluntary-pension conditions ([IGR art 14, Annexes A-B][igr]; [DD 156/2026, art 17][dd156]). A deduction reduces income; a credit reduces tax.

### Family credits

Family credits apply only to fiscal residents and are pro-rated by month ([IGR art 16(4)][igr]). Children count as dependants if minors, or aged up to 26 and in legal study, or permanently unable to work, or registered unemployed and living with the taxpayer ([IGR art 16(2)][igr]). A spouse and the other relatives count only if their own gross income does not exceed the social pension amount (no limit for disabled persons) ([IGR art 16(3)][igr]). The child credit goes to one parent or 50% to each; if claims exceed 100%, each parent gets 50%. The same rule covers guardians named by court decree ([IGR art 16(5), replaced by DD 156/2026, art 3][dd156]). The 20% uplift needs more than two dependants or a disabled dependant; two children alone do not trigger it ([IGR art 16(7)][igr]). If the Tax Office finds a dependant's income over the limit, the credit is lost and the return corrected ([IGR art 16(8)][igr]).

### SMaC credit

The SMaC credit (article 16(8-bis) and Annex E) reduces tax on wages, assimilated income and pensions of residents and non-residents, for purchases made in San Marino with the SMaC card. Residents also get it against other ordinarily taxed income ([IGR art 16(8-bis), (8-ter)][igr]). Excluded spend: fuel over 1,500 a year, utilities and phone, property and casualty insurance, vehicle purchases, and banking and financial services; residents can count home utilities and insurance within the Annex E1(2) cap ([IGR Annex E, art E1(1)-(2)][igr]). Online purchases count only from suppliers with a San Marino seat, branch or permanent establishment ([IGR Annex E, art E1(3)][igr]). Spend by dependants counts, and spend by a cohabiting spouse or non-dependent cohabitants counts above their own limit, up to the taxpayer's limit ([IGR Annex E, art E2][igr]). Resident diplomatic staff at the listed missions and residents with certified 100% disability get the credit without documentation ([IGR art 16(8-quater)][igr]).

For separately taxed business and self-employed income, the SMaC credit comes off the 18% tax instead, at the article 17(1-ter) rates in section 2. Between 25,000 and 50,000 the percentage is 900 divided by (5,000 plus one fifth of income over 25,000), rounded down to four decimals ([IGR art 17(1-ter)][igr]). A person with both business income and wages or pensions elects in the return which SMaC credit to use; both cannot be claimed ([IGR art 17(1-quater), added by DD 156/2026, art 4][dd156]).

### Foreign tax credit

Final, non-refundable foreign tax on foreign income included in the base is credited up to San Marino net tax x (foreign income / total income) ([IGR art 18(1)][igr]). For business or self-employed income the fraction is foreign receipts / total receipts, after admitted losses ([IGR art 18(2)][igr]). Compute per State. An omitted return or undeclared foreign income loses the credit ([IGR art 18(6)][igr]).

## 4. Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Employer and pension payer transmit IGR G income and withholding data | 15 April following the tax year | [IGR art 85(2)][igr] |
| Year-end withholding adjustment on wages | Collected by February of the following year | [IGR art 101(5)][igr] |
| Annual return (electronic, by 24:00) | 31 July following the tax year | [IGR art 93(1), (4)][igr] |
| Balance payment | Same date as the return | [IGR art 124(1)][igr] |
| Business and self-employed advances | 35% by 31 August and 55% by 30 November, on prior-year tax net of foreign business-income credits; not due if the activity is suspended or ceased before the date | [IGR art 124(2)][igr] |

No return is needed by a person with only wages from one employer or only a pension, if the payer transmits the article 85 certification by the return deadline, or by a person with only exempt income up to the social pension amount or income under final withholding ([IGR art 84(1)][igr]). Payroll withholding is on account: the employer annualises expected income at the bands and applies the family and SMaC credits the employee requests; medical and rent credits are claimed in the return ([IGR art 101][igr]).

A return filed within 30 days after 31 July is valid but carries the late-filing charge. A return filed later is null: it cannot be used to claim a refund of a credit shown in it, but the Tax Office can still collect tax on it ([IGR art 93(2)-(3)][igr]).

## 5. Penalties and interest

| Item | Amount | Source |
|---|---|---|
| Late return (art 137(2)(a)), general | 400 | [IGR art 139(1)(d), replaced by DD 156/2026, art 16][dd156] |
| Late return filed within 30 days of the deadline, general | 200 | [DD 156/2026, art 16][dd156] |
| Late return covering only wages, pensions, certified San Marino land and buildings or art 104(3) income | 100, or 50 within 30 days | [DD 156/2026, art 16][dd156] |
| Omitted return (2021 onward) where the payer's certificate was filed and the person had only wages, pensions or certified property income | 100 | [Law 141/2025, art 54(4)][l141] |
| Late payment interest | Legal interest rate plus 2 points, from the due date to payment; not charged on penalties | [IGR art 128][igr] |
| Assessment paid within 60 days of notice | Penalties reduced by 50% | [IGR art 129][igr] |

## 6. Cross-border points

- Non-residents are taxed only on article 5 income; they get the SMaC credit on wages and pensions but no family credits ([IGR arts 5, 16(4), 16(8-bis)][igr]).
- Frontier workers paid by a San Marino employer have San Marino-source employment income ([IGR art 5][igr]); relief in their residence State depends on that State's treaty and credit rules.
- Payments to non-residents for professional services, capital income and equipment rentals carry withholding: see `sm-cross-border`.
- Foreign tax on a resident's income: the article 18 credit in section 3.

## 7. Two worked examples that recompute

### Example 1: employee, gross wage 30,000 with SMaC interpolation

A resident employee earns 30,000 gross. All three default contribution components apply (9.9%), there are no benefits, other income or family credits, and the employee has enough SMaC spend for the full credit. Forfait 2,100; contributions 2,970; taxable wage 24,930. Tax: 900 + 1,040 + (24,930 - 18,000) x 17% = 3,118.10. Taxable income of 24,930 falls between the 20,900 and 25,080 rows, so the credit is interpolated: 1,444.62 on a spend limit of 5,455.14 (26.48%). Net IGR 1,673.48. The Tax Office calculator returned the same credit and spend limit for this case.

```oa-check
name: San Marino 2026 employee wage 30,000 with interpolated SMaC credit
inputs:
  gross_wage: 30000
  deductible_contribution_rate: 0.099
  lower_income_endpoint: 20900
  upper_income_endpoint: 25080
  lower_credit: 1300
  upper_credit: 1450
  lower_spend: 4250
  upper_spend: 5500
steps:
  wage_forfait: min(gross_wage * 0.07, 2800)
  deductible_contributions: gross_wage * deductible_contribution_rate
  taxable_wage: gross_wage - wage_forfait - deductible_contributions
  tariff_tax: 10000 * 0.09 + 8000 * 0.13 + (taxable_wage - 18000) * 0.17
  endpoint_fraction: (taxable_wage - lower_income_endpoint) / (upper_income_endpoint - lower_income_endpoint)
  maximum_credit: round(lower_credit + endpoint_fraction * (upper_credit - lower_credit), 2)
  required_eligible_spend: round(lower_spend + endpoint_fraction * (upper_spend - lower_spend), 2)
  stated_credit_percentage: floor(maximum_credit / required_eligible_spend * 10000) / 100
  annual_igr_after_full_credit: tariff_tax - maximum_credit
expected:
  wage_forfait: 2100
  deductible_contributions: 2970
  taxable_wage: 24930
  tariff_tax: 3118.10
  maximum_credit: 1444.62
  required_eligible_spend: 5455.14
  stated_credit_percentage: 26.48
  annual_igr_after_full_credit: 1673.48
```

The same rules give: taxable income 85,000, tax before credits 19,340 across all eight bands; taxable wage 8,000, tax 720, and the 752.40 no-SMaC credit capped at 720, so net tax is nil with no refund.

### Example 2: self-employed professional with the business SMaC credit (edge case)

A resident professional has taxable professional income of 20,000 (after deductible contributions), no wages, no losses and 5,000 of eligible SMaC spend. Separate tax at the 2026 rate of 18%: 3,600 (the statutory 17% would give 3,400). Income is under 25,000, so the business SMaC credit is 18% of spend up to 5,000: 900. Net 2,700. If this person also had wages, they would have to elect one SMaC credit under article 17(1-quater).

```oa-check
name: San Marino 2026 self-employed income with business SMaC credit
inputs:
  business_taxable_income: 20000
  separate_rate_2026: 0.18
  eligible_smac_spend: 5000
steps:
  separate_igr: business_taxable_income * separate_rate_2026
  eligible_credit: min(separate_igr, min(eligible_smac_spend, 5000) * 0.18)
  net_separate_igr: separate_igr - eligible_credit
expected:
  separate_igr: 3600
  eligible_credit: 900
  net_separate_igr: 2700
```

The same rules give: two resident parents sharing two dependent children 50/50 for the whole year each get 250 (500 x 50%), with no uplift; foreign income of 15,000 within total income of 60,000 and San Marino net tax of 10,000 caps the foreign credit at 2,500.

## 8. Ask the client first

1. Registered residence, where the person actually lived in 2026 and where family and economic interests sit.
2. Every income type: wages, pensions, business or professional income, property in and outside San Marino, foreign dividends and interest, termination or arrears payments.
3. Payslips and the employer's IGR G certificate, with the contributions actually deducted.
4. Dependants: relationship, age, study or unemployment status, their own income, months dependent and the other parent's share.
5. SMaC card spend by the taxpayer and household, plus medical and rent receipts paid traceably.
6. Foreign tax paid, with final assessments and payment proof.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law 166/2013 (IGR), official coordinated text updated to 22 December 2025: arts 1-18, 22-30, 84-85, 93, 101, 124, 128-129, 139, Annexes C and E | https://www.consigliograndeegenerale.sm/on-line/documento17086436.html | 2026-10-30 |
| Law 141/2025 of 12 November 2025, art 54 (commencement, 18% rate 2026-2030, cadastral phase-out, omitted-return charge) | https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html | 2026-10-30 |
| Delegated Decree 156/2026 of 12 October 2026, arts 2-10, 16-20 | https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33 | 2026-10-30 |
| ISS circular 2187/UC/2026 of 22 April 2026 (2026 contribution rates) | https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49158490.html | 2026-10-30 |
| Tax Office public 2026 IGR calculator (Law 141/2025) | https://www.pa.sm/portalepa/servlet/portalepa.hic.servizi.HGCalcoloIGRLegge141_2025?MPasso=1&MTipo=G&profondita=1 | 2026-10-24 |

Not yet confirmed: the 2026 social pension amount (dependants' income limit and filing exemption); the 2026 legal interest rate; the controlled-rent (canone calmierato) levels; the 2027 return forms and attachment circular; mixed-income ordering beyond article 17(1-bis) and (1-quater); the special residence regimes.

[igr]: https://www.consigliograndeegenerale.sm/on-line/documento17086436.html
[l141]: https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html
[dd156]: https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33
[calc]: https://www.pa.sm/portalepa/servlet/portalepa.hic.servizi.HGCalcoloIGRLegge141_2025?MPasso=1&MTipo=G&profondita=1

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
