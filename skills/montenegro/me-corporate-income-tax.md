---
name: me-corporate-income-tax
description: "Montenegro corporate profit tax (porez na dobit pravnih lica) for tax year 2026. Covers who pays (resident companies on worldwide profit, non-residents on profit of a Montenegrin permanent establishment), the progressive rates of 9% up to EUR 100,000, 12% up to EUR 1,500,000 and 15% above, the move from accounting profit to taxable profit, disallowed and capped costs (donations 3.5%, entertainment 1%, memberships 0.1% of revenue), salaries deductible when paid, bad debts, tax depreciation in five groups (2.5% to 30%), capital gains, five-year loss carry-forward, the new-company incentive, withholding tax at 15% (30% for listed territories), the PD return and payment three months after year end, fines, late-payment interest and limitation periods. Trigger phrases: porez na dobit, PD prijava, Montenegro corporate tax, d.o.o. tax Montenegro, amortizacija OA. Related skills: me-cross-border, me-transfer-pricing, montenegro-income-tax."
version: 0.2
category: international
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Montenegro corporate income tax, tax year 2026

This skill computes the corporate profit tax of a company for a 2026 tax period. The law is the Corporate Profit Tax Law (Zakon o porezu na dobit pravnih lica, "CPTL"), consolidated by the Ministry of Finance through amendment 88/24. No amendment was published between 88/24 and 104/26, so that text is the law for 2026. [Amendment 104/26][amend] (Official Gazette 17 July 2026) is in force but applies from 1 January 2027 (104/26 art. 19); its anti-profit-shifting chapter and anti-abuse rule apply only from Montenegro's accession to the EU (104/26 art. 17). Tax depreciation follows the Ministry depreciation rulebook (through 124/24). Interest, limitation and collection follow the Tax Administration Law (Zakon o poreskoj administraciji, "TAL"), which CPTL art. 42 applies to everything the CPTL does not regulate.

## Who this applies to

- **Taxpayers.** Every resident or non-resident legal person that carries on business for profit (CPTL art. 2).
- **Residents.** A legal person incorporated in Montenegro or with its seat of effective management and control in Montenegro (CPTL art. 3(1)). Residents are taxed on profit made in and outside Montenegro (art. 4(1)).
- **Non-residents.** A legal person not incorporated in Montenegro and without effective management there, doing business through a permanent establishment (art. 3(2)). The establishment is taxed on its own profit (art. 4(3)). A building site or assembly project is a permanent establishment only if it lasts more than six months (art. 4(4)); storage, display, delivery, purchasing, information gathering and preparatory or auxiliary activities are not (art. 4(5)). A non-resident without a permanent establishment is reached only by withholding on the income in art. 29 (art. 4(6)): see [the cross-border skill](me-cross-border.md).
- **Non-profit bodies.** State and local bodies, public funds and institutions, tourist organisations, sports clubs and federations, religious communities, artistic associations, political parties, chambers, unions and NGOs set up for non-profit work pay no profit tax on that work, but are taxpayers for any profit-making activity (art. 6). An NGO registered for business activity reduces its tax base by EUR 4,000 if it uses the profit for its statutory aims (art. 32).
- **Tax period.** The financial year, which is the calendar year, except on liquidation, a status change or a start of business during the year (art. 39).
- **Large groups.** A member of a multinational or large domestic group whose consolidated revenue was at least EUR 750 million in at least two of the four fiscal years before the reporting year is also covered by the Global Minimum Tax Law (Zakon o globalnom minimalnom porezu na dobit pravnih lica, Official Gazette 33/26, in force 10 March 2026). Where its effective tax rate in Montenegro is below 15%, it pays a domestic top-up tax, with the return and payment due within 18 months after the end of the fiscal year (arts. 2(1), 5, 30(1), 37). This skill does not compute the top-up tax.
- **Out of this skill.** Sole traders (preduzetnici) pay personal income tax: see [the income tax skill](montenegro-income-tax.md). Pricing between related parties: see [the transfer pricing skill](me-transfer-pricing.md). Withholding mechanics, treaties and foreign tax credits: see [the cross-border skill](me-cross-border.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Profit up to EUR 100,000.00 | 9% | 2026 | [CPTL art. 28(2)(1)][law] |
| Profit EUR 100,000.01 to EUR 1,500,000.00 | EUR 9,000 + 12% of the excess over EUR 100,000 | 2026 | [CPTL art. 28(2)(2)][law] |
| Profit above EUR 1,500,000.00 | EUR 177,000 + 15% of the excess over EUR 1,500,000 | 2026 | [CPTL art. 28(2)(3)][law] |
| Donations for health, social, educational, scientific, religious, cultural, sports, humanitarian, environmental and civil-society purposes | deductible up to 3.5% of total revenue | 2026 | [CPTL art. 14(1)][law] |
| Donations to national sports federations | deductible up to 5% of total revenue | 2026 | [CPTL art. 14(2)][law] |
| Entertainment (reprezentacija) | deductible up to 1% of total revenue | 2026 | [CPTL art. 15][law] |
| Membership fees to chambers and associations | deductible up to 0.1% of total revenue; fees fixed by law in full | 2026 | [CPTL art. 16][law] |
| Bad debt write-off | receivable older than 365 days, plus other conditions | 2026 | [CPTL art. 17(1)][law] |
| Bad debt impairment | at least 60 days past due at the end of the tax period | 2026 | [CPTL art. 17(4)][law] |
| Depreciable fixed asset | useful life over one year and value over EUR 300 (not land or works of art) | 2026 | [CPTL art. 13(2)][law]; [Rulebook art. 2][dep] |
| Depreciation group I (buildings and other immovables) | 2.5%, straight line, asset by asset | 2026 | [CPTL art. 13(3)-(4)][law]; [Rulebook arts. 4-5][dep] |
| Depreciation groups II / III / IV / V | 10% / 15% / 20% / 30%, declining balance on the group pool | 2026 | [CPTL art. 13(3), (5)][law]; [Rulebook arts. 4, 6][dep] |
| Small pool balance written off | closing group balance under EUR 1,000 | 2026 | [Rulebook art. 9][dep] |
| Repairs to group II to V assets | expensed up to 5% of the group balance; the excess is added to the pool | 2026 | [Rulebook art. 10][dep] |
| Business losses carried forward | no more than 5 years | 2026 | [CPTL art. 25(1)][law] |
| Capital losses carried forward | against capital gains of the next 5 years | 2026 | [CPTL art. 22(6)][law] |
| New company in an underdeveloped municipality | tax reduced by 100% for the first 8 years, total relief capped at EUR 200,000 | 2026 | [CPTL art. 31(1), (4)][law] |
| Reinvestment in agriculture | tax reduced by the amount invested, capped at EUR 300,000 over 3 years | 2026 | [CPTL art. 31d][law] |
| Tax consolidation of a group | parent controls at least 75% of each subsidiary; applies for at least 5 years | 2026 | [CPTL arts. 35(1), 37(1)][law] |
| Withholding tax on dividends to legal persons, and on interest, royalties, capital gains, rent, consulting, market research and audit fees to non-resident legal persons | 15% of the gross amount | 2026 | [CPTL art. 29(1), (4)][law] |
| Withholding tax for a non-resident from a listed low-tax territory | 30% of the gross amount | 2026 | [CPTL art. 29(5)-(7), (10)][law]; [Ministry list][list] |
| Withholding on loans to individuals (except non-related individuals up to EUR 5,000 a year) | 15% of the gross amount | 2026 | [CPTL art. 28a(1)-(2)][law] |
| Non-resident capital gains and rent not withheld by the payer | 15%, own return within 30 days | 2026 | [CPTL art. 29c][law] |
| Fines for CPTL offences | legal person EUR 1,000 to 20,000; responsible person EUR 500 to 2,000 | 2026 | [CPTL art. 42a][law] |
| Late-payment interest, 1 January to 17 July 2026 | 0.03% a day | 2026 | [TAL art. 95(1), text before 104/26][tal-old] |
| Late-payment interest, 18 July to 31 December 2026 | 5.4% a year (ECB main refinancing rate + 3 points, set each half-year) | 2026 | [TAL art. 95(1)-(5)][tal]; [104/26 TAL arts. 20, 26][tal-amend]; [Tax Administration decision of 24 July 2026][kamata] |
| Limitation periods | 5 years to assess, 5 years to collect, 10 years absolute | 2026 | [TAL arts. 100, 101, 103][tal] |

Article 28 writes the upper bands as "12% on the amount over 100,000.01" and "15% on the amount over 1,500,000.01". The fixed amounts (9,000 and 177,000) match whole-euro boundaries, so this skill computes the bands at EUR 100,000 and EUR 1,500,000; the difference is a fraction of a cent.

## The taxable base

### Step 1: start from the accounts

The base is taxable profit: profit before tax in the income statement, prepared under the accounting law or IAS/IFRS, adjusted as the CPTL requires (art. 7(1)-(2)). Revenue and expenses are taken as booked unless the CPTL says otherwise (arts. 8, 10). Effects of a change in accounting policy on first application of IAS/IFRS are recognised in equal parts over five tax periods (art. 7(4)-(5)).

### Step 2: take out exempt income

- Dividends, profit shares and liquidation distributions from another legal person are excluded if the payer is itself a taxpayer under the CPTL (art. 9). Foreign dividends are outside art. 9; they are taxed, with credit under arts. 33 to 34b.
- The accounting capital gain on land, buildings, property rights, shares and securities is removed from the base (art. 9a), and the accounting capital loss on those assets is added back (art. 18a(3)). The tax capital gain is computed separately in Step 6.

### Step 3: add back disallowed costs (art. 11)

Costs not incurred for the business; costs that cannot be documented; interest on late taxes and contributions; interest paid to non-residents above the usual commercial rate; administrative charges paid by a permanent establishment to its foreign head office; payments to employees or others out of profit distribution; fines and penalties; impairment of a receivable from a person to whom the company owes money, up to that debt; contributions to political organisations; gifts and other transfers without payment; default interest between related persons.

Impairment of assets (the difference between book value and recoverable amount) is not deductible when booked. It is deductible when the asset is sold, scrapped or damaged by force majeure (art. 18a(1)). A specific exception covers impairment of a stake in a privatised company acquired by converting a receivable (art. 18a(2)).

### Step 4: timing rules for pay

Salaries, author fees, contract-for-work fees, occasional self-employment income paid to individuals, retirement severance, redundancy and other termination payments are deductible in the period in which they are paid (art. 11a). Add back an amount booked this year and unpaid at year end; deduct a prior-year amount paid this year that was added back before.

### Step 5: capped and conditional costs

- **Materials and goods sold:** weighted average or FIFO, as in the accounts (art. 12).
- **Donations (art. 14):** only to legal persons working for the listed purposes, used exclusively for them; in cash, goods, rights or services. Cap 3.5% of total revenue, or 5% for national sports federations. Donations to research projects or innovation infrastructure that gave the company incentive-beneficiary status are not deductible (art. 14(5)).
- **Entertainment (art. 15):** up to 1% of total revenue, if spent to improve the business, documented and the recipient is not a related person.
- **Memberships (art. 16):** up to 0.1% of total revenue; fees whose amount is fixed by law are deductible in full.
- **Bad debts (art. 17):** a write-off is deductible if the receivable was earlier included in revenue, is written off in the books as uncollectable, has been sued on, put to enforcement or claimed in liquidation or bankruptcy, and is older than 365 days. The lawsuit condition is waived where court fees for suing the debtor exceed the whole receivable from that debtor. An impairment is deductible if at least 60 days have passed from the due date to the end of the period. Amounts recovered later, or claims withdrawn, are taxed when that happens; recoveries of amounts never deducted are not taxed.
- **Provisions (art. 18):** banks, insurers and brokers follow their sector rules. Provisions for renewable natural resources, warranties and lawsuits follow the accounting rules. Provisions for severance and jubilee awards are deductible up to the amounts set by the labour rules.
- **Related-party interest (arts. 19 and 20):** interest paid to a related lender is deductible only up to the arm's-length amount; interest charged to a related borrower is taxed at no less than the arm's-length amount. Each year the Ministry sets arm's-length interest rates for the following year by 31 December; the taxpayer can instead apply the general arm's-length methods (art. 38b(2)-(3)).
- **Transfer pricing adjustment:** profit must be computed at arm's length with related persons (25% or more of shares, votes or profit, actual control, or family links) (arts. 38, 38a). Add the positive difference to the base (art. 38a(4)). Method and documentation: see [the transfer pricing skill](me-transfer-pricing.md).

### Step 6: tax depreciation

Replace accounting depreciation with tax depreciation (art. 13; Rulebook). Fixed assets with a life over one year and value over EUR 300 are depreciable, except land and works of art (Rulebook art. 2). The calculation is made on form OA (Rulebook art. 3).

- **Group I (2.5%):** buildings, roads, pipelines, power plants, IT infrastructure and all other immovables (Rulebook art. 4). Straight line, asset by asset: 1/40 of cost plus improvements that exceed 5% of cost. Investment property carried at fair value uses 2.5% of cost (Rulebook art. 5).
- **Groups II to V:** for example cars, office equipment and air conditioning in group II (10%); tools, buses, trucks and other equipment not listed elsewhere in group III (15%); radio, TV and telephone equipment in group IV (20%); electronic and IT data processing equipment, rental and taxi cars, tractors and construction machinery in group V (30%) (Rulebook art. 4). Each group is one pool: opening balance plus purchases minus sales, times the group rate. The rest is the next year's opening balance (Rulebook art. 6).
- **Pool rules:** if sale proceeds in a year exceed the pool balance, the excess is taxable income and the pool goes to zero (Rulebook art. 7). If the proceeds from the sale of all assets in a group are lower than the balance, the remaining balance is deducted (Rulebook art. 8). A closing balance under EUR 1,000 is deducted in full (Rulebook art. 9). Repairs up to 5% of the group balance are an expense; above 5% they are added to the pool (Rulebook art. 10).
- **Intangibles and leases:** concessions, patents, copyrights, franchises and other rights, and right-of-use assets of a lessee, are deductible at the accounting amortisation (CPTL art. 13(6)-(7); Rulebook art. 11). Natural resources use a production-ratio method (Rulebook art. 12).

### Step 7: capital gains

Articles 21 to 24 sit in chapter V of the CPTL (the tax base), so the net capital gain is part of taxable profit and is taxed at the art. 28 rates. A capital gain is the sale price of land, buildings, property rights, shares or securities less the adjusted acquisition cost (arts. 21, 22(1)). The sale price is the market value of the consideration less selling costs (art. 23); the taxpayer must value the asset at market value on sale, and the tax authority adjusts a price below market (art. 22(3)-(4)). The acquisition cost is the book cost less tax depreciation; real estate cost is indexed by retail price growth from purchase to sale; securities bought at different prices use FIFO (art. 24). Capital losses are set off against capital gains of the same year, and the rest is carried forward against capital gains of the next five years (art. 22(5)-(6)). A transfer of assets in a merger, consolidation or division, and a distribution of share capital, is not a sale; the gain is deferred until the company formed by the status change sells the asset, if the owners received shares in it plus any cash not exceeding 10% of the nominal value of those shares (art. 26). On liquidation, assets are treated as sold at market value, except a transfer from subsidiary to parent (art. 27).

### Step 8: losses

Business losses, other than capital losses, are carried forward against profit of the following periods for no more than five years (art. 25(1)). The right survives a status change and is split in proportion to asset values, with notice to the tax authority (art. 25(2)-(3)). There is no carry-back.

### Step 9: tax, reliefs and credits

Apply the art. 28 bands to taxable profit. Then deduct reliefs and credits:

- **New company in an underdeveloped municipality (art. 31):** tax reduced by 100% for the first eight years, total capped at EUR 200,000 (including any other state aid). The company must actually operate there. Not available to companies formed by merger, split or another status change, or where a company in the same or similar activity closed in the three prior years, or where a founder is a related person, or to a company receiving state aid for firms in difficulty, or to firms in transport, shipbuilding, steel, trade or catering (except primary catering) (art. 31(6)-(10)). A branch of an existing company qualifies in proportion to its profit, with separate records. Apply within 30 days of registration in the Central Register of Business Entities (CRPS); the tax authority decides by ruling; a state-aid statement is filed with each return (art. 31a).
- **Research and innovation incentives:** exemption for holders of incentive status under the research and innovation law (art. 31c).
- **Agriculture (arts. 31d, 31e):** tax reduced by profit reinvested in agricultural projects or invested in agricultural businesses, capped at EUR 300,000 over three years; the company and the businesses invested in must be entered in the Register of Agricultural Holdings; apply within 60 days of the end of the year (reinvestment) or of the investment; not combined with art. 31.
- **Foreign tax credit (art. 33):** foreign tax paid on foreign profit, capped at the Montenegrin tax on that profit.
- **Credit for tax of a foreign subsidiary (arts. 34a, 34b):** for a holding of 10% or more for at least one year before the return; the dividend is grossed up by the foreign withholding; unused credit carries forward five years.
- **Group consolidation (arts. 35 to 37):** resident parent and subsidiaries with at least 75% control; the parent applies by 31 December of the current tax period and the tax authority decides within 30 days; losses of one member offset profits of others; each member still files its own return; the regime lasts at least five years, and leaving early repays the benefit.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Corporate tax return (Form PD with schedules PG1 and PG2) | within three months of the end of the tax period; 31 March 2027 for calendar year 2026 | [CPTL art. 40(3)][law]; [Return rulebook art. 2][return] |
| Payment of the tax shown on the return | same day as the return | [CPTL art. 40(3)][law] |
| Attachments to the return | income statement and balance sheet prepared under the accounting law | [CPTL art. 40(4)][law] |
| Filing method | electronic only, signed by the taxpayer or an authorised person, to the tax office of the main place of business | [CPTL art. 40(6)][law]; [Return rulebook art. 3][return] |
| Withholding tax | paid at the time of each payment | [CPTL arts. 28a(2), 29(4)][law] |
| Annual withholding report | by the end of February for the previous year | [CPTL arts. 28a(3), 29(11)][law] |
| Non-resident capital gain or rent return | within 30 days of earning the income, through a tax proxy | [CPTL art. 29c(3)][law] |
| New-company incentive application | within 30 days of CRPS registration | [CPTL art. 31a(1)][law] |
| Group consolidation application | by 31 December of the current tax period | [CPTL art. 35(3)][law] |
| Transfer pricing documentation | large taxpayers file it with the return; others hold it at filing and supply it within 45 days of a request; transitional date 30 June of the following year "until 2027" | [CPTL arts. 38c, 44b][law] |

There are no monthly advance payments: the article that provided for them (art. 41) is repealed. The whole tax is paid with the return.

## Penalties and interest

- **Fines (CPTL art. 42a):** EUR 1,000 to 20,000 for the company, and EUR 500 to 2,000 for the responsible person, for failing to compute the tax under the law, failing to file the return electronically within three months, failing to attach the income statement and balance sheet, failing to compute, withhold or pay withholding tax (including on loans to individuals), missing the withholding report, failing to file the state-aid statement while using a relief, and failing to file or produce transfer pricing documentation.
- **Late-payment interest (TAL art. 95):** charged daily from the day after the due date on tax unpaid or underpaid; no interest on interest. Until 17 July 2026 the rate was 0.03% a day. Amendment 104/26 to the TAL took effect on 18 July 2026 (104/26 TAL art. 26). From then the rate is the ECB main refinancing rate on the first day of the half-year plus three percentage points, set each half-year and published by the Tax Administration. For 18 July to 31 December 2026 the Tax Administration set 5.4% a year. From 18 July 2026 interest on overpaid tax uses the same rate (TAL art. 96).
- **Limitation (TAL arts. 100 to 103):** the right to assess tax expires five years after the end of the year in which it should have been assessed; the right to collect expires five years after the end of the year of assessment; any official act interrupts both. Assessment, collection and refund always expire ten years after the end of the relevant year, except that tax secured by a pledge or mortgage does not expire, other than the interest and other charges on it (TAL art. 103(3)).

## Cross-border points

- **Residents** are taxed on worldwide profit and claim credit for foreign tax under arts. 33 to 34b (see Step 9). A double tax treaty prevails over the CPTL (art. 34(1)); the tax authority issues residence certificates (art. 34(2)).
- **Withholding (art. 29):** 15% of the gross amount on dividends and profit shares paid to resident and non-resident legal persons, on liquidation distributions to legal persons, and on interest, royalties, capital gains, rent, consulting, market research and audit fees paid to non-resident legal persons. The same 15% applies to payments to resident and non-resident individuals for used products, semi-finished products and agricultural products bought from a producer who is a VAT payer, and to fees paid to non-resident legal persons for entertainment, artistic or sports performances in Montenegro (art. 29(2)-(3)). The rate is 30% where the non-resident is from a territory on the Ministry's list (lower tax and no information exchange), unless it is also resident in a treaty state (art. 29(5)-(7), (10)). A permanent establishment that pays these amounts also withholds, unless the amount is income of that establishment (art. 29(8)-(9)).
- **Treaty rates at source (art. 29a):** the payer applies the treaty only if the non-resident proves residence with a certificate from its tax authority and is the beneficial owner. If the payer applies a treaty without that proof, it pays the shortfall.
- **Interest to residents:** art. 29 withholding on interest applies only to non-resident legal persons.
- **Dividends to individuals:** not under the CPTL. A dividend paid to a resident or non-resident individual is capital income taxed at 15% of the gross amount, withheld by the company when it pays ([PIT Law arts. 37, 50][pit]); see [the income tax skill](montenegro-income-tax.md).
- **Non-resident capital gains and rent from persons who do not withhold (art. 29c):** 15%, declared by the non-resident through a tax proxy within 30 days; the tax authority assesses by ruling.
- **EU directive chapters:** the merger, interest-royalties and parent-subsidiary chapters (VIa and VIIa) apply only from EU accession (art. 45a). Until then, dividends to an EU parent bear 15% subject to the treaty.
- **Changes from 1 January 2027 (104/26):** withholding on loans to individuals falls only on the amount above EUR 5,000 a year, and that non-taxable part does not apply to related persons (104/26 art. 8); non-resident performers file their own 30-day return where no one withholds (104/26 art. 9); the domestic law or the treaty applies, whichever is more favourable (104/26 art. 11, new art. 29i); an investment in agricultural businesses is defined as acquiring shares or interests in them (104/26 art. 12), and the agricultural relief application changes to 60 days from the reinvestment or investment and no later than the end of that fiscal year (104/26 art. 13). Not part of the 2026 computation.

## Worked examples

Hypothetical figures in EUR. Each example states its own facts.

### Example 1: accounts profit to tax

A company has profit before tax of 150,000 and total revenue of 1,000,000. It booked accounting depreciation of 18,000; tax depreciation on form OA is 14,000. It booked non-business costs of 1,000 and fines of 500. Salaries of 10,000 accrued for 2026 were unpaid at year end; salaries of 4,000 accrued and added back in 2025 were paid in 2026. Qualifying donations were 50,000, entertainment 15,000 (to non-related recipients) and voluntary memberships 3,000. A transfer pricing adjustment adds 6,000. An unused 2023 business loss of 20,000 is available. No capital transactions, reliefs or credits.

Caps: donations 3.5% x 1,000,000 = 35,000, so 15,000 is added back; entertainment 1% = 10,000, add back 5,000; memberships 0.1% = 1,000, add back 2,000. Adjusted profit = 150,000 + 18,000 - 14,000 + 1,000 + 500 + 10,000 - 4,000 + 15,000 + 5,000 + 2,000 + 6,000 = 189,500. Loss used 20,000, taxable profit 169,500. Tax = 9,000 + 12% x 69,500 = 17,340, due with the return by 31 March 2027.

```oa-check
name: Montenegro ordinary accounts to progressive corporate tax
inputs:
  accounting_profit: 150000
  total_revenue: 1000000
  accounting_depreciation: 18000
  tax_depreciation: 14000
  nonbusiness_costs: 1000
  fines: 500
  current_unpaid_remuneration: 10000
  prior_added_back_remuneration_paid: 4000
  qualifying_donations_booked: 50000
  eligible_representation_booked: 15000
  voluntary_dues_booked: 3000
  transfer_pricing_addback: 6000
  eligible_loss_available: 20000
steps:
  - donation_addback: max(0, qualifying_donations_booked - total_revenue * 0.035)
  - representation_addback: max(0, eligible_representation_booked - total_revenue * 0.01)
  - dues_addback: max(0, voluntary_dues_booked - total_revenue * 0.001)
  - adjusted_profit: accounting_profit + accounting_depreciation - tax_depreciation + nonbusiness_costs + fines + current_unpaid_remuneration - prior_added_back_remuneration_paid + donation_addback + representation_addback + dues_addback + transfer_pricing_addback
  - loss_used: min(max(0, adjusted_profit), eligible_loss_available)
  - taxable_profit: max(0, adjusted_profit - loss_used)
  - first_band_tax: min(taxable_profit, 100000) * 0.09
  - second_band_tax: min(max(0, taxable_profit - 100000), 1400000) * 0.12
  - upper_band_tax: max(0, taxable_profit - 1500000) * 0.15
  - corporate_tax: round(first_band_tax + second_band_tax + upper_band_tax, 2)
expected:
  donation_addback: 15000
  representation_addback: 5000
  dues_addback: 2000
  adjusted_profit: 189500
  loss_used: 20000
  taxable_profit: 169500
  corporate_tax: 17340
```

### Example 2: building and an IT pool

A company owns a building (group I) with a depreciable cost of 400,000 for the full year, no additions or disposals. Its group V pool (IT data processing equipment) opens at 10,000; it buys equipment for 3,000 and sells equipment for 2,000; assets remain in the pool. No repairs. Accounting depreciation on these assets is 20,000.

Building: 400,000 x 2.5% = 10,000. Pool: 10,000 + 3,000 - 2,000 = 11,000; x 30% = 3,300; closing balance 7,700, above the EUR 1,000 small-balance limit, so it carries forward. Tax depreciation 13,300; the net add-back is 20,000 - 13,300 = 6,700.

```oa-check
name: Montenegro building and group V pool depreciation
inputs:
  building_tax_base: 400000
  building_rate: 0.025
  pool_opening: 10000
  pool_purchases: 3000
  pool_disposal_proceeds: 2000
  pool_rate: 0.30
  accounting_depreciation: 20000
steps:
  - building_deduction: building_tax_base * building_rate
  - pool_base: pool_opening + pool_purchases - pool_disposal_proceeds
  - pool_deduction: pool_base * pool_rate
  - pool_closing: pool_base - pool_deduction
  - total_tax_depreciation: building_deduction + pool_deduction
  - net_depreciation_addback: accounting_depreciation - total_tax_depreciation
expected:
  building_deduction: 10000
  pool_base: 11000
  pool_deduction: 3300
  pool_closing: 7700
  total_tax_depreciation: 13300
  net_depreciation_addback: 6700
```

### Example 3: an adjustment that crosses the top band

Taxable profit is 1,490,000 before a further transfer pricing adjustment of 30,000, which takes it to 1,520,000. No loss, relief or credit.

Tax before: 9,000 + 12% x 1,390,000 = 175,800. Tax after: 177,000 + 15% x 20,000 = 180,000. The extra tax is 4,200: 10,000 of the adjustment at 12% and 20,000 at 15%, not 15% on all of it.

```oa-check
name: Montenegro progressive upper band adjustment
inputs:
  taxable_profit_before: 1490000
  additional_adjustment: 30000
steps:
  - taxable_profit_after: taxable_profit_before + additional_adjustment
  - tax_before: round(min(taxable_profit_before, 100000) * 0.09 + min(max(0, taxable_profit_before - 100000), 1400000) * 0.12 + max(0, taxable_profit_before - 1500000) * 0.15, 2)
  - tax_after: round(min(taxable_profit_after, 100000) * 0.09 + min(max(0, taxable_profit_after - 100000), 1400000) * 0.12 + max(0, taxable_profit_after - 1500000) * 0.15, 2)
  - additional_tax: tax_after - tax_before
expected:
  taxable_profit_after: 1520000
  tax_before: 175800
  tax_after: 180000
  additional_tax: 4200
```

## Ask the client first

1. Where is the company incorporated and where is it actually managed? For a foreign company, what does it do in Montenegro and for how long (permanent establishment test)?
2. What is the financial year, and was there a start, merger, split or liquidation during it?
3. Who are the related persons (25% or more of shares, votes or profit, or family), and what did the company buy from, sell to or lend to them?
4. Were any salaries, author fees or severance payments for the year unpaid at year end, or prior-year amounts paid this year?
5. Did the company sell land, buildings, shares or securities, or does it carry unused business or capital losses (and from which years)?
6. Does it hold a ruling for the new-company incentive, the agricultural relief or group consolidation, and what payments did it make abroad (dividends, interest, royalties, services) with what treaty evidence?

[law]: https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0
[amend]: https://wapi.gov.me/download/8951908b-625c-4219-aefe-0c86501ddaf8?version=1.0
[dep]: https://wapi.gov.me/download/17fea3fc-8c45-434d-b0a2-9a251c3729da?version=1.0
[return]: https://wapi.gov.me/download/96c3699a-765d-4d19-b15b-e539e9e17691?version=1.0
[list]: https://wapi.gov.me/download/10ea79a6-8f36-463d-ab8c-b88ab655b61c?version=1.0
[pit]: https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0
[tal]: https://wapi.gov.me/download/8e3ee8d0-f10c-453a-90ad-6439ac07aca2?version=1.0
[tal-old]: https://wapi.gov.me/download/2dd530ac-eec4-4d0c-9d8f-0c9e7ebc5b86?version=1.0
[tal-amend]: https://wapi.gov.me/download/c22f3c59-7e52-4213-bbe4-3cd9d8d3a373?version=1.0
[kamata]: https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0

## Sources

| Source | URL | Read on |
|---|---|---|
| Corporate Profit Tax Law, Ministry of Finance consolidation through 88/24: arts. 2 to 45a (scope, base, depreciation, capital gains, losses, rates, withholding, reliefs, consolidation, transfer pricing, return, fines) | https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0 | 2026-10-30 |
| Ministry of Finance page on corporate profit tax (lists the current law and rulebooks; the linked law file is the same 88/24 consolidation) | https://www.gov.me/clanak/porez-na-dobit-pravnih-lica-2 | 2026-10-30 |
| Law amending the Corporate Profit Tax Law, Official Gazette 104/26 (17 July 2026): arts. 8, 9, 11, 12, 13, 17, 19 | https://wapi.gov.me/download/8951908b-625c-4219-aefe-0c86501ddaf8?version=1.0 | 2026-10-30 |
| Rulebook on classifying fixed assets into groups and depreciation methods, through 124/24: arts. 2 to 12 and form OA | https://wapi.gov.me/download/17fea3fc-8c45-434d-b0a2-9a251c3729da?version=1.0 | 2026-10-30 |
| Rulebook on the form and content of the corporate profit tax return, through 20/25: arts. 2 and 3 | https://wapi.gov.me/download/96c3699a-765d-4d19-b15b-e539e9e17691?version=1.0 | 2026-10-30 |
| Ministry list of territories with tax sovereignty under CPTL art. 29 | https://wapi.gov.me/download/10ea79a6-8f36-463d-ab8c-b88ab655b61c?version=1.0 | 2026-10-30 |
| Global Minimum Tax Law (Zakon o globalnom minimalnom porezu na dobit pravnih lica), Official Gazette 33/26 (published and in force 10 March 2026): arts. 2, 5, 30, 32, 37 | https://www.sluzbenilist.me/propisi/391203/download | 2026-10-30 |
| Personal Income Tax Law, consolidated text through 160/25: arts. 37, 50 (tax on dividends paid to individuals) | https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0 | 2026-10-30 |
| Tax Administration Law, Ministry consolidation through 104/26: arts. 95, 96, 100 to 103 | https://wapi.gov.me/download/8e3ee8d0-f10c-453a-90ad-6439ac07aca2?version=1.0 | 2026-10-30 |
| Tax Administration Law, Ministry consolidation published March 2026 (before 104/26): art. 95 (0.03% a day) | https://wapi.gov.me/download/2dd530ac-eec4-4d0c-9d8f-0c9e7ebc5b86?version=1.0 | 2026-10-30 |
| Law amending the Tax Administration Law, Official Gazette 104/26: arts. 20, 21, 26 (new interest rule, in force the day after publication) | https://wapi.gov.me/download/c22f3c59-7e52-4213-bbe4-3cd9d8d3a373?version=1.0 | 2026-10-30 |
| Tax Administration decision on the default interest rate for 18 July to 31 December 2026 (5.4% a year), 24 July 2026 | https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0 | 2026-10-30 |

Not yet confirmed: the field layout of Form PD, schedules PG1 and PG2 and form OA in the current e-filing system (the published rulebook does not contain the form itself), including which schedule carries the capital gain; whether the art. 44b transitional date of 30 June "until 2027" covers 2026 transfer pricing documentation prepared in 2027; the arm's-length interest rates the Ministry set for 2026 under art. 38b(2); whether Rulebook art. 8 (deduction of the remaining pool balance) applies only when every asset in the group is sold; the first fiscal year for which the Global Minimum Tax Law top-up tax is due (the law states no start date other than entry into force on 10 March 2026, and its art. 32 transition table begins with fiscal years starting in 2026).

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
