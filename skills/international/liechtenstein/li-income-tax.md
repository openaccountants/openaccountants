---
name: li-income-tax
description: >
  Prepare 2026 Liechtenstein individual wealth-and-income tax (Vermögens- und
  Erwerbssteuer) workpapers under the Tax Act (SteG) and Tax Ordinance (SteV).
  Covers residence, the minimum-income exemption (SteV art. 8), the three
  statutory state-tax tariffs (single, single parent, joint spouses; zero band to
  CHF 15,855 / 23,783 / 31,710, top rate 8%), the 4% deemed yield on net wealth,
  wealth valuation and debts, deductions (earning costs CHF 1,600, commuting,
  meals, insurance, pension 18% cap, children CHF 12,700, donations), loss use
  (70% cap), the municipal surcharge (150% to 250% of state tax), rounding,
  filing extensions, payment, 4% interest and fines. Trigger on: Liechtenstein
  income tax, Erwerbssteuer, Vermögenssteuer, Sollertrag, Gemeindesteuerzuschlag,
  Steuererklärung Liechtenstein. Out of scope: expenditure (lump-sum) taxation,
  trusts and foundations, capital-payment taxation and treaty cases.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.4
---

# Liechtenstein individual income and wealth tax v0.4

## Who this applies to

SteG article 6 makes individuals with domestic domicile or habitual abode subject to unlimited wealth/income taxation, subject to the specific exceptions and relief rules. Foreign residents have the specified domestic wealth/income categories; article 7 controls start/end dates. This ordinary-resident 2026 workpaper is not a residence/treaty or special-regime determination. Current source is the [Tax Act consolidated 1 July 2026][law]; selected provisions and read limits are below.

## Rates, bands and thresholds

Before using the tariff, screen the separate **Existenzminimum exemption** in SteG article 15(2)(i). For an unlimited-liability resident, article 14 income that does not exceed the applicable minimum is exempt. If only part of the income is domestically taxable, test total income; for liability lasting less than a year, annualise that total. This test is not a further deduction from taxable income and is distinct from the zero band and fixed tariff subtraction. [SteG, articles 15(2)(i) and 19][law]

SteV article 8 sets these monthly gross minima, with the amended base amounts first applying to tax year 2025 and continuing in the current 2026 text:

| Established category | CHF per month | CHF for a full twelve months |
|---|---:|---:|
| Single | 2,100 | 25,200 |
| Qualifying single parent | 2,600 | 31,200 |
| Jointly assessed spouses/registered partners | 3,200 | 38,400 |
| Separately assessed spouses/registered partners in the same household, or factual cohabiting partners | 1,600 each | 19,200 each |
| Each child aged up to 5, additional | 300 | 3,600 |
| Each child aged 6–11, additional | 450 | 5,400 |
| Each child aged 12 or older, additional | 600 | 7,200 |

Establish the actual family/child category, article 14 total income including relevant deemed wealth yield, and liability period before deciding eligibility. Resolve changing family circumstances or disputed attribution separately; do not replace this gross-income test with post-deduction taxable income **x**. [SteV, article 8 and its amendment notes][ordinance]

For income not exempt under that screen, the following reproduces article 19(1). Values are CHF taxable income **x**, not gross salary. “Subtract” is the fixed amount in the statutory formula, not another itemised deduction. The tariff's basic allowance is embedded in its zero band and formula. Qualifying single-parent status is the statutory family-law category, not any adult living alone with a child. Special capital/substitute wealth taxation has different rules.

### Ordinary tariff, article 19(1)(a)

| Taxable income x | State tax |
|---|---|
| Up to 15,855 | 0 |
| 15,856–21,140 | 1% × x − 159 |
| 21,141–42,280 | 3% × x − 581 |
| 42,281–73,990 | 4% × x − 1,004 |
| 73,991–105,700 | 5% × x − 1,744 |
| 105,701–137,410 | 6% × x − 2,801 |
| 137,411–169,120 | 6.5% × x − 3,488 |
| 169,121–211,400 | 7% × x − 4,334 |
| 211,401 or more | 8% × x − 6,448 |

### Qualifying single parent, article 19(1)(b)

| Taxable income x | State tax |
|---|---|
| Up to 23,783 | 0 |
| 23,784–31,710 | 1% × x − 238 |
| 31,711–63,420 | 3% × x − 872 |
| 63,421–110,985 | 4% × x − 1,506 |
| 110,986–158,550 | 5% × x − 2,616 |
| 158,551–206,115 | 6% × x − 4,202 |
| 206,116–253,680 | 6.5% × x − 5,232 |
| 253,681–317,100 | 7% × x − 6,501 |
| 317,101 or more | 8% × x − 9,672 |

### Joint spouses, article 19(1)(c)

| Combined taxable income x | State tax |
|---|---|
| Up to 31,710 | 0 |
| 31,711–42,280 | 1% × x − 317 |
| 42,281–84,560 | 3% × x − 1,163 |
| 84,561–147,980 | 4% × x − 2,008 |
| 147,981–211,400 | 5% × x − 3,488 |
| 211,401–274,820 | 6% × x − 5,602 |
| 274,821–338,240 | 6.5% × x − 6,976 |
| 338,241–422,800 | 7% × x − 8,667 |
| 422,801 or more | 8% × x − 12,895 |

Source for every threshold/rate/subtraction: [SteG, article 19][law]. Apply the statutory wealth/income rounding below before the printed tariff; do not interpolate across the endpoints. Final tax rounding and special-assessment application still need the current return instructions.

## The base

1. Establish family status, children, residence periods and the applicable assessment route. Article 8 ordinarily combines spouses/registered partners living in an unseparated relationship; its separate-assessment election and child-income rules are distinct. SteV article 6 requires the joint written separate-assessment application/withdrawal by 31 December of the relevant year and at least five years' separate assessment. Do not select the joint tariff merely from one person's marital label. [SteG, articles 8 and 18][law]; [SteV, article 6][ordinance]
2. Reconcile assets, values and liabilities. Article 9 addresses taxable wealth; articles 10–12 contain exclusions, debt allocation and valuation rules. Foreign property/PE and partly domestic wealth need the actual allocation rules. A negative wealth base or deduction for every worldwide debt is not assumed. Trusts, foundations, valuation disputes and substitute wealth taxation remain specialist cases.
3. For ordinary taxable net wealth, apply the 4% Sollertrag under articles 5 and 14(2)(l), then include that deemed yield in taxable income. Article 15(1) prevents separately taxing actual returns on wealth already subjected to that wealth-tax mechanism. Do not add the same taxed asset's interest/dividend again solely because it appears in a bank statement. The 4% figure is now statutory for 2026, not an annual Finance Act assumption. [SteG, articles 5 and 14–15][law]; [Act 2024/483, commencement II(2)][amendment]
4. Reconcile employment, self-employment, property, pensions and other receipts under articles 14–16, with their exclusions and actual deduction conditions. Article 15's private-asset gain exclusions do not decide a business-asset or separate property-gain case. Article 16 governs expenses, losses and personal deductions. The tariff allowance is embedded in the formula; it must not be deducted a second time from the input base.
5. Retain the final established taxable income **x**, including the applicable deemed wealth yield, before selecting the state formula. Articles 18, 21 and 22 contain part-year/special-income/foreign-relief rules; do not apply the simple full-year examples indiscriminately.

### Ordinary wealth and debt workpaper

SteG article 9 starts with all movable and immovable wealth, and attributes a partnership without legal personality to its members. Articles 9(3)–(4) and SteV 7 have separate beneficiary/founder and substitute-payment rules; the ordinary workpaper does not value a trust/foundation interest.

| Ordinary step | Statutory method | Official source |
|---|---|---|
| Household/personal-use assets and private vehicles | Exclude up to CHF 26,400, or CHF 52,800 for joint spouses, from the combined qualifying value; not a general cash allowance | [SteG 10(a)][law] |
| Necessary occupational/agricultural/business tools | Stated CHF 2,100 limit; establish qualifying articles/value | [SteG 10(b)][law] |
| Other exempt wealth | Article 10 separately lists qualifying public collections, evidenced agricultural products, foreign land and foreign PEs | [SteG 10(c)–(f)][law] |
| Ordinary valuation date | Beginning of tax year or beginning of liability | [SteG 12(1)][law] |
| Quoted securities | Actual quoted price | [SteG 12(1)(c)][law] |
| Unquoted securities, rights and claims | Market value, ordinarily not below nominal unless contrary evidence; disputed/doubtful claims reflect recoverability. Unquoted-security valuation also requires SteV 7a/Annex 1 | [SteG 12(1)(d)][law]; [SteV 7a][ordinance] |
| Recurring rights and private redeemable life insurance | Equivalent arm's-length acquisition value for the stated recurring rights; old-employment pensions excluded from wealth valuation. Redeemable life policies use surrender value plus surplus until maturity | [SteG 12(1)(e)–(f)][law] |
| Land/buildings | Ordinarily earnings value, at least official tax-assessed value | [SteG 12(2)][law] |
| Business assets | Acquisition/production cost less depreciation/value adjustments | [SteG 12(3)][law] |
| Debt | Actual principal-debtor obligations; only the taxpayer's share of joint debt. Where only part of wealth is domestically taxable, allocate debt by domestic-taxable/total wealth ratio; debt cannot make taxable wealth negative | [SteG 11][law] |

Keep the gross asset schedule, each exemption, date/value proof, total worldwide wealth and debt share/allocation separately. No universal balance-sheet or nominal-value rule replaces the stated classifications. Use the ordinary unquoted-company workpaper below; actual company classifications and values, foreign asset values and disputed/actuarial rights still require their own evidence.

SteG 18(1) rounds wealth **down to CHF 100 before conversion into deemed income**, and income **down to CHF 10**. Apply these at the stated bases, retaining the unrounded reconciliation. This is not permission to round each invoice or to invent a final-tax rounding convention. [SteG 18(1)][law]

### Unquoted company shares: ordinary valuation workpaper

Use SteV 7a and Annex 1 before carrying an unquoted company interest into the wealth schedule. The starting accounts are the last accounts closed before the holder's tax year begins; use consolidated accounts where commercial law requires them. Where the consolidated accounts omit tax-permitted reserves, the ordinance permits corresponding equity and earnings adjustments. The official 2026 helper illustrates valuation at **1 January 2026**, ordinarily using **31 December 2025** accounts for a calendar-year company. [SteV 7a(3), Annex 1][ordinance]; [2026 helper, opening instructions][valuation-helper]

First check the exceptions. If the taxpayer proves the ordinary method does not represent market value, SteV 7a(2)(a) permits a different valuation. An actual transfer between independent parties supplies the purchase price as market value under 7a(2)(b), while the company's economic position has not materially changed. Retain the transaction and valuation evidence. [SteV 7a(2)][ordinance]

For an operating trading, industrial or service company, prepare these separate steps:

| Step | Method | Official source |
|---|---|---|
| Substance value S | Reported equity **after profit appropriation**, plus hidden reserves on participations and taxed hidden reserves. Revalue underlying unquoted-company participations under Annex 1 A(1); if that value is below their carrying value, retain the carrying value | [SteV Annex 1 A(3)][ordinance] |
| Earnings R | Commercial net earnings, adjusted for non-business expenses. Annualise a period shorter or longer than twelve months to twelve months. The authority can adjust results affected by fundamental business changes or exceptional events | [SteV Annex 1 A(2)][ordinance] |
| Earnings value E | **max(0, (2 × current annualised R + preceding annualised R) × 0.85 ÷ (3 × K))**. The 0.85 factor is the 15% risk deduction. K is **20%** for regulated financial institutions and service providers under FMA supervision, **15%** for other legal persons | [SteV Annex 1 A(2), formula on printed page 34][ordinance] |
| Operating company value | **(2 × E + S) ÷ 3**, subject to the non-operating-asset adjustments and minimum below | [SteV Annex 1 A(1), formula on printed page 34][ordinance] |

For shareholder receivables and non-business assets within SteG 54, remove their value from S for the operating weighting and remove their capitalised net earnings from the earnings component. Add those asset values back in full afterwards. The minimum is **60% of operating substance value plus 100% of those excluded asset values**. Keep the asset classification, valuation, related net results and the article 54 reconciliation; do not merely remove the asset's income and leave its value weighted inside S as well. [SteV Annex 1 A(1)][ordinance]

Use substance value until a newly formed company has representative results. Holding, finance and property companies, companies in liquidation and inactive companies use substance value under Annex 1 B. **Banks and insurers are not finance companies for that exception**; classify them under the actual rules before choosing a method or K. [SteV Annex 1 A(2), B][ordinance]

Annex 1 C bases the minority deduction on **voting rights**, for value determined under A: below 20% voting rights gives a **20% deduction**; at least 20% but below 50% gives **10%**; at least 50% gives **zero**. Private shareholder agreements do not change that statutory treatment. Establish the holder's economic interest and voting rights separately; do not apply the deduction automatically to an Annex 1 B company or assume unequal capital and voting interests are identical. [SteV Annex 1 C][ordinance]

The official helper is supporting calculation material. Its cells F70/G70 use one ownership percentage to allocate value, and J70 uses that same input for the minority lookup. Its P44/P57 formulas round company value down to CHF 100. Keep those form operations distinct from the statutory valuation and from SteG 18's rounding of the taxpayer's total wealth; they do not establish a final-tax rounding rule. Reconcile unusual share classes, consolidated reserves, actual non-operating assets and representative earnings before using the result. [2026 helper, cells F70:K70, P44, P57][valuation-helper]

### Ordinary income deductions and exclusions

Match each receipt to SteG 14–15 before deductions: actual returns on wealth already subject to the wealth mechanism are excluded under 15(1); personal asset gains and business/property/participation gains have different 15(2) gates. Do not turn every credited receipt into taxable salary or every asset disposal into exempt private gain.

| Deduction screen | Current statutory rule and boundary | Official source |
|---|---|---|
| Ordinary business expenses | Actual business-supported costs under 16(2)(b)(1), not private living costs | [SteG 16][law] |
| Own business-capital interest | Article 16(2)(b)(2) expressly uses the article 5 Sollertrag and imports 12(3) and 54(2)–(6). It does not import 54(1) through that reference. Establish the personal-business capital, valuations and special adjustments; do not automatically copy the corporate no-current-loss rule | [SteG 16(2)(b)(2)][law] |
| Business losses | Evidenced unused prior losses, ordinary 70% current-taxable-income cap; definitive cessation has its stated exception. Foreign PE losses have nonduplication, annual-proof and recapture by earlier 5 years/end unlimited liability | [SteG 16(2)(b)(3)–(4)][law] |
| Employee earning costs | CHF 1,600 ordinary allowance, with the supported extraordinary-cost route below; no duplicate allowance plus full actual costs | [SteG 16(2)(c)][law]; [SteV 12–16][ordinance] |
| Specified social/accident pensions | 70% deduction only for the AHV/IV and accident-invalidity pension categories named in 16(2)(d), not every occupational pension | [SteG 16(2)(d)][law] |
| Eligible child | CHF 12,700, with actual custody/support/education conditions, no conflicting maintenance deduction and half each for the stated jointly held custody/separate assessment | [SteG 16(3)(a)][law] |
| Legal maintenance/support | Actual payments in the specified spouse/parent/legal-support categories | [SteG 16(3)(b)][law] |
| Own statutory insurance | Actual own AHV/IV/FAK/ALV/mandatory-accident contributions under the stated provision | [SteG 16(3)(c)][law] |
| Private life/health/other qualifying accident premiums | Actual qualifying payments capped at CHF 3,700, CHF 7,400 for joint spouses, plus CHF 2,200 per eligible child | [SteG 16(3)(d)][law] |
| Recognised occupational pension | Qualifying one-off/current contributions, capped at 18% of the expressly listed article 14(2)(a,b,c,d,f) income categories | [SteG 16(3)(e)][law] |
| Child education | Actual eligible evidenced costs capped at CHF 12,700 per child/year, less scholarships; primary/secondary/domestic music school and permanently employed-child exclusions apply | [SteG 16(3)(f)][law] |
| Uninsured medical/accident/dental | Qualifying unreimbursed costs capped at CHF 6,300 per person. Costs over CHF 300 per person require receipts; CHF 300 is not stated as a deduction from every claim | [SteG 16(3)(g)][law] |
| Qualifying donations | Stated eligible recipients and 10% pre-business-loss taxable-income limit; individual gifts not exceeding CHF 100 are excluded. Total donations over CHF 300 require evidence. This is not 10% of gross salary; establish the prescribed cap base before calculation | [SteG 16(3)(h)][law] |
| Occupational education/retraining | Actual eligible costs capped at CHF 12,700, with a first secondary-II qualification or the stated age 20/first-qualification exclusion conditions | [SteG 16(3)(i)][law] |
| Part-year and disallowed expenses | Fixed-franc 16(2)–(3) deductions are proportional to duration. Private living/status costs, private damage insurance and direct/indirect taxes are not deductible | [SteG 16(4)–(5)][law] |

Agricultural yield-unit/accounting elections, corporate-rule cross-references in 16(6), special capital pensions, indirect participations and disputed cap bases require their complete applicable chain. The table supplies ordinary screens, not automatic entitlement or a universal deduction order.

### Employee earning costs: allowance versus supported excess

SteV 12 uses CHF 1,600 as the ordinary earning-cost allowance. If qualifying evidenced costs exceed it, only the excess is added under 12(2), producing the supported total rather than CHF 1,600 plus that full total. Articles 13–16 identify commuting and additional outside meals as the extraordinary categories. [SteV 12–16][ordinance]

For the article 14(1) commuting route, document the average home/work distance and actual eligible days. Recognise one return trip per day, at most **200 km per day**, and at most **220 days/year**, or **200 days for teachers**. Apply **CHF 0.50/km to the first 10,000 annual eligible kilometres** and **CHF 0.40/km above 10,000**. Domestic home/work locations also have the article 14(2)/Annex 2 lump-sum route, with stated teacher, part-time and part-year reductions; do not claim both routes. Employer payment of the full commute excludes the deduction; a partial contribution is wage income with the full cost deduction, and passenger reimbursements reduce uncovered costs. [SteV 14][ordinance]

For qualifying meals where work is outside the place of residence, SteV 16 gives **CHF 1,100 for 220 days**, or **CHF 1,000 for 200 teacher days**. Employer canteen availability or employer cost contributions exclude that deduction; cash contributions are wage income. Reduce the allowance for part-time/non-full-year employment as required. Establish actual eligibility before adding meals to the commuting workpaper. [SteV 16][ordinance]

### Municipality, business losses and payroll credits

Article 75 sets the municipality surcharge as a percentage **of state tax**, fixed annually by the municipality, legally between 150% and 250%. This is not 150%–250% of taxable income. Obtain the municipality's rate for the year. Article 75(2) excludes an added surcharge on source withholding under article 25. Do not add a municipality percentage to the wage-tax deduction itself. [SteG, article 75][law]

For an ordinary assessment with the municipality's surcharge m:

    municipality tax = state tax × m
    combined tax before credits = state tax + municipality tax

For business losses under article 16(2)(b)(3), assess prior unused loss evidence and the ordinary 70% current-taxable-income cap; the year of definitive business cessation has a separate exception. A multiplication using an assumed loss register is not proof of entitlement. The personal capital-interest rule itself refers to article 54(2)–(6), as distinguished above; no broader corporate-rule import is assumed. [SteG, article 16][law]

Resident wages also have payroll withholding; use [li-payroll-social](li-payroll-social.md) for its distinct base and instructions. Article 29 credits withholding in an ordinary assessment and addresses excess amounts. Preserve wage certificates and all prepayments, relief and final assessment data before deciding a balance/refund; a payroll percentage is not the final state/municipality tariff. [SteG, articles 24–29][law]

### Retained predecessor workpapers

Further cases, recomputed with the tariff above (the minimum-income case is the first worked example below):

- Ordinary case: CHF 80,000 other taxable income plus 4% of CHF 500,000 taxable wealth gives CHF 100,000 income, CHF 3,256 state tax and CHF 8,140 combined tax with an assumed 150% municipal surcharge.
- Joint case: CHF 200,000 established joint income gives CHF 6,512 state tax and CHF 18,233.60 combined with an assumed 180% surcharge.
- Qualifying single parent: CHF 150,000 established income gives CHF 4,884 state tax and CHF 14,652 combined with an assumed 200% surcharge.
- Ordinary business loss: CHF 100,000 relevant positive income and CHF 90,000 established unused losses permits CHF 70,000 use and leaves CHF 20,000 losses. Definitive cessation and other special cases are excluded.

The municipal surcharges in these cases are assumptions, not the 2026 rates of any municipality.

## Deadlines and filing

Article 94 requires truthful, complete, signed filing even without a personal form/notice. The filing date for 2026 income is the one set in the tax administration's 2026 return documents; on 30 October 2026 the authority's page listed only the 2025 forms and guidance, so take the date from the 2026 invitation when it is issued. Obtain the current return and deduction/election instructions and supporting account, asset, family and foreign-income evidence.

SteV 39 requires the applicable accounts/data sheet, foreign-property acquisition/official values, participation valuations, certificates, deduction evidence and agricultural workpaper/accounts where corresponding entries are made. Under SteV 40, a reasoned written extension request goes to the responsible municipal tax office **before the ordinary filing deadline**, for **at most five months**. An extension **over one month** requires an advance payment of **80% of the prior-year tax**. It is not an automatic change to payment maturity. [SteV 39–40][ordinance]

The authority's current eTax page recommends preparing the individual return in eTax and permits electronic transmission with attachments. Retain actual year-specific forms, representation/access, receipts and any extension decision. [Current eTax instructions][etax]; [current forms index][forms]

## Penalties and interest

Article 114 generally requires payment within 30 days of legal maturity, subject to its exceptions; the actual assessment/delivery and special-departure facts matter. SteV article 45 sets late interest at 4%, while the precise start/base and actual notice must be established. Article 135's procedural fines require its post-reminder intentional/negligent breach, with ordinary CHF 1,000 and serious/repeat CHF 10,000 maxima. These are not automatic filing charges. Exact interest day-count and appeals/correction application remain incomplete; the ordinary extension method is supplied above. [SteG, articles 94, 113–114 and 135][law]; [SteV, article 45][ordinance]

## Cross-border points

For part-domestic liability, SteG 18(1a) distinguishes directly connected deductions from its ratio/foreign-law treatment of other deductions and uses the worldwide wealth/income rate. Article 15(2)(i) separately uses total annualised income for the minimum-income screen. Do not apply the ordinary resident example to a treaty/nonresident/part-year case. Use the [cross-border skill](li-cross-border.md) for the separate domestic, treaty, foreign-credit and claim methods and their explicit application gaps. [SteG 15(2)(i), 18, 21–23][law]

## Two worked examples that recompute

### Minimum-income exemption screen

Assume an unlimited-liability single resident for the full year, no child addition and CHF 24,000 total article 14 income after including every relevant source and deemed wealth yield. The CHF 25,200 annual minimum exceeds that established total by CHF 1,200. Article 15(2)(i) therefore exempts this income; do not compute a positive tariff liability merely because a post-deduction figure falls above the zero band. The arithmetic below checks the threshold and headroom; statutory eligibility is an express case assumption.

```oa-check
name: Liechtenstein assumed full-year single minimum-income screen
inputs:
  statutory_monthly_gross_minimum: 2100
  months_in_full_year: 12
  established_total_article_14_income: 24000
steps:
  annual_gross_minimum: statutory_monthly_gross_minimum * months_in_full_year
  income_below_minimum: annual_gross_minimum - established_total_article_14_income
expected:
  annual_gross_minimum: 25200
  income_below_minimum: 1200
```

### Employee costs feed the taxable-income base once

Assume a full-year ordinary-tariff employee, CHF 90,000 established taxable gross wages, and 220 eligible days with a documented 60 km daily return commute under SteV 14(1). No commute reimbursement/passenger contribution applies. The 13,200 km give CHF 5,000 for the first 10,000 km plus CHF 1,280 for the rest. Assume the full CHF 1,100 outside-meal allowance is eligible, with no employer canteen or meal support. Total supported earning costs are CHF 7,380, exceeding the CHF 1,600 allowance; do not claim CHF 8,980.

Assume actual eligible own statutory insurance CHF 5,000, private premiums CHF 2,500 and recognised occupational contributions CHF 7,000, with the stated pension cap base CHF 90,000. The pension ceiling is CHF 16,200, so all CHF 7,000 is allowed. With no other income/deduction and CHF 300,000 established taxable net wealth, employment after deductions is CHF 68,120;4% wealth yield adds CHF 12,000. Rounded taxable income is CHF 80,120; state tax is CHF 2,262. An assumed 150% municipal surcharge gives CHF 5,655 combined before credits. With CHF 5,000 established total withholding credit, already including any applicable withholding interest, the assumed balance is CHF 655. This does not decide real asset values, reimbursement, pension eligibility, town rate or final assessment. [SteG 5, 16, 18–19, 29, 75][law]; [SteV 12–16][ordinance]

```oa-check
name: Liechtenstein assumed employee expense pension and wealth bridge
inputs:
  taxable_gross_wages: 90000
  eligible_work_days: 220
  eligible_daily_return_km: 60
  first_km_band: 10000
  first_km_rate: 0.50
  excess_km_rate: 0.40
  established_eligible_meals: 1100
  ordinary_job_allowance: 1600
  eligible_own_statutory_insurance: 5000
  eligible_private_premiums_paid: 2500
  applicable_private_premium_cap: 3700
  eligible_occupational_contribution: 7000
  established_pension_cap_income: 90000
  pension_cap_rate: 0.18
  established_taxable_net_wealth: 300000
  statutory_wealth_yield: 0.04
  selected_tariff_rate: 0.05
  selected_tariff_subtraction: 1744
  assumed_municipal_surcharge: 1.50
  established_creditable_withholding: 5000
steps:
  annual_commuting_km: eligible_work_days * eligible_daily_return_km
  commuting_cost: min(annual_commuting_km, first_km_band) * first_km_rate + max(0, annual_commuting_km - first_km_band) * excess_km_rate
  supported_job_costs: commuting_cost + established_eligible_meals
  earning_cost_deduction: ordinary_job_allowance + max(0, supported_job_costs - ordinary_job_allowance)
  pension_cap: established_pension_cap_income * pension_cap_rate
  allowed_pension: min(eligible_occupational_contribution, pension_cap)
  allowed_private_premiums: min(eligible_private_premiums_paid, applicable_private_premium_cap)
  adjusted_employment_income: taxable_gross_wages - earning_cost_deduction - eligible_own_statutory_insurance - allowed_private_premiums - allowed_pension
  rounded_wealth: floor(established_taxable_net_wealth / 100) * 100
  deemed_wealth_income: rounded_wealth * statutory_wealth_yield
  rounded_taxable_income: floor((adjusted_employment_income + deemed_wealth_income) / 10) * 10
  state_tax: rounded_taxable_income * selected_tariff_rate - selected_tariff_subtraction
  municipal_tax: state_tax * assumed_municipal_surcharge
  combined_before_credits: state_tax + municipal_tax
  assumed_balance: combined_before_credits - established_creditable_withholding
expected:
  annual_commuting_km: 13200
  commuting_cost: 6280
  supported_job_costs: 7380
  earning_cost_deduction: 7380
  pension_cap: 16200
  allowed_pension: 7000
  allowed_private_premiums: 2500
  adjusted_employment_income: 68120
  rounded_wealth: 300000
  deemed_wealth_income: 12000
  rounded_taxable_income: 80120
  state_tax: 2262
  municipal_tax: 3393
  combined_before_credits: 5655
  assumed_balance: 655
```

## Ask the client first

Obtain residence/family/election facts, the municipality/year rate, all assets/debts and values, income and benefits, assessed losses, actual deductions, foreign taxes and withholding/prepayment certificates. Refer partial-year migration, foreign relief, special pension/capital receipts, foundations/trusts, expenditure taxation, wealth substitutions, business disposals and contested classifications.

## Sources

| Source | URL | Read on |
|---|---|---|
| Steuergesetz (SteG), LR 640.0, consolidated 1 July 2026, articles 2, 5-19, 21-29, 75, 94, 113-114, 135 | https://www.gesetze.li/konso/pdf/2010340000 | 2026-10-30 |
| Steuerverordnung (SteV), consolidated 1 July 2026, articles 6-8, 12-16, 39-40, 45 | https://www.gesetze.li/konso/pdf/2010437000 | 2026-10-30 |
| LGBl. 2024 Nr. 483, amendment of the SteG (4% Sollertrag in article 5 from tax year 2026) | https://www.gesetze.li/chrono/pdf/2024483000 | 2026-10-24 |
| Steuerverwaltung, eTax electronic return | https://www.llv.li/de/landesverwaltung/steuerverwaltung/etax-elektronische-steuererklaerung | 2026-10-30 |
| Steuerverwaltung, wealth and income tax (forms, guidance, municipal surcharges) | https://www.llv.li/de/landesverwaltung/steuerverwaltung/steuern-natuerliche-personen/vermoegens--und-erwerbssteuer | 2026-10-31 |
| Steuerverwaltung, 2026 unquoted-company valuation helper, sheet Bewertung 2026 | https://www.llv.li/servicekonto/steuerverwaltung/unternehmensanteile-ohne-kursnotiz-bewertung-2026.xlsx | 2026-10-31 |

Not yet confirmed: the 2026 municipal surcharge of each municipality (the authority page lists surcharges up to 2025 only); the filing date for 2026 returns; expenditure (lump-sum) taxation for non-working foreign residents; substitute wealth taxation of trusts and foundations; actual unquoted-share valuations outside the ordinary method described here, unequal share-class allocations and actuarial rights; final rounding of the assessed tax; the exact interest day-count.

[valuation-helper]: https://www.llv.li/servicekonto/steuerverwaltung/unternehmensanteile-ohne-kursnotiz-bewertung-2026.xlsx
[etax]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/etax-elektronische-steuererklaerung
[forms]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/steuern-natuerliche-personen/vermoegens--und-erwerbssteuer
[law]: https://www.gesetze.li/konso/pdf/2010340000
[ordinance]: https://www.gesetze.li/konso/pdf/2010437000
[amendment]: https://www.gesetze.li/chrono/pdf/2024483000

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
