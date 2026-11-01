---
name: fo-individual-income-tax
description: >
  Prepare 2026 Faroese personal-tax working papers for employees, sole traders
  and investors. Establish residence, separate A-income from B-income and
  investment income, reconcile business expenses and pension deductions, and
  compute national and municipal tax, family credits and the statutory income-tax
  ceiling. Check the separate capital-income calculation, housing-interest
  support, rental election, preliminary payments and annual settlement. Use for
  Faroese personal income tax, self-employed profit, child tax credits, private
  investments, foreign work and individual tax returns. Shipping, part-year
  credits, treaty relief, benefits and specified implementation questions
  require additional work identified in Sources. This is tier-2 material
  accepted for partial draft publication after independent AI review; professional
  attestation remains pending.
jurisdiction: FO
category: international
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: "0.5"
verified_by: pending
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Faroe Islands individual income tax v0.5

> **Checked against the law.** This Guide prepares income-year 2026 working papers. Selected current law and authority tables were read on 25 October 2026, with the church-tax, spouse and bounded part-year methods checked on 28 October; professional review is pending.

## Who this applies to

Faroese domestic full liability arises from a home under Tax Act §1(1)(1), or, without a home, a stay of at least **180 days in a twelve-month period**, interrupted or not, under §1(1)(4). Exactly 180 meets that stay test; fewer days do not disprove the separate home test. Other statutory routes include specified students/apprentices abroad and seafarers. Determine commencement/cessation and treaty residence separately. Fully liable persons start with worldwide income under §25; nonresidents are limited to §2 categories. [Tax Act §§1–2, 25][tax]

Employees, sole traders, partners, investors and landlords require different schedules. Spouses are individually assessed under §4; allocate a joint business by actual participation and spouse remuneration by actual work. The municipal allowance equalisation in §4(1) is not general joint national-rate taxation. Children are separately taxable subject to §5's family-business wage and gifted-asset-income rules. [Tax Act §§4–5][tax]

Do not import Danish tax bands, an automatic 183-day exemption or a universal net-pay percentage. Pensions, social charges and separate capital tax require their own bases.

## Rates, bands and thresholds

National tax on established annual ordinary taxable income `I`, in DKK:

| Income interval | National tax formula | Tax year / official source |
|---|---|---|
| Below 65,000 | 0 | 2026; [Assessment Act §1(1)(1)](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |
| 65,000 to below 180,000 | 13% × (I − 65,000) | 2026; [§1(1)(2)](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |
| 180,000 to below 330,000 | 14,950 + 15% × (I − 180,000) | 2026; [§1(1)(3)](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |
| 330,000 to below 450,000 | 37,450 + 20% × (I − 330,000) | 2026; [§1(1)(4)](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |
| 450,000 to below 600,000 | 61,450 + 25% × (I − 450,000) | 2026; [§1(1)(5)](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |
| At least 600,000 | 98,950 + 30% × (I − 600,000) | 2026; [§1(1)(6)](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |

[TAKS's dated 2026 table][national] confirms those amounts. Adjacent formulas agree at the boundaries; no step tax is imposed on the whole income.

| Other item | Rule | Tax year / official source |
|---|---|---|
| Municipal exempt amount | First DKK 30,000 of the statutory ordinary base | 2026; [Tax Act §46](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) |
| Municipal rate / child credit | Exact municipality row; Tórshavnar 19% and DKK 9,000 per qualifying child | 2026; [TAKS municipal table](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/talva-yvir-kommunuskatt-kirkjuskatt-og-barnafradratt); [Tax Act §§46–47](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) |
| Church tax | Members only; Tórshavn/Ternuryggur 0.85%, Argir/Borðan/Nólsoy 0.90%; check exact locality footnotes elsewhere | 2026; [TAKS table, footnote 8](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/talva-yvir-kommunuskatt-kirkjuskatt-og-barnafradratt) |
| National child credit | DKK 10,700 if child under 7 on 1 January; DKK 7,500 if 7–17 | 2026; [Assessment Act §2](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |
| Specified pensioner national credit | Married DKK 10,500 / single DKK 16,200 for specified early/disability pensions; old-age pension credit up to DKK 6,000 | 2026; [Assessment Act §3](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |
| National/municipal/church income-tax ceiling | 50% of statutory taxable income; proportional reduction of the excess | 2026; [Tax Act §54(2)](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) |
| Separate individual capital tax | 35% of positive §14 net gain | 2026; [Capital Income Act §14](https://logir.fo/Logtingslog/164-fra-21-12-2001-um-skatting-av-kapitalvinningi-sum-seinast-broytt-vid-logtingslog-nr-173) |
| Eligible housing-interest support | 35% of qualifying interest; ordinary own-home interest base capped at DKK 100,000 per property, not per co-owner | 2026; [Interest Support Act §§3, 5](https://logir.fo/Logtingslog/148-fra-30-12-1996-um-studul-til-rentuutreidslur-av-lanum-sum-seinast-broytt-vid-logtingslog) |
| Qualifying residential gross-rental election | 25% above combined DKK 100,000 annual allowance; three-year binding election | 2026; [Assessment Act §8a](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |
| Specified limited-tax-liability A-income-only workers | 42% gross; qualifying FAS-equivalent shipping 35% under the stated tests | 2026; [Assessment Act §8(1)](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) |

## The base

### Ordinary income and deductions

Build separate schedules for wages/benefits, business profit, rents, foreign income and investments. Use the payroll Guide’s [dated 2026 benefit-value schedule](fo-payroll-contributions.md#ordinary-benefit-valuation) for ordinary housing, utilities, meals and cars, with its stated adjustment/exemption limits. A/B classification determines collection, not a new exemption. Tax Act §§57, 60–62 define the routes; doubt about classification is decided by TAKS under §62(2). Ordinary wage/A-income timing generally follows payment, with §28's backstop at the end of the following calendar year and acceleration when liability ceases. [Tax Act §§25, 28, 57, 60–62][tax]

For business profit, reconcile sales and expenses, remove private withdrawals/use, correct inventory and replace accounting depreciation with the statutory asset schedule. Section 31 permits expenses incurred to earn, secure and maintain business income but expressly excludes ordinary expenses of earning A-income/personal employment income. Do not deduct an employee's ordinary work costs as sole-trader costs. Business interest/finance costs follow §33(1)(1), including its unpaid-interest clawback. Pre-trading research expenditure has the separate §32 start-year/next-three-years rule. Carry business losses under §33a only when not usable earlier; debt-release loss reductions must be applied. [Tax Act §§26, 31–33a][tax]

Equipment depreciation requires the Depreciation Act classification, pool, disposal and private-use rules. The ordinary exclusive-business pool maximum is 30%; qualifying items or positive pool remainders of DKK 20,000 or less have separate immediate-deduction rules. Keep the underlying asset evidence; the corporate Guide's [asset schedules](fo-corporate-income-tax.md) explain these shared provisions, without applying its company rate to a person. [Depreciation Act §§1–8][depreciation]

Before finalising an individual's depreciation or investment-fund deduction, apply Tax Act §31(2)–(6)'s separate **personal-consumption floor**. If taxable income is below the statutory consumption computation, increase income toward that amount, but by no more than the depreciation/investment-fund deductions covered by the rule. Section 31(4) excludes year-bound depreciation that would otherwise be lost. Under §31(5), the denied depreciation is treated as not taken in that year; preserve it in the asset records instead of losing it or deducting it twice. For spouses, the statutory consumption calculation includes both spouses' full-year income and opening/closing assets and liabilities. This floor is distinct from an asset's private-use adjustment. Obtain the actual consumption working paper before confirming the base. [Tax Act §31(2)–(6)][tax]

Regulation 98/1987 §1 gives the ordinary indirect consumption calculation: opening net assets plus taxable income, asset increases outside taxable income, deductions that did not reduce assets and nontaxable valuation increases; subtract non-consumption asset reductions not deducted in arriving at income, taxable income that did not increase assets, nondeductible valuation decreases and closing net assets. Reconcile each component. A direct calculation is permitted where acceptable annual accounts include all income/expenses and opening/closing assets/liabilities. Apply §2's particular spouse, separation and death rules rather than mechanically combining every household. [Regulation 98/1987 §§1–3][consumption]

Eligible paid pension contributions have deduction/exclusion under Pension Act §12(3)–(4) in the year contributed, including the specified voluntary payments. Do not deduct the same payment twice. The pension contribution itself has a separate pension tax under §12(2)/annex 1, with provisional 40% withholding and final income-linked rates; a personal income-tax deduction does not make the pension payment tax-free. Mandatory contribution funding, exceptions and collection are in the [payroll Guide](fo-payroll-contributions.md). [Pension Act §§2, 12 and annex 1][pension]

### Family, municipality and ceiling

For a full-year cohabiting spouse case under §4, first establish each spouse's own taxable income. Where the lower nonnegative income is below DKK 30,000 and the other is above it, the ordinary adjustment transfers the unused amount: `transfer = 30,000 − lower income`; raise the lower income to DKK 30,000 and reduce the higher income by that transfer. TAKS expressly illustrates DKK 20,000 / 300,000 becoming DKK 30,000 / 290,000, and DKK 0 / 300,000 becoming DKK 30,000 / 270,000, automatically at year-end. Keep the spouses separately assessed on the adjusted bases. This bounded method does not settle negative-income, separation, death or part-year spouse cases. [Tax Act §4][tax]; [TAKS spouse adjustment][spouse]

For national child credit, establish full liability, required residence, custody/child's home, child age on 1 January and child's Faroese residence or retained full liability while studying abroad. Apply the recipient/transfer rules and proportional reduction where the recipient's liability covers only part of the year. A child taken into statutory care ends entitlement. The credit reduces tax, not taxable income; an excess is refundable under §2(3). [Assessment Act §2][rate]

Determine the tax municipality under §§41–44, ordinarily residence on 1 December before the income year, with commencement/move rules. Apply the current municipal child credit separately from the national amount. TAKS explains the written agreement/preliminary-registration process for transferring or sharing eligible credit and the refund treatment where credit exceeds tax. Preserve the actual allocation rather than giving both parents the full credit. Pensioner national credits have separate eligibility under Assessment Act §3; unused credit transfers to municipal tax only up to that tax under Tax Act §47(2). [Tax Act §§41–47][tax]; [Assessment Act §§2–3][rate]; [TAKS child credit][child]

For municipal calculation, §47 directs rounding taxable income down to a multiple of DKK 100 before computing the tax. Keep that rounding distinct from payment rounding. Compute each national/municipal/church component, eligible credits and the §54(2) proportional ceiling adjustment in a traceable schedule. The ceiling does not establish a 50% limit on every tax, contribution and pension outflow together. Use the bounded part-year method below; unusual credit/ceiling interactions require the additional checks listed in Sources. [Tax Act §§24(2), 46–47, 54(2)][tax]

For an ordinary full-year church member, calculate church tax on the ordinary municipal income base **after the DKK 30,000 exempt amount**, using the actual parish rate. Church Finance Act §§11–13 separates national and local church rates and uses the municipal collection rules. The official 2024 audit report expressly confirms that TAKS calculates church tax in the same way as municipal tax, deducting the municipal exempt amount first. Read with Tax Act §§46–47, the working-paper base is `max(income rounded down to DKK 100 − 30,000, 0)`. Apply the church rate to that base separately; a municipal child credit does not reduce the base. The report also records the Finance Ministry's explanation that the special 42%/35% limited-liability gross levy does not attract an additional church charge. This full-year method does not settle changes of membership during a year, part-year allowances or final sub-krone settlement rounding. [Church Finance Act §§11–14][church]; [Tax Act §§46–47][tax]; [Landsgrannskoðanin, 2024 report §4.10, pp. 44–46][church-audit]; [2026 parish rates][municipal]

### Ordinary arrival and departure during the year

Liability continues while the statutory residence/source conditions are met. Acquiring a home without actually taking up residence does not itself start the home-based route; the 180-day stay route instead starts retrospectively from the first qualifying arrival. Preserve the actual home, arrival/departure and presence evidence. A registration date alone does not decide tax residence. A home retained after departure requires the actual facts to be assessed. [Tax Act §§1, 6–8][tax]; [TAKS VLS C.1][residence]

For a bounded 2026 ordinary resident period with no credits, church membership, foreign relief, spouse transfer or special-rate income, §24(2) requires conversion to full-year income. The TAKS 2026 calculator demonstrates the administrative sequence: actual taxable income × `365 / taxable days`, rounded down to DKK 100; compute the current full-year national and municipal taxes on that annualised base, then multiply their sum by `taxable days / 365`. The municipal exempt amount is applied in the annual calculation before this reduction. Treat this as the observed calculator working-paper method, not an express statutory rounding rule for every component. [Tax Act §§24(2), 46–47][tax]; [TAKS calculator guidance][calculator-info]; [TAKS 2026 calculator][calculator]

**Observed control, not a client assessment:** for DKK 150,000 income over 180 taxable days in Tórshavn, without church tax or any credit, the official calculator shows annualised income DKK 304,100, gross annual tax DKK 85,644 and reduced tax DKK 42,235.40; its final income-tax display is DKK 42,235. The unrounded annual equivalent is DKK 304,166.67. This recomputes as national DKK 33,565 plus municipal DKK 52,079, then ×180/365. Its separately displayed 3% AM charge is DKK 4,500 on actual income. The calculator is expressly indicative. Its displayed child-credit amount differs from the current Assessment Act, so no child-credit result is adopted from it. Part-year credits, spouse cases, changing church membership and final settlement rounding remain separate questions. [Assessment Act §§1–2][rate]; [TAKS calculator][calculator]

### Capital income, rentals and interest support

Separate non-business securities/claims/debt/options/dividends/interest under the Capital Income Act. Securities gains generally use realised proceeds less acquisition basis and FIFO for equal-right shares; business-related investments instead follow §3's ordinary-income route, subject to its irrevocable mark-to-market election. For individuals, §6(4)'s DKK 1,000 annual claim/debt-gain threshold and listed-instrument loss condition are specific rules, not a general allowance against all share gains. Private interest income enters the separate §14 computation under §10, subject to express exemptions. [Capital Income Act §§1, 3–10][capital]

Aggregate eligible §14 categories, carry unused capital losses to the earliest available future capital net gains, and apply 35% to a positive balance. Do not deduct a private capital loss against salary. Reconcile dividend/bank-interest withholding and the separate assessment under §§15–18 instead of taxing the same receipt twice. Pension-scheme investments excluded by §1(5) are not an ordinary private portfolio. Gifts, inheritance and family succession have separate §§11–13 rules. [Capital Income Act §§1, 11–18][capital]

Residential rent can follow ordinary accounts or the §8a gross election. The DKK 100,000 allowance is combined where there are co-owners, and the election binds for three years. TAKS requires qualifying direct residential letting for at least three months with the tenant actually resident; do not extend the election to short-stay tourism. Ordinary rental accounts require their own expense and asset schedules. [Assessment Act §8a][rate]; [TAKS housing/rents][rent]

For personal housing/student/other specified borrowing, the separate Interest Support Act supplies relief instead of a general private-interest deduction. Establish full liability and the actual loan purpose/date, qualifying own home and ownership. Home support is capped per property and commissions are excluded. Mixed home/business property is expressly treated under this Act by §2a; mixed-purpose loans must first be split. Negative loan interest reduces eligible expense, and double reimbursement is prohibited. Apply on the required form with bank evidence; the ordinary own-home formula is min(eligible interest, 100,000) × 35%, subject to all eligibility rules. Student loans and older borrowing do not automatically share that property cap. [Interest Support Act §§1–8][support]

### Special work categories

Screen foreign-work §25b income and its exclusions before applying Assessment Act §1(2)'s 35% route. For 2026, Tax Act §33(1)(13) allows its 30% deduction capped at DKK 48,000, subject to §33(2)'s transitional maximum DKK 96,000 for the stated 2024 Nordic-relief population. The distinct foreign-work expense allowance under §33(1)(12) is DKK 120 per qualifying day in 2026, with its two-continuous-month/100-day stay tests and income cap; do not stack it onto excluded §25b income. [Tax Act §§25b, 33(1)(12)–(13), (2)][tax]; [Assessment Act §1(2)][rate]

The statutory fishing-income deduction is 14% of qualifying catch income up to DKK 300,000 under §33(1)(17). Qualifying apprentices have up to DKK 50,000 annual deduction, proportional to qualifying days, under §33(1)(19); an ordinary student internship is not an apprenticeship. FAS/DIS, frontier work, overseas public service and treaty exemptions still require their own facts and authority. [Tax Act §33(1)(17), (19)][tax]

## Deadlines and filing

Ordinary individual returns are due **1 May following the income year**, subject to the specified §100(3) exceptions, including its §2 nonresident category deadline. A correct and complete issued statement can remove the separate return requirement under §101(2); an absent form does not. A permitted extension cannot pass **15 August** under §105. Self-employed accounts and the applicable property statement accompany filing, with accounts submitted on Borgaragluggin. For ordinary calendar-year 2026 resident filing, the starting date is 1 May 2027; verify the actual issued assessment and any extension. [Tax Act §§100–105][tax]; [TAKS returns][returns]

Update preliminary registration where expected income changes. B-tax is ordinarily due on the first of each month, payable through the 20th, with weekend/public-holiday extension; if annual B-tax is **below** DKK 1,000, two instalments fall on 1 June and 1 December under §74. Extra voluntary preliminary payment can be made by **31 January** of the assessment year under §76. [Tax Act §§67–76][tax]

Reconcile final tax with A/B and voluntary payments under §77. Ordinary residual tax carries a **4% supplement**; the usual assessed schedule is three equal instalments due 1 May/June/July, payable through the 20th, with the small-balance and later-issued assessment rules in §78. A balance including supplement of DKK 100 or less is not collected; DKK 1,000 or less uses the specified single-instalment route. Follow the actual assessment rather than inventing monthly deductions after year-end. [Tax Act §§77–80][tax]

Separate capital reporting follows §18 and the applicable ordinary return deadline; a correct complete issued capital statement needs no additional form. Capital residual tax of DKK 500 or less is not collected and refunds below DKK 50 are not paid. Those are settlement thresholds, not investment-gain exemptions. Tax is due the first of the month after assessment, payable through the 20th. [Capital Income Act §18][capital]

## Penalties and interest

A missing/late complete ordinary return permits estimated assessment, a DKK 1,000–5,000 fine, and tax increases of 2% if less than seven days late or 5% if at least seven days late. Section 104(3) permits relief on supported application, not automatically. Late tax/preliminary tax carries **0.7% per commenced month** from the due date under §135. Separate capital-return/payment rules are in Capital Income Act §18, including the corresponding late-return fine/increases and 0.7% monthly payment interest. [Tax Act §§104, 135][tax]; [Capital Income Act §18][capital]

False/misleading information with evasion intent is subject to Tax Act §139 fine, detention or up to two years' imprisonment, with separate gross-negligence treatment. Sections 139a–141 cover specified statement corrections, nonfiling and information/control failures. No fixed offence fine is invented here. Distinguish the §78 residual-tax supplement from late-payment interest or an offence penalty. [Tax Act §§78, 139–141][tax]

## Cross-border points

Classify domestic versus treaty residence, work location, payer, actual days, income article and relief evidence. The 42% A-income-only nonresident rule does not govern every foreign person's Faroese property/business income. A stay below 180 days does not itself prove treaty exemption. Tax Act §1(3) restricts deductions for a treaty-foreign resident to expenses concerning income the Faroes may tax. [Tax Act §§1–2][tax]; [Assessment Act §§1, 8][rate]

Capital Income Act §19 permits capped foreign-tax credit for capital income from a country **without** a double-tax treaty. Tax Act §154 supplies the separate ordinary-income credit; the [cross-border Guide’s bounded method](fo-cross-border-payments.md#ordinary-foreign-tax-credit) explains source expenses, the positive-base fraction and credit ordering. Treaty credits/exemptions, nonpositive bases and the other stated limits require their own authority; do not use §19 as a universal credit rule. Individual securities departure/entry and deferral are covered in the [cross-border Guide](fo-cross-border-payments.md). [Capital Income Act §§2a–2f, 19][capital]


[Church calculation and its supporting arithmetic](../../../ledgers/faroe-islands-2026-evidence/fo-individual-income-tax-supplementary-controls.md) is retained in supplementary research.

## Two worked examples that recompute

### 1. Ordinary full-year resident

Assume a full-year adult resident in Tórshavnar, no church membership, child/pensioner credit or special income, and established ordinary taxable income DKK 300,000 after base adjustments. National tax is DKK 32,950 and municipal tax DKK 51,300, total DKK 84,250. This is income tax, not take-home pay or total pension/social charges. [Assessment Act §1][rate]; [Tax Act §46][tax]; [2026 municipality row][municipal]

```oa-check
name: Faroese ordinary full-year resident income tax
inputs:
  base: 300000
steps:
  national: 14950 + (base - 180000) * 0.15
  municipal: (base - 30000) * 0.19
  income_tax: national + municipal
expected:
  national: 32950
  municipal: 51300
  income_tax: 84250
```

### 2. Sole trader, child credit and private investments

Assume a full-year eligible non-church Tórshavnar resident, with DKK 600,000 business revenue, DKK 260,000 deductible non-private costs, and an ordinary exclusive-business opening equipment pool DKK 200,000 with no additions/disposals. Electing 30% depreciation gives DKK 60,000. An independently eligible DKK 40,000 pension payment made in 2026 is deducted once, leaving ordinary income DKK 240,000. Assume the independently verified statutory personal-consumption computation is DKK 200,000, so the §31 floor requires no increase; this is a case input, not a statutory fixed allowance. The resident is the sole eligible recipient of the full-year credits for one child aged five on 1 January. National tax DKK 23,950 less DKK 10,700 credit is DKK 13,250; municipal DKK 39,900 less DKK 9,000 is DKK 30,900. Separate non-business share gains DKK 40,000, fully eligible share loss DKK 5,000 and bank interest DKK 5,000 give DKK 40,000 capital net gain and DKK 14,000 capital tax. Combined ordinary/capital income tax is DKK 58,150, before withholding credits. Pension contribution tax and social charges are separate. Assume no prior capital losses, foreign credit, private-use adjustment, special regime or other deduction. [Tax Act §§31, 46][tax]; [Assessment Act §§1–2][rate]; [Pension Act §12][pension]; [Depreciation Act §2][depreciation]; [Capital Income Act §§4, 10, 14][capital]; [municipal row][municipal]

```oa-check
name: Faroese sole trader deductions credits and separate capital result
inputs:
  revenue: 600000
  costs: 260000
  equipment_pool: 200000
  depreciation_rate: 0.30
  eligible_paid_pension: 40000
  verified_personal_consumption: 200000
  national_child_credit: 10700
  municipal_child_credit: 9000
  share_gain: 40000
  eligible_share_loss: 5000
  bank_interest: 5000
steps:
  depreciation: equipment_pool * depreciation_rate
  base_before_consumption_floor: revenue - costs - depreciation - eligible_paid_pension
  consumption_floor_increase: min(max(verified_personal_consumption - base_before_consumption_floor, 0), depreciation)
  ordinary_base: base_before_consumption_floor + consumption_floor_increase
  national_before_credit: 14950 + (ordinary_base - 180000) * 0.15
  municipal_before_credit: (floor(ordinary_base / 100) * 100 - 30000) * 0.19
  national_tax: national_before_credit - national_child_credit
  municipal_tax: municipal_before_credit - municipal_child_credit
  capital_net: share_gain - eligible_share_loss + bank_interest
  capital_tax: capital_net * 0.35
  income_tax: national_tax + municipal_tax + capital_tax
expected:
  depreciation: 60000
  consumption_floor_increase: 0
  ordinary_base: 240000
  national_before_credit: 23950
  municipal_before_credit: 39900
  national_tax: 13250
  municipal_tax: 30900
  capital_net: 40000
  capital_tax: 14000
  income_tax: 58150
```

## Ask the client first

- Where was the home, tax residence and actual presence, with dates of arrival, departure and any municipality move?
- Which receipts are employment, business, rental, pension, investment or foreign-work income, and what was paid/withheld when?
- What costs, asset registers, private use, carried losses and pension payments support the ordinary base?
- What are the children's ages on 1 January, custody/home/residence, credit allocation and relevant pensioner status?
- Which securities, acquisition bases, bank-interest statements, foreign taxes and migration events need a separate capital schedule?
- What preliminary registrations, final statements, returns, extension decisions, loan-support approvals and payment receipts exist?

## Sources

| Source | Provisions / purpose | Read on |
|---|---|---|
| [Current Tax Act](https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt) | §§1–5, 24–34, 41–47, 54, 57–80, 100–105, 135, 139–141; selected personal-tax provisions | 2026-10-25 |
| [Assessment Act](https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170) | §§1–3, 8–8a; bands, credits, special categories and rental election | 2026-10-25 |
| [Capital Income Act](https://logir.fo/Logtingslog/164-fra-21-12-2001-um-skatting-av-kapitalvinningi-sum-seinast-broytt-vid-logtingslog-nr-173) | §§1–19, selected ordinary/private classification and individual computation provisions | 2026-10-25 |
| [Regulation 98/1987](https://logir.fo/Kunngerd/98-fra-14-12-1987-um-uppgerd-av-skattligu-eginnytsluni) | §§1–3; statutory personal-consumption working paper and household cases | 2026-10-25 |
| [Depreciation Act](https://logir.fo/Logtingslog/52-fra-29-12-1971-um-skattligar-avskrivingar-vm-sum-seinast-broytt-vid-logtingslog-nr-174) | §§1–8; equipment deduction used in the example | 2026-10-25 |
| [Pension Act](https://logir.fo/Logtingslog/49-fra-14-05-2013-um-eftirlonarsamansparing-og-skatt-af-eftirlon-og-rentutryggingum) | §§1–3, 12, 17, annex 1; eligible paid contributions and separate pension taxation | 2026-10-25 |
| [Interest Support Act](https://logir.fo/Logtingslog/148-fra-30-12-1996-um-studul-til-rentuutreidslur-av-lanum-sum-seinast-broytt-vid-logtingslog) | §§1–8; loan purposes, property cap, rate and application | 2026-10-25 |
| [TAKS 2026 national table](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/talva-yvir-landsskatt) | Cross-check statutory bands | 2026-10-25 |
| [TAKS 2026 municipal/church/child table](https://www.taks.fo/fo/borgari/gjoeld-og-agodar/talva-yvir-kommunuskatt-kirkjuskatt-og-barnafradratt) | Current municipality rates, credits and locality footnotes | 2026-10-25 |
| [TAKS child credit](https://www.taks.fo/fo/borgari/fradrattur/barnafradrattur) | Allocation/application/refund procedure | 2026-10-25 |
| [Church Finance Act](https://logir.fo/Logtingslog/61-fra-07-06-2007-um-figgjarvidurskifti-folkakirkjunnar) | §§11–15; membership, national/local church tax and municipal collection rules | 2026-10-28 |
| [Landsgrannskoðanin 2024 annual report](https://lg.fo/download/file/f3e290b4e758ae966b65955f9beb36e8c540831d.pdf) | §4.10, pp. 44–46; TAKS's actual church-tax base and limited-liability explanation | 2026-10-28 |
| [TAKS spouse adjustment](https://www.taks.fo/fo/borgari/fradrattur/hjunafradrattur) | Explicit full-year 0/300,000 and 20,000/300,000 adjustment examples; Tax Act §4 checked with them | 2026-10-28 |
| [TAKS VLS C.1](https://www.taks.fo/fo/log/vegleidingarskriv-vls-2015/c-subjektiv-skattskylda-likamligir-personar-tviskatting) | Selected residence commencement/cessation discussion, cross-checked against current §§6–8; obsolete examples excluded | 2026-10-28 |
| [TAKS calculator](https://www.eskatt.fo/sjtp/sjtpsim.aspx) and [guidance](https://www.taks.fo/fo/borgari/skattur/skattaroknarin) | Actual 2026 synthetic no-credit/no-church 365-day and 180-day runs at DKK 150,000; indicative observed method, child-credit display excluded | 2026-10-28 |
| [TAKS housing/rents](https://www.taks.fo/fo/borgari/skattur/skattur-og-husaleiga) | Gross-rental eligibility and ordinary-accounts distinction | 2026-10-25 |
| [TAKS return procedure](https://www.taks.fo/en/individuals/tax/tax-return) | Statements, accounts, returns and extensions | 2026-10-25 |

Not yet confirmed: part-year credit and spouse adjustments beyond the bounded no-credit calculator method, part-year or membership-change church calculations and final sub-krone settlement rounding, unusual ceiling/credit interaction, benefit part-year/payment adjustments and full exemption implementation, foreign-credit nonpositive bases, tax changes, unused-credit treatment and treaty relief, all overseas/shipping worker computations, special business/asset regimes, detailed loan-support filing and foreign-loan evidence rules. Separate travel/double-household support regimes need applicability review. Those are remaining ordinary/special-case gaps, not exemptions; the personal-tax domain remains partial. Independent whole-pack AI review accepted the previous v0.4 material for partial tier-2 draft publication on 25 October 2026; this update requires fresh review. Professional attestation remains pending.

[tax]: https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt
[rate]: https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170
[capital]: https://logir.fo/Logtingslog/164-fra-21-12-2001-um-skatting-av-kapitalvinningi-sum-seinast-broytt-vid-logtingslog-nr-173
[consumption]: https://logir.fo/Kunngerd/98-fra-14-12-1987-um-uppgerd-av-skattligu-eginnytsluni
[depreciation]: https://logir.fo/Logtingslog/52-fra-29-12-1971-um-skattligar-avskrivingar-vm-sum-seinast-broytt-vid-logtingslog-nr-174
[pension]: https://logir.fo/Logtingslog/49-fra-14-05-2013-um-eftirlonarsamansparing-og-skatt-af-eftirlon-og-rentutryggingum
[support]: https://logir.fo/Logtingslog/148-fra-30-12-1996-um-studul-til-rentuutreidslur-av-lanum-sum-seinast-broytt-vid-logtingslog
[national]: https://www.taks.fo/fo/borgari/gjoeld-og-agodar/talva-yvir-landsskatt
[municipal]: https://www.taks.fo/fo/borgari/gjoeld-og-agodar/talva-yvir-kommunuskatt-kirkjuskatt-og-barnafradratt
[child]: https://www.taks.fo/fo/borgari/fradrattur/barnafradrattur
[church]: https://logir.fo/Logtingslog/61-fra-07-06-2007-um-figgjarvidurskifti-folkakirkjunnar
[church-audit]: https://lg.fo/download/file/f3e290b4e758ae966b65955f9beb36e8c540831d.pdf
[rent]: https://www.taks.fo/fo/borgari/skattur/skattur-og-husaleiga
[returns]: https://www.taks.fo/en/individuals/tax/tax-return
[spouse]: https://www.taks.fo/fo/borgari/fradrattur/hjunafradrattur
[residence]: https://www.taks.fo/fo/log/vegleidingarskriv-vls-2015/c-subjektiv-skattskylda-likamligir-personar-tviskatting
[calculator-info]: https://www.taks.fo/fo/borgari/skattur/skattaroknarin
[calculator]: https://www.eskatt.fo/sjtp/sjtpsim.aspx

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
