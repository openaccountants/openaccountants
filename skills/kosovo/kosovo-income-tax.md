---
name: kosovo-income-tax
description: >
  Compute Kosovo personal income tax for 2026 individuals, sole traders and partners from the current Personal Income Tax Law and its amendments. Covers residence, worldwide and Kosovo-source income, progressive annual bands, small-business gross taxation, the actual-income election, allowable expenses, capital allowances, losses, rent, royalties, gifts, inheritance, capital gains, instalments and foreign tax credits. Separates personal business income from corporate income tax, routes wages and pension contributions to their current skills, and identifies the outdated donation label in the tax authority calculator. Use for annual PD or DI returns, IS or IL advances, self-employment, investment disposals, taxable transfers and income-tax reconciliation.
version: 0.2
jurisdiction: XK
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants skill License v1.0 (content)
---

# Kosovo personal income tax v0.2

Tax year **2026**. Checked against the law on **30 October 2026** (tier 2); no
licensed accountant has signed it off. The operative PIT law is
**05/L-028**, amended by **08/L-142**. The 2015 PDF's original four-band table
has been replaced; it is not the current rate schedule. 08/L-142 entered into
force on publication, 23 August 2024 (art. 7), and it is the only act amending
05/L-028 in the Official Gazette record.

## Who this applies to

Residents, non-resident individuals, personal business enterprises,
partnerships and associations receiving taxable income are within PIT Law
arts. 2–4. Resident individuals have a principal residence in Kosovo or are
physically present for 183 days in any twelve-month period. Resident personal
businesses/partnerships are established or effectively managed in Kosovo.
Residents are taxed on worldwide taxable income; non-residents on Kosovo-
source taxable income. Determine the source and applicable treaty rather
than using the bank-account location as the test ([05/L-028 arts. 2–4](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf)).

This skill covers ordinary individual income, sole-trader computation and
partnership allocation. Legal entities use
[xk-corporate-income-tax](xk-corporate-income-tax.md). Wages and pension
components use [kosovo-payroll](kosovo-payroll.md) and
[kosovo-social-contributions](kosovo-social-contributions.md). Their health-law
implementation gap remains relevant to a final payroll or contribution result.
Special mining depletion, legacy asset pools, special tax-holiday grants and
transaction-specific treaty relief require their additional instruments.

## Rates, bands and thresholds

Amounts are EUR; rates and thresholds below apply to 2026 unless stated.

| Item | Amount or rule | Official authority |
|---|---|---|
| Annual taxable income, first band | Up to EUR 3,000 inclusive: 0% | [08/L-142 art. 5, replacing PIT art. 6](https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360&langid=2) |
| Annual second band | Above EUR 3,000 to EUR 5,400 inclusive: 8% of excess over EUR 3,000 | [Replacement PIT art. 6(1.2)](https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360&langid=2) |
| Annual top band | Above EUR 5,400: EUR 192 plus 10% of excess over EUR 5,400 | [Replacement PIT art. 6(1.3)](https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360&langid=2) |
| Gross-method individual business boundary | Annual business gross income at most EUR 50,000, with no mandatory real-income status/election | [PIT arts. 32–34, 43(2.1)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Gross-method trade, transport, agriculture and similar business | 3% of quarterly gross receipts; minimum EUR 37.50 for a quarter with income | [PIT art. 43(2.1.1), (2.1.3)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Gross-method services, professions, crafts, entertainment and similar | 9% of quarterly gross receipts; minimum EUR 37.50 for a quarter with income | [PIT art. 43(2.1.2), (2.1.3)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Real-income business PIT | The 0%/8%/10% annual bands above, **not a flat 10% of profit** | [PIT arts. 6, 43(2.2)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [08/L-142 art. 5](https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360&langid=2) |
| Representation expense limit | 1% of annual gross income | [PIT art. 16(2)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Ordinary public-interest donation limit | 10% of taxable income before the donation deduction; qualifying recipients and proof required | [PIT art. 28(1)–(4)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Category 1 depreciation | 5% straight line, buildings/construction | [PIT art. 20(3.1), (4.1)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Category 2 depreciation | 20% straight line, specified vehicles, computers, office equipment and other listed assets | [PIT art. 20(3.2), (4.2)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Category 3 depreciation | 10% straight line, machinery and other listed/residual assets | [PIT art. 20(3.3), (4.3)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Low-value property | Up to EUR 1,000 currently expensed, except a component of a whole above that amount | [PIT art. 20(8)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Qualifying new/first-used Kosovo production assets | Additional 10% acquisition-cost deduction in first-use year | [PIT art. 22](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Loss carryforward | Up to six successive tax periods, oldest first; ownership/form restrictions apply | [PIT art. 26](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Non-business rent deemed cost option | 10% of gross rent; quarterly tax is 10% of the remaining base, less withholding | [PIT arts. 27, 44](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Interest/royalty withholding | 10%, subject to statutory exemptions and an applicable treaty | [PIT art. 39(1)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [AI 01/2016 art. 38](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233) |
| Rent withholding by an obliged payer | 9% of gross rent | [PIT art. 39(4)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Special-category withholding by a business natural person | 3% of gross payments to non-business farmers and collectors of recycling materials, berries, herbs and similar; WR by the 15th of the next month; certificate by 1 March | [PIT art. 40](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |
| Non-exempt resident gifts | Other-income inclusion where annual value exceeds EUR 5,000; specified family/education exemptions | [PIT art. 14(2)–(4)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |

Separate income-tax boundaries from VAT's registration test. A low turnover does
not establish exemption from pension, payroll or VAT obligations.

## The base

### Classify income and choose the correct business method

Gross income includes wages, rent, intangibles, interest, business income,
capital gains and other income. Apply the timing rules in arts. 7, 10 and 32:
non-business and eligible small-business receipts use actual/constructive
receipt; actual-income business items use accrual, subject to statutory
exceptions. Amounts available without substantial restriction are not postponed
merely because they were not withdrawn.

A sole trader at or below EUR 50,000 who has not elected real income uses the
3%/9% gross method. Separate activities and retain receipt records. Expenses
do not reduce a gross-method base. A quarter with no income has no income-tax
payment but still requires a zero return; this does **not** cancel the separate
self-employed pension minimum (PIT art. 43(2.1); Pension Funds Law art. 6(12)).

Above EUR 50,000, on the required status, or on a valid election, determine net
taxable income and apply the individual progressive bands. Partnerships and
groups must maintain the full books; allocate net profit/loss by the partnership
agreement to the partners, who make their own required advances. A partnership
is not automatically taxed like an incorporated company
([PIT arts. 32–34, 42–43](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf)).

An election/threshold transition binds the year and at least three following
tax periods. Existing taxpayers notify the election by 1 March; a new taxpayer's
first quarterly statement records it. Return to the small-business method
requires the elapsed period, turnover below the boundary and TAK approval by
1 March of the requested year. Do not switch retrospectively simply because
expenses increased ([PIT arts. 33(3)–(4), 43(3)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf)).

### Reconcile actual-income deductions, assets and losses

Start with income, deduct costs wholly, exclusively and directly related to
producing that income, then reconcile disallowances and capital allowances.
Keep documentary evidence. A withholding-related accrued expense unpaid by
31 March of the following period is deductible in its payment period rather
than the accrual year (PIT art. 15; AI art. 20).

| Adjustment | Treatment and article |
|---|---|
| Private costs, income tax, public-authority fines/penalty interest and recoverable VAT | Add back; PIT art. 30 |
| Representation versus advertising | Representation has the 1%-of-gross limit; genuine media advertising/promotion is fully deductible; art. 16 |
| Related-party wages, interest, rent and other charges | Deduct only open-market amount; art. 19 |
| Bad debts | Previously recorded income, no legal-validity dispute, collection evidence, at least six months overdue and no more than 24 months; judicial action except amounts at most EUR 500; issue the required **"Bad Debt" document for the uncollected amount referencing the original invoice**, supporting seller-income and purchaser-expense reduction; related/repeated-debtor restrictions; recoveries taxable; art. 17(1.6), (2)–(3) |
| Tangible assets | Exclude non-wasting land/art from depreciation; assign correct category, cost and first use; leasehold improvements over lease duration; art. 20 |
| Repairs/improvements | Capitalise qualifying life extension of at least a year where expenditure exceeds EUR 1,000; smaller repairs/improvements expense; art. 23 |
| Intangible assets | Straight-line over contractual useful life; where no term is defined, up to 20 years; art. 24 |
| Additional first-use deduction | Only the asset classes and new/first-use Kosovo conditions in art. 22; not a second deduction for a transferred existing Kosovo business asset |
| Donations | Qualifying public-interest recipient, payment proof and no direct donor/related-person benefit; ordinary 10% ceiling; extra relief requires the special law; art. 28 |
| Employee education | Direct payment to recognised institution, role-related, no new occupation and 24-month retention condition; job training separate; art. 29 |

The table is governed by [PIT arts. 15–30](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); detailed implementation is in
[AI 01/2016 arts. 20–32](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233). Do not treat the contribution sentence in
the English art. 30(2) translation as permission to deduct excess pension:
AI art. 32(2) lists pension/health contributions above the legal maximum as
unallowable. Reconcile allowable paid pension separately, without double
counting it in both operating costs and the annual pension-deduction line.
TAK's current PD24 layout includes the pension deduction, losses, withholdings
and instalment credits ([PD24 layout](https://crmm.atk-ks.org/en/Public/CalculatorDetail?id=35)).

Track loss vintages and prior use. Carry forward at most six successive periods,
oldest first, only for the business that created the loss. More than 50%
ownership change or conversion of a personal business into another legal form
ends the carryforward under art. 26(5). Do not transfer the loss to a new company.

### Other individual income and exclusions

Non-business rent has actual-cost records or the statutory 10% deemed-cost
option. Quarterly payment under art. 44 is 10% of the resulting base less rent
withholding. A property-letting business follows the business method; mixed
business/personal-property rent requires the allocation in AI art. 45. Royalties
received in an independent business belong to business income; otherwise the
intangible-income rules apply, with eligible direct costs and withholding
credits (PIT arts. 11–12, 15, 27, 39, 44–45; AI arts. 17–18, 45–46).

Capital gain is disposal proceeds/other consideration less documented
acquisition and improvement cost, reduced by prior allowed depreciation.
Related-party undervalue is adjusted to open-market value. AI art. 33(2)
provides an 80%-of-sale-value cost where cost is undocumented; this is not a
blanket 20% tax rate. Business capital gains/losses follow the business rules,
with legacy pools separately tested. Instalment gains are spread straight-line
over the enforceable agreement. Involuntary conversion has a two-year
same-character replacement condition; non-business public-interest
expropriation has its separate art. 8(1.20) exemption
([PIT arts. 8, 31](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [AI arts. 33–34](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233)).

Review art. 8 exclusions before taxing gross receipts: dividends received by
resident/non-resident persons; Kosovo government pensions/social assistance;
specified public-authority instrument interest; qualifying diplomatic/donor
income; medical/damage/death compensation; and qualifying family inheritances.
Spouse/child/parent inheritance is exempt; other heirs' inheritance is exempt
only within the statutory EUR 5,000 condition. Article 14 separately exempts
specified spouse/parent/child gifts regardless of value and tuition paid
directly to a recognised institution. A loan, gift or bank transfer needs its
actual evidence; the bank label is not an exemption. Conditions for subsidies,
grants, training and employer-paid education must be established
([PIT arts. 8, 13–14](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf)).

Wage PIT is calculated after employee pension deduction. Ordinary monthly
principal-employer bands correspond to the current annual bands; secondary
withholding is 10% of taxable wages. Government pensions are not the same as
Trust pension withdrawals: the latter have PIT withholding rules in art. 38
and AI art. 37(5). Use the payroll skill for the computation and certificate.

## Deadlines and filing

| Obligation | Deadline / current form | Official authority |
|---|---|---|
| Gross-method business tax/contribution | IS, by 15 April, 15 July, 15 October and 15 January after each quarter | [PIT art. 43](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [TAK timetable](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Actual-income business advances | IL/IL24, by the 15th following each quarter | [PIT art. 43](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [Current IL24](https://crmm.atk-ks.org/en/Public/CalculatorDetail?id=34) |
| Personal rent/intangible quarterly statement | IR, by the 15th following each quarter | [PIT arts. 44–45](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [TAK timetable](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Annual individual/business PIT and balance | PD/PD24 or DI as applicable, by 31 March following the year; 2026 balance by 31 March 2027 | [PIT arts. 46–48](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [TAK forms](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Partnership information return | DO, by 31 March following the year | [PIT art. 42(2)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [TAK timetable](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Wage/other source withholding | WM/CM or WR as applicable, by the 15th following the month | [PIT arts. 38–41](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [TAK timetable](https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/) |
| Real-income election / approved return to gross method | 1 March of the relevant year; new-business first-return election exception | [PIT art. 33(3)–(4)](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf) |

Use TAK EDI after obtaining the required registration. Every person carrying
on an economic activity also submits its purchase and sales books electronically:
monthly if VAT-registered, otherwise every three months (LB/LSH by the 15th after
the quarter); a missing book is fined under 08/L-257 art. 101(1)
([08/L-257 art. 43(3)–(4)](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf)). A filing date that falls on a
non-business day moves to the next business day (08/L-257 art. 13(7)). An error
found later is corrected by an amended declaration within three years of the
mandatory filing date, with any extra tax paid with it (08/L-257 art. 14(2), (5)). Full business records
include sales, purchases, cash diaries, capital/depreciation records and
necessary financial records. Gross-method businesses still keep minimum
sales, purchase and cash records (PIT arts. 33–34).

Actual-income advances use one-quarter of estimated annual progressive PIT
less relevant quarterly withholding, or the eligible previous-year 110%
method. The current IL24 confirms 110% of prior-year liability divided by four;
a prior-year loss disqualifies that method. Final annual tax deducts eligible
withholding, instalments and capped foreign credit. Refund/forward-credit
claims require the actual reconciliation (PIT art. 43(2.2), (4)–(7); art. 47).

The annual-return exceptions in art. 48(2) must be applied to the actual income
sources and withholding, not every person with a tax number. Wage-only fully
withheld income has the statutory exception; other income or unwithheld income
requires review. Capital gains, taxable gifts and other art. 46 income are
reconciled annually. Do not skip a required quarterly return just because no
income-tax payment arises.

**Source conflict:** the publicly accessible PD/PD24 calculator labels its
charity field "5%". PIT art. 28 sets the ordinary ceiling at **10%**. Apply the
statute, document the correct computation and resolve the filing treatment;
do not import that outdated calculator label as the current law.

## Penalties and interest

Use current procedure Law 08/L-257. Article 99 charges EUR 50 per missed
mandatory liability-producing return for business natural persons, EUR 20 for
non-business natural persons and EUR 150 for legal entities. Article 100(1)
charges 15% of an understatement difference at most 10% of correct tax and
25% where it exceeds 10%; art. 100(4) excludes overlapping art. 101 penalties
in the specified cases. Failure to withhold/pay over tax or pension has its
25%-of-shortfall rule in art. 103
([08/L-257 arts. 99–103](https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf)).

Article 24 accrues interest by month or part-month, for at most ten years, at
the Minister's rate published by TAK; the law requires that rate to be higher
than commercial bank lending rates in Kosovo (art. 24(3)). A compliant instalment agreement stops
interest from the following month; default reinstates it. Do not use an old late-filing percentage or a
commercial-debt reference rate as current tax interest.

PIT art. 43(7) separately governs inadequate business advances, including the
20% difference tolerance, eligible prior-year payment protection, prior-year
assessment-adjustment restriction and first-year cumulative payment rule.
Check its conditions before calculating an advance shortfall penalty; do not
add a generic monthly fine to every difference.

## Cross-border points

Test resident worldwide income and non-resident Kosovo-source income first.
A foreign customer or bank account does not remove business income from a
resident's return. Under PIT arts. 36 and 47, foreign income tax on income also
taxed in Kosovo is creditable only up to Kosovo tax on the same income; an
applicable in-force treaty governs its own relief. AI art. 36 requires foreign
authority evidence translated and notarised in Kosovo. Do not claim a foreign
VAT, pension or unrelated-country charge as income-tax credit
([PIT arts. 4, 36, 47](https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf); [AI art. 36](https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233)).

A personal-business related-party adjustment follows PIT art. 35's open-market
rule and stated method sequence. Do not automatically replace it with the
corporate statute's best-method wording. The cross-border and transfer-pricing
skills address the related corporate framework and nonresident withholding.

Actual asset sales remain subject to art. 31, and entity/form changes can
forfeit losses under art. 26(5). These provisions do not alone prove either a
universal residence-departure tax or its absence. A proposed migration or asset
transfer needs the relevant exit/cessation provisions and treaty evidence.

## Two worked examples that recompute

### 1. Small service business, quarterly gross method

Assume a sole trader within the EUR 50,000 annual boundary, no real-income
election/mandatory status, service receipts EUR 4,000 for the quarter and no
withholding. PIT is 9% × EUR 4,000 = EUR 360, above the EUR 37.50 minimum.
Assume the following quarter has zero receipts: its income-tax payment is zero,
but a zero return and separate pension review remain required. Business costs
do not reduce this gross-method computation.

```oa-check
name: Kosovo small service business positive and zero-income quarters
inputs:
  service_receipts: 4000
  zero_quarter_receipts: 0
steps:
  - positive_quarter_pit: max(37.50, service_receipts * 0.09)
  - zero_quarter_pit: zero_quarter_receipts * 0.09
expected:
  positive_quarter_pit: 360
  zero_quarter_pit: 0
```

### 2. Actual-income owner with paid pension and brought-forward loss

Assume annual business receipts EUR 80,000, allowable operating costs EUR
40,000, allowable paid owner pension EUR 2,400 not already in those costs,
and an unused eligible loss EUR 6,000 from the same unchanged business within
the six-year period. No other income, donation or foreign tax credit applies;
any applicable health expense is already reconciled in the allowable costs.
Taxable income is EUR 31,600. PIT is EUR 192 plus 10% of EUR 26,200 =
EUR 2,812. With EUR 2,000 instalments and no withholding the balance is EUR
812. A flat 10% of the taxable amount would incorrectly give EUR 3,160.

```oa-check
name: Kosovo actual-income progressive PIT with pension and eligible loss
inputs:
  annual_receipts: 80000
  allowable_operating_costs: 40000
  paid_allowable_owner_pension: 2400
  eligible_loss: 6000
  instalments: 2000
steps:
  - business_net: annual_receipts - allowable_operating_costs
  - before_loss: business_net - paid_allowable_owner_pension
  - loss_used: min(eligible_loss, max(0, before_loss))
  - taxable_income: max(0, before_loss - loss_used)
  - middle_band: max(0, min(taxable_income, 5400) - 3000) * 0.08
  - top_band: max(0, taxable_income - 5400) * 0.10
  - annual_pit: middle_band + top_band
  - balance_due: annual_pit - instalments
expected:
  business_net: 40000
  before_loss: 37600
  loss_used: 6000
  taxable_income: 31600
  annual_pit: 2812
  balance_due: 812
```

## Ask the client first

1. What are the residence, days, work/property locations, foreign income and treaty position for the relevant period?
2. What business form, annual gross receipts, activities, real-income election and prior mandatory-method history apply?
3. Which wage, rent, interest, royalty, disposal, gift, inheritance and pension receipts exist, and what was withheld?
4. What records support actual costs, asset basis/first use, paid pension, health treatment, donations and related-party amounts?
5. What loss vintages, ownership or legal-form changes, prior-year tax and instalments must be reconciled?
6. Which registrations, returns, payment evidence and foreign authority credit certificates are available or outstanding?

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| PIT Law 05/L-028 arts. 2–48; use the replacement art. 6 below | https://www.atk-ks.org/wp-content/uploads/2017/07/LAW_NO._05_L_-028__ON_PERSONAL_INCOME_TAX.pdf | 2026-10-30 |
| Law 08/L-142 art. 5, current progressive PIT bands | https://gzk.rks-gov.net/ActDetail.aspx?ActID=96360&langid=2 | 2026-10-30 |
| PIT AI 01/2016 arts. 14–20, 26–38, 44–48 | https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=12233 | 2026-10-30 |
| Current tax-procedure Law 08/L-257 arts. 13–14, 24, 43, 99–103 | https://www.atk-ks.org/wp-content/uploads/2024/01/LAW_NO._08_L-257_ON_THE_ADMINISTRATION_OF_TAX_PROCEDURES.pdf | 2026-10-30 |
| TAK current rates and forms timetable, read in ordinary browser | https://www.atk-ks.org/en/portfolio/informata-te-pergjithshme-per-tatimet-ne-kosove/ | 2026-10-30 |
| TAK IL24 layout, 110% prior-year option and pension base | https://crmm.atk-ks.org/en/Public/CalculatorDetail?id=34 | 2026-10-30 |
| TAK PD24 layout; donation label conflict identified above | https://crmm.atk-ks.org/en/Public/CalculatorDetail?id=35 | 2026-10-30 |
| Pension Funds Law 04/L-101 art. 6(12) | https://bqk-kos.org/wp-content/uploads/2024/11/Law-on-Pension-Funds.pdf?lang=en | 2026-10-30 |
| Pension amendment 04/L-168 art. 3 | https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=8655 | 2026-10-30 |

| Gazette record of 05/L-028: 08/L-142 is the only amending act | https://gzk.rks-gov.net/ActDetail.aspx?ActID=11014&langid=2 | 2026-10-30 |

Not yet confirmed: numeric 2026 tax late-interest rate; filing treatment of the PD24 donation-field conflict; case-specific residence exit/cessation treatment; operative health phase for a final payroll/contribution result.

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
