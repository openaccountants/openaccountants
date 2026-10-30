---
name: li-income-tax
description: >
  Prepare 2026 Liechtenstein individual wealth-and-income tax workpapers. Use for
  ordinary resident taxation, family-status tariff selection, deemed wealth yield,
  the separate minimum-income exemption, state tax, municipality surcharge, business loss screening and
  reconciliation of payroll withholding. Establish residence, family/election facts,
  taxable net wealth, income categories, deductions and the municipality's actual
  annual rate before computing. The Guide replaces approximate summary brackets
  with the statutory formulas and separates the tariff allowance from deductible
  expenses. It does not complete asset valuations, all deductions, lump-sum pension
  taxation, trusts, expenditure taxation, treaties, exact filing calendars or live
  filing, and remains pending local accountant review.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.3
---

# Liechtenstein individual income and wealth tax v0.3

Historical source/editorial evidence is in the [24 October review record](../../../docs/research/2026-10-24-liechtenstein-pack-review.md), confined to its exact predecessor and scope. The [current country review register](../../../ledgers/li-pack-review-evidence/README.md) identifies the 30 October review, repairs and exact-file verification. Named Liechtenstein accountant review remains open.

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

SteG article9 starts with all movable and immovable wealth, and attributes a partnership without legal personality to its members. Articles9(3)–(4) and SteV7 have separate beneficiary/founder and substitute-payment rules; the ordinary workpaper does not value a trust/foundation interest.

| Ordinary step | Statutory method | Official source |
|---|---|---|
| Household/personal-use assets and private vehicles | Exclude up to CHF26,400, or CHF52,800 for joint spouses, from the combined qualifying value; not a general cash allowance | [SteG10(a)][law] |
| Necessary occupational/agricultural/business tools | Stated CHF2,100 limit; establish qualifying articles/value | [SteG10(b)][law] |
| Other exempt wealth | Article10 separately lists qualifying public collections, evidenced agricultural products, foreign land and foreign PEs | [SteG10(c)–(f)][law] |
| Ordinary valuation date | Beginning of tax year or beginning of liability | [SteG12(1)][law] |
| Quoted securities | Actual quoted price | [SteG12(1)(c)][law] |
| Unquoted securities, rights and claims | Market value, ordinarily not below nominal unless contrary evidence; disputed/doubtful claims reflect recoverability. Unquoted-security valuation also requires SteV7a/Annex1 | [SteG12(1)(d)][law]; [SteV7a][ordinance] |
| Recurring rights and private redeemable life insurance | Equivalent arm's-length acquisition value for the stated recurring rights; old-employment pensions excluded from wealth valuation. Redeemable life policies use surrender value plus surplus until maturity | [SteG12(1)(e)–(f)][law] |
| Land/buildings | Ordinarily earnings value, at least official tax-assessed value | [SteG12(2)][law] |
| Business assets | Acquisition/production cost less depreciation/value adjustments | [SteG12(3)][law] |
| Debt | Actual principal-debtor obligations; only the taxpayer's share of joint debt. Where only part of wealth is domestically taxable, allocate debt by domestic-taxable/total wealth ratio; debt cannot make taxable wealth negative | [SteG11][law] |

Keep the gross asset schedule, each exemption, date/value proof, total worldwide wealth and debt share/allocation separately. No universal balance-sheet or nominal-value rule replaces the stated classifications. The detailed unquoted-company valuation, foreign asset values and disputed/actuarial rights remain separate workpapers.

SteG18(1) rounds wealth **down to CHF100 before conversion into deemed income**, and income **down to CHF10**. Apply these at the stated bases, retaining the unrounded reconciliation. This is not permission to round each invoice or to invent a final-tax rounding convention. [SteG18(1)][law]

### Ordinary income deductions and exclusions

Match each receipt to SteG14–15 before deductions: actual returns on wealth already subject to the wealth mechanism are excluded under15(1); personal asset gains and business/property/participation gains have different15(2) gates. Do not turn every credited receipt into taxable salary or every asset disposal into exempt private gain.

| Deduction screen | Current statutory rule and boundary | Official source |
|---|---|---|
| Ordinary business expenses | Actual business-supported costs under16(2)(b)(1), not private living costs | [SteG16][law] |
| Own business-capital interest | Article16(2)(b)(2) expressly uses the article5 Sollertrag and imports12(3) and54(2)–(6). It does not import54(1) through that reference. Establish the personal-business capital, valuations and special adjustments; do not automatically copy the corporate no-current-loss rule | [SteG16(2)(b)(2)][law] |
| Business losses | Evidenced unused prior losses, ordinary70% current-taxable-income cap; definitive cessation has its stated exception. Foreign PE losses have nonduplication, annual-proof and recapture by earlier5years/end unlimited liability | [SteG16(2)(b)(3)–(4)][law] |
| Employee earning costs | CHF1,600 ordinary allowance, with the supported extraordinary-cost route below; no duplicate allowance plus full actual costs | [SteG16(2)(c)][law]; [SteV12–16][ordinance] |
| Specified social/accident pensions |70% deduction only for the AHV/IV and accident-invalidity pension categories named in16(2)(d), not every occupational pension | [SteG16(2)(d)][law] |
| Eligible child | CHF12,700, with actual custody/support/education conditions, no conflicting maintenance deduction and half each for the stated jointly held custody/separate assessment | [SteG16(3)(a)][law] |
| Legal maintenance/support | Actual payments in the specified spouse/parent/legal-support categories | [SteG16(3)(b)][law] |
| Own statutory insurance | Actual own AHV/IV/FAK/ALV/mandatory-accident contributions under the stated provision | [SteG16(3)(c)][law] |
| Private life/health/other qualifying accident premiums | Actual qualifying payments capped at CHF3,700, CHF7,400 for joint spouses, plus CHF2,200 per eligible child | [SteG16(3)(d)][law] |
| Recognised occupational pension | Qualifying one-off/current contributions, capped at18% of the expressly listed article14(2)(a,b,c,d,f) income categories | [SteG16(3)(e)][law] |
| Child education | Actual eligible evidenced costs capped at CHF12,700 per child/year, less scholarships; primary/secondary/domestic music school and permanently employed-child exclusions apply | [SteG16(3)(f)][law] |
| Uninsured medical/accident/dental | Qualifying unreimbursed costs capped at CHF6,300 per person. Costs over CHF300 per person require receipts; CHF300 is not stated as a deduction from every claim | [SteG16(3)(g)][law] |
| Qualifying donations | Stated eligible recipients and10% pre-business-loss taxable-income limit; individual gifts not exceeding CHF100 are excluded. Total donations over CHF300 require evidence. This is not10% of gross salary; establish the prescribed cap base before calculation | [SteG16(3)(h)][law] |
| Occupational education/retraining | Actual eligible costs capped at CHF12,700, with a first secondary-II qualification or the stated age20/first-qualification exclusion conditions | [SteG16(3)(i)][law] |
| Part-year and disallowed expenses | Fixed-franc16(2)–(3) deductions are proportional to duration. Private living/status costs, private damage insurance and direct/indirect taxes are not deductible | [SteG16(4)–(5)][law] |

Agricultural yield-unit/accounting elections, corporate-rule cross-references in16(6), special capital pensions, indirect participations and disputed cap bases require their complete applicable chain. The table supplies ordinary screens, not automatic entitlement or a universal deduction order.

### Employee earning costs: allowance versus supported excess

SteV12 uses CHF1,600 as the ordinary earning-cost allowance. If qualifying evidenced costs exceed it, only the excess is added under12(2), producing the supported total rather than CHF1,600 plus that full total. Articles13–16 identify commuting and additional outside meals as the extraordinary categories. [SteV12–16][ordinance]

For the article14(1) commuting route, document the average home/work distance and actual eligible days. Recognise one return trip per day, at most **200km per day**, and at most **220days/year**, or **200days for teachers**. Apply **CHF0.50/km to the first10,000 annual eligible kilometres** and **CHF0.40/km above10,000**. Domestic home/work locations also have the article14(2)/Annex2 lump-sum route, with stated teacher, part-time and part-year reductions; do not claim both routes. Employer payment of the full commute excludes the deduction; a partial contribution is wage income with the full cost deduction, and passenger reimbursements reduce uncovered costs. [SteV14][ordinance]

For qualifying meals where work is outside the place of residence, SteV16 gives **CHF1,100 for220days**, or **CHF1,000 for200 teacher days**. Employer canteen availability or employer cost contributions exclude that deduction; cash contributions are wage income. Reduce the allowance for part-time/non-full-year employment as required. Establish actual eligibility before adding meals to the commuting workpaper. [SteV16][ordinance]

### Municipality, business losses and payroll credits

Article 75 sets the municipality surcharge as a percentage **of state tax**, fixed annually by the municipality, legally between 150% and 250%. This is not 150%–250% of taxable income. Obtain the actual municipality/year rate; the earlier 150%–180% headline is not a statutory limit or verified 2026 municipality list. Article 75(2) excludes an added surcharge on source withholding under article 25. Do not add a municipality percentage to the wage-tax deduction itself. [SteG, article 75][law]

For an ordinary assessment with a verified surcharge m:

    municipality tax = state tax × m
    combined tax before credits = state tax + municipality tax

For business losses under article 16(2)(b)(3), assess prior unused loss evidence and the ordinary 70% current-taxable-income cap; the year of definitive business cessation has a separate exception. A multiplication using an assumed loss register is not proof of entitlement. The personal capital-interest rule itself refers to article54(2)–(6), as distinguished above; no broader corporate-rule import is assumed. [SteG, article 16][law]

Resident wages also have payroll withholding; use [li-payroll-social](li-payroll-social.md) for its distinct base and instructions. Article 29 credits withholding in an ordinary assessment and addresses excess amounts. Preserve wage certificates and all prepayments, relief and final assessment data before deciding a balance/refund; a payroll percentage is not the final state/municipality tariff. [SteG, articles 24–29][law]

### Retained predecessor workpapers

All five old executable blocks are preserved unchanged in the [original-controls annex](../../../ledgers/li-income-tax-evidence/retained-original-controls.md); their substantive cases remain here. The minimum-income case remains executable below.

- Ordinary case: CHF80,000 other taxable income plus4% of CHF500,000 taxable wealth gives CHF100,000 income, CHF3,256 state tax and CHF8,140 combined tax with an assumed150% municipal surcharge.
- Joint case: CHF200,000 established joint income gives CHF6,512 state tax and CHF18,233.60 combined with an assumed180% surcharge.
- Qualifying single parent: CHF150,000 established income gives CHF4,884 state tax and CHF14,652 combined with an assumed200% surcharge.
- Ordinary business loss: CHF100,000 relevant positive income and CHF90,000 established unused losses permits CHF70,000 use and leaves CHF20,000 losses. Definitive cessation and other special cases are excluded.

Those municipal rates, bases and eligibility facts are express assumptions, not a list of actual2026 town rates.

## Deadlines and filing

Article 94 requires truthful, complete, signed filing even without a personal form/notice. Confirm the municipality/authority's allocated 2027 due date for 2026 income; the earlier approximate April headline is not used as a verified deadline. Obtain the current return and deduction/election instructions and supporting account, asset, family and foreign-income evidence.

SteV39 requires the applicable accounts/data sheet, foreign-property acquisition/official values, participation valuations, certificates, deduction evidence and agricultural workpaper/accounts where corresponding entries are made. Under SteV40, a reasoned written extension request goes to the responsible municipal tax office **before the ordinary filing deadline**, for **at most five months**. An extension **over one month** requires an advance payment of **80% of the prior-year tax**. It is not an automatic change to payment maturity. [SteV39–40][ordinance]

The authority's current eTax page recommends preparing the individual return in eTax and permits electronic transmission with attachments. Retain actual year-specific forms, representation/access, receipts and any extension decision. No private account or filing was exercised; a future2027 allocated deadline is not inferred from the2025 forms currently listed on the authority's individual-tax page. [Current eTax instructions][etax]; [current forms index][forms]

## Penalties and interest

Article 114 generally requires payment within 30 days of legal maturity, subject to its exceptions; the actual assessment/delivery and special-departure facts matter. SteV article 45 sets late interest at 4%, while the precise start/base and actual notice must be established. Article 135's procedural fines require its post-reminder intentional/negligent breach, with ordinary CHF 1,000 and serious/repeat CHF 10,000 maxima. These are not automatic filing charges. Exact interest day-count and appeals/correction application remain incomplete; the ordinary extension method is supplied above. [SteG, articles 94, 113–114 and 135][law]; [SteV, article 45][ordinance]

## Cross-border points

For part-domestic liability, SteG18(1a) distinguishes directly connected deductions from its ratio/foreign-law treatment of other deductions and uses the worldwide wealth/income rate. Article15(2)(i) separately uses total annualised income for the minimum-income screen. Do not apply the ordinary resident example to a treaty/nonresident/part-year case. Use the [cross-border Guide](li-cross-border.md) for the separate domestic, treaty, foreign-credit and claim methods and their explicit application gaps. [SteG15(2)(i),18,21–23][law]

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

Assume a full-year ordinary-tariff employee, CHF90,000 established taxable gross wages, and220 eligible days with a documented60km daily return commute under SteV14(1). No commute reimbursement/passenger contribution applies. The13,200km give CHF5,000 for the first10,000km plus CHF1,280 for the rest. Assume the full CHF1,100 outside-meal allowance is eligible, with no employer canteen or meal support. Total supported earning costs are CHF7,380, exceeding the CHF1,600 allowance; do not claim CHF8,980.

Assume actual eligible own statutory insurance CHF5,000, private premiums CHF2,500 and recognised occupational contributions CHF7,000, with the stated pension cap base CHF90,000. The pension ceiling is CHF16,200, so all CHF7,000 is allowed. With no other income/deduction and CHF300,000 established taxable net wealth, employment after deductions is CHF68,120;4% wealth yield adds CHF12,000. Rounded taxable income is CHF80,120; state tax is CHF2,262. A verified case-only150% municipal surcharge gives CHF5,655 combined before credits. With CHF5,000 established total withholding credit, already including any applicable withholding interest, the assumed balance is CHF655. This does not decide real asset values, reimbursement, pension eligibility, town rate or final assessment. [SteG5,16,18–19,29,75][law]; [SteV12–16][ordinance]

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
  assumed_verified_municipal_surcharge: 1.50
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
  municipal_tax: state_tax * assumed_verified_municipal_surcharge
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

Obtain residence/family/election facts, the municipality/year rate, all assets/debts and values, income and benefits, assessed losses, actual deductions, foreign taxes and withholding/prepayment certificates. Refer partial-year migration, foreign relief, special pension/capital receipts, foundations/trusts, expenditure taxation, wealth substitutions, business disposals and contested classifications. All deductions/valuation methods, actual annual calendar, specialist law and named accountant review remain open; IT-IND coverage stays partial.

## Sources

Historical selected reads on24October2026:

- [SteG, consolidated 1 July 2026][law], articles 5–8, selected 9–16, 18–19, 24–29, 75, 94, 113–114 and 135. The full asset/deduction/foreign-relief/special-regime chain has not been audited.
- [SteV, consolidated 1 July 2026][ordinance], article 6 election, article 8 minimum-income exemption and article 45 interest; full current return/election procedures remain to be reconciled.
- [Act 2024/483][amendment], article 5 and commencement II(2); its article 19 schedule was compared with the current consolidation, not assumed from the prior approximate summary.

Current selected passages reread30October2026: SteG9–12,15–16,18–19,75 and SteV6,8,12–16,39–40; current eTax/form-index instructions. The ledger also binds the retained rules to their exact source passages. Full special-regime/actuarial/unquoted-company valuation and current assigned calendar remain unresolved.

[etax]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/etax-elektronische-steuererklaerung
[forms]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/steuern-natuerliche-personen/vermoegens--und-erwerbssteuer
[law]: https://www.gesetze.li/konso/pdf/2010340000
[ordinance]: https://www.gesetze.li/konso/pdf/2010437000
[amendment]: https://www.gesetze.li/chrono/pdf/2024483000

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
