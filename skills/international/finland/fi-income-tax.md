---
name: fi-income-tax
description: >
  Prepare Finnish individual income-tax computations for tax year 2026 covering
  wages, benefits, pensions, dividends, investment disposals, rental income and
  ordinary sole-trader profits. Establish earned and capital income, calculate
  statutory deductions and credits, select municipal and parish rates, and
  reconcile state tax, health contributions and broadcasting tax. Use for Form 5,
  business profit allocation, 2026 commuting costs, household credit, pension
  deductions, dividend splits, capital losses and personal assessment. Includes
  two executable examples, current statutory references and explicit distinctions
  between final liability and withholding. Cross-border residence and relief use
  the linked individual cross-border Guide; Åland municipal differences require
  the separate regional schedule.
version: 1.7
jurisdiction: FI
tax_year: 2026
last_updated: 2026-10-26
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Finland individual income tax v1.7

**Tax year:** 2026. Source-cited ordinary individual computation; independent source-review evidence is in the [pack README](README.md). The October 2026 amendments below apply to the whole 2026 assessment, including eligible payments before commencement.

## Who this applies to

A Finnish-resident individual is taxable on worldwide income, with treaty relief where applicable; nonresidents have income-specific Finnish-source rules. Establish status/periods using the [individual cross-border Guide](fi-individual-cross-border-residence.md). This Guide computes ordinary mainland tax and identifies the separate Åland municipal route. A freelance label does not itself decide employment, business or other income-producing activity. [Income Tax Act 1535/1992, sections 9–11, 29–30][law].

Keep earned and capital categories separately. Wages, taxable benefits, pensions and ordinary social-security benefits enter earned income unless a specific exemption applies. Rent, taxable interest, dividends' capital portion and investment gains enter capital income. A sole trader divides a reconciled business result; an incorporated company is a different taxpayer. Preserve income/expense evidence, residence, municipality, parish membership and family/age inputs. [Income Tax Act, sections 29–33b, 38, 61, 64, 92][law].

## Rates, bands and thresholds

| 2026 taxable earned income EUR | State tax at lower limit EUR | Rate on excess | Law |
|---|---:|---:|---|
| 0–22,000 | 0 | 12.64% | [2026 scale Act 1140/2025, section 1][scale] |
| 22,000–32,600 | 2,780.80 | 19% | [Section 1][scale] |
| 32,600–40,100 | 4,794.80 | 30.25% | [Section 1][scale] |
| 40,100–52,100 | 7,063.55 | 33.25% | [Section 1][scale] |
| Above 52,100 | 11,053.55 | 37.5% | [Section 1][scale] |

| Item | Applicable 2026 amount / formula | Primary source |
|---|---|---|
| Capital tax | 30% through EUR 30,000 annual taxable capital income; 34% above | [Income Tax Act, section 124][law] |
| Municipal/parish | Select the actual municipality/parish from the annual decision; Helsinki municipal 5.30%, Lutheran 1.00%, Orthodox 1.80% | [Vero annual decision under Assessment Procedure Act section 91a(3)][local-rates] |
| Wage expense deduction | EUR 750, capped at wage income; qualifying actual ordinary expenses replace it if greater | [Income Tax Act, section 95][law] |
| Commuting | Actual cheapest qualifying mode, deduction after EUR 800 own liability capped at EUR 7,000; specified benefit months reduce own liability by EUR 75 each, minimum EUR 150 | [Income Tax Act, section 93, Act 873/2026 commencement][law] |
| Basic deduction | Up to EUR 4,265, reduced by 18% of income above EUR 4,265 after prior qualifying deductions; never above remaining income | [Income Tax Act, section 106][law] |
| Work-income credit | 18% of qualifying work income, maximum EUR 3,430; reduce 2% of net earned income between EUR 35,000 and 50,550, with no further reduction above 50,550 | [Income Tax Act, section 125][law] |
| Credit cap supplements | EUR 1,200 if aged 65 before year start; EUR 105 per minor child in custody at year end, doubled for the statutory sole-custodian/no-spouse case | [Income Tax Act, section 125(3)–(4)][law] |
| Pension deduction | Full maximum EUR 11,080 from annual national pension × 1.173 rounded up to next EUR 10, capped at pension; taper below | [Income Tax Act, section 100][law]; [Kela 2026 full pension EUR 787.07/month][kela] |
| Pension supplement tax | 5.85% of pension after pension deduction above EUR 60,000 | [Income Tax Act, section 124(4)][law] |
| Health care | 1.10% of established health-care base plus 0.39% of the eligible positive care-base/daily-base difference; pure pension/benefit base can therefore bear 1.49%; apply the mixed-base and §14(2) exclusion rules below | [Health Insurance Act, chapter 18 sections 14–20][health-law]; [2026 tax bases][tax-bases] |
| Daily allowance | 0.88% of qualifying wage/work base if annual wage/work income at least EUR 17,255; liability starts the month after the 16th birthday and continues through the month of the 68th birthday; entrepreneur supplement uses separate YEL rules | [Health Insurance Act, chapter 18 sections 5, 15, 23–24][health-law]; [2026 tax bases][tax-bases] |
| Broadcasting tax | Covered mainland residents reaching 18 in the year: 2.5% above EUR 15,150 of the larger of net earned+capital income or confirmed YEL+MYEL income, capped at EUR 160 | [Broadcasting Tax Act, sections 1–2][yle-law] |
| Ordinary household credit | 40% qualifying registered-company labour charge including VAT, or 15% qualifying directly paid wages plus listed employer contributions; EUR 150 own liability; ordinary-work maximum EUR 2,100/person | [Income Tax Act, sections 127a–127c, 127f][law] |
| Oil-heating replacement | 60% qualifying contractor labour, or 30% wages plus listed employer contributions; combined household-credit ceiling EUR 3,500/person, of which other work at most EUR 2,100 | [Income Tax Act, section 127f][law] |

**Currency corrections.** Act 873/2026 commenced on 13 October but expressly applies the amended commuting rule to tax year 2026 and section 127f to eligible payments from 1 January 2026. Do not divide the annual commuting/credit calculation at 13 October. The Vero household-credit summary still displaying EUR 1,600/35% and the English automatic-deductions page retaining a 3.44% upper work-credit taper conflict with the current statute; use the enacted rules above. [Income Tax Act, sections 93, 125, 127f and amendment commencement][law]; [older household summary][household]; [automatic deductions summary][automatic].

## The base

### Earned income and deductions, in order

1. Sum taxable wages including cash and valued fringe benefits, pensions, taxable benefits, other earned receipts, business earned portions and earned dividends. Use the [payroll Guide](fi-employer-payroll.md) for benefit valuation; classify exempt allowances and benefits under their actual statutory conditions rather than excluding anything labelled reimbursement. [Income Tax Act, sections 61–69, 71–73, 92][law].
2. From wage income deduct the greater of the EUR 750 standard expense deduction (limited to wages) or actual qualifying ordinary employment costs. Unemployment-fund fees and allowed commuting are separate deductions, not absorbed into EUR 750. Commuting uses real working days and the cheapest available mode; private-car use needs its qualifying facts and annual authority cost basis. From 2026 labour-market membership fees and home/vacation-home costs incurred to earn **wages**, whether flat-rate or actual, are not deductible. Eligible nonwage home-office use instead follows the authority's capped schedule: EUR 980 full-time/more than half workdays, EUR 490 regular part-time, EUR 245 occasional repeated use. Avoid double deductions across income categories. [Income Tax Act, sections 31, 93, 95][law]; [Vero home office][office].
3. From net earned income deduct statutory employee pension, unemployment and health daily-allowance contributions and eligible mandatory pension payments. YEL is deductible once in business, personally or through the spouse route; add back business-booked YEL if claimed personally. It is not both an expense and a personal deduction. [Income Tax Act, section 96][law]; [YEL deduction instructions][yel].
4. For pensions, start with maximum EUR 11,080, subtract 51% of net earned income above that maximum up to EUR 22,500, then 19.6% above EUR 22,500; floor at zero and cap at the pension amount. Pension receipts do not earn the work-income credit merely because they are earned income. Then compute basic deduction from income after the preceding applicable deductions: `min(remaining_income, max(0, 4265 − 0.18 × max(0, remaining_income − 4265)))`. Apply confirmed earned-category losses under section 118. [Income Tax Act, sections 100, 106, 118, 125][law].
5. Apply the state scale and actual municipal/parish rates to their established bases. Mainland bases share the ordinary deduction rules; Åland municipal law differs. Compute work-income credit using **qualifying work income** for the 18% amount and **net earned income** for the taper. Its cap includes qualifying age/child additions. Apply first against state earned tax, with any unused amount proportionately against municipal/church/health-care tax, before the later tax credits. Do not subtract it from the daily-allowance contribution. [Income Tax Act, sections 106, 124–125][law].

For health care, establish the municipal-tax-like base **C** under Health Insurance Act chapter 18 §§14,16–19, substituting YEL/MYEL confirmed income for the specified entrepreneurial receipts once and without deducting those pension premiums from the care base. Calculate basic care contribution as `C × 1.10%`. For an ordinary mix of wages and pension/benefits, add `max(0, C − D) × 0.39%`, where **D** is the statutory daily-allowance income base, not the contribution actually paid. Do **not** set D to zero just because wage/work income is below EUR 17,255: the base still offsets the care supplement even when the 0.88% payment is zero. The supplement is not charged on the receipts specified in §14(2); retain their separate classification and exclude them from the surcharge calculation. Apply D only to receipts within actual daily-allowance age/coverage: it begins the month after the 16th birthday and continues through the 68th-birthday month. Ordinary wages outside that age-covered period do not enter D and can therefore bear the 0.39% care surcharge, subject to the §14(2) exclusions. This differs from below-EUR-17,255 wages within the covered age period, which remain in D. The death-year exclusion in §5 also applies. [Health Insurance Act, chapter 18 §§5,14–20][health-law].

For an ordinary wage/pension mix with already-established C = EUR 35,000 and D = EUR 30,000 and no §14(2) receipts, care contribution is EUR 385 + EUR 19.50 = **EUR 404.50**, rather than 1.49% of gross pension added to 1.10% of gross wages. The municipal deductions have already entered C. Pure pension/benefit income with D = 0 bears 1.49% of its established care base. Compute daily allowance separately on its own wage/work base. Employee health is inside tax-card withholding and is not deducted again as a separate payroll insurance item. [Health Insurance Act, chapter 18 §§14–20][health-law]; [Vero 2026 insured-contribution guidance §§2.2.2–2.3][health-detail].

### Capital receipts, gains and losses

For normal accounts, 85% of a qualifying listed-company dividend is taxable capital income. For an unlisted-company dividend compute 8% annual return on the **adjusted mathematical value** of the holding: within that amount 25% is taxable capital and 75% exempt up to the recipient's EUR 150,000 aggregate annual qualifying dividends; the part above EUR 150,000 is 85% taxable capital. Above the 8% return, 75% is taxable earned income and 25% exempt. Subtract specified company housing and shareholder loans from the value, and apply the 2026 related-share-exchange valuation adjustment in section 33b(1); do not assume last balance-sheet equity equals the dividend base. Work-contribution dividends have a separate earned-income rule. Foreign-company comparability uses section 33c, and equity-savings-account dividends use section 53b instead of this ordinary 85% rule. [Income Tax Act, sections 33a–33c, 53b][law]; [Valuation Act, sections 2–10][value-law].

For a taxable disposal calculate proceeds minus undepreciated actual acquisition cost and selling costs, comparing that deduction with the deemed acquisition cost of 20% of proceeds, or 40% for ownership at least ten years. Use one method, not deemed cost plus separate selling costs. Deduct prior depreciation from actual cost. An exempt own-home gain requires at least two years' ownership and continuous own/family permanent-home use for at least two years during ownership before sale; check partial use and the statutory land limits. Ordinary small-disposal gain exemption applies when aggregate included proceeds do not exceed EUR 1,000; this is not a EUR 1,000 gain allowance. [Income Tax Act, sections 45–50][law].

Deduct eligible disposal losses against gains, then eligible other capital income; unused losses carry for the following five years. Losses on exempt own homes, personal-use property and the specified small disposals are disallowed. A disposal loss does **not** generate a capital-deficit tax credit. An equity-savings-account loss is recognised only when the account is closed and follows its separate ordering. [Income Tax Act, sections 50, 53b][law].

Rental income is gross rent and tenant-paid owner expenses less attributable income-producing costs: maintenance charges and **expensed** housing-company finance charges, insurance, qualifying repairs, management and permitted property depreciation. Capitalised housing-company charges and capital improvements enter acquisition cost or the proper depreciation schedule; purchase price of housing-company shares is not annually depreciated. Allocate mixed/private use and below-market/non-income-producing arrangements correctly. Debt interest is a separate income-producing-debt deduction; principal repayments, own-home and consumer interest are not deductible. Keep rental periods, invoices and the housing company's expensing/capitalisation confirmation. [Income Tax Act, sections 29, 31, 54, 58][law]; [Vero rental deductions][rent]; [property transfer Guide](fi-property-transfer-tax.md).

Net eligible capital expenses/interest/current-business-loss election can create a capital deficit under section 60. Ordinary deficit credit is 30%, maximum EUR 1,400 plus EUR 400 for one dependent minor child or EUR 800 for two or more, subject to spouse transfer/unused-ceiling rules. Residual capital-category loss carries ten years; distinguish it from five-year disposal losses. Apply the statutory credit ordering and spouse rules rather than both carrying and crediting the same amount. [Income Tax Act, sections 58–60, 118, 131–134][law].

### Sole trader: reconcile before splitting

Use business recognition, deductions, inventory and depreciation rules under the Business Income Tax Act; the [corporate Guide's ordinary asset/cost schedules](fi-corporate-income-tax.md) identify shared base rules, but corporate participation/group/interest restrictions do not automatically apply to a sole trader. Private drawings are not wages/expenses. Own/spouse remuneration and specified young-child pay are excluded; mixed-use assets/cars and negative-equity borrowing require their statutory allocation. [Business Income Tax Act, sections 7–8, 16, 18, 30, 33–34][business-law].

Deduct usable same-source prior losses, then 5% entrepreneur deduction from the positive remaining distributable business income; it cannot create a loss. Compute capital allocation on prior-year business assets less eligible liabilities valued under Valuation Act sections 15–17, plus 30% of qualifying wages paid in the preceding twelve months. Qualifying fixed assets use tax residual/required comparison values, not arbitrary market value. Statutorily excluded bank deposits/debt securities do not enter the sole trader's net assets. For a start-up use the year's closing net assets. [Income Tax Act, sections 30a, 38, 41][law]; [Valuation Act, sections 3, 8, 15–17][value-law].

Ordinary capital allocation is the annual 20% return; elect 10% or all earned income before assessment ends, subject to the compulsory capital minimum for qualifying fixed-asset real-estate/securities gains. Adjust for the length of the relevant tax period. Spouses divide the earned portion by work contributions and capital portion by net-asset interests; lacking contrary evidence the statutory equal allocation applies. A current business loss can be claimed wholly/partly against capital income before assessment closes (joint-business spouses must both request), or carried as confirmed business loss for ten following tax years. Record the election and avoid duplicate use. [Income Tax Act, sections 14, 38, 59, 119][law]; [Form 5 instructions][form5].

### Credits and final reconciliation

Check household-credit **work eligibility**, location/use, payment year, contractor's prepayment registration at payment or the EEA alternative evidence, invoice labour/material split and any prohibited subsidy/double claim. For ordinary 2026 contractor work, calculate 40% of qualifying labour including VAT, subtract EUR 150 once for the year and limit ordinary work to EUR 2,100/person. Oil-heating replacement has the separate enhanced rate within the EUR 3,500 combined maximum. Spouse allocation/insufficient tax follows section 127c; this is a tax credit, not an income deduction or a cash refund exceeding tax capacity. Maintenance support under a qualifying agreement/judgment gives 1/8 of payments, capped at EUR 80 per minor child under section 127. [Income Tax Act, sections 127–127c, 127f][law].

Add broadcasting tax based on the statutory net-income/YEL alternative; do not deduct it from personal taxable income. Calculate health contributions and any pension supplement, then apply foreign-tax relief/other applicable credits in their legal order. Reconcile withholding and credited prepayments against the resulting assessment. A payroll tax rate is only a collection mechanism; it is not the final marginal or effective annual rate. [Income Tax Act, sections 31, 124–134][law]; [Broadcasting Tax Act][yle-law].

### Åland: parallel state and municipal schedules

Use Åland Municipal Tax Act 2011:119 sections 1–2: national income classification is incorporated except where Åland makes its own deduction rules. Keep two base columns. State tax uses the national earned-income deductions above; for each scale band subtract 12.64 percentage points from its marginal rate (equivalently mainland pre-credit scale tax minus 12.64% of the same taxable state base). Do not apply a mainland scale lower-limit tax together with an Åland marginal rate without adjusting the accumulated lower-band tax. Capital tax remains the national capital schedule. [Income Tax Act, section 124][law]; [Åland Municipal Tax Act, sections 1–2][ax-law].

For the Åland municipal column:

- Sections 9 and 13 allow the EUR 750 wage expense route and separate unemployment-fund/commuting costs; the 2026 amendment removes labour-market membership fees and wage home-office costs, with the same nonwage capped-office route. Mandatory pension, unemployment and daily-allowance contributions follow section 14 without duplicate YEL deductions.
- Section 10 uses commuting own liability EUR 750 and maximum deduction EUR 6,000. If more than half the deductible travel costs are public transport, waive the own liability. Qualifying unemployment/parental months reduce it EUR 80/month, minimum EUR 160. This regional rule is not replaced by the national October EUR 800/75/150 amendment. Ferry/long-journey work-location accommodation can qualify for actual rent up to EUR 6.90/m²/month for at most 30m² under section 10; the separate second-work-home allowance in section 11 is at most EUR 250/full month (and rent/benefit value), with the two-home/over-100km and no-duplication conditions.
- Pension deduction under section 19 has full amount `ceil((annual full single national pension × 1.346 − 1480) / 10) × 10`, capped at pension; reduce by 51% of net earned income above that full amount and floor at zero. Disability deduction section 20 is up to EUR 440 × established disability percentage (at least 30%), limited to nonpension net earned income, with the statutory pension/history exceptions.
- Section 21 study-grant deduction is at most EUR 2,600 and the grant, reduced by 50% of net earned income above EUR 2,600; additionally EUR 340 per qualifying full-time study term. The reduced-taxpaying-capacity deduction section 17 is at most EUR 1,400 in full hundreds; sole illness costs must meet both EUR 700 and 10% net-income tests. Section 18's former general medical-expense deduction and section 22's former municipal earned-income allowance are repealed.
- After the applicable deductions use section 23's **2026** basic deduction: `min(remaining_income, max(0, 3925 − 0.084 × max(0, remaining_income − 3925)))`, then deduct confirmed earned-category losses. The EUR 3,925 amount applies for all tax year 2026 under amendment 2026:10, effective 1 March.
- Multiply the established municipal base by the actual Åland municipality/parish rates in the annual decision. Section 25 allows the national work credit's unused state portion proportionately against municipal, church and health-care tax; sections 26/26a incorporate household relief including national section 127f; section 28 incorporates capital-deficit relief. Keep their ordering and capacity restrictions. [Åland Municipal Tax Act, sections 9–28 and 2026:10 commencement][ax-law].

Personal Åland media fee is **EUR 128 for 2026**, if the resident reaches 18 in the year and the larger of national net earned+capital income or confirmed YEL+MYEL income exceeds EUR 14,000. It is a fixed fee, not 2.5% of the excess; it is not personally deductible. Municipal residence for moves and part-year residence must be established before choosing media fee versus broadcasting tax. [Åland Media Fee Act 2019:103, sections 2, 4][ax-media-law]; [Vero 2026 indexed fee/relief guidance][ax-media].

Additional ordinary mainland deductions are fact-specific, not automatic: section 95a second-work-home allowance up to EUR 450/full month and rent/benefit value, with qualifying family/two-workplace facts, over-100km distances and no duplicate exempt compensation; section 105 study-grant deduction at most EUR 2,600/grant, reduced 50% above EUR 2,600 net earned income; section 98 substantially reduced taxpaying capacity up to EUR 1,400 in full hundreds, with illness-only costs meeting both EUR 700 and 10% tests. Apply before basic deduction where the statute places them. [Income Tax Act, sections 95a, 98, 105][law].

## Deadlines and filing

Review the pre-completed personal return and correct missing/wrong income, deductions, foreign items and assets in MyTax by its allocated date; preserve acknowledgement and assessment. Form 5 is required for business including inactive years, with the allocated filing deadline. A date in spring 2026 for **2025** income is not the deadline for **2026** income. The 2026 reporting timeline puts personal returns in March 2027; the issued 2027 deadline/assessment controls. Update tax cards/prepayments during the year and track separate assessment-end dates for elections, corrections and confirmed losses. [Assessment Procedure Act, sections 7–8][assessment]; [Vero personal return][personal-return]; [Form 5 instructions][form5]; [2026 reporting timeline][timeline].

## Penalties and interest

Assessment Procedure Act section 33 sets EUR 50 individual late fee for the relevant reporting before assessment closes. Sections 32–32b ordinarily charge 2% of added income, with distinct 3–10% repeated/manifest-disregard, 5% estimated, 1% specified unclear/unreasonable and 0.5% qualifying post-assessment voluntary-correction routes. Added-tax routes apply where the income base cannot be used. Individual minimum EUR 75 is subject to statutory nonimposition exceptions; an authority decision, date and conduct determine the route. [Assessment Procedure Act, sections 32–33][assessment].

Ordinary late-paid 2026 tax bears 9.5% annual interest from the day after due date through payment using actual days/365. Relief interest on back tax/additional prepayment is a distinct 4.5% route for 2026, with the statutory EUR 20 back-tax interest deduction where applicable. Follow the decision and period; do not treat all assessment interest as late-payment interest. [Vero interest guidance][interest].

## Cross-border points

Use the [individual cross-border Guide](fi-individual-cross-border-residence.md) for residence, foreign employment, nonresident classifications and credit/exemption. Treaty residence does not remove domestic reporting automatically. Åland state scale percentages are reduced by 12.64 percentage points under section 124; municipal bases/deductions follow Åland's own law and must be computed separately, while residents pay the regional media fee instead of mainland broadcasting tax. Use the parallel regional schedule in The base; the mainland worked example does not apply there. [Income Tax Act, section 124][law]; [Vero Åland deductions][aland].

## Two worked examples that recompute

**1. Wage income through the ordinary mainland components.** Assume a fully Finnish-insured 40-year-old, no children, no church membership, Helsinki home municipality, EUR 40,000 ordinary wages, no other income/deductions, standard EUR 750 expenses, pension EUR 2,920, unemployment EUR 356 and daily allowance EUR 352, all bases/eligibility established. Net earned income for credit taper is EUR 39,250. Taxable earned base is EUR 35,622 and basic deduction zero. Work credit is EUR 3,345. With illustrative cent rounding by component, state tax after credit EUR 2,363.96, municipal EUR 1,887.97, health care EUR 391.84, daily allowance EUR 352 and broadcasting EUR 160 total EUR 5,155.77. Pension/unemployment are additional employee deductions, not added tax. Actual assessment rounding controls the filing.

```oa-check
name: Finland ordinary 2026 wage computation with local tax and work credit
inputs:
  gross_wages: 40000
  standard_expenses: 750
  employee_pension: 2920
  employee_unemployment: 356
  daily_allowance: 352
steps:
  net_earned_income: gross_wages - standard_expenses
  taxable_earned_income: net_earned_income - employee_pension - employee_unemployment - daily_allowance
  basic_deduction: max(0, 4265 - max(0, taxable_earned_income - 4265) * 0.18)
  state_scale_tax: round(4794.80 + (taxable_earned_income - 32600) * 0.3025, 2)
  work_credit: min(gross_wages * 0.18, 3430) - max(0, min(net_earned_income, 50550) - 35000) * 0.02
  state_after_credit: state_scale_tax - work_credit
  municipal_tax: round(taxable_earned_income * 0.053, 2)
  health_care: round(taxable_earned_income * 0.011, 2)
  broadcasting_tax: min(160, max(0, net_earned_income - 15150) * 0.025)
  total_tax_and_health: state_after_credit + municipal_tax + health_care + daily_allowance + broadcasting_tax
expected:
  net_earned_income: 39250
  taxable_earned_income: 35622
  basic_deduction: 0
  state_scale_tax: 5708.96
  work_credit: 3345
  state_after_credit: 2363.96
  municipal_tax: 1887.97
  health_care: 391.84
  broadcasting_tax: 160
  total_tax_and_health: 5155.77
```

**2. Business profit allocation and capital bands.** Assume business revenue EUR 100,000, fully established deductible costs EUR 40,000, usable prior losses EUR 10,000, full-year capital-allocation base EUR 20,000, 20% election, no fixed-asset gain minimum/spouse issue, and other established taxable capital income EUR 41,000. Entrepreneur deduction is EUR 2,500 and distributable income EUR 47,500: capital EUR 4,000, earned EUR 43,500. Aggregate taxable capital income EUR 45,000 gives EUR 14,100 capital tax. The earned portion feeds the separate full personal computation; this example does not apply the wage-only EUR 750 deduction to business profit.

```oa-check
name: Finland sole trader allocation and aggregate capital bands
inputs:
  revenue: 100000
  deductible_costs: 40000
  prior_losses: 10000
  allocation_base: 20000
  other_taxable_capital_income: 41000
steps:
  profit_after_losses: revenue - deductible_costs - prior_losses
  entrepreneur_deduction: profit_after_losses * 0.05
  distributable_income: profit_after_losses - entrepreneur_deduction
  business_capital: min(distributable_income, allocation_base * 0.20)
  business_earned: distributable_income - business_capital
  aggregate_capital: other_taxable_capital_income + business_capital
  capital_tax: min(aggregate_capital, 30000) * 0.30 + max(0, aggregate_capital - 30000) * 0.34
expected:
  profit_after_losses: 50000
  entrepreneur_deduction: 2500
  distributable_income: 47500
  business_capital: 4000
  business_earned: 43500
  aggregate_capital: 45000
  capital_tax: 14100
```

## Ask the client first

1. What residence/periods, municipality, parish membership, age, spouse and custody facts apply?
2. What wages, benefits, pensions, business profits, dividends, rents, gains and foreign receipts were paid or realised?
3. Which costs, debt purposes, pension payments, tax-loss decisions and prior credit balances are evidenced?
4. What business assets/debts, wage additions, spouse work and allocation elections apply?
5. Which ownership/holding-period, dividend-value, home-use and household-work facts establish exemption or relief?
6. Which tax-card, prepayment, return and assessment deadlines/decisions need reconciliation?

## Sources

| Primary source | Scope / provisions read | Read on |
|---|---|---|
| [Income Tax Act 1535/1992][law] | Sections 9–14, 29–33c, 38–41, 45–60, 61–69, 93–100, 106, 118–125, 127–127f, 131–134; Act 873/2026 commencement | 2026-10-26 |
| [2026 state-scale Act 1140/2025][scale] | Sections 1–2 | 2026-10-26 |
| [Business Income Tax Act 360/1968][business-law] | Ordinary business costs, assets, interest and depreciation | 2026-10-26 |
| [Valuation Act 1142/2005][value-law] | Sections 2–10, 15–17; dividend and sole-trader assets | 2026-10-26 |
| [Health Insurance Act 1224/2004][health-law] | Chapter 18 sections 14–24; bases and annual-rate mechanism | 2026-10-26 |
| [Broadcasting Tax Act 484/2012][yle-law] | Sections 1–2 | 2026-10-26 |
| [Assessment Procedure Act 1558/1995][assessment] | Sections 7–8, 32–33 | 2026-10-26 |
| [Vero municipal/parish 2026 decision][local-rates]; [tax bases][tax-bases] | Actual local lookup and 2026 health rates | 2026-10-26 |
| [Kela 2026 benefits][kela] | Full national pension used for section 100 formula | 2026-10-26 |
| [Vero Form 5][form5]; [YEL deduction][yel]; [home office][office]; [rental deductions][rent] | Operational classifications and claim evidence | 2026-10-26 |
| [Vero personal return][personal-return]; [timeline][timeline]; [interest][interest] | Filing/assessment and payment procedures | 2026-10-26 |
| [Vero 2026 insured-contribution guidance][health-detail] | §§2.2.2–2.3: mixed health-care and daily-allowance bases | 2026-10-26 |
| [Vero household summary][household]; [automatic deductions][automatic] | Stale passages identified above; statute prevails | 2026-10-26 |
| [Åland Municipal Tax Act 2011:119][ax-law] | Sections 1–2, 9–28, 2026:10 commencement; current official browser text | 2026-10-26 |
| [Åland Media Fee Act 2019:103][ax-media-law]; [Vero 2026 media fee][ax-media] | Sections 2, 4 and indexed EUR 128 amount | 2026-10-26 |
| [Vero Åland deductions][aland] | Claim routes; its older national commuting figures are superseded by Act 873/2026 | 2026-10-26 |

Not yet confirmed: separately scoped agriculture/forestry, seafarer, equity-remuneration and exceptional investment regimes. The ordinary mainland/Åland source-review evidence is recorded in the pack README; no professional attestation is claimed.

[law]: https://www.finlex.fi/fi/lainsaadanto/1992/1535
[scale]: https://www.finlex.fi/fi/lainsaadanto/2025/1140
[business-law]: https://www.finlex.fi/fi/lainsaadanto/1968/360
[value-law]: https://www.finlex.fi/fi/lainsaadanto/2005/1142
[health-law]: https://www.finlex.fi/fi/lainsaadanto/2004/1224
[yle-law]: https://www.finlex.fi/fi/lainsaadanto/2012/484
[assessment]: https://www.finlex.fi/fi/lainsaadanto/1995/1558
[local-rates]: https://www.vero.fi/syventavat-vero-ohjeet/paatokset/47465/kuntien-ja-seurakuntien-tuloveroprosentit-vuonna-2026/
[tax-bases]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/tax_card/tax-rate-and-income-ceiling/tax-bases/
[kela]: https://www.kela.fi/ajankohtaista/muutoksia-kelan-etuuksiin-vuonna-2026
[insurance]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/being-an-employer/social-insurance-contributions/
[form5]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/taxation-of-self-employed-individuals/instructions-for-filing/
[yel]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/taxation-of-self-employed-individuals/deductions/pension-premiums-yel/
[office]: https://www.vero.fi/henkiloasiakkaat/vahennykset/tulonhankkimismenot/tyohuonevahennys/
[rent]: https://www.vero.fi/en/individuals/property/rental_income/deductions/
[personal-return]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/your_tax_return_and_tax_assessment_deci/instructions-for-filing/
[timeline]: https://vero.fi/en/individuals/tax-cards-and-tax-returns/your_tax_return_and_tax_assessment_deci/tax-decision/when-can-i-report-income-or-deductions-for-my-tax-assessment/
[interest]: https://www.vero.fi/en/individuals/payments/paying-taxes/interest-on-late-payments/
[household]: https://vero.fi/en/individuals/deductions/Tax-credit-for-household-expenses/tax-credit-amount/
[automatic]: https://www.vero.fi/en/individuals/deductions/what-can-I-deduct/these-deductions-are-calculated-automatically-by-the-tax-administration/
[aland]: https://www.vero.fi/en/individuals/deductions/what-can-I-deduct/deductions-for-the-residents-of-aland/

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

[ax-law]: https://www.regeringen.ax/alandsk-lagstiftning/alex/2011119
[ax-media-law]: https://www.regeringen.ax/alandsk-lagstiftning/alex/2019103
[ax-media]: https://www.vero.fi/sv/Detaljerade_skatteanvisningar/anvisningar/89754/medieavgift-i-landskapet-%C3%A5land4/

[health-detail]: https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/338472/vakuutetun-sairausvakuutusmaksu2/
