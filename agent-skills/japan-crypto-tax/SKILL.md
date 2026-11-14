---
name: japan-crypto-tax
description: "Use this skill whenever asked about Japan cryptocurrency or digital asset taxation. Trigger on phrases like \"crypto tax Japan\", \"Bitcoin Japan tax\", \"暗号資産 税金\", \"仮想通貨 税金\", \"cryptocurrency Japan\", \"crypto income Japan\", \"miscellaneous income crypto\", \"雑所得\", \"NTA crypto\", \"staking tax Japan\", \"mining tax Japan\", \"NFT tax Japan\", \"DeFi tax Japan\", \"確定申告 crypto\", \"kakutei shinkoku crypto\", \"bitFlyer tax\", \"Coincheck tax\", \"crypto-to-crypto Japan\", \"総平均法\", \"移動平均法\", or any question about the income tax, reporting, or cost basis treatment of cryptocurrency, tokens, or digital assets for Japan tax residents. Covers NTA Crypto FAQ guidance, miscellaneous income classification, aggregate taxation, cost basis methods (total average / moving average), the ¥200,000 filing threshold, and Kakutei Shinkoku reporting. ALWAYS read this skill before touching any Japan crypto work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/japan-crypto-tax"
  jurisdiction: "JP"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Japan Crypto Tax

> **General reference only.** This skill produces working papers for professional review. It has not been approved by an accountant for any particular person, entity, election or filing. Confirm the applicable facts and official forms before filing, paying or taking a position.

## Scope

2026 individual Japanese crypto-income working papers: JPY transaction reconstruction, income classification, cost pools, taxable receipts/disposals, deductions and filing handoff. The latest NTA crypto FAQ opened is dated December 2025 and is expressly a 2025-2026 filing-cycle interpretation, not a 2026 revised FAQ. Current 2026 Tax Answers supply personal rates/deductions. Corporate mark-to-market rules, crypto derivatives, token legal classification and complex DeFi contracts require separate analysis.

Quick reference: ordinary individual crypto gains are generally miscellaneous income under aggregate taxation, with a business-income exception. Total average is the no-election default; moving average requires the correct notification/election. Spending/swapping is not tax-free merely because no JPY was received. NFT income is not universally miscellaneous. NTA crypto FAQ1-1 to1-7,2-1 to2-11, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf; NTA No.1525-2, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1525-2.htm.

## Ask the client first

- Residence/non-permanent residence, arrival/departure, other income, employment/withholding and deductions.
- All exchanges/wallets, opening quantities/JPY bases, transfers, swaps, stablecoins and complete transaction timestamps.
- Crypto type, existing total/moving-average election, acquisition-year notices and any change approval.
- Mining, staking, lending, airdrops, forks, NFT/DeFi/LP activity, receipts and price evidence.
- Business activity/revenue, books retained, expenses/private-use allocation and prior returns.
- Salary statements, other non-salary income and reasons to file a return even if a narrow filing exception applies.

## The method, step by step

### Classify and reconstruct in JPY

Ordinary crypto trading gains are generally other miscellaneous income, not stock/securities separate-rate capital gains. Business classification requires the actual facts and NTA criteria: FAQ2-2 says where annual crypto transaction revenue exceeds JPY 3,000,000, retention of books/documents generally points to business income, while no books generally points to business-related miscellaneous income; profitability and other facts can still require individual judgment. Crypto used incidentally in an existing business may belong to that business income. Do not assume all organized activity qualifies or all crypto is necessarily non-business. NTA crypto FAQ2-2, Income Tax Act arts.27,35-36, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf.

Combine all wallets/exchanges by crypto type, track same-owner transfers without a fictitious sale, and reconcile opening quantity plus acquisitions less disposals to closing quantity. Express each real receipt/disposal and fee in JPY using documented transaction-time valuation; annual reports may use TTM for foreign currency. Use the principally used exchange's market price where the FAQ permits it. A stablecoin or LP token needs classification of its rights, not an assumption that every token is legally the same crypto. NTA FAQ2-7 to2-9, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf.

| Event | Treatment and conditions | Official source |
|---|---|---|
| Sale for money | Proceeds less disposal cost and qualifying expenses; timing generally delivery date with permitted contract-date election applied consistently | Income Tax Act arts.35-37; NTA FAQ1-1,2-1, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf |
| Buy goods with crypto | Crypto disposal at value of goods received, less disposed-crypto basis; acquired goods recorded separately | NTA FAQ1-2, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf |
| Crypto-for-crypto swap | Disposal of surrendered asset at value of received asset; received asset's acquisition basis recorded at that value; not 2 separate taxable gains for the same taxpayer on both legs | NTA FAQ1-3, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf |
| Mining/staking/lending reward | Receipt FMV included in income, directly related costs considered; receipt value becomes acquisition basis for later disposal | NTA FAQ1-5,1-7,2-3, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf |
| Fork with no established market/value at split | No income at split under the FAQ facts, acquisition cost JPY 0; subsequent use/sale creates income | NTA FAQ1-6, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf |
| Salary paid in crypto | Employment income and withholding analysis, not automatically miscellaneous income | NTA FAQ5-1, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf |
| Gift/low-price disposal | Donor-side deemed proceeds rules and recipient gift-tax/basis rules must both be checked; do not apply only gift tax | NTA FAQ2-10,4-1 to4-2, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf |
| Missing acquisition evidence | Reconstruct first; FAQ allows acquisition cost 5% of disposal proceeds as a fallback, rather than universally assuming zero | NTA FAQ2-7, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf |

### Compute basis correctly

Choose/evidence the method by crypto type. On first acquisition, or first acquisition of a different type, file 所得税の暗号資産の評価方法の届出書 by that year's return deadline, ordinarily 15 March of the following year. Without notice the default is total average. To change an adopted/default method, file 所得税の暗号資産の評価方法の変更承認申請書 by 15 March of the intended change year and obtain approval; absence of approval/rejection by 31 December is deemed approval. A change before ordinarily 3 years without special reason can be rejected. Sources: Income Tax Act art.48-2 and Income Tax Order arts.119-2 to119-5; NTA FAQ2-4 to2-6, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf.

Total average: unit cost = (opening carrying cost + all current-year acquisition costs) / (opening units + all current-year acquired units). Disposal cost = opening cost + purchases less closing units × that average. Where ordinary inventory movements reconcile, this equals sold units × annual average. Record acquisition fees consistently and avoid deducting them again as sale expenses.

Moving average: at each acquisition compute (remaining pre-acquisition carrying cost + new acquisition cost) / (remaining units + acquired units). Each disposal consumes its units at the then-current average and reduces carrying cost. The final average values only the closing holdings. Annual disposal cost is opening cost plus acquisition cost less closing carrying value. **Do not multiply all annual sales by the final year-end average.** Sources: NTA FAQ2-4's worked example and formula, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf. FIFO is not one of the individual evaluation methods here. Income Tax Enforcement Order art.119-2(2) excludes from these average-pool acquisitions a different cryptoasset acquired only temporarily as necessary to buy, sell or exchange the intended asset. Trace the exact linked transactions and separately establish proceeds and costs; this pool exclusion does not grant a blanket tax exemption. The ordinary swap example in NTA FAQ1-3 footnote2 expressly excludes that temporary-asset case. Sources: https://laws.e-gov.go.jp/law/340CO0000000096 and the NTA FAQ above.

Deduct sale fees and other costs to the legally allowed extent; allocate internet/phone/computer use objectively. Capital equipment can need depreciation; neither a purchase nor a software subscription is automatically wholly deductible. Do not include general living costs. Income category affects how broadly expenses are considered. NTA FAQ2-3, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf.

### Compute aggregate tax and filing need

| Taxable income after JPY 1,000 rounding down | National rate | Quick deduction | Official source |
|---|---|---|---|
| JPY 1,000-1,949,000 | 5% | JPY 0 | Income Tax Act art.89; NTA No.2260, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| JPY 1,950,000-3,299,000 | 10% | JPY 97,500 | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| JPY 3,300,000-6,949,000 | 20% | JPY 427,500 | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| JPY 6,950,000-8,999,000 | 23% | JPY 636,000 | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| JPY 9,000,000-17,999,000 | 33% | JPY 1,536,000 | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| JPY 18,000,000-39,999,000 | 40% | JPY 2,796,000 | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |
| JPY 40,000,000 and above | 45% | JPY 4,796,000 | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm |

For 2026, add reconstruction surtax 2.1% of the relevant national tax after applicable credits; do not describe a combined national/local marginal rate as the actual tax bill. The NTA page also flags the high-income minimum-tax provision, so very high-income cases require that separate computation. Local inhabitant tax has its own base, deductions and municipality rules; obtain the local assessment/rules. NTA No.2260, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm.

| Total income, resident annual 2026 return | Basic deduction under provisions effective 1 December 2026 | Official source |
|---|---|---|
| No more than JPY 4,890,000 | JPY 1,040,000 ; monetary amounts derived from Japanese 万/億 units | Income Tax Act art.86; Special Measures Act art.41-16-2; NTA No.1199, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over JPY 4,890,000 to JPY 6,550,000 | JPY 670,000 ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over JPY 6,550,000 to JPY 23,500,000 | JPY 620,000 ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over JPY 23,500,000 to JPY 24,000,000 | JPY 480,000 ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over JPY 24,000,000 to JPY 24,500,000 | JPY 320,000 ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over JPY 24,500,000 to JPY 25,000,000 | JPY 160,000 ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |
| Over JPY 25,000,000 | JPY 0 ; monetary amounts derived from Japanese 万/億 units | same, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm |

This basic deduction is determined by total income, including crypto, not by crypto income alone. Special early death/departure returns filed before 1 December 2026 use the pre-amendment timing rules and can claim correction relief after commencement. Nonresidents do not receive the resident top-ups. Do not use the old JPY 480,000 standard amount across ordinary 2026 returns. NTA No.1199, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm.

The JPY 200,000 national filing exception is narrow: for the relevant single-source fully withheld salary case, salary receipts must not exceed JPY 20,000,000 and total other income (excluding salary/retirement) must not exceed JPY 200,000, alongside the other conditions. Multiple salaries, family-company payments and other special cases need their own test. If filing for another reason, include the other taxable income even below the exception amount. Do not claim a universal crypto allowance or automatically require every self-employed person to file regardless of deductions/tax. NTA No.1900, Income Tax Act arts.120-121, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1900.htm. This national exception does not establish a municipal inhabitant-tax filing exemption.

## Boundary and exception table

| Issue | Action |
|---|---|
| Other miscellaneous crypto losses | Net legally compatible gains/losses within the category/year; a net miscellaneous loss cannot offset salary/other income or be carried forward under the ordinary crypto treatment. NTA FAQ2-11, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf |
| Genuine business classification | Apply the business-income rules and any properly established blue-return relief; do not claim its loss treatment merely by relabelling trades |
| NFT/FT with no exchangeable economic value | NTA says outside the described taxable transactions; establish rights and economic value first. No.1525-2, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1525-2.htm |
| NFT receipt | Service consideration can be business/salary/miscellaneous; accidental receipt can be occasional income; other cases generally miscellaneous. No.1525-2, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1525-2.htm |
| NFT disposal | Capital-gain category can apply where the NFT is a capital-gain asset; repeated profit-seeking disposals can be business/miscellaneous. No.1525-2, https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1525-2.htm |
| NFT creation/royalty/swaps/worthlessness | Determine the actual rights, remuneration, continuity and income category; do not apply the former blanket miscellaneous-loss rule |
| Airdrop and DeFi yield/LP entry/exit | Reconstruct receipts/rights/valuation; mining/lending FAQ does not settle every airdrop, LP-token exchange or liquidity withdrawal; unresolved contract cases are excluded below |
| Nonresident trading through Japanese exchange | Exchange location alone does not make gain Japan-source; assess PE and special residence facts. NTA FAQ1-8, https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf |

## Worked cases

Use the NTA FAQ's transaction pattern to demonstrate why the basis choice matters. Purchases: 4 BTC for JPY 1,845,000; 2 BTC for JPY 1,650,000; sell 2 BTC; then buy 0.5 BTC for JPY 542,800 and sell 3 BTC. Total sale proceeds JPY 5,295,000, closing 1.5 BTC, ignoring fees. Total average is JPY 621,200; closing cost JPY 931,800 and disposal cost JPY 3,106,000, producing JPY 2,189,000 income. These are derived from FAQ2-4, not assumed tax rates.

```oa-check
name: Total-average disposal cost and closing inventory reconcile
inputs:
  first_cost: 1845000
  second_cost: 1650000
  third_cost: 542800
  purchased_units: 6.5
  closing_units: 1.5
  proceeds: 5295000
steps:
  - total_cost: first_cost + second_cost + third_cost
  - average: total_cost / purchased_units
  - closing_cost: closing_units * average
  - disposal_cost: total_cost - closing_cost
  - income: proceeds - disposal_cost
expected:
  average: 621200
  closing_cost: 931800
  disposal_cost: 3106000
  income: 2189000
```

With a valid moving-average election, the first sale consumes 2 BTC at JPY 582,500 each. The later purchase raises the remaining pool to JPY 2,872,800 for 4.5 BTC, or JPY 638,400 each. The last sale consumes 3 BTC at that average. Annual disposal cost is JPY 3,080,200 and income JPY 2,214,800. Using the final average for all 5 BTC incorrectly gives JPY 3,192,000 cost, overstating cost by JPY 111,800. Choose the method under its lawful election, not retrospectively for the preferred result.

```oa-check
name: Moving-average sales use the cost pool at each disposal
inputs:
  first_cost: 1845000
  second_cost: 1650000
  third_cost: 542800
  proceeds: 5295000
steps:
  - first_average: (first_cost + second_cost) / 6
  - first_sale_cost: first_average * 2
  - remaining_cost: first_cost + second_cost - first_sale_cost
  - second_average: (remaining_cost + third_cost) / 4.5
  - second_sale_cost: second_average * 3
  - disposal_cost: first_sale_cost + second_sale_cost
  - income: proceeds - disposal_cost
  - wrong_cost: second_average * 5
  - wrong_overstatement: wrong_cost - disposal_cost
expected:
  first_average: 582500
  second_average: 638400
  disposal_cost: 3080200
  income: 2214800
  wrong_overstatement: 111800
```

Historical 2025 fixture retained for continuity, not as a current tax assessment: the old total-average example has salary receipts JPY 6,000,000, opening 0.5 BTC on January 1 with JPY 2,000,000 cost, a March 15 purchase of 1 BTC for JPY 8,000,000, a June 20 purchase of 0.5 BTC with stated cost JPY 9,000,000, and an October 10 sale of 1 BTC for JPY 12,000,000 plus JPY 30,000 sale fees. On those stated aggregate costs, 2 BTC cost JPY 19,000,000, average JPY 9,500,000, disposal income JPY 2,470,000 and closing 1 BTC cost JPY 9,500,000, all derived. The old JPY 8,470,000 salary-plus-crypto total combined gross salary receipts with net crypto income and is not taxable total income; salary deductions and actual filing conditions remain necessary. The old mining fixture was 0.05 BTC received during 2025, value JPY 500,000, electricity JPY 80,000 and a JPY 300,000 computer with assumed 30% crypto use over an assumed 4-year life. Its arithmetic JPY 300,000 / 4 × 30% = JPY 22,500 is preserved only as a hypothetical depreciation input: actual useful life, method, in-service period and business use were not established by that fixture and must be evidenced before deduction.

A swap retains the earlier example's logic: surrendering 2 ETH with JPY 600,000 basis for 0.1 BTC worth JPY 1,000,000 gives ETH gain JPY 400,000 and BTC acquisition cost JPY 1,000,000. A mining receipt valued JPY 500,000 with evidenced electricity JPY 80,000 and permitted depreciation JPY 22,500 yields JPY 397,500 net receipt income; the JPY 500,000 receipt valuation is the acquired-token basis. Depreciation permission must be established separately.

## When to refuse or refer

Never apply stock separate rates or FIFO by analogy, ignore swaps, carry ordinary miscellaneous losses into salary or future years, treat own-wallet transfers as sales, or ignore the evaluation notification/change approval. Never label all NFTs miscellaneous. Missing opening holdings, cost evidence, valuation, token rights or residence facts must be resolved or referred. Do not recommend loss crystallisation as a universally lawful wash-sale strategy merely because no specific rule was identified. Outputs are estimates for professional review.

## Filing and payment

Use the NTA 暗号資産の計算書 appropriate to the lawful method, reconcile annual reports from bitFlyer, Coincheck, GMO Coin and any overseas exchanges to wallets, and carry the correct category to 確定申告 (Kakutei Shinkoku) through the current e-Tax return-creation flow or paper form. Enter other income, deductions and credits; preserve calculation sheets, method notices and accepted-return receipt. Ordinary statutory return timing is 16 February to 15 March of the following year, adjusted for weekends/holidays and special rules; confirm the actual 2026-income filing/payment calendar before issuing a dated instruction. The 2025-2026 filing cycle's ordinary final day was 16 March 2026, not Sunday 15 March. Bank-debit and local instalment dates require their own current notices.

## Completion checklist

All wallets reconciled; JPY values supported; business/miscellaneous/NFT categories tested; method and notices established; basis and fees not double-counted; mining/staking/lending receipts included; loss boundaries applied; total-income deductions and filing exception checked; municipal filing and actual payment dates tracked.

## Sources

| Source | URL | Read on |
|---|---|---|
| NTA crypto FAQ, December2025; Read for 2025-2026 filing cycle: questions1-1 to1-8,2-1 to2-11,4-1 to4-2,5-1; operative methods/elections, adjacent exceptions and examples | https://www.nta.go.jp/publication/pamph/pdf/virtual_currency_faq_03.pdf | 2026-11-14 |
| NTA No.2260; Read for 2026 tax table, rounding, surtax and high-income caveat | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2260.htm | 2026-11-14 |
| NTA No.1199; Read for 2026 column, resident additions, taper and early death/departure exception | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1199.htm | 2026-11-14 |
| NTA No.1525-2; Read for economic-value scope and all receipt/disposal income-category distinctions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1525-2.htm | 2026-11-14 |
| NTA No.1900; Read for salary filing conditions, multiple salaries and exceptions | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/1900.htm | 2026-11-14 |

Not yet confirmed: 2026 revised crypto FAQ and enacted commencement of any future separate-tax regime; uniform local 10%/combined 15%-55% table; airdrop-on-claim timing and no-value receipt outside FAQ fork facts; automatic LP-token deposit/withdrawal disposal and all DeFi contracts; absence of every anti-avoidance/wash-sale provision; generic gift JPY 1,100,000/rate schedule, business loss carry-forward/carry-back conditions; universal exchange transaction-reporting/suspicious-report claims, dedicated audit-team claim and generic 15%-20% underreporting penalties; exact 2026-income return/bank-debit dates and local June/four-instalment schedule. These legacy topics are excluded from usable guidance until official confirmation. The old zero-basis default, final-average-times-all-sales formula and blanket NFT classification are corrected above. The old total-average illustration (opening 0.5 BTC cost JPY 2,000,000, acquisitions costing JPY 17,000,000, sale JPY 12,000,000, fee JPY 30,000) still arithmetically gives JPY 2,470,000 crypto income, but its aggregation of JPY 6,000,000 gross salary as taxable salary income was not a complete tax calculation; use the salary-income deduction and current personal deductions before tax.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `japan-crypto-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/japan-crypto-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
