---
name: bulgaria-income-tax
description: "Bulgarian personal income tax (данък върху доходите на физическите лица) for tax year 2026 under the Personal Income Taxes Act (ZDDFL), in euro after the 1 January 2026 changeover. Covers residence (art. 4), the income categories (art. 10), the flat 10% rate on the general annual base (art. 48(1)), the statutory expense deductions for freelancers and other business income (25%, 40%, 60%; art. 29), rent (10%), gains, the 15% tax on sole traders (ET) taxed on their corporate-tax profit (arts. 26, 28, 48(2)), the 5% final tax on dividends (arts. 38, 46(3)), quarterly advance tax, the reliefs (children, disabled children, young families, donations, voluntary insurance, home repairs, cashless payments), the art. 50 annual return due 30 April (30 June for sole traders), the 5% early e-filing discount and the ZDDFL fines. Trigger on: Bulgaria income tax, ДДФЛ, ГДД, годишна данъчна декларация, чл. 50, freelancer Bulgaria 25%, ЕТ 15%, данъчно облекчение за деца. Out of scope: social contributions (bulgaria-social-contributions), employer payroll (bulgaria-payroll), non-residents and treaties (bg-cross-border), companies (bg-corporate-income-tax)."
version: 0.2
jurisdiction: BG
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bulgaria: personal income tax (ДДФЛ), tax year 2026

Source-cited draft: not reviewed by an accountant, not for filing.

Personal income tax is set by the Personal Income Taxes Act (Закон за данъците върху доходите на физическите лица, ZDDFL). Article numbers below refer to the lex.bg consolidated text, amended to State Gazette 85/2026. The tax year is the calendar year (art. 15). The National Revenue Agency (NRA, НАП) administers the tax.

Bulgaria adopted the euro on 1 January 2026. Some ZDDFL amounts still read in leva (fines, the disability relief, the loan-reporting thresholds, the young-family loan cap). Under the Euro Introduction Act those amounts are read as euro at the fixed rate of BGN 1.95583, divided without rounding the rate and then rounded to the cent (Euro Act arts. 11(2), 12 and 13). Where this skill shows a euro figure for a leva amount, it is that converted figure. The child relief amounts for 2026 are published in euro by the NRA.

Related skills in this pack: social contributions in [bulgaria-social-contributions](bulgaria-social-contributions.md), employer withholding in [bulgaria-payroll](bulgaria-payroll.md), non-residents, treaties and the foreign tax credit in [bg-cross-border](bg-cross-border.md), companies in [bg-corporate-income-tax](bg-corporate-income-tax.md). The pack also holds [bulgaria-tax-optimization](bulgaria-tax-optimization.md) and [bg-tax-overview](bg-tax-overview.md); both still carry 2025 material and overlap in part with this skill.

## Who this applies to

- **Residents (art. 4).** An individual of any citizenship is resident if any one test is met: a permanent address in Bulgaria; presence in Bulgaria for more than 183 days in any 12-month period; being sent abroad by the Bulgarian state, its bodies or Bulgarian enterprises (with family members); or a centre of vital interests in Bulgaria. Under the 183-day test the person is resident for the year in which presence exceeds 183 days; the days of leaving and arriving each count; days spent only for study or medical treatment do not count (art. 4(2), (3)). A person with a permanent address whose centre of vital interests is not in Bulgaria is not resident (art. 4(5)).
- **Residents are taxed on worldwide income (art. 6); non-residents only on Bulgarian-source income (art. 7).** Non-resident rules, final withholding at 10% and treaty relief are in [bg-cross-border](bg-cross-border.md).
- **Income categories (art. 10(1)).** (1) employment; (2) business income as a sole trader (едноличен търговец, ET); (3) other business income (freelancers, liberal professions, non-employment contracts, registered farmers); (4) rent and other paid use of rights or property; (5) transfer of rights or property (gains); (6) other income under art. 35, alternative tax and final taxes.
- **Two regimes for business income.** A sole trader registered as ET, any individual who is a trader under the Commerce Act, and a registered farmer who opts in under art. 29a are taxed at 15% on their corporate-tax profit (arts. 26, 28, 48(2)). Every other self-employed individual is taxed at 10% on income less a fixed statutory deduction (arts. 29, 30, 48(1)).
- **Foreign-currency income** is converted to euro at the BNB reference rate on the day the income is received (art. 10(3), as amended for 2026).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Tax on the general annual base (employment, other business income, rent, gains, other income) | 10% flat, no tax-free band | 2026 | https://lex.bg/laws/ldoc/2135538631 (ZDDFL art. 48(1)) |
| Sole trader (ET), trader individual, art. 29a farmer: tax on the art. 28 base | 15% | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 48(2)) |
| Dividends and liquidation shares (Bulgarian or foreign source), final tax | 5% | 2026 | https://lex.bg/laws/ldoc/2135538631 (arts. 38(1), 46(3)) |
| Statutory deduction: registered farmers, unprocessed farm produce | 60% of income | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 29(1)(1)) |
| Statutory deduction: farming, forestry, hunting and fishing produce; author and licence fees; performing artists; crafts not under patent tax; lawyers and notaries | 40% of income | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 29(1)(2)) |
| Statutory deduction: other liberal professions and non-employment contracts (граждански договори) | 25% of income | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 29(1)(3)) |
| Statutory deduction: rent and paid use of property or rights | 10% of income | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 31(1)) |
| Statutory deduction: gain on real estate; net gain on shares, financial assets, crypto-assets and non-euro currency | 10% of the gain | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 33(1), (3)) |
| Child relief (art. 22v), reduction of the annual base | one child EUR 3,067.75; two EUR 6,135.50; three or more EUR 9,203.25 | 2026 | https://nra.bg/wps/portal/nra/taxes/danak-vurhu-dohodite-na-fizicheski-lica/danuchni-oblekchenia-za-deca/danuchni_oblekchenia_za-deca |
| Disabled child relief (art. 22g), 50% or more disability | EUR 6,135.50 per child | 2026 | same NRA page |
| Child reliefs used during the year (monthly from the employer, or against Q1 to Q3 advance tax on other business income and rent) | per month: one child EUR 255.65; two EUR 511.29; three or more EUR 766.94; disabled child EUR 511.29 | 2026 | same NRA page |
| Relief for own reduced working capacity of 50% or more | BGN 7,920 = EUR 4,049.43 | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 18(1)) |
| Young families: mortgage interest | interest on the first BGN 100,000 = EUR 51,129.19 of principal | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 22a(2)) |
| Voluntary pension; voluntary health insurance and life insurance | each group up to 10% of the annual bases | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 19(1)) |
| Donations | 5%, 15% (culture) or 50% (named health funds) of the annual bases; total cap 65% | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 22(1), (2)) |
| Home repair labour relief | up to BGN 2,000 = EUR 1,022.58 | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 22e(1)) |
| Cashless payments relief | 1% of the tax on the general base, max BGN 500 = EUR 255.65 | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 22d(2)) |
| Early e-filing discount | 5% of the balance due, max BGN 500 = EUR 255.65 | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 53(6)) |
| Rounding of the annual tax | to the whole euro | 2026 | https://lex.bg/laws/ldoc/2135538631 (art. 48(8)) |
| Leva to euro conversion | BGN 1.95583 = EUR 1, rounded to the cent | 2026 | https://lex.bg/bg/laws/ldoc/2137244903 (Euro Act arts. 11 to 13) |

## The taxable base

**General annual base (art. 17).** Each income category gets its own annual base. The general annual base is the sum of the bases under arts. 25 (employment), 30 (other business income), 32 (rent), 34 (gains) and 36 (other income), less the reliefs. The 10% rate applies to that total.

- **Employment (arts. 24, 25).** Gross pay and benefits, less the employee's own mandatory social and health contributions (Bulgarian or foreign). The employer withholds monthly and makes the year-end recalculation by 31 January (art. 49); see [bulgaria-payroll](bulgaria-payroll.md).
- **Other business income (arts. 29, 30).** Income received in the year less the statutory deduction (25%, 40% or 60%, from the rate table). Actual expenses are not deducted. Then subtract the contributions the self-insured person must pay for the year for their own account (or the contributions withheld, if not self-insured) and mandatory contributions paid abroad (art. 30, items 1 and 2). Contribution rates and insurable-income limits are in [bulgaria-social-contributions](bulgaria-social-contributions.md).
- **Rent (arts. 31, 32).** Income less 10%. Leasing instalments without transfer of ownership count as rent (art. 31(2)).
- **Gains (art. 33).** Real estate: sale price less documented cost, less 10%. Vehicles, art and collectibles: sale price less cost. Shares, other financial assets, crypto-assets and trading in currencies other than the euro: the year's realised gains less the year's realised losses, deal by deal, less 10% (art. 33(3), (4)). Exempt (art. 13(1)(1)): one residential property held more than three years, or up to two properties (and any number of farm and forest plots) held more than five years, subject to the other conditions of art. 13.
- **Sole traders (arts. 26, 28).** The taxable income is the tax profit under the Corporate Income Tax Act, with its loss carry-forward (art. 26(3)). From it subtract the self-insured contributions due for the year and mandatory contributions paid abroad (art. 28(1)). Then subtract reliefs not already used against the general base: voluntary insurance, disability, art. 20 contributions, and the unused part of the child and disabled-child reliefs (art. 28(2)). The 15% rate applies to what is left.

**Reliefs.** Disability (art. 18), voluntary insurance (art. 19), art. 20 pension-service contributions, children (art. 22v) and disabled children (art. 22g) come off the general annual bases first, then off the sole-trader base (art. 21). Conditions that change the answer:

- **Children (art. 22v).** The child is under 18 (the relief applies in the year of birth and in the year the child turns 18), resident in the EU or EEA at 31 December, and not in full state residential care. Only one parent claims; the part one parent cannot use against their own bases may be claimed by the other on the annual return; if both claim in full, each owes tax on the relief used (art. 22v(4), (9)). The claimant must have no public debts subject to enforced collection (NRA page).
- **Disabled children (art. 22g).** EUR 6,135.50 for each child with 50% or more disability under a decision in force; the child is under 18 on 1 January of the year (art. 22g(2)(2)). It can be claimed alongside the ordinary child relief (NRA page).
- **Child reliefs during 2026.** An employee may have the monthly amounts in the rate table taken off the monthly tax base by the main employer, on a one-time written declaration. A freelancer or landlord who pays their own advance tax may take the same monthly amounts off the advance tax for the first three quarters, but not where the payer withholds the advance tax or the reliefs were already used through an employer. Sole traders and trader individuals cannot use them in advance (NRA page). The year-end calculation under art. 49 or the annual return still applies.
- **Young families (art. 22a).** Interest paid in the year on a mortgage to buy the family's only home; married couple; at least one spouse under 35 when the loan was signed; only one spouse claims.
- **Donations (art. 22).** 5% for donations to the health, social, educational, religious, public-benefit and other bodies listed in art. 22(1)(1); 15% for culture; 50% for the named child-treatment and assisted-reproduction funds; all donations together capped at 65% of the bases. Donations to similar EU or EEA bodies qualify (art. 22(5)).
- **Home repairs (art. 22e).** Labour (not materials) for improving or repairing one Bulgarian home the taxpayer owns, done by an EU or EEA resident who is not a related person, with a document and proof of payment.
- **Cashless payments (art. 22d).** All cash income in the general base received by bank, and cashless spending of at least 80% of that income: 1% of the tax, capped at EUR 255.65.

**Final taxes outside the annual base.** Dividends and liquidation shares carry a 5% final tax on the gross amount (arts. 38(1), (2), 46(3)). A Bulgarian company withholds it by the end of the month after the quarter in which the dividend was voted (art. 65(2)). For foreign dividends the resident pays the 5% by 30 April of the next year and declares it on the annual return (arts. 50(1)(3), 67(4)).

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Annual return (ГДД, art. 50), individuals | 10 January to 30 April 2027 for 2026 income | ZDDFL art. 53(1) |
| Annual return, sole traders, trader individuals, art. 29a farmers (with the annual activity report) | 1 March to 30 June 2027 | arts. 51(1), 53(1) |
| Balance of tax on the general base | 30 April 2027 | art. 67(5) |
| Balance of the 15% sole-trader tax | 30 June 2027 | art. 67(5) |
| Early e-filing discount | file electronically and pay by 31 March 2027; no debts under enforcement | art. 53(6) |
| One-time correction of the return | by 30 September 2027 | art. 53(2) |
| Advance tax on other business income and rent, where the payer is not a company or self-insured person (or the recipient declared self-insured status to the payer) | own payment by the end of the month after each quarter; none for the fourth quarter | arts. 43(6), 44, 67(1), (2) |
| Advance tax withheld by a company payer (10% on income less the statutory deduction) | payer pays by the end of the month after the quarter; no withholding in Q4 unless the recipient asks | arts. 43(4), 65(12), (13) |
| Sole trader advance tax | 15%, under the Corporate Income Tax Act instalment rules | art. 43(8) |
| Child relief through the employer | declaration to the main employer 30 November to 31 December 2026; employer recalculates and refunds by 31 January 2027 | art. 49(4) to (6); NRA child relief page |

**Who must file.** Every resident with income taxed on the general base or the sole-trader base (art. 50(1)(1)), income under the local patent tax or taxi tax (art. 50(1)(2)), foreign dividends (art. 50(1)(3)), foreign shareholdings and property (art. 50(1)(4)), and private loans over BGN 10,000 = EUR 5,112.92 in the year or BGN 40,000 = EUR 20,451.68 of outstanding balances (art. 50(1)(5)). No return is needed for employment income only where the main employer made the year-end recalculation and withheld the full tax, or for only exempt income or Bulgarian dividends (art. 52). Reliefs not given through the employer are claimed only on the return (art. 23). Self-insured persons file electronically only (art. 53(7)). The return goes to the NRA territorial office of the permanent address (art. 54).

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Return not filed on time | fine up to BGN 500 = EUR 255.65; repeat up to BGN 1,000 = EUR 511.29 | ZDDFL art. 80(1), (3) |
| Data left out or wrong, so the tax is lower | fine up to BGN 1,000 = EUR 511.29; repeat up to BGN 2,000 = EUR 1,022.58 | art. 80(2), (3) |
| Loans under art. 50(1)(5) not declared or wrongly declared | 10% of the undeclared amount; repeat 15% | art. 80a |
| Self-employed person fails to issue a document for income received | BGN 100 to 500 = EUR 51.13 to 255.65 per document; repeat BGN 200 to 1,000 = EUR 102.26 to 511.29 | art. 80b |
| Payer fails to withhold or pay tax on time | up to BGN 1,000 = EUR 511.29; repeat up to BGN 2,000 = EUR 1,022.58 | art. 81 |
| Sole trader fails to file the annual activity report | up to BGN 500 = EUR 255.65; repeat up to BGN 1,000 = EUR 511.29 | art. 83 |
| Late payment of tax | statutory interest (законна лихва) from the due date | Law on Interest on Taxes, Fees and Other Similar State Receivables, art. 1, https://lex.bg/laws/ldoc/2123675140 |
| Relief claimed by both parents or both spouses | each owes the tax on the relief they used | arts. 22a(6), 22v(9), 22g(8) |

Euro figures are the leva amounts in the statute converted at BGN 1.95583 and rounded to the cent (Euro Act arts. 12, 13).

## Cross-border points

- **Foreign income of residents.** Declared on the annual return with proof of foreign tax and contributions (art. 50(5)). Foreign tax is credited per country and per type of income, capped at the Bulgarian tax on that income (art. 76); where a treaty uses exemption with progression no proof of tax is needed (art. 50(6)). Details in [bg-cross-border](bg-cross-border.md).
- **Foreign contributions.** Mandatory social contributions paid abroad for the person's own account reduce the employment, business and sole-trader bases (arts. 25(1), 28(1), 30).
- **EU and EEA residents.** The child, disabled-child and young-family reliefs are also open to non-residents established for tax purposes in an EU or EEA state (arts. 22v(1), 22g(1), 22a(5)). An EU or EEA resident with Bulgarian income may elect to be taxed through the annual return as a resident would (art. 37a; see bg-cross-border).
- **Arriving or leaving.** Residence is tested per year under art. 4. The ZDDFL has no split-year rule and no exit tax on individuals.
- **Foreign dividends.** 5% final tax payable by 30 April of the next year, less any foreign tax credit (arts. 38(1)(2)(b), 67(4)).

## Worked examples

### Example 1: freelancer on the 25% deduction, one child

Maria is resident in Bulgaria and works as an IT consultant under service contracts, outside any trade register. In 2026 she receives EUR 48,000 from foreign clients, so no Bulgarian payer withholds tax. She is self-insured, active all year, without the optional illness and maternity cover. Her taxable income of EUR 36,000 is above the 2026 annual maximum insurable income of EUR 26,281.48, so the contributions due for her own account are 27.8% of EUR 26,281.48, which is EUR 7,306.25 (rates and limits from [bulgaria-social-contributions](bulgaria-social-contributions.md)). She has one child aged 6, and her husband does not claim the child relief. During the year she paid EUR 2,100 of quarterly advance tax.

Her taxable income is EUR 48,000 less 25%, so EUR 36,000. Less contributions of EUR 7,306.25 gives an annual base of EUR 28,693.75. The child relief of EUR 3,067.75 brings it to EUR 25,626.00. Tax at 10% is EUR 2,562.60. After the EUR 2,100 of advances the balance is EUR 462.60, rounded to EUR 463 under art. 48(8). She files by 30 April 2027. If she files electronically and pays by 31 March 2027, the 5% discount under art. 53(6) also applies; that variation is not computed here.

```oa-check
name: BG freelancer 25% deduction, one child, 2026
inputs:
  gross_income: 48000
  max_insurable: 26281.48
  contribution_rate: 27.8
  child_relief: 3067.75
  advances_paid: 2100
steps:
  - taxable_income: gross_income - gross_income * 25 / 100
  - contributions: round(max_insurable * contribution_rate / 100, 2)
  - annual_base: taxable_income - contributions
  - base_after_relief: annual_base - child_relief
  - tax: base_after_relief * 10 / 100
  - balance: tax - advances_paid
  - balance_rounded: round(balance)
expected:
  taxable_income: 36000.00
  contributions: 7306.25
  annual_base: 28693.75
  base_after_relief: 25626.00
  tax: 2562.60
  balance_rounded: 463.00
```

### Example 2: sole trader at 15%, child relief carried to the ET base, early e-filing

Georgi runs a sole trader business (ET) and has no other income. His 2026 tax profit under the Corporate Income Tax Act is EUR 60,000. He is self-insured all year with the optional illness and maternity cover, and his profit is above the 2026 annual maximum insurable income of EUR 26,281.48, so his contributions due for 2026 are 31.3% of EUR 26,281.48, which is EUR 8,226.10 (from [bulgaria-social-contributions](bulgaria-social-contributions.md)). He has one child aged 10, and his wife does not claim. He paid EUR 6,000 of 15% advance instalments. He files electronically on 20 March 2027, pays the same day, and has no debts under enforcement.

The edge case: Georgi has no income in the general base, so the child relief cannot be used there. Art. 28(2)(4) lets him take the unused relief off the sole-trader base. The base is EUR 60,000 less EUR 8,226.10 contributions, so EUR 51,773.90, less EUR 3,067.75, so EUR 48,706.15. Tax at 15% is EUR 7,305.92 (EUR 7,305.9225 unrounded). After EUR 6,000 of advances the balance is EUR 1,305.92. The 5% discount is EUR 65.30, below the EUR 255.65 cap. He pays EUR 1,240.62, rounded to EUR 1,241 (art. 48(8)). Had he filed between 1 April and 30 June 2027, the full EUR 1,306 would be due by 30 June.

```oa-check
name: BG sole trader 15%, unused child relief, early e-filing discount, 2026
inputs:
  tax_profit: 60000
  max_insurable: 26281.48
  contribution_rate: 31.3
  child_relief: 3067.75
  advances_paid: 6000
  discount_cap: 255.65
steps:
  - contributions: round(max_insurable * contribution_rate / 100, 2)
  - base: tax_profit - contributions - child_relief
  - tax: base * 15 / 100
  - balance: tax - advances_paid
  - discount: min(round(balance * 5 / 100, 2), discount_cap)
  - payable: round(balance - discount)
expected:
  contributions: 8226.10
  base: 48706.15
  tax: 7305.9225
  discount: 65.30
  payable: 1241.00
```

## Ask the client first

1. Is the client resident in Bulgaria for 2026 (permanent address, days present, centre of vital interests), and resident anywhere else?
2. How is the business run: ET or registered trader (15% on profit), freelancer or contract income (10% after a 25% or 40% deduction), or registered farmer?
3. Who pays the income: a Bulgarian company or self-insured person that withholds advance tax, or foreign or private payers?
4. What contributions are due for the year as self-insured, and were mandatory contributions paid abroad?
5. Children under 18, disability decisions, a young-family mortgage, donations: and does the other parent or spouse claim any relief?
6. Any foreign income, foreign dividends, foreign shareholdings or private loans to report?

## Sources

| Source | URL | Read on |
|---|---|---|
| Personal Income Taxes Act (ZDDFL), consolidated to ДВ бр. 85/2026, arts. 4, 6, 7, 10, 13, 15, 17 to 23, 24 to 36, 38, 42 to 46, 48 to 54, 65, 67, 80 to 83 | https://lex.bg/laws/ldoc/2135538631 | 2026-10-23 |
| NRA, child and disabled child reliefs for 2026, including monthly and quarterly use during the year | https://nra.bg/wps/portal/nra/taxes/danak-vurhu-dohodite-na-fizicheski-lica/danuchni-oblekchenia-za-deca/danuchni_oblekchenia_za-deca | 2026-10-24 |
| Euro Introduction Act, consolidated, arts. 11, 12, 13 | https://lex.bg/bg/laws/ldoc/2137244903 | 2026-10-24 |
| Law on Interest on Taxes, Fees and Other Similar State Receivables, art. 1 | https://lex.bg/laws/ldoc/2123675140 | 2026-10-24 |

Not yet confirmed: the gazette text of the 2026 State Budget Act provision that sets the child reliefs and their monthly use in euro (the amounts above come from the NRA page; the ZDDFL itself still reads BGN 200, 400 and 600 and BGN 2,000; the Act was not reachable on dv.parliament.bg or lex.bg on 2026-10-24); the statutory interest rate on late tax after the euro changeover; whether DOPK fines can apply alongside the ZDDFL fines; the full conditions of the art. 13(1)(1) home-sale exemption; and any rate changes the Ministry of Finance has proposed for later years.

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
